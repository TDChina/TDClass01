# -*- coding: utf-8 -*-
import pymel.core as pm
from . import model


def show():
    View()


class View(object):

    window_name = 'presets_manager'
    docker_name = '%s_docker' % window_name
    current_view = None

    def __init__(self):
        View.current_view = self

        if pm.window(self.window_name, exists=True):
            pm.deleteUI(self.window_name)
        if pm.dockControl(self.docker_name, exists=True):
            pm.deleteUI(self.docker_name)

        self.win = pm.window(self.window_name)
        self.frm_lyt = pm.formLayout(numberOfDivisions=100)
        self.prj_omg = pm.optionMenu(label='Current Preset:',
                                     changeCommand=lambda *args: self.update(target=args[0]))
        self.new_btn = pm.button(parent=self.frm_lyt, label='New', command=self.new)
        self.save_btn = pm.button(parent=self.frm_lyt, label='Save', command=self.save)
        self.prs_lyt = pm.rowColumnLayout(parent=self.frm_lyt, numberOfColumns=2)
        pm.optionMenu(self.prj_omg, e=True, height=25)

        self.frm_lyt.attachForm(self.prj_omg, 'left', 5)
        self.frm_lyt.attachPosition(self.prj_omg, 'right', 0, 60)
        self.frm_lyt.attachControl(self.new_btn, 'left', 5, self.prj_omg)
        self.frm_lyt.attachPosition(self.new_btn, 'right', 0, 80)
        self.frm_lyt.attachControl(self.save_btn, 'left', 5, self.new_btn)
        self.frm_lyt.attachForm(self.save_btn, 'right', 5)
        self.frm_lyt.attachControl(self.prs_lyt, 'top', 5, self.prj_omg)
        self.setters = []

        for preset in model.preset_template:
            pm.text(label='%s:' % preset['label'], align='right')
            if preset.get('items', None):
                prs_ctl = pm.optionMenu(parent=self.prs_lyt,
                                        changeCommand=preset['setter'])
                for val in preset['items']:
                    pm.menuItem(parent=prs_ctl, label=val)
                self.setters.append({'label': preset['label'], 'control': prs_ctl,
                                     'type': pm.optionMenu, 'arg': 'value'})
            else:
                prs_ctl = pm.textField(parent=self.prs_lyt,
                                       changeCommand=preset['setter'])
                self.setters.append({'label': preset['label'], 'control': prs_ctl,
                                     'type': pm.textField, 'arg': 'text'})

        self.update(init=True)

        pm.dockControl(self.docker_name, area='left', content=self.win,
                       allowedArea=['right', 'left'], label='Presets Manager')

    def update(self, init=False, target=None):
        for item in pm.optionMenu(self.prj_omg, q=True, itemListLong=True):
            pm.deleteUI(item)
        for preset in model.get_presets():
            pm.menuItem(parent=self.prj_omg, label=preset['name'])

        if init:
            current_preset = pm.optionVar(q='currentPreset') if pm.optionVar(exists='currentPreset') else model.default
            try:
                pm.optionMenu(self.prj_omg, e=True, value=current_preset)
            except RuntimeError:
                current_preset = model.default
        else:
            if target:
                current_preset = target
                pm.optionMenu(self.prj_omg, e=True, value=target)
            else:
                current_preset = pm.optionMenu(self.prj_omg, q=True, value=True)

        for preset in model.get_presets():
            if current_preset == preset['name']:
                for setter in self.setters:
                    setter['type'](setter['control'], **{'e': True, setter['arg']: preset[setter['label']]})
                model.apply(preset)

        pm.optionVar(stringValue=('currentPreset', current_preset))

    def new(self, *_):
        result = pm.promptDialog(title='New Preset', message='Enter Name:',
                                 button=['OK', 'Cancel'], defaultButton='OK',
                                 cancelButton='Cancel', dismissString='Cancel')

        if result:
            preset_name = pm.promptDialog(q=True, text=True)
            model.set_preset(preset_name)
            self.update(target=preset_name)

    def save(self, *_):
        preset_name = pm.optionMenu(self.prj_omg, q=True, value=True)
        model.set_preset(preset_name)
        self.update(target=preset_name)
