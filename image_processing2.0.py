import cv2
import numpy as np
import matplotlib.pyplot as plt
img = [cv2.imread(r"")]
testimg = cv2.imread(r"")
sampleset = []
for x in range(len(img)):
    height = np.size(img[x], 0)
    width = np.size(img[x], 1)
    size = height * width
    i = 0
    j = 0

    samplelist = []
    for i in range(height):
        for j in range(width):
