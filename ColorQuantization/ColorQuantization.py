# IMAGE CLUSTERING
import numpy as np
import os
import cv2
import sys

#Imgae clustering function
def cluster_image(img_id):
    imageName = 'image_' + str(img_id) + '.jpg'
    image = cv2.imread(imageName)
    reshape = image.reshape((-1, 3))
    reshape = np.float32(reshape)
    # So in this we have defined the number of clusters and the k-means that should be performed.
    value = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    K_value = 3
    #Choosend random centers
    ret, label, center = cv2.kmeans(reshape, K_value, None, value, 10, cv2.KMEANS_RANDOM_CENTERS)
    # this should be converted into the orginal image
    center = np.uint8(center)
    #flatterning the image
    res = center[label.flatten()]
    result = res.reshape(image.shape)
    cv2.imwrite(os.path.join(directory, imageName), result)
    print('Clustering is done for the image ' + imageName)

#Main mrthod that checks if the directory already exists or not.
if __name__ == '__main__':
    directory = 'quantizedImages'
    if not os.path.exists(directory):
        os.mkdir(directory)
        for image_id in range(1, 4):
         cluster_image(image_id)
    else:
        print("remove directory")
