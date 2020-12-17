import ba7
import cv2
import damageDetection1 as dd1
import damageDetection as dd
import hilfsfunktionen as hf
import numpy as np

substrate = "lichtmikroskop"
picture = "dick gut"

path = ''.join([substrate, "/", picture, ".png"])
img = cv2.imread(path)

#img = hf.show("eingabe", img,2)
#img = hf.quarter(img,1)
#img = img[50:img.shape[0]-50,50:img.shape[1]-50]

ergebnis,img,coordinates = dd.damageDetection(img,"sandwich")

hf.show("maineinzel", img,8)

if ergebnis == False:
    print("!!!schlecht!!!")
else:
    print("gut")

cv2.waitKey(0)