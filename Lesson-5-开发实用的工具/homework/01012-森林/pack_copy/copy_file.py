# -*- coding: UTF-8 -*-

import shutil
import os


def copy_file(scr_path, dst_dir):
    """
    拷贝文件到目标目录
    如果出现同名文件，但是内容不同，则改名复制该文件并输出提示
    Args:
        scr_path: 原始文件path
        dst_dir: 目标目录

    Returns:
        返回新目录文件的path
    """
    # 去除首尾空格和尾部"\"
    dst_dir = dst_dir.strip()
    dst_dir = dst_dir.rstrip('\\')

    # 检测同名文件 对比文件大小，改名复制
    file_name = os.path.basename(scr_path)
    new_file_path = os.path.join(dst_dir, file_name)
    file_is_exists = os.path.exists(new_file_path)
    if file_is_exists:
        if os.path.getsize(scr_path) != os.path.getsize(new_file_path):
            file_base_name, file_extend = os.path.splitext(file_name)   # 拆分文件名 扩展名
            file_new_name = file_base_name + '_re' + file_extend
            dst_path = dst_dir + '\\' + file_new_name
            shutil.copy(scr_path, dst_path)
            print 'Found same name file, The new one renamed: %s' % file_new_name
            return dst_path
        else:
            return new_file_path
    else:
        shutil.copy(scr_path, dst_dir)
        return new_file_path


if __name__ == "__main__":
    pass
