import json
from Core import basic_functions, music_functions
import xml.etree.ElementTree

API_key = "46ab0cf62548d9fbd9bd4ba79e40f168"

directory1 = "../Rsc/Data/Original_Music_Source/LastFM/"
directory2 = "../Rsc/Data/Original_Music_Source/Itunes/"

cleaned_directory1 = "../Rsc/Data/Cleaned_Music_Source/LastFM/"
cleaned_directory2 = "../Rsc/Data/Cleaned_Music_Source/Itunes/"

files_list = basic_functions.get_files_from_folder(directory1)


def manage_Itunes_Xml():
    for data_file in files_list:
        #if data_file.startswith("LastFM_top_songs"):
        if data_file.startswith("Itunes_top_songs_austria_20160429.xml"):
            #PARSE DATA HERE
            #cleaned_data = clean_LastFM_Json(directory1, data_file)
            test(data_file)

def clean_from_folder(source_directory, output_directory, filename):
    cleaned_Top_Charts = {}
    cleaned_Top_Charts["ID"] = filename

    cleaned_Top_Charts["TopCharts"] = []

    url = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=switzerland&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&limit=10&format=json"
    data = basic_functions.get_Json_From_URL(url)
    tracks_list = data["tracks"]["track"]

    for track_info in tracks_list:
        track_rank = track_info["@attr"]["rank"]
        track_name = track_info["name"]
        track_artist = track_info["artist"]["name"]
        track_genre = music_functions.get_Genre_GraceNote_DISTINCT(track_artist, track_name)
        track_weather_ID = "track_weather_ID"
        cleaned_track_info = {"track_rank": track_rank, "track_name": track_name, "track_artist": track_artist, "track_genre": track_genre, "track_weather_ID": track_weather_ID }
        cleaned_Top_Charts["TopCharts"].append(cleaned_track_info)

    basic_functions.save_Json_To_File(cleaned_directory2, "test_xml_cleaning", data)

def test(namefile):
    cleaned_Top_Charts = {}
    cleaned_Top_Charts["ID"] = namefile

    cleaned_Top_Charts["TopCharts"] = []

    url = "https://itunes.apple.com/ch/rss/topsongs/limit=10/explicit=true/json"
    data = basic_functions.get_Json_From_URL(url)
    #print data
    print data["feed"]["entry"]

    tracks_list = data["feed"]["entry"]
    rank = 1
    for track_info in tracks_list:

        track_info["title"]["label"]
        track_rank = rank
        track_name_artist = track_info["title"]["label"].partition(' - ')
        track_name = track_name_artist[0]
        track_artist = track_name_artist[2]
        track_genre = music_functions.get_Genre_GraceNote_DISTINCT(track_artist, track_name)
        track_weather_ID = "TRACK_WEATHER_ID_HERE"
        cleaned_track_info = {"track_rank": track_rank, "track_name": track_name, "track_artist": track_artist, "track_genre": track_genre, "danceability": track_weather_ID, "energy": track_weather_ID, "tempo": track_weather_ID, "track_weather_ID": track_weather_ID }
        rank = rank + 1
        cleaned_Top_Charts["TopCharts"].append(cleaned_track_info)

    basic_functions.save_Json_To_File(cleaned_directory2, "test_xml_cleaning", cleaned_Top_Charts)

#manage_LastFM_Json()
test("test")
print "OK"
print "--------------------------------------"

