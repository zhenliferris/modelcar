import cv2
import numpy as np
import utlis


def getLaneCurve(img):
    imgCopy = img.copy()
    imgThres = utlis.thresholding(img)

    h,w,c = img.shape
    points = utlis.valTrackbars()
    imgWarp = utlis.warpImg(imgThres,points,w,h)
    imgWarpPoints = utlis.drawPoints(imgCopy,points)

    cv2.imshow('Thres', imgThres)
    cv2.imshow('Warp', imgWarp)
    cv2.imshow('Warp Points', imgWarpPoints)
    return None

if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    #region of intrest, initial size
    intialTrackBarVals = [102,80,20,214]
    utlis.initializeTrackbars(intialTrackBarVals)
    frameCounter = 0
    while True:
        frameCounter +=1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter=0

        success, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        getLaneCurve(img)

        cv2.imshow('Vid',img)
        cv2.waitKey(1)