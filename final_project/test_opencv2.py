import numpy as np
import cv2

cap = cv2.VideoCapture(-1)
cap.set(3, 320)
cap.set(4, 240)

while True:
    _, frame = cap.read()
    # frame = cv2.resize(frame, (400, 240))
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray, 50, 150, 3)
    # img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # lines = cv2.HoughLinesP(edges, 1, np.pi/180, 1, minLineLength=55, maxLineGap=9)
    # for line in lines:
    #     x1, x2, y1, y2 = line[0]
    #     if x1 < 150 or x1 > 500 or x2 > 500 or y2 < 500:
    #         continue

    #     cv2.line(img_rgb, (x1,y1), (x2,y2), (255,0,0), 4)
    
    # cv2.imshow("output", img_rgb)
    cv2.imshow("original", frame)
    if cv2.waitKey(1) == ord('q'):
        break


