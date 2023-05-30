# Vehicle  / Engine

#=========ABSTRACTION=======
class Vehicle:
    def __init__(self, engine):
        self.engine = engine 

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

class Car(Vehicle):

    def drive(self):
        print("Car is being driven")

class Motorcycle(Vehicle):

    def ride(self):
        print("Motorcycle is being ridden")




#=========IMPLEMENTATION=======
class Engine:
    def start(self):
        pass
    
    def stop(self):
        pass

class CarEngine(Engine):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

class MotorcycleEngine(Engine):
    def start(self):
        print("Motorcycle engine started")
    
    def stop(self):
        print("Motorcycle engine stopped")


class TruckEngine(Engine):
    def start(self):
        print("Truck engine started")
    
    def stop(self):
        print("Truck engine stopped") 


# car_engine = CarEngine()
# car = Car(car_engine)
# car.start_engine()
# car.drive()
# car.stop_engine()

# car2 = Car(TruckEngine())
# car2.start_engine()
# car2.drive()
# car2.stop_engine()

motorcycle_engine = MotorcycleEngine()
motorcycle = Motorcycle(motorcycle_engine)
motorcycle.start_engine()  
motorcycle.ride() 
motorcycle.stop_engine()
