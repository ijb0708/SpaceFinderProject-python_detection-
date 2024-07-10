"""
Created on 2020. 7. 29.

@author: Administrator
"""

PPROGRAM_ROOT_PATH = ()

import json
import cv2

import sys

sys.path.append(PPROGRAM_ROOT_PATH)

from SpaceFinderModules.Caculaters import getRectSize
from SpaceFinderModules.ImageConverters import ToEdgeByAccuratey, ToEdgeByObjectly
from SpaceFinderModules.SpaceFinderClasses import Space

# import cx_Oracle as ora
import numpy as np

PROJECT_FILE_PATH = PPROGRAM_ROOT_PATH
PAKINGLOT = "41"


# conn = ora.connect("")
# dbCur = conn.cursor()

# sql = 'update parkingspace set ISuse = :1 where GP_ID = :2 and SPACEID = :3'

json_data = None

CAR_VAL = 4000

spaces = []


def maskRoi(gray_img, approx, firstLoc):
    approx = np.array(
        [
            [approx[0] - firstLoc],
            [approx[1] - firstLoc],
            [approx[2] - firstLoc],
            [approx[3] - firstLoc],
        ]
    )
    mask = np.zeros_like(gray_img)
    mask = cv2.fillPoly(mask, [approx], 255)
    roi_image = cv2.bitwise_and(gray_img, mask)
    return roi_image


def readData():

    with open(
        PROJECT_FILE_PATH + "space_jsons/realSpaceData" + PAKINGLOT + ".json", "r"
    ) as inFile:
        json_data = json.load(inFile)

        for json_space in json_data["spaces"]:
            print(json_space["realSpace"], " type : ", type(json_space["realSpace"]))
            space = Space(idNum=json_space["id"], realLocations=json_space["realSpace"])
            space.setIsEmpty(False)
            spaces.append(space)


cap = cv2.VideoCapture(0)

# readData()

while True:

    ret, frame = cap.read()

    process_image = ToEdgeByAccuratey(frame, rati=3, deg=4)

    roi_status = []

    for space in spaces:

        f_rect = np.array(space.getRealLocations())
        #         print(space.getRealLocations(), type(space.getRealLocations()))

        if space.getIsEmpty():
            cv2.drawContours(frame, [f_rect], 0, (0, 0, 255), 3)
        else:
            cv2.drawContours(frame, [f_rect], 0, (0, 255, 0), 3)
        b_rect = space.getboundRect()
        cv2.rectangle(
            frame,
            (b_rect[0], b_rect[1]),
            (b_rect[0] + b_rect[2], b_rect[1] + b_rect[3]),
            (255, 0, 0),
            3,
        )
        roi = process_image[
            b_rect[1] : b_rect[1] + b_rect[3], b_rect[0] : b_rect[0] + b_rect[2]
        ]
        m_roi = maskRoi(gray_img=roi, approx=f_rect, firstLoc=(b_rect[0], b_rect[1]))

        sizes = getRectSize(b_rect)

        #         print( ( (sizes[0] + sizes[1] + sizes[2] + sizes[3]) ) * 1 )
        #         roi_value = np.sum(roi)/255 - (b_rect[2]+b_rect[3])*6
        #         if (roi_value <= 0) :
        #             roi_value=0

        #         roi_status.append((np.sum(m_roi)/255, np.mean(m_roi), np.std(m_roi)))
        roi_status.append(np.mean(m_roi))

        roi_value = np.mean(m_roi)

        if roi_value >= 50:
            isEmptyNow = True
        else:
            isEmptyNow = False

        if isEmptyNow != space.getIsEmpty():
            if isEmptyNow:
                sql_value = ("f", PAKINGLOT, space.getIdNum())
            else:
                sql_value = ("t", PAKINGLOT, space.getIdNum())

            #            dbCur.execute(sql, sql_value)
            #            conn.commit()
            print("test")

        space.setIsEmpty(isEmptyNow)

    print(roi_status)
    cv2.imshow("test", frame)
    cv2.imshow("ptest", process_image)

    k = cv2.waitKey(100) & 0xFF

    if k == 27:
        break


# dbCur.close()
# conn.close()

cap.release()
cv2.destroyAllWindows()
