
class ClientJournal:
    '''
    The class for working with app subscriptions
    '''

    def __init__(self):
        '''
        constructor
        '''
        self.clients = []

    def display_clients(self)->None:
        '''
        This method prints all clients
        '''
        count = 1
        for client in self.clients:
            print(
                f"{count}.{client['name']},{client['surname']},{client['purchase_date']},{client['end_date']},{client['subscription_duration']}\n ")
            count+=1

    def change_name(self, old_name: str, old_surname: str, new_name: str, new_surname: str) -> None:
        '''
        This method finds a person by first and last name and changes them to new ones
        '''
        for client in self.clients:
            if client['name'] == old_name and client['surname'] == old_surname:
                client['name'] = new_name
                client['surname'] = new_surname

    def change_subscription_duration(self, name: str, surname: str, new_duration: int) -> None:
        '''
        This method finds a person by first and last name and changes the duration of the subscription to the application
        '''
        for client in self.clients:
            if client['name'] == name and client['surname'] == surname:
                client['subscription_duration'] = new_duration

    def check_client_existence(self, name: str, surname: str) -> bool:
        '''
        This method checks if the client exists by first name and surname
        '''
        for client in self.clients:
            if client['name'] == name and client['surname'] == surname:
                return True
        return False

    def add_client(self, name: str, surname: str, purchase_date: str, end_date: str, duration: int) -> None:
        '''
        This method adds a new user to the client list
        '''
        self.clients.append(
            {
                'name': name,
                'surname': surname,
                'purchase_date': purchase_date,
                'end_date': end_date,
                'subscription_duration': duration
            }
        )

    def remove_client(self, name: str, surname: str) -> None:
        '''
        This method removes the user from the list
        '''
        for client in self.clients:
            if client['name'] == name and client['surname'] == surname:
                self.clients.remove(client)

    def sort_clients_by_name(self) -> None:
        '''
        This method sorts all users by name
        '''
        self.clients.sort(key=lambda x: x['name'])

    def sort_clients_by_subscription_duration(self) -> None:
        '''
        This method sorts all users by name subscription duration
        '''
        self.clients.sort(key=lambda x: x['subscription_duration'])

    def read_from_file(self, file_name: str) -> None:
        '''
        This method allows you to append into the list all users from a file
        '''
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                self.add_client(data[0], data[1], data[2],
                                data[3], int(data[4]))

    def write_to_file(self, file_name: str) -> None:
        '''
        This method allows you to read all users from a file
        '''
        with open(file_name, 'w') as file:
            for client in self.clients:
                file.write(
                    f"{client['name']},{client['surname']},{client['purchase_date']},{client['end_date']},{client['subscription_duration']}\n")


if __name__ == "__main__":
        try:
            journal = ClientJournal()
            journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
            journal.add_client("Emily", "Johnson", "2022-02-15", "2023-02-15", 12)
            journal.add_client("Michael", "Williams", "2021-11-20", "2022-03-20", 4)
            journal.add_client("Sarah", "Brown", "2022-03-10", "2022-05-10", 2)
            journal.add_client("David", "Jones", "2022-04-05", "2022-10-05", 6)
            journal.read_from_file("clients.txt")
            journal.sort_clients_by_name()
            journal.write_to_file("sorted_clients.txt")

            # Additional work with the ClientJournal class
            journal.display_clients()
            journal.remove_client("John", "Doe")
            journal.display_clients()
        except Exception as e:
            print(f"Error: {e}")