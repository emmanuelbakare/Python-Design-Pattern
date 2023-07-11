from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting the car...")

class Motorcycle(Vehicle):
    def start(self):
        print("Starting the motorcycle...")


class Bicycle(Vehicle):
    def start(self):
        print("Starting the bicycle...")


class VehicleFactory:
    def __init__(self):
        self.factory = dict(car = Car, motorcycle = Motorcycle, bicycle = Bicycle)

    def create_vehicle(self, vehicle_type):
        if vehicle_type in self.factory:
            vehicle =self.factory.get(vehicle_type)
            return vehicle() 
        


# Client code
factory = VehicleFactory()

car = factory.create_vehicle("car")
car.start() 


motorcycle = factory.create_vehicle("motorcycle")
motorcycle.start() 

bicycle = factory.create_vehicle("bicycle")
bicycle.start()
