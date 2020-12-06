import cv2
import numpy as np
import hilfsfunktionen as hf

# gauss, threshold, opening, closing, cut, Konturengröße
parameters = [[1,   501,    15, 1,  50,     2000], #dunkel
              [25,  1501,   32, 32, 100,    7000], #sandwich
              [1,   251,    31, 1,  200,    7000]] #glas

substrates = {"dunkel":0,"sandwich":1,"glas":2}

def damageDetection(img, substrate):
    index = substrates[substrate]

    result = True
    coordinates = []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Blur
    blur = cv2.GaussianBlur(gray, (parameters[index][0],parameters[index][0]), 0)
#Threshold
    if substrate == "glas":
        thresh_type = cv2.THRESH_BINARY_INV
    else:
        thresh_type = cv2.THRESH_BINARY
    threshold = cv2.adaptiveThreshold(blur, 255,
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      thresh_type, parameters[index][1], 0)
#Opening
    kernelo = np.ones((parameters[index][2],parameters[index][2]), np.uint8)
    opening = cv2.morphologyEx(threshold,cv2.MORPH_OPEN,kernelo)
#Closing
    kernelc = np.ones((parameters[index][3],parameters[index][3]), np.uint8)
    closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernelc)
# Schwärzen
    img[:, 0:parameters[index][4]] = 0
    img[:, img.shape[1] - parameters[index][4]:img.shape[1]] = 0
    img[0:parameters[index][4],:] = 0
    img[img.shape[0] - parameters[index][4]:img.shape[0],:] = 0


    contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        if cv2.contourArea(cnt) > parameters[index][5]:

            cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)

            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.2*peri, True)

            if len(approx) == 1:
                continue
            cv2.drawContours(img, [approx], -1, (255, 0, 0), 3)
            p1_x = approx[0, 0, 0]
            p1_y = approx[0, 0, 1]
            p2_x = approx[1, 0, 0]
            p2_y = approx[1, 0, 1]

            if (p1_x > parameters[index][4] and p1_x < img.shape[1] - parameters[index][4]) and \
                    (p1_y > parameters[index][4] and p1_y < img.shape[0] - parameters[index][4]):
                result = False
                coordinates.insert(0, [p1_x, p1_y])
            if (p2_x > parameters[index][4] and p2_x < img.shape[1] - parameters[index][4]) and \
                    (p2_y > parameters[index][4] and p2_y < img.shape[0] - parameters[index][4]):
                result = False
                coordinates.insert(0, [p2_x, p2_y])

    numpy_horizontal_concat = np.concatenate((gray, blur, threshold), axis=1)
    numpy_horizontal_concat2 = np.concatenate((opening, closing, np.zeros((img.shape[0],img.shape[1]), np.uint8)), axis=1)
    numpy_vertical_concat = np.concatenate((numpy_horizontal_concat,numpy_horizontal_concat2), axis=0)
    hf.klein2("kombi", numpy_vertical_concat)

    return result, img, coordinates