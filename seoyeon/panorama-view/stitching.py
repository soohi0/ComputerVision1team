#!/usr/bin/env python
import cv2 as cv
import sys

img_names = ['data/00_80.png', 'data/01_80.png', 'data/cropped_02_80.png', 'data/cropped_03_80.png']
output = 'result/panorama_fisheye.jpg'
imgs = []
for img_name in img_names:
    img = cv.imread(cv.samples.findFile(img_name))
    if img is None:
        print("can't read image " + img_name)
        sys.exit(-1)
    imgs.append(img)

PANORAMA = 0
SCANS = 1

stitcher = cv.Stitcher.create(PANORAMA)
status, pano = stitcher.stitch(imgs)
if status != cv.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    sys.exit(-1)
cv.imwrite(output, pano)
print("stitching completed successfully. %s saved!" % output)

cv.destroyAllWindows()