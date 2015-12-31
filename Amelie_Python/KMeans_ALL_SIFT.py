__author__ = 'ligang'

import os
import json
import numpy as np
import cv2
import time

def getAllDes(path):
    res = None
    for f in os.listdir(path):
        if not f.endswith('.npy'):
            continue
        des = np.load(os.path.join(path, f))
        if res is None:
            res = des
        else:
            res = np.vstack((res, des))
    print 'num of des waiting to k-means ',  res.shape
    return res

def getVectorFromLabelAndKpCount(file, label):
    res = []

    s = open(file, 'r').read()
    kpCounts = json.loads(s)

    base = 0
    for kpCount in kpCounts:

        vector = [0] * 100
        for i in xrange(kpCount):
            labelIndex = base + i
            belongClass = label[labelIndex]
            vector[belongClass] = vector[belongClass]+1

        res.append(vector)
        base = base + kpCount


    return res


workDir = '/Users/ligang/Documents/Emilie/sift_dress_cutted_1'

des = getAllDes(workDir)

k = 10000
attempts = 100
eps = 10.0

startTime = time.time()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, attempts, eps)
ret, label, center = cv2.kmeans(des, k, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
endTime = time.time()

useTime = endTime - startTime

print('use time: ', useTime)

#
# res = getVectorFromLabelAndKpCount('/Users/ligang/Documents/Emilie/dress_cutted_1_sift_kp_count.txt', label)
#
# np.save('/Users/ligang/Documents/Emilie/dress_cutted_1_sift_center', center)
#
# resFile = open('/Users/ligang/Documents/Emilie/label.txt', 'w')
# resFile.write(str(res))
# resFile.close()
