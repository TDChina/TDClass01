#
#
# 3DE4.script.name:	Export all Distort node To Nuke by LCY
#
# 3DE4.script.version:	v1.0
#
# 3DE4.script.gui:	Main Window::3DE4::File::Export
# 3DE4.script.gui:	Main Window::Calc
#
# 3DE4.script.comment:  Export all Distort node To Nuke
#


c	= tde4.getCurrentCamera()
pg	= tde4.getCurrentPGroup()
if c!=None and pg!=None:
	n	= tde4.getCameraNoFrames(c)
	width	= tde4.getCameraImageWidth(c)
	height	= tde4.getCameraImageHeight(c)
	pl	= tde4.getPointList(pg,1)
	if len(pl)>0:
		path	= tde4.postFileRequester("Export all Distort node To Nuke...","*.nk")
		if path!=None:
			f	= open(path,"w")
			if not f.closed:
				f.write("set cut_paste_input [stack 0]\n")
				f.write("version 10.5 v5\n")
				f.write("BackdropNode {\n")
				f.write(" inputs 0\n")
				f.write("Constant {\n")
				f.write(" inputs 0\n")
				f.write(" channels rgb\n")
				f.write(" format "2048 858 0 0 2048 858 1 kxq")
				f.write(" name Constant1\n")
				f.write(" selected true\n")
				f.write(" xpos 373\n")
				f.write(" ypos -380\n")
				f.write("}\n")
				f.write("Expression {\n")
				f.write(" name Expression1")
				f.write(" selected true\n")
				f.write(" xpos 373\n")
				f.write(" ypos -308\n")
				f.write("}\n")
				f.write("Reformat {\n")
				f.write(" type scale\n")
				f.write(" scale 1.1\n")
				f.write(" resize none\n")
				f.write(" filter Rifman\n")
				f.write(" clamp true\n")
				f.write(" pbb true\n")
				f.write(" name 3de_Reformat\n")
				f.write(" selected true\n")
				f.write(" xpos 373\n")
				f.write(" ypos -194\n")
				f.write("}\n")

				
		else:
				tde4.postQuestionRequester("Export all Distort node To Nuke...","Error, couldn't save file.","Ok")
else:
	tde4.postQuestionRequester("Export all Distort node To Nuke...","There is no Point or Camera.","Ok")
 
