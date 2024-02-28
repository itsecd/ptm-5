from math import sqrt
from typing import Tuple, Union    
import sympy

def square_eq_solver(a: int, b: int, c: int) -> Union[str, Tuple[float, float]]:
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.

    Args:
        a (int): Coefficient of x^2
        b (int): Coefficient of x
        c (int): Constant term

    Returns:
    Union[str, Tuple[float, float]]: 
        If real roots exist, returns a tuple of roots.
        If no real roots exist, returns a message as a string.
    """
    if a == 0:
        if b != 0:
            return (-c / b,)
        else:
            return "No real roots"
    else:
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            root1 = (-b + discriminant ** 0.5) / (2 * a)
            root2 = (-b - discriminant ** 0.5) / (2 * a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2 * a)
            return (root,)
        else:
            return "No real roots"

def derivatives(x: sympy.Symbol, y: sympy.Symbol, expr: sympy.Expr) -> Tuple[sympy.Expr, sympy.Expr]:
    """
    Calculates the partial derivatives of an expression with respect to x and y.

    Args:
        x: Symbol for differentiation with respect to x
        y: Symbol for differentiation with respect to y
        expr: Expression to differentiate

    Returns:
        Tuple[derivative with respect to x, derivative with respect to y]
    """
    df_dx = sympy.diff(expr, x)
    df_dy = sympy.diff(expr, y)
    print("Частная производная от выражения по x:", df_dx)
    print("Частная производная от выражения по y:", df_dy)
    return df_dx, df_dy

def indefinite_integral(expr: sympy.Expr) -> sympy.Expr:
    """
    Computes the indefinite integral of an expression with respect to x.

    Args:
        expr: Expression to integrate

    Returns:
        Indefinite integral of the expression
    """
    x = sympy.symbols('x')
    return sympy.integrate(expr)

def price(a: int, b: float, c: float) -> Tuple[float, float]:
    """
    Calculates two prices based on given coefficients.

    Args:
        a (int): Coefficient 1
        b (float): Coefficient 2
        c (float): Coefficient 3

    Returns:
        Tuple of two prices
    """
    p1 = round(b * c, 1)
    p2 = a * c
    return p1, p2

def commission(a: float, b: float, p1: float, p2: float) -> Tuple[float, float, float]:
    """
    Computes three components of a commission based on given prices and coefficients.

    Args:
        a (float): Coefficient 1
        b (float): Coefficient 2
        p1 (float): Price 1
        p2 (float): Price 2

    Returns:
        Tuple of commission components
    """
    c1 = p1 * b
    c2 = p2 * b
    c3 = (p1 - p2) * 0.13
    return c1, c2, c3

def trapezoid_area(height: float, base_1: float, base_2: float) -> float:
    """
    Calculates the area of a trapezoid given its height and the lengths of two bases.

    Args:
        height (float): Height of the trapezoid
        base_1 (float): Length of the first base
        base_2 (float): Length of the second base

    Returns:
        Area of the trapezoid
    """
    area = ((base_1 + base_2) * height) / 2
    print('Площадь трапеции: ', area)
    return area

def info() -> None:
    print("1. Вычисление корня квадратного уравнения\n"
          "2. Вычисление частной производной\n"
          "3. Вычисление неопределённого интеграла\n"
          "4. Вычисление цены\n"
          "5. Вычисление комиссии\n"
          "6. Вычисление площади трапеции\n")


def main() -> None:
    info()
    action = input('Введите номер действия: ')
    match(action):
        case('1'):
            a, b, c = map(int, input('Пожалуйста, введите три числа через пробел: ').split())
            result1 = square_eq_solver(a, b, c)
        case('2'):
            x, y = sympy.symbols('x y')
            expr = input('Введите уравнение: ')
            result2 = derivatives(x, y, expr)
        case('3'):
            x = sympy.symbols('x')
            expr = input('Введите уравнение: ')
            result3 = indefinite_integral(x, expr)
        case('4'):
            pricesale = float(input('Введите цену продажи:'))
            p1, p2 = price(1807, pricesale, 6)
            print(p1, p2)
        case('5'):
            pricesale = float(input('Введите цену продажи:'))
            p1, p2 = price(1807, pricesale, 6)
            c1, c2, c3 = commission(0.13, 0.000725, p1, p2)
            print(c1, c2, c3)
        case('6'):
            height = float(input("Height of trapezoid: "))
            base1 = float(input('Base one value: '))
            base1 = float(input('Base two value: '))
            result4 = trapezoid_area(height, base1, base1)


if __name__ == '__main__':
   main()