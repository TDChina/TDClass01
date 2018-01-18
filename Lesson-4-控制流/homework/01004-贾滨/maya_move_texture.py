# -*- coding: utf-8 -*-
# 复制到 Maya Python里执行
import pymel.core as pm
import os
import sys
sys.path.append(r"d:\Users\bin\Desktop\maya_move_texture")
import move_file
reload(move_file)


# 新的文件夹位置
new_texture_dir = r"d:\Users\bin\Desktop\maya_move_texture\new_texture"
file_node_ls = pm.ls(typ="file")
for old_file_node in file_node_ls:
    # 获取老贴图路径
    file_texture = old_file_node + ".fileTextureName"
    old_texture_path = pm.getAttr(file_texture)
    # 移动文件
    move_file.move_file(old_texture_path, new_texture_dir)
    # 拆分获得文件名
    file_name = os.path.basename(old_texture_path)
    # 从新制定新文件路径路径
    pm.setAttr(file_texture, new_texture_dir + "/" + file_name, type="string")
