# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os
import shutil

# **输入新路径**
new_path = u"C:/Users/bin/GitTD/TDClass01/Class-4-控制流/homework/01004-贾滨/new_texture_file"
all_file_node = cmds.ls(typ="file")
for all_file_node in all_file_node:
    file_texture_name = all_file_node + ".fileTextureName"
    old_path_file = cmds.getAttr(file_texture_name)  # 获取老的路径
    old_file = os.path.basename(old_path_file)  # 拆分获得路径
    new_path_file = new_path + "/" + old_file
    if os.path.isfile(new_path_file):  # 判断是否有相同文件
        os.remove(new_path_file)  # 移除
    shutil.move(old_path_file, new_path)  # 移动到新的路径
    cmds.setAttr(file_texture_name, new_path + "/" + old_file, type="string")  # 从新指定贴图
