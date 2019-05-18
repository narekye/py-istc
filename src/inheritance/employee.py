from .human import Human


class Employee(Human):
    def details(self, company, salary):
        # print(self.__name, "works at", company) # no way, self.__name is a private attribute
        print(self.name, "works at", company, "with salary", salary, "$")


pass
