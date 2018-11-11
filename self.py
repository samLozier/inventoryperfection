import os
from getfile import getfile
from database import database
from uploadinventory import uploadinventory

links = database()
destination = '/Users/samlozier/Downloads/aofile.csv'
for i in links:
    try:
        getfile(i, destination)
    finally:
        print('alldone')

for filename in os.listdir(destination):
    uploadinventory(filename)






