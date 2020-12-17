import cv2
import numpy as np
import  hilfsfunktionen as hf

def empty(a):
    pass

path = "heute/Scan.png"

cv2.namedWindow("TrackBars") #Neues Fenster anlegen und Ziehregler hinzufügen
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",1,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",21,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",39,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",130,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    img = hf.show("input",img,16)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #HSV Bild erstellen
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars") #Ziehreglerpositionen einlesen
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max) #zur Überischt Ziehreglerpostionen ausdrucken
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper) #Bild bei der die Pixel in der Range ziwschen min und max weiß sind und der Rest schwarz
    imgResult = cv2.bitwise_and(img,img,mask=mask) #Maskenbild über Originalbild legen und verunden

    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)