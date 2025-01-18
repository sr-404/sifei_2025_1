import cv2 as cv
import numpy as np


    

image = cv.imread('/Users/summer/Desktop/WechatIMG29844.jpg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) 
cv.imshow('gray',gray)
r,binary = cv.threshold(gray,120,25,cv.THRESH_BINARY)
cv.imshow("b",binary)
cv.waitKey()


# 1、根据二值图找到轮廓


contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# 轮廓      层级                               轮廓检索模式(推荐此)  轮廓逼近方法
 
# 2、画出轮廓
dst = cv.drawContours(image, contours, -1,                (0, 0, 255), 3)
    #                           轮廓     第几个(默认-1：所有)   颜色       线条厚度
 
cv.imshow('dst', dst)
print(len(contours))
cv.waitKey()
cv.destroyAllWindows
