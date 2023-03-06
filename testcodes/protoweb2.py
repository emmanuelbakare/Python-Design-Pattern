import copy
class Webpage:

    def __init__(self):
        self.header = None
        self.content = None
        self.footer = None 

    def page(self):
        return  f'{self.header} {self.content}{self.footer}'
       
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
home.header= "<heading> This is the heading for HOME </heading>"
home.content= "<body> Body content for HOME goes here </body>"
home.footer= "<footer>This is the Footer for HOME </footer>"

# create page from this 
pg = PageMaker() 
pg.register_page("home", home)
about = pg.create_page("home",
                       header="<head2>This is the new header for About us </head2>",
                       content = "<div class='moral'>This page is for the morals </div>",
                       footer = "<footer>This is the Footer for ABOUT US </footer>")

print("====HOME PAGE========")
print(home.page() )
print("====ABOUT PAGE========")
print(about.page() )  