import pytest
from player import Player, WEAPONS
from dicts.utils import *
from monster import Monster

@pytest.fixture
def player():
    return Player(name="Test Player", hp=10, weapon=WEAPONS[SWORD])

@pytest.fixture
def player_with_bow():
    return Player(name="Test Player", hp=10, weapon=WEAPONS[BOW])

def test_player_initialization(player):
    assert player.name == "Test Player"
    assert player.hp == 10
    assert player.weapon == WEAPONS['SWORD']
    assert player.skill == 0
    assert player.max_skill == 3

def test_player_attack(player):
    enemy = Monster("Enemy", 4, 5)
    player.attack(enemy)
    assert enemy.hp == 1
    assert enemy.alive == True
    assert enemy.lenght == 8
    assert player.skill == 1 
    player.attack(enemy)
    assert enemy.hp == -2
    assert enemy.alive == False
    assert player.skill == 2

def test_double_trouble(player):
    enemy = Monster("Enemy", 10, 5)
    enemy_2 = Monster("Enemymorethanmaxdmg", 6, 5)
    player.skill = 3
    player.double_trouble(enemy)
    player.double_trouble(enemy_2)
    assert enemy.hp == 4  
    assert enemy_2.length == 20
    assert enemy_2.alive == False

def test_show_method(player, capsys):
    player.skill = 3
    player.show()
    captured = capsys.readouterr()
    assert "Test Player" in captured.out
    assert "10" in captured.out
    assert "HP" in captured.out
    assert "Sword" in captured.out
    assert "3" in captured.out
    assert "Sword (DMG: 3)" in captured.out
    assert "Double Trouble" in captured.out
    assert "ooo" in captured.out
    assert "Weapon" in captured.out
    assert "Skill" in captured.out
    assert " (Ready!)" in captured.out

def test_arrow_storm(player_with_bow):
    enemys = [Monster("Enemy0", 10, 5), Monster("Enemy1", 1, 5), Monster("Enemy2", 5, 5)]
    player_with_bow.skill = 3
    player_with_bow.arrow_storm(enemys)
    assert enemys[0].hp == 8
    assert enemys[0].alive == True   
    assert enemys[1].hp == -1
    assert enemys[1].alive == False
    assert enemys[2].hp == 3