#-*- coding: UTF-8 -*-
# From Python
import os, sys, shutil, string
import subprocess
# From Nuke
import nuke, nukescripts
def CmdZbatchRender():
    p = nuke.Panel( 'ZbatchRender' )
    p.addSingleLineInput( 'first', nuke.root().firstFrame() )
    p.addSingleLineInput( 'last', nuke.root().lastFrame() )
    p.addSingleLineInput( 'path', nuke.root().name() )
    p.addEnumerationPulldown('Write', 'Write1 Write2 Write3 Write4 Write5 Write6' )
    p.addEnumerationPulldown('Cpu', '22 24  30 32 46 48' )
    p.addEnumerationPulldown('batch size', '2 4 6 8' )
    p.show()
    first = p.value('first')
    last = p.value('last')
    path = p.value('path')
    Cpu = p.value('Cpu')
    Write = p.value('Write')
    batch = p.value('batch size')
    f = open("C:\Program Files\Nuke9.0v5\zbatch.bat",'w')  
    f.write('set min=')
    f.write(first)
    f.write('\n''set max=')
    f.write(last)
    f.write('\n''set Path=')
    f.write(path)
    f.write('\n''set Write=')
    f.write(Write)
    f.write('\n''set cpu=')
    f.write(Cpu)
    f.write('\n''set batch=')
    f.write(batch)
    f.close()
cmd=os.system