class Bike:
    def __init__(self, colour, num_tyre, gears):
        self.colour = colour
        self.num_tyre = num_tyre
        self.gears = gears
    def display_details(self):
        print("Bike Details:")
        print(f"Colour: {self.colour}")
        print(f"Number of tyres: {self.num_tyre}")
        print(f"Gears: {self.gears}")
class Car:
    def __init__(self, colour, num_tyre, gears):
        self.colour = colour
        self.num_tyre = num_tyre
        self.gears = gears
    def display_details(self):
        print("Car Details:")
        print(f"Colour: {self.colour}")
        print(f"Number of tyres: {self.num_tyre}")
        print(f"Gears: {self.gears}")
class Scooty:
    def __init__(self, colour, num_tyre, gears):
        self.colour = colour
        self.num_tyre = num_tyre
        self.gears = gears
    def display_details(self):
        print("Scooty Details:")
        print(f"Colour: {self.colour}")
        print(f"Number of tyres: {self.num_tyre}")
        print(f"Gears: {self.gears}")
Xpulse = Bike("Black", 2, 5)
XUV700 = Car("Dark Blue", 4, 6)
Activa = Scooty("White", 2, 0)
XUV700.display_details()
print("\n")
Xpulse.display_details()
print("\n")
Activa.display_details()