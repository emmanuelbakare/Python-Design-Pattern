# Complex subsystem
class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name 
    
    def get_price(self):
        return self.price
    
class Inventory:
    def __init__(self):
        self.product_list = [] 

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)
    
    def get_products(self):
        return self.product_list

class Payment:
    def __init__(self):
        self.total = 0 

    def add_product(self, product):
        self.total +=product.get_price()

    def remove_product(self, product):
        self.total -=product.get_price()

    def get_total(self):
        return self.total
    
#facade 
class OnlineStore:

    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()

    def add_product_to_cart(self, name, price):
        product = Product(name, price)
        self.inventory.add_product(product)
        self.payment.add_product(product)
        

    def remove_product_from_cart(self, name):
        products = self.inventory.get_products()

        for product in products:
            if product.get_name() == name:
                self.inventory.remove_product(product)
                self.payment.remove_product(product)
                break

    def checkout(self):
        total = self.payment.get_total()
        print(f"Total amount due: ${total}")

    def cart_list(self):
        print("Product \t Price")
        print("*"*25)
        products = self.inventory.get_products()

        for product in products:
            print(f"{product.get_name()}\t\t ${product.get_price()}")
        print("*"*25)
# Client
if __name__ == '__main__':
    store = OnlineStore()
    store.add_product_to_cart("Shirt", 20)
    store.add_product_to_cart("Pants", 30)
    store.add_product_to_cart("Skirts", 35)
    store.add_product_to_cart("Shoe", 135)

    store.remove_product_from_cart("Shirt")
    store.cart_list()
    store.checkout()


    