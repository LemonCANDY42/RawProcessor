# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 17:26
# @Author  : Kenny Zhou
# @FileName: raw2png.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com
import cv2
import numpy as np
from PIL import Image

if __name__ == '__main__':
	path = "/Users/kennymccormick/github/mario/08_20_14_902.raw"
	width = 640
	height = 480

	with open(path, "rb") as rawimg:
		rawimg_np = np.fromfile(rawimg, np.dtype('u2'), width * height).reshape(height, width)
		print(rawimg_np.dtype)
		img = Image.fromarray(rawimg_np, mode='I;16')
		img.save('test.png')

