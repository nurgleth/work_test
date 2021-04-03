from math import pi


def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Не верный тип данных")
    if radius < 0:
        raise ValueError("Радиус должен быть положительным")
    return pi * radius ** 2
