class Product:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
    
    def __str__(self):
        return f"A : ({self.a}), B : ({self.b}),C : ({self.c})"

class Builder:
    def __init__(self):
        self._product = Product()

    def part_a(self):
        pass

    def part_b(self):
        pass

    def part_c(self):
        pass

    def get_product(self):
        return self._product

class ConcreteBuilder1(Builder):
    def part_a(self):
        self._product.a = "A1"
    
    def part_b(self):
        self._product.b = "B1"
    
    def part_c(self):
        self._product.c = "C1"

class ConcreteBuilder2(Builder):
    def part_a(self):
        self._product.a = "A2"
    
    def part_b(self):
        self._product.b = "B2"
    
    def part_c(self):
        self._product.c = "C2"

class Director:
    def __init__(self):
        self.builder = None 
    
    def create_builder(self, builder):
        self.builder = builder
    
    def construct_product(self):
        self.builder.part_a()
        self.builder.part_b()
        self.builder.part_c()

if __name__=="__main__":
    director = Director()
    director.create_builder(ConcreteBuilder1())
    director.construct_product()
    product1 = director.builder.get_product()
    print(product1)

    director.create_builder(ConcreteBuilder2())
    director.construct_product()
    product2 = director.builder.get_product()
    print(product2)
    