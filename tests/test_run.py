import pytest
from unittest.mock import patch, MagicMock
import main

@pytest.fixture
def mock_clicker():
    with patch('main.Afk_Clicker.make_pycwnd', return_value=MagicMock()) as mock_make_pycwnd, \
         patch('main.Afk_Clicker.mouse_click') as mock_mouse_click, \
         patch('main.Afk_Clicker.keystroke') as mock_keystroke, \
         patch('main.sleep', side_effect=InterruptedError) as mock_sleep:

        yield {
            "make_pycwnd": mock_make_pycwnd,
            "mouse_click": mock_mouse_click,
            "keystroke": mock_keystroke,
            "sleep": mock_sleep
        }

def test_run(mock_clicker):
    clicker = main.Afk_Clicker(mouse_btn=1, keyboard_key=0x41)
    hwnd_main = MagicMock()
    
    with pytest.raises(InterruptedError):
        clicker.run(hwnd_main)
    
    mock_clicker["make_pycwnd"].assert_called_once_with(hwnd_main)
    mock_clicker["mouse_click"].assert_called()
    mock_clicker["keystroke"].assert_called_with(hwnd_main)
    mock_clicker["sleep"].assert_called()
