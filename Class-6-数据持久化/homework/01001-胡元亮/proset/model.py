# -*- coding: utf-8 -*-
import os, json
import pymel.core as pm

default = 'default'
json_path = os.path.join(unicode(os.path.split(__file__)[0], 'gbk'), 'presets.json')
preset_template = [{'label':  'FPS',
                    'items':  ['game', 'film', 'pal', 'ntsc', 'show', 'palf', 'ntscf'],
                    'getter': lambda: pm.currentUnit(q=True, time=True),
                    'setter': lambda t: pm.currentUnit(time=t),
                    },
                   {'label': 'Render Width',
                    'getter': lambda: pm.getAttr('defaultResolution.width'),
                    'setter': lambda w: pm.setAttr('defaultResolution.width', int(w)),
                    },
                   {'label': 'Render Height',
                    'getter': lambda: pm.getAttr('defaultResolution.height'),
                    'setter': lambda h: pm.setAttr('defaultResolution.height', int(h)),
                    },
                   ]


def apply(preset):
    for pt in preset_template:
        pt['setter'](preset[pt['label']])


def get_presets():
    try:
        with open(json_path) as f:
            return json.load(f)
    except IOError:
        empty_preset = [{'name': default}]
        for preset in preset_template:
            empty_preset[0][preset['label']] = preset['getter']()

        with open(json_path, 'w') as f:
            json.dump(empty_preset, f, indent=2)

    return empty_preset


def set_preset(preset):
    pm.optionVar(stringValue=('currentPreset', preset['name']))
    with open(json_path) as f:
        presets = json.load(f)

    add = True
    for p in presets:
        if preset['name'] == p['name']:
            add = False
            for field in preset:
                p[field] = preset[field]

    if add:
        presets.append(preset)

    with open(json_path, 'w') as f:
        json.dump(presets, f, indent=2)
