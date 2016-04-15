from Core import functions

directory1 = "../Rsc/Data/LastFM/"

fname_AT = "top_songs_austria.json"
fname_CH = "top_songs_switzerland.json"

#Top Songs Swiss - geo.getTopTracks:
url_lastFM_Top_Songs_CH = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=switzerland&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&format=json"
#Top Songs Austria - geo.getTopTracks:
url_lastFM_Top_Songs_AT = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=austria&api_key=46ab0cf62548d9fbd9bd4ba79e40f168&format=json"


lastFM_Top_Songs_AT_Json = functions.get_Json_From_URL(url_lastFM_Top_Songs_AT)

lastFM_Top_Songs_CH_Json = functions.get_Json_From_URL(url_lastFM_Top_Songs_CH)


functions.save_Json_To_File(directory1, fname_AT, lastFM_Top_Songs_AT_Json)

functions.save_Json_To_File(directory1, fname_CH, lastFM_Top_Songs_CH_Json)

# DO SOMETHING WITH THE DATA HERE