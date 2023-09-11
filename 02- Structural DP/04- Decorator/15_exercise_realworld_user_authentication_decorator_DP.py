
from abc import ABC, abstractmethod 
class User:
    def __init__(self, username, password, two_factor_pass):
        self.username = username
        self.password = password 
        self.two_factor_pass = two_factor_pass

class Authenticator(ABC):
    def __init__(self, user):
        self.user = user 
    
    @abstractmethod
    def authenticate(self, password):
        pass 

class PasswordAuthenticator(Authenticator):

    def authenticate(self, password):
        if self.user.password == password:
            print(f"User {self.user.username} is authenticated successfully")
            return True
        else:
            print(f" user '{self.user.username}' authentication FAILED!!!")
            return False 
        
class TwoWayAuthenticator(Authenticator):
    def authenticate(self, password):
        if self.user.password == password:
            print("1st Level Authentication passed")

            pass2 = input("Enter 2nd Level Authentication: ")
            if self.user.two_factor_pass == pass2:
                print("1st Level Authentication passed")
                print(f"User '{self.user.username}' is authenticated successfully")
                return True
            else:
                print("Authentication failed on 2nd Level")
                return False
        else:
            print("Authentication Failed on 1st Level")
            return False 


user = User("user1","pass","pass123")
# auth = PasswordAuthenticator(user)
# auth.authenticate("pass") 
auth2 = TwoWayAuthenticator(user)
auth2.authenticate("pass")
            
            

        

    