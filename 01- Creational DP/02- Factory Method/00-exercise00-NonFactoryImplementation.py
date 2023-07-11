class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def start(self):
        if self.vehicle_type == "car":
            print("Starting the car...")
        elif self.vehicle_type == "motorcycle":
            print("Starting the motorcycle...")
        elif self.vehicle_type == "bicycle":
            print("Starting the bicycle...")
        else:
            print("Invalid vehicle type!")


# Client code
car = Vehicle("car")
car.start()

motorcycle = Vehicle("motorcycle")
motorcycle.start()

bicycle = Vehicle("bicycle")
bicycle.start()
