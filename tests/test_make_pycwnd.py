import pytest
from unittest.mock import patch, MagicMock
import main

@pytest.fixture
def mock_win32ui():
    with patch('main.win32ui', new=MagicMock()) as mock_ui:
        mock_ui.CreateWindowFromHandle = MagicMock()
        yield mock_ui

def test_make_pycwnd(mock_win32ui):
    hwnd = 12345
    expected_pycwnd = MagicMock()
    mock_win32ui.CreateWindowFromHandle.return_value = expected_pycwnd

    afk_clicker = main.Afk_Clicker()
    result_pycwnd = afk_clicker.make_pycwnd(hwnd)
    assert result_pycwnd == expected_pycwnd
    mock_win32ui.CreateWindowFromHandle.assert_called_once_with(hwnd)