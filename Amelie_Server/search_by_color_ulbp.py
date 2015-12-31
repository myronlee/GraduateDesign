__author__ = 'ligang'

import color
import ulbp
import top_k
import File_Operation
import Distance
import heapq
import shutil
import os

def search(img_path):
    cf = color.get_color_feature(img_path)
    unlbp_feature = ulbp.ulbp(img_path)

    cfs = File_Operation.read_list_from_file('/Users/ligang/Documents/cfs.txt')
    ulbps = File_Operation.read_list_from_file('/Users/ligang/Documents/ulbp.txt')

    distances = []

    for cf_tuple, ulbp_tuple in zip(cfs, ulbps):
        assert cf_tuple[0] == ulbp_tuple[0]

        d_color = Distance.distance(cf, cf_tuple[1])
        d_ulbp = Distance.distance(unlbp_feature, ulbp_tuple[1])
        d = d_color + d_ulbp

        distances.append((cf_tuple[0], d))

    top_distances = heapq.nsmallest(20, distances, key=lambda x: x[1])
    dstDir = '/Users/ligang/Documents/Emilie/colorlbp_search_result'
    img_set_dir = '/Users/ligang/Documents/Emilie/dress'
    for top in top_distances:
        shutil.copy2(os.path.join(img_set_dir, top[0]), os.path.join(dstDir, top[0]))
    print top_distances




if __name__ == '__main__':
    img_path = '/Users/ligang/Documents/Emilie/dress/140_0.jpg'
    print search(img_path)