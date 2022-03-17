import cv2

def clickPic():
    #videocapture will open camera and 0 is for default camera
    img = cv2.VideoCapture(0)
    active = True
    while active == True:
        #ret is telling if camera is working or not and frame is the actual image
        ret, frame = img.read()
        #to save
        cv2.imwrite('image.png', frame)
        active = False
    img.release()
    cv2.destroyAllWindows()

clickPic()