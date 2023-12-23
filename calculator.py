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
        return round(math.sin(value),3)

    def cos(self, value):
        return round(math.cos(value),3)

    def tan(self, value):
        return round(math.tan(value),3)

    def cot(self, value):
        if math.tan(value) == 0:
            return float('inf')
        return round(1 / math.tan(value))

    # Примитивное численное дифференцирование
    def derivative(self, func, x, h=1e-5):
        return (func(x + h) - func(x)) / h

    # Примитивное численное интегрирование
    def integral(self, func, a, b, n=1000):
        h = (b - a) / n
        total = sum(func(a + i * h) for i in range(n))
        return total * h

    # Простой метод поиска точек пересечения линейных функция 
    def find_intersection(self, b1, k1, b2, k2):
        if b1 == b2:
            if k1 == k2:
                return "Линии совпадают"
            else:
                return "Линии параллельны и не пересекаются"
    
        x = (k2 - k1) / (b1 - b2)
        y = b1 * x + k1
        return (x, y)
    def find_parabolas_intersection(self, a, b, c, d, e, f):
        A = a - d
        B = b - e
        C = c - f

        # Если A равно 0, уравнение становится линейным
        if A == 0:
            if B == 0:
                return "Параболы не пересекаются" if C != 0 else "Параболы совпадают"
            x = -C / B
            y = a * x**2 + b * x + c
            return [(x, y)]

        # Вычисляем дискриминант
        discriminant = B**2 - 4*A*C
        if discriminant < 0:
            return "Параболы не пересекаются"

        # Вычисляем корни уравнения
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-B + sqrt_discriminant) / (2*A)
        x2 = (-B - sqrt_discriminant) / (2*A)

        # Вычисляем соответствующие значения y
        y1 = a * x1**2 + b * x1 + c
        y2 = a * x2**2 + b * x2 + c
        y1 = round(y1, 3)
        y2 = round(y2, 3)
        x1 = round(x1, 3)
        x2 = round(x2, 3)
        # Если дискриминант равен 0, параболы пересекаются в одной точке
        if discriminant == 0:
            return [(x1, y1)]

        # Если дискриминант больше 0, параболы пересекаются в двух точках
        return [(x1, y1), (x2, y2)]
