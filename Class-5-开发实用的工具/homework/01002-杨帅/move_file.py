# coding=utf8
# Copyright (C) 2017 David
# 2018/1/1


import os
import shutil

def move_file(src_path, dst_dir):
    # 提取src_path的文件名src_name
    src_name = os.path.split(src_path)[1]
    # 根据src_path的文件名src_name和dst_dir组装成dst_path
    dst_path = os.path.join(dst_dir, src_name)
    # 把文件从src_path移动到dst_dir
    shutil.move(src_path,dst_path)
    return dst_path

if __name__ == '__main__':
    move_file()