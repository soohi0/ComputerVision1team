import cv2
from AroundViewMonitoring import avm
import datetime


# frontStream = cv2.VideoCapture(0)
# backStream = cv2.VideoCapture(1)
# frontStream = cv2.VideoCapture("dataset/front_camera.avi")
# backStream = cv2.VideoCapture("dataset/back_camera.avi")

avm = avm()

# frontFrame = cv2.imread("Front_View.jpg")
# backFrame = cv2.imread("Back_View.jpg")
startTime = datetime.datetime.now()
while True:
    # isGrabbed, frontFrame = frontStream.read()
    # isGrabbed2, backFrame = backStream.read()
    # if not isGrabbed or not isGrabbed2:
    #     break

    frontFrame = cv2.imread("dataset/StrechedOut_Front_Topview.jpg")
    backFrame = cv2.imread("dataset/StrechedOut_Rear_Topview.jpg")

    birdView = avm.runAVM(frontFrame, backFrame)
    cv2.imshow("Bird's Eye View", birdView)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("dataset/StrechedOut_Bird's_eye_View.jpg", birdView)

endTime = datetime.datetime.now()
time = (endTime - startTime).total_seconds()
print ("Approximate elapsed time is %(fps)d: "%{"fps": time})
cv2.destroyAllWindows()