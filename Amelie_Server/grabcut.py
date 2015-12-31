__author__ = 'ligang'

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/ligang/Documents/Emilie/dress/103_0.jpg')
shape = img.shape[:2]
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# rect = (240, 350, 990, 1315)
top = int(shape[1] * 0.25)
left = int(shape[0] * 0.2)
bottom = int(shape[1] * 0.85)
right = int(shape[0] * 0.8)

rect = (top, left, bottom, right)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

cv2.imwrite('/Users/ligang/Documents/Emilie/103_0_cutted.jpg', img)

plt.imshow(img), plt.colorbar(), plt.show()
