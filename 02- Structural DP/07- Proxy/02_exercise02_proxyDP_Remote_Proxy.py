from abc import ABC, abstractmethod

# Remote service interface
class RemoteService(ABC):
    @abstractmethod
    def perform_action(self):
        pass 

# Real remote service implementation
class RemoteServiceImpl(RemoteService):
    def perform_action(self):
        print("Performing the actual action in the remote service.")

# remote proxy
class RemoteServiceProxy(RemoteService):
    def __init__(self, remoteservice):
        self._service = remoteservice
    
    def perform_action(self):
        print("Proxy: Before performing the action.")
        self._service.perform_action()
        print("Proxy: After performing the action.")


remote_service = RemoteServiceImpl() 
proxy = RemoteServiceProxy(remote_service)


# remote_service.perform_action()
proxy.perform_action()
