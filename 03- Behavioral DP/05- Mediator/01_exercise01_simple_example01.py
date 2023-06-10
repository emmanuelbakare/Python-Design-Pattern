class ChatRoomMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_message(message)


class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send_message(self, message):
        print(f"\n{self.name} sends: {message}")
        self.chatroom.send_message(message, self)

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")


#client code - Usage
chatroom = ChatRoomMediator()

alice = User("Alice", chatroom)
bob = User("Bob", chatroom)
charlie = User("Charlie", chatroom)

chatroom.add_user(alice)
chatroom.add_user(bob)
chatroom.add_user(charlie)

alice.send_message("Hi, everyone!")
bob.send_message("Hey, Alice!")
charlie.send_message("Hello, guys!")

