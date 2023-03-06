class Product:
    def __init__(self): 
        self.part_a = None 
        self.part_b = None 
        self.part_c = None 
        self.part_d = None 
    
    def __str__(self):
        return f"A ({self.part_a}), B({self.part_b}), C({self.part_c}), D({self.part_d})"

class ProductBuilder:
    def __init__(self):
        self._product = Product() 
    
    def set_part_a(self, val):
        self._product.part_a = val 
    
    def set_part_b(self, val):
        self._product.part_b = val

    def set_part_c(self, val):
        self._product.part_c = val

    def set_part_d(self, val):
        self._product.part_d = val
    
    def get_product(self):
        return self._product
    
if __name__=="__main__":
    build = ProductBuilder()
    build.set_part_a(10)
    build.set_part_b(20)
    build.set_part_c(30)
    build.set_part_d(40)

    product = build.get_product()

    print(product)
    print("*"*50)
    build = ProductBuilder()
    build.set_part_a(100)
    build.set_part_b(200)
    build.set_part_c(300)
    build.set_part_d(400)

    product = build.get_product()

    print(product)
    
 
