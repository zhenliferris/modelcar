import cv2
import utlis

cap = cv2.VideoCapture(0)
intialTrackBarVals = [114, 109, 32, 231]
utlis.initializeTrackbars(intialTrackBarVals)

def getImg(display= False,size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)