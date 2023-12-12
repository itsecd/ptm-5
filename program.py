import sys


class MultiTree:
    """
    Класс, хранящий список объектов
    этого класса и инф. об объекте
    """

    def __init__(self) -> None:
        """Конструктор"""
        self.__nodes = []
        self.__data = float()
    
    def append(self, obj: "MultiTree") -> None:
        """Добавление объекта в список"""
        self.__nodes.append(obj)

    def find(self, obj: "MultiTree") -> bool:
        """Осуществляет поиск объекта в списке"""
        return obj in self.__nodes
    
    def __getitem__(self, index: int) -> "MultiTree":
        """Обращение по индексу (исключение вызывается Python"ом)"""
        return self.__nodes[index]
    
    def clear(self) -> None:
        """Очищение объекта класса MultiTree от всех значений"""
        for obj in self.__nodes:
            if obj.is_empty() == False:
                obj.clear()
        self.__nodes.clear()

    def is_empty(self) -> bool:
        """Проверка списка объектов на пустоту"""
        return True if len(self.__nodes) == 0 else False

    def count(self) -> int:
        """Возвращает количество объектов в списке"""
        return len(self.__nodes)

    def set_value(self, value) -> None:
        """Присваивает переданное зн-е пер-ой __data"""
        self.__data = value
    
    def get_value(self) -> float:
        """Возвращает зн-е пер-ой __data"""
        return self.__data
    
    value = property(get_value, set_value)