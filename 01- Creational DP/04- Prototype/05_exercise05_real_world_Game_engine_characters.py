import copy

class GameObject:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)
    
class Character(GameObject):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health

class Enemy(GameObject):
    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength 

# Game Engine
class GameEngine:
    def __init__(self):
        self.prototype_objects = {}     

    def register_prototype(self, key, prototype):
        self.prototype_objects[key] = prototype 

    def create_game_object(self, key):
        prototype = self.prototype_objects.get(key) 
        if prototype:
            return prototype.clone()
        else:
            raise ValueError(f"Prototype with key '{key}' does not exist.")
        

# Usage
engine = GameEngine()

# Register prototypes
character_prototype = Character("Player", 100)
engine.register_prototype("player", character_prototype)

enemy_prototype = Enemy("Enemy", 50)
engine.register_prototype("enemy", enemy_prototype)


# Create game objects
player = engine.create_game_object("player")
player.health = 150

enemy = engine.create_game_object("enemy")
enemy.strength = 75

# Print object details
print("{} with Strenght:{}".format(player.name, player.health))
print("{} with Strength:{}".format(enemy.name, enemy.strength)) 

