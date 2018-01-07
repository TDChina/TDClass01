# -*- coding: utf-8 -*-
import pymel.core as pm
from . import model
reload(model)

def show():
    MainUI()


class MainUI(object):

    window_name = 'presets_manager'
    docker_name = '%s_docker' % window_name
    current_view = None

    def __init__(self):
        # Singleton
        MainUI.current_view = self

        # Make sure only one single Maya docker
        if pm.window(self.window_name, exists=True):
            pm.deleteUI(self.window_name)
        if pm.dockControl(self.docker_name, exists=True):
            pm.deleteUI(self.docker_name)

        # Setup basic UI
        self.win = pm.window(self.window_name)
        self.frm_lyt = pm.formLayout(numberOfDivisions=100)
        self.prj_omg = pm.optionMenu(label='Current Preset:', height=25,
                                     changeCommand=lambda *args: self.update(target=args[0]))
        self.new_btn = pm.button(parent=self.frm_lyt, label='New', command=self.new)
        self.save_btn = pm.button(parent=self.frm_lyt, label='Save', command=self.save)
        self.prs_lyt = pm.rowColumnLayout(parent=self.frm_lyt, numberOfColumns=2)

        self.frm_lyt.attachForm(self.prj_omg, 'left', 5)
        self.frm_lyt.attachPosition(self.prj_omg, 'right', 0, 60)
        self.frm_lyt.attachControl(self.new_btn, 'left', 5, self.prj_omg)
        self.frm_lyt.attachPosition(self.new_btn, 'right', 0, 80)
        self.frm_lyt.attachControl(self.save_btn, 'left', 5, self.new_btn)
        self.frm_lyt.attachForm(self.save_btn, 'right', 5)
        self.frm_lyt.attachControl(self.prs_lyt, 'top', 5, self.prj_omg)

        # Setup options UI based on template
        self.setters = []
        for preset in model.preset_template:
            pm.text(label='%s: ' % preset['label'], align='right')
            # If the preset has items, then it is enumerable, which can be represented by an optionMenu.
            # Otherwise a textField will do.
            creator, arg = (pm.optionMenu, 'value') if preset.get('_items', None) else (pm.textField, 'text')
            # Create the control and use preset's setter as its callback function
            opt_ctl = creator(parent=self.prs_lyt, changeCommand=preset['setter'])
            for lbl in preset.get('_items', []):
                pm.menuItem(parent=opt_ctl, label=lbl)
            # Save control's info for later use.
            self.setters.append({'label': preset['label'], 'control': opt_ctl, 'creator': creator, 'arg': arg})

        # Update options values
        self.update(init=True)

        # Add the window to a Maya docker
        pm.dockControl(self.docker_name, area='left', content=self.win,
                       allowedArea=['right', 'left'], label='Presets Manager')

    def update(self, init=False, target=None):
        """
        Update options values when required.
        The values displayed and the actual Maya preferences are synchronous.
        :param init: Only available in __init__.
        :param target: The target preset to change to.
        """
        # Update presets list
        for item in pm.optionMenu(self.prj_omg, q=True, itemListLong=True):
            pm.deleteUI(item)
        for preset in model.get_presets():
            pm.menuItem(parent=self.prj_omg, label=preset['name'])

        if init:  # If MainUI is just opened, retrieve current preset from Maya's optionVar.
            current_preset = pm.optionVar(q='currentPreset') if pm.optionVar(exists='currentPreset') else model.default
            try:
                pm.optionMenu(self.prj_omg, e=True, value=current_preset)
            except RuntimeError:
                current_preset = model.default

        else:  # Or set current preset to a specified one.
            if target:
                current_preset = target
                pm.optionMenu(self.prj_omg, e=True, value=target)
            else:
                current_preset = pm.optionMenu(self.prj_omg, q=True, value=True)

        # Apply current preset.
        for preset in model.get_presets():
            if current_preset == preset['name']:
                for setter in self.setters:
                    # Make sure each option value display is correct.
                    setter['creator'](setter['control'], **{'e': True, setter['arg']: preset[setter['label']]})
                model.apply(preset)

        pm.optionVar(stringValue=('currentPreset', current_preset))

    def new(self, *args):
        """
        Callback function for button "New".
        Create a new preset.
        """
        result = pm.promptDialog(title='New Preset', message='Enter Name:',
                                 button=['OK', 'Cancel'], defaultButton='OK',
                                 cancelButton='Cancel', dismissString='Cancel')

        if result == 'OK':
            preset_name = pm.promptDialog(q=True, text=True)
            model.set_preset(preset_name)
            self.update(target=preset_name)

    def save(self, *args):
        """
        Callback function for button "Save".
        Save changes to current preset.
        """
        preset_name = pm.optionMenu(self.prj_omg, q=True, value=True)
        model.set_preset(preset_name)
        self.update(target=preset_name)
