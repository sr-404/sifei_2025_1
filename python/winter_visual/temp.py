import cv2 as cv
import numpy as np

# 读取图像
image_path = 'reverse_tar.png'  # 替换为您的图片文件路径
image = cv.imread(image_path)

# 转换为HSV颜色空间
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# 定义蓝色的HSV范围
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

# 创建蓝色的掩码
mask = cv.inRange(hsv, lower_blue, upper_blue)

# 提取蓝色区域
blue_region = cv.bitwise_and(image, image, mask=mask)

# 找到轮廓
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 假设最大的轮廓是标靶
if contours:
    largest_contour = max(contours, key=cv.contourArea)
    x, y, w, h = cv.boundingRect(largest_contour)

    # 计算旋转角度
    rect = cv.minAreaRect(largest_contour)
    box = cv.boxPoints(rect)
    box = np.int0(box)  # 转换为整数
    center = (x + w // 2, y + h // 2)  # 计算中心点
    points = box[0] + center  # 将第一个点移动到中心
    points[1:] += center  # 将其他点也移动到中心
    points = points.reshape(-1, 2)  # 转换为二维数组
    angles = np.arctan2(points[:, 1], points[:, 0])  # 计算角度
    angle = np.degrees(np.min(angles))  # 找到最小角度

    # 旋转图像
    M = cv.getRotationMatrix2D(center, angle, 1)
    rotated = cv.warpAffine(image, M)
    rotated_blue_region = cv.bitwise_and(rotated, rotated, mask=mask)

    # 显示结果
    cv.imshow('Original', image)
    cv.imshow('Rotated', rotated_blue_region)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("No blue target found")