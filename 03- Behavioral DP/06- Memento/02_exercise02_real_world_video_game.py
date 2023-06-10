class GameState: #memento
    def __init__(self, level, score):
        self.level = level
        self.score = score

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score
    
class Game:  # originator
    def __init__(self):
        self.level = 1
        self.score = 0
    
    def next_level(self):
        self.level += 1
    
    def add_score(self,score):
        self.score += score

    def save_state(self):
        return GameState(self.level, self.score)
    
    def restore_state(self, state):
        self.level = state.get_level()
        self.score = state.get_score()


class Caretaker: #Caretaker
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]
    

# Client code - Usage example
game = Game()
caretaker = Caretaker()

print("Initial State: Level -", game.level, ", Score -", game.score)

game.add_score(12)
game.add_score(4)
game.add_score(20)
print("Current State: Level -", game.level, ", Score -", game.score)  
caretaker.add_memento(game.save_state())

game.next_level()
game.add_score(10)
game.add_score(9)
print("Current State: Level -", game.level, ", Score -", game.score)

game.restore_state(caretaker.get_memento(0))
print("Current State: Level -", game.level, ", Score -", game.score)
