class Engine:
    def engine_type(self):
        print("This vehicle has a diesel engine")
class Wheels:
    def number_of_wheels(self):
        print("This vehicle has 4 wheels")
class Truck(Engine,Wheels):
    pass
truck=Truck()
truck.number_of_wheels()
truck.number_of_wheels()