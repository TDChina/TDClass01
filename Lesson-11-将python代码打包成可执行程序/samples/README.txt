cxfreeze.bat 
   pip��װ��cx_freeze��cmd���޷����� cxfreezeʱ��������ű����� python.exe���ڵ��ļ����µ�Scripts�ļ�����
   ��Scripts����PATH����������
   
   ʾ��:
       set PATH=C:\Python27\Scripts;%PATH% 

ui-noconsole\cxfreeze_build.bat
   ����cxfreeze�����console����
   
   cxfreeze_build.bat�еĲ�����
       cmd��ִ�� python setup.py build

ui-with-data[pyinstaller]\pyinstaller_build.bat
   ���ڴ��������Դ�ļ���GUI����
   �����Դ�Ĳ����� ui-with-data.spec �� 24-27 ��
   