# -*- coding: utf-8 -*-
# @File    : faceCombo
# @Author  : cgpengda

from maya import cmds
from maya import OpenMayaUI

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2 import __version__
    from shiboken2 import wrapInstance
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide import __version__
    from shiboken import wrapInstance

_win = 'faceCombo'
maya_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
maya_window = wrapInstance(long(maya_window_ptr), QWidget)


class FaceCombo(QMainWindow):
    def __init__(self, parent=maya_window):
        super(FaceCombo, self).__init__(parent)
        self.setWindowFlags(Qt.Window)
        self.setObjectName(_win)
        self.setWindowTitle("Face Combo V2.0")
        self.setMinimumSize(QSize(360, 480))
        self.setStyleSheet("font: 10pt;")
        self.resize(360, 480)
        # Layout
        self.central_widget = QWidget()
        self.gridLayout01 = QGridLayout(self.central_widget)
        self.target_scrollArea = QScrollArea(self.central_widget)
        self.target_widgetContents = QWidget()
        self.gridLayout02 = QGridLayout(self.target_widgetContents)
        self.target_layout = QHBoxLayout()
        self.first_layout = QVBoxLayout()
        self.second_layout = QVBoxLayout()
        self.button_layout01 = QHBoxLayout()
        self.button_layout02 = QHBoxLayout()
        # Widget
        self.target_label = QLabel("Target List")
        self.first_target_list = QListWidget()
        self.first_target_spin = QDoubleSpinBox()
        self.line = QFrame()
        self.second_target_list = QListWidget()
        self.second_target_spin = QDoubleSpinBox()
        self.combo_label = QLabel("Combo List")
        self.combo_list = QListWidget()
        self.create_button = QPushButton("Create")
        self.create_close_button = QPushButton("Close")
        self.edit_button = QPushButton("Edit")
        self.edit_close_button = QPushButton("Close")
        self.delete_button = QPushButton("Delete")
        self.mirror_button = QPushButton("Mirror")
        # Set widget
        self.central_widget.setFocusPolicy(Qt.NoFocus)
        self.gridLayout01.setContentsMargins(5, 5, 5, 5)
        self.gridLayout01.setSpacing(5)
        self.target_scrollArea.setWidget(self.target_widgetContents)
        self.target_scrollArea.setWidgetResizable(True)
        self.target_scrollArea.setFocusPolicy(Qt.NoFocus)
        self.gridLayout02.setContentsMargins(2, 5, 2, 5)
        self.gridLayout02.setSpacing(5)
        self.target_label.setAlignment(Qt.AlignCenter)
        self.first_target_list.setFocusPolicy(Qt.NoFocus)
        self.first_target_spin.setReadOnly(True)
        self.first_target_spin.setEnabled(False)
        self.first_target_spin.setMaximum(1)
        self.first_target_spin.setMinimum(0)
        self.first_target_spin.setDecimals(3)
        self.first_target_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.second_target_list.setFocusPolicy(Qt.NoFocus)
        self.second_target_spin.setReadOnly(True)
        self.second_target_spin.setEnabled(False)
        self.second_target_spin.setMaximum(1)
        self.second_target_spin.setMinimum(0)
        self.second_target_spin.setDecimals(3)
        self.second_target_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.combo_label.setAlignment(Qt.AlignCenter)
        self.combo_list.setFocusPolicy(Qt.NoFocus)
        self.create_button.setMinimumSize(QSize(0, 30))
        self.create_close_button.setMinimumSize(QSize(0, 30))
        self.create_close_button.hide()
        self.edit_button.setMinimumSize(QSize(0, 30))
        self.edit_close_button.setMinimumSize(QSize(0, 30))
        self.edit_close_button.hide()
        self.delete_button.setMinimumSize(QSize(0, 30))
        self.mirror_button.setMinimumSize(QSize(0, 30))
        # Set layout
        self.setCentralWidget(self.central_widget)
        self.gridLayout01.addWidget(self.target_scrollArea, 0, 0, 1, 1)
        self.gridLayout01.addLayout(self.button_layout01, 1, 0, 1, 1)
        self.gridLayout01.addLayout(self.button_layout02, 2, 0, 1, 1)
        self.gridLayout02.addLayout(self.target_layout, 0, 0, 1, 1)
        self.target_layout.addLayout(self.first_layout)
        self.target_layout.addLayout(self.second_layout)
        self.first_layout.addWidget(self.target_label)
        self.first_layout.addWidget(self.first_target_list)
        self.first_layout.addWidget(self.first_target_spin)
        self.first_layout.addWidget(self.line)
        self.first_layout.addWidget(self.second_target_list)
        self.first_layout.addWidget(self.second_target_spin)
        self.second_layout.addWidget(self.combo_label)
        self.second_layout.addWidget(self.combo_list)
        self.button_layout01.addWidget(self.create_button)
        self.button_layout01.addWidget(self.create_close_button)
        self.button_layout01.addWidget(self.edit_button)
        self.button_layout01.addWidget(self.edit_close_button)
        self.button_layout02.addWidget(self.delete_button)
        self.button_layout02.addWidget(self.mirror_button)
        # Menu
        self.menu = QMenuBar(self)
        self.edit_menu = QMenu("Edit")
        self.help_menu = QMenu("Help")
        self.load_blendshape_action = QAction("Load Blendshape")
        self.create_combo_action = QAction("Create Combo", self)
        self.edit_combo_action = QAction("Edit Combo", self)
        self.delete_combo_action = QAction("Delete Target", self)
        self.mirror_combo_action = QAction("Mirror Target", self)
        self.updata_combo_action = QAction("Updata Combo", self)
        self.about_tools_action = QAction("About Tools", self)
        self.about_author_action = QAction("About Author", self)
        self.setMenuBar(self.menu)
        self.edit_menu.addAction(self.load_blendshape_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.create_combo_action)
        self.edit_menu.addAction(self.edit_combo_action)
        self.edit_menu.addAction(self.delete_combo_action)
        self.edit_menu.addAction(self.mirror_combo_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.updata_combo_action)
        self.help_menu.addAction(self.about_tools_action)
        self.help_menu.addAction(self.about_author_action)
        self.menu.addAction(self.edit_menu.menuAction())
        self.menu.addAction(self.help_menu.menuAction())


def main():
    if cmds.window(_win, exists=True):
        cmds.deleteUI(_win, window=True)
    win = FaceCombo()
    win.show()


if __name__ == '__main__':
    main()
