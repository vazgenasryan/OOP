class Calculate:
    @staticmethod
    def _is_valid_number(number):
        return isinstance(number, int) or isinstance(number, float)

    def __init__(self, number):
        if self._is_valid_number(number):
            self.__number = number
        else:
            raise ValueError('This number class have not been int or float! ')

    @property
    def number(self):
        return self.__number

    def __add__(self, other):
        if isinstance(other, Calculate):
            return Calculate(self.__number + other.__number)
        else:
            if self._is_valid_number(other):
                return Calculate(self.__number + other)
            else:
                raise ValueError('The number must be int or float')

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        """"This is do (+=) calculate"""""
        if isinstance(other, Calculate):
            self.__number += other.__number
        else:
            self.__number += other
        return self

    def __sub__(self, other):
        """"This is do (-) calculate"""""
        if isinstance(other, Calculate):
            return Calculate(self.__number - other.__number)
        else:
            if self._is_valid_number(other):
                return Calculate(self.__number - other)
            else:
                ValueError('The number must be int or float')

    def __rsub__(self, other):
        if self._is_valid_number(other):
            return Calculate(other - self.__number)
        else:
            ValueError('The number must be int or float')

    def __isub__(self, other):
        """"This is do (-=) calculate"""""
        if isinstance(other, Calculate):
            self.__number -= other.__number
        else:
            self.__number -= other
        return self

    def __mul__(self, other):
        if isinstance(other, Calculate):
            return Calculate(self.__number * other.__number)
        else:
            if self._is_valid_number(other):
                return Calculate(self.__number * other)
            else:
                raise ValueError('The number must be int or float')

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        """"This is do (*=) calculate"""""
        if isinstance(other, Calculate):
            self.__number *= other.__number
        else:
            self.__number *= other
        return self

    def __truediv__(self, other):
        if isinstance(other, Calculate):
            return Calculate(self.__number / other.__number)
        else:
            if self._is_valid_number(other):
                return Calculate(self.__number / other)
            else:
                raise ValueError('The number must be int or float')

    def __rtruediv__(self, other):
        if self._is_valid_number(other):
            return Calculate(other / self.__number)
        else:
            ValueError('The number must be int or float')

    def __itruediv__(self, other):
        """"This is do (/=) calculate"""""
        if isinstance(other, Calculate):
            self.__number /= other.__number
        else:
            self.__number /= other
        return self

    def __floordiv__(self, other):
        if isinstance(other, Calculate):
            return Calculate(self.__number // other.number)
        else:
            if self._is_valid_number(other):
                return Calculate(self.__number // other)
            else:
                raise ValueError('The number must be int or float')

    def __rfloordiv__(self, other):
        if self._is_valid_number(other):
            return Calculate(other // self.__number)
        else:
            ValueError('The number must be int or float')

    def __ifloordiv__(self, other):
        """"This is do (//=) calculate"""""
        if isinstance(other, Calculate):
            self.__number //= other.__number
        else:
            self.__number //= other
        return self

    def __mod__(self, other):
        if isinstance(other, Calculate):
            return Calculate(self.__number % other.__number)
        else:
            if self._is_valid_number(other):
                return Calculate(self.__number % other)
            else:
                raise ValueError('The number must be int or float')

    def __rmod__(self, other):
        if self._is_valid_number(other):
            return Calculate(other % self.__number)
        else:
            ValueError('The number must be int or float')

    def __imod__(self, other):
        """"This is do (%=) calculate"""""
        if isinstance(other, Calculate):
            self.__number %= other.__number
        else:
            self.__number %= other
        return self

    def __pow__(self, power, modulo=None):
        if isinstance(power, Calculate):
            return Calculate(self.__number ** power.__number)
        else:
            if self._is_valid_number(power):
                return Calculate(self.__number ** power)
            else:
                raise ValueError('The number must be int or float')

    def __rpow__(self, other):
        if self._is_valid_number(other):
            return Calculate(other ** self.__number)
        else:
            ValueError('The number must be int or float')

    def __ipow__(self, other):
        """"This is do (%=) calculate"""""
        if isinstance(other, Calculate):
            self.__number **= other.__number
        else:
            self.__number **= other
        return self

    def __eq__(self, other):
        if isinstance(other, Calculate):
            return self.__number == other.__number
        else:
            if self._is_valid_number(other):
                return self.__number == other
            else:
                raise ValueError("The number must be int or float")

    def __ne__(self, other):
        if isinstance(other, Calculate):
            return self.__number != other.number
        else:
            if self._is_valid_number(other):
                return self.__number != other
            else:
                raise ValueError("The number must be int or float")

    def __lt__(self, other):
        if isinstance(other, Calculate):
            return self.__number < other.number
        else:
            if self._is_valid_number(other):
                return self.__number < other
            else:
                raise ValueError("The number must be int or float")

    def __le__(self, other):
        if isinstance(other, Calculate):
            return self.__number <= other.number
        else:
            if self._is_valid_number(other):
                return self.__number <= other
            else:
                raise ValueError("The number must be int or float")

    def __gt__(self, other):
        if isinstance(other, Calculate):
            return self.__number > other.number
        else:
            if self._is_valid_number(other):
                return self.__number > other
            else:
                raise ValueError("The number must be int or float")

    def __ge__(self, other):
        if isinstance(other, Calculate):
            return self.__number >= other.number
        else:
            if self._is_valid_number(other):
                return self.__number >= other
            else:
                raise ValueError("The number must be int or float")

    def __str__(self):
        return f'{self.__number}'

    def __repr__(self):
        return f'{self.__number}, type is {type(self.__number)}'


c1 = Calculate(15)
c2: Calculate = Calculate(10)
c3 = c1 * c2
c3 = 7 ** c2
# print(c3)
c3 /= 7
c3 **= 7
print(c3 >= 1.2142656789020128e+43)
print(c3)
print(c1)
