''' 
logger class that stores different log messages and the date it was generated

'''

from datetime import datetime

class Logger:

    __instance = None

    @staticmethod
    def get_instance(filename):
        if Logger.__instance is None:
            Logger(filename)
        return Logger.__instance
    
    def __init__(self, filename):
        if Logger.__instance is not None:
            raise Exception("Logger is a singleton")
        else:
            print("initializing file...")
            self.__filename = filename
            Logger.__instance = self

    def __store_log(self,msg):
        with open(self.__filename, 'a') as file:
            file.write(f"[{datetime.today()}] - {msg}\n")

    # info, warning, error, critical
    def info(self, msg):
        self.__store_log(f"INFO: {msg}")
    
    def warning(self, msg):
        self.__store_log(f"WARNING: {msg}")
    
    def error(self, msg):
        self.__store_log(f"ERROR: {msg}")
    
    def critical(self, msg):
        self.__store_log(f"CRITICAL: {msg}")
    

log1 = Logger.get_instance("file1.txt")

log1.info("This is an information")
log1.warning("Warning of a impending danger")
log1.error("This is an error")
log1.critical("This is a critical Mistake")


log2 = Logger.get_instance("file2.txt")
log2.info("2. --- This is an information")
log2.warning("2. --- Warning of a impending danger")
log2.error("2. --- This is an error")
log2.critical("2. --- This is a critical Mistake")