from database.mysqldb import MySQLDatabase #adaptee
from database.postgresdb import PostgreSQLDatabase #adaptee


class Database:  #target
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
    mysql_adapter = MySQLAdapter(MySQLDatabase())
    mysql_adapter.select("Record 1")
    mysql_adapter.update("Record 1")
    mysql_adapter.delete("Record 1")

    postgres_adapter = PostgreAdapter(PostgreSQLDatabase())
    postgres_adapter.select("RECORD 3")
    postgres_adapter.update("RECORD 4")

    
