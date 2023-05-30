from abc import ABC, abstractmethod

# Subject interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass 

# Real subject implementation
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Processing request.")

# Protection proxy
class ProtectionProxy(Subject):
    def __init__(self, real_subject, access_level):
        self.real_subject = real_subject
        self.access_level = access_level

    def request(self):
        if self.access_level == input("Enter Pasword: "):
            self.real_subject.request()
        else:
            print("Access Denied. You don't have sufficient privileges.")


#client code 

real_subject = RealSubject()

admin_proxy = ProtectionProxy(real_subject, "admin")
admin_proxy.request()  
