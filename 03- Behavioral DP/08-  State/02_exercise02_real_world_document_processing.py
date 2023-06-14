
#state  draft -> Review -> Finalize ->Published 
from abc import ABC, abstractmethod


class DocumentState(ABC):
    @abstractmethod
    def process_document(self, document):
        pass

class DraftState(DocumentState):
     def process_document(self, document):
        print("Processing document in the Draft state.")
        # Perform operations specific to the Draft state
        document.state = ReviewState()
     
class ReviewState(DocumentState):
     def process_document(self, document):
        print("Processing document in the Review state.")
        # Perform operations specific to the Review state
        document.state = FinaliseState()
     
class FinaliseState(DocumentState):
     def process_document(self, document):
        print("Processing document in the Finalize state.")
        # Perform operations specific to the Finalize state
        document.state = PublishedState()
     
class PublishedState(DocumentState):
     def process_document(self, document):
        print("Document is already published.")
     

     






# context - document
class Document:
    def __init__(self):
        self.state = DraftState()

    def process(self):
        self.state.process_document(self)


# Usage example
document = Document()
document.process() 
document.process() 
document.process() 
document.process() 

 