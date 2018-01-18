import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import maya.cmds as mc
import maya.mel as mel

img = QImage(r"E:\_test\td_class\pikaqiu.jpg")
img = img.scaledToWidth(50)

width, height = img.width(), img.height()
scale = 1

for x in range(0, width):
    for y in range(0, height):
        c = img.pixel(x, y)
        r, g, b, a = QColor(c).getRgbF()  # float  0-1 0-255
        r, g, b, a = r * scale, g * scale, b * scale, a * scale

        color = int('%02x%02x%02x%02x' % (r, g, b, a), 16)

        if r == g == b > 180:
            continue

        # node create
        cube = mc.polyCube()
        mel.eval("scale %s %s %s " % (r, g, b))
        mel.eval("move %s %s %s" % (x * 2, 0, y * 2))
