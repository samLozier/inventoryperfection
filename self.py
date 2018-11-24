import glob
import os

import config as cfg
from methods import database_getlinks
from methods import database_uploadcsv
from methods import dropboxGetfile

print('connecting to data base')
links = database_getlinks()
print('got links from database')


#download files from dropbox

print('getting files from Dropbox')
for i in links:
    if '/' in i:
        filename = i.rsplit('/', 1)[1]
        print(filename)
    else:
        filename = i
        print('didnt find filename in link string')
    destination = cfg.destination['destination']
    print(destination)

    try:
        fullpath = os.path.join(destination, filename)
        dropboxGetfile(fullpath, i)

    finally:
        print('gotfile')
print('Downloaded all files from Dropbox')


# read csv data into database

print('updating database')

dirs = cfg.localdirectory['localdirectory']

for filename in glob.glob(dirs):

    print(filename)
    database_uploadcsv(filename)

print('Inventory Update Complete')






