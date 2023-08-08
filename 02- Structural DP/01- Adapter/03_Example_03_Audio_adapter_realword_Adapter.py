class AudioPlayer():
    def play(self, audio_type, filename):
        if audio_type == 'mp3':
            print(f"Playing '{filename}' as MP3")
        elif audio_type == 'wav':
            print(f"Playing '{filename}' as WAV")
        else:
            raise ValueError(f"Unsupported audio type: {audio_type}")


class AdvancedAudioPlayer: #Adaptee
    def play_mp4(self, filename):
        print(f"Playing {filename} as MP4")

#########################################################       

class MediaPlayer:  #Target
    def play(self, audio_type, filename):
        raise NotImplementedError
    

class Mp4Adapter(MediaPlayer): #Adapter
    def __init__(self, audio_player):
        self._audio_player = audio_player
    
    def play(self, audio_type, filename):
        if audio_type == 'mp4':
            self._audio_player.play_mp4(filename)
        else:
            raise ValueError(f"Unsupported audio type: {audio_type}")
        

audio = AudioPlayer()
audio.play("mp3","Give me the song") 
audio.play("wav","Looking Bright") 
# audio.play("mp4","Looking Bright") 

mp4_player = AdvancedAudioPlayer()
mp4audio =  Mp4Adapter(mp4_player)
        
mp4audio.play("mp4","Save the date")
    