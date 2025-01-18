import cv2
import numpy as np

# 初始化视频捕捉
cap = cv2.VideoCapture("real_tar.mp4")  # 使用摄像头，传入视频文件路径可以处理视频文件

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 转换为HSV空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设置蓝色的HSV范围
    lower_blue = np.array([100, 120, 50])  
    upper_blue = np.array([140, 255, 255])  
    #创建蓝色mask，像素值在指定的颜色范围内时为白色（255），不在指定范围内时为黑色（0）
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)


    # 对掩码进行轮廓检测
    def detect_contours(mask):
        #只检测外部轮廓，返回轮廓的二维数组，
        #第3个参数指压缩水平方向、垂直方向、对角线方向的元素，只保留该方向的终点坐标。一个矩形只用4个点来保存信息
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            #计算每个轮廓面积
            siz=cv2.contourArea(contour)
            if 1000<siz<25000:  # 过滤轮廓面积
                cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)#绘制轮廓

                # 计算重心
                moments = cv2.moments(contour)
                if moments["m00"] != 0:        #确认面积不为0
                    cX = int(moments["m10"] / moments["m00"])
                    cY = int(moments["m01"] / moments["m00"])
                    cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)     #绘制圆点，粗细-1代表填充
                    

                    #计算最小外接矩形，返回一个对象包含矩形的中心点坐标、size(W&L)、旋转角度
                    rect = cv2.minAreaRect(contour)
                    point=rect[0]   #中心点坐标
                    print(point)
                    siz=rect[1]     #size
                    print(siz)
                    angle=rect[2]   #angle
                    print(angle)
                    box = cv2.boxPoints(rect)
                    box=np.int32(box)
                    cv2.drawContours(frame, [box], -1, (225, 225, 225), 2)

    # 检测蓝色块
    detect_contours(mask_blue)

    # 显示结果
    cv2.imshow("mask",mask_blue)
    cv2.imshow("Frame", frame)
    #  'q' for quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()