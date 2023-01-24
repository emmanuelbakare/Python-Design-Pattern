class Singleton:
    class __Singleton:
        def __init__(self):
            self.value = None 

        def __str__(self):
            return "{0!r} {1}".format(self,self.value)
        
        #logging script 
        print('Logging Here')

    instance = None 

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance 

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self,name):
        return setattr(self.instance,name)

s1 = Singleton() 
s2 = Singleton()
print(s1, s2)
print(s1 is s2)