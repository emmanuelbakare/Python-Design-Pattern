class Singleton:
    _instance = None 

    def __init__(self):
        if self._instance is not None:
            raise Exception("Singleton instance already exists")
        self._instance = self

    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()  

print(s1 is s2)

print(s1)
print(s2)