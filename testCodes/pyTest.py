"""
Created on 2020. 7. 25.

@author: Administrator
"""

PPROGRAM_ROOT_PATH = (
    # project path
)

import sys

sys.path.append(PPROGRAM_ROOT_PATH)

import os
from _operator import itemgetter
import json
from math import sqrt

import cv2

from SpaceFinderModules.Detecters import detectionRect
from SpaceFinderModules.ImageConverters import ToEdgeByAccuratey
from SpaceFinderModules.SpaceFinderClasses import Space
import numpy as np


print("test")
print(cv2.__version__)

cap = cv2.VideoCapture(0)

FRAME_WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
FRAME_HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# PROJECT_FILE_PATH = "C:/Users/Administrator/Desktop"
PROJECT_FILE_PATH = os.path.realpath(__file__)

PAKINGLOT = "41"

print(FRAME_WIDTH, " ", FRAME_HEIGHT, " ", sqrt(FRAME_WIDTH**2 + FRAME_WIDTH**2))
print(
    sqrt(FRAME_WIDTH**2 + FRAME_WIDTH**2) / 12,
    " ",
    sqrt(FRAME_WIDTH**2 + FRAME_WIDTH**2) / 2,
)


def sortRects(rects):
    for idx, t in enumerate(rects):
        for j in range(idx + 1, len(rects)):
            if rects[idx][0][0][0] > rects[j][0][0][0]:
                temp = rects[idx]
                rects[idx] = rects[j]
                rects[j] = temp

    return rects


while True:

    ret, frame = cap.read()

    processing = ToEdgeByAccuratey(frame)
    Rects, RectCount = detectionRect(
        processing, filterSize=(50, 400), epsilonDeg=0.08, Type=cv2.RETR_TREE
    )

    for rect in Rects:

        cv2.drawContours(frame, [rect], 0, (0, 255, 0), 3)

    cv2.imshow("frame", frame)
    cv2.imshow("test", processing)

    k = cv2.waitKey(100) & 0xFF

    if k == ord("p") or k == ord("P"):
        print(str(FRAME_WIDTH) + " " + str(FRAME_HEIGHT))

    if k == ord("c") or k == ord("C"):

        Rects = sortRects(Rects)
        print(Rects, type(Rects))

        spaces = []
        for idx, rect in enumerate(Rects):
            space = Space(idNum=idx, realLocations=rect.reshape(-1, 2))
            spaces.append(space)

        print("detected space count : ", str(len(spaces)))
        print("complete!!")

    if k == ord("d") or k == ord("D"):
        print("drawObject")

        data = {}

        data["parkinglot"] = PAKINGLOT
        data["FrameWidth"] = FRAME_WIDTH
        data["FrameHeight"] = FRAME_HEIGHT

        data["RectWidth"] = 50
        data["RectHeight"] = 80

        data["DrawRects"] = []

        MAX_FLOOR = 6
        floor_ONof = [False for i in range(0, MAX_FLOOR)]
        mappingFloor = [0 for i in range(0, MAX_FLOOR)]
        useFloor = 0
        for space in spaces:
            rect_data = {}

            firstLocation = space.getRealLocations()[0].tolist()
            data["RectHeight"] = firstLocation

            pointY = np.int(space.getRealLocations()[0][1])

            print(type(pointY), " ", pointY)

            rect_data["id"] = space.getIdNum()
            rect_data["isEmpty"] = False
            for f in range(0, MAX_FLOOR):
                if (
                    pointY > ((FRAME_HEIGHT / MAX_FLOOR) * f)
                    and ((FRAME_HEIGHT / MAX_FLOOR + 1) * (f + 1)) >= pointY
                ):
                    if floor_ONof[f] == True:
                        rect_data["floor"] = mappingFloor[f]
                    else:
                        floor_ONof[f] = True
                        useFloor += 1
                        mappingFloor[f] = useFloor
                        rect_data["floor"] = mappingFloor[f]

            data["DrawRects"].append(rect_data)

        with open(
            PROJECT_FILE_PATH + "space_jsons/drawSpaceData" + PAKINGLOT + ".json", "w"
        ) as outFile:
            json.dump(data, outFile, indent=4)

    if k == ord("m") or k == ord("M"):
        print("createObject", str(len(spaces)))
        data = {}

        data["parkinglot"] = PAKINGLOT
        data["spaces"] = []

        for space in spaces:

            space_data = {}

            locationData = space.getRealLocations().tolist()

            print(locationData)

            space_data["id"] = space.getIdNum()
            space_data["realSpace"] = locationData

            data["spaces"].append(space_data)

        with open(
            PROJECT_FILE_PATH + "space_jsons/realSpaceData" + PAKINGLOT + ".json", "w"
        ) as outFile:
            json.dump(data, outFile, indent=4)

        print("complete!!")

    #    if k == ord('n') or k == ord('N') :
    #        conn = ora.connect("")
    #        dbCur = conn.cursor()
    #        print("out")
    #        sql = 'insert into parkingspace(gp_id, spaceid, isUse, locate) values(:1, :2, :3, :4)'
    #
    #        for space in spaces :
    #            if(space.getIsEmpty()):
    #                empty = 'f'
    #            else :
    #                empty = 't'
    #
    #            data = (PAKINGLOT, space.getIdNum(), empty, str(space.getRealLocations()))
    #            dbCur.execute(sql, data)
    #            conn.commit()
    #            print("in")
    #
    #        dbCur.close()
    #        conn.close()

    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
