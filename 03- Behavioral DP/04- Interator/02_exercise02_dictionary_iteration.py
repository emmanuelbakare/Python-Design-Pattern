# Iterator implements __next__(),__iter__()
# Iterator takes in an iterable (list, tuple, string etc) as parameter
class MyIterator:
    def __init__(self, iterable_data):
        self.iterable = iterable_data
        self.keys = list(iterable_data.keys())
        self.index = 0

    def __next__(self):  # python 3.x
        if self.has_next():
            key = self.keys[self.index]
            value = self.iterable[key]
            self.index += 1
            return key,value
        else:
            raise StopIteration
    
    def next(self): # python 2.x
        return self.__next__()

    def has_next(self):
        return self.index < len(self.iterable)    
    
    
    def __iter__(self):
        return self


# Client Code 
if __name__ == '__main__':

    #iterable - List, tuple, dictionary etc
    lst1= ["Sola","Deji","Maxwell","Simon"]
    lst2 = ("House","Cars","Cash","Management")
    lst3 = "Python"
    lst4= {"name":"Sola", "age":34,"gender":"male","level":300}

    iterator = MyIterator(lst4)

    
    for key,value in iterator:
        print(f"{key} : {value}") 
      

    
     
         

     
    
    

