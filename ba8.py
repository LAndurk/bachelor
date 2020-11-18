# Plexiglasteile
import cv2
import numpy as np
import hilfsfunktionen as hf

ergebnis = True

#Preprocessing
img = cv2.imread("Bilder/x2.png")
x = int(img.shape[1] / 4)  # Breite
y = int(img.shape[0] / 4)  # Höhe
img = cv2.resize(img,(x,y))
#img = hf.quarter(img,1)
#img = img[50:img.shape[0]-50,50:img.shape[1]-50]
hoehe = img.shape[0]
breite = img.shape[1]
#rohbild = img.copy()
imgBW = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)

 #adaptives threshold preprocessing
threshold = cv2.adaptiveThreshold(imgBW,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,301,0)
cv2.line(threshold,(int(breite/2),0),(int(breite/2),hoehe),(255,255,255),3) #vertikal
cv2.line(threshold,(0,int(hoehe/2)),(breite,int(hoehe/2)),(255,255,255),3) #horizontal
cv2.imshow("threshold",threshold)
kernel = np.ones((7,7),np.uint8)
thresholdEro = cv2.erode(threshold, kernel, iterations=1)
cv2.imshow("thresholdEro", thresholdEro)
thresholdDil = cv2.dilate(thresholdEro, kernel, iterations=1)
cv2.imshow("thresholdDil", thresholdDil)

#approx
contours, hierarchy = cv2.findContours(thresholdDil, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    print("Area",cv2.contourArea(cnt))
    if cv2.contourArea(cnt) > 100:
        #print(cnt)
        cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)
        #print(len(approx))
        print(approx)
        print("Length",len(approx))
        if len(approx)==1:
            continue
        cv2.drawContours(img, [approx], -1, (255, 0, 0), 3)
        print(approx[0,0,0])
        print(approx[0,0,1])
        print(approx[1,0,0])
        print(approx[1,0,1])
        #print(img.shape[1]-10)
        if  (approx[0,0,0]>10 and approx[0,0,0]<img.shape[1]-10) and (approx[0,0,1]>10 and approx[0,0,1]<img.shape[0]-10) \
            or (approx[1, 0, 0] > 10 and approx[1, 0, 0] < img.shape[1] - 10) and (approx[1, 0, 1] > 10 and approx[1, 0, 1] < img.shape[0] - 10):
            print("schlecht")
            ergebnis = False
#cv2.imshow("rohbild",rohbild)
cv2.imshow("img",img)

if ergebnis == False:
    print("!!!Schlechtteil!!!")
else:
    print("Gutteil")
cv2.waitKey(0)