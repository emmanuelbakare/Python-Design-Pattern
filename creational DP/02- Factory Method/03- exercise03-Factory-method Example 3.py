from abc import ABC, abstractmethod

class PetCreator(ABC):

     @abstractmethod
     def create_pet(self):
        pass

class DogCreator(PetCreator):
    def create_pet(self):
        return Dog()

class CatCreator(PetCreator):
    def create_pet(self):
        return Cat()

 
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
 

class PetClient:
    def __init__(self):
        self.creators = dict(dog=DogCreator(), cat = CatCreator() )

    def get_pet(self, pet_type):

        creator = self.creators.get(pet_type)
        if creator:
            return creator.create_pet()
        else:
            return None


pet_client = PetClient()

pet = pet_client.get_pet('dog')

if pet:
    pet.talk()
else:
    print("The Pet doesnt exist")

      
