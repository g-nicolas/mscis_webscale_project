import urllib2
from Core import basic_functions
url = "http://api.musicgraph.com/api/v2/track/search?api_key=c8303e90962e3a5ebd5a1f260a69b138&artist_name=Adele&title=hello"
data = basic_functions.get_Json_From_URL(url)
response = urllib2.urlopen(url)
print response
print data

def music_graph_request_builder()