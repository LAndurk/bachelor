import ba7
import cv2
import damageDetection1 as dd1
import damageDetection as dd
import hilfsfunktionen as hf
import numpy as np

substrate = "heute"
picture = "1"

path = ''.join([substrate, "/", picture, ".png"])
img = cv2.imread(path)

x = int(img.shape[1] / 2)  # Breite
y = int(img.shape[0] / 2)  # Höhe
#img = cv2.resize(img,(x,y))
#img = hf.quarter(img,1)
#img = img[50:img.shape[0]-50,50:img.shape[1]-50]

ergebnis,img,coordinates = dd.damageDetection(img,"sandwich2")

hf.klein("img",img)

if ergebnis == False:
    print("!!!schlecht!!!")
else:
    print("gut")

cv2.waitKey(0)