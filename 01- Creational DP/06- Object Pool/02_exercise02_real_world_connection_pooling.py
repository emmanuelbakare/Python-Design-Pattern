import random
import time

class Connection:
    def __init__(self, id):
        self.id = id
        self.is_connected = False

    def connect(self):
        # Simulate connection establishment
        print(f"Connecting to server... Connection ID: {self.id}")
        time.sleep(1)
        self.is_connected = True
        print(f"Connected! Connection ID: {self.id}")

    def disconnect(self):
        # Simulate connection termination
        print(f"Disconnecting from server... Connection ID: {self.id}")
        time.sleep(1)
        self.is_connected = False 
        print(f"Disconnected! Connection ID: {self.id}")


class ConnectionPoolManager:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.available_connections = []
        self.in_use_connections = []

        for i in range(max_connections):
            self.available_connections.append(Connection(i))

    def acquire_connection(self):
        if self.available_connections:
            conn = self.available_connections.pop()
            self.in_use_connections.append(conn)
            conn.connect()
            return conn
        else:
            raise Exception("No connections available in the pool.")
        
    def release_connection(self, conn):
        conn.disconnect()
        self.in_use_connections.remove(conn)
        self.available_connections.append(conn)


# Usage example
pool = ConnectionPoolManager(3)

# Acquire connections from the pool
conn1 = pool.acquire_connection()
conn2 = pool.acquire_connection()

# Use the connections
print(f"Using connection {conn1.id}")
time.sleep(random.randint(1, 3))
print(f"Using connection {conn2.id}")
time.sleep(random.randint(1, 3))

print(f"Available connection {len(pool.available_connections)}, used connections {len(pool.in_use_connections)}")

pool.release_connection(conn1)
pool.release_connection(conn2)

print(f"Available connection {len(pool.available_connections)}, used connections {len(pool.in_use_connections)}")