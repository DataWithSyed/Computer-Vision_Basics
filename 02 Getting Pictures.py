import cv2
import numpy as np

cap = cv2.imread('new.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (300,300), (255,255,255), 15)
cv2.imshow('cap', img)
cv2.waitKey(0)
cv2.destroyAllWindows

      
