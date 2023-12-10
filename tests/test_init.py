import pytest
import main
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_win32con():
    with patch('main.win32con', new=MagicMock()) as mock_win32con:
        mock_win32con.MK_LBUTTON = 'MK_LBUTTON'
        mock_win32con.WM_LBUTTONUP = 'WM_LBUTTONUP'
        mock_win32con.WM_LBUTTONDOWN = 'WM_LBUTTONDOWN'
        mock_win32con.MK_RBUTTON = 'MK_RBUTTON'
        mock_win32con.WM_RBUTTONUP = 'WM_RBUTTONUP'
        mock_win32con.WM_RBUTTONDOWN = 'WM_RBUTTONDOWN'
        yield mock_win32con

@pytest.mark.parametrize("mouse_btn, expected_values", [
    (1, ('MK_LBUTTON', 'WM_LBUTTONUP', 'WM_LBUTTONDOWN')),
    (2, ('MK_RBUTTON', 'WM_RBUTTONUP', 'WM_RBUTTONDOWN')),
    (0, (0, 0, 0)),
    ])
def test_init(mouse_btn, expected_values, mock_win32con):
    clicker = main.Afk_Clicker(mouse_btn=mouse_btn)
    assert clicker.mouse_btn == expected_values[0]
    assert clicker.mouse_btn_up == expected_values[1]
    assert clicker.mouse_btn_dn == expected_values[2]