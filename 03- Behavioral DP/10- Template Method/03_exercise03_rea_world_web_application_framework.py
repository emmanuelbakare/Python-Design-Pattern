from abc import ABC, abstractmethod

class WebApplicationFrameworkTemplate(ABC):
    def handle_request(self, request):
        self.authenticate(request)
        self.route_request(request)
        self.execute_business_logic(request)
        self.render_response(request)
    
    def authenticate(self, request):
        print("Authenticating the request.")

    def route_request(self, request):
        print("Routing the request to the appropriate handler.")

    @abstractmethod
    def execute_business_logic(self, request):
        pass

    def render_response(self, request):
        print("Rendering the response.")


class DjangoFramework(WebApplicationFrameworkTemplate):
    def execute_business_logic(self, request):
        print("Executing business logic using Django.")

class FlaskFramework(WebApplicationFrameworkTemplate):
    def execute_business_logic(self, request):
        print("Executing business logic using Flask.")


# Usage
if __name__ == "__main__":
    django_framework = DjangoFramework() 
    django_framework.handle_request("GET /products")

    print("*"*30)

    flask_framework = FlaskFramework()
    flask_framework.handle_request("POST /login")
    