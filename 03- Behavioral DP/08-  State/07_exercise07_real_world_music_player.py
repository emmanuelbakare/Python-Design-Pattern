from abc import ABC, abstractmethod


class MusicPlayerState(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass


class ReadyState(MusicPlayerState):
    def play(self, player):
        print("Music is playing.")
        player.state = PlayingState()

    def pause(self, player):
        print("Cannot pause. Music is not playing.")

    def stop(self, player):
        print("Cannot stop. Music is not playing.")

class PlayingState(MusicPlayerState):
    def play(self, player):
        print("Cannot play. Music is already playing.")

    def pause(self, player):
        print("Music is paused.")
        player.state = PausedState()

    def stop(self, player):
        print("Music stopped.")
        player.state = ReadyState()

class PausedState(MusicPlayerState):
    def play(self, player):
        print("Resuming music playback.")
        player.state = PlayingState()

    def pause(self, player):
        print("Cannot pause. Music is already paused.")

    def stop(self, player):
        print("Music stopped.")
        player.state = ReadyState()   
    


class MusicPlayer:
    def __init__(self):
        self.state = ReadyState()

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)


# Usage example
player = MusicPlayer() 

player.play()
player.pause() 
player.pause()
player.play()
player.stop()
player.play()
player.stop()
player.pause()
 
