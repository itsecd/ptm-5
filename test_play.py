from Game import Play
import random
from fake import FakeScreen, FakeRandom

"""
Модуль для тестирования класса Play.
"""


class TestPlay:
    @classmethod
    def setup_class(cls) -> None:
        """
        Начальная инициализация полей тестового класса.
        :return: нет возвращаемого значения.
        """
        cls.play = Play("#", "*")
        cls.random = FakeRandom()

    def test_load_content(self):
        """
        Функция тестирует загрузку начального экрана при запуске игры.
        :return: Нет возвращаемого значения.
        """
        width = 100
        height = 200
        self.play._x_len = width
        self.play._y_len = height
        self.play._load_content(FakeScreen())
        assert self.play._snake_body == [[height // 2, width // 2]] and self.play._current_direction == "right"

    def test_get_apple_position(self):
        """
        Функция тестирует корректность сгенерированной позиции яблока (не должно попасть на тело змейки).
        :return: Нет возвращаемого значения.
        """
        width = 100
        height = 200
        self.random.random_value = 30
        self.play._snake_body = [[30, 31]]
        self.play._x_len = width
        self.play._y_len = height
        tmp = random.randint
        random.randint = self.random.randint
        apple = self.play._get_apple_position()
        random.randint = tmp
        assert apple not in self.play._snake_body

    def test_change_direction(self):
        """
        Функция тестирует корректность изменения направления движения змейки.
        :return: Нет возвращаемого значения.
        """
        result = []
        screen = FakeScreen()
        screen.pressed_key = 97
        self.play._current_direction = "up"
        self.play._get_new_direction(screen)
        result.append(self.play._current_direction)
        screen.pressed_key = 100
        self.play._current_direction = "up"
        self.play._get_new_direction(screen)
        result.append(self.play._current_direction)
        screen.pressed_key = 115
        self.play._current_direction = "up"
        self.play._get_new_direction(screen)
        result.append(self.play._current_direction)
        assert result == ["left", "right", "up"]

    def test_pause(self):
        """
        Функция тестирует режим паузы во время игры.
        :return: Нет возвращаемого значения.
        """
        result = []
        screen = FakeScreen()
        screen.pressed_key = 10
        self.play._pause = False
        self.play._get_new_direction(screen)
        result.append(self.play._pause)
        self.play._get_new_direction(screen)
        result.append(self.play._pause)
        assert result == [True, False]

    def test_move_snake_head(self):
        """
        Функция тестирует перемещение головы змейки по полю в соответствии с её текущим направлением.
        :return: Нет возвращаемого значения.
        """
        result = []
        screen = FakeScreen()
        self.play._snake_body = [[10, 10]]
        self.play._current_direction = 'right'
        self.play._move_snake_head(screen)
        result.append(self.play._snake_body[0])
        self.play._snake_body = [[10, 10]]
        self.play._current_direction = 'left'
        self.play._move_snake_head(screen)
        result.append(self.play._snake_body[0])
        self.play._snake_body = [[10, 10]]
        self.play._current_direction = 'up'
        self.play._move_snake_head(screen)
        result.append(self.play._snake_body[0])
        self.play._snake_body = [[10, 10]]
        self.play._current_direction = 'down'
        self.play._move_snake_head(screen)
        result.append(self.play._snake_body[0])
        assert result == [[10, 11], [10, 9], [9, 10], [11, 10]]

    def test_remove_tail(self):
        """
        Функция тестирует удаление хвоста змейки при её движении.
        :return: Нет возвращаемого значения.
        """
        screen = FakeScreen()
        self.play._snake_body = [[11, 10], [10, 10], [9, 10]]
        self.play._current_direction = 'bottom'
        self.play.apple = [50, 50]
        self.play._remove_the_tail(screen)
        assert self.play._snake_body == [[11, 10], [10, 10]]

    def test_eat_apple(self):
        """
        Функция тестирует сохранение размера змейки при поедании ею яблока.
        :return: Нет возвращаемого значения.
        """
        screen = FakeScreen()
        self.play.score = [0, 5]
        self.play._snake_head = [11, 10]
        self.play._snake_body = [[11, 10], [10, 10], [9, 10]]
        self.play.apple = [11, 10]
        self.play._remove_the_tail(screen)
        assert self.play._snake_body == [[11, 10], [10, 10], [9, 10]] and self.play.score[1] == 6

    def test_run_into_wall(self):
        """
        Функция тестирует условие смерти змейки при её столкновении со стеной.
        :return: Нет возвращаемого значения.
        """
        result = []
        self.play._x_len = 100
        self.play._y_len = 200
        self.play._snake_head = [11, 10]
        self.play._snake_body = [[11, 10]]
        result.append(self.play._condictions_to_lose())
        self.play._snake_head = [2, 10]
        self.play._snake_body = [[2, 10]]
        result.append(self.play._condictions_to_lose())
        self.play._snake_head = [197, 10]
        self.play._snake_body = [[197, 10]]
        result.append(self.play._condictions_to_lose())
        self.play._snake_head = [11, 5]
        self.play._snake_body = [[11, 5]]
        result.append(self.play._condictions_to_lose())
        self.play._snake_head = [11, 94]
        self.play._snake_body = [[11, 94]]
        result.append(self.play._condictions_to_lose())
        assert result == [None, 1, 1, 1, 1]

    def test_run_into_itself(self):
        """
        Функция тестирует условие смерти змейки при её столкновении с частью своего тела.
        :return: Нет возвращаемого значения.
        """
        self.play._snake_head = [11, 10]
        self.play._snake_body = [[11, 10], [10, 10], [10, 9], [11, 9], [11, 10]]
        assert self.play._condictions_to_lose() == 1
