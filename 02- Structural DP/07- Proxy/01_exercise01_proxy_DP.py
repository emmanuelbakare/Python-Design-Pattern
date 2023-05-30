class SubjectInterface:
    def operation(self):
        pass 

class Subject(SubjectInterface):

    def operation(self):
        print("...Implementing The Operation")


class SubjectProxy(SubjectInterface):
    def __init__(self, subject):
        self._subject  = subject 

    def operation(self):
        print("BEFORE Operation: check status")
        self._subject.operation()
        print("AFTER Operation: log status")


proxy = SubjectProxy(Subject())

proxy.operation()
