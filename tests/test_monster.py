import pytest
from dicts.weapons_skills import Player, WEAPONS
from monster import Monster
from dicts.utils import *

@pytest.fixture
def stub_monster():
    return StubMonster("Bob", 25, 10)

@pytest.fixture
def monster():
    return Monster("Wolf", 10, 5)

class StubMonster:
    def __init__(self, name, hp, dmg, action='defence', ):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.dmg = dmg
        self.action = action
        self.alive = True
        self.length = 0

    def update_data(self):
        pass


def test_monster_initialization(stub_monster):
    monster = Monster("Bob", 25, 10, 'defence')
    assert monster.name == stub_monster.name
    assert monster.hp == stub_monster.hp
    assert monster.max_hp == stub_monster.max_hp
    assert monster.dmg == stub_monster.dmg
    assert monster.action == stub_monster.action
    assert monster.alive == stub_monster.alive
    assert monster.length == stub_monster.length
    
def test_line(monster):
    monster.length = 5
    assert "┌-----┐" == monster.line("top")
    assert "---------------" == monster.line("mid")
    assert "└-----┘" == monster.line("bot")
    assert '\n' * 120 == monster.line("clear")

def test_update_data(monster):
    monster.hp = -5
    monster.update_data()
    assert monster.alive == False
    assert monster.name == "Dead Wolf"
    assert monster.length == 14
    monster.name = "Wolf 0123456789"
    monster.update_data()
    assert monster.name == "Dead 0123456789"
    assert monster.length == 16

def test_show_monster(monster):
    monster.hp -= 1
    assert monster.show('min') == "┌-------------------------------┐\n|Wolf |HP: █████████░ 9 |DMG: 5 |\n└-------------------------------┘"
    assert monster.length == 31
    monster.alive = False
    assert monster.show('min') == "┌----------┐\n|Dead Wolf |\n└----------┘"
    assert monster.length == 10
    assert monster.show('max') == "┌--------------┐\n|Dead Wolf     |\n└--------------┘"
    assert monster.length == 14    
    monster.alive = True
    assert monster.show('max') == "┌--------------┐\n|Dead Wolf     |\n|HP:9          |\n|DMG:5         |\n└--------------┘"
    assert monster.length == 14

def test_attack(monster, stub_monster):
    monster.attack(stub_monster)
    assert stub_monster.hp == 20