import pytest
import os
from unittest.mock import patch

from main import Heroes


@pytest.fixture
def hero() -> Heroes:
    return Heroes()


def test_change_class(hero: Heroes):
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_class("Warrior")
    assert hero.hero_class == "Warrior"


def test_change_hp(hero: Heroes):
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_hp(100)
    assert hero.hp == 100


def test_change_damage(hero: Heroes):
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_damage(20)
    assert hero.damage == 20


def test_change_armor(hero: Heroes):
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_armor(50)
    assert hero.armor == 50


def test_change_lvl(hero: Heroes):
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.change_lvl(5)
    assert hero.lvl == 5


def test_hero_exists(hero: Heroes):
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.add_hero(11, 'HorseMan', 150, 300, 70, 30)
    assert hero.hero_exists(6) == True
    assert hero.hero_exists(12) == False


def test_can_survive(hero: Heroes):
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.add_hero(11, 'HorseMan', 150, 300, 70, 30)
    assert hero.can_survive(6) == False
    assert hero.can_survive(11) == True
    with pytest.raises(ValueError):
        hero.can_survive(None)


@pytest.mark.parametrize("filename", ["test_heroes.csv", "nonexistent_file.csv"])
def test_read_from_csv(hero: Heroes, filename: str) -> None:
    hero.read_from_csv(filename)


@pytest.mark.parametrize("filename", ["test_heroes.csv", "nonexistent_file.csv"])
def test_write_to_csv(hero: Heroes, filename: str) -> None:
    hero.add_hero(6, 'Mage', 80, 30, 5, 7)
    hero.add_hero(12, 'Warlock', 85, 40, 3, 9)
    hero.add_hero(11, 'Shaman', 95, 30, 7, 3)
    hero.write_to_csv(filename)

    assert os.path.exists(filename)
    assert os.path.getsize(filename) > 0


if __name__ == "__main__":
    pytest.main(["-v", "-color=yes"])
