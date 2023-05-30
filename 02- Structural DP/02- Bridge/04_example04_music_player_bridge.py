# Music Player -> Spotify,AppleMusic, etc

class MusicPlayer:
    def __init__(self, implementation):
        self.implementation = implementation

    def play(self, song):
        self.implementation.play_song(song) 

class MusicPlayerImplementation:
    def play_song(self, song):
        pass

class AppleMusic(MusicPlayerImplementation):
    def play_song(self, song):
        print("Playing '{}' on Apple Music".format(song))

class Spotify(MusicPlayerImplementation):
    def play_song(self, song):
        print("Playing '{}' on Spotify Music".format(song))


spotify_player = MusicPlayer(Spotify())

spotify_player.play("This new day")

apple_music = MusicPlayer(AppleMusic())
apple_music.play("God's Done it all")
