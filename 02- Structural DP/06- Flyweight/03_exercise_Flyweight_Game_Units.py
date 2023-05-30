import random
class UnitType:
    def __init__(self, name, image):
        self.name = name
        self.image = image

class Unit:
    def __init__(self, x, y, unit_type):
        self.x = x
        self.y = y
        self.unit_type = unit_type
    
    def draw(self):
        print(f"Drawing {self.unit_type.name} at ({self.x}, {self.y}) with image {self.unit_type.image}")


class UnitFactory:
    def __init__(self):
        self.unit_types = {}

    def get_unit_type(self, name, image):
        if name not in self.unit_types:
            unit_type = UnitType(name, image)
            self.unit_types[name] = unit_type
        return self.unit_types[name]
    
if __name__ == "__main__":
    factory = UnitFactory()

    unit_types = [
        factory.get_unit_type("Soldier", "soldier.png"),
        factory.get_unit_type("Tank", "tank.png"),
        factory.get_unit_type("Mouse", "mouse.png"),
        factory.get_unit_type("Lion", "lion.png")  
    ]

    for i in range(10):
        screenx = random.randint(0,1080)
        screeny = random.randint(0,1920)
        unit = Unit(screenx,screeny, random.choice(unit_types))
        unit.draw()
    print("Total Units Made:", i+1)
    print("Total Objects Created:", len(unit_types))
         

