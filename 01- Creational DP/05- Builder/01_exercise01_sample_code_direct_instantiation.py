class House:
    def __init__(self):
        self.floor = None
        self.wall = None
        self.roof = None
        self.furniture = dict()

    def __str__(self):
        return f"Floor: {self.floor}\n" \
               f"Wall: {self.wall}\n" \
               f"Roof: {self.roof}\n" \
               f"Furniture: {self.furniture}\n" \


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_floor(self, amount):
        self.house.floor = amount
        return self
    
    def set_wall(self, amount):
        self.house.wall = amount
        return self
    
    def set_roof(self, amount):
        self.house.roof = amount
        return self
    
    def set_furniture(self, name, amount):
        if not self.house.furniture.get(name):
            self.house.furniture[name] = 0
        self.house.furniture[name] += amount

        return self
    
    def get_house(self):
        return self.house

print("===House HOUSE===")
small_house_builder = HouseBuilder()
small_house_builder.set_floor(9).set_wall(12). \
    set_furniture("Chairs",5).set_furniture("Chairs", 4). \
    set_furniture("Tables", 8)
    
small_house = small_house_builder.get_house()
# house =  House(4, 10,3)
print(small_house) 


print("\n===BIG HOUSE===")
big_house_builder = HouseBuilder()
big_house_builder.set_floor(24).set_roof(11).set_wall(45). \
    set_furniture("Sofa",25). \
    set_furniture("Sofa",5). \
    set_furniture("Tables", 8)

big_house_builder.set_furniture("Cupboard",4).set_furniture("Bed",10)

big_house = big_house_builder.get_house()
print(big_house)