class Vehicle:
    def description(self):
        print("This is a vehicle")
class Engine:
    def engine_type(self):
        print("Engine type is diesel")
class Car(Vehicle,Engine):
    def wheels(self):
        print("Car has 4 wheels")
car=Car()
car.description()
car.engine_type()