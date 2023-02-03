from abc import ABC, abstractmethod

class Pet(ABC):

    @abstractmethod
    def talk(self):
        pass 

class Dog(Pet):
    def talk(self):
        print("Dogs Talk: Woof")

class Cat(Pet):
    def talk(self):
        print("Cat Talk:Meow ")

class Cattle(Pet):
    def talk(self):
        print("Cattle Talk: Mooo ")

class PetFactory:
    def __init__(self):
        self.pets = dict(dog=Dog, cat = Cat, cattle=Cattle)

    def get_pet(self, pet_type):

        if pet_type in self.pets:
            return self.pets[pet_type]()
        return None

factory = PetFactory()
pet = factory.get_pet('dog')
if pet:
    pet.talk()
else:
    print("The Pet doesnt exist")
