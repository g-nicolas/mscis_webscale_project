#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2
import urllib
import json
from Libs.spotipy import util as util
from Core import basic_functions, music_functions
from Libs import spotipy
from Libs import requests
import base64



#spot_id = music_functions.get_track_spotify_id('artist', 'track')

spotify = spotipy.Spotify()
#print spotify.audio_features("4sPmO7WMQUAf45kwMOtONw")

def spotify_request_builder(track_spotify_id=''):
    api_url = "http://api.spotify.com/v1/audio-features/"
    sample_track_id = "4sPmO7WMQUAf45kwMOtONw"
    spot_id = music_functions.get_track_spotify_id("eminem", "mosh")
    print spot_id
    print "oui"
    api_token = "Bearer BQA-RjE0QwY-GlEVc9TpyAuedEgU4tvYR5f8_LHX6XTze6bfR1V-4wQKguy199vAB2vbQBoYM9mmMUY6O8IY8c5j09Z-luAf-9HvDHWt2e0Ujcd9wysOSIiGC13le6dJUjuY26SKfMU"
    url = api_url+sample_track_id
    #api_token = base64.standard_b64encode(api_token )
    # headers = {'user-agent': 'my-app/0.0.1'}
    #header = {'Host': 'api.spotify.com', 'Accept': 'application/json', 'Content-Type': 'application/json',
     #         'Accept-Encoding': 'gzip, deflate, compress',
      #        'Authorization': 'Bearer BQCkX0MDb6YqrjyTmaIEVxEoDcmOc2ud-pJrkZsdMIZ3SOLTvaAXbryVGWiVY0JQzIWSSYT9zxO2qQaNdRHlgkg4CAlzdsjHIBCmYkVD9Qk2Bs3NtHtxLB-idawMQTy69KqYgu668yc',
       #       'User-Agent': 'Spotify API Console v0.1'}
    #header = {'Host': 'api.spotify.com', 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer' + api_token, 'User-Agent': 'Spotify API Console v0.1'}
    #query = requests.get(url, headers=header)
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer BQA-RjE0QwY-GlEVc9TpyAuedEgU4tvYR5f8_LHX6XTze6bfR1V-4wQKguy199vAB2vbQBoYM9mmMUY6O8IY8c5j09Z-luAf-9HvDHWt2e0Ujcd9wysOSIiGC13le6dJUjuY26SKfMU',
    }

    query = requests.get('https://api.spotify.com/v1/audio-features/'+sample_track_id, headers=headers)
    return query.json()

sample_track_id = "3X38ErFiKgzUxinBlhwuWm"

def get_track_audio_features():
    #spot_id = music_functions.get_track_spotify_id("adele", "hello")
    #print spot_id
    #track_audio_features = spotify.audio_features(spot_id)
    #"https://api.spotify.com/v1/audio-features/4sPmO7WMQUAf45kw"
    #return track_audio_features
    #
    headers = {
        'Authorization': 'Basic ZjM...zE=',
    }

    data = 'grant_type=authorization_code&code=MQCbtKe...44KN&redirect_uri=https%3A%2F%2Fwww.foo.com%2Fauth'

    requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

#print spotify_request_builder("")

#get_track_audio_features()
#request = music_functions.music_graph_request_builder("the weeknd", "can't feel my face")
#request_data = basic_functions.get_Json_From_URL(request)

#"curl -H "Authorization: Basic MmMxM2RlMGM3YTY4NGFlNWIxYzNmZDk0NmJkNDU3OTg6YmRlYmZhY2VhZjNiNDhjZGJlNjJjMGU3OTc2MDZmMzE=" -d grant_type=authorization_code -d code=MQCbtKe...44KN -d redirect_uri=https%3A%2F%2Fwww.foo.com%2Fauth https://accounts.spotify.com/api/token"
#"curl -H "Authorization: Basic MmMxM2RlMGM3YTY4NGFlNWIxYzNmZDk0NmJkNDU3OTg6YmRlYmZhY2VhZjNiNDhjZGJlNjJjMGU3OTc2MDZmMzE=" -d grant_type=client_credentials -d code=MQCbtKe...44KN -d redirect_uri=https%3A%2F%2Fwww.foo.com%2Fauth https://accounts.spotify.com/api/token"


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


print get_audio_features("3X38ErFiKgzUxinBlhwuWm")["danceability"]
