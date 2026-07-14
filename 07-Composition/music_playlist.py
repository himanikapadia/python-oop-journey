class Song:
    # Constructor initializes the song's attributes.
    def __init__(self,title,artist):
        self.title=title
        self.artist=artist

    #Display Song details
    def display(self):
        print(f"🎵 {self.title:<10}   | {self.artist}")

class Playlist:
    def __init__(self,name):
        self.name=name
        #created an empty list to store Song objects.
        self.songs=[]

    def add_song(self,song):
        #Adds a Song object to the playlist.
        # Playlist stores (HAS) Song objects.
        self.songs.append(song)

    def show_playlist(self):
         print(f"\n===== {self.name} =====")
         for song in self.songs:
            song.display()

#Driver's code

# Creating Song objects
song1=Song("Perfect","Ed Sheran")
song2=Song("Kalank","Arijit Singh")
song3=Song("Khairyat","Pritam")

# Creating a Playlist object
play=Playlist("Favorites")

# Adding Song objects into the Playlist.
# Playlist HAS Song objects -> Composition.
play.add_song(song1)
play.add_song(song2)
play.add_song(song3)

# Display all songs in the playlist.
play.show_playlist()

