import cv2

cap = cv2.VideoCapture(-1)
# cap.set(3, 320)
# cap.set(4, 320)


while True:
    _, frame = cap.read()
    cv2.imshow('Output', frame)
    cv2.waitKey(1)