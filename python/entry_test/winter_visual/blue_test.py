import cv2 as cv
import numpy as np

# 初始化摄像头
cap = cv.VideoCapture(0)

# 定义蓝色的 HSV 阈值
# 蓝色的 HSV 范围
lower_blue = np.array([100, 50, 90])
upper_blue = np.array([140, 200, 255])

while True:
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 将 BGR 图像转换为 HSV 图像
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 创建蓝色的掩码
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # 对原图像和掩码进行位运算
    res = cv.bitwise_and(frame, frame, mask=mask)

    # 显示结果
    cv.imshow('Original', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', res)

    # 按 'q' 键退出
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv.destroyAllWindows()