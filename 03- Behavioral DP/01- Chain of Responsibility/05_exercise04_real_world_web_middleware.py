from abc import ABC, abstractmethod

class Middleware(ABC):
    def __init__(self, successor=None):
        self.successor = successor
    @abstractmethod
    def handle_request(self, request):
        pass

class AuthenticationMiddleware(Middleware):
    def handle_request(self, request):
        if self.authenticated(request):
            print("AuthenticationMiddleware: User authenticated.") 
            if self.successor is not None:
                self.successor.handle_request(request)
        else:
            print("Authentication failed.")


    def authenticated(self, request):
            print("authenticating request...", request)
            return True

class AuthorizationMiddleware(Middleware):
    def handle_request(self, request):
        if self.authorized(request):
            print("AuthorizationMiddleware: User authorized.")
            if self.successor is not None:
                self.successor.handle_request(request)
        else:
            print("AuthorizationMiddleware: Authorization failed.")

    def authorized(self, request):
        print("authorized request...", request)
        return True


class LoggingMiddleware(Middleware):
    def handle_request(self, request):
        print("LoggingMiddleware: Logging the request.")
        if self.successor is not None:
            self.successor.handle_request(request)
        else:
            print('Logging Ended')


middleware_chain =LoggingMiddleware(AuthenticationMiddleware(AuthorizationMiddleware()))

middleware_chain.handle_request("DATA REQUEST")