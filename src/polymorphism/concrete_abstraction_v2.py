from .abstraction import Abstraction


class ConcreteAbstractionV2(Abstraction):
    def __init__(self, name, age, university):
        Abstraction.__init__(self, name, age)
        self.university = university

    def display_info(self):
        print("Student", self.name, "goes to", self.university)
