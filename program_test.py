import pytest
import os
import json
from BIN_and_statistic import check_hash, find_number, luhn_algo, make_statistic
from read import read_settings


@pytest.mark.parametrize("path", ["data/settings.json, sdgdss"])
def test_read_settings(path):
    with pytest.raises(Exception):
        read_settings(path)


def test_check_hash():
    result = \
        check_hash({"last_digits": "9920",
                    "hash":
                    "78495810cec383f3f82049d03a522f5141583d1d6577235c74084c1d21f7a1df4612c05c0d6b5eb15edd1270ab5069f0"},
                   220070, 785612)
    assert result == 2200707856129920


def test_luhn_algo():
    result = luhn_algo({"save_path": "data/card_data.json"})
    assert not result


def test_find_number():
    settings = {"hash":
                "78495810cec383f3f82049d03a522f5141583d1d6577235c74084c1d21f7a1df4612c05c0d6b5eb15edd1270ab5069f0",
                "first_digits": "220070", "last_digits": "9920", "save_path": "test/card_data.json"}
    find_number(settings, 6)
    with open(settings["save_path"]) as json_file:
        data = json.load(json_file)
    assert data["card_number"] == "2200707856129920"


@pytest.fixture
def clean_json():
    if os.path.isfile("test/card_data.json"):
        os.remove("test/card_data.json")
    yield


def test_make_statistic():
    settings = {"hash":
                "78495810cec383f3f82049d03a522f5141583d1d6577235c74084c1d21f7a1df4612c05c0d6b5eb15edd1270ab5069f0",
                "first_digits": "220070", "last_digits": "9920", "save_path": "test/card_data.json",
                "thread_number": "12",
                "pic_path": "test/picture.png"}
    make_statistic(settings)
    with open(settings["save_path"]) as json_file:
        data = json.load(json_file)
    assert data["card_number"] == "2200707856129920"
    assert os.path.isfile(settings["pic_path"])


@pytest.fixture
def clean_json_and_pic():
    if os.path.isfile("test/card_data.json"):
        os.remove("test/card_data.json")
    if os.path.isfile("test/picture.png"):
        os.remove("test/picture.png")
    yield

