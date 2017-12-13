from maya import cmds

cube = cmds.polyCube()
cubeShape = cube[0]
#print (cube)
#可以用print来检查cube里包含的东西，这里的cube是一个list。
#type (cubeShape)
#可用type来查看物体的类型。
circle = cmds.circle()
circleShape = circle[0]

cmds.parent(cubeShape, circleShape)

cmds.setAttr(cubeShape+".translate", lock=True)
cmds.setAttr(cubeShape+".rotate", lock=True)
cmds.setAttr(cubeShape+".scale", lock=True)

cmds.select(circleShape)
