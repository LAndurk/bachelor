import ba7
import cv2

path="Eingangsbilder/12.png"
img = cv2.imread(path)
x = int(img.shape[1] / 4)  # Breite
y = int(img.shape[0] / 4)  # Höhe
img = cv2.resize(img,(x,y))
#img = hf.quarter(img,1)
#img = img[50:img.shape[0]-50,50:img.shape[1]-50]
#print(img.shape)

ergebnis,img,coordinates = ba7.damageDetection(img)
if ergebnis == False:
    print("!!!schlecht!!!")
else:
    print("gut")

cv2.waitKey(0)