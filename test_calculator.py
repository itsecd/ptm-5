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
    assert calc.sin(math.pi / 2) == 1
    assert calc.cos(math.pi) == -1
    assert calc.tan(math.pi / 4) == 1
    assert calc.cot(math.pi / 4) == 1

def test_derivative(calc):
    assert calc.derivative(lambda x: x**2, 2) == pytest.approx(4.0, 0.01)

def test_integral(calc):
    assert calc.integral(lambda x: x, 0, 1) == pytest.approx(0.5, 0.01)

def test_find_intersection(calc):
    assert 0.5 in calc.find_intersection(lambda x: 2*x, lambda x: x + 1, 0, 1)