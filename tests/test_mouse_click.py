import pytest
from unittest.mock import MagicMock
import main

@pytest.fixture
def mock_pycwnd():
    pycwnd = MagicMock()
    pycwnd.SendMessage = MagicMock()
    pycwnd.UpdateWindow = MagicMock()
    return pycwnd

@pytest.mark.parametrize("mouse_btn", [1, 2])
def test_mouse_click(mock_pycwnd, mouse_btn):
    clicker = main.Afk_Clicker(mouse_btn=mouse_btn)
    mock_pycwnd = MagicMock()

    clicker.mouse_click(mock_pycwnd)
    x = 300
    y = 300
    lParam = y << 15 | x
    mock_pycwnd.SendMessage.assert_any_call(clicker.mouse_btn_dn, clicker.mouse_btn, lParam)
    mock_pycwnd.SendMessage.assert_any_call(clicker.mouse_btn_up, 0, lParam)
    mock_pycwnd.UpdateWindow.assert_called_once()