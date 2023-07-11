class NoneSingleton:
    def __init__(self, name):
        self.name = name 

ns1 = NoneSingleton("Boy")
ns2 = NoneSingleton("Girl")

print(ns1, ns2)

print(ns1 is ns2) 

print(f"ns1: {ns1.name}, ns2: {ns2.name}")