import cv2 as cv
import numpy as np

# 初始化摄像头
cap = cv.VideoCapture(0)

# 定义蓝色的 HSV 阈值
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

    # 应用 Canny 边缘检测
    edges = cv.Canny(mask, 100, 200)

    # 将边缘图与原图合并，以便在原图上显示边缘
    # 使用 cv.addWeighted 将边缘图（白色边缘）叠加到原图上
    # 注意：边缘图需要转换为3通道图像才能与原图合并
    edges_bgr = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    result_with_edges = cv.addWeighted(frame, 1, edges_bgr, 1, 0)

    # 显示结果
    cv.imshow('Original', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', res)
    cv.imshow('Edges', edges)
    cv.imshow('Result with Edges', result_with_edges)

    # 按 'q' 键退出
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv.destroyAllWindows()