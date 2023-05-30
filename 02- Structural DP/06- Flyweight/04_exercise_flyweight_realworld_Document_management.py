
class Document:
    _created = 0
    def __init__(self, title, author,content):
        self.title = title
        self.author = author
        self.content = content
        Document._created += 1

class DocumentFactory:
    def __init__(self):
        self.docs = {} 

    def get_document(self, title, author,content):
        if (title, author) not in self.docs:
            doc = Document(title, author, content)
            self.docs[(title, author)] = doc 
        return self.docs[(title, author)]


class DocumentManager:
    def __init__(self):
        self.documents = []
        self.factory = DocumentFactory()
    
    def add_document(self, title, author, content):
        # doc = Document(title, author, content)
        doc = self.factory.get_document(title, author, content)
        self.documents.append(doc)

    def print_documents(self):
        for doc in self.documents:
            print(f"Title:", doc.title)
            print(f"Author: ", doc.author)
            print(f"Content: ", doc.content)
            print("="*25)


if __name__ == "__main__":
    document = DocumentManager()
    document.add_document("Things Fall Apart", "Chinua Achedue", "Things all apart that the center cannot hold.")
    document.add_document("Things Fall Apart", "Chinua Achedue", "Things all apart that the center cannot hold.")
    document.add_document("doc2","Matthew James", "This is another document printed")
    document.add_document("doc3","Adeolu Kola", "Document from Adeolu")
    document.add_document("doc3","Adeolu Kola", "Document from Adeolu")
    
    document.print_documents()
    print("Total Objects Created:",Document._created)