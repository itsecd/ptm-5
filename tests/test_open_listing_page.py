import pytest
import sys
from unittest import mock
from unittest.mock import patch

# @pytest.fixture
# def fixture():
sys.modules['mediafile'] = mock.Mock()
sys.modules['cmdline'] = mock.Mock()
import bbc_tracklist

@patch('lxml.html.fromstring')
@patch('bbc_tracklist.requests.get')
def test_open_listing_page(mock_get, mock_html_to_lxml):
    html_content = "<html></html>"
    mock_get.return_value = html_content
    result = mock_get("some_val")
    
    assert result == html_content
    mock_get.assert_called_with("some_val")

    result = "<lxml></lxml>"
    # mock_html_to_lxml = mock.Mock()
    mock_html_to_lxml.return_value = result
    html_to_lxml = mock_html_to_lxml(mock_get.return_value)
    assert result == html_to_lxml
    mock_html_to_lxml.assert_called_with(mock_get.return_value)
    