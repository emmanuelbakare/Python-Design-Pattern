class Vehicle:
    def __init__(self, model):
        self.model = model
    
    def start_engine(self):
        print(f'{self.model} engine started')
        
    def stop_engine(self):
        print(f'{self.model} engine stopped')

class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model)
        
    def drive(self):
        print(f'{self.model} car is being driven')
        
class Motorcycle(Vehicle):
    def __init__(self, model):
        super().__init__(model)
        
    def ride(self):
        print(f'{self.model} motorcycle is being ridden')


car = Car("BMW")
car.start_engine()  
car.drive() 
car.stop_engine() 


motorcycle = Motorcycle("Harley Davidson")
motorcycle.start_engine()  
motorcycle.ride()  
motorcycle.stop_engine()  