# coding=utf8
import os
import pymel.core as pm
import copy_file as cf


def bach_move_file():
    # input dst_dir
    dst_dir = r"D:\Ben\Python\TDClass\lesson4\new_ic"    # FIXME
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    # 找出贴图文件节点
    all_file_nodes = pm.ls( type = 'file' )
    # 循环提取加修改
    for file_node in all_file_nodes:
        # 在节点里提取文件路径
        file_path = file_node.fileTextureName.get()
        # 把文件路径分解为 路径："scr_dir" 文件名：“scr_name"
        scr_dir, scr_name = os.path.split(file_path)
        # 调用 copy_file 拷贝文件
        cf.copy_file(scr_dir, scr_name, dst_dir)
        # set path to destination directory
        file_node.fileTextureName.set( dst_dir + os.sep + scr_name )




if __name__ == '__main__':
    pass