__author__ = 'ligang'

import CaculateColorVector
import Top_K
import File_Operation
import Distance
import heapq

def search(img_path):
    cf = CaculateColorVector.get_color_feature(img_path)
    cfs = File_Operation.read_list_from_file('/Users/ligang/Documents/cfs.txt')
    distances = []
    for cf_tuple in cfs:
        d = Distance.distance(cf, cf_tuple[1])
        distances.append((cf_tuple[0], d))
    top_distances = heapq.nsmallest(10, distances, key=lambda x: x[1])
    print top_distances




if __name__ == '__main__':
    img_path = '/Users/ligang/Documents/Emilie/dress/78_0.jpg'
    print search(img_path)