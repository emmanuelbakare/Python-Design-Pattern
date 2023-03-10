from abc import ABC, abstractmethod

class WebsiteBuilder(ABC):

    @abstractmethod
    def build_header(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_footer(self):
        pass

    @abstractmethod
    def get_result(self):
        pass 

class HomePageBuilder(WebsiteBuilder):
    def __init__(self):
        self.result = "" 

    def build_header(self):
        self.result += "<header><h1>Welcome to our Website!</h1></header>"

    def build_body(self):
        self.result += "<body><p>This is the home page.</p></body>"

    def build_footer(self):
        self.result += "<footer><p>Thanks for visiting our website!</p></footer>"

    def get_result(self):
        return self.result 


class AboutPageBuilder(WebsiteBuilder):
    def __init__(self):
        self.result = ""

    def build_header(self):
        self.result += "<header><h1>About Us</h1></header>"
    
    def build_body(self):
        self.result += "<body><p>We are a company that makes websites.</p></body>"
    
    def build_footer(self):
        self.result += "<footer><p>Thanks for visiting our about page!</p></footer>"
    
    def get_result(self):
        return self.result 
    
class WebsiteDirector:
    def __init__(self, builder):
        self.builder = builder 

    def build_website(self):
        self.builder.build_header()
        self.builder.build_body()
        self.builder.build_footer()

if __name__ == '__main__':
    print("==========PRINT HOME PAGE==============")
    home_builder = HomePageBuilder() 
    director = WebsiteDirector(home_builder)
    director.build_website()
    home_page = home_builder.get_result() 
    print(home_page)

    print()
    print("==========PRINT ABOUT US PAGE==============")
    about_builder = AboutPageBuilder()
    director = WebsiteDirector(about_builder)
    director.build_website()
    about_page = about_builder.get_result() 
    print(about_page)
