import json
import pytest
import tempfile

from laba1 import (parse_data, change_years, day_num_to_str,
                   month_num_to_str, check_month, change_months, load_settings)


@pytest.mark.parametrize("url, years, expected_url", [
    ("https://www.gismeteo.ru/diary/4618/2008/1/", 2009,
     "https://www.gismeteo.ru/diary/4618/2009/1/"),
    ("https://www.gismeteo.ru/diary/4618/2010/1/", 2011,
     "https://www.gismeteo.ru/diary/4618/2011/1/")
])
def test_change_years(years, url, expected_url):
    result = change_years(years, url)
    assert result == expected_url


@pytest.mark.parametrize("input_day, expected_day", [
    (4, "04"),
    (10, "10"),
])
def test_redact_days(input_day, expected_day):
    result = day_num_to_str([str(input_day)])
    assert result == expected_day


@pytest.mark.parametrize("input_month, expected_month", [
    (4, "04"),
    (10, "10"),
])
def test_redact_month(input_month, expected_month):
    result = month_num_to_str(input_month)
    assert result == expected_month


@pytest.mark.parametrize("url, expected_month", [
    ("https://www.gismeteo.ru/diary/4618/2008/1/", 12),
    ("https://www.gismeteo.ru/diary/4618/2015/1/", 12)
])
def test_check_month(url, expected_month):
    result = check_month(url)
    assert result == expected_month


@pytest.mark.parametrize("url, month, change_type, expected_url", [
    ("https://www.gismeteo.ru/diary/4618/2008/12/", 12,
     1, "https://www.gismeteo.ru/diary/4618/2008/12/"),
    ("https://www.gismeteo.ru/diary/4618/2008/8/", 9,
     2, "https://www.gismeteo.ru/diary/4618/2008/1/")
])
def test_change_months(url, month, change_type, expected_url):
    result = change_months(url, month, change_type)
    assert result == expected_url


@pytest.fixture
def temporary_settings_file():
    data = {"url": "https://www.gismeteo.ru/diary/4618/2008/1/",
            "year": 2008}
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(json.dumps(data))
        return temp_file.name


def test_load_settings(temporary_settings_file):
    url, year = load_settings(temporary_settings_file)
    assert url == "https://www.gismeteo.ru/diary/4618/2008/1/"
    assert year == 2008


def test_parse_data():
    url = "https://www.gismeteo.ru/diary/4618/2008/1/"
    year = 2008
    result = parse_data(url, year)
    assert result == "https://www.gismeteo.ru/diary/4618/2023/1/"
