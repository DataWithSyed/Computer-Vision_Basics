import numpy as np
#os.environ['OPENCV_IO_MAX_IMAGE_PIXELS']=str(2**64)
import cv2

img = cv2.imread('C:/Users/Taha/Pictures/Computer Vision/001.jpg', cv2.IMREAD_COLOR)



cv2.rectangle(img, (20,25), (400,400), (0,255,0), 5)





cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
