# -*- coding: utf-8 -*-
# 读取设置
import maya.cmds as mc
import json


# 设置读取路径
open_file = open(r"C:\Users\bin\GitTD\GitTest\TDChina\TDClass06\homework\01004-jiabin\maya_conf.json", "r")
maya_conf = json.loads(open_file.read())
open_file.close()
# 字典
time_unit = maya_conf["conf_time_unit"]
playback_min = maya_conf["conf_playback_min"]
playback_max = maya_conf["conf_playback_max"]
playback_start = maya_conf["conf_playback_start"]
playback_end = maya_conf["conf_playback_end"]
Resolution_width = maya_conf["conf_Resolution_width"]
Resolution_height = maya_conf["conf_Resolution_height"]
Resolution_dar = maya_conf["conf_Resolution_dar"]
# 设置时间
mc.currentUnit(time = time_unit)
mc.playbackOptions(minTime = playback_min)
mc.playbackOptions(maxTime = playback_max)
mc.playbackOptions(animationStartTime = playback_start)
mc.playbackOptions(animationEndTime = playback_end)
# 设置分辨率
mc.setAttr("defaultResolution.width", Resolution_width)
mc.setAttr("defaultResolution.height", Resolution_height)
mc.setAttr("defaultResolution.dar", Resolution_dar)
