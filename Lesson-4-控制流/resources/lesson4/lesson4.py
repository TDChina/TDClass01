from random import randint
import pymel.core as pm
import mtoa.utils as mutils

mutils.createLocator("aiSkyDomeLight", asLight=True)

for i in range(12):
    box = pm.polyCube(ch=0)[0]
    box.translate.set(randint(-20, 20), randint(-20, 20), randint(-20, 20))
    scale = randint(1, 5)
    box.scale.set(scale, scale, scale)
    shader = pm.shadingNode('aiStandard', asShader=True)
    pm.select(box)
    pm.hyperShade(assign=shader)
    file_node = pm.createNode("file")
    file_node.fileTextureName.set("C:/Users/strack/Pictures/ic/IC.%04d.jpg" % (i+1))
    file_node.outColor >> shader.color
