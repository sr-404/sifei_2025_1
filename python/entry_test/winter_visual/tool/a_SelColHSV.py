import cv2 as cv
import numpy as np

# 鼠标回调函数
def get_pixel_color(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # 获取鼠标点击位置的像素值
        bgr_color = frame[y, x]
        # 将 BGR 颜色转换为 HSV 颜色
        hsv_color = cv.cvtColor(np.uint8([[bgr_color]]), cv.COLOR_BGR2HSV)[0][0]
        print(f"HSV color at ({x}, {y}): {hsv_color}")

# 读取图像
image_path = 'real_tar.png'
frame = cv.imread(image_path)

if frame is None:
    print("Error: Could not open or find the image.")
    exit()

# 创建窗口并设置鼠标回调函数
cv.namedWindow('Image')
cv.setMouseCallback('Image', get_pixel_color)

while True:
    # 显示图像
    cv.imshow('Image', frame)
    
    # 按 'q' 键退出
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cv.destroyAllWindows()