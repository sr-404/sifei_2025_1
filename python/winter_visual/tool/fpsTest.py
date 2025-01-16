import cv2 as cv
import numpy as np
import time

# 初始化摄像头
cap = cv.VideoCapture(0)

# 设置期望的帧率和分辨率
desired_fps = 20
desired_width = 40
desired_height = 80

# 设置摄像头属性
cap.set(cv.CAP_PROP_FPS, desired_fps)
cap.set(cv.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, desired_height)

# 初始化帧计数器和开始时间
frame_count = 0
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 更新帧计数器
    frame_count += 1

    # 计算经过时间
    elapsed_time = time.time() - start_time

    # 计算当前帧率
    if elapsed_time > 0:
        actual_fps = frame_count / elapsed_time
        # 将帧率显示在图像上
        cv.putText(frame, f"FPS: {actual_fps:.2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv.imshow('frame', frame)

    # 按 'q' 键退出
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv.destroyAllWindows()