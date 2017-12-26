# -*- coding: utf-8 -*-
import os
import shutil
import string
import nukescripts as nsp


def old_material_path(node_name):   # 通过选择的节点，读取该节点导入的文件路径
    node_file_path = node_name['file'].getValue()
    return node_file_path


def move_material_path(old_path, new_path):    # 检测素材是单帧或者序列并将文件拷贝到新路径
    if old_path.find('%04d') != -1:
        old_path = os.path.dirname(old_path)
    shutil.move(old_path, new_path)


def change_node_file_path(old_path, node_name, new_path):   # 检测素材是单帧或者序列并将新路径与素材名称连接起来
    if old_path.find('%04d') != -1:
        new_path = new_path + '/' + os.path.basename(os.path.dirname(old_path)) + '/' + os.path.basename(old_path)
    else:
        new_path = new_path + '/' + os.path.basename(old_path)
    node_name['file'].setValue(new_path)


def translation_str(in_new_path, intab, outtab):    # 转换路径分隔符，因nuke直接用原始字符串会出bug，因此有这一步
    trantab = string.maketrans(intab, outtab)
    new_str = in_new_path.translate(trantab)
    return new_str


def move_readnode_material_path(new_material_path):
    all_read_node = nsp.nuke.allNodes('Read')
    for node in all_read_node:
        move_material_path(old_material_path(node), translation_str(new_material_path, '\\', '/'))
        change_node_file_path(old_material_path(node), node, translation_str(new_material_path, '\\', '/'))
    print('pass')


 #  move_readnode_material_path(r'C:\Users\iw12104\Pictures\test')


