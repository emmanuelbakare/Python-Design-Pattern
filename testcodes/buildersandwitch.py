class Sandwich:
    def __init__(self):
        self._bread = None
        self._meat = None 
        self._cheese = None 
        self._vegetables = [] 
        self._sauces = []
    
    def __str__(self):
        ingredients = "Bread: " + self._bread + "| Meat: " + self._meat
        if self._cheese:
            ingredients += "| Cheese: " + self._cheese
        ingredients += "| Vegetables: " + ', '.join(self._vegetables)
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
        self.sandwich._meat = "chicken"

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
        self.sandwich._bread = "whole wheat bread"
    
    def add_meat(self):
        self.sandwich._meat = "tofu"
    
    def add_vegetables(self):
        self.sandwich._vegetables.append("spinach")
        self.sandwich._vegetables.append("bell pepper")
    
    def add_sauces(self):
        self.sandwich._sauces.append("hummus")
        self.sandwich._sauces.append("tahini")
    

class Waiter:
    def __init__(self):
        self.sandwich_buider = None 
    
    def sandwich_builder(self, builder):
        self.sandwich_buider = builder
    
    def create_sandwich(self):
        self.sandwich_buider.add_bread()
        self.sandwich_buider.add_meat()
        self.sandwich_buider.add_cheese()
        self.sandwich_buider.add_vegetables()
        self.sandwich_buider.add_sauces()
    
    def get_sandwich(self):
        return self.sandwich_buider.get_sandwich()
    
if __name__ == '__main__':
    waiter = Waiter()
    waiter.sandwich_builder(ClubSandwichBuilder())
    waiter.create_sandwich()
    print("======CLUB SANDWICH =======")
    sandwich = waiter.get_sandwich()
    print(sandwich)

    waiter = Waiter()
    waiter.sandwich_builder(VeggieSandwichBuilder())
    waiter.create_sandwich()
    print("======VEGGIE SANDWICH =======")
    sandwich = waiter.get_sandwich()
    print(sandwich)







