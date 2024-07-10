"""
Created on 2020. 7. 25.

@author: Administrator
"""

import numpy as np


def accLength(loc1, loc2):

    loc = loc1 - loc2

    squLoc = np.square(loc)
    sumLoc = np.sum(squLoc)
    result = np.floor(np.sqrt(sumLoc))

    return result


def accAngle(center, loc1, loc2):

    if str(type(center)) == "<class 'numpy.ndarray'>":
        center = center.ravel()
        loc1 = loc1.ravel()
        loc2 = loc2.ravel()

    top = (
        loc1[1] * (center[0] - loc2[0])
        + center[1] * (loc2[0] - loc1[0])
        + loc2[1] * (loc1[0] - center[0])
    )
    bot = ((loc1[0] - center[0]) * (center[0] - loc2[0])) + (
        (loc1[1] - center[1]) * (center[1] - loc2[1])
    )

    rad = np.arctan2(top, bot)
    rad = np.abs(rad)
    angle = np.degrees(rad)

    return angle, rad


def checkRectSize(rect, minSize, maxSize):

    r = accLength(rect[0], rect[2])
    l = accLength(rect[1], rect[3])

    if r > minSize and r < maxSize and l > minSize and l < maxSize:
        return True
    else:
        return False


def checkRectAngle(rect, minAngle, maxAngle):

    ul = accAngle(rect[0], rect[1], rect[3])
    ur = accAngle(rect[1], rect[0], rect[2])
    dr = accAngle(rect[2], rect[1], rect[3])
    dl = accAngle(rect[3], rect[0], rect[2])

    angle = ul[0] + ur[0] + dr[0] + dl[0]

    if angle >= minAngle and angle <= maxAngle:
        return True
    else:
        return False


def getRectSize(rect):

    up = accLength(rect[0], rect[1])
    down = accLength(rect[3], rect[2])
    left = accLength(rect[0], rect[3])
    right = accLength(rect[1], rect[2])
    leftDiag = accLength(rect[0], rect[2])
    rightDiat = accLength(rect[1], rect[3])

    return up, down, left, right, leftDiag, rightDiat
