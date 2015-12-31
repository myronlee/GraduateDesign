__author__ = 'ligang'

import cv2
from matplotlib import pyplot as plt
import math
import time
import os
import File_Operation

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def normalize(l):
    s = sum(l) * 1.0
    return [e/s for e in l]

def ulbp(img_path):
    try:
        img = cv2.imread(img_path, 0)
    except Exception, exception:
        print exception
        return []
    except IOError, error:
        print error
        return []

    uniform_table = [0,1,2,3,4,58,5,6,7,58,58,58,8,58,9,10,11,58,58,58,58,58,58,58,12,58,58,58,13,58,
        14,15,16,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,17,58,58,58,58,58,58,58,18,
        58,58,58,19,58,20,21,22,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,
        58,58,58,58,58,58,58,58,58,58,58,58,23,58,58,58,58,58,58,58,58,58,58,58,58,58,
        58,58,24,58,58,58,58,58,58,58,25,58,58,58,26,58,27,28,29,30,58,31,58,58,58,32,58,
        58,58,58,58,58,58,33,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,34,58,58,58,58,
        58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,
        58,35,36,37,58,38,58,58,58,39,58,58,58,58,58,58,58,40,58,58,58,58,58,58,58,58,58,
        58,58,58,58,58,58,41,42,43,58,44,58,58,58,45,58,58,58,58,58,58,58,46,47,48,58,49,
        58,58,58,50,51,52,58,53,54,55,56,57]

    ulbp_feature = [0]*59

    if img is None:
        return []

    # loop each point
    for x in xrange(1, len(img)-1):
        for y in xrange(1, len(img[0])-1):
            center = img[x][y]
            lbp = 0

            if center <= img[x-1][y-1]:
                lbp = lbp + 1
            if center <= img[x-1][y]:
                lbp = lbp + 2
            if center <= img[x-1][y+1]:
                lbp = lbp + 4
            if center <= img[x][y+1]:
                lbp = lbp + 8
            if center <= img[x+1][y+1]:
                lbp = lbp + 16
            if center <= img[x+1][y]:
                lbp = lbp + 32
            if center <= img[x+1][y-1]:
                lbp = lbp + 64
            if center <= img[x][y-1]:
                lbp = lbp + 128

            unlbp_id = uniform_table[lbp]
            ulbp_feature[unlbp_id] = ulbp_feature[unlbp_id]+1

    return normalize(ulbp_feature)


if __name__ == '__main__':
    # img_path = '/Users/ligang/Documents/Emilie/dress/85_0.jpg'
    # print ulbp(img_path)

    workDir = '/Users/ligang/Documents/Emilie/dress'

    startTime = time.time()

    count = 0
    data = []

    for filename in os.listdir(workDir):
        ulbp_feature = ulbp(os.path.join(workDir, filename))
        if ulbp_feature is None:
            continue
        if len(ulbp_feature) > 0:
            data.append((filename, ulbp_feature))
            count = count + 1
            print count

    endTime = time.time()
    useTime = endTime - startTime
    eachTime = useTime / count
    print count, eachTime

    File_Operation.write_list_to_file('/Users/ligang/Documents/ulbp.txt', data)
