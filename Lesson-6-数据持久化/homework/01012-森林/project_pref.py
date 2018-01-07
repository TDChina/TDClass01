# -*- coding: UTF-8 -*-
import pymel.core as pm
import json
import os
import glob


class Preference(object):

    def __init__(self):
        self.project_dir = r"project_dir"   # 放置项目配置json的文件夹路径
        self.project_list_dict = {}  # 这是一个字典：{项目文件名：项目文件路径}
        self.project_name = "None"  # 项目名字

    @staticmethod
    def save_pref(project_file_path):
        """
        读取当前maya文件的配置，并保存JSON文件
        Args:
            project_file_path: 被保存JSON的文件的路径

        Returns:
            无

        """
        # 读取当前文件配置
        current_time_unit = pm.currentUnit(query=True, time=True)
        current_res_width = pm.PyNode("defaultResolution").width.get()
        current_res_height = pm.PyNode("defaultResolution").height.get()
        current_device_ratio = pm.PyNode("defaultResolution").deviceAspectRatio.get()
        current_pixel_ratio = pm.PyNode("defaultResolution").pixelAspect.get()
        current_pref = {
            "time_unit": current_time_unit,
            "res_width": current_res_width,
            "res_height": current_res_height,
            "res_device_ratio": current_device_ratio,
            "res_pixel_ratio": current_pixel_ratio}

        current_conf = json.dumps(current_pref, sort_keys=True, indent=4)

        # 写入当前配置到文件
        with open(project_file_path, "w") as current_pref_file:
            current_pref_file.write(current_conf)

    @staticmethod
    def set_pref(project_file_path):
        """
        读取JSON文件，并应用到maya
        Args:
            project_file_path:被读取的JSON的文件的路径

        Returns:
            无
        """
        # 提取项目的配置文件
        with open(project_file_path, "r") as read_conf_file:
            current_conf_file_read = read_conf_file.read()
            current_conf_read = json.loads(current_conf_file_read)

        set_time_unit = current_conf_read["time_unit"]
        set_res_w = current_conf_read["res_width"]
        set_res_h = current_conf_read["res_height"]
        set_device_ratio = current_conf_read["res_device_ratio"]
        set_pixel_ratio = current_conf_read["res_pixel_ratio"]

        # 以配置文件设置maya
        pm.currentUnit(time=set_time_unit)
        pm.PyNode("defaultResolution").deviceAspectRatio.set(set_device_ratio)
        pm.PyNode("defaultResolution").pixelAspect.set(set_pixel_ratio)
        pm.PyNode("defaultResolution").width.set(set_res_w)
        pm.PyNode("defaultResolution").height.set(set_res_h)


class WindowUI(Preference):

    # 假装这里有一段GUI代码：
    #   有一个 文本框，显示project_name
    #   有一个 下拉列表，里面是项目JSON文件的文件名，用户可以选择项目
    #   有一个【刷新项目列表】的button：按下后，调用refresh_list() 更新下拉列表
    #   有一个【应用该项目配置】的button：按下后，调用set_project_pref()应用设置，并更新project_name
    #   有一个【保存当前配置】的button：按下后，提示输入project_name，然后调用save_current_pref()

    def refresh_list(self):
        """
        刷新项目列表
        Returns:
            返回项目列表的字典
        """
        self.project_list_dict = {}
        json_filter = self.project_dir + "\\" + "*.json"  # 过滤非json文件
        project_list = glob.glob(json_filter)
        # 更新字典
        for i in project_list:
            base_name = os.path.basename(i)
            name = os.path.splitext(base_name)[0]
            self.project_list_dict[name] = i
        return self.project_list_dict

    def save_current_pref(self, project_name):
        """
        保存保存当前文件的配置到project_dir
        Args:
            project_name: 项目的名字

        Returns:
            返回project_name
        """
        project_file_name = project_name + ".json"
        project_file_path = os.path.join(self.project_dir, project_file_name)
        self.save_pref(project_file_path)
        return project_name

    def set_project_pref(self, project_file_path):
        """
        应用项目JSON文件配置
        Args:
            project_file_path: 项目JSON文件的路径

        Returns:
            返回project_name
        """
        self.set_pref(project_file_path)
        project_file_name = os.path.basename(project_file_path)
        project_name = os.path.splitext(project_file_name)[0]
        self.project_name = project_name
        return project_name


if __name__ == "__main__":

    test = WindowUI()
    test.project_dir = r"F:\temp"  # 指路经
    test.refresh_list()  # 刷新项目列表
    print test.project_list_dict  # 打印当前项目列表字典

    test.save_current_pref("project01")  # 保存当前maya的JSON文件，并命名为"project01"
    test.refresh_list()  # 刷新项目列表
    test.set_project_pref(test.project_list_dict["project01"])  # 应用"project01"的配置到当前maya文件
