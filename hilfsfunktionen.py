import cv2
import numpy as np

def quarter(img,quadrant):
    x = img.shape[1]  # Breite
    y = img.shape[0]  # Höhe
    if quadrant == 1:
        img = img[:int(y / 2) - 1,int(x / 2) + 1:]
    elif quadrant == 2:
      img = img[:int(y / 2) - 1, :int(x / 2) - 1]
    elif quadrant == 3:
        img = img[int(y / 2) + 1:, :int(x / 2) - 1]
    elif quadrant == 4:
        img = img[int(y / 2) + 1:, int(x / 2) + 1:]

    return img

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

""""
archivierter Code
"""

""""#globales threshold preprocessing
_,threshold = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
thresholdEro = cv2.erode(threshold, kernel, iterations=1)
cv2.imshow("thresholdEro", thresholdEro)
thresholdDil = cv2.dilate(thresholdEro, kernel, iterations=1)
cv2.imshow("thresholdDil", thresholdDil)

imgCanny = cv2.Canny(thresholdDil,100,200)
cv2.imshow("imgCanny",imgCanny)
"""

"""" #cornerHarris
thresholdDil = np.float32(thresholdDil)
harris = cv2.cornerHarris(thresholdDil,2,3,0.04)
cv2.imshow("harris",harris)
harris = cv2.dilate(harris,None)
cv2.imshow("harrisdil",harris)
"""

""""#HoughLinesP
imgCanny = cv2.Canny(thresholdDil,100,200)
cv2.imshow("imgCanny",imgCanny)

lines = cv2.HoughLinesP(imgCanny,1,np.pi/180,1,minLineLength=100,maxLineGap=50)
print(lines)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("img2",img)
"""

"""" #findContours
imgContour = img.copy()
contours,hierarchy = cv2.findContours(thresholdDil,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 0: #kleine Konturen (kleiner als 500 Pixel) die fälschlicherweise entdeckt wurden ignorieren
            #print(area) #Pixelgröße?
            cv2.drawContours(imgContour,cnt,-1,(0,0,0),3)
cv2.imshow("imgContour",imgContour)
"""