class Car:

    carName = ""

    def __init__(self, carName):
        self.carName = carName

    def move_car(self, speed):
        print("Driver drives the car with name ", self.carName, " with ", speed, " km/h speed")


pass
