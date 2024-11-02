import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow("Inter", frame)

    if cv2.waitKey(40) == 27:
        break


cv2.destroyAllWindows()
cap.release()

