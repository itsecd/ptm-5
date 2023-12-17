from unittest.mock import patch, MagicMock
from Game import Menu


@patch('Game.curses')
def test_menu_initialization(mock_curses: MagicMock) -> None:
    """
    Тестирует правильность инициализации класса Menu.
    Проверяет, что начальный выбранный элемент (selected_item) равен 0.
    """
    menu = Menu()
    assert menu.selected_item == 0, "Начальный выбранный элемент должен быть 0"


@patch('Game.curses')
def test_menu_display(mock_curses: MagicMock) -> None:
    """
    Тестирует функциональность отображения меню.
    Проверяет, что для отображения элементов меню вызываются нужные функции.
    """
    mock_screen = MagicMock()
    menu = Menu()
    menu._Menu__show_menu(mock_screen)
    mock_screen.addstr.assert_called()


@patch('Game.curses')
def test_menu_keyboard_input(mock_curses: MagicMock) -> None:
    """
    Тестирует обработку ввода с клавиатуры в меню.
    Проверяет, что при нажатии клавиш меню реагирует соответствующим образом.
    """
    mock_screen = MagicMock()
    menu = Menu()
    mock_screen.getch.return_value = mock_curses.KEY_UP
    menu._Menu__keyboard(mock_screen)


@patch('Game.curses')
def test_menu_loop(mock_curses: MagicMock) -> None:
    """
    Тестирует игровой цикл меню.
    Проверяет, что цикл меню корректно обрабатывает ввод и обновляет экран.
    """
    mock_screen = MagicMock()
    menu = Menu()
    with patch.object(menu, '_Menu__keyboard', return_value=True):
        menu._Menu__loop(mock_screen)
        mock_screen.clear.assert_called()
        mock_screen.refresh.assert_called()
