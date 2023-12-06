from Game import ScoreBoard, Play, Menu
import curses
import pytest


class FakeScreen:
    """
    Класс подменяет класс Screen библиотеки curses.
    """
    def __init__(self):
        """
        Инициализация класса FakeScreen.
        Поле attributes - список строк, расположенных на экране с их координатами.
        Поле highlight_item - текущий выделенная на экране строка.
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


class TestMenu:
    @classmethod
    def setup_class(cls) -> None:
        """
        Начальная инициализация полей тестового класса и подмена функций библиотеки curses.
        :return: нет возвращаемого значения.
        """
        cls.menu = Menu()
        curses.color_pair = fake_color_pair

    def test_show_menu(self):
        """
        Функция тестирует отображение элементов меню по центру экрана.
        :return: Нет возвращаемого значения.
        """
        width = 100
        height = 200
        self.menu._x_len = width
        self.menu._y_len = height
        screen = FakeScreen()
        self.menu._show_menu(screen)
        assert screen.attributes == [(height // 2 - 1, width // 2 - len('Play') // 2, 'Play'),
                                     (height // 2, width // 2 - len('Scoreboard') // 2, 'Scoreboard'),
                                     (height // 2 + 1, width // 2 - len('EXIT') // 2, 'EXIT')]

    def test_highlight_item(self):
        """
        Функция тестирует выделение текущего выбранного элемента меню.
        :return: Нет возвращаемого значения.
        """
        width = 100
        height = 200
        self.menu._x_len = width
        self.menu._y_len = height
        self.menu.selected_item = 1
        screen = FakeScreen()
        self.menu._show_menu(screen)
        assert screen.highlight_item == 1

    def test_out_of_list(self):
        """
        Функция тестирует неизменяемость текущего выбранного элемента при попытке выхода за пределы списка меню.
        :return: Нет возвращаемого значения.
        """
        result = []
        screen = FakeScreen()
        self.menu.selected_item = 0
        screen.pressed_key = 119
        self.menu._keyboard(screen)
        result.append(self.menu.selected_item)
        self.menu.selected_item = 2
        screen.pressed_key = 115
        self.menu._keyboard(screen)
        result.append(self.menu.selected_item)
        assert result == [0, 2]

    def test_change_item(self):
        """
        Функция тестирует корректность смены текущего элемента меню.
        :return: Нет возвращаемого значения.
        """
        result = []
        screen = FakeScreen()
        self.menu.selected_item = 1
        screen.pressed_key = 119
        self.menu._keyboard(screen)
        result.append(self.menu.selected_item)
        self.menu.selected_item = 1
        screen.pressed_key = 115
        self.menu._keyboard(screen)
        result.append(self.menu.selected_item)
        assert result == [0, 2]

    def test_select_item(self):
        """
        Функция тестирует выбор определённого элемента меню.
        :return: Нет возвращаемого значения.
        """
        screen = FakeScreen()
        self.menu.selected_item = 1
        screen.pressed_key = 10
        assert self.menu._keyboard(screen)

