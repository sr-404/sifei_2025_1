import cv2
import numpy as np
img = cv2.imread('/Users/summer/Desktop/T2.png')  #读进来是BGR格式
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #变成HSV格式
ls = np.ones((15,15),dtype=int)


xx=0
yy=0
for x in range(18,560,37):
    print("x",x)
    for y in range(18,560,37):
        print("y",y)
        H = hsv[y,x]
       # print(H)
        color=0
        if H.any == ("[0 0 0]"):
            color = 1       #黑
        elif H.any == ("[  0   0 255]"):
            color = 0     #白
        elif H.any == ("[  0 255 255]"):
            color = 2     #红
        elif H.any == ("[ 99 255 232]"):
            color = 3     #蓝
        ls[xx,yy]=1
        yy+=1
    xx+=1   

#print(ls)


