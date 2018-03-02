"""
7.3 Jukebox
Design a musical jukebox using object oriented principles.
"""

import random as random

# Objects Jukebox, song, album, artist

class Song:
    def __init__(self, title, album, artist):
        self.__title = title
        self.__album = album
        self.__artist = artist

    def get(self):
        return self

    def getAlbum(self):
        return self.__album

class Album:
    def __init__(self, name, artist, songs=list()):
        self.__name = name
        self.__artist = artist
        self.__songs = songs # should be a list of songs or empty

    def addSong(self, song):
        self.__songs.append(song)

    def getSongs(self):
        return self.__songs

    def getFirst(self):
        if self.__songs == []:
            return -1
        else:
            return self.__songs[0]

    def randomSong(self):
        return random.select(self.__songs)  # unsure how to randomly select from list

    def nextSong(self, song):
        if self.__songs[-1]==song:
            return -1
        else:
            for index in range(len(self.__songs)):
                if self.__songs[index]==songs:
                    return self.__songs[index+1]

    def getArtist(self):
        return self.__artist

class Artist:
    def __init__(self, name):
        self.__name = name

    def getArtist(self):
        return self.__name

class Jukebox:
    # Jukebox is comprised of Albums with artist and song list
    def __init__(self):
        self.__albums = []
        self.__isRandom = True
        self.__currentSong = None
        self.__currentAlbum = None

    def addAlbum(self, album):
        self.__albums.append(album)
        self.__currentSong = album.getFirst()
        self.__currentAlbum = album

    def shuffle(self):
        self.__isRandom = True

    def noShuffle(self):
        self.__isRandom = False

    def next(self):
        self.__currentAlbum().nextSong(self.__currentSong)
        
