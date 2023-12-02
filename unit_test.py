import json
import tempfile

import pytest

from lab1 import (check_max_month, check_max_year, days_redact, months_redact,
                  read_settings_file, url_month_change, url_year_change)


@pytest.mark.parametrize("url, expected_year", [("https://www.gismeteo.ru/diary/4618/2008/1/", 2023)])
def test_check_max_year(url, expected_year):
    result = check_max_year(url)
    assert result == expected_year


@pytest.mark.parametrize("url, expected_month", [("https://www.gismeteo.ru/diary/4618/2008/1/", 12), ("https://www.gismeteo.ru/diary/4618/2020/3/", 12)])
def test_check_max_month(url, expected_month):
    result = check_max_month(url)
    assert result == expected_month


@pytest.mark.parametrize("url, month, change_type, expected_url", [
    ("https://www.gismeteo.ru/diary/4618/2008/12/", 12,
     1, "https://www.gismeteo.ru/diary/4618/2008/1/"),
    ("https://www.gismeteo.ru/diary/4618/2008/8/", 9,
     2, "https://www.gismeteo.ru/diary/4618/2008/9/")
])
def test_url_month_change(url, month, change_type, expected_url):
    result = url_month_change(url, month, change_type)
    assert result == expected_url


@pytest.mark.parametrize("url, years, expected_url", [
    ("https://www.gismeteo.ru/diary/4618/2008/1/", 2009,
     "https://www.gismeteo.ru/diary/4618/2009/1/")
])
def test_url_year_change(url, years, expected_url):
    result = url_year_change(url, years)
    assert result == expected_url


@pytest.mark.parametrize("input_number, expected_output", [
    (9, "09"),
    (15, "15"),
])
def test_days_redact(input_number, expected_output):
    result = days_redact([str(input_number)])
    assert result == expected_output


@pytest.mark.parametrize("input_month, expected_output", [
    (9, "09"),
    (12, "12"),
])
def test_months_redact(input_month, expected_output):
    result = months_redact(input_month)
    assert result == expected_output


@pytest.fixture
def temporary_settings_file():
    data = {"url": "https://www.gismeteo.ru/diary/4618/2008/1/",
            "year_counter": 2008}
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(json.dumps(data))
        return temp_file.name


def test_read_settings_file(temporary_settings_file):
    url, year_counter = read_settings_file(temporary_settings_file)
    assert url == "https://www.gismeteo.ru/diary/4618/2008/1/"
    assert year_counter == 2008
