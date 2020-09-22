'''
Created on 2020. 7. 25.

@author: Administrator
'''

import cv2
import numpy as np

class SpaceClass:
    
    SPACE_COUNT=0
    ID_COIUNT=0
    FULL_CAM_WIDTH=None
    FULL_CAM_HEIGHT=None

    def __init__(self, realLocations, idNum=None, isEmpty=False):
            
        if idNum != None:
            self._idNum = idNum
        else :
            self._idNum = SpaceClass.ID_COIUNT
                
        SpaceClass.ID_COIUNT+=1
        
        self._realLocations =realLocations
        self._isEmpty = isEmpty
        
    def __del__(self):
        SpaceClass.SPACE_COUNT-=1
    
    def setIsEmpty(self, isEmpty):
        self._isEmpty = isEmpty
        
    def getIdNum(self):
        return self._idNum
    
    def getRealLocations(self):
        return self._realLocations
    
    def getboundRect(self):
        boundRect = np.array(self._realLocations)
        x, y, w, h= cv2.boundingRect(boundRect)
        return x, y, w, h
    
    def getIsEmpty(self):
        return self._isEmpty