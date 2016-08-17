import wx
import wx.lib.masked.textctrl
import wx.lib.stattext
from WorkspaceView import IMG_LOCATION
class MotorView:
    def __init__(self, workspace):
        self.workspace = workspace
        self.cycleArray = []
        self.manualArray = []
        self.initMotorImages()
        self.initStaticMotorText()
        self.initMotorCheckBoxes()
        self.initMotorInput()
        self.motorController = None

    def initMotorInput(self):
        self.exaustFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'exaustFanCycleOnValue', parent=self.workspace,
              pos=wx.Point(560, 56), size=wx.Size(48, 23), style=0, value='0')
        self.cycleArray.append(self.exaustFanCycleOnValue)

        self.exaustFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'exaustFanCycleOffValue', parent=self.workspace,
              pos=wx.Point(688, 56), size=wx.Size(48, 23), style=0, value='0')

        self.cycleArray.append(self.exaustFanCycleOffValue)
        self.ventFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'ventFanCycleOnValue', parent=self.workspace,
              pos=wx.Point(560, 144), size=wx.Size(48, 23), style=0, value='0')
        self.cycleArray.append(self.ventFanCycleOnValue)

        self.ventFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'ventFanCycleOffValue', parent=self.workspace,
              pos=wx.Point(688, 144), size=wx.Size(48, 23), style=0, value='0')
        self.cycleArray.append(self.ventFanCycleOffValue)

        self.intakeFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'intakeFanCycleOnValue', parent=self.workspace,
              pos=wx.Point(560, 240), size=wx.Size(48, 23), style=0, value='0')
        self.cycleArray.append(self.intakeFanCycleOnValue)
        self.intakeFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'intakeFanCycleOffValue', parent=self.workspace,
              pos=wx.Point(688, 240), size=wx.Size(48, 23), style=0, value='0')
        self.cycleArray.append(self.intakeFanCycleOffValue)
        self.cycleOffExaustFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOffExaustFan',
              parent=self.workspace, pos=wx.Point(736, 56),
              size=wx.Size(56, 23), style=0)
        self.cycleOffExaustFan.SetSelection(0)
        self.cycleArray.append(self.cycleOffExaustFan)

        self.cycleOnVentFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOnVentFan',
              parent=self.workspace, pos=wx.Point(608, 144),
              size=wx.Size(56, 23), style=0)
        self.cycleOnVentFan.SetSelection(0)
        self.cycleArray.append(self.cycleOnVentFan)

        self.cycleOffVentFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOffVentFan',
              parent=self.workspace, pos=wx.Point(736, 144),
              size=wx.Size(56, 23), style=0)
        self.cycleOffVentFan.SetSelection(0)
        self.cycleArray.append(self.cycleOffVentFan)

        self.cycleOnIntakeFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOnIntakeFan',
              parent=self.workspace, pos=wx.Point(608, 240),
              size=wx.Size(56, 23), style=0)
        self.cycleOnIntakeFan.SetSelection(0)
        self.cycleArray.append(self.cycleOnIntakeFan)

        self.cycleOffIntakeFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOffIntakeFan',
              parent=self.workspace, pos=wx.Point(736, 240),
              size=wx.Size(56, 23), style=0)
        self.cycleOffIntakeFan.SetSelection(0)
        self.cycleArray.append(self.cycleOffIntakeFan)
        self.cycleOnExaustFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOnExaustFan',
              parent=self.workspace, pos=wx.Point(608, 56),
              size=wx.Size(56, 23), style=0)

        self.cycleOnExaustFan.SetSelection(0)
        self.cycleArray.append(self.cycleOnExaustFan)

    def initMotorImages(self):
        self.ventFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "ventFan.jpg",
                                                               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                              name=u'ventFanPicture', parent=self.workspace,
                                              pos=wx.Point(400, 136), size=wx.Size(64, 56), style=0)
        self.waterAirPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "air&pump.jpg",
                                                                wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                               name=u'waterAirPicture', parent=self.workspace,
                                               pos=wx.Point(24, 48), size=wx.Size(64, 56), style=0)
        self.intakeFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "intakeFan.jpg",
                                                                 wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                name=u'intakeFanPicture', parent=self.workspace,
                                                pos=wx.Point(400, 232), size=wx.Size(64, 56), style=0)



        self.exhaustFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "exaustFan.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'exhaustFanPicture', parent=self.workspace,
               pos=wx.Point(400, 40), size=wx.Size(64, 56), style=0)

    def initStaticMotorText(self):
        self.environmentControlText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                    label=u'Environmental Control',
                                                                    name=u'environmentControlText',
                                                                    parent=self.workspace, pos=wx.Point(464, 8),
                                                                    size=wx.Size(154, 16), style=0)
        self.environmentControlText.SetFont(wx.Font(8, wx.SCRIPT, wx.NORMAL,
                                                    wx.NORMAL, False, u'Lucida Calligraphy'))

        self.intakeFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                           label=u'Intake Fan', name=u'intakeFanText',
                                                           parent=self.workspace, pos=wx.Point(400, 216),
                                                           size=wx.Size(69, 15), style=0)
        self.intakeFanText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                           wx.NORMAL, False, u'Showcard Gothic'))

        self.ventFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                         label=u'Vent Fan', name=u'ventFanText',
                                                         parent=self.workspace, pos=wx.Point(400, 120),
                                                         size=wx.Size(56, 15), style=0)
        self.ventFanText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
                                         False, u'Showcard Gothic'))
        self.waterPumpAirTitle = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                               label=u'Water/Air Pump', name=u'waterPumpAirTitle',
                                                               parent=self.workspace, pos=wx.Point(8, 32), size=wx.Size(104,
                                                                                                              15),
                                                               style=0)
        self.waterPumpAirTitle.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                               wx.NORMAL, False, u'Showcard Gothic'))

        self.exhaustFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Exhaust Fan', name=u'exhaustFanText',
                                                            parent=self.workspace, pos=wx.Point(392, 24),
                                                            size=wx.Size(80, 15), style=0)
        self.exhaustFanText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))

        self.exaustFanCycleOnText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'Cycle On', name=u'exaustFanCycleOnText',
                                                                  parent=self.workspace, pos=wx.Point(560, 40),
                                                                  size=wx.Size(104, 15), style=0)
        self.exaustFanCycleOnText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.exaustFanCycleOnText)
        self.exaustFanCycleOffText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                   label=u'Cycle Off', name='exaustFanCycleOffText',
                                                                   parent=self.workspace, pos=wx.Point(688, 40),
                                                                   size=wx.Size(104, 15), style=0)
        self.exaustFanCycleOffText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                                  wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.exaustFanCycleOffText)

        self.cycleOnVentFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                label=u'Cycle On', name=u'cycleOnVentFanText',
                                                                parent=self.workspace, pos=wx.Point(560, 128),
                                                                size=wx.Size(104, 15), style=0)
        self.cycleOnVentFanText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                                  wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOnVentFanText)

        self.cycleOffVentFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                 label=u'Cycle Off', name=u'cycleOffVentFanText',
                                                                 parent=self.workspace, pos=wx.Point(688, 128),
                                                                 size=wx.Size(104, 15), style=0)
        self.cycleOffVentFanText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                                  wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOffVentFanText)
        self.cycleOnIntakeFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'Cycle On', name=u'cycleOnIntakeFanText',
                                                                  parent=self.workspace, pos=wx.Point(560, 224),
                                                                  size=wx.Size(104, 15), style=0)
        self.cycleOnIntakeFanText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                                  wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOnIntakeFanText)

        self.cycleOffIntakeFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                   label=u'Cycle Off', name=u'cycleOffIntakeFanText',
                                                                   parent=self.workspace, pos=wx.Point(688, 224),
                                                                   size=wx.Size(104, 15), style=0)

        self.cycleOffIntakeFanText.SetFont(wx.Font(8, wx.DECORATIVE, wx.NORMAL,
                                                  wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOffIntakeFanText)

        
    def initMotorCheckBoxes(self):

        self.exhaustFanCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'exhaustFanCheckBox',
              parent=self.workspace, pos=wx.Point(472, 56),
              size=wx.Size(78, 15), style=0)
        self.exhaustFanCheckBox.SetValue(False)
        self.manualArray.append(self.exhaustFanCheckBox)
        self.ventFanCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'ventFanCheckBox',
              parent=self.workspace, pos=wx.Point(472, 152),
              size=wx.Size(78, 15), style=0)
        self.ventFanCheckBox.SetValue(False)
        self.manualArray.append(self.ventFanCheckBox)

        self.waterAirCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'waterAirCheckBox',
              parent=self.workspace, pos=wx.Point(96, 64), size=wx.Size(78,
              15), style=0)
        self.waterAirCheckBox.SetValue(False)
        self.manualArray.append(self.waterAirCheckBox)
        self.intakeFanCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'intakeFanCheckBox',
              parent=self.workspace, pos=wx.Point(472, 248),
              size=wx.Size(78, 15), style=0)
        self.intakeFanCheckBox.SetValue(False)
        self.manualArray.append(self.intakeFanCheckBox)

    def initController(self, controller):
        self.motorController = controller

    def initListeners(self):
        # exhaust listner
        self.exhaustFanCheckBox.Bind(wx.EVT_CHECKBOX, self.motorController.processExhaustFanCheckbox)
        self.exaustFanCycleOnValue.Bind(wx.EVT_TEXT_ENTER, self.motorController.processExhaustFanCycleOn)
        self.exaustFanCycleOffValue.Bind(wx.EVT_TEXT_ENTER, self.motorController.processExhaustFanCycleOff)
        self.cycleOnExaustFan.Bind(wx.EVT_CHOICE, self.motorController.processExhaustFanCycleOnUnits)
        self.cycleOffExaustFan.Bind(wx.EVT_CHOICE, self.motorController.processExhaustFanCycleOffUnits)

        #intake listener
        self.intakeFanCheckBox.Bind(wx.EVT_CHECKBOX, self.motorController.processIntakeFanCheckbox)
        self.intakeFanCycleOnValue.Bind(wx.EVT_TEXT_ENTER, self.motorController.processIntakeFanCycleOn)
        self.intakeFanCycleOffValue.Bind(wx.EVT_TEXT_ENTER, self.motorController.processIntakeFanCycleOff)
        self.cycleOnIntakeFan.Bind(wx.EVT_CHOICE, self.motorController.processIntakeFanCycleOnUnits)
        self.cycleOffIntakeFan.Bind(wx.EVT_CHOICE, self.motorController.processIntakeFanCycleOffUnits)

        #vent listener

        self.ventFanCheckBox.Bind(wx.EVT_CHECKBOX, self.motorController.processVentFanCheckbox)
        self.ventFanCycleOnValue.Bind(wx.EVT_TEXT_ENTER, self.motorController.processVentFanCycleOn)
        self.ventFanCycleOffValue.Bind(wx.EVT_TEXT_ENTER, self.motorController.processVentFanCycleOff)
        self.cycleOnVentFan.Bind(wx.EVT_CHOICE, self.motorController.processVentFanCycleOnUnits)
        self.cycleOffVentFan.Bind(wx.EVT_CHOICE, self.motorController.processVentFanCycleOffUnits)

        #water pump listner

        self.waterAirFanCheckBox.Bind(wx.EVT_CHECKBOX, self.motorController.processWAterAirPumpFanCheckbox)


