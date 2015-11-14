__author__ = 'ligang'

import json
import time
import os
import cv2
import shutil
from matplotlib import pyplot as plt

import Top_K


def distance_of_vector(a, b):
    if len(a) != len(b):
        return -1
    distance = 0
    for i in xrange(len(a)):
        x = a[i]
        y = b[i]
        distance = distance + (x-y)*(x-y)
    return distance

def loadList(filename):
    f = open(filename, 'r')
    s = f.read()
    f.close()
    return json.loads(s)

def normalizeAllVector(vectors):
    normalizedVectors = []
    for vector in vectors:
        s = sum(vector)
        normalizedVector = [0]*len(vector)
        for i, d in enumerate(vector):
            if d != 0:
                normalizedVector[i] = d * 1.0 / s
        normalizedVectors.append(normalizedVector)
    return normalizedVectors



if __name__ == '__main__':
    queryIndex = 1
    vectors = loadList('/Users/ligang/Documents/Emilie/normalized_vectors.txt')

    distances = []
    queryVector = vectors[queryIndex]

    startTime = time.time()

    for vector in vectors:
        distances.append(distance_of_vector(queryVector, vector))

    endTime = time.time()
    useTime = endTime - startTime
    print 'caculate %d distances use time : %d s' % (len(vectors), useTime)

    top_k_images = Top_K.top_k_dists(distances, 20)
    print top_k_images

    dstDir = '/Users/ligang/Documents/Emilie/search_result'
    image_names = []
    img_set_dir = '/Users/ligang/Documents/Emilie/dress_cutted_1'
    filenames = os.listdir(img_set_dir)
    for top_image in top_k_images:
        image_name =  filenames[top_image[0]]

        # img = cv2.imread(os.path.join(img_set_dir, image_name))
        # cv2.imshow(image_name, img)

        shutil.copy2(os.path.join(img_set_dir, image_name), os.path.join(dstDir, image_name))

        image_names.append(image_name)
        # plt.imshow(img), plt.colorbar(), plt.show()

    print image_names