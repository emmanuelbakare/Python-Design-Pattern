from abc import ABC, abstractmethod


class NPCState(ABC):
    @abstractmethod
    def perform_action(self, character):
        pass

class IdleState(NPCState):
    def perform_action(self, character):
        print("NPC is idle and not performing any action.")

class AggressiveState(NPCState):
    def perform_action(self, character):
        print("NPC is in aggressive state and attacking the player.")

class FriendlyState(NPCState):
    def perform_action(self, character):
        print("NPC is in friendly state and providing assistance to the player.")


class GameCharacter:
    def __init__(self):
        self.state = IdleState()

    def perform_action(self):
        self.state.perform_action(self)

    def set_state(self, state):
        self.state = state


#usage
character = GameCharacter()


character.perform_action() 


character.set_state(AggressiveState())
character.perform_action() 


character.set_state(FriendlyState())
character.perform_action() 
