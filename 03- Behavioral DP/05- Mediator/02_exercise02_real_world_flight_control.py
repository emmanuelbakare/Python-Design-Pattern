class AirTrafficControlMediator:
    def __init__(self):
        self.aircrafts = []

    def register_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def notify_aircraft(self, sender, message):
        print()
        for aircraft in self.aircrafts:
            if aircraft != sender:
                aircraft.receive_message(message)


class Aircraft:
    def __init__(self, callsign, mediator):
        self.callsign = callsign
        self.mediator = mediator

    def send_message(self, message):
        self.mediator.notify_aircraft(self, message) 

    def receive_message(self, message):
        print(f"Aircraft {self.callsign} received message: {message}")


mediator = AirTrafficControlMediator()

aircraft1 = Aircraft("Flight123", mediator)
aircraft2 = Aircraft("Flight456", mediator)
aircraft3 = Aircraft("Flight789", mediator)

mediator.register_aircraft(aircraft1)
mediator.register_aircraft(aircraft2)
mediator.register_aircraft(aircraft3) 

aircraft1.send_message("Traffic advisory: Descend to 10,000 feet.")
aircraft2.send_message("Roger that. Descending to 10,000 feet.")