from abc import ABC, abstractmethod
import os

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class FileSystemIterator(Iterator):
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.stack = [root_directory]
    
    def has_next(self):
        return bool(self.stack)
    
    def next(self):
        if not self.has_next():
            raise StopIteration
        
        current_path = self.stack.pop()
        if os.path.isdir(current_path):
            subdirectories = os.listdir(current_path)
            for subdirectory in subdirectories:
                self.stack.append(os.path.join(current_path, subdirectory))
        return current_path
    
class FileSystemTraversal:
    def __init__(self, root_directory):
        self.root_directory = root_directory
    
    def traverse(self):
        return FileSystemIterator(self.root_directory)
    
#client code 
root_directory = "C:\codes\python"

file_system_traversal = FileSystemTraversal(root_directory)
iterator = file_system_traversal.traverse()

while iterator.has_next():
    path = iterator.next() 
    print(path)
