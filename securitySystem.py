import cv2
import dropbox
import time
import random

start = time.time()

def clickPic():
    img = cv2.VideoCapture(0)
    active = True
    num = random.randint(0,100)
    while active==True:
        ret, frame = img.read()
        name = 'img'+str(num)+'.png'
        cv2.imwrite(name, frame)
        start = time.time()
        active = False
    print('picture captured')
    img.release()
    cv2.destroyAllWindows()
    return(name)

def upload(name):
    dbx = dropbox.Dropbox('sl.BD_tClVVuuYU2rIxKAUuQly19YBR_ZLHjZa6etRyXB25QWRTxvQR6Vh6SSUdpYLafAZiUcgLDZtbcs5GY43dkmUJ3JGgsCfzX3Br2ua3zLCWBaiij07rR_egX2G3iEzZGD1EjFU')
    with open(name,'rb') as file:
        dbx.files_upload(file.read(), '/'+name)
    print('image has been uploaded')

while True:
    if time.time()-start>=5:
        name=clickPic()
        upload(name)

    