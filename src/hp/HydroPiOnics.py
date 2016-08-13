

import wx
import wx.lib.masked.timectrl
import wx.lib.masked.combobox
import wx.lib.masked.textctrl
import wx.calendar
import wx.lib.stattext
import wx.lib.scrolledpanel
import wx.lib.buttons
import os
import sys
from gui.HydroPiOnicsView import HydroPiOnicsView
from data.HydroPiOnicsM import HydroPiOnicsM
from controller.HydroPiOnicsController import HydroPiOnicsController
from gui.MenuBarView import MenuBarView
from data.MenuBar import MenuBar
from controller.MenuBarController import MenuBarController
from gui.MonitorView import MonitorView
from data.Monitor import Monitor
from controller.MonitorController import MonitorController
from gui.WorkspaceView import WorkspaceView


def create(parent):
    return HydroPiOnics(parent)

class HydroPiOnics(wx.Frame):

    def _init_ctrls(self, prnt):
        pass





        # self.exhaustFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSEXHAUSTFANCHECKBOX,
        #       label=u'On/Off', name=u'exhaustFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 56),
        #       size=wx.Size(78, 15), style=0)
        # self.exhaustFanCheckBox.Show(True)
        # self.exhaustFanCheckBox.Enable(False)
        # self.exhaustFanCheckBox.SetValue(True)
        # self.exhaustFanCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnExhaustFanCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSEXHAUSTFANCHECKBOX)
        #






        # self.ventFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSVENTFANCHECKBOX,
        #       label=u'On/Off', name=u'ventFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 152),
        #       size=wx.Size(78, 15), style=0)
        # self.ventFanCheckBox.SetValue(True)
        #
        # self.waterAirCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSWATERAIRCHECKBOX,
        #       label=u'On/Off', name=u'waterAirCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 64), size=wx.Size(78,
        #       15), style=0)
        # self.waterAirCheckBox.SetValue(False)
        # self.waterAirCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnWaterAirCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSWATERAIRCHECKBOX)
        #
        # self.intakeFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSINTAKEFANCHECKBOX,
        #       label=u'On/Off', name=u'intakeFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 248),
        #       size=wx.Size(78, 15), style=0)
        # self.intakeFanCheckBox.SetValue(True)
        #
        # self.humidifierCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSHUMIDIFIERCHECKBOX,
        #       label=u'On/Off', name=u'humidifierCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 440),
        #       size=wx.Size(78, 15), style=0)
        # self.humidifierCheckBox.SetValue(True)
        #
        # self.airHeaterCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSAIRHEATERCHECKBOX,
        #       label=u'On/Off', name=u'airHeaterCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 528),
        #       size=wx.Size(78, 15), style=0)
        # self.airHeaterCheckBox.SetValue(True)




        # self.airFilterFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSAIRFILTERFANCHECKBOX,
        #       label=u'On/Off', name=u'airFilterFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 336),
        #       size=wx.Size(78, 15), style=0)
        # self.airFilterFanCheckBox.SetValue(True)
        #


        # self.ledCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSLEDCHECKBOX,
        #       label=u'On/Off', name=u'ledCheckBox', parent=self.scrolledPanel1,
        #       pos=wx.Point(472, 608), size=wx.Size(78, 15), style=0)
        # self.ledCheckBox.SetValue(False)
        #


        # self.mixToPlantCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSMIXTOPLANTCHECKBOX,
        #       label=u'On/Off', name=u'mixToPlantCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 160),
        #       size=wx.Size(78, 15), style=0)
        # self.mixToPlantCheckBox.SetValue(True)
        # self.mixToPlantCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnMixToPlantCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSMIXTOPLANTCHECKBOX)
        #
        # self.planToMixCheckbox = wx.CheckBox(id=wxID_HYDROPIONICSPLANTOMIXCHECKBOX,
        #       label=u'On/Off', name=u'planToMixCheckbox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 256),
        #       size=wx.Size(84, 15), style=0)
        # self.planToMixCheckbox.SetValue(True)
        # self.planToMixCheckbox.Bind(wx.EVT_CHECKBOX,
        #       self.OnPlanToMixCheckboxCheckbox,
        #       id=wxID_HYDROPIONICSPLANTOMIXCHECKBOX)
        #
        # self.mixToDrainCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSMIXTODRAINCHECKBOX,
        #       label=u'On/Off', name=u'mixToDrainCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 360),
        #       size=wx.Size(84, 15), style=0)
        # self.mixToDrainCheckBox.SetValue(True)
        # self.mixToDrainCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnMixToDrainCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSMIXTODRAINCHECKBOX)
        #
        ##### Temperature Range and PH level Range Will not be implemented Yet since I cannot control them
        ## Incorporating in future upgrades

        # self.cycleOnWaterAirPumpValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEONWATERAIRPUMPVALUE,
        #       name=u'cycleOnWaterAirPumpValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(176, 88), size=wx.Size(48, 23), style=0, value='')
        # self.cycleOnWaterAirPumpValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOnWaterAirPumpValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEONWATERAIRPUMPVALUE)
        #
        # self.cycleOffWaterAirPumpValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEOFFWATERAIRPUMPVALUE,
        #       name=u'cycleOffWaterAirPumpValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(280, 88), size=wx.Size(56, 23), style=0, value='')
        # self.cycleOffWaterAirPumpValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOffWaterAirPumpValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEOFFWATERAIRPUMPVALUE)
        #
        # self.cycleOnMixToPlantText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONMIXTOPLANTTEXT,
        #       label=u'Cycle On', name=u'cycleOnMixToPlantText',
        #       parent=self.scrolledPanel1, pos=wx.Point(176, 184),
        #       size=wx.Size(96, 15), style=0)
        #
        # self.cycleOffMixToPlantText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTTEXT,
        #       label=u'Cycle Off', name=u'cycleOffMixToPlantText',
        #       parent=self.scrolledPanel1, pos=wx.Point(280, 184),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOnMixToPlantValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEONMIXTOPLANTVALUE,
        #       name=u'cycleOnMixToPlantValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(176, 200), size=wx.Size(48, 24), style=0, value='')
        # self.cycleOnMixToPlantValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOnMixToPlantValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEONMIXTOPLANTVALUE)
        #
        # self.cycleOffMixToPlantValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTVALUE,
        #       name=u'cycleOffMixToPlantValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(280, 200), size=wx.Size(56, 24), style=0, value='')
        # self.cycleOffMixToPlantValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOffMixToPlantValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTVALUE)
        #
        # self.drainSystemCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSDRAINSYSTEMCHECKBOX,
        #       label=u'Drain System', name=u'drainSystemCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(192, 360),
        #       size=wx.Size(84, 15), style=0)
        # self.drainSystemCheckBox.SetValue(False)
        # self.drainSystemCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnDrainSystemCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSDRAINSYSTEMCHECKBOX)
        #
        # self.exaustFanCycleOnText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSEXAUSTFANCYCLEONTEXT,
        #       label=u'Cycle On', name=u'exaustFanCycleOnText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 40),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.genStaticText3 = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSGENSTATICTEXT3,
        #       label=u'Cycle Off', name='genStaticText3',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 40),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.exaustFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSEXAUSTFANCYCLEONVALUE,
        #       name=u'exaustFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 56), size=wx.Size(48, 23), style=0, value='')
        #
        # self.exaustFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSEXAUSTFANCYCLEOFFVALUE,
        #       name=u'exaustFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 56), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOnVentFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONVENTFANTEXT,
        #       label=u'Cycle On', name=u'cycleOnVentFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 128),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOffVentFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFVENTFANTEXT,
        #       label=u'Cycle Off', name=u'cycleOffVentFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 128),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.ventFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSVENTFANCYCLEONVALUE,
        #       name=u'ventFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 144), size=wx.Size(48, 23), style=0, value='')
        #
        # self.ventFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSVENTFANCYCLEOFFVALUE,
        #       name=u'ventFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 144), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOnIntakeFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONINTAKEFANTEXT,
        #       label=u'Cycle On', name=u'cycleOnIntakeFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 224),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOffIntakeFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFINTAKEFANTEXT,
        #       label=u'Cycle Off', name=u'cycleOffIntakeFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 224),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.intakeFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSINTAKEFANCYCLEONVALUE,
        #       name=u'intakeFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 240), size=wx.Size(48, 23), style=0, value='')
        #
        # self.intakeFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSINTAKEFANCYCLEOFFVALUE,
        #       name=u'intakeFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 240), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOnAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONAIRFILTERFANTEXT,
        #       label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 320),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.airFilterFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSAIRFILTERFANCYCLEONVALUE,
        #       name=u'airFilterFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 336), size=wx.Size(48, 23), style=0, value='')
        #
        # self.airFilterFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSAIRFILTERFANCYCLEOFFVALUE,
        #       name=u'airFilterFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 336), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOffAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFAIRFILTERFANTEXT,
        #       label=u'Cycle Off', name=u'cycleOffAirFIlterFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 320),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOnLedText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONLEDTEXT,
        #       label=u'Cycle On', name=u'cycleOnLedText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 592),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOffLedText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFLEDTEXT,
        #       label=u'Cycle Off', name=u'cycleOffLedText',
        #       parent=self.scrolledPanel1, pos=wx.Point(696, 592),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.ledCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSLEDCYCLEONVALUE,
        #       name=u'ledCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 608), size=wx.Size(48, 23), style=0, value='')
        #
        # self.ledCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSLEDCYCLEOFFVALUE,
        #       name=u'ledCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(696, 608), size=wx.Size(48, 23), style=0, value='')
        #
        # self.temperatureTextStart = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSTEMPERATURETEXTSTART,
        #       label=u'F', name=u'temperatureTextStart',
        #       parent=self.scrolledPanel1, pos=wx.Point(184, 424),
        #       size=wx.Size(16, 36), style=0)
        # self.temperatureTextStart.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
        #       wx.NORMAL, False, u'Segoe Print'))
        #

        # self.cycleOnExaustFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONEXAUSTFAN, name=u'cycleOnExaustFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 56),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnExaustFan.SetStringSelection(u's')
        # self.cycleOnExaustFan.SetSelection(0)
        #
        # self.CycleOnWaterPump = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONWATERPUMP, name=u'CycleOnWaterPump',
        #       parent=self.scrolledPanel1, pos=wx.Point(224, 88),
        #       size=wx.Size(48, 23), style=0)
        # self.CycleOnWaterPump.SetSelection(0)
        # self.CycleOnWaterPump.Bind(wx.EVT_CHOICE, self.OnCycleOnWaterPumpChoice,
        #       id=wxID_HYDROPIONICSCYCLEONWATERPUMP)
        #
        # self.CycleOffWaterPump = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFWATERPUMP, name=u'CycleOffWaterPump',
        #       parent=self.scrolledPanel1, pos=wx.Point(336, 88),
        #       size=wx.Size(48, 23), style=0)
        # self.CycleOffWaterPump.SetSelection(0)
        # self.CycleOffWaterPump.Bind(wx.EVT_CHOICE,
        #       self.OnCycleOffWaterPumpChoice,
        #       id=wxID_HYDROPIONICSCYCLEOFFWATERPUMP)
        #
        # self.cycleOffPlantMixCycle = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFPLANTMIXCYCLE,
        #       name=u'cycleOffPlantMixCycle', parent=self.scrolledPanel1,
        #       pos=wx.Point(336, 200), size=wx.Size(48, 23), style=0)
        # self.cycleOffPlantMixCycle.SetSelection(0)
        # self.cycleOffPlantMixCycle.Bind(wx.EVT_CHOICE,
        #       self.OnCycleOffPlantMixCycleChoice,
        #       id=wxID_HYDROPIONICSCYCLEOFFPLANTMIXCYCLE)
        #
        # self.cycleOnPlantMixCycle = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONPLANTMIXCYCLE,
        #       name=u'cycleOnPlantMixCycle', parent=self.scrolledPanel1,
        #       pos=wx.Point(224, 200), size=wx.Size(48, 23), style=0)
        # self.cycleOnPlantMixCycle.SetSelection(0)
        # self.cycleOnPlantMixCycle.Bind(wx.EVT_CHOICE,
        #       self.OnCycleOnPlantMixCycleChoice,
        #       id=wxID_HYDROPIONICSCYCLEONPLANTMIXCYCLE)
        #
        # self.cycleOffExaustFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFEXAUSTFAN, name=u'cycleOffExaustFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(736, 56),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffExaustFan.SetSelection(0)
        #
        # self.cycleOnVentFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONVENTFAN, name=u'cycleOnVentFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 144),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnVentFan.SetSelection(0)
        #
        # self.cycleOffVentFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFVENTFAN, name=u'cycleOffVentFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(736, 144),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffVentFan.SetSelection(0)
        #
        # self.cycleOnIntakeFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONINTAKEFAN, name=u'cycleOnIntakeFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 240),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnIntakeFan.SetSelection(0)
        #
        # self.cycleOffIntakeFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFINTAKEFAN, name=u'cycleOffIntakeFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(736, 240),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffIntakeFan.SetSelection(0)
        #
        # self.cycleOnAirFIlterFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONAIRFILTERFAN,
        #       name=u'cycleOnAirFIlterFan', parent=self.scrolledPanel1,
        #       pos=wx.Point(608, 336), size=wx.Size(56, 23), style=0)
        # self.cycleOnAirFIlterFan.SetSelection(0)
        #
        # self.cycleOffAirFilterFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFAIRFILTERFAN,
        #       name=u'cycleOffAirFilterFan', parent=self.scrolledPanel1,
        #       pos=wx.Point(736, 336), size=wx.Size(56, 23), style=0)
        # self.cycleOffAirFilterFan.SetSelection(0)
        #
        # self.cycleOnLed = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONLED, name=u'cycleOnLed',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 608),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnLed.SetStringSelection(u'')
        # self.cycleOnLed.SetSelection(0)
        #
        # self.cycleOffLed = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFLED, name=u'cycleOffLed',
        #       parent=self.scrolledPanel1, pos=wx.Point(744, 608),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffLed.SetSelection(0)
        #
        # self.delayStartCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSDELAYSTARTCHECKBOX,
        #       label=u'Delay Start', name=u'delayStartCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(408, 648),
        #       size=wx.Size(78, 23), style=0)
        # self.delayStartCheckBox.SetValue(False)
        # self.delayStartCheckBox.Bind(wx.EVT_CHECKBOX, self.OnCheckBox3Checkbox,
        #       id=wxID_HYDROPIONICSDELAYSTARTCHECKBOX)
        #
        # self.checkPHCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSCHECKPHCHECKBOX,
        #       label=u'Check PH', name=u'checkPHCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(176, 256),
        #       size=wx.Size(88, 16), style=0)
        # self.checkPHCheckBox.SetValue(True)
        # self.checkPHCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnCheckPHCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSCHECKPHCHECKBOX)
        #
        # self.delayStartTime = wx.lib.masked.timectrl.TimeCtrl(display_seconds=True,
        #       fmt24hr=False, id=wxID_HYDROPIONICSDELAYSTARTTIME,
        #       name=u'delayStartTime', oob_color=wx.NamedColour('Yellow'),
        #       parent=self.scrolledPanel1, pos=wx.Point(488, 648),
        #       size=wx.Size(85, 23), style=0, useFixedWidthFont=True,
        #       value='12:00:00 AM')
        #
        # self.systemStatusText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSSYSTEMSTATUSTEXT,
        #       label=u'System Status:', name=u'systemStatusText',
        #       parent=self.scrolledPanel1, pos=wx.Point(784, 688),
        #       size=wx.Size(78, 13), style=0)
        # self.systemStatusText.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
        #       False, u'Small Fonts'))
        #
        # self.systemStatus = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSSYSTEMSTATUS,
        #       label=u'', name=u'systemStatus', parent=self.scrolledPanel1,
        #       pos=wx.Point(872, 688), size=wx.Size(12, 13), style=0)
        # self.systemStatus.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
        #       False, u'Small Fonts'))

    def __init__(self, parent):

        self.initFrameMVC()
        self.initMenuBarMVC()
        self.initMonitorMVC()
        self.initWorkspaceMVC()
        self._init_ctrls(parent)
    def initFrameMVC(self):
        self.gui = HydroPiOnicsView(self)
        self.guiModel =  HydroPiOnicsM()
        self.guiController = HydroPiOnicsController(self.guiModel, self.gui, self)
    def initMenuBarMVC(self):
        self.menuView = MenuBarView()
        self.SetMenuBar(self.menuView)
        self.menuModel = MenuBar()
        self.menuController = MenuBarController(self.menuModel, self.menuView, self)
    def initMonitorMVC(self):
        self.monitorView = MonitorView(self)
        self.monitorModel = Monitor()
        self.monitorController = MonitorController(self.monitorModel, self.monitorView, self)
    def initMotorMVC(self):
        pass
    def initRelayMVC(self):
        pass
    def initWorkspaceMVC(self):
        self.workspaceView = WorkspaceView(self)
    def getGUIController(self):
        return self.guiController
    # def OnCheckBox12Checkbox(self, event):
    #     event.Skip()
    #
    # def OnManualToggleButtonLeftDclick(self, event):
    #     event.Skip()
    #
    # def OnCheckBox3Checkbox(self, event):
    #     event.Skip()
    #
    # def OnExhaustFanCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnWaterAirCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnMixToPlantCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnPlanToMixCheckboxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnMixToDrainCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnPHLevelStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnPhLevelEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnPHRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnPHRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnWaterAirPowerSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnCycleOnWaterAirPumpValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOffWaterAirPumpValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOnMixToPlantValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOffMixToPlantValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnDrainSystemCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnCycleOnWaterPumpChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOffWaterPumpChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOffPlantMixCycleChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOnPlantMixCycleChoice(self, event):
    #     event.Skip()
    #
    # def OnCheckPHCheckBoxCheckbox(self, event):
    #     event.Skip()
    # def initPage(self, parent):
    #     pass
    # def initMotor(self, parent):
    #     pass
    # def initRelay(self, parent):
    #     pass


if __name__ == '__main__':
    app = wx.App()
    frame = create(None)
    frame.Show()

    app.MainLoop()
