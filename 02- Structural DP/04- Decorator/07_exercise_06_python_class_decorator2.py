def gender(gtype):
    def wrapper(cls):
        cls.gender = gtype
        return cls
    return wrapper


@gender("Male") 
class Person:
    pass 


# print(p.__dict__)
print(Person.__dict__) 