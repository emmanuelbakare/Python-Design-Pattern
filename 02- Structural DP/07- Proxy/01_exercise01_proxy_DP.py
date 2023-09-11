from abc import ABC, abstractmethod

class SubjectInterface(ABC): # the subject
    @abstractmethod
    def operation(self):
        pass



class RealSubject(SubjectInterface): 
    def operation(self):
        print("Perform an Operation from Real Subject")



class ProxySubject(SubjectInterface):
    def __init__(self, real_subject):
        self.real_subject = real_subject
    
    def operation(self):
        print("---Perform some other actions---")
        self.real_subject.operation()


real_subject = RealSubject()
# real_subject.operation()
proxy_subject = ProxySubject(real_subject)
proxy_subject.operation()