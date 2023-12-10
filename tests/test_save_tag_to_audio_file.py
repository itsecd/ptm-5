import pytest
import sys
from unittest import mock
from unittest.mock import patch

sys.modules['mediafile'] = mock.Mock()
sys.modules['cmdline'] = mock.Mock()
import bbc_tracklist

# @pytest.mark.parametrize(0, 1, 2)
# @patch('bbc_tracklist.mediafile.MediaFile')
@pytest.mark.parametrize("scenario, new_tracklisting, should_raise_error", [
    (0, 'Track1', False),
    (1, 'Track1', False),
    (2, 'Track1', True),
])
@patch('bbc_tracklist.mediafile.MediaFile')
def test_save_tag_to_audio_file(mock_mediafile, scenario, new_tracklisting, should_raise_error):
    # mock_mediafile = mock.Mock()
    if scenario == 0:
        mock_mediafile.lyrics = None
    elif scenario == 1:
        mock_mediafile.lyrics = 'Existing Lyrics'
    elif scenario == 2:
        mock_mediafile.lyrics = 'Tracklisting' + new_tracklisting

    mock_mediafile.return_value = mock_mediafile

    audio_file = 'test_audio.mp3'

    if should_raise_error:
        with pytest.raises(bbc_tracklist.TagNotNeededError):
            bbc_tracklist.save_tag_to_audio_file(audio_file, new_tracklisting)
    elif scenario == 1:
        assert mock_mediafile.lyrics + new_tracklisting == 'Existing Lyrics' + new_tracklisting
    elif scenario == 0:
        assert mock_mediafile.lyrics is None
        mock_mediafile.lyrics = new_tracklisting
        assert mock_mediafile.lyrics == 'Track1'
    #     expected_lyrics = 'exist'
    #     bbc_tracklist.save_tag_to_audio_file(audio_file, new_tracklisting)
    #     assert mock_mediafile.lyrics == expected_lyrics
    #     mock_mediafile.save.assert_called_once()
    # else:
    #     pass
