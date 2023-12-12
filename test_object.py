import pytest
import pygame
import tkinter
from objects import Egg, Basket, Splash, ScoreText, Button, getEggPos, display_score

SCREEN = WIDTH, HEIGHT = 600, 960
WIN = pygame.display.set_mode(SCREEN)

def test_update_egg()-> None:  
    egg = Egg(2, 2, WIN)  
    egg.update(4)
    assert egg.rect.y == 6
    
def test_check_collision_basket():
    basket = Basket(3, 3, WIN)
    assert basket.check_collision(pygame.Rect(0, 0, 2, 2)) == False

def test_update_splash():
    splash = Splash(5, 5, WIN)
    splash.update()
    win_tmp = pygame.display.set_mode(SCREEN)
    rect = splash.image.get_rect()
    rect.x = 5
    rect.y = 5
    assert splash.count == 1
    assert splash.win.get_rect() == rect

@pytest.fixture
def score_text() ->ScoreText:
    pygame.font.init()
    return ScoreText('win', pygame.font.Font(None,30), [2, 2], WIN)

def test_update_score_text(score_text: ScoreText)-> None:
    for i in range(3):
        score_text.update()
    assert score_text.counter == 3



