from abc import ABC, abstractmethod

#Reciever 
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


################################################
#Command
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class DepositCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)

    def undo(self):
        self.account.withdraw(self.amount)

class WithdrawCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.withdraw(self.amount) 

    def undo(self):
        self.account.deposit(self.amount)



 
################################################
#Invoker

class TransactionManager:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last_command(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()



################################################
#client

account = BankAccount("123456789", 1000.0)
transaction_manager = TransactionManager()

transaction_manager.execute_command(DepositCommand(account, 500.0))
transaction_manager.execute_command(WithdrawCommand(account, 200.0))
account.display_balance()  
print()
transaction_manager.undo_last_command()
account.display_balance()