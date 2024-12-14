from abc import ABC, abstractmethod
class AbstractVehicle(ABC):
    def __init__(self, colour, num_tyre, gears):
        self.colour = colour
        self.num_tyre = num_tyre
        self.gears = gears
    def display_details(self):
        print(f"Colour: {self.colour}")
        print(f"Number of tyres: {self.num_tyre}")
        print(f"Gears: {self.gears}")
class Bike(AbstractVehicle):
    def display_details(self):
        print("Bike Details:")
        super().display_details()
class Car(AbstractVehicle):
    def display_details(self):
        print("Car Details:")
        super().display_details()
class Scooty(AbstractVehicle):
    def display_details(self):
        print("Scooty Details:")
        super().display_details()
bike = Bike(colour="Red", num_tyre=2, gears=6)
car = Car(colour="Blue", num_tyre=4, gears=5)
scooty = Scooty(colour="Black", num_tyre=2, gears=1)
bike.display_details()
car.display_details()
scooty.display_details()