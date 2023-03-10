import sqlite3 

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self._conn = None 

    @property 
    def conn(self):
        if self._conn is None:
            self._conn = sqlite3.connect(self.db_file)
        return self._conn
    
db = Database("example.db") 
cur = db.conn.cursor() 
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

while True:
    name = input("Enter Your Name: ")

    if not name:
        break
    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
    db.conn.commit() 

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print(rows)

