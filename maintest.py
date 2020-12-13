import cv2
import ba7
import damageDetection1 as dd1
import damageDetection as dd2
import hilfsfunktionen as hf
""""
label = [False, False, False, False, False, False, False, False, False, False,
         False, False, True, True, False, False, False, True, True, True,
         False, True, False, True, False, False, False, True, False]
"""
# linksoben(2), rechtsoben(1), rechtsunten(4)
# streng
label = [[False, False, False],
         [False, False, False], #2
         [True, True, False],
         [False, False, True],  # ~4-2?
         [False, True, True],
         [False, False, False], #6
         [False, False, False],
         [True, True, False], #8
         [True, True, False],
         [True, False, False], #10
         [True, True, True],
         [False, True, True], #12
         [True,True,True],
         [True,True,True], #14
         [True,True,False],
         [True,True,False], #16
         [False,False,True]]

all = len(label) * 3
right = 0
falsenegative = 0
"""" #Originalbild, nicht geviertelt
for i in range(1,30):
    path = "Bilder/"
    path = ''.join([path,str(i),".png"])
    img = cv2.imread(path)
    x = int(img.shape[1] / 4)  # Breite
    y = int(img.shape[0] / 4)  # Höhe
    img = cv2.resize(img, (x, y))

    ergebnis,img,coordinates = ba7.damageDetection(img)

    if ergebnis == label[i-1]:
        counter = counter+1
    ausgabe = ''.join([str(i), str(label[i-1]), str(ergebnis)])
    cv2.imshow(ausgabe, img)
"""
for i in range(1, len(label) + 1):
    path = "Eingangsbilder/"
    path = ''.join([path, str(i), ".png"])
    if i == 2:
        all = all - 3
        continue

    for quadrant in [2, 1, 4]:
        eintrag_labelquadrant = None
        if quadrant == 2:
            eintrag_labelquadrant = 0
        elif quadrant == 1:
            eintrag_labelquadrant = 1
        else:
            eintrag_labelquadrant = 2

        img = cv2.imread(path)
        x = int(img.shape[1] / 4)  # Breite
        y = int(img.shape[0] / 4)  # Höhe
        img = cv2.resize(img, (x, y))
        img_quarter = hf.quarter(img, quadrant)

        ergebnis, img, coordinates = dd2.damageDetection(img_quarter,"dunkel")

        if ergebnis == label[i - 1][eintrag_labelquadrant]:
            right = right + 1
        else:
            ausgabe = ''.join([str(i), "-", str(quadrant),
                               str(label[i - 1][eintrag_labelquadrant]),
                               str(ergebnis)])
            cv2.imshow(ausgabe, img)
            if label[i - 1][eintrag_labelquadrant]:
                falsenegative = falsenegative + 1
            # else:
            #    falschgut = falschgut+1


"""" #ohne zweiter for-Schleife, überarbeitet
    img2 = hf.quarter(img, 2)
    img1 = hf.quarter(img, 1)
    img4 = hf.quarter(img, 4)

    ergebnis2,img2,coordinates2 = ba7.damageDetection(img2)
    #print(label[i-1][2])
    if ergebnis2 == labelquadrant[i-1][0]:
        richtig = richtig + 1
    elif labelquadrant[i-1][0] == True:
            falschschlecht = falschschlecht+1
    ausgabe = ''.join([str(i),"-2", str(labelquadrant[i - 1][0]), str(ergebnis2)])
    cv2.imshow(ausgabe, img2)
    ergebnis1, img1, coordinates1 = ba7.damageDetection(img1)
    if ergebnis1 == labelquadrant[i-1][1]:
        richtig = richtig + 1
    elif labelquadrant[i - 1][1] == True:
        falschschlecht = falschschlecht + 1
    ausgabe = ''.join([str(i),"-1", str(labelquadrant[i - 1][1]), str(ergebnis1)])
    cv2.imshow(ausgabe, img1)
    ergebnis4,img4,coordinates4 = ba7.damageDetection(img4)
    if ergebnis4 == labelquadrant[i-1][2]:
        richtig = richtig + 1
    elif labelquadrant[i-1][2] == True:
        falschschlecht = falschschlecht+1
    ausgabe = ''.join([str(i),"-4", str(labelquadrant[i - 1][2]), str(ergebnis4)])
    cv2.imshow(ausgabe, img4)
"""
""""
cv2.destroyWindow("threshold")
cv2.destroyWindow("thresholdEro")
cv2.destroyWindow("thresholdDil")
cv2.destroyWindow("img")
"""

print("all:", all)
print("right:", right)
print("test result:", int(100 * right / all), "%")
print("________")
print("falsepositive:", all - right - falsenegative)
print("falsenegative (Pseudofehler):", falsenegative)

cv2.waitKey(0)
