import pytest
import random

from monster import Monster

@pytest.fixture
def monster() -> Monster:
    return Monster("monster", 5, 1,'hit')

def test_line(monster: Monster) -> None:
    top = monster.line("top")
    mid = monster.line("mid")
    bot = monster.line("bot")
    clear = monster.line("clear")
    assert (top, mid, bot, clear) == ("┌┐", "", "└┘", '\n' * 120)

def test_attack(monster: Monster) -> None:
    enemy = Monster("enemy", 5, 1,'hit')
    monster.attack(enemy)
    assert enemy.hp == 4 

def test_show(monster: Monster) -> None:
    total = monster.show("min")
    assert total == "┌-----------------------------┐\n|monster |HP: █████ 5 |DMG: 1 |\n└-----------------------------┘"

def test_update_data_not_alive(monster: Monster) -> None:
    deader = Monster("deader", 1, 10,'hit')
    monster.attack(deader)
    assert deader.alive == False
    assert deader.name == "Dead deader"

def test_update_data_alive(monster: Monster) -> None:
    deader = Monster("deader", 5, 3,'hit')
    monster.attack(deader)
    assert deader.alive == True
    assert deader.length == 9