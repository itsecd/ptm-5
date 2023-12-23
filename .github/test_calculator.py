import pytest
from main import add, subtract, multiply, divide, power, calculate_rectangle_area


def test_add():
    assert add(4, 99) == 103
    assert add(-1, 1) == 0
    assert add(-100, -99) == -199


def test_subtract():
    assert subtract(4, 99) == -95
    assert subtract(-1, 1) == -2
    assert subtract(-100, -99) == 1


def test_multiply():
    assert multiply(4, 50) == 200
    assert multiply(-1, 1) == -1
    assert multiply(-100, 2) == -200


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_power():
    assert power(4, 2) == 16
    assert power(1, 2) == 1
    assert power(9, 1/2) == 3


def test_calculate_rectangle_area():
    assert calculate_rectangle_area(1, 2) == 2
    assert calculate_rectangle_area(5, 5) == 25
    assert calculate_rectangle_area(10, 10) == 100


@pytest.mark.parametrize("a, b, expected", [(1, -2, -1), (4, 5, 9), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (4, 5, 20), (0, 0, 0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, -2, 3), (10, 5, 5), (0, 0, 0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 1, 2), (10, 5, 2), (1, -1, -1)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 1, 2), (10, 2, 100), (4, 1/2, 2)])
def test_power(a, b, expected):
    assert power(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 1, 2), (10, 20, 200), (4, 1/2, 2)])
def test_calculate_rectangle_area(a, b, expected):
    assert calculate_rectangle_area(a, b) == expected
