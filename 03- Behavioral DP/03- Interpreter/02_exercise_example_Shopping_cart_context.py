# Context class to hold the shopping cart information
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self,item_name, quantity):
        self.items[item_name] = quantity

    def get_item(self,item_name):
        return self.items.get(item_name,0)
    

class Expression:
    def interpret(self, context):
        pass

class ItemPrice(Expression):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def interpret(self, context):
        quantity = context.get_item(self.name)
        return self.price * quantity
    

class Addition(Expression):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1 
        self.expression2 = expression2

    def interpret(self, context):
        return self.expression1.interpret(context) + self.expression2.interpret(context)

    

class Subtraction(Expression):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1 
        self.expression2 = expression2

    def interpret(self, context):
        return self.expression1.interpret(context) - self.expression2.interpret(context)
    

if __name__== "__main__":
    cart = ShoppingCart()
    cart.add_item("Mango",2)
    cart.add_item("PaperRoll",7)
    cart.add_item("Deodorant",3)

    expression =  Subtraction(
        ItemPrice("Deodorant",15),
        Addition(
            ItemPrice("PaperRoll",3),
            ItemPrice("Mango", 5)
        )
    )
   
     # Deodorant(3*$15 =$45), 
    # PaperRoll(7*$3 = $21), 
    # Mango(2*5$ =$10) 
    # Total $45 - $21 + $10 =$14
    total_cost = expression.interpret(cart)

    print(f"Total Cost: ${total_cost}")