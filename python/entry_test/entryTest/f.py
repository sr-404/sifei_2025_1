import cv2 as cv
import numpy as np
# 提取轮廓

    

image = cv.imread('/Users/summer/Desktop/T1.jpeg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(gray,kernel,iterations = 2)
cv.imshow('dilation',dilation)   #对灰度图进行膨胀
# 1、根据二值图找到轮廓
if 1==1:

    contours, hierarchy = cv.findContours(dilation, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 轮廓      层级                               轮廓检索模式(推荐此)  轮廓逼近方法
 
    # 2、画出轮廓
    dst = cv.drawContours(image, contours, -1,                (0, 0, 255), 3)
    #                           轮廓     第几个(默认-1：所有)   颜色       线条厚度
 
    cv.imshow('dst', dst)
    print(len(contours))
cv.waitKey()
