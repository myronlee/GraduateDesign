__author__ = 'ligang'

import os
import numpy as np
import cv2
import time


mask = np.zeros((297, 235), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (20, 5, 215, 297)

workDir = '/Users/ligang/Documents/Emilie/dress'
destDir = '/Users/ligang/Documents/Emilie/dress_cutted_1'

startTime = time.time()
count = 0

for filename in os.listdir(workDir):
    img = cv2.imread(os.path.join(workDir, filename))

    if img is None:
        continue

    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    cv2.imwrite(os.path.join(destDir, filename), img)

    print filename, str(count)
    count = count + 1
    # if count == 10:
    #     break

endTime = time.time()
useTime = endTime - startTime


print 'use time', str(useTime)
print 'count', str(count)
print 'average use time', str(useTime*1.0/count)