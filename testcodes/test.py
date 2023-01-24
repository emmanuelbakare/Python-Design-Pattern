from datetime import datetime
class Logger:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if Logger.__instance is None:
            print('Instantiating new logger')
            Logger.__instance = super().__new__(cls)
        return Logger.__instance

    def __init__(self, filename):
        if Logger.__instance is None:
            print("initializing new logger")
        self.__filename = filename 
    
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

log1 = Logger("file1.txt")
log1.info("Welcome to this information")
log1.warning("This warning is true")
log1.critical("matters of this type are critical")

log2 = Logger("file2.txt")
log2.info("2. - Welcome to this information")
log2.warning("2. - This warning is true")
log2.critical("2. - matters of this type are critical")

    
