import math


# Функции для математических операций
def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second != 0:
        return first / second
    else:
        raise ValueError("Деление на ноль!")


def modulo(first, second):
    if second != 0:
        return first % second
    else:
        raise ValueError("Деление на ноль!")


def integer_division(first, second):
    if second != 0:
        return first // second
    else:
        raise ValueError("Деление на ноль!")


def power(first, second):
    return first ** second


# Функции для расчета площади различных фигур
def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def calculate_circle_area(r):
    return math.pi * r * r


def calculate_rectangle_area(a, b):
    return a * b


# Главная функция для выполнения операции
def main():
    operation = input("Введите математическую операцию (+, -, *, /, mod, div, pow): ")

    if operation in ['+', '-', '*', '/', 'mod', 'div']:
        first = float(input("Введите первое число: "))
        second = float(input("Введите второе число: "))
    elif operation == 'pow':
        first = float(input("Введите основание: "))
        second = float(input("Введите степень: "))

    if operation == '+':
        print(add(first, second))
    elif operation == '-':
        print(subtract(first, second))
    elif operation == '*':
        print(multiply(first, second))
    elif operation == '/':
        try:
            print(divide(first, second))
        except ValueError as e:
            print(e)
    elif operation == 'mod':
        try:
            print(modulo(first, second))
        except ValueError as e:
            print(e)
    elif operation == 'div':
        try:
            print(integer_division(first, second))
        except ValueError as e:
            print(e)
    elif operation == 'pow':
        print(power(first, second))
        figure = input("Введите фигуру (треугольник, круг, прямоугольник): ")
        if figure == 'треугольник':
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(calculate_triangle_area(a, b, c))
        elif figure == 'круг':
            r = float(input("r = "))
            print(calculate_circle_area(r))
        elif figure == 'прямоугольник':
            a = float(input("a = "))
            b = float(input("b = "))
            print(calculate_rectangle_area(a, b))
