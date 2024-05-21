class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    
    def play(self):
        print(f"Playing {self.title} by {self.artist}...")

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
        print(f"Added {song.title} by {song.artist} to the playlist {self.name}")
    
    def remove_song(self, song):
        self.songs.remove(song)
        print(f"Removed {song.title} by {song.artist} from the playlist {self.name}")
    
    def play_all(self):
        print(f"Playing all songs in the playlist {self.name}...")
        for song in self.songs:
            song.play()

class MusicPlayer:
    def __init__(self):
        self.playlists = []
    
    def add_playlist(self, playlist):
        self.playlists.append(playlist)
        print(f"Added playlist {playlist.name}")
    
    def remove_playlist(self, playlist):
        self.playlists.remove(playlist)
        print(f"Removed playlist {playlist.name}")
    
    def play_playlist(self, playlist_name):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                playlist.play_all()
                break
        else:
            print(f"Playlist {playlist_name} not found")

# Example Usage:
song1 = Song("Song1", "Artist1", 3.5)
song2 = Song("Song2", "Artist2", 4.0)
playlist = Playlist("MyPlaylist")
playlist.add_song(song1)
playlist.add_song(song2)
music_player = MusicPlayer()
music_player.add_playlist(playlist)
music_player.play_playlist("MyPlaylist")
