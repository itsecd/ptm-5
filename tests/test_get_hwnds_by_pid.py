import pytest
import main
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_win32gui():
    with patch('main.win32gui', new=MagicMock()) as mock_gui:
        yield mock_gui

@pytest.fixture
def mock_win32process():
    with patch('main.win32process', new=MagicMock()) as mock_process:
        yield mock_process

def test_get_hwnds_by_pid(mock_win32gui, mock_win32process):
    mock_win32gui.IsWindowVisible.return_value = True
    mock_win32gui.IsWindowEnabled.return_value = True
    mock_win32process.GetWindowThreadProcessId.side_effect = lambda hwnd: (None, 12345) if hwnd == 'hwnd1' else (None, 54321)

    afk_clicker = main.Afk_Clicker()

    def enum_windows(callback, hwnds):
        callback('hwnd1', hwnds)
        callback('hwnd2', hwnds)

    mock_win32gui.EnumWindows.side_effect = enum_windows
    hwnds = afk_clicker.get_hwnds_by_pid(12345)
    assert 'hwnd1' in hwnds
    assert 'hwnd2' not in hwnds