import pytest
from main import square_root, power, factorial, add, subtract, multiply, divide, \
    quadratic_formula, calculate_hypotenuse, calculate_gcd


#Обычные тесты
def test_square_root():
    assert square_root(16) == 4
    assert square_root(625) == 25
    with pytest.raises(ValueError):
        square_root(-1)


def test_power():
    assert power(2, 3) == 8
    assert power(-2, 4) == 16
    assert power(-3, 3) == -27


def test_factorial():
    assert factorial(0) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120


def test_add():
    assert add(4, 9) == 13
    assert add(-6, 60) == 54
    assert add(-2, -4) == -6


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(9, 19) == -10
    assert subtract(6, -19) == 25


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-5, 5) == -25
    assert multiply(-7, -7) == 49


def test_divide():
    assert divide(20, 5) == 4
    assert divide(-8, 4) == -2
    with pytest.raises(ValueError):
        divide(15, 0)


#Тесты с параметризованным тестированием
@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, -5, 6, (2, 3)),
        (2, -8, 8, (2, 2)),
        (6, 8, 10, ("No real roots")),
    ]
)
def test_quadratic_formula(a, b, c, expected):
    assert quadratic_formula(a, b, c) == expected


@pytest.mark.parametrize("a, b, expected", [(3, 4, 5.0), (6, 8, 10.0)])
def test_calculate_hypotenuse(a, b, expected):
    assert calculate_hypotenuse(a, b) == expected


def test_calculate_hypotenuse_negative():
    with pytest.raises(ValueError):
        calculate_hypotenuse(5, -5)


@pytest.mark.parametrize("x, y, expected", [(8, 12, 4), (0, 5, 5)])
def test_calculate_gcd(x, y, expected):
    assert calculate_gcd(x, y) == expected


def test_calculate_gcd_both_zero():
    with pytest.raises(ValueError):
        calculate_gcd(0, 0)
