from Music import music_manager
from Libs import spotipy

import basic_functions, music_functions


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

directory1 = "../Rsc/Data/Original_Music_Source/LastFM/"
directory2 = "../Rsc/Data/Original_Music_Source/Itunes/"
directory3 = "../Rsc/Data/Original_Music_Source/Deezer/"

# Check if the folder exists, otherwise creates it
basic_functions.folder_exist(directory1)
basic_functions.folder_exist(directory2)
basic_functions.folder_exist(directory3)

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
print music_functions.get_Genre_GraceNote("The Weeknd", "Can't Feel My Face")
print "--------------------------------------"
print "--------------------------------------"
print music_functions.get_Genre_GraceNote_DISTINCT("The Weeknd", "Can't Feel My Face")
print "--------------------------------------"
#music_functions.get_Genre_GraceNote_DISTINCT('Drake', 'one dance')

basic_functions.get_files_from_folder(directory1)

#get_Metadata_Spotify("Drake", "One dance")
#print pygn.search(clientID, userID, 'ACDC', 'back in black')
#result = pygn.search(clientID=clientID, userID=userID, artist='ACDC', track='Hells Bells')
#print(json.dumps(result, sort_keys=True, indent=4))
