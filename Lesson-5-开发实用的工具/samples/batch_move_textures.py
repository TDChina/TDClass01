# coding=utf8
# Copyright (c) 2017 CineUse
import pymel.core as pm
import move_file as mf


def batch_move_textures(dst_dir):
    # 获取所有的File节点
    all_file_texture_nodes = pm.ls(type="file")
    # 循环
    for file_node in all_file_texture_nodes:
        # 获取当前节点的贴图路径信息
        file_path = file_node.fileTextureName.get()
        # 移动并改名这个贴图文件
        new_path = mf.move_file(file_path, dst_dir)
        # 修改节点贴图路径属性
        file_node.fileTextureName.set(new_path)
    pass


if __name__ == "__main__":
    batch_move_textures("")
