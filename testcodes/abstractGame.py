from abc import ABC, abstractmethod
#build game types- build the character, weapons and game level

class GameObject(ABC):
    @abstractmethod
    def display(self):
        pass 
#===================================================
class Character(GameObject):
    def display(self):
        pass 

class Knight(Character):
    def display(self):
        print("Knight Character")

class Astranault(Character):
    def display(self):
        print("Astranault Character")

class Soldier(Character):
    def display(self):
        print("Rucky Character")
#=====================================================

#==== WEAPON============
class Weapon(GameObject):
    def display(self):
        pass 

class Sword(Weapon):
    def display(self):
        print("Sword Weapon")

class Gun(Weapon):
    def display(self):
        print("Gun Weapon")

class LightSaber(Weapon):
    def display(self):
        print("LightSaber Weapon")
#================================================

#========= LEVEL===================


class Level(GameObject):
    def display(self):
        pass 

class School(Level):
    def display(self):
        print("School Level")

class Castle(Level):
    def display(self):
        print("Castle Level")

class SpaceShip(Level):
    def display(self):
        print("Space Ship Level")

#============================= Game Factory =============================
class GameFactory(ABC):
    @abstractmethod
    def create_character(self):
        pass 

    @abstractmethod
    def create_weapon(self):
        pass 

    @abstractmethod
    def create_level(self):
        pass 

    

class ScifiGameFactory(GameFactory):
    def create_character(self):
        return  Astranault()
    
    def create_weapon(self):
        return  LightSaber()
    
    def create_level(self):
        return SpaceShip()
    
class MedievalGameFactory(GameFactory):
    def create_character(self):
        return  Knight()
    
    def create_weapon(self):
        return  Sword()
    
    def create_level(self):
        return Castle()
    
class ModernGameFactory(GameFactory):
    def create_character(self):
        return  Soldier()
    
    def create_weapon(self):
        return  Gun()
    
    def create_Level(self):
        return School()
 
def main():
    factories = dict(medieval= MedievalGameFactory, 
                     modern = ModernGameFactory,
                     scifi=ScifiGameFactory)
    
    factory_list = ", ".join(factories)

    while True:
        factory_type = input(f"Enter the Type of Game {factory_list} : ")

        if factory_type in factories:
            break
        else:
            print(f"Try Again this game time does not exist. Choose between {factory_list}")
    
    return factories[factory_type]()

     
if __name__=="__main__":
    factory = main()
    # Create character
    character =factory.create_character() 
    character.display()

    # Create Weapon
    weapon =factory.create_weapon() 
    weapon.display()
    
    # Create level
    level =factory.create_level() 
    level.display()

    



 