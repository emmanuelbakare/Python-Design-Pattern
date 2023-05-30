from database.mysqldb import MySQLDatabase
from database.postgresdb import PostgreSQLDatabase


# Define the Target interface

class Database:
    def insert(self, data):
        pass

    def delete(self, data):
        pass

    def update(self, data):
        pass

    def select(self, data):
        pass


class MySQLAdapter(Database):
    def __init__(self, adaptee):
        self._adaptee = adaptee 

    def insert(self, data):
        self._adaptee.mysql_insert(data)

    def delete(self, data):
        self._adaptee.mysql_delete(data)

    def update(self, data):
        self._adaptee.mysql_update(data)

    def select(self, data):
        self._adaptee.mysql_select(data)




class PostgreAdapter(Database):
    def __init__(self, adaptee):
        self._adaptee = adaptee 

    def insert(self, data):
        self._adaptee.postgresql_insert(data)

    def delete(self, data):
        self._adaptee.postgresql_delete(data)

    def update(self, data):
        self._adaptee.postgresql_update(data)

    def select(self, data):
        self._adaptee.postgresql_select(data)









if __name__=="__main__":
    mysqldb = MySQLDatabase()
    mysql_adapter = MySQLAdapter(mysqldb)
    mysql_adapter.select("RECORD 1")
    mysql_adapter.delete("RECORD 1")

    postgres_db = PostgreSQLDatabase()
    postgres_adapter = PostgreAdapter(postgres_db)

    postgres_adapter.select("RECORD 3")
    postgres_adapter.update("RECORD 4")

