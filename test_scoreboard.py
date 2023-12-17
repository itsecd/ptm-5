from unittest.mock import patch, MagicMock
from Game import ScoreBoard


@patch('Game.curses')
def test_scoreboard_run(mock_curses: MagicMock) -> None:
    """
    Тестирует инициализацию и запуск экрана таблицы результатов в классе ScoreBoard.
    Проверяет, что начальные настройки экрана таблицы результатов были выполнены.
    """
    mock_screen = MagicMock()
    scoreboard = ScoreBoard()
    scoreboard._ScoreBoard__run(mock_screen)
    mock_screen.curs_set.assert_called_with(False)
    mock_screen.clear.assert_called()


@patch('Game.curses')
def test_scoreboard_loop(mock_curses: MagicMock) -> None:
    """
    Тестирует игровой цикл таблицы результатов в классе ScoreBoard.
    Проверяет, что цикл таблицы результатов корректно обрабатывает события и обновляет экран.
    """
    mock_screen = MagicMock()
    scoreboard = ScoreBoard()
    scoreboard._ScoreBoard__loop(mock_screen)
    mock_screen.clear.assert_called()
    mock_screen.refresh.assert_called()


@patch('Game.curses')
def test_scoreboard_add_score(mock_curses: MagicMock) -> None:
    """
    Тестирует добавление нового результата в таблицу результатов.
    Проверяет, что новый результат корректно добавляется в список результатов.
    """
    scoreboard = ScoreBoard()
    test_score = ["2023-12-17", 100]
    scoreboard.add_score(test_score)
    assert test_score in scoreboard._ScoreBoard__score_list, "Новый результат должен быть добавлен в список результатов"