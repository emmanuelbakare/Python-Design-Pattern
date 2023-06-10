
class RecordIterator:
    def __init__(self, records):
        self.records = records
        self.index = 0

    def has_next(self):
        return self.index < len(self.records)
    
    def __next__(self):
        if self.has_next():
            record = self.records[self.index]
            self.index += 1
            return record
        else:
            raise StopIteration

    def next(self):
        return self.__next__()

class DatabaseResultSet(RecordIterator):
    def __init__(self, result_set):
        # self.result_set = result_set
        super().__init__(result_set)

    # more cut, add, edit
    def __iter__(self):
        return RecordIterator(self.records)

result_set = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Alice", "age": 25},
    {"id": 3, "name": "Bob", "age": 35},
]


iterator = DatabaseResultSet(result_set)

# iterator = record_set.get_iterator()

# print(iterator.next()) 
# print(iterator.next()) 
# print(iterator.next()) 


while iterator.has_next():
    record = iterator.next()
    print(record)

# for item in iterator:
#     print(item)