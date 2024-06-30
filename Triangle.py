class Triangle:

    def __init__(self, a, b, c):
        if self.there_are_triangle(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError('Invalid data! ')

    def there_are_triangle(self, a, b, c):
        return a + b > c and b + c > a and a + c > b

    def __str__(self):
        return f'a = {self.a} b = {self.b}, c = {self.c}'

    def perimetr(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimetr() / 2
        return f'Triangle area S = {p * (p - self.a) * (p - self.b) * (p - self.c) ** 0.5}'

    def triangle_equilateral(self):
        return self.a == self.b == self.c

    def triangle_equal(self):
        return self.a ** 2 + self.b ** 2 == self.c ** 2 or self.c ** 2 + self.b ** 2 == self.a ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2


triangle1 = Triangle(3, 4, 5)
print(triangle1)
print(f'Triangle P = {triangle1.perimetr()}')
print(triangle1.area())
print(triangle1.triangle_equilateral())
print(triangle1.triangle_equal())