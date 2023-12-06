from Game import Menu
import curses
from fake import FakeScreen, fake_color_pair


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

