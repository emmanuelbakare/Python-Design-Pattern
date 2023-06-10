import os

class ChatRoom:
    def __init__(self, name):
        self.name = name 
        self.users = []

    def add_user(self,user):
        self.users.append(user) 
        self.create_chat_log(user)

    def send_message(self, message, sender):
        self.create_chat_log(sender=sender, message=message)
        for user in self.users:
            if user!=sender:
                self.recieve_message(user,message)
                self.create_chat_log(sender=sender,reciever=user, message=message)

    def recieve_message(self,user, message):
        print(f"{user.name} recieved Message: '{message}'") 

    def create_chat_log(self, sender=None, reciever=None,message=None):
        user = reciever if reciever else sender

        name = user.name
        fullpath = f"{os.getcwd()}\chat\{name.lower()}.txt"  ## c:\codes\chat\alice.txt

        if not message: 
            message = f"\n{sender} chatroom Logs"
            message += f"\n{'*'*len(message)}"

        else:
            message = f"{sender}: {message}"


        with open(fullpath, 'a') as chatlog:
            chatlog.write(f"{message}\n")


    def __str__(self):
        return self.name
    

class User:
    def __init__(self, name):
        self.name = name
        self.current_chatroom = None

    def send_message(self, message):
        print(f"{self.name} sends message: '{message}'")
        if self.current_chatroom:
            self.current_chatroom.send_message(message, self)
        else:
            print("Error: Message not Delivered")
            print("You need to Join a group before you can send message")


    def join_room(self, chatroom):
        if self not in chatroom.users:
            chatroom.add_user(self)
        else:
            print(f"You already a member of {chatroom}")

    def enter_room(self, chatroom):
        if self in chatroom.users:
            self.current_chatroom = chatroom
            print(f"\n{self} Entered {chatroom} room...")
        else:
            print(f"\nAccess Denied - You are not a member of {chatroom} room") 
            self.current_chatroom = None

    def __str__(self):
        return self.name


        
#create chatrooms
CRpolitics = ChatRoom("Politics")
CRinfotech = ChatRoom("Information Technology")
CRentertainment = ChatRoom("Entertainment")
CRfashion = ChatRoom("Fashion")

# create users
alice = User("Alice")
deji = User("Deji")
bryan = User("Bryan")
andrew = User("Andrew")
linda = User("Linda")
kerry = User("Kerry") 

#joining politics group
alice.join_room(CRpolitics)
deji.join_room(CRpolitics)
bryan.join_room(CRpolitics)

alice.enter_room(CRpolitics)
alice.send_message("Hi Guys are you there!")

deji.enter_room(CRpolitics)
deji.send_message("Hi Alice i'm cool. Whats Up!.")

bryan.enter_room(CRpolitics)
bryan.send_message("I'm a little busy guys, I'll chat you up later.")

alice.enter_room(CRpolitics)
alice.send_message("Ok Bryan. Deji, whats your thought about fuel subsidy removal?")



# information technology rooom joining
alice.join_room(CRinfotech)
andrew.join_room(CRinfotech)
kerry.join_room(CRinfotech)
deji.join_room(CRinfotech) 



andrew.enter_room(CRinfotech)
andrew.send_message("Hello group, can we chat about our best programming languages?")

alice.enter_room(CRinfotech)
alice.send_message("Sure, I love Python")


kerry.enter_room(CRinfotech)
kerry.send_message("Yes, Python it is for me, easy to learn with lots of great libraries")


alice.send_message("Python is a one stop shop for several application, just name it, python's got it")
kerry.send_message("Sure, I do alot of data analysis with Pandas and Numpy in Python")
andrew.send_message("Yea, I mostly use Django  for web development and API development")
deji.send_message("Python lovers, you guys wont let us rest. Here we go again... whatever.")