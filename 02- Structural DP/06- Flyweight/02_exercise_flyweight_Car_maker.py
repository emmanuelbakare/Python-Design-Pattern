import random

class Car:
    def __init__(self, make, model, color):
        self.make = make 
        self.model = model
        self.color = color
        self.shipped_to = None 

    def get_info(self):
        print(f"Make: {self.make}, Model: {self.model}")
        print(f"Color: {self.color}, Shipped To: {self.shipped_to}")
        print()


class CarFactory:
    _cars = {}
    _created = 0

    @staticmethod
    def create_car(make, model, color):
        if (make, model, color) not in CarFactory._cars:
            car = Car(make, model, color)
            CarFactory._cars[(make, model, color)]= car
            CarFactory._created += 1
        return CarFactory._cars[(make, model, color)]

if __name__ == "__main__": 
    cars = [
        CarFactory.create_car("Toyota","Venza","Red"),
        CarFactory.create_car("Toyota","Corolla","Blue"),
        CarFactory.create_car("Toyota","Camry","Ash"),
        CarFactory.create_car("Toyota","Venza","Red"),
        CarFactory.create_car("Toyota","Corolla","Blue"),
        CarFactory.create_car("Toyota","Corolla","Blue"),
    ]

    location = ["Nigeria","Germany", "USA","Japan", "China","France"]

    for num, car in enumerate(cars, 1):
        print("Car:",num)
        car.shipped_to = random.choice(location)
        car.get_info()

    print("Total Car:", len(cars))
    print("Total Objects: ", CarFactory._created)
