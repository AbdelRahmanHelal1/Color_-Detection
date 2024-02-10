import cv2
import numpy as np

import time

cap=cv2.VideoCapture(0)


#######################
def empty():
    pass
#name of window
cv2.namedWindow("fire detection")
cv2.resizeWindow("fire detection",500,250)
cv2.createTrackbar("huemin","fire detection",0,179,empty)
cv2.createTrackbar("huemax","fire detection",179,179,empty)
cv2.createTrackbar("satmin","fire detection",0,255,empty)
cv2.createTrackbar("satmax","fire detection",255,255,empty)
cv2.createTrackbar("valmin","fire detection",252,255,empty)
cv2.createTrackbar("valmax","fire detection",255,255,empty)

while True:
    _,img=cap.read()
    #convert image into hsv color
    imghvs=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    x1 = cv2.getTrackbarPos("huemin", "fire detection")
    x2 = cv2.getTrackbarPos("huemax", "fire detection")
    y1 = cv2.getTrackbarPos("satmin", "fire detection")
    y2 = cv2.getTrackbarPos("satmax", "fire detection")
    z1 = cv2.getTrackbarPos("valmin", "fire detection")
    z2 = cv2.getTrackbarPos("valmax", "fire detection")
    print(x1, y1, z1, x2, y2, z2)
    low = np.array([x1, y1, z1])
    uper = np.array([x2, y2, z2])
    mask = cv2.inRange(imghvs, low, uper)
    #imageresult = cv2.bitwise_and(img, img, mask=mask)
    contour,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cont in contour:
        area= cv2.contourArea(cont)
        arc = cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, 0.01 * arc, True)
        x, y, w, h = cv2.boundingRect(approx)
        if area > 100:
            cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 2)


    cv2.imshow("img",img)
    cv2.imshow("mask",mask)

    #cv2.imshow("mask",mask)
    if cv2.waitKey(1)==ord("s"):
        break
cap.release()
cv2.destroyAllWindows()