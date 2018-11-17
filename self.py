import glob
import os

from database import database
from dropboxget import dropboxGetfile
from uploadinventory import uploadinventory

print('connecting to databse')
links = database()
print('got links')


#download files from dropbox

print('getting files')
for i in links:
    if '/' in i:
        filename = i.rsplit('/', 1)[1]
        print(filename)
    else:
        filename = i
        print('didnt find filename in link string')
    destination = '/Users/samlozier/Downloads/newfiles/'

    try:
        fullpath = os.path.join(destination, filename)
        dropboxGetfile(fullpath, i)

    finally:
        print('gotfile')
print('Downloaded all files')


# read csv data into database

print('updating database')

dirs = '/Users/samlozier/Downloads/newfiles/*.csv'

for filename in glob.glob(dirs):

    print(filename)
    uploadinventory(filename)

print('updated database')






