from abc import ABC, abstractmethod


class ExceptionHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod  
    def handle_exception(self, exception):
        pass


class NullPointerHandler(ExceptionHandler):
    def handle_exception(self, exception):
        if isinstance(exception, NullPointerException):
            print("NullPointerHandler: Handling NullPointerException")
            # Perform appropriate exception handling actions
        elif self.successor is not None:
            self.successor.handle_exception(exception)


class DivideByZeroHandler(ExceptionHandler):
    def handle_exception(self, exception):
        if isinstance(exception, DivideByZeroException):
             print("DivideByZeroHandler: Handling DivideByZeroException")
            # Perform appropriate exception handling actions
        elif self.successor is not None:
            self.successor.handle_exception(exception)


class OutOfMemoryHandler(ExceptionHandler):
    def handle_exception(self, exception):
        if isinstance(exception, OutOfMemoryException):
            print("OutOfMemoryHandler: Handling OutOfMemoryException")
            # Perform appropriate exception handling actions
        elif self.successor is not None:
            self.successor.handle_exception(exception)
        else:
            print("No Handler for ", exception.__class__.__name__)


class DatabaseErrorHandler(ExceptionHandler):
    def handle_exception(self, exception):
        if isinstance(exception, DatabaseError):
            print("DatabaseErrorHandler: Handling DatabaseError")
            # Perform appropriate exception handling actions
        elif self.successor is not None:
            self.successor.handle_exception(exception)
        else:
            print("No Handler for ", exception.__class__.__name__ )
        


# Custom exceptions
class NullPointerException(Exception):
    pass

class DivideByZeroException(Exception):
    pass

class OutOfMemoryException(Exception):
    pass

class DatabaseError(Exception):
    pass 
 


null_pointer_handler = NullPointerHandler()
divide_by_zero_handler = DivideByZeroHandler()
out_of_memory_handler = OutOfMemoryHandler()
database_handler = DatabaseErrorHandler()


null_pointer_handler.successor = divide_by_zero_handler
divide_by_zero_handler.successor = out_of_memory_handler
out_of_memory_handler.successor = database_handler

# Simulating exceptions
exceptions = [
    NullPointerException(),
    DivideByZeroException(),
    OutOfMemoryException(),
    ValueError(),
    DatabaseError(),
  
]


for exception in exceptions:
    null_pointer_handler.handle_exception(exception)
