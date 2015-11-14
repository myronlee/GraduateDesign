__author__ = 'ligang'

import cv2
import numpy as np

img = cv2.imread('8_1.jpg')
img2 = cv2.imread('8_2.jpg')

sift = cv2.SIFT()

kp, des = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(img2, None)

print len(kp)
print len(kp2)

print des[0]
print type(des)


cv2.imwrite('8_1_kp.jpg', cv2.drawKeypoints(img, kp))
cv2.imwrite('8_2_kp.jpg', cv2.drawKeypoints(img, kp2))
