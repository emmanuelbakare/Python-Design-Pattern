# iterator
class MyCollectionIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def has_next(self):
        return self.index < len(self.iterable)
    
    def __next__(self):
        if self.has_next():
            value = self.iterable[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
        
    def next(self):
        return self.__next__()
    
    # def __iter__(self):
    #     return self
        


# aggregate 
class MyCollection:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    # def create_iterator(self):
    #     return MyCollectionIterator(self.data)
    def __iter__(self):
        return MyCollectionIterator(self.data)


collection = MyCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

# iterator = collection.create_iterator()

# while iterator.has_next():
#     item = iterator.next()
#     print(item) 

# for item in iterator:
#     print(item)

for item in collection:
    print(item)