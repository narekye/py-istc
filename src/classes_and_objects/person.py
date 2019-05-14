class Person:
    name = ""

    # Constructor for this class
    def __init__(self, name):
        self.name = name

    # Custom method which is attached to this class
    def display_info(self):
        print("Hi my name is: ", self.name)

    # Destructor for the instance
    def __del__(self):
        print("Person with", self.name, " was removed from the memory")

