from collections import deque
from imutils.video import VideoStream
import numpy as numpy
import argparse
import cv2
import imutils
import time
from pynput import mouse

def main():
    cap = cv2.VideoCapture('rtsp://admin:amcrest@192.168.1.21:554/cam/realmonitor?channel=1&subtype=0')
    f = open("points.txt",'w')
    inAir = False
    avg = None
    prevAvg = None
    orangeLower = (0, 85, 204)
    orangeUpper = (255, 255, 255)
    pts = deque(maxlen=64)
    time.sleep(2.0)
    x = 0
    y = 0
    center = 0
    
    while True:
        frame = cap.read()
        frame = frame[1]
        frame = imutils.resize(frame,width = 600)
        
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv, orangeLower, orangeUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c) ##value to keep is x,y
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 10:
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
        
        pts.appendleft(center)
        
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) &0xFF
        
        f.write(x,y,"\n")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
