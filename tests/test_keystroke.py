import pytest
from unittest.mock import patch, MagicMock
import main

@pytest.fixture
def mock_win32con():
    with patch('main.win32con', new=MagicMock()) as mock_con:
        mock_con.WM_CHAR = 'WM_CHAR'
        yield mock_con

@pytest.fixture
def mock_win32api():
    with patch('main.win32api', new=MagicMock()) as mock_api:
        yield mock_api

@pytest.fixture
def mock_afk_clicker(mock_win32api):
    afk_clicker = main.Afk_Clicker(keyboard_key=0x41)
    afk_clicker.get_child_hwnd = MagicMock(return_value=12345)
    return afk_clicker

def test_keystroke(mock_afk_clicker, mock_win32api, mock_win32con):
    parent_hwnd = 67890
    mock_afk_clicker.keystroke(parent_hwnd)
    mock_win32api.PostMessage.assert_called_once_with(12345, mock_win32con.WM_CHAR, 0x41, 0)