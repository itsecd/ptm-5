import pytest
import random

from monster import Monster

@pytest.fixture
def monster() -> Monster:
    return Monster("monster", 5, 1,'hit')

@pytest.fixture
def dead_monster() -> Monster:
    return Monster("monster", 0, 1,'hit')

@pytest.fixture
def long_dead_monster() -> Monster:
    return Monster("monster with long name", 0, 1,'hit')

@pytest.mark.parametrize("shape", ["top", "mid", "bot", "clear"])
def test_line(monster: Monster, shape: str) -> None:
    result = monster.line(shape)
    assert result in ("┌┐", "", "└┘", '\n' * 120)

def test_attack(monster: Monster) -> None:
    enemy = Monster("enemy", 5, 1,'hit')
    monster.attack(enemy)
    assert enemy.hp == 4 

@pytest.mark.parametrize("mode", ["min", "max"])
def test_show_alive(monster: Monster, mode: str) -> None:
    result = monster.show(mode)
    assert result in ["┌-----------------------------┐\n|monster |HP: █████ 5 |DMG: 1 |\n└-----------------------------┘", "┌---------┐\n|monster  |\n|HP:5     |\n|DMG:1    |\n└---------┘"]

def test_update_data_dead(monster: Monster) -> None:
    deader = Monster("deader", 1, 10,'hit')
    monster.attack(deader)
    assert deader.alive == False
    assert deader.name == "Dead deader"

def test_update_data_alive(monster: Monster) -> None:
    deader = Monster("deader", 5, 3,'hit')
    monster.attack(deader)
    assert deader.alive == True
    assert deader.length == 9

def test_update_data_long_name(long_dead_monster: Monster) -> None:
    long_dead_monster.update_data()
    assert long_dead_monster.name == "Dead with long name"


@pytest.mark.parametrize("mode", ["min", "max"])
def test_show_dead(dead_monster: Monster, mode: str) -> None:
    dead_monster.update_data()
    result = dead_monster.show(mode)
    assert result == "┌-------------┐\n|Dead monster |\n└-------------┘"