import cv2 as cv
import numpy as np

def load_and_resize_image(image_path, new_size=(480, 640)):
    """加载图像并调整大小。"""
    img = cv.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image from {image_path}.")
        return None
    return cv.resize(img, new_size)

def apply_gaussian_blur(image):
    """对图像应用高斯模糊。"""
    return cv.GaussianBlur(image, (5, 5), 0)

def detect_blue_areas(img, lower_blue, upper_blue):
    """检测图像中的蓝色区域。"""
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    return mask

def find_contours(mask):
    """在掩码中找到轮廓。"""
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours, color=(0, 255, 0), thickness=2):
    """在图像上绘制轮廓。"""
    img_draw = cv.drawContours(image.copy(), contours, -1, color, thickness)
    return img_draw

def fit_ellipse_and_rotate(image, contour):
    """拟合椭圆并旋转图像。"""
    #(x, y)为椭圆中心点坐标
    (x, y), (Ma, ma), angle = cv.fitEllipse(contour)
    #参数是旋转中心点、角度和缩放因子，返回一个旋转矩阵
    M = cv.getRotationMatrix2D((x, y), angle, 1)
    #旋转函数
    res = cv.warpAffine(image, M,None)
    return res

#接收图片，调整大小
image_path = "reverse_tar.png"
img = load_and_resize_image(image_path)
if img is None:
    print("fail to find photo")
#高斯模糊并在mask上画出轮廓
img_blur = apply_gaussian_blur(img)
lower_blue = np.array([100, 43, 50])
upper_blue = np.array([130, 255, 255])
img_mask = detect_blue_areas(img_blur, lower_blue, upper_blue)
contours = find_contours(img_mask)
img_draw = draw_contours(img, contours)



for contour in contours:
    rect = cv.minAreaRect(contour)
    box = cv.boxPoints(rect)
    box = np.int32(box)
    cv.drawContours(img, [box],0, (0, 255, 0), 2)

    # 计算质心
    moments = cv.moments(contour)
    if moments["m00"] != 0:
        cX = int(moments["m10"] / moments["m00"])
        cY = int(moments["m01"] / moments["m00"])
        cv.circle(img, (cX, cY), 7, (0, 0, 255), -1)

    # 计算最小外接矩形，返回一个对象包含矩形的中心点坐标、size(W&L)、旋转角度
    rect = cv.minAreaRect(contour)
    point = rect[0]   # 中心点坐标
    print(point)
    siz = rect[1]     # size
    print(siz)
    angle = rect[2]   # angle
    print(angle)
    box = cv.boxPoints(rect)
    box = np.int32(box)
    cv.drawContours(img, [box], -1, (0, 0, 255), 2)

    # 旋转变换
    res = fit_ellipse_and_rotate(img, contours[0])
    cv.imshow("Rotated", res)
    cv.imshow("Original", img)
    cv.imshow("Gaussian Blur", img_blur)
    cv.imshow("Mask", img_mask)
    cv.imshow("Contours", img_draw)

    cv.waitKey(0)
    cv.destroyAllWindows()

