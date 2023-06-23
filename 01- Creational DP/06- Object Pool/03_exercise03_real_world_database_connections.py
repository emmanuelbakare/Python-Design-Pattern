import sqlite3

class DatabaseConnection:
    def __init__(self,connection):
        self.connection = connection

    def query(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query,params) if params else cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def insert(self,emp):
        return self.query("INSERT INTO employee VALUES(?,?,?)",(emp.firstname,emp.lastname,emp.age))
    
    def release(self):
        # Reset connection state if necessary
        # For example, closing the cursor and committing any pending transactions
        self.connection.rollback()



class Employee:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class DatabaseConnectionPoolManager:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.available_connections = []
        self.in_use_connections = []

        self.connection = self.initialize_connection_and_db()

        for _ in range(max_connections):
            self.available_connections.append(DatabaseConnection(self.connection))

    def initialize_connection_and_db(self):
        connection = sqlite3.connect(":memory:")
        cursor = connection.cursor()
        # create employee Table
        cursor.execute("""CREATE TABLE employee 
            (firstname TEXT,
            lastname TEXT,
            age INTEGER)
            """)
        
        #populate the employees table with lists of Employee data
        employees= [
                Employee(firstname="Oladele", lastname="Ayodeji", age=32),
                Employee(firstname="Emmanuel", lastname="Bakare", age=94),
                Employee(firstname="Martins", lastname="Floyd", age=14),
        ] 

        for emp in employees:
            cursor.execute("INSERT INTO employee VALUES(?,?,?)",(emp.firstname,emp.lastname,emp.age))
        
        #close the cursor, commit the changes and return the connection
        cursor.close()  
        connection.commit() 
        return connection
    
    def acquire_connection(self):
        if self.available_connections:
            dbconnection = self.available_connections.pop()
            self.in_use_connections.append(dbconnection)
            return dbconnection
        else:
            raise Exception("No connections available in the pool.")
        
    def release_connection(self, connection):
        connection.release()
        self.in_use_connections.remove(connection)
        self.available_connections.append(connection)


# Usage example
pool = DatabaseConnectionPoolManager(3)

# Acquire connections from the pool
conn1 = pool.acquire_connection()
conn2 = pool.acquire_connection()

# Execute queries using the connections
query1 = "SELECT * FROM employee"
query2 = "SELECT * FROM employee WHERE age < 50"
result1 = conn1.query(query1)
result2 = conn2.query(query2)

print(f"\nQUERY: {query1}\nRESULT: {result1}")
print(f"\nQUERY: {query2}\nRESULT: {result2}")

print()

print("Insert New Records...")
# Use available connections to insert employees into the database 
emp1 = Employee(firstname="Florence", lastname="Johnson", age=42)
emp2 = Employee(firstname="Abubakar", lastname="Ahmed", age=24)

conn1.insert(emp1)
conn2.insert(emp2)

# acquire the 3rd connection in the available connections, use it to add an Employee 
conn3 = pool.acquire_connection()
emp3 = Employee(firstname="Jackson", lastname="Thompson", age=14)
conn3.insert(emp3)

#run query on database and print out result
query3 = "SELECT * FROM employee"
result3 = conn1.query(query3)
print(f"\nQUERY: {query1}\nRESULT: {result3}")


# attempt to acquire 4th connection that doesn't exist
# conn4= pool.acquire_connection()

print(f"Available : {len(pool.available_connections)}, In Use: {len(pool.in_use_connections)}")

# Release connections back to the pool
pool.release_connection(conn1)
pool.release_connection(conn2)
pool.release_connection(conn3)

print(f"\nConnection After Release")
print(f"Available : {len(pool.available_connections)}, In Use: {len(pool.in_use_connections)}")


print()
for conn in pool.available_connections:
    print(conn.connection)