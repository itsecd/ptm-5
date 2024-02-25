from math import sqrt
from sympy import symbols, diff, integrate
import sympy

def square_eq_solver(a, b, c):
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

def derivatives(x, y, expr):
    df_dx = diff(expr, x)
    df_dy = diff(expr, y)
    print("Частная производная от выражения по x:", df_dx)
    print("Частная производная от выражения по y:", df_dy)
    return df_dx, df_dy

def indefinite_integral(expr):
    x = sympy.symbols('x')
    return sympy.integrate(expr)

def price(a, b, c):
    p1 = round(b * c, 1)
    p2 = a * c
    return p1, p2

def commission(a, b, p1, p2):
    c1 = p1 * b
    c2 = p2 * b
    c3 = (p1 - p2) * 0.13
    return c1, c2, c3

def trapezoid_area(height, base_1, base_2):
    area = ((base_1 + base_2) * height) / 2
    print('Площадь трапеции: ', area)
    return area

def info():
    print("1. Вычисление корня квадратного уравнения\n"
          "2. Вычисление частной производной\n"
          "3. Вычисление неопределённого интеграла\n"
          "4. Вычисление цены\n"
          "5. Вычисление комиссии\n"
          "6. Вычисление площади трапеции\n")


def main():
    info()
    action = input('Введите номер действия: ')
    match(action):
        case('1'):
            a, b, c = map(int, input('Пожалуйста, введите три числа через пробел: ').split())
            result1 = square_eq_solver(a, b, c)
        case('2'):
            x, y = symbols('x y')
            expr = input('Введите уравнение: ')
            result2 = derivatives(x, y, expr)
        case('3'):
            x = symbols('x')
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