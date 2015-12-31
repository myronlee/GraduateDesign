__author__ = 'ligang'
import os
import time
import numpy as np
import cv2

def caculate(sift, filename):
    img = cv2.imread(filename)
    if img is None:
        return None
    kp, des = sift.detectAndCompute(img, None)
    return des

def save(filename, des):
    np.save(filename, des)

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

if __name__ == '__main__':
    path = '/Users/ligang/Documents/Emilie/dress'
    des_path = '/Users/ligang/Documents/Emilie/sift_dress'
    sift = cv2.SIFT()

    kp_count = []

    startTime = time.time()

    for file in os.listdir(path):
        if not file.endswith('.jpg'):
            continue

        img_file = os.path.join(path, file)
        des = caculate(sift, img_file)

        if des is None:
            continue

        des_file = os.path.join(des_path, file)
        save(des_file, des)

        kp_count.append(des.shape[0])
        print des.shape[0]

    stopTime = time.time()

    print 'total use time :', stopTime - startTime

    print 'image num:', len(kp_count)

    print 'average use time :', (stopTime - startTime) / len(kp_count)

    print 'average kp num:', sum(kp_count) / len(kp_count)

    write_file('/Users/ligang/Documents/Emilie/dress_sift_kp_count.txt', str(kp_count))
