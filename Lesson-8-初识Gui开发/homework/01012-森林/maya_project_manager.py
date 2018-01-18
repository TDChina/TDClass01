# -*- coding: UTF-8 -*-
# Maya 2017+
# Qt.py module is required

import pymel.core as pm
from Qt.QtWidgets import *
from Qt.QtCore import *
from Qt.QtGui import *
import json
import os
import glob
import re


class Preference(object):

    def __init__(self):
        super(Preference, self).__init__()
        self.project_dir = r""  # 放置项目配置json的文件夹路径
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
        current_device_ratio = pm.PyNode(
            "defaultResolution").deviceAspectRatio.get()
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


class WindowUI(Preference, QWidget):

    #   有一个 Label，显示project_name
    #   有一个【Select Pref Directory】的button，点击后选择项目配置的存放文件夹
    #   有一个 ComboBox，里面是项目JSON文件的文件名，用户可以选择项目
    #   有一个【Refresh List】的button：按下后，调用refresh_list() 更新下拉列表
    #   有一个【SET!】的button：按下后，调用set_project_pref()应用设置，并更新project_name
    #   有一个【Save Current Pref】的button：按下后，提示输入project_name，然后调用save_current_pref()

    def __init__(self):
        super(WindowUI, self).__init__()

        # Project Name
        self.current_pj_name_label = QLabel(self.project_name)
        self.current_pj_name_label.setAlignment(Qt.AlignCenter)
        self.current_pj_name_label.setFont(QFont("", 20, QFont.Bold))
        # 设置项目pref存放文件夹
        self.pj_json_dir = QPushButton("Select Pref Directory")
        self.pj_json_dir.clicked.connect(self.set_pj_dir_btn_clicked)
        # label
        self.pj_name = QLabel("Project Name:")
        # 项目列表  combobox
        self.refresh_list()
        self.project_list_cb = QComboBox()
        pj_list_key = list(self.project_list_dict.keys())
        self.project_list_cb.addItems(pj_list_key)
        # set!  button
        self.set_pj_btn = QPushButton("SET!")
        self.set_pj_btn.clicked.connect(self.set_btn_clicked)
        # Refresh List  button
        self.refresh_btn = QPushButton("Refresh List")
        self.refresh_btn.clicked.connect(self.refresh_btn_clicked)
        # Save current pref  button
        self.save_current_json = QPushButton("Save Current Pref")
        self.save_current_json.clicked.connect(self.save_btn_clicked)
        # 使用说明
        self.help_btn = QPushButton("Help")
        self.help_btn.clicked.connect(self.help_clicked)

        self.init_ui()

    def init_ui(self):
        # UI窗口设置
        self.setWindowTitle("Project Manager")
        self.resize(300, 250)
        self.setMinimumSize(200, 250)
        self.setMaximumSize(500, 350)
        self.layout()
        self.show()

    def layout(self):
        main_layout = QVBoxLayout()
        pj_select_layout = QHBoxLayout()
        pj_set_layout = QHBoxLayout()

        main_layout.addWidget(self.current_pj_name_label)
        main_layout.addWidget(self.pj_json_dir)

        pj_select_layout.addWidget(self.pj_name)
        pj_select_layout.addWidget(self.project_list_cb)
        pj_select_layout.setStretch(1, 4)

        pj_set_layout.addWidget(self.refresh_btn)
        pj_set_layout.addWidget(self.set_pj_btn)

        main_layout.addLayout(pj_select_layout)
        main_layout.addLayout(pj_set_layout)
        main_layout.addWidget(self.save_current_json)
        main_layout.addWidget(self.help_btn)
        self.setLayout(main_layout)

    def set_pj_dir_btn_clicked(self):
        # 弹窗选择项目存放文件夹
        self.project_dir = QFileDialog.getExistingDirectory(
            self, "Please select json dir")
        # 刷新项目列表
        self.refresh_btn_clicked()

    def set_btn_clicked(self):
        # 判断当前项目是否可用
        if self.project_list_cb.currentText() == "":
            QMessageBox.warning(self, "Project Error", "Unavailable Project")
        else:
            project_file_path = self.project_list_dict[self.project_list_cb.currentText()]
        # 设置maya
            self.set_project_pref(project_file_path)
        # 刷新项目显示名称
            self.current_pj_name_label.setText(self.project_list_cb.currentText())
        # 提示修改成功
            QMessageBox.information(self, "Tip", "Success")

    def refresh_btn_clicked(self):
        # 刷新项目列表
        self.project_list_cb.clear()
        self.refresh_list()
        pj_list_key = list(self.project_list_dict.keys())
        self.project_list_cb.addItems(pj_list_key)

    def save_btn_clicked(self):
        # 判断项目文件夹是否存在
        path_exists = os.path.exists(self.project_dir)
        if path_exists:
            while True:
                # 弹窗提示输入project name
                pref_save_name, ok = QInputDialog.getText(
                    self,
                    "Name",
                    "Please enter project name:",
                    QLineEdit.Normal,
                    "enter project name here")

                if ok:
                    # 判断文件名是否为空
                    if pref_save_name.strip() != "":
                        # 非法字符替换为下划线
                        error_str = r"[\/\\\:\*\?\"\<\>\|]"
                        pref_save_name = re.sub(error_str, "_", pref_save_name)
                        # 调用save_current_pref保存
                        self.save_current_pref(pref_save_name)
                        # 提示成功
                        QMessageBox.information(self, "Tip", "Success")
                        # 更新项目列表和项目名
                        self.refresh_btn_clicked()
                        self.current_pj_name_label.setText(pref_save_name)
                        self.project_list_cb.setCurrentText(pref_save_name)
                        break
                    else:
                        # 提示文件名为空
                        QMessageBox.warning(
                            self, "Name Error", "Project name is empty")
                        continue
                else:
                    # Cancel
                    break
        else:
            # 项目路径不存在
            QMessageBox.warning(self, "Error", "Unavailable Project Path")

    def help_clicked(self):
        QMessageBox.about(self, "Help",
                          "<b>Select Pref Directory : </b> Select <i>project_pref_folder</i><br><br>"
                          "<b>Project Name : </b> Select correct project<br><br>"
                          "<b>Refresh List : </b> Refresh project list<br><br>"
                          "<b>SET! : </b> Apply pref to current maya file<br><br>"
                          "<b>Save Current Pref : </b> Save current maya perf to <i>project_pref_folder</i>")


if __name__ == "__main__":
    run = WindowUI()
