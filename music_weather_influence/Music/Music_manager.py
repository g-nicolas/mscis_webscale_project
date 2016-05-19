from Core import basic_functions

import time

directory1 = "../Rsc/Data/Original_Music_Source/LastFM/"
directory2 = "../Rsc/Data/Original_Music_Source/Itunes/"
directory3 = "../Rsc/Data/Original_Music_Source/Deezer/"

fname_LastFM_CH = "LastFM_top_songs_switzerland"
fname_LastFM_AT = "LastFM_top_songs_austria"
fname_Itunes_AT = "Itunes_top_songs_austria"
fname_Itunes_CH = "Itunes_top_songs_switzerland"
fname_Spotify_AT = "Spotify_top_songs_austria"
fname_Spotify_CH = "Spotify_top_songs_switzerland"
fname_Deezer_AT = "Deezer_top_songs_austria"
fname_Deezer_CH = "Deezer_top_songs_switzerland"


#Last FM Top Songs Swiss - geo.getTopTracks:
url_lastFM_Top_Songs_CH = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=switzerland&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&limit=50&format=json"

#Last FM Top Songs Austria - geo.getTopTracks:
url_lastFM_Top_Songs_AT = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=austria&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&limit=50&format=json"

#Itunes Top Songs Swiss:
url_Itunes_Top_Songs_CH = "https://itunes.apple.com/ch/rss/topsongs/limit=100/explicit=true/json"

#Itunes Top Songs Austria:
url_Itunes_Top_Songs_AT = "https://itunes.apple.com/at/rss/topsongs/limit=100/explicit=true/json"

#Spotify Top Songs Swiss:
url_Spotify_Top_Songs_CH = "https://itunes.apple.com/ch/rss/topsongs/limit=100/explicit=true/json"

#Spotify Top Songs Austria:
url_Spotify_Top_Songs_AT = "https://itunes.apple.com/at/rss/topsongs/limit=100/explicit=true/json"

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
    # Fetch data
    lastFM_Top_Songs_AT_Json = basic_functions.get_Json_From_URL(url_lastFM_Top_Songs_AT)
    lastFM_Top_Songs_CH_Json = basic_functions.get_Json_From_URL(url_lastFM_Top_Songs_CH)

    itunes_Top_Songs_CH_XML = basic_functions.get_XML_From_URL(url_Itunes_Top_Songs_CH)
    itunes_Top_Songs_AT_XML = basic_functions.get_XML_From_URL(url_Itunes_Top_Songs_AT)

    # Save data to folder
    basic_functions.save_Json_To_File(directory1, fname_LastFM_CH, lastFM_Top_Songs_CH_Json)
    basic_functions.save_Json_To_File(directory1, fname_LastFM_AT, lastFM_Top_Songs_AT_Json)
    basic_functions.save_XML_To_File(directory2, fname_Itunes_CH, itunes_Top_Songs_CH_XML)
    basic_functions.save_XML_To_File(directory2, fname_Itunes_AT, itunes_Top_Songs_AT_XML)

    # DO SOMETHING WITH THE DATA HERE
