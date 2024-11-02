# for opening a video from your computer
import numpy as np
import cv2


cap = cv2.VideoCapture('Wildli)


while True:
    ret, frame = cap.read()

    cv2.imshow('output', frame)
    if(cv2.waitKey(0) & OxFF == ord('q')):
        break


cap.release()
cv2.destroyAllWindows()
