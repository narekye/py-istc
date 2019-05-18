from .abstraction import Abstraction


class ConcreteAbstraction(Abstraction):
    def __init__(self, name, age, company):
        Abstraction.__init__(self, name, age)
        self.company = company

    def display_info(self):
        Abstraction.display_info(self)
        print("Company:", self.company)
