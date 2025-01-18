import cv2 as cv
import numpy as np

# 蓝色的 HSV 范围
lower_blue = np.array([100, 50, 90])
upper_blue = np.array([140, 200, 255])

# 读取图像
image_path = 'real_tar.png'  # 替换为您的图片文件路径
image = cv.imread(image_path)

# 检查图像是否成功加载
if image is None:
    print("Error: Image not found.")
    exit()

# 将 BGR 图像转换为 HSV 图像
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # 创建蓝色的掩码
mask = cv.inRange(hsv, lower_blue, upper_blue)

# 转换为灰度图
#gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)

# 应用高斯模糊来减少噪声
blurred = cv.GaussianBlur(mask, (5, 5), 0)

# 使用Canny边缘检测
edges = cv.Canny(blurred, 50, 150)

# 检测轮廓
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
c=cv.drawContours(mask, contours, -1, (0,255,0), 3)
print(len(contours))
# 绘制轮廓和拟合的矩形
for contour in contours:
    # 计算轮廓的最小外接矩形
    rect = cv.minAreaRect(contour)
    box = cv.boxPoints(rect)
    box = np.int0(box)  # 转换为整数
    # 绘制矩形
    cv.rectangle(image, (int(rect[0][0]), int(rect[0][1])), (int(rect[1][0]), int(rect[1][1])), (0, 255, 0), 2)

# 显示结果
cv.imshow('Rectangle Fitting', image)
cv.imshow('s',mask)
cv.imshow('a',c)
cv.waitKey(0)
cv.destroyAllWindows()