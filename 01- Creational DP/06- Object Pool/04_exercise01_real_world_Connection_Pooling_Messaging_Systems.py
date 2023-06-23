import time
import queue
import threading

class MessagingConnection:
    def __init__(self, connection_id):
        self.connection_id = connection_id

    def send_message(self, message):
        print(f"Sending message '{message}' through connection {self.connection_id}")
        time.sleep(1)

    def close(self):
        # Simulate closing the connection
        print(f"Closing connection {self.connection_id}")


class ConnectionPoolManager:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.available_connections = queue.Queue(max_connections)
        self.lock = threading.Lock()

        for i in range(max_connections):
            connection = MessagingConnection(i)
            self.available_connections.put(connection)

    def acquire_connection(self):
        return self.available_connections.get()
    
    def release_connection(self, connection):
        self.available_connections.put(connection)


# Usage example
pool = ConnectionPoolManager(5)

connection1 = pool.acquire_connection()
connection2 = pool.acquire_connection()
connection3 = pool.acquire_connection()

# Use the connections to send messages
connection1.send_message("Hello, connection 1!")
connection2.send_message("Hi, connection 2!")
connection3.send_message("Great Job, connection 3!") 


# Release connections back to the pool
connection1.close()
connection2.close()
connection3.close()
print("Total Queue items BEFORE release",pool.available_connections.qsize())


pool.release_connection(connection1)
pool.release_connection(connection2)
pool.release_connection(connection3)
print("Total Queue items BEFORE release",pool.available_connections.qsize())


