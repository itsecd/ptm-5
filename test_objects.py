import pytest
import pygame
import math
from objects import Road, Coins, Button, Nitro, Tree

SCREEN = WIDTH, HEIGHT = 288, 512
WIN = pygame.display.set_mode(SCREEN)

@pytest.fixture
def road() -> Road:
    return Road()

@pytest.mark.parametrize("speed", [10, 20, 30, 40, 50])    
def test_list_update_road(road: Road, speed: int):
    y1_res = [10, 20, 30, 40, 50]
    y2_res = [10-HEIGHT, 20-HEIGHT, 30-HEIGHT, 40-HEIGHT, 50-HEIGHT]
    road.update(speed)
    assert road.y1 in y1_res
    assert road.y2 in y2_res
    
def test_update_road(road: Road)-> None:   
    road.update(4)
    assert road.y1 == 4  
    assert road.y2 == 4-HEIGHT      
    
def test_init_road()-> None:
    road = Road()
    assert road.x == 30
    assert road.y1 == 0
    assert road.y2 == -HEIGHT
    assert road.move == True
    
def test_update_coins():
    coins = Coins(5, 5)
    for i in range(30):
        coins.update(1)    
    assert coins.counter == 30

@pytest.fixture
def nitro() -> Nitro:
    return Nitro(1,1)

@pytest.mark.parametrize("nitro_on", [True, False])
def test_nitro_gas(nitro: Nitro, nitro_on:bool)-> None:
    gas = []
    for i in range(2):
        nitro.update(nitro_on)
        gas.append(nitro.gas)
    assert math.fabs(gas[1]-gas[0]) == 1

def test_init_tree()-> None:
    tree = Tree(10, 20)
    assert tree.rect.x == 10
    assert tree.rect.y == 20

@pytest.fixture
def button()-> Button:
    restart_img = pygame.image.load('app.png')
    return Button(restart_img, SCREEN, 2, 2)

def test_draw(button: Button):
    assert button.clicked == False
    assert button.draw(WIN) == False    