import cv2
import numpy as np

img = cv2.imread('/Users/summer/Desktop/T2.png')
hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_color = np.array()
