#!/usr/bin/python
import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,bw = cv2.threshold(gray, 200,230, cv2.THRESH_BINARY)
edges = cv2.Canny(bw, 100, 200, apertureSize=3)

#lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=7)

for x0,y0,x1,y1 in lines[0]:
    x0 = 0
    x1 = img.shape[1]
    if y0-y1 < 10 and y0-y1 > -10:
        cv2.line(img, (x0,y0), (x1,y1), (255, 0, 255), 2)

#for rho,theta in lines[0]:
#
    #offset = 0.03
    #if (np.pi/2)-theta > -offset and (np.pi/2)-theta < offset:
        #print (np.pi/2)-theta
        #a = np.cos(theta)
        #b = np.sin(theta)
        #x0 = a*rho
        #y0 = b*rho
        #x1 = int(x0 + 1000*(-b))
        #y1 = int(y0 + 1000*(a))
        #x2 = int(x0 - 1000*(-b))
        #y2 = int(y0 - 1000*(a))
#
        #color = (255,0,255)
        ##if int(theta) == 0:
        ##    color = (255,0,0)
        ##elif int(theta) == 1:
        ##    color = (0, 255, 0)
        ##    print (np.pi/2)-theta
           # 
        #cv2.line(img, (x1,y1), (x2, y2), color, 2)
#
cv2.imwrite("gray.jpg", bw)
cv2.imwrite("out.jpg", img)
