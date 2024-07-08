'''
Created on 2020. 7. 31.

@author: Administrator
'''
'''
Created on 2020. 7. 27.

@author: Administrator
'''


import cv2

from SpaceFinderModules.ImageConverters import ToBinery, ToEdgeByAccuratey
import pytesseract as pts
import re

pts.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

cap = cv2.VideoCapture(2)

PAKINGLOT = '0'

redoText = None
insertText = None
textType =['n', 'n', 'n', 'c', 'n', 'n', 'n', 'n']
#conn = ora.connect("")
#dbCur = conn.cursor()

#sql = 'insert into parkingcar(gp_id, carid, stime) values(:1,:2,sysdate)'

while(True) :
    
    ret, frame = cap.read()
    
    acc = ToEdgeByAccuratey(frame, rati=5, deg=5)
    
    testText = pts.image_to_string(frame, lang='kor')
     
    resText=''
    
    print("tess",testText)
    
    for c in testText:
        if c.isalnum():
            resText+=c
    
    passText = False
    if len(resText) ==8 or len(resText) ==7:
        resText = resText.zfill(8)
        for i in range(0,8):
            passText = True
            
            if textType[i] == 'c' and resText[i].isdigit():
                passText = False
            
            if textType[i] == 'n' and resText[i].isalpha() :
                passText = False
    
    if passText:
        print("out", resText, " ",redoText, " ", insertText)
        if redoText == resText and insertText != resText :
            #dbCur.execute(sql, (PAKINGLOT, resText))
            #conn.commit()
            insertText = resText
            print("in", resText, " ",redoText, " ", insertText)
             
        redoText = resText
    
    cv2.imshow('frame_test2', acc)
    
    k= cv2.waitKey(100) & 0xff
    
    if k == 27 :
        break

#dbCur.close()
#conn.close()
cap.release()
cv2.destroyAllWindows()