import os
import urllib2
import json

# Files/Folders related functions
def file_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print "Folder created"
    else:
        print "Folder already exist"


def file_creator(path, filename):
    if os.path.exists(path):
        if not os.path.isfile(path + filename):
            file = open(path + filename + ".txt", "w")
            # file.write("hello world in the new file")
            file.close()
            print "File created"
        else:
            print "File already exist"
    else:
        print "Folder does not exist"
        file_exist(path)
        file_creator(path, filename)

def file_creator_writer(path, filename, content):
    if os.path.exists(path):
        if not os.path.isfile(path + filename):
            file = open(path + filename + ".txt", "w")
            file.write(content)
            file.close()
            print "File created"
        else:
            print "File already exist"
    else:
        print "Folder does not exist"
        file_exist(path)
        file_creator(path, filename)


# LastFM REST Requests related functions
def get_Json_From_URL(url):
    response = urllib2.urlopen(url)
    data = json.load(response)
    return data

# Writing JSON data to File
def save_Json_To_File(path, filename, json_data):
    with open(path + filename, 'w') as f:
        json.dump(json_data, f)









