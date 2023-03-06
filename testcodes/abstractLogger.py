from abc import ABC, abstractmethod



class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def get_color(self, ctype="WARNING"):
        return getattr(self, ctype, None)


class Logger(ABC):
    
    @abstractmethod
    def log(self, message):
        pass 
    

class FileLogger(Logger):
    def log(self, message, ctype="WARNING"):
        with open('file.txt', 'a') as file:
            file.write(f'{ctype} - {message}\n')

class ConsoleLogger(Logger):
    def log(self, message, ctype="OKBLUE"):
        color = Colors()
        # print(f"{Colors.get_color('OKGREEN')}{message}{Colors.get_color('ENDC')}")
        print(color.get_color(ctype), message, color.get_color("ENDC"))

# ===============ABSTRACT FACTORY=============================       

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self):
        pass 

class ConsoleLoggerFactory(LoggerFactory):
    
    def create_logger(self):
        return ConsoleLogger() 

class FileLoggerFactory(LoggerFactory):
    
    def create_logger(self):
        return FileLogger() 
    




def client():
    factories = dict(console=ConsoleLoggerFactory, file=FileLoggerFactory)
    logger_list= ", ".join(factories)

    
    while True:
        logger_type = input(f"Log to ({logger_list}): ")
        
        if logger_type in factories:
            break
    
    logger= factories[logger_type]()
    return logger.create_logger()


if __name__ == "__main__":
    message= input("Message to Log: Type some Logs : ")
    logger= client()
    logger.log(message)
    

            