__author__ = 'ligang'

import heapq
import random
import time

def heapq_sort(l):
    start = time.time()
    heapq.nsmallest(50, l)
    end = time.time()
    return end - start

def qsort(l):
    start = time.time()
    sorted(l)
    end = time.time()
    return end - start

if __name__ == '__main__':
    heapq_time = 0
    qsort_time = 0
    for i in xrange(100):
        l = [int(random.random()*10000)for i in xrange(36960)]
        heapq_time += heapq_sort(l)
        # print  l[:10]
        # l = [int(random.random()*10000) in xrange(36960)]
        qsort_time += qsort(l)
        # print  l[:10]


    print heapq_time*1000, qsort_time*1000