from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[ConsoleLogger] {message}")

class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as file:
            file.write(f"[FileLogger] {message}\n")

class DatabaseLogger(Logger):
    def log(self, message):
        # Database logging implementation
        print(f"[DatabaseLogger] {message}")

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()
    
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()
    
class DatabaseLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return DatabaseLogger()
    
# Client code
def perform_logging(factory: LoggerFactory, message: str):
    logger = factory.create_logger()
    logger.log(message)


console_logger_factory = ConsoleLoggerFactory()
perform_logging(console_logger_factory,"This is a console log message.")

file_logger_factory = FileLoggerFactory()
perform_logging(file_logger_factory, "This is a file log message.")

print()
database_logger_factory = DatabaseLoggerFactory()
perform_logging(database_logger_factory, "This is a database log message.")
