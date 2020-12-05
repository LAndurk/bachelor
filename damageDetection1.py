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

            if (p1_x > 10 and p1_x < img.shape[1] - 10) and \
                    (p1_y > 10 and p1_y < img.shape[0] - 10):
                result = False
                coordinates.insert(0, [p1_x, p1_y])
            if (p2_x > 10 and p2_x < img.shape[1] - 10) and \
                    (p2_y > 10 and p2_y < img.shape[0] - 10):
                result = False
                coordinates.insert(0, [p2_x, p2_y])

    return result, img, coordinates
