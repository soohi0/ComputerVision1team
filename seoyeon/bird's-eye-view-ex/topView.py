"""
This code is used to obtain the bird's view of
a robot with two cameras installed(front and back cameras)
"""
from cv2 import *
from Undistortion import UndistortFisheye
from PerspectiveTransformation import EagleView
import numpy as np

# frontStream = cv2.VideoCapture("dataset/front_camera.avi")
# backStream = cv2.VideoCapture("dataset/back_camera.avi")

frontCamera = UndistortFisheye("Front_Camera")
backCamera = UndistortFisheye("Back_Camera")

frontEagle = EagleView()
backEagle = EagleView()

#####

def fun_read_data(filename):
    image = imread(filename)
    imshow('getPoints', image)
    setMouseCallback('getPoints', fun_callback_mouse)
    waitKey(0)  # 키입력으로 윈도우 종료
    destroyAllWindows()

    k_max = len(points)
    for k in range(k_max):
        x, y = points[k][0], points[k][1]
        drawMarker(image, (x, y), (255, 0, 0), 0)
        putText(image, str(k+1), (x, y-10), FONT_ITALIC, 0.5, (0, 255, 255))
    return image

points = []
def fun_callback_mouse(event, x, y, flags, NULL):
    if event == EVENT_LBUTTONDOWN:
        points.append((x, y))

x1 = fun_read_data('dataset/dash_cam.jpg')
imshow('showPoints', x1)
waitKey(0)  # 키입력으로 윈도우 종료
# h, w = x.shape[:2]
srcPoints1 = np.array(points, np.float32)
# dstPoints = np.array([[100, 100], [w-100, 100], [w-100, h-100], [100, h-100]], np.float32)

points.clear()

x2 = fun_read_data('dataset/StrechedOut_Rear_View.jpg')
imshow('showPoints', x2)
waitKey(0)  # 키입력으로 윈도우 종료
srcPoints2 = np.array(points, np.float32)

#####
# frontEagle.setDimensions((186, 195), (484, 207), (588, 402), (97, 363))
# backEagle.setDimensions((171, 240), (469, 240), (603, 452), (52, 441))
frontEagle.setDimensions(srcPoints1[0], srcPoints1[1], srcPoints1[2], srcPoints1[3])
backEagle.setDimensions(srcPoints2[0], srcPoints2[1], srcPoints2[2], srcPoints2[3])

while True:
    # _, frontFrame = frontStream.read()
    # _, backFrame = backStream.read()
    frontFrame = cv2.imread("dataset/dash_cam.jpg")
    backFrame = cv2.imread("dataset/StrechedOut_Rear_View.jpg")
    
    # frontView = frontCamera.undistort(frontFrame)
    topDown_Front = frontEagle.transfrom(frontFrame)
    # backView = backCamera.undistort(backFrame)
    topDown_Back = backEagle.transfrom(backFrame)

    cv2.imshow("Front Bird's Eye View", topDown_Front)
    cv2.imshow("Back Bird's Eye View", topDown_Back)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("dataset/dash_cam_top.jpg", topDown_Front)
        # cv2.imwrite("dataset/StrechedOut_Rear_Topview.jpg", topDown_Back)
        print(srcPoints1)
        # print(srcPoints2)

cv2.destroyAllWindows()