import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dorito_aisle.jpg', 0)
ret,img = cv2.threshold(img, 200,230, cv2.THRESH_BINARY)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
