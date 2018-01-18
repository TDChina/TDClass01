cxfreeze.bat 
   pip安装完cx_freeze后，cmd中无法调用 cxfreeze时，将这个脚本放入 python.exe所在的文件夹下的Scripts文件夹中
   将Scripts加入PATH环境变量中
   
   示例:
       set PATH=C:\Python27\Scripts;%PATH% 

ui-noconsole\cxfreeze_build.bat
   用于cxfreeze打包无console程序
   
   cxfreeze_build.bat中的操作：
       cmd中执行 python setup.py build