import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

filepath1="/data/outputs/{name}"
a = os.path.basename(filepath1)
b= a.split('.')[0]
img = cv2.imread('D:\\papers\\paddle4ui\\data\\output\\1\\7.png')  # 0表示灰度图
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.show()
hist = cv2.calcHist([img], [0], None, [2], [0, 256])
hist /= hist.sum()
print(hist[0][0])
print(hist[1][0])
hist_point=hist[1][0]
H, S, V = cv2.split(img)
v = V.ravel()[np.flatnonzero(V)]   #亮度非零的值
average_v  = sum(v)/len(v)
print(average_v)