import pytest
from main import add, subtract, multiply, divide, modulo, integer_division, power, calculate_triangle_area, \
    calculate_circle_area, calculate_rectangle_area


#Тесты для базовых математических операций
def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1


def test_divide():
    assert divide(10, 5) == 2
    assert divide(-1, 1) == -1
    with pytest.raises(ValueError):
        divide(10, 0)


def test_integer_division():
    assert integer_division(10, 5) == 2
    assert integer_division(10, 3) == 3
    with pytest.raises(ValueError):
        integer_division(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 3) == -8


#Тесты для математических операций
@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-2, -3, -5), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (-2, -3, 1), (0, 0, 0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (-2, -3, 6), (0, 0, 0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (-6, 3, -2)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(6, 0)


@pytest.mark.parametrize("a, b, expected", [(7, 3, 2), (-7, 3, -3)])
def test_integer_division(a, b, expected):
    assert integer_division(a, b) == expected


def test_integer_division_by_zero():
    with pytest.raises(ValueError):
        integer_division(7, 0)


@pytest.mark.parametrize("a, b, expected", [(2, 3, 8), (-2, 3, -8)])
def test_power(a, b, expected):
    assert power(a, b) == expected


#Тест для расчета площади фигуры
@pytest.mark.parametrize("a, b, c, expected", [(3, 4, 5, 6.0), (6, 8, 10, 24.0)])
def test_calculate_triangle_area(a, b, c, expected):
    assert calculate_triangle_area(a, b, c) == expected

