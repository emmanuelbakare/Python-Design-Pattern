class Singleton:
    __instance = None 

    def __new__(cls):
        if Singleton.__instance is None:
            Singleton.__instance = super().__new__(cls)
        return Singleton.__instance

    def __init__(self):
        print("class initialized ",self)


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
        