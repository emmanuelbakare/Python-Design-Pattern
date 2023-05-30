
class User:
    def __init__(self,username, password, two_factor_code):
        self.username = username
        self.password = password
        self.two_factor_code = two_factor_code


class Authenticator:
    def __init__(self, user):
        self.user = user

    def authenticate(self,password):
        pass 

class PasswordAuthenticator(Authenticator):

     def authenticate(self,password):
         if self.user.password == password:
            print(f"User {self.user.username} authenticated successfully.")
            return True
         else:
            print("Incorrect password.")
            return False
         
class TwoFactorAuthenticator(Authenticator):
    def authenticate(self, password):
        if self.user.password == password:
            two_factor_code =input("Enter two-factor authentication code: ")
            if self.user.two_factor_code == two_factor_code:
                print(f"User {self.user.username} authenticated successfully.")
                return True 
            else:
                print("Two Factor unthentication Incorrect")
                return False
        else:
            print("Password Incorrect")
            return False









         
user = User("alice", "password123", "123456")
two_factor = TwoFactorAuthenticator(user)

two_factor.authenticate("password123")