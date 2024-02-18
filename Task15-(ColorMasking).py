import cv2
import numpy as np

#seting up callback functions for trackbars

def onTrack1(val):
    global huelow
    huelow=val

def onTrack2(val):
    global hueHigh
    hueHigh=val

def onTrack3(val):
    global satlow
    satlow=val

def onTrack4(val):
    global satHigh
    satHigh=val

def onTrack5(val):
    global vallow
    vallow=val

def onTrack6(val):
    global valHigh
    valHigh=val

cv2.namedWindow('Trackbars')

cv2.resizeWindow('Trackbars',400,300)

#initial values of trackbar slider

huelowe=0

hueHigh=0

satlow=0

satHigh=0

vallow=0

valHighe=0

#reating trackbars

cv2.createTrackbar('Hue low', 'Trackbars', 110, 179, onTrack1)
cv2.createTrackbar('Hue High', 'Trackbars', 158, 179, onTrack2)
cv2.createTrackbar('Sat low', 'Trackbars', 0, 255, onTrack3)
cv2.createTrackbar('Sat High', 'Trackbars', 255, 255, onTrack4) 
cv2.createTrackbar('Val low', 'Trackbars', 134, 255, onTrack5) 
cv2.createTrackbar('Val High', 'Trackbars', 255, 255, onTrack6)

image = cv2.imread("C:/Users/karth/Downloads/ball.jpeg")
while True:
    frameHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([huelow,satlow,vallqow])#lower and upper boundary for color range in HSV
    upperBound = np.array([hueHigh,satHigh,valHigh])
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)#Creating Mask usingthe color range
    masked = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('mask', mask)
    cv2.imshow('Ball', image)
    cv2.imshow('masked',masked)
    print('lowerBound: ', lowerBound)
    print('upperBound: ', upperBound)
    if cv2.waitKey(1) & 0xff == ord('q'): # to quit the camera press 'q'
        break
cv2.destroyAllWindows()