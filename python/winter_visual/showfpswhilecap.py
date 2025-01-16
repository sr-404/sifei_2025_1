import numpy as np
import cv2 as cv
import time

# 初始化摄像头
cap = cv.VideoCapture(0)

# 设置帧率，例如设置为30帧/秒
desired_fps = 20
cap.set(cv.CAP_PROP_FPS, desired_fps)

# 初始化帧计数器和开始时间
frame_count = 0
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 更新帧计数器
    frame_count += 1

    # 计算经过时间
    elapsed_time = time.time() - start_time

    # 计算当前帧率
    if elapsed_time > 0:
        actual_fps = frame_count / elapsed_time
        # 将帧率显示在图像上
        cv.putText(gray, f"FPS: {actual_fps:.2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv.imshow('frame', gray)

    # 按 'q' 键退出
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv.destroyAllWindows()