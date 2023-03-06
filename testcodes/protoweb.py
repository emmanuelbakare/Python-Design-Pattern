import copy
class Webpage:

    def __init__(self):
        self.header = None
        self.footer = None 


    def set_page(self, ctype,content):
        setattr(self, ctype, content )
    
    def contents(self):
        return "".join([web for name, web in self.__dict__.items() if name not in ('header','footer')])
    def page(self):
        return  f' {self.header} {self.contents()}{self.footer}'
       
#         return f"{self.header}{self.body}{self.footer}"
class PageMaker:
    
    def __init__(self):
        self._page = {}
    
    def register_page(self, name, page):
        self._page[name] = page 
        
    def unregister_page(self, name):
        del self._page[name] 
        
    def create_page(self,name, **contents):
        webpage = copy.deepcopy(self._page.get(name))
        webpage.__dict__.update(contents)
        return webpage
        
home = Webpage()
home.set_page("header","<header> HOME PAGE heading</header>")
home.set_page("moral","<p>This is the moral section of the page</p>")
home.set_page("body","<body> Put in all the body and images needed</body>")
home.set_page("footer","<footer>Thank you for coming</footer>")
home.set_page("section","<section> This is the section of the program </section>")


# create page from this 
pg = PageMaker() 
pg.register_page("home", home)
about = pg.create_page("home", 
                       header="<head2>This is the new header for About us </head2>",
                       moral = "<div class='moral'>This page is for the morals </div>")
about.set_page("section","<section> A NEW SECTION FOR ABOUT US</section>")
print("====HOME PAGE========")
print(home.page() )
print("====ABOUT PAGE========")
print(about.page() )