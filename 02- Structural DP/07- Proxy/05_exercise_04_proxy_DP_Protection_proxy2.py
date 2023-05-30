from abc import ABC, abstractmethod
from random import randint

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass 

    @abstractmethod
    def withdraw(self, amount):
        pass 

    @abstractmethod
    def get_balance(self):
        pass 


class RealBankAccount(BankAccount):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount 
    
    def withdraw(self, amount):
        if amount <= self._balance: 
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self._balance   
    

class BankAccountProxy(BankAccount):
    def __init__(self):
        self.real_account = None
        self._username = input("Enter Username: ")
        self._password = input("Enter Password: ")

    def authenticated(self):
        dbuser_password = self.password_source(self._username)

        if dbuser_password == self._password:
            if not self.real_account:
                self.real_account = RealBankAccount(randint(1000000,9999999), 0)
                print()
                print("ACCOUNT: ", self.real_account._account_number)
                print("="*20)
            return True
        else:
            raise ValueError("Authentication failed") 
        
    def deposit(self, amount):
        if self.authenticated():
            self.real_account.deposit(amount)

    def withdraw(self, amount):
        if self.authenticated():
            self.real_account.withdraw(amount)
    
    def get_balance(self):
        if self.authenticated():
            return self.real_account.get_balance()
            
    def password_source(self,pwd):
        pwd_list = {
            "user1": "pass1",
            "user2": "pass2",
            "admin": "admin",
        }

        return pwd_list.get(pwd)
    


## client code

   
account1 = BankAccountProxy()

try:
    to_deposit = 1000
    to_withdraw = 120

    account1.deposit(to_deposit)
    print(f"Balance: ${account1.get_balance()}")

    print(f"Make Withdrawal of ${to_withdraw}")
    account1.withdraw(to_withdraw)
    print(f"Balance: ${account1.get_balance()}")
    print("*"*18)
except ValueError as e:
     print(e)



account2 = BankAccountProxy()

try:
    to_deposit = 3000
    to_withdraw = 1120

    account2.deposit(to_deposit)
    print(f"Balance: ${account2.get_balance()}")

    print(f"Make Withdrawal of ${to_withdraw}")
    account2.withdraw(to_withdraw)
    print(f"Balance: ${account2.get_balance()}")
    print("*"*18)
except ValueError as e:
     print(e)



