import pytest
import os
from unittest.mock import patch

from main import Heroes


@pytest.fixture
def hero() -> Heroes:
    return Heroes()


def test_change_class(hero: Heroes):
    """
    Test for changing the hero's class.

    :param hero: The Heroes instance.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_class("Warrior")
    assert hero.hero_class == "Warrior"


def test_change_hp(hero: Heroes):
    """
    Test for changing the hero's HP.

    :param hero: The Heroes instance.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_hp(100)
    assert hero.hp == 100


def test_change_damage(hero: Heroes):
    """
    Test for changing the hero's damage.

    :param hero: The Heroes instance.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_damage(20)
    assert hero.damage == 20


def test_change_armor(hero: Heroes):
    """
    Test for changing the hero's armor.

    :param hero: The Heroes instance.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_armor(50)
    assert hero.armor == 50


def test_change_lvl(hero: Heroes):
    """
    Test for changing the hero's level.

    :param hero: The Heroes instance.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_lvl(5)
    assert hero.lvl == 5


def test_hero_exists(hero: Heroes):
    """
    Test for checking the existence of a hero with the specified ID.

    :param hero: The Heroes instance.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.add_hero(11, 'HorseMan', 150, 300, 70, 30)
    assert hero.hero_exists(6) == True
    assert hero.hero_exists(12) == False


def test_can_survive(hero: Heroes):
    """
    Test for checking the hero's ability to survive in battle.

    :param hero: The Heroes instance.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.add_hero(11, 'HorseMan', 150, 300, 70, 30)
    assert hero.can_survive(6) == False
    assert hero.can_survive(11) == True
    with pytest.raises(ValueError):
        hero.can_survive(None)


@pytest.mark.parametrize("filename", ["test_heroes.csv", "nonexistent_file.csv"])
def test_read_from_csv(hero: Heroes, filename: str) -> None:
    """
    Test for reading hero data from a CSV file.

    :param hero: The Heroes instance.
    :param filename: The name of the CSV file.

    :return: None
    """
    try:
        hero.read_from_csv(filename)
    except Exception as e:
        pytest.fail(f"Exception {e} occurred when reading from {filename}")

    assert True 


@pytest.mark.parametrize("filename", ["test_heroes.csv", "nonexistent_file.csv"])
def test_write_to_csv(hero: Heroes, filename: str) -> None:
    """
    Test for writing hero data to a CSV file.

    :param hero: The Heroes instance.
    :param filename: The name of the CSV file.

    :return: None
    """
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.add_hero(12, 'Warlock', 85, 40, 3, 9)
    hero.add_hero(11, 'Shaman', 95, 30, 7, 3)
    hero.write_to_csv(filename)

    assert os.path.exists(filename)
    assert os.path.getsize(filename) > 0