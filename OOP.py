class Car:
    car_tire = 4

    def __init__(self, company_name, model, year):
        self.company = company_name
        self.model = model
        self.year = year

    def cars_atribut(self, mile, max_speed):
        return f"{self.model} is drive {mile} mile and maximum speed is {max_speed} Km/H"

    def __str__(self):
        return f'{self.model}, {self.year}'


car_1 = Car('Toyota', 'Camry', '2008')
print(car_1)
print(car_1.__dict__)
print(car_1.cars_atribut(85, 185))