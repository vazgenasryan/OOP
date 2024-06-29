class BankUser:
    count_enter_parol = 3

    @staticmethod
    def is_valid_account_number(account_number):
        clean_account_number = account_number.replace(' ', '')
        return clean_account_number.isdigit() and len(clean_account_number) == 16

    @staticmethod
    def money_account(account_money):
        return int(account_money)

    @staticmethod
    def is_valid_name_surname(user_name, user_surname, age):
        return user_name.isalpha() and user_surname.isalpha() and age.isdigit()

    @staticmethod
    def is_valid_parol(password):
        return len(password) > 8 and password.isalpha()

    def __init__(self, name, surname, age, account_number, account_money, password):
        if self.is_valid_account_number(account_number) and self.is_valid_name_surname(name, surname,
                                                                                       age) and self.money_account(
                account_money) and self.is_valid_parol(password):
            self._name = name
            self._surname = surname
            self._age = age
            while self.count_enter_parol > 0:
                enter_parol = input('Please Enter password ')
                if enter_parol == password:
                    self.__account_number = account_number
                    self.__account_money = account_money
                    self.__password = password
                    break
                else:
                    self.count_enter_parol = self.count_enter_parol - 1
                    if self.count_enter_parol == 0:
                        print('Your account is blocked')

        else:
            raise ValueError('Error Invalid..Bye!')

    def __str__(self):
        return f'Անուն՝ {self._name} Ազգանուն ՝ {self._surname} Տարիք ՝{self._age} Բանկային քարտի համար ՝ {self.__account_number}, Հաշվի մնացորդ ՝ {self.__account_money} դրամ'


user1 = BankUser('Վազգեն', 'Ասրյան', '21', '4444 5555 6666 8888', '5000', 'vazgenasryan')
print(user1)