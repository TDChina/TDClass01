# encoding: utf-8

import sys
from PySide import QtGui

if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    
    win = QtGui.QMainWindow()
	win.show
    
    app.exec_()
    sys.exit()