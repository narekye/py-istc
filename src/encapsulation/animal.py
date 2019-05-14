# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
#
#     def display_info(self):
#         print("Name: ", self.name, "Age: ", self.age)


class Animal:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    def set_age(self, age):
        if age in range(1, 100):
            self.age = age
        else:
            print("Incorrect age!!")  # Or throw an exception

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Name: ", self.__name, "Age: ", self.__age)
