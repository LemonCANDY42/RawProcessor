# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 10:50
# @Author  : Kenny Zhou
# @FileName: check_bit.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

if __name__ == "__main__":

	# 读入图片：默认彩色图，cv2.IMREAD_GRAYSCALE灰度图，cv2.IMREAD_UNCHANGED包含alpha通道
	path = "/Users/kennymccormick/Downloads/WXWork Files/Caches/Images/2023-05/ea15bcfa32877b352cc2e00e6eb420a2_HD/1656507331715334146.jpg"
	plt.figure('图片显示')
	img = cv2.imread(path, cv2.CV_16UC1)
	print(img.dtype)
	print(img.shape)
	plt.imshow(img, cmap='gray')
	plt.show()
