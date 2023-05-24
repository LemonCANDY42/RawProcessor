# -*- coding: utf-8 -*-
# @Time    : 2023/5/24 11:09
# @Author  : Kenny Zhou
# @FileName: ergodic_process_files.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

from pathlib import Path
def process_folder(folder,suffix,func,func_args:dict= {}):
    # 遍历文件夹中的所有png文件
    results_dict = {}
    for filename in folder.iterdir(): # 使用Path对象的iterdir方法来遍历目录下的文件和子目录
        if suffix:
            if filename.suffix == suffix: # 使用Path对象的suffix属性来获取文件后缀名
                # 处理单个文件
                result = func(filename,**func_args)
                results_dict[filename] = result
        else:
            # 处理单个文件
            result = func(filename,**func_args)
            results_dict[filename] = result

    return results_dict