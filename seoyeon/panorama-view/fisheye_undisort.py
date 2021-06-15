import cv2
import numpy as np


# ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
# K = np.array((3,3))
# R = np.array((3,3))
# T = np.array((4,1))
#
# P = np.array([[0.9995185086, 0.0041276589, -0.0307524527, 0.7264036936],
#             [-0.0307926666, 0.0100608424, -0.9994751579, -0.1499658517],
#             [-0.0038160970, 0.9999408692, 0.0101830998, -1.0686400091]])
#
# K, R, T, _, _, _, _ = cv2.decomposeProjectionMatrix(P)
#
# print(K)
# print(R)
# print(T)

# ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
def undistortMap(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imwrite('./result/03_80_map.png', undistorted_img)
    # cv2.imshow("undistorted", undistorted_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def undisort(img_path):
    img = cv2.imread(img_path)
    undistorted_img = cv2.fisheye.undistortImage(img, K, D, None, Knew)
    cv2.imwrite('./result/03_80_ud.png', undistorted_img)

def undistort_image(img_path, balance=0.0, dim2=None, dim3=None):
    img = cv2.imread(img_path)
    dim1 = img.shape[:2][::-1]  #dim1 is the dimension of input image to un-distort
    if not dim2:
        dim2 = dim1
    if not dim3:
        dim3 = dim1
    scaled_K = K * dim1[0] / DIM[0]  # The values of K is to scale with image dimension.
    scaled_K[2][2] = 1.0  # Except that K[2][2] is always 1.0
    # This is how scaled_K, dim2 and balance are used to determine the final K used to un-distort image. OpenCV document failed to make this clear!
    new_K = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(scaled_K, D, dim2, np.eye(3), balance=balance)
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(scaled_K, D, np.eye(3), new_K, dim3, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imwrite('./result/03_80_other.png', undistorted_img)

DIM = (1400, 1400)

# K = np.array([[1.3363220825849971e+03, 0., 7.1694323510126321e+02],
#               [0., 1.3357883350012958e+03, 7.0576498308221585e+02],
#               [0., 0., 1.]])
#
# D = np.array([1.6798235660113681e-02, 1.6548773243373522e+00,
#               4.2223943394772046e-04, 4.2462134260997584e-04])
#
# Knew = K.copy()
# Knew[:2, :2] = 0.4 * Knew[:2, :2]
#
# input = 'data/02_80.png'
# output = './result/02_80.png'
# undistortMap(input)
# undisort(input)
# undistort_image(input)

K = np.array([[1.4854388981875156e+03, 0., 6.9888316784030962e+02],
              [0., 1.4849477411748708e+03, 6.9814541887723055e+02],
              [0., 0., 1.]])

D = np.array([4.9370396274089505e-02, 4.5068455478645308e+00,
              1.3477698472982495e-03, -7.0340482615055284e-04])

Knew = K.copy()
Knew[:2, :2] = 0.4 * Knew[:2, :2]

input = 'data/03_80.png'
output = './result/03_80.png'
undistortMap(input)
undisort(input)
undistort_image(input)