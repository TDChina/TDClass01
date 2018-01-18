# -*- mode: python -*-

block_cipher = None


a = Analysis(['ui-with-data.py'],
             pathex=['E:\\_test\\td_class\\11\\ui-with-data'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [
            ('pikaqiu.jpg','pikaqiu.jpg','DATA'),
          ],
          name='ui-with-data',               
          debug=False,
          strip=False,
          upx=True,
          console=True )
