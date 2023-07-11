from abc import ABC, abstractmethod

class Document(ABC): #product
    @abstractmethod
    def open(self):
        pass

class WordDocument(Document):
    def open(self):
        print("Opening Word document...")

class PdfDocument(Document):
    def open(self):
        print("Opening PDF file...")

class HtmlDocument(Document):
    def open(self):
        print("Opening HTML file...")


class DocumentFactory(ABC):  #creator -Product
    @abstractmethod
    def create_document(self) -> Document:
        pass

class WordDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return WordDocument()
    
class PdfDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PdfDocument()


class HtmlDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return HtmlDocument()
    

# Client code
def process_document(factory: DocumentFactory):
    document = factory.create_document()
    document.open()


word_factory = WordDocumentFactory()
process_document(word_factory)

pdf_factory = PdfDocumentFactory()
process_document(pdf_factory)


html_factory = HtmlDocumentFactory()
process_document(html_factory) 

