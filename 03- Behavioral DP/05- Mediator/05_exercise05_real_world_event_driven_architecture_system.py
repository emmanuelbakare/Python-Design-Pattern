class EventMediator:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, subscriber):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    def unsubscribe(self, event_type, subscriber):
        if event_type in self.subscribers and subscriber in self.subscribers[event_type]:
            self.subscribers[event_type].remove(subscriber)


    def publish_event(self, event_type, data):
        if event_type in self.subscribers:
            for subscriber in self.subscribers[event_type]:
                 subscriber.receive_event(event_type, data)


class Subscriber:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def subscribe_event(self, event_type):
        self.mediator.subscribe(event_type, self)

    def unsubscribe_event(self, event_type):
        self.mediator.unsubscribe(event_type, self)

    def receive_event(self, event_type, data):  
        print(f"{self.name} received {event_type} event with data: {data}")


#client code -usage

mediator = EventMediator()

subscriber1 = Subscriber("Subscriber1", mediator)
subscriber2 = Subscriber("Subscriber2", mediator)
subscriber3 = Subscriber("Subscriber3", mediator)


subscriber1.subscribe_event("event1")
subscriber2.subscribe_event("event1")
subscriber2.subscribe_event("event2")
subscriber3.subscribe_event("event2")


mediator.publish_event("event1", "Data 1")
print()
mediator.publish_event("event2", "Data 2")

subscriber1.unsubscribe_event("event1")
print()
mediator.publish_event("event1", "Data 3")
print()
mediator.publish_event("event2", "Data 4")
 # subscribers ={
    #     'event1':[ 'subscriber2'],
    #     'event2':['subscriber2', 'subscriber3'],
    #     'event3':[]
    # }