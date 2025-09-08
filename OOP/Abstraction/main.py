# abstraction

#       -hiding the complexity behind the interface 
#       -interface and implementation
#       -the idea of promise

from abc import ABC,abstractmethod

class MusicPlayer(ABC):

    """
    Music player has to have 
    -play
    -pause
    -shuffle
    
    """

    # interface and promise that we are making
    @abstractmethod  #ensure gurented of override this method
    def play(self):
        raise Exception("Not Implemented")

    def pause(self):
        raise Exception("Not Implemented")

    def shuffle(self):
        raise Exception("Not Implemented")

# class YoutubeMusicPlayer(MusicPlayer):
#     def play(self):
#         """
#         it will connect to the server
#         might check the licence 
#         buffer the song
#         play the song
        
#         """
#         print("I am playing on yt")

#     def pause(self):
#         pass

#     def shuffle(self):
#         pass

# class SpotifyMusicPlayer(MusicPlayer):
#     def play(self):
#         """
#         it will connect to the server
#         might check the licence 
#         buffer the song
#         play the song
        
#         """
#         print("I am playing on spotify")
#     def pause(self):
#         pass

#     def shuffle(self):
#         pass
class MyMusicPlayer(MusicPlayer):
    
    def play(self):
        print("Playing the music")
    def pause(self):
        pass

    def shuffle(self):
        pass

# mp1=YoutubeMusicPlayer()
# mp2=SpotifyMusicPlayer()
mp3=MyMusicPlayer()

# for player in (mp1,mp2,mp3):
#     player.play()
mp3.play()