 # 1․ Գրել BankUser class, որը․
#    - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
#      -- անունը և ազգանունը - տառերից բաղկացած,
#      -- տարիքը - բնական թիվ,
#      -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
#      -- գումարը - դրական թիվ,
#      -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
#    - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
#    - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
#    - կունենա մեթոդ, որը կվերադարձնի մարդու անունը, ազգանունը և տարիքը,
#    - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
#    - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
#    - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել,
#    - 3 անգամ սխալ գաղտնաբառ հավաքելուց հետո տվյալ user-ի համար հասանելիությունը class-ի
# ամբողջ ֆունկցիոնալությանը կլինի արգելված։
class BankUser:
    @staticmethod
    def _valid_name_surname_age(user_name, user_surname, user_age):
        return isinstance(user_name, str) and isinstance(user_surname, str) and isinstance(user_age,
                                                                                           int) and user_name.isalpha() and user_surname.isalpha() and user_age > 0

    @staticmethod
    def __is_valid_account_number(account_number):
        return isinstance(account_number, str) and len(account_number) == 19 and (
                account_number[:4] + account_number[5:9] + account_number[10:14] +
                account_number[15:]).isdigit() and account_number[4::5] == '   ' or len(
            account_number) == 16 and account_number.isdigit()

    @staticmethod
    def _passw(password):
        return isinstance(password, str) and len(password) > 8

    @staticmethod
    def _money_account(money_account):
        return isinstance(money_account, int | float) and money_account > 0

    def __init__(self, name, surname, age, account_number, money_account, password):
        if self._valid_name_surname_age(name, surname, age) and self.__is_valid_account_number(
                account_number) and self._passw(password) and self._money_account(money_account):
            self._name = name
            self._surname = surname
            self._age = age
            self.__account_number = account_number
            self.__money_account = money_account
            self.__password = password
            self._count_enter_parol = 3
            self._blocked = False
        else:
            raise ValueError('Not find you user! Sorry ')

    def block(self):
        if self._blocked:
            return False
        return True

    def user_passw(self):
        if input('Enter your password ') == self.__password:
            return True
        print('Invalid Input')
        self._count_enter_parol -= 1
        if self._count_enter_parol == 0:
            self._blocked = True
            print('Your account is blocked')
        return False

    def user_info(self):
        if self.block():
            if self.user_passw():
                print(f'{self._name} {self._surname} {self._age}')

    def user_card_info(self):
        if self.block():
            if self.user_passw():
                print(f'Card info ` Account number : {self.__account_number} Account money : {self.__money_account}')

    def user_account_unblock(self):
        if self.block() is False:
            name = input('Enter your name: ')
            surname = input('Enter your surname')
            age = int(input('Enter your age'))
            enter_your_old_password = input('Enter your password: ')
            if name == self._name and surname == self._surname and age == self._age and enter_your_old_password == self.__password:
                self._blocked = False
                print('Your account unblocked ')
                return True
            print('Invalid data')
        else:
            print('Your account unblocked')

    def add_money(self):
        if self.block():
            add_money = int(input('add_money'))
            if self.__money_account > 0 and isinstance(add_money, float | int) and self.__money_account > add_money:
                self.__money_account += add_money
        else:
            print('Not can you add money. Sorry')


user1 = BankUser('Վազգեն', 'Ասրյան', 21, '4444 5555 6666 8888', 5000, 'qwerty123')