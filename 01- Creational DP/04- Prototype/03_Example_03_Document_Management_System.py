import copy

class Document:
    def __init__(self, title, content, font, font_size, logo):
        self.title = title
        self.content = content
        self.font = font
        self.font_size = font_size
        self.logo = logo

    def __str__(self):
        return f"Title : {self.title}\nContent: {self.content}\nFont:{self.font}\nFont size: {self.font_size}\nLogo: {self.logo}"
    
    
    


class DocumentMaker:

    def __init__(self):
        self._document ={}
    
    def register_document(self, name, obj):
        self._document[name] = obj

    def unregister_document(self, name):
        del self._document[name]

    def create_document(self, name, **attrs):
        new_document = copy.deepcopy(self._document.get(name))
        new_document.__dict__.update(attrs)
        return new_document

if __name__=="__main__":
    prototype = DocumentMaker()

    prototype.register_document("contract", Document("Payment contract","Terms and conditions", "Arial", 12, "Company Logo"))
    prototype.register_document("report", Document("Report", "Quarterly Sales", "Times New Roman", 14, "Company Logo"))
    prototype.register_document("presentation", Document("Presentation", "New Product Launch", "Calibri", 16, "Company Logo"))

    computer_contract = prototype.create_document("contract",
                                                  title="Computer Server Contract",
                                                  content = "Buy 10 computer server for Unix and Windows Systems")
    
    monthly_report = prototype.create_document("report", 
                                               title="Monthly Report 2023", 
                                               content="Monthly Financial Report for June 2023")
    monthly_report_2 = prototype.create_document("report", 
                                               title="Monthly Report 2023 Quarter 1", 
                                               content="Monthly Financial Report for Jan - March 2023")
    Python_presentation = prototype.create_document("presentation", 
                                                    title="New Product Presentation", 
                                                    content="Introducing our new product Python Product Line")
    
    print("========== MONTHLY REPORT ===============")
    print(monthly_report)
    
    print("========== MONTHLY REPORT QUARTER 1===============")
    print(monthly_report_2)

    print("========== CONTRACTS ===============")
    print(computer_contract)
    
    print("========== PRESENTATION ===============")
    print(Python_presentation)
    
   
    