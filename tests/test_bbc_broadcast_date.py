import pytest
import sys
from unittest import mock
from unittest.mock import patch

sys.modules['mediafile'] = mock.Mock()
sys.modules['cmdline'] = mock.Mock()
import bbc_tracklist

@patch('bbc_tracklist.open_listing_page')
def test_get_broadcast_date(mock_open_listing_page):
    expected_date = "2023-12-10"

    mock_etree = mock.Mock()
    mock_etree.xpath.return_value = [expected_date]
    mock_open_listing_page.return_value = mock_etree

    result = bbc_tracklist.get_broadcast_date('some_pid')
    assert result == expected_date