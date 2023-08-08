from abc import ABC, abstractmethod
#============= Abstraction ============= 
#(Abstract Class) - Web Application Prototype   
class WebApplicationFramework(ABC):
    def __init__(self, db_driver):
        self.db_driver = db_driver  

    @abstractmethod
    def route(self, path):
        pass

    @abstractmethod
    def render_template(self, template):
        pass

    def execute_query(self, query):
        self.db_driver.connect()
        self.db_driver.execute(query)
        self.db_driver.disconnect() 


#-----Refinning Abstraction -----
#(Concrete Abstraction) Web Application samples - eg, Flask, Django etc
class Flask(WebApplicationFramework):
    def route(self, path):
        print(f"Routing {path} using Flask...")
    
    def render_template(self, template):
        print(f"Rendering template '{template}' using Flask...")


class Django(WebApplicationFramework):
    def route(self, path):
        print(f"Routing {path} using Django...")

    def render_template(self, template):
        print(f"Rendering template '{template}' using Django...")

#########################################################################################


#============= Implementation =============
# Database Driver Abstract Class
class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def disconnect(self):
        pass

#-----Concrete Implementation -----
# Database Driver Examples - eg. MySqlDriver, PostgresDriver etc

class MySQLDriver(DatabaseDriver):
    def connect(self):
        print("Connecting to MySQL database...")

    def execute(self, query):
        print(f"Executing query '{query}' using MySQL driver...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")


class PostgreSQLDriver(DatabaseDriver):
    def connect(self):
        print("Connecting to PostgreSQL database...")
    
    def execute(self, query):
        print(f"Executing query '{query}' using PostgreSQL driver...")
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")



flask = Flask(MySQLDriver())
flask.route('/')
flask.render_template('index.html')
flask.execute_query('SELECT * FROM users')


print()
django_app = Django(PostgreSQLDriver())
django_app.route('/admin')
django_app.render_template("admin.html")
django_app.execute_query("SELECT * FROM admin")