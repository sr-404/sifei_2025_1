import cv2 as cv
import numpy as np
    

image = cv.imread('/Users/summer/Desktop/T1.jpeg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

kernel = np.ones((1,2),np.uint8)
dilation = cv.dilate(gray,kernel,iterations = 2)
cv.imshow('dilation',dilation)   #对灰度图进行膨胀
kernel2 = np.ones((30,30),np.uint8)
erosion = cv.erode(dilation,kernel2)

cv.imshow('erosion',erosion)





contours, hierarchy = cv.findContours(erosion, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 轮廓      层级                               轮廓检索模式  轮廓逼近方法
 
    # 2、画出轮廓
dst = cv.drawContours(image, contours, -1,                (0, 0, 255), 3)
    #                           轮廓     所有               颜色       线条厚度
 
cv.imshow('dst', dst)
print(len(contours))
cv.waitKey()
cv.destroyAllWindows
