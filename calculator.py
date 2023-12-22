import math
from sympy import symbols, diff

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def logarithm(self, a, base):
        if a <= 0 or base <= 0:
            raise ValueError("Logarithm arguments must be greater than zero")
        return math.log(a, base)

    def derivative(self, function, variable, point):
        x = symbols(variable)
        func = eval(function)
        deriv = diff(func, x)
        return deriv.subs(x, point)