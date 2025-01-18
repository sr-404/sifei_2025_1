import cv2
import numpy as np

# 初始化视频捕捉
cap = cv2.VideoCapture("real_tar.mp4")

def detect_contours(mask, frame):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if 1000 < area < 25000:
            cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)
            moments = cv2.moments(contour)
            if moments["m00"] != 0:
                cX = int(moments["m10"] / moments["m00"])
                cY = int(moments["m01"] / moments["m00"])
                cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int32(box)
                cv2.drawContours(frame, [box], -1, (225, 225, 225), 2)

def num_roi(mask, frame):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if 1000 < area < 25000:
            filled_image = cv2.drawContours(mask.copy(), [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
            result_image = cv2.subtract(filled_image, mask)
            contours_1, _ = cv2.findContours(result_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour_1 in contours_1:
                x, y, w, h = cv2.boundingRect(contour_1)
                cv2.imshow("ROI", frame[y:y+h, x:x+w])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 120, 50])
    upper_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    detect_contours(mask_blue, frame)
    num_roi(mask_blue, frame)

    cv2.imshow("mask", mask_blue)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()