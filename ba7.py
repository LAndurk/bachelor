# ToDo: Problem adaptive thresholding bei großen schwarzen Bereichen ohne Leiterbahn
# ToDo: Problem Randbereich

import cv2
import numpy as np


def damageDetection(img):

    ergebnis = True
    coordinates = []

    imgSobel = cv2.Sobel(img,cv2.CV_64F,0,1)
    cv2.imshow("Sobel",imgSobel)

    #Preprocessing
    imgBW = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    threshold = cv2.adaptiveThreshold(imgBW,500,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,301,0)
    cv2.imshow("threshold",threshold)
    #cv2.imwrite("Ausgangsbilder/thresholdpic.png", threshold)
    kernel = np.ones((7,7),np.uint8)
    thresholdEro = cv2.erode(threshold, kernel, iterations=1)
    cv2.imshow("thresholdEro", thresholdEro)
    #cv2.imwrite("Ausgangsbilder/eropic.png", thresholdEro)
    thresholdDil = cv2.dilate(thresholdEro, kernel, iterations=1)
    cv2.imshow("thresholdDil", thresholdDil)
    #cv2.imwrite("Ausgangsbilder/dilpic.png", thresholdDil)

    imgSobel2 = cv2.Sobel(thresholdDil,cv2.CV_64F,0,1)
    cv2.imshow("Sobel2",imgSobel2)

    imgCanny = cv2.Canny(thresholdDil,10,10)
    #cv2.imshow("Canny", imgCanny)

    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(len(contours))
    for cnt in contours:
    #for i in range(len(contours)):
        if True: #cv2.contourArea(cnt) > 0:
            print("+1")
            #print(contours[i])
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
            cv2.imshow("contourspic", img)
            cv2.imwrite("Ausgangsbilder/contourspic.png", img)
            #peri = cv2.arcLength(cnt, True)
            #approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)
            #print(approx)
            #print("Area", cv2.contourArea(cnt))
            #print("Length",len(approx))
            #if len(approx)==1:
            #    continue

            #cv2.drawContours(img, [approx], -1, (255, 0, 0), 3)
            #cv2.imshow("approxpic", img)
            #cv2.imwrite("Ausgangsbilder/approxpic.png", img)
            #p1_w=approx[0,0,0]
            #p1_h=approx[0,0,1]
            #p2_w=approx[1,0,0]
            #p2_h=approx[1,0,1]
            #if  (p1_w>10 and p1_w<img.shape[1]-10) and (p1_h>10 and p1_h<img.shape[0]-10):
            #    ergebnis = False
            #    coordinates.insert(0,[p1_w,p1_h])
            #if (p2_w > 10 and p2_w < img.shape[1] - 10) and (p2_h > 10 and p2_h < img.shape[0] - 10):
                #print("schlecht")
            #    ergebnis = False
            #    coordinates.insert(0,[p2_w,p2_h])
            #print("______________")
    #Ausgabe
    #print(coordinates)
    cv2.imshow("img",img)
    return ergebnis,img,coordinates