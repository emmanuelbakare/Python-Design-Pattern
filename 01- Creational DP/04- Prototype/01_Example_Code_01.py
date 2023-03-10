import copy

class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y 

class Prototype:
    def __init__(self):
        self._obj = {}

    def register_object(self, name, obj):
        self._obj[name] = obj

    def unregister_object(self, name):
        del self._obj[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._obj.get(name))
        obj.__dict__.update(attr)
        return obj

if __name__ =="__main__":
    sq = Square(10,20)
    proto = Prototype()
    proto.register_object("square", sq)
    rec = proto.clone("square",x= 100, y =200)
    cube = proto.clone("square",x= 500, y =1000, z = 1500)
    print("SQUARE : ", sq.__dict__,", RECTANGLE", rec.__dict__,", CUBE: ", cube.__dict__)

    

    

 

    

    





