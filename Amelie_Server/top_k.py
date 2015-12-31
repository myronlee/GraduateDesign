__author__ = 'ligang'

import heapq

# top-k
def top_k_dists(dists, k):
    images = []
    for index, dist in enumerate(dists):
        images.append((index, dist))

    # heap = images[:k]
    # heapq.heapify(heap)

    # for i in xrange(k, len(images)):

    #     # if the dist is small than the current biggest dist, replace the biggest dist with this one
    #     if images[i].dist < heap[0].dist:
    #         biggest = heapq.heapreplace(heap, images[i])

    # top_k_images = sorted(heap, key=lambda x:x.dist)
    top_k_images = heapq.nsmallest(k, images, key=lambda x:x[1])

    # top_k_distances = []
    # for image in top_k_images:
    #     top_k_distances.append((image.name, image.dist))

    return top_k_images