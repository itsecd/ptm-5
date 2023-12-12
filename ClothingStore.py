import csv
import logging


class Clothes:
    """
    This is class for clothes
    """
    def __init__(self, name, color, size, brand, material, price):
        self.name = name
        self.color = color
        self.size = size
        self.brand = brand
        self.material = material
        self.price = price


class Manager:
    """
    This is class for manager, who manage clothing store
    """
    def __init__(self):
        self.clothes_store = []

    def add_clothes(self, clothes: Clothes) -> None:
        """
        Add 1 object(Clothes) in store
        :param clothes: Object Clothes
        :return: No return
        """
        self.clothes_store.append(clothes)

    def remove_clothes(self, clothes: Clothes) -> None:
        """
        Remove 1 clothes from store
        :param clothes: Clothes need to removed
        :return: No return
        """
        for clothess in self.clothes_store:
            if clothess.name == clothes.name and clothess.brand == clothes.brand and clothess.size == clothes.size:
                self.clothes_store.remove(clothess)

    def display_clothes(self) -> None:
        """
        Show list clothes in screen
        :return: No return
        """
        for clothes in self.clothes_store:
            print(f"Name: {clothes.name}, Color: {clothes.color}, Size: {clothes.size},"
                  f" Brand: {clothes.brand}, Material: {clothes.material}, Price: {clothes.price}")

    def find_clothes(self, name) -> list:
        """
        Find informations about clothes
        :param name: name object Clothes
        :return: If found, return this clothes, if not found, no return
        """
        lst = []
        for clothes in self.clothes_store:
            if clothes.name == name:
                lst.append(clothes)
        return lst

    def write_to_csv(self, file_path: str) -> None:
        """
        Write to file csv
        :param file_path: name of file (need write '.csv' in the last)
        :return: no return
        """
        try:
            with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Name', 'Color', 'Size', 'Brand', 'Material', 'Price'])
                for clothes in self.clothes_store:
                    writer.writerow([clothes.name, clothes.color, clothes.size,
                                     clothes.brand, clothes.material, clothes.price])
        except Exception as err:
            logging.error(f"Exists error {err}")

    def read_from_csv(self, file_path: str) -> None:
        """
        Read list of clothes from file csv
        :param file_path: name of file (need write '.csv' in the last)
        :return: No return
        """
        try:
            with open(file_path, 'r', encoding='utf-8', newline='') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                if header != ['Name', 'Color', 'Size', 'Brand', 'Material', 'Price']:
                    raise ValueError("Unexpected file format")

                for row in reader:
                    name, color, size, brand, material, price = row
                    clothes = Clothes(name, color, size, brand, material, float(price))
                    self.clothes_store.append(clothes)
        except FileNotFoundError:
            logging.info(f"File {file_path} not exists")
        except Exception as err:
            logging.error(f"During open file had error {err}")

    def is_null(self) -> bool:
        """
        Check store empty ore not
        :return: False if not empty, True if empty
        """
        return len(self.clothes_store) == 0

    def clear_store(self) -> None:
        """
        Remove all of clothes in store
        :return:
        """
        self.clothes_store = []


if __name__ == "__main__":
    store_manager = Manager()
    print(store_manager.is_null())
    store_manager.add_clothes(Clothes("Shirt", "Blue", "L", "Levi's", "Cotton", 1500))
    store_manager.add_clothes(Clothes("Trouser", "Black", "30", "Wrangler", "Denim", 1799))
    store_manager.add_clothes(Clothes("Trouser", "Brown", "30", "Louis Vuitton", "Denim", 2000))
    store_manager.add_clothes(Clothes("Hoodie", "Gray", "XL", "Palm Anger", "Polyester", 2599))
    store_manager.add_clothes(Clothes("Hat", "Red", "M", "Adidas", "Wool", 1999))
    store_manager.add_clothes(Clothes("Scarf", "Brown", "35", "Gucci", "Silk", 1499))
    store_manager.write_to_csv("clothes.csv")
    clothes = Clothes("Trouser", "Brown", "30", "Louis Vuitton", "Denim", 2000)
    store_manager.display_clothes()
    store_manager.remove_clothes(clothes)
    print()
    store_manager.display_clothes()
