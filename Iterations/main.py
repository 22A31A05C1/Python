from abc import ABC, abstractmethod
class AbstractVehicle(ABC):
    def __init__(self, colour, num_tyre, gears):
        self.colour = colour
        self.num_tyre = num_tyre
        self.gears = gears
    @abstractmethod
    def display_details(self):
        pass
class Car(AbstractVehicle):
    def display_details(self):
        return f"Car details: Colour = {self.colour}, Tyres = {self.num_tyre}, Gears = {self.gears}"
car = Car('Red', 4, 5)
print(car.display_details())