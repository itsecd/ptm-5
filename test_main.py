import pytest
from sympy import symbols

from main import (square_eq_solver, derivatives, indefinite_integral,
                   price, commission, trapezoid_area)

def test_square_eq_solver():
    assert square_eq_solver(10, 0, 0) == (0.0, 0.0)
    assert square_eq_solver(2, 5, -3) == (0.5, -3.0)
    assert square_eq_solver(10, 0, 2) == "No real roots"

def test_derivatives():
    x, y = symbols('x y')
    assert derivatives(x, y, '32*x - y') == (32, -1)
    assert derivatives(x, y, '32 - 1') == (0, 0)
    assert derivatives(x, y, '32 * x**2 - y**2') == (64*x, -2*y)

def test_indefinite_integral():
    x = symbols('x')
    assert indefinite_integral(x, '32*x - 1') == '16*x**2 - x'
    assert indefinite_integral(x, '1/sqrt(x)') == '2*sqrt(x)'
    assert indefinite_integral(x, 'sin(x)') == '-cos(x)'

def test_price():
    assert price(1807, 2, 6) == (12.0, 10842)
    assert price(1807, 20, 6) == (120.0, 10842)
    assert price(1807, 200, 6) == (1200.0, 10842)

def test_commission():
    assert commission(0.13, 0.000725, 12.0, 10842) == (0.0087, 7.860449999999999, -1407.9)
    assert commission(0.13, 0.000725, 120.0, 10842) == (0.087, 7.860449999999999, -1393.8600000000001)
    assert commission(0.13, 0.000725, 1200.0, 10842) == (0.8699999999999999, 7.860449999999999, -1253.46)

def test_trapezoid_area():
    assert trapezoid_area(0, 0, 0) == 0.0
    assert trapezoid_area(5, 0, -5) == 25.0
    assert trapezoid_area(-4, -3, 2) == 8.0

@pytest.mark.parametrize("a, b, c, expected", [(0, 1, 1, -1), (2, 1, 0, (-0.5, 0)), (3, 0, -27, (-3, 3))])
def test_square_eq_solver_param(a, b, c, expected):
    assert square_eq_solver(a, b, c) == expected

@pytest.mark.parametrize("x, y, expr, expected", [('x', 'y', '5 * x**2 - 3 * y', (32, -3)), ('x', 'y', '18 + 332', (0, 0)), ('x', 'y', '182 * x', (182, 0))])
def test_derivatives_param(x, y, expr, expected):
    assert derivatives(x, y, expr) == expected

@pytest.mark.parametrize("expr, expected", [('cos(x)', 'sin(x)'), ('x - 1', 'x**2 - x'), ('sqrt(x)', '2*sqrt(x)')])
def test_indefinite_integral_param(expr, expected):
    assert indefinite_integral(expr) == expected

@pytest.mark.parametrize("a, b, c, expected", [(1807, 13, 6, (78.0, 10842)), (1807, 5, 6, (30.0, 10842)), (1807, 148, 6, (888.0, 10842))])
def test_price_param(a, b, c, expected):
    assert price(a, b, c) == expected

@pytest.mark.parametrize("a, b, c, d, expected", [(0.13, 0.000725, 78.0, 10842, (0.056549999999999996, 7.860449999999999, -1399.32)),
                                                   (0.13, 0.000725, 30.0, 10842, (0.02175, 7.860449999999999, -1405.56)),
                                                     (0.13, 0.000725, 888.0, 10842, (0.6437999999999999, 7.860449999999999, -1294.02))])
def test_commission_param(a, b, c, d, expected):
    assert commission(a, b, c, d) == expected

@pytest.mark.parametrize("a, b, c, expected", [(0, 1, 0, 0.0), (32, 2, 3, 80.0), (18, 18, 18, 324.0)])
def test_trapezoid_area_param(a, b, c, expected):
    assert trapezoid_area(a, b, c) == expected
