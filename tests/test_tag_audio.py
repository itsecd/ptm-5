import pytest
import sys
from unittest import mock
from unittest.mock import patch

sys.modules['mediafile'] = mock.Mock()
sys.modules['cmdline'] = mock.Mock()
import bbc_tracklist

@patch('bbc_tracklist.tag_audio')
@patch('bbc_tracklist.write_text')
@pytest.mark.parametrize("action", ['text', 'tag', 'both'])
def test_output_to_file(mock_write_text, mock_tag_audio, action):
    filename = 'test_filename'
    tracklisting = 'Test_tracklisting'

    if action == 'text':
        bbc_tracklist.output_to_file(filename, tracklisting, action)
        mock_write_text.assert_called_once_with(filename, tracklisting)
        mock_tag_audio.assert_not_called()

    elif action == 'tag':
        bbc_tracklist.output_to_file(filename, tracklisting, action)
        mock_tag_audio.assert_called_once_with(filename, tracklisting)
        mock_write_text.assert_not_called()

    elif action == 'both':
        bbc_tracklist.output_to_file(filename, tracklisting, action)
        mock_tag_audio.assert_called_once_with(filename, tracklisting)
        mock_write_text.assert_called_once_with(filename, tracklisting)
