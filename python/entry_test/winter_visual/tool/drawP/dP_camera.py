import cv2 as cv
import numpy as np

# 初始化摄像头
cap = cv.VideoCapture(0)

# 定义蓝色的 HSV 阈值
#lower = np.array([100, 50, 90])          
#upper = np.array([140, 200, 250])

lower = np.array([0, 100, 100])  # 亮红色到深红色
upper= np.array([10, 255, 255])

while True:
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 将 BGR 图像转换为 HSV 图像
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 创建蓝色的掩码
    mask = cv.inRange(hsv, lower, upper)

    # 对原图像和掩码进行位运算
    res = cv.bitwise_and(frame, frame, mask=mask)

    # 应用 Canny 边缘检测
    edges = cv.Canny(mask, 100, 200)

    # 将边缘图与原图合并，以便在原图上显示边缘
    edges_bgr = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    result_with_edges = cv.addWeighted(frame, 1, edges_bgr, 1, 0)

    # 查找轮廓
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # 绘制每个轮廓的重心
    for contour in contours:
        # 计算轮廓的矩
        M = cv.moments(contour)
        if M["m00"] != 0:
            # 计算重心
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # 在原图上绘制重心
            cv.circle(result_with_edges, (cX, cY), 5, (255, 255, 255), -1)

    # 显示结果
    cv.imshow('Original', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', res)
    cv.imshow('Edges', edges)
    cv.imshow('Result with Edges and Centers', result_with_edges)

    # 按 'q' 键退出
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv.destroyAllWindows()