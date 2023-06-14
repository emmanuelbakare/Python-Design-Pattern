from abc import ABC, abstractmethod

class TrafficManagementSystem: #subject/publisher/observable
    def __init__(self):
        self._observers = []
        self._traffic_status = {}

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def update_traffic_status(self, road, status):
        self._traffic_status[road] = status
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._traffic_status)


class Observer(ABC):
    @abstractmethod
    def update(self, traffic_status):
        pass

class TrafficLight(Observer):
    def __init__(self, road):
        self._road = road

    def update(self, traffic_status):
        status = traffic_status.get(self._road, "unknown")
        print(f"Traffic Light on {self._road}: Traffic status is {status}")


# Usage example
traffic_management_system = TrafficManagementSystem()

traffic_light1 = TrafficLight("Road A") 
traffic_light2 = TrafficLight("Road B")

traffic_management_system.attach(traffic_light1)
traffic_management_system.attach(traffic_light2)

traffic_management_system.update_traffic_status("Road A", "heavy traffic")
print()
traffic_management_system.update_traffic_status("Road B", "moderate traffic")