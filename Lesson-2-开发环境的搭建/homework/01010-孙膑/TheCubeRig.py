from maya import cmds

cube = cmds.polyCube()
cubeShape = cube[0]
#print (cube)
#������print�����cube������Ķ����������cube��һ��list��
#type (cubeShape)
#����type���鿴��������͡�
circle = cmds.circle()
circleShape = circle[0]

cmds.parent(cubeShape, circleShape)

cmds.setAttr(cubeShape+".translate", lock=True)
cmds.setAttr(cubeShape+".rotate", lock=True)
cmds.setAttr(cubeShape+".scale", lock=True)

cmds.select(circleShape)
