from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print (message)


def  CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень из заданного числа."""
    root = CalculateSquareRoot(your_number)
    if your_number <= 0:
        return root == 0
    print (f"Мы вычислили квадратный корень из введённого вами числа."
          f" Это будет: {root}")

calc (25.5)
