import os
import pytest

from card import check_hash, luhn, reverse_number
from load_write import load_settings, read_file, write_file
from stats import load_stats, write_stats


@pytest.mark.parametrize("path", ["test_files/test_settings.json", 55])
def test_load_stats_exceptions(path):
    with pytest.raises(Exception):
        load_stats(path)


@pytest.mark.parametrize("path", ["test_files/test_settings.json", 55])
def test_write_stats_exceptions(path):
    with pytest.raises(Exception):
        write_stats(path)


def test_load_stats():
    path = "test_files/stats_test.csv"
    result = load_stats(path)
    assert result == {
        1: 37.86729431152344,
        2: 24.54872226715088,
        3: 20.36780571937561,
        4: 21.03993844985962,
        5: 21.382314682006836,
    }


@pytest.fixture
def clean_stats_file():
    if os.path.isfile("test_files/write_stats_test.csv"):
        os.remove("test_files/write_stats_test.csv")
    yield


def test_write_stats(clean_stats_file):
    path = "test_files/write_stats_test.csv"
    write_stats(5, 13.3892, path)
    assert load_stats(path) == {5: 13.3892}


def test_load_settings():
    path = "test_files/test_settings.json"
    result = load_settings(path)
    assert result == {
        "hash": "4006234246b4fd2b2",
        "last_numbers": "0254",
        "bins": [510126, 519778],
        "card_number": "data/card_number.txt",
        "stats": "data/stats.csv",
        "graph": "data/graph.jpg",
    }


def test_read_file():
    path = "test_files/test_read.txt"
    result = read_file(path)
    assert result == "5559 Luhn algorithm: false"


@pytest.fixture
def clean_txt_file():
    if os.path.isfile("test_files/test_write.txt"):
        os.remove("test_files/test_write.txt")
    yield


def test_write_file(clean_txt_file):
    path = "test_files/test_write.txt"
    write_file("2784929 hufhwicji", path)
    assert read_file(path) == "2784929 hufhwicji"


@pytest.mark.parametrize(
    "hash, card_number",
    [
        (
            "4006234246b4fd2b2833d740927ab20465afad862c74b1a88ec0869bde5c836c",
            "5559210557390254",
        ),
    ],
)
def test_check_hash(hash, card_number):
    result = check_hash(hash, card_number)
    assert result == 5559210557390254


def test_luhn():
    result = luhn("4561261212345467")
    assert result == True


@pytest.mark.parametrize(
    "number, expected_res", [(12345678, "87654321"), (479636, "636974")]
)
def test_reverse_number(number, expected_res):
    result = reverse_number(number)
    assert result == expected_res
