# -*- coding: UTF-8 -*-

from pack_copy import copy_file as cf
import pymel.core as pm
import os


def batch_copy_textures(dst_dir, use_new_path=False):
    """
    批量复制file节点的贴图文件
    Args:
        dst_dir: 填写需要复制到的目标文件夹路径
        use_new_path: 是否使用新路径替换file节点路径 True/False

    Returns:
        返回一个字典 {file节点: copy的贴图路径}
    """
    # 检测dst_dir路径是否存在,不存在就新建文件夹
    dir_is_exists = os.path.exists(dst_dir)
    if not dir_is_exists:
        os.makedirs(dst_dir)

    # 列出所有file节点
    all_file_texture_nodes = pm.ls(type="file")
    all_texture_name = []
    file_node_new_path = {}
    # 遍历所有file节点
    for file_node in all_file_texture_nodes:
        file_path = file_node.fileTextureName.get()
        file_name = os.path.basename(file_path)
        all_texture_name.append(file_name)

        file_node_exists = os.path.exists(file_path)    # 跳过丢失的贴图
        if file_node_exists:
            # 复制贴图到新路径
            set_path = cf.copy_file(file_path, dst_dir)
            # 指定file节点路径到新路径
            if use_new_path:
                file_node.fileTextureName.set(set_path)
            file_node_new_path[file_node] = set_path    # file节点：copy的贴图路径
        else:
            print '*** TEXTURE FILE NOT FOUND ***  [ Node_name: %s , File_Path: %s ]' % (file_node, file_path)
            file_node_new_path[file_node] = 'miss file'  # file节点：'miss file'
    return file_node_new_path


if __name__ == '__main__':
    test_dir = r'dir'
    batch_copy_textures(test_dir, True)
