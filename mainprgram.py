import ba7
import cv2
import math
import numpy as np


def distancefunct(p1,p2):
    #print(p1[0])
    #print(p1[1])
    #print((p1[0]-p2[0]))
    #print((p1[1]-p2[1])**2)
    distance = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return distance

path="Bilder/1.png"
img = cv2.imread(path)
x = int(img.shape[1] / 4)  # Breite
y = int(img.shape[0] / 4)  # Höhe
img = cv2.resize(img,(x,y))
img_original = img.copy()
""""
img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
"""
#mask = [x][y]
#img = hf.quarter(img,1)
#img = img[50:img.shape[0]-50,50:img.shape[1]-50]
#print(img_original.shape)

ergebnis,img,coordinates = ba7.damageDetection(img)
cv2.destroyAllWindows()
#print("Ergebnis",ergebnis)
#print(len(coordinates))

img_mistake = np.ones((y,x,3),np.uint8)
img_mistake = img_mistake * 255
img_result = np.zeros((y,x,3),np.uint8)
#print(img_mistake.shape)
#print(img_result.shape)
for i in range(len(coordinates)):
    cv2.circle(img_mistake,(coordinates[i][0],coordinates[i][1]),30,(200,255,200),-1)
cv2.bitwise_and(img_original,img_mistake,img_result)

""""
#distance = distance(coordinates[0],coordinates[1])
#print(distance)
delete = False
laenge = len(coordinates)
for p in range(laenge):
    print(delete)
    print(coordinates)

    p = p - (laenge - len(coordinates))
    for i in range(len(coordinates)):
        print(p)
        print(i)
        print(coordinates[p])
        print(coordinates[i])

        distanceval=distancefunct(coordinates[p], coordinates[i])
        print("___")
        if distanceval == 0:
            continue
        if distanceval < 60:
            delete = True
    if delete:
        del coordinates[p]

        delete = False
        print(coordinates)


for i in range(len(coordinates)):
    #print(i)
    #print(coordinates[i][0])
    cv2.circle(result,(coordinates[i][0],coordinates[i][1]),30,(255,0,0),-1)

cv2.imshow("result",result)
"""
#cv2.imshow("img_original",img_original)
#cv2.imshow("img_mistake",img_mistake)
cv2.imshow("img_result",img_result)

""""
img_white = np.ones((y,x,3),np.uint8)
img_white = img_white * 255
cv2.imshow("img_white",img_white)
"""
cv2.waitKey(0)