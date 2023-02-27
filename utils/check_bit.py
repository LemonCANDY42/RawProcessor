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
	path = "/Users/kennymccormick/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/83fca783a6b126dc3ae61fdd7d0090ea/Message/MessageTemp/6f800cc992ac371b552ced4d7b07c850/File/2018-03-04/09_05_19_277.png"
	plt.figure('图片显示')
	img = cv2.imread(path, cv2.CV_16UC1)
	print(img.dtype)
	print(img.shape)
	plt.imshow(img, cmap='gray')
	plt.show()
