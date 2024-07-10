"""
Created on 2020. 7. 25.

@author: Whitepaper
"""

import cv2
import numpy as np
from cv2 import cvtColor, GaussianBlur, threshold, Canny, dilate


def ToHSV(img):
    hsv = cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv


def ToGray(img):
    gray = cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def ToGau(img, rati=3):
    gau = GaussianBlur(img, (rati, rati), 3)
    return gau


def ToCannyEdge(img, mi=50, ma=100):
    edge = Canny(img, mi, ma)
    return edge


def ToDilate(img, deg=5, itera=1):
    kernel = np.ones((deg, deg), np.uint8)
    dilate = threshold(img, kernel, iterations=itera)
    return dilate


def ToBinery(img):
    ret, thr = threshold(img, 127, 255, 0)
    return thr


def ToEdgeByAccuratey(img, rati=3, canny=(50, 100), deg=5):
    grayImg = cvtColor(img, cv2.COLOR_BGR2GRAY)
    gauImg = GaussianBlur(grayImg, (rati, rati), 3)
    cannyImg = Canny(gauImg, canny[0], canny[1])

    kernel = np.ones((deg, deg), np.uint8)
    #     openingImg = cv2.morphologyEx(cannyImg, cv2.MORPH_OPEN, kernel)
    dilateImg = dilate(cannyImg, kernel, iterations=1)

    ret, thr = threshold(dilateImg, 127, 255, 0)

    return thr


def ToEdgeByObjectly(img, rati=3, canny=(50, 100), deg=5):
    grayImg = cvtColor(img, cv2.COLOR_BGR2GRAY)
    gauImg = GaussianBlur(grayImg, (rati, rati), 3)
    cannyImg = Canny(gauImg, canny[0], canny[1])

    kernel = np.ones((deg, deg), np.uint8)

    #     dilateImg = dilate(cannyImg, kernel, iterations =1)
    openingImg = cv2.morphologyEx(cannyImg, cv2.MORPH_OPEN, kernel)
    ret, thr = threshold(openingImg, 127, 255, 0)

    return thr
