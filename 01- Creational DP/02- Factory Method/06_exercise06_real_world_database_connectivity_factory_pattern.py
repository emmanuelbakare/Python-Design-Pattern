from abc import ABC, abstractmethod

######## FACTORY DP###################
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
 
 

class DatabaseFactory:
    def __init__(self):
        self.factory = dict(mysql=MySQLConnection, postgresql=PostgreSQLConnection, oracle=OracleConnection)

    def create_connection(self,db_name):
        if db_name in self.factory:
            connection = self.factory.get(db_name)()
            return connection



#5. Client Code
if __name__ == '__main__':
    db_factory = DatabaseFactory()

    mysql = db_factory.create_connection("mysql") 
    print(mysql.connect())

    pgress = db_factory.create_connection("postgresql")
    print(pgress.connect())

    oracle = db_factory.create_connection("oracle")
    print(oracle.connect())

