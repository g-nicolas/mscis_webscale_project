from Core import basic_functions, music_functions
import os

def clean_lastfm_data_from_url(filename, json_data, output_directory):
    cleaned_Top_Charts = {}
    cleaned_Top_Charts["ID"] = filename
    cleaned_Top_Charts["weather_ID"] = "weather_ID"

    cleaned_Top_Charts["TopCharts"] = []

    # url = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=switzerland&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&limit=10&format=json"

    tracks_list = json_data["tracks"]["track"]
    for track_info in tracks_list:
        track_rank = track_info["@attr"]["rank"]
        track_name = track_info["name"]
        track_artist = track_info["artist"]["name"]
        track_genre = music_functions.get_genre_graceNote_distinct(track_artist, track_name)
        #track_weather_id = "track_weather_ID"
        #cleaned_track_info = {"track_rank": int(track_rank) + 1, "track_name": track_name, "track_artist": track_artist, "track_genre": track_genre, "track_weather_ID": track_weather_id}
        cleaned_track_info = {"track_rank": int(track_rank) + 1, "track_name": track_name, "track_artist": track_artist,
                              "track_genre": track_genre}
        cleaned_Top_Charts["TopCharts"].append(cleaned_track_info)

    basic_functions.save_Json_To_File(output_directory, filename, cleaned_Top_Charts)


def clean_itunes_data_from_url(filename, json_data, output_directory):
    cleaned_top_charts = {}
    cleaned_top_charts["ID"] = filename
    cleaned_top_charts["weather_ID"] = "weather_ID"

    cleaned_top_charts["TopCharts"] = []

    # url = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=switzerland&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&limit=10&format=json"
    # data = basic_functions.get_Json_From_URL(url)
    tracks_list = json_data["feed"]["entry"]
    rank = 1

    for track_info in tracks_list:
        # track_info["title"]["label"]
        track_rank = rank
        track_name_artist = track_info["title"]["label"].partition(' - ')
        track_name = track_name_artist[0]
        track_artist = track_name_artist[2]
        track_genre = music_functions.get_genre_graceNote_distinct(track_artist, track_name)
        #track_weather_id = "track_weather_ID"
        #cleaned_track_info = {"track_rank": track_rank, "track_name": track_name, "track_artist": track_artist, "track_genre": track_genre, "track_weather_ID": track_weather_ID}
        cleaned_track_info = {"track_rank": track_rank, "track_name": track_name, "track_artist": track_artist,
                              "track_genre": track_genre}
        rank += 1
        cleaned_top_charts["TopCharts"].append(cleaned_track_info)

    basic_functions.save_Json_To_File(output_directory, filename, cleaned_top_charts)


def clean_old_lfm():
    directory1 = "../Rsc/Data/Original_Music_Source/LastFM/"
    cleaned_directory1 = "../Rsc/Data/Cleaned_Music_Source/LastFM/"
    file1 = directory1+"LastFM_top_songs_switzerland_20160512"
    files_list = basic_functions.get_files_from_folder(directory1)
    for data_file in files_list:
        if data_file.startswith("LastFM_top_songs_switzerland_20160512"):
            j_file = os.path.join(directory1, data_file)
            j_data = basic_functions.get_Json_From_file(j_file)
            #j_data = basic_functions.get_Json_From_file(data_file)
            clean_lastfm_data_from_url("LastFM_top_songs_switzerland_20160512", j_data, cleaned_directory1)
    #clean_lastfm_data_from_url("LastFM_top_songs_switzerland_20160512", j_data, cleaned_directory1)


def clean_old_lastfm():
    directory1 = "../Rsc/Data/Original_Music_Source/LastFM/"
    cleaned_directory1 = "../Rsc/Data/Cleaned_Music_Source/LastFM/"

    files_list = basic_functions.get_files_from_folder(directory1)
    for data_file in files_list:
        if data_file.startswith("LastFM_top_songs_switzerland_20160512"):
            j_file = os.path.join(directory1, data_file)
            j_data = basic_functions.get_Json_From_file(directory1+j_file)
            clean_lastfm_data_from_url(data_file, j_data, cleaned_directory1)
