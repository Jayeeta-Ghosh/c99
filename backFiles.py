import os
import shutil
src=input("Enter source folder name")
dest=input("Enter destination folder")
src=src+'/'
dest=dest+'/'
listOfFiles=os.listdir(src)
for file in listOfFiles:
    shutil.copy((src+file),dest)