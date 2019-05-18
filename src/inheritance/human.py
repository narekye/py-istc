class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Incorrect age")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(self.__name, "--", self.__age)


pass

