from unittest.mock import patch, MagicMock
from Game import Play


@patch('Game.curses')
def test_play_run(mock_curses: MagicMock) -> None:
    """
    Тестирует инициализацию и запуск игрового процесса в классе Play.
    Проверяет, что были выполнены нужные настройки для начала игры.
    """
    mock_screen = MagicMock()
    play = Play(snake_body_fill='*', apple_fill='@')
    play._Play__run(mock_screen)
    mock_screen.curs_set.assert_called_with(False)
    mock_screen.nodelay.assert_called_with(True)
    mock_screen.clear.assert_called()


@patch('Game.curses')
def test_play_loop(mock_curses: MagicMock) -> None:
    """
    Тестирует игровой цикл класса Play.
    Проверяет, что игровой цикл корректно обрабатывает игровые события.
    """
    mock_screen = MagicMock()
    play = Play(snake_body_fill='*', apple_fill='@')
    with patch.object(play, '_Play__condictions_to_lose', return_value=True):
        play._Play__loop(mock_screen)
        mock_screen.refresh.assert_called()


@patch('Game.curses')
def test_play_load_content(mock_curses: MagicMock) -> None:
    """
    Тестирует загрузку начального содержимого игры.
    Проверяет, что создаются начальные элементы игры, такие как змея и яблоко.
    """
    mock_screen = MagicMock()
    play = Play(snake_body_fill='*', apple_fill='@')
    play._Play__load_content(mock_screen)


@patch('Game.curses')
def test_play_get_new_direction(mock_curses: MagicMock) -> None:
    """
    Тестирует изменение направления движения в игре.
    Проверяет, что направление движения изменяется в ответ на пользовательский ввод.
    """
    mock_screen = MagicMock()
    play = Play(snake_body_fill='*', apple_fill='@')
    mock_screen.getch.return_value = mock_curses.KEY_RIGHT
    play._Play__get_new_direction(mock_screen, "left")