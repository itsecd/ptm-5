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

def test_find_intersection(calc):
    assert (float(1), float(2)) == calc.find_intersection(2,0,1,1)
    assert "Линии совпадают" == calc.find_intersection(4,6,4,6)
    assert "Линии параллельны и не пересекаются" == calc.find_intersection(4,6,4,20)


def test_find_find_parabolas_intersection(calc):
    assert [(0.618, 2.382),(-1.618, 4.618)] == calc.find_parabolas_intersection(2,1,1,1,0,2)
    assert [(1.207, 10.7), (-0.207, 0.8)] == calc.find_parabolas_intersection(5,2,1,1,6,2)
    assert 'Параболы не пересекаются' == calc.find_parabolas_intersection(3,5,6,-3,-5,1)