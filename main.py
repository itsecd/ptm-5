from math import sqrt
from sympy import symbols, diff, integrate

def square_eq_solver(a, b, c):
   result = []
   discriminant = b * b - 4 * a * c

   if discriminant == 0:
       result.append(-b / (2 * a))
   elif discriminant > 0:
       result.append((-b + sqrt(discriminant)) / (2 * a))
       result.append((-b - sqrt(discriminant)) / (2 * a))

   if len(result) > 0:
       for index, value in enumerate(result):
           print(f'Корень номер {index+1} равен {value:.02f}')
   else:
       print('Уравнение с заданными параметрами не имеет корней')

def derivatives(x, y, expr):

    df_dx = diff(expr, x)
    df_dy = diff(expr, y)

    print("Частная производная от выражения по x:", df_dx)
    print("Частная производная от выражения по y:", df_dy)
    return df_dx, df_dy

def indefinite_integral(x, expr):
    integral_expr = integrate(expr, x)

    print("Неопределенный интеграл по x:", integral_expr)

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
    area = ((base_1 + base_2) / 2) * height
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
