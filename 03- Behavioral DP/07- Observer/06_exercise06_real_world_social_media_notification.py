from abc import ABC, abstractmethod

class SocialMediaSubject:   #publisher / subject/observer
    def __init__(self):
        self._observers = []
        self._posts = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def add_post(self, post):
        self._posts.append(post)
        self.notify(post)

    def notify(self, post):
        for observer in self._observers:
            observer.update(post)


class Observer(ABC):
    @abstractmethod
    def update(self, post):
        pass

class User(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, post):
        print(f"User {self._name}: New post - {post}")


# Usage example
social_media = SocialMediaSubject()

user1 = User("John")
user2 = User("Alice")
user3 = User("Bob")

social_media.attach(user1)
social_media.attach(user2)
social_media.attach(user3)

social_media.add_post("Hello, everyone!") 
print()
social_media.add_post("I just had a great weekend!")


social_media.detach(user2)
print()
social_media.add_post("Exciting news!")