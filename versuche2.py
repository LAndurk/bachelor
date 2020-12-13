import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path="Testbilder/1.png"
img = cv.imread(path)
x = int(img.shape[1] / 4)  # Breite
y = int(img.shape[0] / 4)  # Höhe
img = cv.resize(img,(x,y))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret,threshold = cv.threshold(img,100,255,cv.THRESH_BINARY)
cv.imshow("threshold",threshold)

kernel = np.ones((3,3),np.uint8)
gradient = cv.morphologyEx(threshold, cv.MORPH_GRADIENT, kernel)
cv.imshow("gradient",gradient)

""""
kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])
filter = np.array((y,x),np.uint64)
filter = cv.filter2D(img,-1,kernel)
cv.imshow("filter",filter)
"""
""""
laplace = cv.Laplacian(img,cv.CV_64F,ksize=5)
cv.imshow("laplace",laplace)

sobelSobel = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
#print(sobelSobel)
sobelSobelabs = np.absolute(sobelSobel)
#print(sobelSobelabs)
sobelSobelabs8 = np.uint8(sobelSobelabs)
print("sobelSobelabs8",sobelSobelabs8)
cv.imshow("sobelSobel",sobelSobelabs8)

kernel4 = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
sobelx = np.array((y,x),np.uint64)
sobelx = cv.filter2D(img,-1,kernel4)
print("sobelx",sobelx)
#cv.imwrite("Zwischenergebnisbilder/sobelx.png",sobelx)
cv.imshow("sobelx",sobelx)
"""

cv.waitKey(0)