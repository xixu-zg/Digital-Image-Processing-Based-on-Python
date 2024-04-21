import cv2
import matplotlib.pyplot as plt
import math
import numpy as np


def createBox():
    box = np.zeros((100, 100), np.uint8) + 255
    print(type(box))
    shape = box.shape
    box = cv2.circle(box, (30, 50), 25, 0, -1)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if j in range(45, 95) and i in range(25, 75):
                box[i, j] = 195
    return box


def histogram(image):
    (row, col) = image.shape
    hist = [0] * 256
    for i in range(row):
        for j in range(col):
            hist[image[i, j]] += 1
    return hist


image0 = createBox()
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(image0, vmin=0, vmax=255, cmap=plt.cm.gray)
plt.title("idel image")
image_hist0 = histogram(image0)
plt.subplot(1, 2, 2)
plt.bar(range(256), image_hist0)
plt.show()