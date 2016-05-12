from Music import music_manager
from Libs import spotipy

import functions, music_functions


# Files/Folders related functions
#def folder_exist(directory):
#    if not os.path.exists(directory):
#        os.makedirs(directory)
#        print "Folder created"
#    else:
#        print "Folder already exist"




#
# At Startup do that
#

directory1 = "../Rsc/Data/Music/LastFM/"
directory2 = "../Rsc/Data/Music/Itunes/"
directory3 = "../Rsc/Data/Music/Deezer/"

# Check if the folder exists, otherwise creates it
functions.folder_exist(directory1)
functions.folder_exist(directory2)
functions.folder_exist(directory3)

# Launch music manager To Fetch data --> MUST BE DONE ONCE A WEEK
#music_manager.main()


# Test Gracenote Wrapper
#userID = pygn.register(clientID)






def get_Metadata_Spotify(artist="", track=""):
    sp = spotipy.Spotify()
    results = sp.search(q='artist:' + artist, type='artist')
    results1 = sp.search(q='track:' + track, type='track')
    query = "artist:" + artist + "&" + "track:" + track
    track_info = sp.search(q='artist:' + artist + '&' + 'track:' + track, type='track')
    print results1

    print track_info
    print query

#get_Genre_GraceNote("Drake", "One dance")
#get_Genre_GraceNote("Prince", "Purple rain")
#get_Genre_GraceNote("adele", "hello")
print "--------------------------------------"
#get_Genre_GraceNote('Drake', 'one dance')
print "--------------------------------------"
music_functions.get_Genre_GraceNote_DISTINCT('Drake', 'one dance')
#get_Metadata_Spotify("Drake", "One dance")
#print pygn.search(clientID, userID, 'ACDC', 'back in black')
#result = pygn.search(clientID=clientID, userID=userID, artist='ACDC', track='Hells Bells')
#print(json.dumps(result, sort_keys=True, indent=4))
