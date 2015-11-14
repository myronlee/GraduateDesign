import numpy as np
import cv2
from matplotlib import pyplot as plt

# X = np.random.randint(25,50,(25,2))
# Y = np.random.randint(60,85,(25,2))
# Z = np.vstack((X,Y))
#
# # convert to np.float32
# Z = np.float32(Z)
#
# # define criteria and apply kmeans()
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
#
# # Now separate the data, Note the flatten()
# A = Z[label.ravel()==0]
# B = Z[label.ravel()==1]
#
# # Plot the data
# plt.scatter(A[:,0],A[:,1])
# plt.scatter(B[:,0],B[:,1],c = 'r')
# plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
# plt.xlabel('Height'),plt.ylabel('Weight')
# plt.show()

img = cv2.imread('8_1.jpg')
img2 = cv2.imread('8_2.jpg')

sift = cv2.SIFT()

kp, des = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(img2, None)

k = 100
attempts = 100
eps = 10.0

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, attempts, eps)
ret, label, center = cv2.kmeans(np.vstack((des,des2)), k, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)

x = 0