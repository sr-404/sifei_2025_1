import cv2
import numpy as np 
img = cv2.imread('/Users/summer/Desktop/T1.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
k = np.ones((4,4),np.uint8)
r=cv2.morphologyEx(img,cv2.MORPH_CLOSE,k,iterations=2)
cv2.imshow("1",r)
cv2.waitKey()
cv2.destroyAllWindows()
