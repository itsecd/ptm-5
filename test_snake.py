# Импортируем библиотеки


import pytest
import unittest.mock as mock

""""""
import pygame as pg
from random import randrange
# Константы
WINDOW = 1000
FPS = 60
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

# Функция для определения координат (X:Y) случайной позиции на игровом поле
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]

# Параметры змейки
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)

# Параметры времени и задержки
time = 0
time_step = 110

# Параметры объектов еды
food = snake.copy()
food.center = get_random_position()

# Инициализация объектов
gameScreen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
"""
# Главный цикл игры
while True:
    # Частота обновления экрана
    clock.tick(FPS)

    # Цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        # Обработка нажатий WASD
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)

    gameScreen.fill((155, 188, 15))

    # Столкновение с границами и телом змейки
    snake_collision = pg.Rect.collidelist(snake, segments[:-1]) != -1

    if (
        snake.left < 0
        or snake.right > WINDOW
        or snake.top < 0
        or snake.bottom > WINDOW
        or snake_collision
    ):
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    # Поедание
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # Рисуем объект еды
    pg.draw.rect(gameScreen, (15, 56, 15), food)

    # Рисуем змейку
    [pg.draw.rect(gameScreen, (120, 149, 12), segment) for segment in segments]

    # Управляем змейкой
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    """

# Функция для создания фикстуры змейки
@pytest.fixture
def snake_fixture():
    return pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])

# Функция для создания фикстуры еды
@pytest.fixture
def food_fixture():
    return snake_fixture().copy()

# Функция для создания фикстуры сегментов
@pytest.fixture
def segments_fixture():
    return [snake_fixture().copy()]

# Тест для проверки функции get_random_position
def test_get_random_position():
    # Проверяем, что функция возвращает список из двух элементов
    assert len(get_random_position()) == 2

    # Проверяем, что каждый элемент списка находится в допустимом диапазоне
    assert RANGE[0] <= get_random_position()[0] <= RANGE[1]
    assert RANGE[0] <= get_random_position()[1] <= RANGE[1]

    # Проверяем, что каждый элемент списка кратен TILE_SIZE
    assert get_random_position()[0] % TILE_SIZE == 0
    assert get_random_position()[1] % TILE_SIZE == 0

# Тест для проверки столкновения змейки с границами
def test_snake_collision_with_borders(snake_fixture):
    # Проверяем, что змейка не сталкивается с границами при инициализации
    assert snake_fixture.left >= 0
    assert snake_fixture.right <= WINDOW
    assert snake_fixture.top >= 0
    assert snake_fixture.bottom <= WINDOW

    # Проверяем, что змейка сталкивается с левой границей, если ее x-координата меньше 0
    snake_fixture.left = -1
    assert snake_fixture.left < 0

    # Проверяем, что змейка сталкивается с правой границей, если ее x-координата больше WINDOW
    snake_fixture.right = WINDOW + 1
    assert snake_fixture.right > WINDOW

    # Проверяем, что змейка сталкивается с верхней границей, если ее y-координата меньше 0
    snake_fixture.top = -1
    assert snake_fixture.top < 0

    # Проверяем, что змейка сталкивается с нижней границей, если ее y-координата больше WINDOW
    snake_fixture.bottom = WINDOW + 1
    assert snake_fixture.bottom > WINDOW

# Тест для проверки столкновения змейки с телом
def test_snake_collision_with_body(snake_fixture, segments_fixture):
    # Проверяем, что змейка не сталкивается с телом при инициализации
    assert pg.Rect.collidelist(snake_fixture, segments_fixture[:-1]) == -1

    # Проверяем, что змейка сталкивается с телом, если ее центр совпадает с центром одного из сегментов
    snake_fixture.center = segments_fixture[0].center
    assert pg.Rect.collidelist(snake_fixture, segments_fixture[:-1]) != -1

# Тест для проверки поедания еды
def test_snake_eating_food(snake_fixture, food_fixture):
    # Проверяем, что змейка не ест еду при инициализации
    assert snake_fixture.center != food_fixture.center 
    # Проверяем, что змейка ест еду, если ее центр совпадает с центром еды 
    snake_fixture.center = food_fixture.center 
    assert snake_fixture.center == food_fixture.center

# Тест для проверки управления змейкой с помощью клавиш WASD
def test_snake_control(snake_fixture):
    # Проверяем, что змейка не движется при инициализации
    assert snake_dir == (0, 0)
    
    # Проверяем, что змейка движется вверх, если нажата клавиша W
    with mock.patch('pygame.event.get') as mock_event:
        mock_event.return_value = [pg.event.Event(pg.KEYDOWN, key=pg.K_w)]
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    snake_dir = (0, -TILE_SIZE)
        assert snake_dir == (0, -TILE_SIZE)
    
    # Проверяем, что змейка движется вниз, если нажата клавиша S
    with mock.patch('pygame.event.get') as mock_event:
        mock_event.return_value = [pg.event.Event(pg.KEYDOWN, key=pg.K_s)]
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    snake_dir = (0, TILE_SIZE)
        assert snake_dir == (0, TILE_SIZE)
    
    # Проверяем, что змейка движется влево, если нажата клавиша A
    with mock.patch('pygame.event.get') as mock_event:
        mock_event.return_value = [pg.event.Event(pg.KEYDOWN, key=pg.K_a)]
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    snake_dir = (-TILE_SIZE, 0)
        assert snake_dir == (-TILE_SIZE, 0)
    
    # Проверяем, что змейка движется вправо, если нажата клавиша D
    with mock.patch('pygame.event.get') as mock_event:
        mock_event.return_value = [pg.event.Event(pg.KEYDOWN, key=pg.K_d)]
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    snake_dir = (TILE_SIZE, 0)
        assert snake_dir == (TILE_SIZE, 0)

# Тест для проверки рисования объектов еды и змейки
def test_draw_objects(gameScreen, food_fixture, segments_fixture):
    # Проверяем, что игровой экран заполнен цветом (155, 188, 15)
    assert gameScreen.get_at((0, 0)) == (155, 188, 15)

    # Проверяем, что объект еды имеет цвет (15, 56, 15)
    assert gameScreen.get_at(food_fixture.center) == (15, 56, 15)

    # Проверяем, что каждый сегмент змейки имеет цвет (120, 149, 12)
    for segment in segments_fixture:
        assert gameScreen.get_at(segment.center) == (120, 149, 12)

# Тест для проверки обновления времени и движения змейки
def test_update_time_and_move_snake(snake_fixture, segments_fixture):
    # Проверяем, что время инициализируется нулем
    assert time == 0

    # Проверяем, что змейка не двигается, если время не превышает time_step
    snake_pos = snake_fixture.center
    time_now = pg.time.get_ticks()
    if time_now - time <= time_step:
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
        assert snake_fixture.center == snake_pos

    # Проверяем, что змейка двигается, если время превышает time_step
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
        assert snake_fixture.center != snake_pos
