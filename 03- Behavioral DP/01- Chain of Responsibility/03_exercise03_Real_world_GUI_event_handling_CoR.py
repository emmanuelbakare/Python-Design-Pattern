from abc import ABC, abstractmethod

class Event:
    def __init__(self, event_type):
        self.event_type = event_type


class EventHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor
    @abstractmethod
    def handle_event(self, event):
        pass

class ClickHandler(EventHandler):
    def handle_event(self, event):
        if event.event_type == 'button_click':
             print("click event handled by ClickHandler")
        elif self.successor is not None:
            self.successor.handle_event(event)

class MouseMoveHandler(EventHandler):
    def handle_event(self, event):
        if event.event_type == 'mouse_move':
             print("Mouse move event handled by MouseMoveHandler")
        elif self.successor is not None:
            self.successor.handle_event(event)

class KeyPressHandler(EventHandler):
    def handle_event(self, event):
        if event.event_type == 'key_press':
             print("Key press event handled by KeyPressHandler")
        elif self.successor is not None:
            self.successor.handle_event(event)
             

click_handler = ClickHandler()
mouse_handler = MouseMoveHandler()
key_handler = KeyPressHandler()

click_handler.successor = mouse_handler
mouse_handler.successor = key_handler


# Simulating events
events = [
    Event('mouse_move'),
    Event('button_click'),
    Event('key_press'),
]

for event in events:  
    click_handler.handle_event(event)
