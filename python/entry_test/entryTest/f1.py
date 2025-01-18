import cv2 as cv
import numpy as np
# 提取轮廓

    

image = cv.imread('/Users/summer/Desktop/T1.jpeg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
k = np.ones((2,2),np.uint8)
r =cv.morphologyEx(gray,cv.MORPH_CLOSE,k,iterations=3)
cv.imshow("r",r)
cv.waitKey()