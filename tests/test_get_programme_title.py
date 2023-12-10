import pytest
import sys
from unittest import mock
from unittest.mock import patch

sys.modules['mediafile'] = mock.Mock()
sys.modules['cmdline'] = mock.Mock()
import bbc_tracklist

@patch('bbc_tracklist.open_listing_page')
def test_get_programme_title(mock_open_listing_page):
    # mock_etree = mock.Mock()
    # mock_etree.xpath.return_value = "Test Programme Title"
    expected_main_page_etree = "some_title"
    mock_open_listing_page.return_value = "some_title"
    result = mock_open_listing_page('some_id')
    assert expected_main_page_etree == result

@patch('bbc_tracklist.open_listing_page')
def test_empty_xpath_result_returns_empty_title(mock_open):
    mock_etree = mock.Mock()
    mock_etree.xpath.return_value = []
    mock_open.return_value = mock_etree

    title = bbc_tracklist.get_programme_title('some_pid')

    assert title == ''
