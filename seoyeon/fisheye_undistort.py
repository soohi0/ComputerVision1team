import cv2
import numpy as np
import glob

assert float(cv2.__version__.rsplit('.', 1)[0]) >= 3, 'OpenCV version 3 or newer required.'

K = np.array([[788.629315,  0.,             687.158398],
              [0.,          786.382230,     317.752196],
              [0.,          0.,             1.]])

# zero distortion coefficients work well for this image
D = np.array([1.6798235660113681e-02, 1.6548773243373522e+00,
              4.2223943394772046e-04, 4.2462134260997584e-04])

# use Knew to scale the output
Knew = K.copy()
Knew[:2, :2] = 0.5 * Knew[:2, :2]

imgs = glob.glob('image01/*.png')
for fname in imgs:
    img = cv2.imread(fname)
    img_undistorted = cv2.undistort(img, K, D, None, K)
    cv2.imwrite('./result/'+fname, img_undistorted)
    # cv2.imshow('undistorted', img_undistorted)
    # cv2.waitKey()

imgs = glob.glob('image02/*.png')
for fname in imgs:
    img = cv2.imread(fname)
    img_undistorted = cv2.undistort(img, K, D, None, Knew)
    cv2.imwrite('./result/'+fname, img_undistorted)
    # cv2.imshow('undistorted', img_undistorted)
    # cv2.waitKey()