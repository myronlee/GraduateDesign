__author__ = 'ligang'

import pickle

def write_list_to_file(path, l):
    f = open(path, 'wb')
    pickle.dump(l, f)
    f.close()

def read_list_from_file(path):
    f = open(path, 'rb')
    l = pickle.load(f)
    f.close()
    return l