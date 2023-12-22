import math

class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            return None
        return a / b

    def multiply(self, a, b):
        return a * b

    def solve_quadratic(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return None  
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

    def logarithm(self, value, base):
        return math.log(value, base)

    def sin(self, value):
        return math.sin(value)

    def cos(self, value):
        return math.cos(value)

    def tan(self, value):
        return math.tan(value)

    def cot(self, value):
        if math.tan(value) == 0:
            return float('inf')
        return 1 / math.tan(value)

    # Примитивное численное дифференцирование
    def derivative(self, func, x, h=1e-5):
        return (func(x + h) - func(x)) / h

    # Примитивное численное интегрирование
    def integral(self, func, a, b, n=1000):
        h = (b - a) / n
        total = sum(func(a + i * h) for i in range(n))
        return total * h

    # Простой метод поиска точек пересечения
    def find_intersection(self, func1, func2, a, b, n=1000):
        h = (b - a) / n
        intersections = []
        for i in range(n):
            x = a + i * h
            if abs(func1(x) - func2(x)) < 1e-4:
                intersections.append(x)
        return intersections