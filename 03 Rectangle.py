import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
  #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imread('frame')
  #  cv2.imshow('gray', gray)
    cv2.rectangle(cap, (15,25), (400,350), (0,255,0), 5)

    cv2.imshow(cap)

    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()
