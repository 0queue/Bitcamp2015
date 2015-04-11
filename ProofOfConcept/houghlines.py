#!/usr/bin/python
import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])
img2 = img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,bw = cv2.threshold(gray, 200,230, cv2.THRESH_BINARY)
edges = cv2.Canny(bw, 100, 200, apertureSize=3)

ys = []

#lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=7)

for x0,y0,x1,y1 in lines[0]:
    x0 = 0
    x1 = img.shape[1]
    if y0-y1 < 10 and y0-y1 > -10:
        ys.append(y0)

ys.sort()
dv = 30
for i in range(len(ys) - 1):
    if ys[i+1] - ys[i] < dv:
        ys[i] = (ys[i] + ys[i+1]) /2
        cv2.line(img2, (0,ys[i]), (img.shape[1],ys[i]), (255, 0, 255), 2)

cv2.imwrite("gray.jpg", bw)
cv2.imwrite("out.jpg", img)
cv2.imwrite("out2.jpg", img2)
