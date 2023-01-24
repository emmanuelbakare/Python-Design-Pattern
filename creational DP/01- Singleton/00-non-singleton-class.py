class NoneSingleton:

    def __init__(self):
        self.name = "None Singleton" 


ns1 = NoneSingleton()
ns2 = NoneSingleton()

print(ns1, ns2)

print(ns1 is ns2)