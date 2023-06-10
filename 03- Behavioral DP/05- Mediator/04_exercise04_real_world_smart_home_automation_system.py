class SmartHomeMediator:
    def __init__(self):
        self.components = {}

    def register_component(self, component_name, component):
        self.components[component_name] = component

    def send_command(self, component_name, command):
        if component_name in self.components:
            self.components[component_name].execute_command(command)
        else:
            print(f"Component '{component_name}' not found.")

    def get_component_state(self, component_name):
        if component_name in self.components:
            return self.components[component_name].get_state()
        else:
            print(f"Component '{component_name}' not found.")
            return None
        

class SmartComponent:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.state = "OFF"

    def execute_command(self, command):
        pass

    def get_state(self):
        return self.state
    
class LightComponent(SmartComponent):
    def execute_command(self, command):
        if command == "ON":
            self.state = "ON"
            print(f"Light '{self.name}' turned ON.")
        elif command == "OFF":
            self.state = "OFF"
            print(f"Light '{self.name}' turned OFF.")


class ACComponent(SmartComponent):
    def execute_command(self, command):
        if command == "ON":
            self.state = "ON"
            print(f"AC '{self.name}' turned ON.")
        elif command == "OFF":
            self.state = "OFF"
            print(f"AC '{self.name}' turned OFF.")
        elif command.startswith("SET_TEMP"):    
            temperature = command.split(":")[1]    # startswith("SET_TEMP:22")
            self.state = f"ON (Temperature: {temperature})"
            print(f"AC '{self.name}' set to {temperature}°C.")


#usage 
mediator = SmartHomeMediator()

light = LightComponent("Living Room Light", mediator)
ac = ACComponent("Bedroom AC", mediator)

mediator.register_component("light", light)
mediator.register_component("ac", ac)

mediator.send_command("light", "ON")  
mediator.send_command("ac", "ON")
mediator.send_command("ac", "SET_TEMP:22")
mediator.send_command("light", "OFF")

print()

print(mediator.get_component_state("light"))
print(mediator.get_component_state("ac"))
print(mediator.get_component_state("fan"))



        

