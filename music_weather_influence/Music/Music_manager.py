from Core import basic_functions, music_functions
import music_parser

import time

directory1 = "../Rsc/Data/Original_Music_Source/LastFM/"
directory2 = "../Rsc/Data/Original_Music_Source/Itunes/"
directory3 = "../Rsc/Data/Original_Music_Source/Deezer/"


output_directory1 = "../Rsc/Data/Cleaned_Music_Source/LastFM/"
output_directory2 = "../Rsc/Data/Cleaned_Music_Source/Itunes/"

fname_LastFM_CH = "LastFM_top_songs_switzerland"
fname_LastFM_AT = "LastFM_top_songs_austria"

fname_Itunes_AT = "Itunes_top_songs_austria"
fname_Itunes_CH = "Itunes_top_songs_switzerland"
#fname_Spotify_AT = "Spotify_top_songs_austria"
#fname_Spotify_CH = "Spotify_top_songs_switzerland"
#fname_Deezer_AT = "Deezer_top_songs_austria"
#fname_Deezer_CH = "Deezer_top_songs_switzerland"


#Last FM Top Songs Swiss - geo.getTopTracks:
url_lastFM_Top_Songs_CH = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=switzerland&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&limit=50&format=json"

#Last FM Top Songs Austria - geo.getTopTracks:
url_lastFM_Top_Songs_AT = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=austria&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&limit=50&format=json"

#Itunes Top Songs Swiss:
url_Itunes_Top_Songs_CH = "https://itunes.apple.com/ch/rss/topsongs/limit=100/explicit=true/json"

#Itunes Top Songs Austria:
url_Itunes_Top_Songs_AT = "https://itunes.apple.com/at/rss/topsongs/limit=100/explicit=true/json"

#Spotify Top Songs Swiss:
#url_Spotify_Top_Songs_CH = "https://itunes.apple.com/ch/rss/topsongs/limit=100/explicit=true/json"

#Spotify Top Songs Austria:
#url_Spotify_Top_Songs_AT = "https://itunes.apple.com/at/rss/topsongs/limit=100/explicit=true/json"

#Deezer Top Songs Swiss:
#url_Deezer_Top_Songs_CH = "https://itunes.apple.com/ch/rss/topsongs/limit=100/explicit=true/xml"

#Spotify Top Songs Austria:
#url_Deezer_Top_Songs_AT = "https://itunes.apple.com/at/rss/topsongs/limit=100/explicit=true/xml"



if __name__ == "__main__":

    # Fetch data
    lastFM_Top_Songs_AT_Json = basic_functions.get_Json_From_URL(url_lastFM_Top_Songs_AT)
    lastFM_Top_Songs_CH_Json = basic_functions.get_Json_From_URL(url_lastFM_Top_Songs_CH)

    itunes_Top_Songs_CH_XML = basic_functions.get_XML_From_URL(url_Itunes_Top_Songs_CH)
    itunes_Top_Songs_AT_XML = basic_functions.get_XML_From_URL(url_Itunes_Top_Songs_AT)

    # Save data to folder
    basic_functions.save_Json_To_File(directory1, fname_LastFM_CH, lastFM_Top_Songs_AT_Json)
    basic_functions.save_Json_To_File(directory1, fname_LastFM_AT, lastFM_Top_Songs_AT_Json)
    basic_functions.save_XML_To_File(directory2, fname_Itunes_CH, itunes_Top_Songs_CH_XML)
    basic_functions.save_XML_To_File(directory2, fname_Itunes_AT, itunes_Top_Songs_AT_XML)

def main():
    ################################################
    #  Fetch data
    ################################################
    lastFM_Top_Songs_CH_Json = basic_functions.get_Json_From_URL(url_lastFM_Top_Songs_CH)
    lastFM_Top_Songs_AT_Json = basic_functions.get_Json_From_URL(url_lastFM_Top_Songs_AT)

    itunes_Top_Songs_CH_Json = basic_functions.get_Json_From_URL(url_Itunes_Top_Songs_CH)
    itunes_Top_Songs_AT_Json = basic_functions.get_Json_From_URL(url_Itunes_Top_Songs_AT)

    ################################################
    #  Save original data to folder
    ################################################
    basic_functions.save_Json_To_File(directory1, fname_LastFM_CH, lastFM_Top_Songs_CH_Json)
    basic_functions.save_Json_To_File(directory1, fname_LastFM_AT, lastFM_Top_Songs_AT_Json)

    basic_functions.save_Json_To_File(directory2, fname_Itunes_CH, itunes_Top_Songs_CH_Json)
    basic_functions.save_Json_To_File(directory2, fname_Itunes_AT, itunes_Top_Songs_AT_Json)

    ################################################
    #  Clean data here
    ################################################
    music_parser.clean_lastfm_data_from_url(fname_LastFM_CH, lastFM_Top_Songs_CH_Json, output_directory1)
    music_parser.clean_lastfm_data_from_url(fname_LastFM_AT, lastFM_Top_Songs_AT_Json, output_directory1)

    music_parser.clean_itunes_data_from_url(fname_Itunes_CH, itunes_Top_Songs_CH_Json, output_directory2)
    music_parser.clean_itunes_data_from_url(fname_Itunes_AT, itunes_Top_Songs_AT_Json, output_directory2)

    # DO SOMETHING WITH THE DATA HERE
def clean_old_itunes():
    ################################################
    files_list = basic_functions.get_files_from_folder(directory2)
    for data_file in files_list:
        #if data_file.startswith("LastFM_top_songs"):
        if data_file.startswith("LastFM_"):
            #PARSE DATA HERE
            print data_file
            #cleaned_data = clean_LastFM_Json(directory1, data_file)
            #test(data_file)
            pass

def clean_old_lastfm():
    ################################################
    files_list = basic_functions.get_files_from_folder(directory1)
    for data_file in files_list:
        #if data_file.startswith("LastFM_top_songs"):
        if data_file.startswith("LastFM_"):
            clean_from_folder(directory1, directory3, data_file)
            #cleaned_data = clean_LastFM_Json(directory1, data_file)
            #test(data_file)
            pass

def clean_from_folder(source_directory, output_directory, filename):
    cleaned_Top_Charts = {}
    cleaned_Top_Charts["ID"] = filename

    cleaned_Top_Charts["TopCharts"] = []

    #print source_directory+filename
    data = basic_functions.get_Json_From_file(source_directory+filename)
    tracks_list = data["tracks"]["track"]
    print data
    for track_info in tracks_list:
        track_rank = track_info["@attr"]["rank"]
        track_name = track_info["name"]
        track_artist = track_info["artist"]["name"]
        track_genre = music_functions.get_genre_graceNote_distinct(track_artist, track_name)
        track_weather_ID = "track_weather_ID"
        #cleaned_track_info = {"track_rank": track_rank, "track_name": track_name, "track_artist": track_artist, "track_genre": track_genre, "track_weather_ID": track_weather_ID }
        #cleaned_Top_Charts["TopCharts"].append(cleaned_track_info)

    #basic_functions.save_Json_To_File(output_directory, "test_json_cleaning", cleaned_Top_Charts)