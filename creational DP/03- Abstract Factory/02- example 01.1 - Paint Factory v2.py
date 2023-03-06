from abc import ABC, abstractmethod

#RED PAINT PRODUCT
class AbstractProduct(ABC):

    @abstractmethod
    def paint(self):
        pass 

class ProductDarkRed(AbstractProduct):
    def paint(self):
        return "Dark Red Paint Product"

class ProductLightRed(AbstractProduct):
    def paint(self):
        return "Light Red Paint Product"

class ProductDarkBlue(AbstractProduct):
    def paint(self):
        return "Dark Blue Paint Product"

class ProductLightBlue(AbstractProduct):
    def paint(self):
        return "Light Blue Paint Product"

class ProductDarkGreen(AbstractProduct):
    def paint(self):
        return "Dark Green Paint Product"

class ProductLightGreen(AbstractProduct):
    def paint(self):
        return "Light Green Paint Product"


#Paint Creator and Factory -- Light and Dark Paint

class PaintCreator(ABC):

    @abstractmethod
    def red_paint_factory(self):
        pass

    @abstractmethod
    def blue_paint_factory(self):
        pass

    @abstractmethod
    def green_paint_factory(self):
        pass

#DARK PAINT FACTORY
class DarkPaintCreatorFactory(PaintCreator):
    def red_paint_factory(self):
        return ProductDarkRed()
    
    def blue_paint_factory(self):
        return  ProductDarkBlue()
    
    def green_paint_factory(self):
        return  ProductDarkGreen()

#LIGHT PAINTS FACTORY
class LightPaintCreatorFactory(PaintCreator):
    def red_paint_factory(self):
        return ProductLightRed()
    
    def blue_paint_factory(self):
        return  ProductLightBlue()
    
    def green_paint_factory(self):
        return  ProductLightGreen()

class Client:
    def __init__(self, factory:PaintCreator):
        self.factory = factory 

    def show_paints(self):
        red = self.factory.red_paint_factory()
        blue = self.factory.blue_paint_factory()
        green = self.factory.green_paint_factory()

        print(red.paint())
        print(blue.paint())
        print(green.paint())

if __name__=="__main__":
    darkpaints = Client(DarkPaintCreatorFactory())
    darkpaints.show_paints()
    print()
    lightpaints = Client(LightPaintCreatorFactory())
    lightpaints.show_paints() 

