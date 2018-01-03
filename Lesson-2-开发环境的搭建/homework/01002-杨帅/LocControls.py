#这是一个定位骨骼控制器的小插件
#先选骨骼，再加选控制器的组，执行代码即可定位控制器
import maya.cmds as mc
selected = mc.ls(sl=1)
mc.delete(mc.parentConstraint(selected[0],selected[1],mo=False))