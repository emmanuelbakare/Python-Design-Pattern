def male(cls):
    cls.gender = "male"
    return cls

def female(cls):
    cls.gender = "female"
    return cls

@female
class Person:
    pass 


# print(p.__dict__)
print(Person.__dict__) 