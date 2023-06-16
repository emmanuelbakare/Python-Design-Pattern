from abc import ABC, abstractmethod

class DatabaseQueryExecutionTemplate(ABC):
    def execute_query(self, query):
        self.connect_to_database()
        result = self.run_query(query)
        self.process_results(result)
        self.disconnect_from_database()

    def connect_to_database(self):
        print("Connecting to the database.")

    @abstractmethod
    def run_query(self, query):
        pass

    def process_results(self, result):
        print("Processing query results:", result)

    def disconnect_from_database(self):
        print("Disconnecting from the database.")



class MySQLQueryExecution(DatabaseQueryExecutionTemplate):
    def run_query(self, query):
        print("Executing MySQL query:", query)
        # Logic to execute query using MySQL
        return {
            "customerid":29038,
            "name": "Banky",
            "discount": False
        }

    def process_results(self, result):
        print("Processing MySQL query results:", result)
        # Logic to process MySQL query results

class PostgreSQLQueryExecution(DatabaseQueryExecutionTemplate):
    def run_query(self, query):
        print("Executing PostgreSQL query:", query)
        # Logic to execute query using PostgreSQL
        return {
            "productid":"PI09",
            "name": "Laptop",
            "total": 200
        }

    def process_results(self, result):
        print("Processing PostgreSQL query results:", result)
        # Logic to process PostgreSQL query results


# Usage
if __name__ == "__main__": 
    mysql_query_executor = MySQLQueryExecution()
    mysql_query_executor.execute_query("SELECT * FROM customers")

    print('*'*30)

    postgres_query_executor = PostgreSQLQueryExecution()
    postgres_query_executor.execute_query("SELECT * FROM products")