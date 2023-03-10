from abc import ABC, abstractmethod

#RED PAINT PRODUCT
class AbstractProductRed(ABC):

    @abstractmethod
    def paint_red(self):
        pass 

class ProductDarkRed(AbstractProductRed):
    def paint_red(self):
        return "Dark Red Paint Product"

class ProductLightRed(AbstractProductRed):
    def paint_red(self):
        return "Light Red Paint Product"

# BLUE PAINT PRODUCT
class AbstractProductBlue(ABC):

    @abstractmethod
    def paint_blue(self):
        pass 

class ProductDarkBlue(AbstractProductBlue):
    def paint_blue(self):
        return "Dark Blue Paint Product"

class ProductLightBlue(AbstractProductBlue):
    def paint_blue(self):
        return "Light Blue Paint Product"

#GREEN PAINT PRODUCT
class AbstractProductGreen(ABC):

    @abstractmethod
    def paint_green(self):
        pass 

class ProductDarkGreen(AbstractProductGreen):
    def paint_green(self):
        return "Dark Green Paint Product"

class ProductLightGreen(AbstractProductGreen):
    def paint_green(self):
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

        print(red.paint_red())
        print(blue.paint_blue())
        print(green.paint_green())

if __name__=="__main__":
    darkpaints = Client(DarkPaintCreatorFactory())
    darkpaints.show_paints()
    print()
    lightpaints = Client(LightPaintCreatorFactory())
    lightpaints.show_paints()

