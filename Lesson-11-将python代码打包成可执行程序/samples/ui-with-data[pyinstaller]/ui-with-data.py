import sys
import os
from PySide.QtCore import *
from PySide.QtGui import *

if __name__ == "__main__":

    def resource_path(relative_path):
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    app = QApplication(sys.argv)
    label = QLabel()
    label.setPixmap(QPixmap(resource_path("pikaqiu.jpg")))
    label.show()
    sys.exit(app.exec_())
