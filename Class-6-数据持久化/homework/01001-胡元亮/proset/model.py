# -*- coding: utf-8 -*-
import os, json
import pymel.core as pm

default = 'default'
json_path = os.path.join(unicode(os.path.split(__file__)[0], 'gbk'), 'presets.json')

# Template Specifications:
# label:  Option display name
# _items: Items of the option, if it is enumerable
# getter: Function to get the option value from Maya
# setter: Function to set the option value into Maya
preset_template = [{'label':  'FPS',
                    '_items': ['game', 'film', 'pal', 'ntsc', 'show', 'palf', 'ntscf'],
                    'getter': lambda: pm.currentUnit(q=True, time=True),
                    'setter': lambda t: pm.currentUnit(time=t),
                    },
                   {'label':  'Render Width',
                    'getter': lambda: pm.getAttr('defaultResolution.width'),
                    'setter': lambda w: pm.setAttr('defaultResolution.width', int(w)),
                    },
                   {'label':  'Render Height',
                    'getter': lambda: pm.getAttr('defaultResolution.height'),
                    'setter': lambda h: pm.setAttr('defaultResolution.height', int(h)),
                    },
                   ]


def apply(preset):
    """
    Apply the preset into Maya
    :param preset: The preset to apply.
    """
    for pt in preset_template:
        pt.get('setter', lambda _: None)(preset.get(pt['label']))


def get_presets():
    """
    Get presets from json_path.
    :return: All presets
    """
    try:
        with open(json_path) as f:
            return json.load(f)
    except IOError:
        empty_preset = [{'name': default}]
        for preset in preset_template:
            empty_preset[0][preset['label']] = preset['getter']()  # Retrieve settings from maya

        with open(json_path, 'w') as f:
            json.dump(empty_preset, f, indent=2)

        return empty_preset


def set_preset(preset_name):
    """
    Save changes to current preset.
    :param preset_name: Name of the preset to be saved.
    """
    pm.optionVar(stringValue=('currentPreset', preset_name))

    new_preset = {'name': preset_name}
    for preset in preset_template:
        new_preset[preset['label']] = preset['getter']()

    with open(json_path) as f:
        presets = json.load(f)

    add = True
    for p in presets:
        if new_preset['name'] == p['name']:
            add = False
            for field in new_preset:
                p[field] = new_preset[field]

    if add:
        presets.append(new_preset)

    with open(json_path, 'w') as f:
        json.dump(presets, f, indent=2)
