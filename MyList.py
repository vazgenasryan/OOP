class MyList:

    def __init__(self, *args):
        self.args = list(args)

    def __getitem__(self, item):
        """"This method is doing index iteration"""""
        return self.args[item]

    def __setitem__(self, key, value):
        """"This method change index value"""""
        self.args[key] = value

    def __delitem__(self, key):
        print(f'This {self.args[key]} element was deleted')
        del self.args[key]

    def append(self, value):
        self.args.append(value)

    def extend(self, iterator):
        self.args.extend(iterator)

    def remove(self, delete_index_value):
        self.args.remove(delete_index_value)

    def pop(self, index=-1):
        self.args.pop(index)

    def insert(self, index, value):
        self.args.insert(index, value)

    def sum_my_list(self):
        my_sum = 0
        for i in self.args:
            my_sum += i
        return my_sum

    def pow_my_list(self):
        my_pow = 1
        for i in self.args:
            my_pow *= i
        return my_pow

    def medium_element_my_list(self):
        if len(self.args) % 2 == 1:
            return self.args[len(self.args) // 2]
        else:
            return self.args[len(self.args) // 2 - 1]

    def the_arithmetic_average(self):
        return self.sum_my_list() / len(self.args)

    def my_list_sort(self):
        list_sort = []
        l1 = self.args.copy()
        for i in range(len(l1)):
            list_sort.append(min(l1))
            l1.remove(min(l1))
        return list_sort

    def max_element(self):
        x = 0
        for i in self.args:
            if i > x:
                x = i
            else:
                x = x
        return x

    def min_element(self):
        x = 0
        for i in self.args:
            if i < x:
                x = i
            else:
                x = x
        return x

    def __len__(self):
        return len(self.args)

    def __str__(self):
        return f'MyList is {self.args}'


b1 = MyList(1, 2, 3, 4, 5, 0, -100)
# print(b1[1])
# b1[1] = 4
# b1.append(5)
# b1.remove(4)
# print(b1)
# print(b1.sum_my_list())
# print(b1.pow_my_list())
# print(b1.medium_element_my_list())
# print(b1.the_arithmetic_average())
# del b1[0]
print(b1.my_list_sort())
print(b1.max_element())
print(b1.min_element())
print(b1)
print(b1.pop(0))
print(b1)
print(b1.insert(2, 7))
print(b1)
