import urllib
import json
from Libs import pygn, requests
from Core import basic_functions

################################################
#  GraceNote
################################################


# Return the genre (only one) of the track as a list
def get_genre_gracenote_plus(artist='', track=''):
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

    genres_list = []
    for subkey in genre_meta:
        #print key
        #print genre_meta[subkey]["TEXT"]
        genres_list.append(genre_meta[subkey]["TEXT"])
    print genres_list


# Return the genre (only one) of the track as a string
def get_genre_graceNote_distinct(artist='', track=''):
    clientID = '14783488-D30D8E1E9B67E9A8776931C7A34DC429'  # Enter your Client ID here
    userID = '279600461518500590-A7E01427C0C625536FB9CDE80ECE1AC6'
    if artist == '' or track == '':
        print('Must query with all field s(artist, track)')
        return None

    print artist
    print track
    # Query the track metadata
    metadata = pygn.search_custom(clientID=clientID, userID=userID, artist=artist, track=track)

    # Get genre values
    print metadata
    if metadata is None:
        return "__NA__"
    genre_meta = metadata.get("genre")

    genres_list = []
    for subkey in genre_meta:

        genres_list.append(genre_meta[subkey]["TEXT"])
    print genres_list
    if genres_list.__len__()>0:
        genre = genres_list.pop(0)
    else:
        genre = "__NA__"

    return genre


def get_Genre_GraceNote(artist='', track=''):
    client_id = '14783488-D30D8E1E9B67E9A8776931C7A34DC429'  # Enter your Client ID here
    user_id = '279600461518500590-A7E01427C0C625536FB9CDE80ECE1AC6'
    if artist == '' or track == '':
        print('Must query with all field s(artist, track)')
        return None
    # Query the track metadata
    metadata = pygn.search(clientID=client_id, userID=user_id, artist=artist, track=track)

    # Get genre values
    genre_meta = metadata.get("genre")

    print metadata

    print metadata.get("genre")
    genre_meta.get("TEXT")

    genres_list = []
    for subkey in genre_meta:

        genres_list.append(genre_meta[subkey]["TEXT"])

    if genres_list.__len__() > 0:
        genre = genres_list.pop(0)
    else:
        genre = "__NA__"

    return genre

################################################
# MUSIC GRAPH
################################################

def music_graph_request_builder(artist='', track=''):
    api_url = "http://api.musicgraph.com/api/v2/track/search?"
    api_key = "4d02e561d8d3dd57109bc41feda598da"
    api_param_artist = "&artist_name="
    api_param_track = "&title="
    # api_limit = "&limit=1"
    request = api_url+"api_key="+api_key+api_param_artist+urllib.quote(artist)+api_param_track+urllib.quote(track)
    return request


def get_track_spotify_id(artist='', track=''):
    request = music_graph_request_builder(artist, track)
    request_data = basic_functions.get_Json_From_URL(request)

    if request_data["pagination"]["count"] == 0:
        print "NO_ID"
        return "NO_ID"
    nam_of_correspondences = request_data["pagination"]["total"]

    response_data = request_data["data"]
    spotify_track_id = ""
    if nam_of_correspondences > 1:
        tracks_list = []

        track_popularity = ""
        for track_data in response_data:
            if "track_spotify_id" in track_data:
                if spotify_track_id == "":
                    spotify_track_id = track_data["track_spotify_id"]
                    track_popularity = track_data["popularity"]
                else:
                    if track_popularity < track_data["popularity"]:
                        track_popularity = track_data["popularity"]
                tracks_list.append(track_data)
    else:
        print "ERROR ICI"
        #spotify_track_id = track_data["track_spotify_id"]
    return spotify_track_id

################################################
# Spotify
################################################
class SpotifyOauthError(Exception):
    pass


def request_access_token():
    # auth_header = base64.b64encode(str(client_id + ':' + client_secret).encode())
    client_id = "2c13de0c7a684ae5b1c3fd946bd45798"
    client_secret = "bdebfaceaf3b48cdbe62c0e797606f31"
    headers = {
        'Authorization': 'Basic MmMxM2RlMGM3YTY4NGFlNWIxYzNmZDk0NmJkNDU3OTg6YmRlYmZhY2VhZjNiNDhjZGJlNjJjMGU3OTc2MDZmMzE=',
    }

    data = {'grant_type': 'client_credentials'}

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data, verify=True)
    print response.status_code
    if response.status_code is not 200:
        raise SpotifyOauthError(response.reason)
    token_info = response.json()
    access_token =  token_info["access_token"]
    return access_token


def get_audio_features(track_id):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + request_access_token(),
    }

    audio_features = requests.get('https://api.spotify.com/v1/audio-features/' + track_id, headers=headers).json()
    return audio_features