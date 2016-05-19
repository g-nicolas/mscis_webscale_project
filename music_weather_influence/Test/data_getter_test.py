import json
import urllib2

from Core import basic_functions

#directory1 = "../Data Folder"
directory1 = "../Rsc/Data/LastFM/"
directory2 = "../Rsc/Data/Spotify/"

#Test if the folder exist, create one if not


#functions.file_creator(directory1, "test.txt")
#functions.file_creator(directory1 , "test2.txt")

#Top Songs Swiss - geo.getTopTracks:
url_lastFM1 = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=switzerland&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&format=json"
url_lastFM2 = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=austria&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&format=json"


def get_Json_From_URL(url):
    response = urllib2.urlopen(url)
    data = json.load(response)
    return data

j = get_Json_From_URL(url_lastFM1)

# Writing JSON data
basic_functions.save_Json_To_File(directory1, "data_test.json", j)



print "\n "
