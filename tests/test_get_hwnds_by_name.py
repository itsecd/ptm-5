import pytest
from unittest.mock import patch, MagicMock
import main

@pytest.fixture
def mock_win32gui():
    with patch('main.win32gui', new=MagicMock()) as mock_gui:
        yield mock_gui

def test_get_hwnds_by_name(mock_win32gui):
    expected_hwnd = 12345
    window_name = "test_name"

    mock_win32gui.FindWindow.side_effect = lambda class_name, window_name_param: expected_hwnd if window_name_param == window_name else 0

    afk_clicker = main.Afk_Clicker()
    hwnd_result = afk_clicker.get_hwnds_by_name(window_name)
    assert hwnd_result == expected_hwnd
    hwnd_result_not_found = afk_clicker.get_hwnds_by_name("wrong_window")
    assert hwnd_result_not_found == 0