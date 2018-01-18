# coding=utf8
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore


class MyDialog(QtGui.QDialog):
    registered = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.setWindowTitle("Register Something")

        # 构建界面
        main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)

        head_layout = QtGui.QHBoxLayout()
        name_label = QtGui.QLabel("Name:")
        self.name_line_edit = QtGui.QLineEdit()
        head_layout.addWidget(name_label)
        head_layout.addWidget(self.name_line_edit)

        body_layout = QtGui.QHBoxLayout()
        sex_label = QtGui.QLabel()
        sex_label.setText("Gender:")
        self.sex_combobox = QtGui.QComboBox()
        body_layout.addWidget(sex_label)
        body_layout.addWidget(self.sex_combobox)

        foot_layout = QtGui.QHBoxLayout()
        id_label = QtGui.QLabel("ID:")
        self.id_line_edit = QtGui.QLineEdit()
        foot_layout.addWidget(id_label)
        foot_layout.addWidget(self.id_line_edit)

        button_layout = QtGui.QHBoxLayout()
        register_button = QtGui.QPushButton("Register")
        register_button.setObjectName("xxxx")
        cancel_button = QtGui.QPushButton("Cancel")
        button_layout.addWidget(register_button)
        button_layout.addWidget(cancel_button)

        main_layout.addLayout(head_layout)
        main_layout.addLayout(body_layout)
        main_layout.addLayout(foot_layout)
        main_layout.addLayout(button_layout)

        # 编辑界面内的数据
        self.sex_combobox.addItems(["male", "female"])

        # 信号连接
        cancel_button.clicked.connect(self.close)
        register_button.clicked.connect(self.do_register)
        self.registered.connect(self.registered_done)

    def do_register(self):
        name = self.name_line_edit.text()
        sex = self.sex_combobox.currentText()
        id_ = self.id_line_edit.text()
        if name and sex and id_:
            print "Registering: name is %s, sex is %s, id is %s" % (name, sex, id_)
            # Todo: 注册到数据库
            self.registered.emit(name)
        else:
            print "Warning: Something is not ready..."

    def registered_done(self, name):
        print "registered done, %s" % name

    def closeEvent(self, event):
        print "I am Closing..."

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F1:
            self.sex_combobox.setCurrentIndex(0)
        if event.key() == QtCore.Qt.Key_F2:
            self.sex_combobox.setCurrentIndex(1)


if __name__ == '__main__':
    app = QtGui.QApplication([])

    dialog = MyDialog()
    dialog.show()

    app.exec_()
