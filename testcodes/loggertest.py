from datetime import datetime
class Logger:

    __instance = None

    @classmethod
    def get_logger(cls, filename):
        if cls.__instance is None:
            Logger(filename)
        return cls.__instance

    def __init__(self, filename):
        if Logger.__instance is not None:
            raise Exception("Logger is a singleton")
        else:
            print("initializing new logger")
            self.__filename = filename 
            Logger.__instance = self

    
    def __write_log(self, msg):
        with open(self.__filename,'a') as file:
            file.write(f'{msg}\n')
    
    def info(self,msg):
        self.__write_log(f"INFO: {datetime.today()}- {msg}")
    
    def error(self,msg):
        self.__write_log(f"ERROR: {datetime.today()}- {msg}")
    
    def warning(self,msg):
        self.__write_log(f"WARNING: {datetime.today()}- {msg}")
    
    def critical(self,msg):
        self.__write_log(f"CRITICAL: {datetime.today()}- {msg}")

log1 = Logger.get_logger("file1.txt")
log1.info("Welcome to this information")
log1.warning("This warning is true")
log1.critical("matters of this type are critical")

log2 = Logger.get_logger("file2.txt")
log2.info("2. - Welcome to this information")
log2.warning("2. - This warning is true")
log2.critical("2. - matters of this type are critical")

    
