"""""
•Create a Computation class with a default constructor (without parameters) 
allowing to perform various calculations on integers numbers.
•Create a method called factorial() which allows to calculate the factorial of an 
integer. 
•Create a method called sum() allowing to calculate the sum of the first n 
integers 1 + 2 + 3 + .. + n. 
•Create a method called is_prime() allowing to test the primality of a given 
integer. 
•Create a method called all_is_prime() allowing to display all prime integer 
numbers from 2 to n. 
•Create a table_mult() method which creates and displays the multiplication 
table of a given integer (from 1 to 10). 
•Then create an all_tables_mult() method to display all the integer 
multiplication tables (from 1 to 10).
"""""


class Computation:
    def __init__(self):
        pass

    def factorial(self, n):
        k = 1
        for i in range(1, n + 1):
            k *= i
        return k

    def summa(self, n):
        k = 0
        for i in range(n + 1):
            k += i
        return k

    def is_prime(self, n):
        l_1 = []
        if n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(1, n // 2 + 1, 2):
                if n % i == 0:
                    l_1.append(i)
            if len(l_1) == 1:
                return True
            return False

    def all_is_prime(self, n):
        l_2 = []
        for i in range(n + 1):
            if self.is_prime(i):
                l_2.append(i)
            else:
                ...
        return l_2

    def table_mult(self, n):
        for i in range(1, 11):
            print(f'{n} * {i} = {n * i}')

    def all_tables_mult(self):
        for i in range(1, 11):
            for j in range(1, 11):
                print(f'{i} * {j} = {i * j}')


a = Computation()
# print(a.factorial(5))
# print(a.summa(5))
# print(a.is_prime(17))
# print(a.all_is_prime(15))
# a.table_mult(3)
a.all_tables_mult()
