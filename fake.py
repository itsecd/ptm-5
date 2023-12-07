"""
Модуль с классами и функциями, подменяющими необходимые для тестирования классы и функции существующих библиотек.
"""


class FakeScreen:
    """
    Класс подменяет класс Screen библиотеки curses.
    """
    def __init__(self):
        """
        Инициализация класса FakeScreen.
        Поле attributes - список строк, расположенных на экране с их координатами.
        Поле highlight_item - текущая выделенная на экране строка.
        Поле pressed_key - текущая нажатая клавиша.
        """
        self.attributes = []
        self.highlight_item = -1
        self.pressed_key = 119

    def addstr(self, x: int, y: int, text: str) -> None:
        """
        Подмена метода addstr. Добавляет к списку строк с координатами введённое значение.
        :param x: координата строки по оси x.
        :param y: координата строки по оси y.
        :param text: текст исходной строки.
        :return: нет возвращаемого значения.
        """
        self.attributes.append((x, y, text))

    def attron(self, color: int) -> None:
        """
        Подмена метода attron. Сохраняет выделенный элемент меню.
        :param color: цвет.
        :return: нет возвращаемого значения.
        """
        self.highlight_item = len(self.attributes)

    def attroff(self, color: int) -> None:
        """
        Подмена метода attroff.
        :param color: цвет.
        :return: нет возвращаемого значения.
        """
        pass

    def getch(self) -> int:
        """
        Подмена метода getch. Возвращает текущую нажатую клавишу.
        :return: текущая нажатая клавиша.
        """
        return self.pressed_key


def fake_color_pair(color_number: int) -> int:
    """
    Подмена функции color_pair библиотеки curses. Возвращает число типа int в качестве цвета.
    :param color_number: номер цвета.
    :return: цвет.
    """
    return color_number


class FakeRandom:
    """
    Класс создан для подмены функции randint модуля random.
    """
    def __init__(self):
        """
        Инициализация класса FakeRandom.
        Параметр random_value - стартовое число, которое будет передано, как случайное.
        Параметр step величина изменения random_value при вызове.
        """
        self.random_value = 0
        self.step = 1

    def randint(self, begin: int, end: int) -> int:
        """
        Подмена метода randint. Увеличивает текущее псевдослучайное число на некоторый шаг.
        :param begin: начало отрезка.
        :param end: конец отрезка.
        :return: псевдослучайное число.
        """
        self.random_value += self.step
        return self.random_value - self.step
