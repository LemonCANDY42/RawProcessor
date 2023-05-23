# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 10:54
# @Author  : Kenny Zhou
# @FileName: depth_image_enhancer.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

import imageio
import numpy as np
import cv2
from pathlib import Path # 导入pathlib模块

# 定义参数
min_depth = 1000 # 深度数据的最小值
max_depth = 5000 # 深度数据的最大值
ratio = 0.33 # 添加深度数据的比例
smooth = True # 是否平滑添加的像素
random_point = True

# 定义一个函数，用于处理单个文件
def process_file(filepath):
    # 读取png文件，并转换为numpy数组
    img = imageio.v2.imread(filepath)

    if random_point:
        # 找到数组中数值为0的位置
        zero_mask = img == 0
        # 从这些位置中随机选择一定比例的位置
        random_mask = np.random.choice([True, False], size=zero_mask.shape, p=[ratio, 1-ratio])
        # 得到最终要添加深度数据的位置
        add_mask = np.logical_and(zero_mask, random_mask)
        # 从正态分布中生成相应数量和区间的随机数，并赋值给这些位置
        img[add_mask] = np.random.normal(loc=(min_depth+max_depth)/2, scale=(max_depth-min_depth)/6, size=add_mask.sum()).astype(np.uint16)

    else:
        # 获取图像的高度和宽度
        h, w = img.shape[:2]
        # 计算要覆盖的区域的高度和宽度
        h_cover = int(h * ratio)
        w_cover = int(w * ratio)
        # 随机选择一个左上角的坐标作为覆盖区域的起点
        x = np.random.randint(0, w - w_cover)
        y = np.random.randint(0, h - h_cover)
        # 从正态分布中生成相应数量和区间的随机数，并赋值给覆盖区域
        img[y:y + h_cover, x:x + w_cover] = np.random.normal(loc=(min_depth + max_depth) / 2, scale=(max_depth - min_depth) / 6,
                                                             size=(h_cover, w_cover)).astype(np.uint16)

    # 如果需要平滑添加的像素，可以使用中值滤波器和膨胀操作
    if smooth:
        img = cv2.medianBlur(img, 5)
        kernel = np.ones((3,3),np.uint8)
        img = cv2.dilate(img,kernel,iterations = 1)
    # 返回处理后的数组
    return img

# 定义一个函数，用于遍历指定文件夹并重复上述操作
def process_folder(folder):
    # 遍历文件夹中的所有png文件
    for filename in folder.iterdir(): # 使用Path对象的iterdir方法来遍历目录下的文件和子目录
        if filename.suffix == '.png': # 使用Path对象的suffix属性来获取文件后缀名
            # 处理单个文件，并得到处理后的数组
            img = process_file(filename)
            # 保存处理后的文件到另一个文件夹（假设是'processed_images'）
            new_folderpath = folder / 'processed_images'
            new_folderpath.mkdir(parents=False, exist_ok=True)
            file_prexif = 'enhancer'
            new_filepath = new_folderpath / new_folderpath.joinpath(f'{file_prexif}_{filename.name}') # 使用Path对象的/运算符来拼接路径

            imageio.imwrite(new_filepath, img)

if __name__ == "__main__":
    # 调用函数，处理指定文件夹
    process_folder(Path('/Users/kennymccormick/Downloads/煤坑测高识别'))
