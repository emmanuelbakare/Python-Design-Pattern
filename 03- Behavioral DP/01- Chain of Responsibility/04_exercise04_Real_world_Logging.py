from abc import ABC, abstractmethod
import logging


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class LogHandler(ABC):
    def __init__(self, level):
        self.level = level
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor
    
    @abstractmethod
    def handle_log(self, message, level):
        pass
    

class InfoLogHandler(LogHandler):
   def handle_log(self, message, level):
        if level == logging.INFO:
            print(f"{bcolors.OKGREEN}InfoLogHandler: {message} {bcolors.ENDC}" )
        elif self.successor is not None:
            self.successor.handle_log(message, level)

class WarningLogHandler(LogHandler):
    def handle_log(self, message, level):
        if level == logging.WARNING:
            print(f"{bcolors.WARNING}WarningLogHandler:{message} {bcolors.ENDC}" )
        elif self.successor is not None:
            self.successor.handle_log(message, level)

class ErrorLogHandler(LogHandler):
    def handle_log(self, message, level):
        if level == logging.ERROR:
            print(f"{bcolors.FAIL}ErrorLogHandler:{message} {bcolors.ENDC}")
        elif self.successor is not None:
            self.successor.handle_log(message, level)
        else:
            print("Message was not handled: ")

class Logger:
    def __init__(self):
        self.info_handler = InfoLogHandler(logging.INFO)
        self.warning_handler = WarningLogHandler(logging.WARNING)
        self.error_handler = ErrorLogHandler(logging.ERROR)

        self.info_handler.set_successor(self.warning_handler)
        self.warning_handler.set_successor(self.error_handler)

    def log(self, message, level):
        self.info_handler.handle_log(message, level)


logger = Logger()

logger.log("This is an information message.", logging.INFO)
logger.log("This is a warning message.", logging.WARNING)
logger.log("This is an error message.", logging.ERROR)
logger.log("This is a debug message.", logging.DEBUG)