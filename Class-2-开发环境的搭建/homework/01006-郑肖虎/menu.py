import nuke
import autoBackup

nuke.menu("Nuke").addCommand("Liaokong/open backup dir","autoBackup.open_backup_dir()")
nuke.addOnScriptSave(autoBackup.make_save)
