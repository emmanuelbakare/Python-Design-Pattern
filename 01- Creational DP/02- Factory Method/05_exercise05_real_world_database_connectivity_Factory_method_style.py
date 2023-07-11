from abc import ABC, abstractmethod

######## FACTORY METHOD DP###################
#1. abstract product
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass


#2. concrete products  #mysql, postgreSQL, oracle
class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to MySQL Database.... Established"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to PostgreSQL Database.... Established"

class OracleConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to ORACLE Database.... Established"
    
#3. abstract Creator (Factory)
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass

#4. concrete Creators (Factory)
class MySQLConnectionFactory(DatabaseConnectionFactory):
    #4.1 Factory Method
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()

class PostgreSQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

class OracleConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return OracleConnection()

#5. Client Code
def connect_to_database(factory: DatabaseConnectionFactory):
     connection = factory.create_connection() 
     print(connection.connect())

mysql_factory = MySQLConnectionFactory()
connect_to_database(mysql_factory)

postgres_factory = PostgreSQLConnectionFactory()
connect_to_database(postgres_factory)

oracle_factory = OracleConnectionFactory()
connect_to_database(oracle_factory)