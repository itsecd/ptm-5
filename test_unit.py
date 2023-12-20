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


if __name__ == "__main__":
    pytest.main(["-v", "-color=yes"])
