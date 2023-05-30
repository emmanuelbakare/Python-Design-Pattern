credential = {
    "user":"Collins",
    "password":"pass",
    "password2":"pass2"
}


def login_required(cls):
    def wrapper(*args, **kwargs):
        xpass = credential.get("password")
        ipass = input("Enter password: ")
        if xpass == ipass:
            return cls(*args, **kwargs)
        else:
            return None

    return wrapper

def two_factor_login_required(cls):
    def wrapper(*args, **kwargs):
        xpass = credential.get("password") 
        ipass = input("Enter Password: ")

        if xpass == ipass:
            xpass2 = credential.get("password2")
            ipass2 = input("Enter Your 2nd Password: ")
            if xpass2 == ipass2:
                return cls(*args, **kwargs)
            else:
                return None
        else:
            return None

    return wrapper


# @login_required
@two_factor_login_required
class Person:
    def __init__(self, name):
        self.name  = name
        
    def __str__(self):
        return self.name
    

person = Person("Collins James")
print(person)