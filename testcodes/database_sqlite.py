import sqlite3

db_name = input("Enter the Database Name: ")
con = sqlite3.connect(f"{db_name}.db")

cus = con.cursor()

cus.execute("""CREATE TABLE customers(
    firstname text,
    lastname text,
    email text
)""")
