class Sandwich:
    def __init__(self):
        self._bread = None 
        self._meat = None 
        self._cheese = None 
        self._vegetables = [] 
        self._sauces = [] 

    def __str__(self):
        ingredients = "Bread: "+self._bread + "| Meat: " + self._meat
        if self._cheese:
            ingredients += "| Cheese: " + self._cheese
        ingredients +="| Vegetables: " + ', '.join(self._vegetables)
        ingredients += "| Sauces: " + ', '.join(self._sauces)
        return ingredients

class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()
    
    def add_bread(self):
        pass
    def add_meat(self):
        pass
    def add_cheese(self):
        pass
    def add_vegetables(self):
        pass
    def add_sauces(self):
        pass
    
    def get_sandwich(self):
        return self.sandwich 

class ClubSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "White Bread"
    
    def add_meat(self):
        self.sandwich._meat = "Chicken"
    
    def add_cheese(self):
        self.sandwich._cheese = "Cheddar"
    
    def add_vegetables(self):
        self.sandwich._vegetables.append("tomato")
        self.sandwich._vegetables.append("lettuce")

    def add_sauces(self):
        self.sandwich._sauces.append("mayo")
        self.sandwich._sauces.append("mustard")

class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "Whole Wheat Bread"
    
    def add_meat(self):
        self.sandwich._meat = "Tofu"
    
    
    def add_vegetables(self):
        self.sandwich._vegetables.append("spinach")
        self.sandwich._vegetables.append("Bell Pepper")

    def add_sauces(self):
        self.sandwich._sauces.append("Hummus")
        self.sandwich._sauces.append("Tahini")

class Waiter:
    def __init__(self):
        self.sandwich_builder  = None 
    
    def get_builder(self, builder):
        self.sandwich_builder = builder 
    
    def create_sandwich(self):
        self.sandwich_builder.add_bread()
        self.sandwich_builder.add_meat()
        self.sandwich_builder.add_cheese()
        self.sandwich_builder.add_vegetables()
        self.sandwich_builder.add_sauces()
    
    def serve_sandwich(self):
        return self.sandwich_builder.get_sandwich()
         

if __name__ == '__main__':
    waiter = Waiter()
    waiter.get_builder(ClubSandwichBuilder())
    waiter.create_sandwich()
    print("======CLUB SANDWICH =======")
    sandwich1 = waiter.serve_sandwich() 
    print(sandwich1)

    waiter.get_builder(VeggieSandwichBuilder())
    waiter.create_sandwich()
    print("======VEGGIE SANDWICH =======")
    sandwich2 = waiter.serve_sandwich()
    print(sandwich2)