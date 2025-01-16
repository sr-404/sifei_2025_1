import cv2
import numpy as np
image = cv2.imread('/Users/summer/Desktop/T1.jpeg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.waitKey()
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(gray,kernel,iterations = 2)
cv2.imshow('dilation',dilation)   #对灰度图进行膨胀
cv2.waitKey()
template_1 = dilation[26:78,0:46]     #样本为左上角第一颗星星  竖行26到78   横列0到46
match = cv2.matchTemplate(dilation,template_1,cv2.TM_CCOEFF_NORMED)    #用该样本进行匹配
locations = np.where(match >= 0.9)
w,h = template_1.shape[0:2]
for p in zip(*locations[::-1]):
    x1, y1 = p[0],p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1,y1), (x2, y2),(0,255,0),2)


cv2.imshow('image',image)
cv2.waitKey()
print(num)