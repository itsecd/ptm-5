import pytest
from menu import Menu
import random


@pytest.fixture
def menu() -> Menu:
    return Menu(window="window")


def test_appendItem(menu: Menu) -> None:
    test_item = "test_item"
    menu.appendItem(test_item)
    assert test_item in menu.items


def test_editItem(menu: Menu) -> None:
    test_item = "test_item"
    menu.appendItem(test_item)
    edit_test_item = "edit_test_item"
    menu.editItem(edit_test_item, 0)
    assert edit_test_item in menu.items


def test_delItem(menu: Menu) -> None:
    test_item = "test_item"
    menu.appendItem(test_item)
    menu.delItem(test_item, 0)
    assert test_item not in menu.items


def test_increaseIndex(menu: Menu) -> None:
    start_index = random.randint(0, 100)
    menu.index = start_index
    menu.increaseIndex()
    assert start_index + 1 == menu.index


def test_decreaseIndex(menu: Menu) -> None:
    start_index = random.randint(0, 100)
    menu.index = start_index
    menu.decreaseIndex()
    assert start_index - 1 == menu.index


@pytest.mark.parametrize("footer", ["test", "tset", "some_test", "tset_emos"])
def test_setFooter(menu: Menu, footer: str) -> None:
    menu.setFooter(footer)
    assert footer == menu.footer


@pytest.mark.parametrize("title", ["test", "tset", "some_test", "tset_emos"])
def test_setTitle(menu: Menu, title: str) -> None:
    menu.setTitle(title)
    assert title == menu.title
