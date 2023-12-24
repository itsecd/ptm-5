class CarServiceList:
    '''
    The class for working with app durations
    '''

    def __init__(self):
        '''
        constructor
        '''
        self.cars = []

    def display_cars(self)->None:
        '''
        This method prints all cars
        '''
        count = 1
        for car in self.cars:
            print(
                f"{count}.{car['brand']},{car['model']},{car['mileage_last_checkup']},{car['mileage_current_checkup']},{car['duration']}\n ")
            count+=1

    def change_car(self, old_brand: str, old_model: str, new_brand: str, new_model: str) -> None:
        '''
        This method finds a person by first and last brand and changes them to new ones
        '''
        for car in self.cars:
            if car['brand'] == old_brand and car['model'] == old_model:
                car['brand'] = new_brand
                car['model'] = new_model
                return True
        return False

    def change_duration(self, brand: str, model: str, new_duration: int) -> None:
        '''
        This method finds a person by first and last brand and changes the duration between checkups to the application
        '''
        for car in self.cars:
            if car['brand'] == brand and car['model'] == model:
                car['duration'] = new_duration
                return True
        return False


    def check_car_existence(self, brand: str, model: str) -> bool:
        '''
        This method checks if the car exists by first brand and model
        '''
        for car in self.cars:
            if car['brand'] == brand and car['model'] == model:
                return True
        return False

    def add_car(self, brand: str, model: str, mileage_last_checkup: str, mileage_current_checkup: str, duration: int) -> None:
        '''
        This method adds a new user to the car list
        '''
        self.cars.append(
            {
                'brand': brand,
                'model': model,
                'mileage_last_checkup': mileage_last_checkup,
                'mileage_current_checkup': mileage_current_checkup,
                'duration': duration
            }
        )

    def remove_car(self, brand: str, model: str) -> None:
        '''
        This method removes the user from the list
        '''
        for car in self.cars:
            if car['brand'] == brand and car['model'] == model:
                self.cars.remove(car)
                return True
        return False

    def sort_cars_by_brand(self) -> None:
        '''
        This method sorts all users by brand
        '''
        self.cars.sort(key=lambda x: x['brand'])

    def sort_cars_by_duration(self) -> None:
        '''
        This method sorts all users by duration 
        '''
        self.cars.sort(key=lambda x: x['duration'])

    def read_from_file(self, file_brand: str) -> None:
        '''
        This method allows you to append into the list all users from a file
        '''
        with open(file_brand, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                self.add_car(data[0], data[1], data[2],
                                data[3], int(data[4]))

    def write_to_file(self, file_brand: str) -> None:
        '''
        This method allows you to read all users from a file
        '''
        with open(file_brand, 'w') as file:
            for car in self.cars:
                file.write(
                    f"{car['brand']},{car['model']},{car['mileage_last_checkup']},{car['mileage_current_checkup']},{car['duration']}\n")


if __name__ == "__main__":
        try:
            journal = CarServiceList()
            journal.add_car("Mazda", "Miata", "10500", "11000", 1)
            journal.add_car("BMW", "E320", "5000", "8732", 12)
            journal.add_car("Toyota", "Crown", "123", "1000", 4)
            journal.add_car("Suzuki", "Jimny", "980", "320", 2)
            journal.read_from_file("cars.txt")
            journal.sort_cars_by_brand()
            journal.write_to_file("sorted_cars.txt")

            # Additional work with the carJournal class
            journal.display_cars()
            journal.remove_car("BMW", "E320")
            journal.display_cars()
        except Exception as e:
            print(f"Error: {e}")