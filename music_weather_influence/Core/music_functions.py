import os
import urllib2
import json
import time
from Libs import pygn



# Return the genre (only one) of the track as a list
def get_Genre_GraceNote_plus(artist='', track=''):
    clientID = '14783488-D30D8E1E9B67E9A8776931C7A34DC429'  # Enter your Client ID here
    userID = '279600461518500590-A7E01427C0C625536FB9CDE80ECE1AC6'
    if artist == '' or track == '':
        print('Must query with all field s(artist, track)')
        return None
    # Query the track metadata
    metadata = pygn.search_custom(clientID=clientID, userID=userID, artist=artist, track=track)

    # Get genre values
    genre_meta = metadata.get("genre")

    print metadata

    #print metadata.get("genre")
    #genre_meta.get("TEXT")
    #print type(genre_meta)
    #print genre_meta.get("TEXT")
    #print genre_meta['1']
    #print genre_meta['2']
    #print genre_meta['3']
    genres_list = []
    for subkey in genre_meta:
        #print key
        #print genre_meta[subkey]["TEXT"]
        genres_list.append(genre_meta[subkey]["TEXT"])
    print genres_list
# Return the genre (only one) of the track as a string
def get_Genre_GraceNote_DISTINCT(artist='', track=''):
    clientID = '14783488-D30D8E1E9B67E9A8776931C7A34DC429'  # Enter your Client ID here
    userID = '279600461518500590-A7E01427C0C625536FB9CDE80ECE1AC6'
    if artist == '' or track == '':
        print('Must query with all field s(artist, track)')
        return None
    # Query the track metadata
    metadata = pygn.search_custom(clientID=clientID, userID=userID, artist=artist, track=track)

    # Get genre values
    genre_meta = metadata.get("genre")

    #print metadata

    #print metadata.get("genre")
    #genre_meta.get("TEXT")
    #print type(genre_meta)
    #print genre_meta.get("TEXT")
    #print genre_meta['1']
    #print genre_meta['2']
    #print genre_meta['3']
    genres_list = []
    for subkey in genre_meta:
        #print key
        #print genre_meta[subkey]["TEXT"]
        genres_list.append(genre_meta[subkey]["TEXT"])
    print genres_list
    if genres_list.__len__()>0:
        genre = genres_list.pop(0)
    else:
        genre = "__NA__"


    return genre

def get_Genre_GraceNote(artist='', track=''):
    clientID = '14783488-D30D8E1E9B67E9A8776931C7A34DC429'  # Enter your Client ID here
    userID = '279600461518500590-A7E01427C0C625536FB9CDE80ECE1AC6'
    if artist == '' or track == '':
        print('Must query with all field s(artist, track)')
        return None
    # Query the track metadata
    metadata = pygn.search(clientID=clientID, userID=userID, artist=artist, track=track)

    # Get genre values
    genre_meta = metadata.get("genre")

    print metadata

    print metadata.get("genre")
    genre_meta.get("TEXT")
    #print type(genre_meta)
    #print genre_meta.get("TEXT")
    #print genre_meta['1']
    #print genre_meta['2']
    #print genre_meta['3']
    genres_list = []
    for subkey in genre_meta:
        #print key
        #print genre_meta[subkey]["TEXT"]
        genres_list.append(genre_meta[subkey]["TEXT"])
    #print genres_list
    if genres_list.__len__() > 0:
        genre = genres_list.pop(0)
    else:
        genre = "__NA__"

    return genre






