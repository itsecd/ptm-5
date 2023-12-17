import pytest
import os
import json
import statistics as st
import scipy.stats as sts
import numpy as np
from BIN_and_statistic import check_hash, find_number, luhn_algo, make_statistic
from read import read_settings
from sample_stats import find_expectation_inter, find_expectation_inter_no_dis, find_emp_gamma


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


@pytest.mark.parametrize("settings, expected_result", [({"save_path": "data/card_data.json"}, False),
                                                       ({"save_path": "test/test_card.json"}, True)])
def test_luhn_algo(settings, expected_result):
    assert luhn_algo(settings) == expected_result


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


@pytest.mark.parametrize("a, sigma2, gamma, n, accuracy", [(10.0, 4, 0.95, 20, 0.0000001),
                                                           (2.0, 1.22, 0.90, 35, 0.0000001),
                                                           (100, 25, 0.99, 40, 0.0000001)])
def test_find_expectation_inter(a, sigma2, gamma, n, accuracy):
    test_sample = np.random.normal(loc=a, scale=np.sqrt(sigma2), size=n)
    left, right = find_expectation_inter(test_sample, gamma, np.sqrt(sigma2))
    expected_left, expected_right = sts.norm.interval(gamma, loc=test_sample.mean(), scale=np.sqrt(sigma2)/np.sqrt(n))
    assert abs(left - expected_left) < accuracy
    assert abs(right - expected_right) < accuracy


@pytest.mark.parametrize("a, sigma2, gamma, n, accuracy", [(10.0, 4, 0.95, 20, 0.0000001),
                                                           (2.0, 1.22, 0.90, 35, 0.0000001),
                                                           (100, 25, 0.99, 40, 0.0000001)])
def test_find_expectation_inter_no_dis(a, sigma2, gamma, n, accuracy):
    test_sample = np.random.normal(loc=a, scale=np.sqrt(sigma2), size=n)
    left, right = find_expectation_inter_no_dis(test_sample, gamma)
    expected_left, expected_right =\
        sts.t.interval(gamma, df=n - 1, loc=test_sample.mean(), scale=np.sqrt(st.pvariance(test_sample)) / np.sqrt(n))
    assert abs(left - expected_left) < accuracy
    assert abs(right - expected_right) < accuracy


@pytest.mark.parametrize("m, a, sigma2, gamma, n, deviation", [(20, 10.0, 4, 0.95, 20, 0.7),
                                                               (30, 2.0, 1.22, 0.90, 35, 0.7),
                                                               (40, 100, 25, 0.99, 40, 0.7)])
def test_find_emp_gamma(m, a, sigma2, gamma, n, deviation):
    gamma_emp = find_emp_gamma(m, a, sigma2, n, gamma)
    assert abs(gamma_emp - gamma) < deviation
