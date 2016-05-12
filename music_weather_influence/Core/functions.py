import os
import urllib2
import json
import time

# Files/Folders related functions
def folder_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print "Folder created"
    else:
        print "Folder already exist"

def file_exist(path, filename):
    if os.path.exists(path):
        if os.path.isfile(path + filename):
            return 1
        else:
            return 0
    else:
        print "Folder does not exist"
        return 2

def file_creator(path, filename):
    if os.path.exists(path):
        if not os.path.isfile(path + filename):
            file = open(path + filename + ".txt", "w")
            file.close()
            print "File created"
        else:
            print "File already exist"
    else:
        print "Folder does not exist"
        folder_exist(path)
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
        folder_exist(path)
        file_creator(path, filename)


# LastFM REST Requests related functions
def get_Json_From_URL(url):
    response = urllib2.urlopen(url)
    data = json.load(response)
    return data

# Writing JSON data to File
def save_Json_To_File(path, filename, json_data):
    if file_exist(path, filename) == 0:
        timestr = time.strftime("%Y%m%d")
        with open(path + filename + "_" + timestr + ".json", 'w') as f:
            json.dump(json_data, f, indent=2)
        print "File " + filename + " created: "
    elif file_exist(path, filename) == 1:
        print "File already exists"
    else:
        print "File already exists"



# Itunes Requests related functions
def get_XML_From_URL(url):
    response = urllib2.urlopen(url)
    #data = json.load(response)
    return response

# Writing XML data to File
def save_XML_To_File(path, filename, url):
    if file_exist(path, filename) == 0:
        timestr = time.strftime("%Y%m%d")
        with open(path + filename + "_" + timestr + ".xml", 'w') as f:
            #f.write(urllib2.urlopen(url).read())
            f.write(url.read())
            f.close()
        print "File " + filename + " created: "
    elif file_exist(path, filename) == 1:
        print "File " + filename + " already exists"
    else:
        print "Wrong Folder. Does not exist"







