# coding=utf8
import os
import shutil


def copy_file(src_dir, src_name, dst_dir):
    src_path = src_dir + os.sep + src_name
    dst_path = dst_dir + os.sep + src_name
    # 拷贝文件。
    shutil.copyfile(src_path, dst_path)


if __name__ == "__main__":
    copy_file(r"D:\Ben\Python\TDClass\lesson4\ic", "IC.0001.jpg", r"D:\Ben\Python\TDClass\lesson4\new_ic")
