import cv2
import numpy as np
cap = cv2.VideoCapture(0)

#FourCC is a 4-byte code used to specify the video codec

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('Video.avi', fourcc,20,(640,480))

while True:
    ret, frame = cap.read()
    flip = cv2. flip(frame, 0)  #By x-axis 0, By Y-axis 1, -1 both axis
    cv2.imshow('Camera feed', frame)
    cv2.imshow('Flipped feed',flip)
    out.write(flip)
    if cv2.waitKey(1) == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
