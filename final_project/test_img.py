import numpy as np
import cv2
import glob



# img0 = cv2.imread('camera_cal/calibration1.jpg')
# img1 = cv2.imread('test6.jpg')
# img2 = cv2.imread('lane4.jpg')
# print(f"img0 = {img0.shape[0]}, {img0.shape[1]}")
# print(f"img1 = {img1.shape[0]}, {img1.shape[1]}")
# print(f"img2 = {img2.shape[0]}, {img2.shape[1]}")
def calibrate_Camera():
    images_path = glob.glob('/home/pi/final_project/camera_cal/calibration*.jpg')
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6*9,3), np.float32)
    objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d points in real world space
    imgpoints = [] # 2d points in image plane.
    for img_path in images_path:
        img = cv2.imread(img_path)
        img = cv2.resize(img, (320, 240))
        # Read calibration image
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
        # Find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, (9,6),None)        
        # If found, add object points, image points
        if ret == True:
            objpoints.append(objp)
            imgpoints.append(corners)
    # Use cv2.calibrateCamera()
    # Do camera calibration given object points and image points
    img_size = (img.shape[1], img.shape[0])
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size,None,None)
    return ret, mtx, dist, rvecs, tvecs
    
ret, mtx, dist, rvecs, tvecs = calibrate_Camera()
print(tvecs)

    
    