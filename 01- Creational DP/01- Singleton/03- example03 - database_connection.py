'''
Implement a singleton database connection class to mysql database 

Prerequisites:
1. Make sure mysql database is installed 
2. pip install mysql-connector-python
'''

import mysql.connector 
import time


class DatabaseConnection:

    __instance = None

    @classmethod
    def get_connection(cls):
        if cls.__instance is None:
              DatabaseConnection()
        return cls.__instance 

    def __init__(self):
            if DatabaseConnection.__instance is not None:
                 raise Exception("connection already established in a singleton")
            else:
                print("initializing database connection...", end=" ")
                self.connection = mysql.connector.connect(host="localhost", database="hrm", user="admin", password="root")
                time.sleep(2)
                print("ESTABLISHED")
                DatabaseConnection.__instance = self
    
    def __str__(self):
        return f"{self.connection}"
    
#client Usage
con1 = DatabaseConnection.get_connection()
con2 = DatabaseConnection.get_connection()

print(con1 is con2)
print(f"CON 1: {con1}, CON2: {con2}")

con1.connection.close()

       

    
   
