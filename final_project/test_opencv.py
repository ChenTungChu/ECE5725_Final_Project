import cv2
import numpy as np

print(cv2.__version__)

videoCap = cv2.VideoCapture(0)

if not videoCap:
    print("Error, cant find camera")
else:
    print("Success")
    
videoWidth = videoCap.get(cv2.CAP_PROP_FRAME_WIDTH)
videoHeight = videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Default video resolution: " + str(int(videoWidth)) + "x" + str(int(videoHeight)))

grayScaleFlag = blurFlag = sharpenFlag = edgeFlag = drawFlag = False
blurKernel = np.ones((3,3)) / 9.0
sharpenKernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

while True:
    returnBool, frame = videoCap.read()
    if grayScaleFlag:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if blurFlag:
        frame = cv2.filter2D(frame, -1, blurKernel)
    if sharpenFlag:
        frame = cv2.filter2D(frame, -1, sharpenKernel)
    if edgeFlag:
        frame = cv2.Canny(frame, 50, 200)
    if drawFlag:
        cv2.circle(frame, (319, 239), 30, (255, 0, 0))
        cv2.putText(feame, 'Hello', (0, 470), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
else:
    print("Error")