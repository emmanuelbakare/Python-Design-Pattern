class Dog:
    def talk(self):
        print("Dogs Talk: Woof")

class Cat:
    def talk(self):
        print("Cat Talk:Meow ")

def pet_factory(pet_type):
    pets = {
        'cat': Cat,
        'dog': Dog,
    }

    return pets[pet_type]()


pet = pet_factory('cat')
pet.talk() 
 