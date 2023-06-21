# Element interface
from abc import ABC, abstractmethod

# Visitor interface
class DocumentVisitor(ABC):
    @abstractmethod
    def visit_paragraph(self, paragraph):
        pass

    @abstractmethod
    def visit_heading(self, heading):
        pass
    
    @abstractmethod
    def visit_image(self, image):
        pass


class WordCounter(DocumentVisitor):
    def __init__(self):
        self.word_count = 0

    def visit_paragraph(self, paragraph):
        words = len(paragraph.text.split())
        self.word_count += words

    def visit_heading(self, heading):
        words = len(heading.text.split())
        self.word_count += words
    
    def visit_image(self, image):
        pass


# Concrete Visitor: Text Formatter
class TextFormatter(DocumentVisitor):
    def visit_paragraph(self, paragraph):
        formatted_text = f"<p>{paragraph.text}</p>"
        print(formatted_text)

    def visit_heading(self, heading):
        formatted_text = f"<h1>{heading.text}</h1>"
        print(formatted_text)

    def visit_image(self, image):
        alt_text = image.alt_text
        image_source = image.source
        formatted_text = f'<img src="{image_source}" alt="{alt_text}">'
        print(formatted_text)




class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Element: Paragraph
class Paragraph(DocumentElement):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor):
        visitor.visit_paragraph(self)

    
# Concrete Element: Heading
class Heading(DocumentElement):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor):
        visitor.visit_heading(self)

# Concrete Element: Image
class Image(DocumentElement):
    def __init__(self, source, alt_text):
        self.source = source
        self.alt_text = alt_text

    def accept(self, visitor):
        visitor.visit_image(self)








# Document class
class Document:
    def __init__(self):
        self.elements = []   #paragraph, heading, images

    def add_element(self, element):
        self.elements.append(element)

    def process(self, visitor):
        for element in self.elements:
            element.accept(visitor)



# Client code
if __name__ == '__main__':
    # Create a document
    document = Document()


    document.add_element(Paragraph("This is a paragraph."))
    document.add_element(Heading("Heading 1 and 2"))
    document.add_element(Image("image.jpg", "Alt text"))
    document.add_element(Paragraph("Another paragraph too."))

    # Process the document using visitors
    word_counter = WordCounter()

    document.process(word_counter)
    print(f"Word Count: {word_counter.word_count}") 

    print()
    text_formatter = TextFormatter()
    document.process(text_formatter)

    