from Game import Play
import random
from fake import FakeScreen, FakeRandom


class TestPlay:
    @classmethod
    def setup_class(cls) -> None:
        """
        Начальная инициализация полей тестового класса и подмена функций библиотеки curses.
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

