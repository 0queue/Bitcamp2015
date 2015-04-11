#!/usr/bin/python
import cv2
import numpy as np

img = cv2.imread("dorito_aisle.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,gray = cv2.threshold(gray, 200,230, cv2.THRESH_BINARY)
edges = cv2.Canny(gray, 100, 200, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
for rho,theta in lines[0]:

    if int(theta) == 1:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        color = (0,0,255)
        #if int(theta) == 0:
        #    color = (255,0,0)
        #elif int(theta) == 1:
        #    color = (0, 255, 0)
            
        cv2.line(img, (x1,y1), (x2, y2), color, 2)

cv2.imwrite("out.jpg", img)
