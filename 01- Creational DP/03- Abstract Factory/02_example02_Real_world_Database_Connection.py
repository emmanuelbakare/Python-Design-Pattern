from abc import ABC, abstractmethod

# Database Connection 
class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLConnection(Connection):
    def connect(self):
        print("Connecting to MySQL database...")

class PostgressConnection(Connection):
    def connect(self):
        print("Connecting to Postgress database...")

# Database Cursor
class Cursor(ABC):
     @abstractmethod
     def execute(self, query: str):
        pass
     
class MySQLCursor(Cursor):
    def execute(self, query: str):
        print(f"Executing query '{query}' on MySQL")

class PostgressCursor(Cursor):
    def execute(self, query: str):
        print(f"Executing query '{query}' on Postgress")
     

# Factory for generating Connection and Cursor for specific database
class AbstractDBFactory(ABC):

    @abstractmethod
    def create_connection(self):
        pass 

    @abstractmethod
    def create_cursor(self):
        pass

class MySQLFactory(AbstractDBFactory):
    def create_connection(self):
        return MySQLConnection()
    
    def create_cursor(self):
        return MySQLCursor()
    

class PostgresFactory(AbstractDBFactory):
    def create_connection(self):
        return PostgressConnection()
    
    def create_cursor(self):
        return PostgressCursor()
    

def client():
    factories = dict(mysql =MySQLFactory, postgres = PostgresFactory)

    fact_list = ", ".join(factories)  # mysql, postgres

    while True:
        db = input(f"Enter database type ({fact_list}): ")

        if db in factories:
            break 
        print(f"This Database Does Not Exist - Try Again... ({fact_list})")

    print("="*30)
    return factories.get(db)()

if __name__ == "__main__":
    db_factory = client()
    db_connect = db_factory.create_connection()
    cursor = db_factory.create_cursor()

    db_connect.connect()   
    cursor.execute("Select * from Student") 
    

