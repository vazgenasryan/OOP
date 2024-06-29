# Lesson 27 presentetion exercisess
# class Car:
#     car_tire = 4
#
#     def __init__(self, company_name, model, year):
#         self.company = company_name
#         self.model = model
#         self.year = year
#
#     def cars_atribut(self, mile, max_speed):
#         return f"{self.model} is drive {mile} mile and maximum speed is {max_speed} Km/H"
#
#     def __str__(self):
#         return f'{self.model}, {self.year}'
#
#
# car_1 = Car('Toyota', 'Camry', '2008')
# print(car_1)
# print(car_1.__dict__)
# print(car_1.cars_atribut(85, 185))
class Triangle:
    triangle_side = 3

    def __init__(self, a, b, c):
        if a + b > c and b + c > a and a + c > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            print('This triangle not defind')

    def __str__(self):
        return f'Triangle side is` a = {self.a}, b = {self.b}, c = {self.c}, P = {self.a + self.b + self.c}, S = {(self.a + self.b + self.c / 2) * (self.a + self.b + self.c / 2 - self.a) * (self.a + self.b + self.c / 2 - self.b) * (self.a + self.b + self.c / 2 - self.c)}'

    def sqear_triangle(self):
        return self.a ** 2 + self.b ** 2 == self.c ** 2 or self.c ** 2 + self.b ** 2 == self.a ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2


triangle1 = Triangle(3, 4, 5)
print(triangle1)
print(triangle1.sqear_triangle())