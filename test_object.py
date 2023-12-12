import pytest
import pygame
import tkinter
from objects import Egg, Basket, Splash, ScoreText, Button, getEggPos, display_score

SCREEN = WIDTH, HEIGHT = 600, 960
WIN = pygame.display.set_mode(SCREEN)

@pytest.fixture
def egg() -> Egg:
    return Egg(5, 5, WIN)


@pytest.mark.parametrize("speed", [10, 20, 30, 40, 50])    
def test_list_update_egg(egg: Egg, speed: int):
    y_res = [15, 25, 35, 45, 55]
    egg.update(speed)
    assert egg.rect.y in y_res

def test_update_egg(egg: Egg)-> None:   
    egg.update(4)
    assert egg.rect.y == 9    

def test_check_collision_basket():
    basket = Basket(3, 3, WIN)
    assert basket.check_collision(pygame.Rect(0, 0, 2, 2)) == False

def test_update_splash():
    splash = Splash(5, 5, WIN)
    for i in range(50):
        splash.update()    
    assert splash.count == 50

@pytest.fixture
def score_text() ->ScoreText:
    pygame.font.init()
    return ScoreText('win', pygame.font.Font(None,30), [2, 2], WIN)

def test_update_score_text(score_text: ScoreText)-> None:
    for i in range(3):
        score_text.update()
    assert score_text.counter == 3

@pytest.mark.parametrize("score_rect", [[2, 2], [3, 3], [4, 4], [5, 5]])
def test_display_score(score_rect: list) -> None:
    pygame.font.init()
    res = display_score(score_text,pygame.font.Font(None,30), score_rect)
    assert score_rect == res[1][0:2]    

@pytest.fixture
def button()-> Button:
    restart_img = pygame.image.load('egg.png')
    return Button(restart_img, None, 2, 2)

def test_draw(button: Button):
    assert button.clicked == False
    assert button.draw(WIN) == False

def test_getEggPos() -> None:
    x_list = [120, 260, 400, 520]
    x, y = getEggPos() 
    assert x in x_list
    assert y == 260

