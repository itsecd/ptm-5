import pytest
from unittest.mock import patch, MagicMock
import main

@pytest.fixture
def mock_win32gui():
    with patch('main.win32gui', new=MagicMock()) as mock_gui:
        yield mock_gui

def test_get_child_hwnd(mock_win32gui):
    parent_hwnd = 12345
    expected_child_hwnd = 67890
    mock_win32gui.GetWindow.return_value = expected_child_hwnd

    afk_clicker = main.Afk_Clicker()

    child_hwnd = afk_clicker.get_child_hwnd(parent_hwnd)
    assert child_hwnd == expected_child_hwnd
    mock_win32gui.GetWindow.assert_called_with(parent_hwnd, main.win32con.GW_CHILD)