import cv2
# import pandas as pd
import numpy as np
import os
# import matplotlib.pyplot as plt

cap = cv2.imread('wires.jpg')
# cap.set(3, 320)
# cap.set(4, 320)
    
frame = cv2.resize(cap, (640, 480))
blur = cv2.GaussianBlur(frame, (5,5), 0)
img_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('original', frame)

# Black color
low_black = np.array([0, 0, 0]) # in hsv 
high_black = np.array([255, 255, 40]) # 40 or 30 
black_mask = cv2.inRange(img_hsv, low_black, high_black)
black = cv2.bitwise_and(frame, frame, mask=black_mask)
cv2.imshow('black_detection', black)
canny = cv2.Canny(black_mask, 50, 150)

'''
ROI: 我們感興趣的區塊, 設計一個矩陣
np.zeros去畫一張以canny為寬高的全黑的圖
cv2.fillPoly: 在roi_mask填上我們的ROI圖並設定那塊區域為255 因此被我們填充的區域(ROI)就是亮的
'''
roi_mask = np.zeros(canny.shape, dtype=np.uint8)
# ROI = np.array([[(0,800),(1400,800),(1400,350),(0,350)]])
# ROI = np.array([[(0,150),(640,150),(640,0),(0,0)]])
ROI = np.array([[(0,480), (640,480), (0,150), (640,150)]])
cv2.fillPoly(roi_mask, pts=ROI, color=255)

ROI_canny = cv2.bitwise_and(canny, roi_mask)
try:
    # lines = cv2.HoughLinesP(ROI_canny, 1, np.pi/180, 50, maxLineGap=50, minLineLength=20)
    lines = cv2.HoughLinesP(ROI_canny, 1, np.pi/180, 50, maxLineGap=150, minLineLength=30)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
except:
    pass
    
cv2.imshow('canny', canny)
cv2.waitKey(0)

if cv2.waitKey(1) == ord('q'):
    cap.release()
    cv2.destroyAllWindows()

