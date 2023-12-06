from Game import Globals, ScoreBoard, Play, Menu
import curses
import pytest


def fake_color_pair(color_number: int):
    return color_number


class FakeScreen:
    def __init__(self):
        self.attributes = []
        self.selected_item = -1

    def addstr(self, x: int, y: int, text: str) -> None:
        self.attributes.append((x, y, text))

    def attron(self, color: int) -> None:
        self.selected_item = len(self.attributes)

    def attroff(self, color: int) -> None:
        pass


class TestMenu:
    @classmethod
    def setup_class(cls):
        cls.menu = Menu()
        curses.color_pair = fake_color_pair

    def test_show_menu(self):
        width = 100
        height = 200
        self.menu._x_len = width
        self.menu._y_len = height
        screen = FakeScreen()
        self.menu._show_menu(screen)
        assert screen.attributes == [(height // 2 - 1, width // 2 - len('Play') // 2, 'Play'),
                                     (height // 2, width // 2 - len('Scoreboard') // 2, 'Scoreboard'),
                                     (height // 2 + 1, width // 2 - len('EXIT') // 2, 'EXIT')]

    def test_selected_item(self):
        width = 100
        height = 200
        selected_item = 1
        self.menu._x_len = width
        self.menu._y_len = height
        self.menu.selected_item = selected_item
        screen = FakeScreen()
        self.menu._show_menu(screen)
        assert screen.selected_item == selected_item

