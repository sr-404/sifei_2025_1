import cv2 as cv
import numpy as np

# 原始图像
img = cv.imread("reverse_tar.png")
img = cv.resize(img, (480, 640))
cv.imshow("original", img)
cv.waitKey(0)
cv.destroyAllWindows()
#高斯模糊
img_blur = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("GaussianBlur", img_blur)
cv.waitKey(0)
cv.destroyAllWindows()

# kernel = np.ones((7, 7), np.uint8)
# img_blur = cv.morphologyEx(img_blur, cv.MORPH_CLOSE, kernel)
# cv.imshow("img_mor", img_blur)
# cv.waitKey(0)
# cv.destroyAllWindows()

# HSV蓝色范围
lower_blue = np.array([100, 43, 46])
upper_blue = np.array([124, 255, 255])

# 寻找图中蓝色区域
img_hsv = cv.cvtColor(img_blur, cv.COLOR_BGR2HSV)
img_mask = cv.inRange(img_hsv, lower_blue, upper_blue)
cv.imshow("img_mask", img_mask)
cv.waitKey(0)
cv.destroyAllWindows()

# 寻找轮廓
contours, _ = cv.findContours(img_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
img_draw = cv.drawContours(img.copy(), contours, -1, (0, 0, 255), 2)
cv.imshow("img_draw", img_draw)
cv.waitKey(0)
cv.destroyAllWindows()

# 选择目标轮廓
'''轮廓选择需改进，目前选择为面积最大的'''
cnt = contours[0]
contours_max = cv.contourArea(contours[0])
for contour in contours:
    contours_tmp = cv.contourArea(contour)
    # print(contours_tmp)
    if contours_tmp > contours_max:
        contours_max = contours_tmp
        cnt = contour
# img_draw_tmp = cv.drawContours(img.copy(), cnt, -1, (0, 0, 255), 2)
# cv.imshow("img_draw_tmp", img_draw_tmp)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 轮廓方向（最优拟合椭圆的方向）
(x, y), (Ma, ma), angle = cv.fitEllipse(cnt)
print(angle)
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
distance = [(leftmost[0] - x)**2 + (leftmost[1] - y)**2, (rightmost[0] - x)**2 + (rightmost[1] - y)**2, (topmost[0] - x)**2 + (topmost[1] - y)**2, (bottommost[0] - x)**2 + (bottommost[1] - y)**2]
index_max = np.argmax(distance)
# index_max = 0
# dis_max = distance[0]
# for i in range(1, 4):
#     if distance[i] > dis_max:
#         dis_max = distance[i]
#         index_max = i
# print(index_max)
if index_max == 0:
    angle += 180
elif index_max == 2:
    if angle > 90:
        angle += 180
elif index_max == 3:
    if angle < 90:
        angle += 180
# ellipse = cv.fitEllipse(cnt)
# cv.ellipse(img, ellipse, (0, 255, 0), 2)
# cv.imshow("img", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

'''旋转变换可改进'''
# 根据angle进行图像旋转变换
rows, cols = img.shape[:2]
M = cv.getRotationMatrix2D((rows/2, cols/2), angle, 0.6)
res = cv.warpAffine(img.copy(), M, (rows, cols))
cv.imshow("res", res)
cv.waitKey(0)
cv.destroyAllWindows()