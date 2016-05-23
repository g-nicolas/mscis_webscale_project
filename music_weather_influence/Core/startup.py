from Music import music_manager
from Libs import spotipy

import basic_functions, music_functions
from Music import music_parser

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
output_directory1 = "../Rsc/Data/Cleaned_Music_Source/LastFM/"
output_directory2 = "../Rsc/Data/Cleaned_Music_Source/Itunes/"

# Check if the folder exists, otherwise creates it
basic_functions.folder_exist(directory1)
basic_functions.folder_exist(directory2)
basic_functions.folder_exist(output_directory1)
basic_functions.folder_exist(output_directory2)

# Launch music manager To Fetch data --> MUST BE DONE ONCE A WEEK
#music_manager.main()
#music_parser.clean_lfm()



