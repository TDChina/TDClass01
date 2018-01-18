# -*- coding: utf-8 -*-
# 获取写入
import maya.cmds as mc
import json

# 获取时间
time_unit = mc.currentUnit(query=True, time=True)
playback_min = mc.playbackOptions(query=True, minTime=True)
playback_max = mc.playbackOptions(query=True, maxTime=True)
playback_start = mc.playbackOptions(query=True, animationStartTime=True)
playback_end = mc.playbackOptions(query=True, animationEndTime=True)
# 获取分辨率
Resolution_width = mc.getAttr("defaultResolution.width")
Resolution_height = mc.getAttr("defaultResolution.height")
Resolution_dar = mc.getAttr("defaultResolution.dar")
# 字典
maya_conf = {"conf_time_unit": time_unit,
             "conf_playback_min": playback_min,
             "conf_playback_max": playback_max,
             "conf_playback_start": playback_start,
             "conf_playback_end": playback_end,
             "conf_Resolution_width": Resolution_width,
             "conf_Resolution_height": Resolution_height,
             "conf_Resolution_dar": Resolution_dar}
# 设置存储路径
open_file = open(r"C:\Users\bin\GitTD\GitTest\TDChina\TDClass06\homework\01004-jiabin\maya_conf.json", "w")
open_file.write(json.dumps(maya_conf))
open_file.close()
