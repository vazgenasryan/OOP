# 1․ Գրել MyShows class, որը․
#    - __init__ ում կստանա
#      -- սերիալի անունը (պետք է լինի տեքստ),
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։
class MyShows:
    @staticmethod
    def _is_valid_serial_name_and_platform(serial_name, serial_platform):
        return isinstance(serial_name, str) and isinstance(serial_platform, str)

    @staticmethod
    def _first_serial_year_and_number(year, serial_number):
        return isinstance(year, int) and isinstance(serial_number, int)

    @staticmethod
    def _put_rating_user(serial_rating):
        return 1 <= serial_rating <= 10

    @staticmethod
    def _main_actor_list(actor_name):
        return type(actor_name) == list and filter(lambda x: x is str, actor_name)

    def __init__(self, serial_name, netflix, serial_year, serial_actors_list, serial_number=1, serial_rating=None):
        if self._is_valid_serial_name_and_platform(serial_name, netflix) and self._first_serial_year_and_number(
                serial_year, serial_number) and self._put_rating_user(serial_rating) and self._main_actor_list(serial_actors_list):
            self.__serial_name = serial_name
            self.__netflix = netflix
            self.__serial_year = serial_year
            self.__serial_actor_list = serial_actors_list
            self.__serial_number = serial_number
            self.__serial_rating = serial_rating
            """This mean question about are you want add your rating or no in number 1 or 0"""
            self.__serial_rating_unblock = int(input('Enter are you want del rating (1 - No, 0 -Yes)?:)  '))
        else:
            raise ValueError

    @property
    def info(self):
        """This property is serial actor name and serial name"""
        return f'Serial name is {self.__serial_name} actors ` {self.__serial_actor_list} years is ` {self.__serial_year}'

    @property
    def name_serial(self):
        """This property is serial name """
        return f'Serial name is ` {self.__serial_name}'

    @property
    def netflix(self):
        """This property is serial site"""
        return f'Hello from {self.__netflix} site'

    @property
    def year_serial(self):
        """This property is serial year"""
        return f'Serial is {self.__serial_year} year'

    @property
    def serial_actor(self):
        """This property is serial actor name"""
        return f"Serial actors are ` {self.__serial_actor_list}"

    @property
    def number_serial(self):
        """This property is serial number"""
        return f"Serial number is {self.__serial_number}"

    @property
    def rating_serial(self):
        """This property is serial rating"""
        return f"Serial rating is {self.__serial_rating}"

    @number_serial.setter
    def number_serial(self, value):
        """This property about is your serial number"""
        if not isinstance(self.__serial_number, int):
            print('Invalid serial number: ')
        else:
            self.__serial_number = value
            print(f'Serial number is {self.__serial_number} :)')

    @rating_serial.setter
    def rating_serial(self, new_rating):
        if not self._put_rating_user(new_rating):
            print('Invalid rating input')
        else:
            self.__serial_rating = new_rating
            print(f'Your serial rating is {self.__serial_rating}')

    @rating_serial.deleter
    def rating_serial(self):
        if self.__serial_rating_unblock == 1:
            return True
        else:
            if self.__serial_rating_unblock == 0:
                print('Your rating is delete')
                del self.__serial_rating
            else:
                print('Invalid input please try again !')

    @property
    def add_name(self):
        a = input('Enter actor name separat (", ")').split(', ')
        return a + self.__serial_actor_list

    def remove_name(self, name):
        if name in self.__serial_actor_list:
            self.__serial_actor_list.remove(name)
        else:
            print('Not find actor name')


serial1 = MyShows('Կաղամարի խաղը', 'armfilm', 2021, ['Լի Չոն Ջի', 'Պակ Հի Սու', 'Հո Սոն Տհե', 'Վի Հա Չժուն',
                                                     'Կիմ Ջու Ռեն', 'Չոն Հո Յոն'], 5, 9)
print(serial1.netflix)
print(serial1.name_serial)
print(serial1.number_serial)
print(serial1.year_serial)
print(serial1.rating_serial)
print(serial1.serial_actor)
serial1.number_serial = 6
serial1.rating_serial = 8
del serial1.rating_serial
# print(serial1.rating_serial)
print(serial1.info)
print(serial1.add_name)
print(serial1.remove_name('Լի Չոն Ջի'))
print(serial1.info)
