import pytest
from calculator import Calculator
import math


@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(3, 4) == 7

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12

def test_solve_quadratic(calc):
    assert calc.solve_quadratic(1, -5, 6) == (3.0, 2.0)

def test_logarithm(calc):
    assert calc.logarithm(math.e, math.e) == 1

def test_trigonometry(calc):
    assert 0.99999 <= calc.sin(math.pi / 2) <= 1.0000000000000002
    assert calc.cos(math.pi) == -1
    assert 0.99999 <= calc.tan(math.pi / 4) <= 1.0000000000000002
    assert 0.99999 <= calc.cot(math.pi / 4) <= 1.0000000000000002

def test_derivative(calc):
    assert calc.derivative(lambda x: x**2, 2) == pytest.approx(4.0, 0.01)

def test_integral(calc):
    assert calc.integral(lambda x: x, 0, 1) == pytest.approx(0.5, 0.01)

@pytest.mark.parametrize(
        "a,b,c,d, expected",[
            (2, 0, 1, 1, (float(1), float(2))),
            (4, 6, 4, 6, "Линии совпадают"),
            (4, 6, 4, 20, "Линии параллельны и не пересекаются")
        ])
def test_find_intersection(calc,a, b, c, d, expected):
    assert calc.find_intersection(a,b,c,d) == expected

@pytest.mark.parametrize(
    "a, b, c, d, e, f, expected",
    [

        (1, 0, 0, 1, 0, 1, "Параболы не пересекаются"),

        (1, 0, 0, 1, 0, 0, "Параболы совпадают"),

        (2, 1, 1, 1, 0, 2, [(0.618, 2.382), (-1.618, 4.618)]),

        (5, 2, 1, 1, 6, 2, [(1.207, 10.7), (-0.207, 0.8)]),

        (5, 2, 1, 1, 6, 2, [(1.207, 10.7), (-0.207, 0.8)])
    ]
)
def test_find_parabolas_intersection(calc,a, b, c, d, e, f, expected):
    assert calc.find_parabolas_intersection(a, b, c, d, e, f) == expected
