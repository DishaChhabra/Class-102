import os
import shutil

src = input('enter a source file/folder : ')
dest = input('enter a destination folder : ')

# to go into the folder
src = src+'/'
dest = dest+'/'
files = os.listdir(src)

for i in files:
    #shutil is used to copy/move files 
    shutil.copy((src+i), dest)