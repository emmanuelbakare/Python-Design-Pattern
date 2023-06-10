# Iterator implements __next__(),__iter__()
# Iterator takes in an iterable (list, tuple, string etc) as parameter
class MyIterator:
    def __init__(self, iterable_data):
        self.iterable = iterable_data
        self.index = 0

    def __next__(self):  # python 3.x
        if self.has_next():
            item = self.iterable[self.index]
            self.index += 1
            return item
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
    lst= ["Sola","Deji","Maxwell","Simon"]

    iterator = MyIterator(lst)

    print("Iterator For Loop")
    print("*"*18)
    print("Index:", iterator.index)
    for item in iterator:
        print(item) 
    print()

    # iterator.index = 0
    print("Index:", iterator.index)
    print("Iterator While Loop")
    print("*"*18)
    
    while iterator.has_next():
        
        print(iterator.next()) 

    
     
         

     
    
    

