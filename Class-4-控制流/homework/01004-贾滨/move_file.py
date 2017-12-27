# -*- coding: utf-8 -*-
# 移动文件到新的路径
import os
import shutil


# 传入老的文件路径 与新的文件夹路径
def move_file(old_path, new_dir):
    # 拆分获得文件名
    file_name = os.path.basename(old_path)
    # 判断老文件夹是否有 文件
    if os.path.isfile(old_path):
        # 组装新的文件路径
        new_file_path = new_dir + "\\" + file_name
        # 判断新文件夹是否有 相同文件 有移除
        if os.path.isfile(new_file_path):
            os.remove(new_file_path)
        # 移动文件
        shutil.move(old_path, new_dir)
        # 拆分获得文件名
        print "Success move '" + file_name + "' file"
    else:
        print "Error no '" + file_name + "' file"
    pass
