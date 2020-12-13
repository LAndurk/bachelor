import cv2
import numpy as np
from matplotlib import pyplot as plt

def hist_lines(im):
    h = np.zeros((300,256,3))
    if len(im.shape)!=2:
        print("hist_lines applicable only for grayscale images")
        #print("so converting image to grayscale for representation"
        im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    hist_item = cv2.calcHist([im],[0],None,[256],[0,256])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    for x,y in enumerate(hist):
        cv2.line(h,(x,0),(x,y),(255,255,255))
    y = np.flipud(h)
    return y

path="Testbilder/5.png"
img = cv2.imread(path)
x = int(img.shape[1] / 4)  # Breite
y = int(img.shape[0] / 4)  # Höhe
img = cv2.resize(img,(x,y))
print(img.shape)
""""
matrix = np.empty((3,0))
channels = cv2.split(img,matrix)
print(channels[0])
print(channels[1])
cv2.imshow("red",channels[0])
cv2.imshow("green",channels[1])
cv2.imshow("blue",channels[2])
"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = img.copy()
cv2.imshow("img",img)

mask = np.zeros((486,648),np.uint8)
cv2.circle(mask,(324,243),243,(255,255,255),-1)
cv2.imshow("mask",mask)
imgmask = cv2.bitwise_and(img,mask)
cv2.imshow("imgmask",imgmask)

lines = hist_lines(img)
cv2.imshow('histogramdavor',lines)

#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256]); plt.show()


kernel1 = np.array([[1/16, 1/8, 1/16],
                    [1/8, 1/4, 1/8],
                    [1/16, 1/8, 1/16]])
kernel2 = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])
kernel3 = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])
kernel4 = np.array([[1, 2, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

laplace = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("laplace",laplace)
""""
sobelx = np.array((486,648),np.uint64)
sobelx = cv2.filter2D(img,-1,kernel3)
cv2.imshow("sobelx",sobelx)
sobely = np.array((486,648),np.uint64)
sobely = cv2.filter2D(img,-1,kernel4)
cv2.imshow("sobely",sobely)

sobelxx = cv2.Sobel(img,cv2.CV_64F,1,0)
cv2.imshow("sobelxx",sobelxx)
sobelyy = cv2.Sobel(img,cv2.CV_64F,1,0)
cv2.imshow("sobelyy",sobelyy)

magnitude = cv2.magnitude(sobelx,sobely)
cv2.imshow("magnitude",magnitude)
"""
equ = cv2.equalizeHist(img2)
cv2.imshow("equ",equ)

lines = hist_lines(equ)
cv2.imshow('histogramdanach',lines)



#hist = cv2.calcHist([filter],[0],None,[256],[0,256])
#plt.hist(filter.ravel(),256,[0,256]); plt.show()

cv2.waitKey(0)