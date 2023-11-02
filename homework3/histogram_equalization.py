import cv2
import numpy as np
from matplotlib import pyplot as plt


# 获取灰度图像
img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("lennagray",gray) # 图片名称 和 图像显示

# 灰度图像的直方图 方法一
plt.figure()
plt.hist(gray.ravel(),256)
plt.show()


# 灰度图像的直方图 方法二
hist =cv2.calcHist([gray],[0],None,[256],[0,256]) # images   channels(灰度图为0，彩色为0,1,2)   mask(一般为none)  histSize(Bin的数目)  BINS(每个像素值的像素数)   
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()


# 彩色图像直方图
chans=cv2.split(img)
colors = ("b","g","r")
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (chan,color) in zip(chans,colors):
    hist=cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])
plt.show()

