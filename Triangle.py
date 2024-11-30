import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def perimetr(self):
        ...

    @abstractmethod
    def area(self):
        ...


class Circle(Shape):

    @staticmethod
    def _is_valid_circle_radius(circle_radius):
        return circle_radius > 0

    def __init__(self, circle_radius):
        if self._is_valid_circle_radius(circle_radius):
            self.circle_radius = circle_radius
        else:
            raise ValueError('Invalid circle radius ')

    def perimetr(self):
        return f"Circle P = {2 * math.pi * self.circle_radius}"

    def area(self):
        return f'Circle S = {math.pi * (self.circle_radius ** 2)}'


class Rectangle(Shape):
    @staticmethod
    def _is_valid_rectangle(length, width):
        return length > 0 and width > 0

    def __init__(self, length, width):
        if self._is_valid_rectangle(length, width):
            self.length = length
            self.width = width
        else:
            raise ValueError('Invalid Rectangle side')

    def perimetr(self):
        return f"Rectangle P = {2 * (self.length + self.width)}"

    def area(self):
        return f'Rectangle S = {self.length * self.width}'


class Triangle(Shape):

    @staticmethod
    def _is_valid_triangle(a, b, c):
        return a + b > c and b + c > a and a + c > b

    @staticmethod
    def _is_valid_side(a, h):
        return a > 0 and h > 0

    def __init__(self, *args):
        if len(args) == 3:
            a, b, c = args
            if isinstance(a, int | float) and isinstance(b, int | float) and isinstance(c,
                                                                                        int | float) and self._is_valid_triangle(a, b, c):
                self.a, self.b, self.c = a, b, c
                self.h = None
        elif len(args) == 2:
            a, h = args
            if isinstance(a, int | float) and isinstance(h, int | float) and self._is_valid_side(a, h):
                self.a, self.h = a, h
                self.b = None
                self.c = None
        else:
            raise ValueError('Invalid triangle ')

    def perimetr(self):
        if self.a and self.b and self.c:
            return self.a + self.b + self.c
        return 'Cannot compute perimeter for a triangle with base and height'

    def area(self):
        if self.a and self.h:
            return f'Triangle S = {(self.a * self.h) / 2}'
        p = self.perimetr() / 2
        return f'Triangle S = {(p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5}'


triangle1 = Triangle(4, 5)
triangle2 = Triangle(4, 5, 6)
print(triangle1.area())
print(triangle2.area())
print(triangle1.perimetr())
