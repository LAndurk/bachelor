import cv2
import numpy as np


def damageDetection(img):
    result = True
    coordinates = []

    imgBW = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgThresh = cv2.adaptiveThreshold(imgBW, 255,
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 301, 0)

    kernel = np.ones((7, 7), np.uint8)
    imgEro = cv2.erode(imgThresh, kernel, iterations=1)
    imgDil = cv2.dilate(imgEro, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:

            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)

            if len(approx) == 1:
                continue

            p1_w = approx[0, 0, 0]
            p1_h = approx[0, 0, 1]
            p2_w = approx[1, 0, 0]
            p2_h = approx[1, 0, 1]

            if (p1_w > 10 and p1_w < img.shape[1] - 10) and \
                    (p1_h > 10 and p1_h < img.shape[0] - 10):
                result = False
                coordinates.insert(0, [p1_w, p1_h])
            if (p2_w > 10 and p2_w < img.shape[1] - 10) and \
                    (p2_h > 10 and p2_h < img.shape[0] - 10):
                result = False
                coordinates.insert(0, [p2_w, p2_h])

    cv2.imshow("img", img)

    return result, img, coordinates
