# -*- coding: utf8 -*-
from maya import cmds


SUFFIXES = {
    "mesh": "geo",
    "camera": None,
    "anything": "anything"
}
# DEFAULT_SUFFIX = 'oth'


def obj_rename(selection=False):
    """
    This function will rename object with suffix
    :param selection:Whether or not use the current selection
    :return: A list of all the objects we operated on
    """
    obj_name = cmds.ls(sl=selection, dag=True, long=True)
    if selection and not obj_name:
        raise RuntimeError("don't have anything selected!")
    obj_name.sort(key=len, reverse=True)
    for obj in obj_name:
        short_name = obj.split("|")[-1]
        children = cmds.listRelatives(obj, children=True, fullPath=True) or []
        if len(children) == 1:
            obj_type = cmds.objectType(children[0])
        else:
            obj_type = cmds.objectType(obj)
        suffix = SUFFIXES.get(obj_type,)
        if not suffix:
            continue
        if obj.endswith('_' + suffix):
            continue
        new_name = "%s_%s" % (short_name, suffix)
        cmds.rename(obj, new_name)
        index = obj_name.index(obj)
        obj_name[index] = obj.replace(short_name, new_name)
    return obj_name
