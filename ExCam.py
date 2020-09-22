'''
Created on 2020. 7. 25.

@author: Administrator
'''
from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows


cap = VideoCapture(0)

while(True) :
    
    ret, frame = cap.read()
    
    imshow('frame', frame)
    
    k= waitKey(100) & 0xff
    
    if k == 27 :
        break

cap.release()
destroyAllWindows()