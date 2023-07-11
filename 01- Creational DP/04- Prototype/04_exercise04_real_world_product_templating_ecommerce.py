import copy

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def clone(self):
        return copy.deepcopy(self)
    

class ECommercePlatform:
    def __init__(self):
        self.prototype_products = {}

    def register_prototype(self, key, prototype_product):
        self.prototype_products[key] = prototype_product

    def create_product(self, key, name, price, category):
        prototype_product = self.prototype_products.get(key)
        if prototype_product:
            new_product = prototype_product.clone()
            new_product.name = name
            new_product.price = price
            new_product.category = category
            return new_product
        else:
            raise ValueError(f"Prototype with key '{key}' does not exist.")
        

# Usage
ecommerce_platform = ECommercePlatform()


# create product templates
clothing_product = Product("Clothing", 49.99, "Apparel")
electronics_product = Product("Electronics", 99.99, "Gadgets")

# Register prototypes
ecommerce_platform.register_prototype("clothing", clothing_product)
ecommerce_platform.register_prototype("electronics", electronics_product)

# Create products from template
product1 = ecommerce_platform.create_product("clothing","T-Shirt", 29.99, "Apparel")
product2 = ecommerce_platform.create_product("electronics","Headphones", 79.99, "Gadgets")
product3 = ecommerce_platform.create_product("electronics","iPhone", 1049.99, "Gadgets")

# Print product details
print(product1.name, product1.price, product1.category)  
print(product2.name, product2.price, product2.category)
print(product3.name, product3.price, product3.category)