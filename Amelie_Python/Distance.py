__author__ = 'ligang'

def distance(la, lb):
    d = 0
    for x, y in zip(la, lb):
        d = d + (x-y) * (x-y)
    return d