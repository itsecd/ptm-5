from Game import ScoreBoard


def test_scoreboard_add_score():
    """
    Тестирует добавление нового результата в таблицу результатов.
    Проверяет, что новый результат корректно добавляется в список результатов.
    """
    scoreboard = ScoreBoard()
    test_score = ["2023-12-17", 100]
    scoreboard.add_score(test_score)
    assert test_score in scoreboard._ScoreBoard__score_list, "Новый результат должен быть добавлен в список результатов"


def test_scoreboard_sorting_scores():
    """
    Тестирует сортировку результатов в таблице результатов.
    Проверяет, что результаты сортируются в правильном порядке.
    """
    scoreboard = ScoreBoard()
    scores = [["2023-12-17", 50], ["2023-12-18", 100], ["2023-12-16", 75]]
    for score in scores:
        scoreboard.add_score(score)
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    assert scoreboard._ScoreBoard__score_list == sorted_scores, "Результаты должны быть отсортированы по убыванию баллов"


def test_scoreboard_initialization():
    """
    Тестирует инициализацию объекта ScoreBoard.
    Проверяет, что все начальные параметры установлены правильно.
    """
    scoreboard = ScoreBoard()
    assert isinstance(scoreboard._ScoreBoard__score_list, list), "Score list должен быть инициализирован как список"