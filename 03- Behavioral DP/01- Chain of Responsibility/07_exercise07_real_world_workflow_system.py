from abc import ABC, abstractmethod
    
class WorkflowStep(ABC):
    def __init__(self, successor=None):
        self.successor = successor
        
    @abstractmethod
    def process(self, data):
        pass

class DataValidationWorkflow(WorkflowStep):
    def process(self, data):
        if self.validate(data):
            print("DataValidationWorkflow: Data is valid.")
            if self.successor is not None:
                self.successor.process(data)
        else:
            print("DataValidationWorkflow: Data validation failed.")

    def validate(self,data):
        return isinstance(data, str)

class DataTransformationWorkflow(WorkflowStep):
    def process(self, data):
        transformed_data = self.transform(data)
        print("DataTransformationWorkflow: Data transformed successfully.")
        if self.successor is not None:
            self.successor.process(transformed_data)

    def transform(self, data):
        return f"__{data.upper()}__"

class DataPersistenceWorkflow(WorkflowStep):
    def process(self, data):
        Database.writer(data)
        print("DataPersistenceWorkflow: Data persisted successfully.")

         

class Database:
    @staticmethod
    def writer(data):
        with open('database.txt', 'a') as datafile:
            datafile.write(data+"\n")
    
    @staticmethod
    def reader():
        data = ""
        with open('database.txt') as datafile:
            data = datafile.readlines()
        return [rec.strip('\n') for rec in data]

workflow = DataValidationWorkflow(DataTransformationWorkflow(DataPersistenceWorkflow()))

names22 = ["Matthew",43.22,"Malik","Bakare",23,"Daniel"]

names = ["Caroline","Brown","Bjorn",True]

for name in names:
    workflow.process(name)

print()
print("DATABASE RECORDS".center(30,"#"))
print(Database.reader())