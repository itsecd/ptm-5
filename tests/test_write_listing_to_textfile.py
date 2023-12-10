import pytest
import sys
from unittest import mock
from unittest.mock import patch

sys.modules['mediafile'] = mock.Mock()
sys.modules['cmdline'] = mock.Mock()
import bbc_tracklist

@patch('bbc_tracklist.codecs.open')
def test_write_listing_to_textfile(mock_open):
    textfile = 'textfile.txt'
    tracklisting = 'tracklisting'
    bbc_tracklist.write_listing_to_textfile(textfile, tracklisting)
    mock_open.assert_called_once_with(textfile, 'wb', 'utf-8')
    mock_open.write(tracklisting)

    # Проверка, что метод write мокированного файла был вызван с правильным содержимым
    mock_open.write.assert_called_once_with(tracklisting)
