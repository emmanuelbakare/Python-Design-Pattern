from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log(self, message):
        pass 

class ConsoleLogger(Logger):
    def log(self, message):
        print(message) 

class FileLogger(Logger):

    def log(self, message):

        with open('filelog.txt', 'a') as file:
            file.write(message,'\n')

class FactoryLogger(ABC):

    @abstractmethod
    def create_logger(self):
        pass 

class ConsoleLoggerFactory(FactoryLogger):

    def create_logger(self):
        return  ConsoleLogger() 
    
class FileLoggerFactory(FactoryLogger):

    def create_logger(self):
        return  FileLogger() 
    

def client():

    factories = dict(console =ConsoleLoggerFactory, file=FileLoggerFactory)
    factory_list = ", ".join(factories)
    
    while True:
        logger_type = input(f"Choose Logger {factory_list} : ")

        if logger_type in factories:
            break 
    
    logger_factory = factories[logger_type]()
    return logger_factory.create_logger()

if __name__ == "__main__":
    message= input("Message to Log : ")

    logger= client()
    logger.log(message)

    


            


client()
    

    