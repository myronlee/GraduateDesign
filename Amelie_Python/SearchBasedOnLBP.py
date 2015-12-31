__author__ = 'ligang'

import Uniform_LBP
import Top_K
import File_Operation
import Distance
import heapq
import shutil
import os

def search(img_path):
    ulbp_f = Uniform_LBP.ulbp(img_path)
    ulbps = File_Operation.read_list_from_file('/Users/ligang/Documents/ulbp.txt')
    distances = []
    for ulbp_tuple in ulbps:
        d = Distance.distance(ulbp_f, ulbp_tuple[1])
        distances.append((ulbp_tuple[0], d))
    top_distances = heapq.nsmallest(20, distances, key=lambda x: x[1])
    dstDir = '/Users/ligang/Documents/Emilie/lbp_search_result'
    img_set_dir = '/Users/ligang/Documents/Emilie/dress'
    for top in top_distances:
        shutil.copy2(os.path.join(img_set_dir, top[0]), os.path.join(dstDir, top[0]))
    print top_distances




if __name__ == '__main__':
    img_path = '/Users/ligang/Documents/Emilie/dress/78_0.jpg'
    print search(img_path)