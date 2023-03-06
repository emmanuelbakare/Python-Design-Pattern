class Product:
    def __init__(self):
        self.part_a =None
        self.part_b = None
        self.part_c = None
        self.part_d = None
        
    def __str__(self):
        return f"A({self.part_a}), B({self.part_b}), C({self.part_c}), D({self.part_d})"
        
class Builder:
    
    def __init__(self):
        self._product = Product()
        
    def set_part_a(self,val):
        self._product.part_a = val
        
    def set_part_b(self,val):
        self._product.part_b = val
        
    def set_part_c(self,val):
        self._product.part_c = val
        
    def set_part_d(self,val):
        self._product.part_d =val
    def get_product(self):
        return self._product

if __name__=="__main__":
    build=Builder()
build.set_part_a(10)
build.set_part_b(20)
build.set_part_c(40)
build.set_part_d(50)
print(build.get_product())