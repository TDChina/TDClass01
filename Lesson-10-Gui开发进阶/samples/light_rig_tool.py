# coding=utf8
# Copyright (c) 2017 CineUse

from PySide2 import QtWidgets
from PySide2 import QtCore
import pymel.core as pm
from maya import OpenMayaUI
from shiboken2 import wrapInstance


class LightModel(QtCore.QAbstractItemModel):
    def __init__(self):
        super(LightModel, self).__init__()

        self.__all_lights = pm.ls(lights=True)

    def rowCount(self, *args, **kwargs):
        return len(self.__all_lights)

    def columnCount(self, *args, **kwargs):
        return 5

    def data(self, index, role):
        """
        在界面自动刷新时运行，不同的role决定不同的信息
        Args:
            index: QIndex，索引，包含行数信息
            role: int，Qt的数据规则

        Returns:

        """
        row = index.row()
        column = index.column()
        light_info = self.__all_lights[row]
        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return light_info.name()

    def update_data(self, all_lights):
        """
        更新所有的灯光信息
        Args:
            all_lights:

        Returns:

        """
        self.beginInsertRows(QtCore.QModelIndex(), 0, len(all_lights)-1)
        self.__all_lights[:] = all_lights
        self.endInsertRows()


class LightTable(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super(LightTable, self).__init__(parent)

        self.model = LightModel()

        self.setModel(self.model)

        #
        self.verticalHeader().setVisible(False)  # hide vertical header
        # self.setSelectionBehavior(self.upload_table.SelectRows)  # select rows
        self.resizeColumnsToContents()
        # self.horizontalHeader().setResizeMode(0, QtWidgets.QHeaderView.Stretch)  # stretch first column



class LightRigToolUi(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LightRigToolUi, self).__init__(parent)

        # init attributes
        self.__all_lights = []

        # make widgets
        main_layout = QtWidgets.QVBoxLayout(self)
        self.light_list = LightTable()
        refresh_button = QtWidgets.QPushButton("Refresh")
        export_button = QtWidgets.QPushButton("Export")
        cancel_button = QtWidgets.QPushButton("Cancel")
        # setup layout
        main_layout.addWidget(self.light_list)
        main_layout.addWidget(refresh_button)
        main_layout.addWidget(export_button)
        main_layout.addWidget(cancel_button)

        # connections
        refresh_button.clicked.connect(self.update_all_lights)
        cancel_button.clicked.connect(self.close)

    def update_all_lights(self):
        """
        更新列表中的灯光信息
        Returns:

        """
        # 获取场景中的灯光列表
        self.__all_lights = pm.ls(lights=True)
        # 更新model中的内容
        self.light_list.model.update_data(self.__all_lights)


def main():
    global tool_ui
    maya_win = get_maya_window()
    tool_ui = LightRigToolUi(maya_win)
    tool_ui.show()


def get_maya_window():
    maya_window = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(maya_window), QtWidgets.QWidget)