class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):

        if Singleton.__instance != None:
            raise Exception("this is singleton")
        else:
            Singleton.__instance = self


s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 is s2)
print(s1,s2)
 