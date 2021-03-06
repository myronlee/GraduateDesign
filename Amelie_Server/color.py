from PIL import Image
from numpy import *
import colorsys
from matplotlib import pyplot as plt
import cv2
import datetime
from PIL import ImageFile
import time
import os
import sys
import File_Operation

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def compress_hsv(h, s, v):
    if 316 <= h or h <= 20:
        H = 0
    elif 21 <= h <= 40:
        H = 1
    elif 41 <= h <= 75:
        H = 2
    elif 76 <= h <= 155:
        H = 3
    elif 156 <= h <= 190:
        H = 4
    elif 191 <= h <= 270:
        H = 5
    elif 271 <= h <= 295:
        H = 6
    elif 296 <= h <= 315:
        H = 7
    else:
        assert False

    if 0 <= s <= 0.2:
        S = 0
    elif 0.2 <= s <= 0.7:
        S = 1
    elif 0.7 <= s <= 1:
        S = 2
    else:
        assert False

    if 0 <= v <= 0.2:
        V = 0
    elif 0.2 <= v <= 0.7:
        V = 1
    elif 0.7 <= v <= 1:
        V = 2
    else:
        assert False

    return H, S, V

def normalize(l):
    s = sum(l) * 1.0
    return [e/s for e in l]

def get_color_feature(image_path):
    try:
        img = Image.open(image_path)
    except Exception, exception:
        print exception
        return []
    except IOError, error:
        print error
        return []

    wl = [0]*72
    for_show = []
    for count, (r, g, b) in img.getcolors(img.size[0]*img.size[1]):
        h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        h = int(h*360)

        H, S, V = compress_hsv(h, s, v)

        W = 9*H + 3*S + V
        assert W < 72
        wl[W] = wl[W] + count

        for i in xrange(count):
            for_show.append(W)

    # print wl
    wl = normalize(wl)
    return wl
    # print wl
    # plt.hist(for_show, 72, normed = True, color = 'gray')
    # # plt.xlim([0,72])
    # # plt.legend(('cdf','histogram'), loc = 'upper left')
    # plt.show()

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # # print sum(wl)

if __name__ == '__main__':
    #
    # cf1 = get_color_feature('/Users/ligang/170_0.jpg')
    # cf2 = get_color_feature('/Users/ligang/189_0.jpg')
    # cf3 = get_color_feature('/Users/ligang/129_0.jpg')
    # dis1 , dis2 = 0, 0
    # for i in xrange(71):
    #     dis1 += (cf1[i]-cf2[i]) * (cf1[i]-cf2[i])
    #     dis2 += (cf1[i]-cf3[i]) * (cf1[i]-cf3[i])
    # print dis1, dis2

    workDir = '/Users/ligang/Documents/Emilie/dress'

    startTime = time.time()
    count = 0
    cfs = []

    for filename in os.listdir(workDir):
        cf = get_color_feature(os.path.join(workDir, filename))
        if len(cf) > 0:
            cfs.append((filename, cf))
            count = count + 1

    endTime = time.time()
    useTime = endTime - startTime
    print useTime, count
    print sys.getsizeof(cfs)

    File_Operation.write_list_to_file('/Users/ligang/Documents/cfs.txt', cfs)
