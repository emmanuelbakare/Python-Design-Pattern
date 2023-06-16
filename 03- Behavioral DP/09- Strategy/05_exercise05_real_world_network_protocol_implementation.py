import abc


class NetworkProtocolTemplate(metaclass=abc.ABCMeta):
    def establish_connection(self):
        self.authenticate()
        self.setup_connection()
        self.send_data()
        self.receive_data()
        self.close_connection() 

    @abc.abstractmethod
    def authenticate(self):
        pass

    @abc.abstractmethod
    def setup_connection(self):
        pass

    @abc.abstractmethod
    def send_data(self):
        pass

    @abc.abstractmethod
    def receive_data(self):
        pass

    def close_connection(self):
        print("Closing the connection.")


class FTPProtocol(NetworkProtocolTemplate):
    def authenticate(self):
        print("Authenticating FTP user.")

    def setup_connection(self):
        print("Setting up FTP connection.")

    def send_data(self):
        print("Sending data via FTP.")

    def receive_data(self):
        print("Receiving data via FTP.")


class HTTPProtocol(NetworkProtocolTemplate):
    def authenticate(self):
        print("Authenticating HTTP user.")

    def setup_connection(self):
        print("Setting up HTTP connection.")

    def send_data(self):
        print("Sending data via HTTP.")

    def receive_data(self):
        print("Receiving data via HTTP.")

# Usage
if __name__ == "__main__":
    ftp_protocol = FTPProtocol()
    ftp_protocol.establish_connection()


    print("-------------------------")

    http_protocol = HTTPProtocol()
    http_protocol.establish_connection()

    