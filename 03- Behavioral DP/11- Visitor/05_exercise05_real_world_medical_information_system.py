# Medical Information System  (Object Structure)
#     |_Medical data Elements
#       * Sympton
#       * Test results
#       * Medical History 
#     |
#     |___ Operations (visitors)
#       * Data Analyser
#       * Diagnostics
#       * Record Processing
from abc import ABC, abstractmethod

class MedicalInformationSystem:
    def __init__(self):
        self.medical_data = []
    
    def add_medical_data(self, data):
        self.medical_data.append(data)

    def process_data(self, visitor):
        for data in self.medical_data:
            data.accept(visitor)


# Element interface
class MedicalData(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Element: Symptoms
class Symptoms(MedicalData):
    def accept(self, visitor):
        visitor.visit_symptoms(self)
    
# Concrete Element: TestResults
class TestResults(MedicalData):
    def accept(self, visitor):
        visitor.visit_test_results(self)

# Concrete Element: MedicalHistory
class MedicalHistory(MedicalData):
    def accept(self, visitor):
        visitor.visit_medical_history(self)



# Visitor interface
class MedicalVisitor(ABC):
    @abstractmethod
    def visit_symptoms(self, symptoms):
        pass
    
    @abstractmethod
    def visit_test_results(self, test_results):
        pass
    
    @abstractmethod
    def visit_medical_history(self, medical_history):
        pass


# Concrete Visitor: DataAnalyzer
class DataAnalyzer(MedicalVisitor):
    def visit_symptoms(self, symptoms):
        # Analyze symptoms data
        print("Analyzing symptoms data")

    def visit_test_results(self, test_results):
        # Analyze test results data
        print("Analyzing test results data")

    def visit_medical_history(self, medical_history):
        # Analyze medical history data
        print("Analyzing medical history data")


# Concrete Visitor: Diagnoser
class Diagnoser(MedicalVisitor):
    def visit_symptoms(self, symptoms):
        # Perform diagnosis based on symptoms
        print("Performing diagnosis based on symptoms")

    def visit_test_results(self, test_results):
        # Perform diagnosis based on test results
        print("Performing diagnosis based on test results")

    def visit_medical_history(self, medical_history):
        # Perform diagnosis based on medical history
        print("Performing diagnosis based on medical history")

# Concrete Visitor: RecordProcessor
class RecordProcessor(MedicalVisitor):
    def visit_symptoms(self, symptoms):
        # Process symptoms record
        print("Processing symptoms record")

    def visit_test_results(self, test_results):
        # Process test results record
        print("Processing test results record")

    def visit_medical_history(self, medical_history):
        # Process medical history record
        print("Processing medical history record")


# Client code
if __name__ == '__main__':
    # Create a medical information system
    medical_system = MedicalInformationSystem()


     # Add medical data to the system
    symptoms = Symptoms()
    test_results = TestResults()
    medical_history = MedicalHistory()


    medical_system.add_medical_data(symptoms)
    medical_system.add_medical_data(test_results)
    medical_system.add_medical_data(medical_history)

    
    # Process data using visitors
    analyzer = DataAnalyzer()
    medical_system.process_data(analyzer)  
    print()
    diagnoser = Diagnoser()
    medical_system.process_data(diagnoser)


    print()
    record_processor = RecordProcessor()
    medical_system.process_data(record_processor)

