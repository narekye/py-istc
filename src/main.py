from classes_and_objects.person import Person
from classes_and_objects.car import Car

from encapsulation.animal import Animal

# from classes_and_objects import variable

# Stage 1, Intro

person = Person("Jane")
person.display_info()

# del person # Hint here

person2 = Person("Sam")
person2.display_info()

car = Car("BMW")
car.move_car(64)

# print(variable)

# Stage 2, encapsulation

dog = Animal("Bax")
dog.display_info()

dog.__age = -10 # Setting from outside
# dog.set_age(-20)
dog.display_info()
