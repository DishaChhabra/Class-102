import os
import shutil

path = input('enter folder to organize - ')
files = os.listdir(path)

for i in files:
    name, ext = os.path.splitext(i)
    if ext == '' :
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+i, path+'/'+ext+'/'+i)
    else :
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+i, path+'/'+ext+'/'+i)
    

