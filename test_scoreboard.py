from Game import ScoreBoard

"""
Модуль для тестирования класса Scoreboard.
"""


class TestScoreBoard:
    @classmethod
    def setup_class(cls) -> None:
        """
        Начальная инициализация полей тестового класса.
        :return: нет возвращаемого значения.
        """
        cls.score_board = ScoreBoard()

    def test_add_single_score(self):
        """
        Функция тестирует добавление рекорда в пустой список рекордов.
        :return: Нет возвращаемого значения.
        """
        self.score_board._score_list = []
        score = [0, 1]
        self.score_board.add_score(score)
        assert self.score_board._score_list == [[0, 1]]

    def test_add_best_score(self):
        """
        Функция тестирует ранжирование в списке рекордов лучшего рекорда.
        :return: Нет возвращаемого значения.
        """
        self.score_board._score_list = [[0, 3], [0, 2]]
        score = [0, 4]
        self.score_board.add_score(score)
        assert self.score_board._score_list == [[0, 4], [0, 3], [0, 2]]

    def test_add_middle_score(self):
        """
        Функция тестирует ранжирование в списке рекордов среднего рекорда.
        :return: Нет возвращаемого значения.
        """
        self.score_board._score_list = [[0, 4], [0, 2]]
        score = [0, 3]
        self.score_board.add_score(score)
        assert self.score_board._score_list == [[0, 4], [0, 3], [0, 2]]

    def test_add_bad_score(self):
        """
        Функция тестирует ранжирование в списке рекордов худшего рекорда.
        :return: Нет возвращаемого значения.
        """
        self.score_board._score_list = [[0, 4], [0, 3]]
        score = [0, 2]
        self.score_board.add_score(score)
        assert self.score_board._score_list == [[0, 4], [0, 3], [0, 2]]
