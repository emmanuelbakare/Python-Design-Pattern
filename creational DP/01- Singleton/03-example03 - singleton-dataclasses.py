from dataclasses import dataclass


@dataclass(init = False)
class Singleton:
    __instance = None 
    name: str 

    def __init__(self):
        print("initializing...")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
        return cls.__instance 

s1 = Singleton()
s2 = Singleton()

s11 = Singleton.get_instance()
s22 = Singleton.get_instance()
s33 = Singleton.get_instance()

print(s1 is s2)
print(s11 is s22)
print(s11 is s33)

   

