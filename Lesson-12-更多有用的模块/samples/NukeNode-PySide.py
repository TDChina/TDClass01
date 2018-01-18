import os
from PySide.QtGui import *

img = QImage(r"E:\_test\td_class\pikaqiu.jpg")
img = img.scaledToWidth(24)

width, height = img.width(), img.height()
scale = 255

for x in range(0, width):
    for y in range(0, height):
        c = img.pixel(x, y)
        r, g, b, a = QColor(c).getRgbF()
        r, g, b, a = r * scale, g * scale, b * scale, a * scale

        color = int('%02x%02x%02x%02x' % (r, g, b, a), 16)

        if r == g == b > 180:
            continue

        node = None
        node = nuke.createNode("Dot")
        node["tile_color"].getValue()
        node["tile_color"].setValue(int(color))
        node.setXpos(int(x * 10))
        node.setYpos(int(y * 10))
