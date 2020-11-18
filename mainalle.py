import ba7
import cv2

#imgArray = []
for i in range(1,23):
    path = "Bilder/"
    path = ''.join([path,str(i),".png"])
    print(path)
    img = cv2.imread(path)
    x = int(img.shape[1] / 4)  # Breite
    y = int(img.shape[0] / 4)  # Höhe
    img = cv2.resize(img, (x, y))

    ergebnis,img = ba7.damageDetection(img)
    ausgabe = ''.join([str(i),str(ergebnis)])
    cv2.imshow(ausgabe,img)
    #imgArray.append(img)
    if ergebnis == False:
        print("!!!schlecht!!!")
    else:
        print("gut")

#imgStack = hf.stackImages(0.6,imgArray)
#cv2.imshow("imgStack",imgStack)

cv2.waitKey(0)