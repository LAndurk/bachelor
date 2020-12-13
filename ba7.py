# ToDo: Problem adaptive thresholding bei großen schwarzen Bereichen ohne Leiterbahn
# ToDo: Problem Randbereich

import cv2
import numpy as np


def damageDetection(img):

    ergebnis = True
    coordinates = []

    #Preprocessing
    imgBW = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("imgBW",imgBW)
    blur = cv2.GaussianBlur(imgBW, (25, 25), 0)
    cv2.imshow("blur",blur)

    threshold = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,301,0)
    cv2.imshow("threshold",threshold)
    kernelero = np.ones((3,3),np.uint8)
    kerneldil = np.ones((3,3),np.uint8)
    thresholdEro = cv2.erode(threshold, kernelero, iterations=1)
    cv2.imshow("thresholdEro", thresholdEro)
    thresholdDil = cv2.dilate(thresholdEro, kerneldil, iterations=1)
    cv2.imshow("thresholdDil", thresholdDil)

    contours, hierarchy = cv2.findContours(thresholdDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
    #for i in range(len(contours)):
        if cv2.contourArea(cnt) > 500:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
            #cv2.imshow("contourspic", img)
            #cv2.imwrite("Ausgangsbilder/contourspic.png", img)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)
            if len(approx)==1:
                continue

            cv2.drawContours(img, [approx], -1, (255, 0, 0), 3)
            #cv2.imshow("approxpic", img)
            #cv2.imwrite("Ausgangsbilder/approxpic.png", img)
            p1_w=approx[0,0,0]
            p1_h=approx[0,0,1]
            p2_w=approx[1,0,0]
            p2_h=approx[1,0,1]
            if  (p1_w>10 and p1_w<img.shape[1]-10) and (p1_h>10 and p1_h<img.shape[0]-10):
                ergebnis = False
                coordinates.insert(0,[p1_w,p1_h])
            if (p2_w > 10 and p2_w < img.shape[1] - 10) and (p2_h > 10 and p2_h < img.shape[0] - 10):
                ergebnis = False
                coordinates.insert(0,[p2_w,p2_h])
    #Ausgabe
    cv2.imshow("img",img)
    return ergebnis,img,coordinates