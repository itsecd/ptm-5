import pytest
from unittest.mock import patch, MagicMock
import sympy
from main import (square_eq_solver, derivatives, price,
                  commission, indefinite_integral, trapezoid_area)


@pytest.mark.parametrize("a, b, c, expected", [
    (1, -3, 2, (2.0, 1.0)),
    (1, -2, 1, (1.0,)),
    (1, 1, 1, "No real roots")
])
def test_square_eq_solver_parametrized(a, b, c, expected):
    assert square_eq_solver(a, b, c) == expected
   
    
def test_derivatives_with_mocks():
    x, y = sympy.symbols('x y')

    mock_diff_x = MagicMock()
    mock_diff_y = MagicMock()

    with patch('main.sympy.diff') as mock_diff:
        mock_diff.side_effect = [mock_diff_x, mock_diff_y]

        expr = x**2 + y**3
        df_dx, df_dy = derivatives(x, y, expr)

        mock_diff.assert_any_call(expr, x)
        mock_diff.assert_any_call(expr, y)

        assert df_dx == mock_diff_x
        assert df_dy == mock_diff_y
    
     
@pytest.mark.parametrize("a, b, c, expected_output", [
    (2, 3.5, 4, (14.0, 8)),
    (0, 5.5, 10, (55.0, 0)),
    (3, 2.1, 7, (14.7, 21))
])
def test_price_calculation(a, b, c, expected_output):
    assert price(a, b, c) == expected_output
    
    
def commission_test():
    p1, p2 = 10842.0, 18.0
    c1, c2, c3 = commission(0.13, 0.000725, p1, p2)
    assert (c1, c2, round(c3, 2)) == (234.0, 144342, 107552.81)
    
    
def test_indefinite_integral():
    x = sympy.symbols('x')
    expr = 2*x
    expected_result = x**2

    result = indefinite_integral(expr)

    assert result == expected_result, f"Expected: {expected_result}, Got: {result}"
    
    
def test_trapezoid_area():
    assert trapezoid_area(5, 3, 7) == 25.0
 
   
@pytest.mark.parametrize("height, base_1, base_2, expected_result",
                         [(5, 3, 7, 25.0),
                          (2, 4, 6, 10.0),
                          (8, 5, 3, 32.0)])
def test_param_trapezoid_area(height, base_1, base_2, expected_result):
    assert trapezoid_area(height, base_1, base_2) == expected_result
    