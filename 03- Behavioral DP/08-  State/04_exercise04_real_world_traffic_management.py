
#state 
from abc import ABC, abstractmethod


class TrafficLightState(ABC):
    @abstractmethod
    def display_light(self):
        pass

    @abstractmethod
    def change_light(self, traffic_light):
        pass

class RedState(TrafficLightState):
    def display_light(self):
        return "Red"
    
    def change_light(self, traffic_light):
        print("Changing from Red to Green")
        traffic_light.state = GreenState()

class GreenState(TrafficLightState):
    def display_light(self):
        return "Green"

    def change_light(self, traffic_light):
        print("Changing from Green to Yellow")
        traffic_light.state = YellowState()

class YellowState(TrafficLightState):
    def display_light(self):
        return "Yellow"

    def change_light(self, traffic_light):
        print("Changing from Yellow to Red")
        traffic_light.state = RedState()





#context
class TrafficLight:
    def __init__(self):
        self.state = RedState()

    def display_light(self):
        return self.state.display_light() 

    def change_light(self):
        self.state.change_light(self)


# Usage example
traffic_light = TrafficLight()

print(traffic_light.display_light()) 
print()
traffic_light.change_light()
print(traffic_light.display_light()) 

print()
traffic_light.change_light()
print(traffic_light.display_light()) 

print()
traffic_light.change_light()
print(traffic_light.display_light()) 