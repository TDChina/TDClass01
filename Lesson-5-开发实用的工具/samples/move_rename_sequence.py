# coding=utf8
# Copyright (c) 2017 CineUse
import os
import glob


def rename_sequence(sequence_path, src_naming, dst_naming, start_frame):
    # 名称描述规则： 用 ???? 来表示 0001 这样的数字
    # 在传入的路径下列举所有符合src_naming的文件
    glob_path = os.path.join(sequence_path, src_naming)
    sequence_file_list = glob.glob(glob_path)
    # 将文件名替换为新的规则
    current_frame = start_frame
    for sequence_file in sequence_file_list:
        # 获取新的文件名
        new_file_name_template = os.path.join(sequence_path, dst_naming)
        number_count = new_file_name_template.count("?")
        new_file_name_template = new_file_name_template.replace("?"*number_count, "%05d")
        new_file_name = new_file_name_template % current_frame
        # 修改文件名
        os.rename(sequence_file, new_file_name)
        # 自增current_frame
        current_frame += 1


if __name__ == '__main__':
    rename_sequence(r"E:\td_class_workspace\lesson4\ic", "IC.????.jpg", "icons_?????.jpg", 1001)
