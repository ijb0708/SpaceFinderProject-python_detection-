"""
Created on 2020. 7. 25.

@author: Administrator
"""

import cv2

from SpaceFinderModules.Caculaters import checkRectSize, checkRectAngle


def detectionRect(img, epsilonDeg=0.1, filterSize=(100, 1000), Type=cv2.RETR_EXTERNAL):
    Rects = []

    contours, hierarchy = cv2.findContours(img, Type, cv2.CHAIN_APPROX_TC89_KCOS)

    RectCount = 0
    for idx, cnt in enumerate(contours):

        isTree = True
        epsilon = epsilonDeg * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        size = len(approx)

        if hierarchy[0][idx][3] == -1:
            isTree = False

        if size == 4 and isTree:
            if checkRectSize(approx, filterSize[0], filterSize[1]) and checkRectAngle(
                approx, 350, 370
            ):
                Rects.append(approx)
                RectCount += 1

    return Rects, RectCount
