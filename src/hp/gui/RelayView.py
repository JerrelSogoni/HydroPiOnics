import wx
from WorkspaceView import WorkspaceView
IMG_LOCATION = WorkspaceView.IMG_LOCATION
class RelayView:
    def __init__(self,workspace, appGUI):
        self.workspace = workspace
        self.appGUI = appGUI
        self.initPumpImages()
        self.initElectronicImages()
        self.initStaticEnvironmentText()
        self.initStaticPumpText()
        self.initRelayCheckBoxes()
        self.initRelayInputs()
        self.initSliders()
        self.initStaticElectronicText()

    def initRelayInputs(self):
        self.drainSystemCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'Drain System', name=u'drainSystemCheckBox',
              parent=self.workspace, pos=wx.Point(192, 360),
              size=wx.Size(84, 15), style=0)
        self.drainSystemCheckBox.SetValue(False)

    
        self.airFilterFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'airFilterFanCycleOnValue', parent=self.workspace,
              pos=wx.Point(560, 336), size=wx.Size(48, 23), style=0, value='')
    
        self.airFilterFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'airFilterFanCycleOffValue', parent=self.workspace,
              pos=wx.Point(688, 336), size=wx.Size(48, 23), style=0, value='')
    
    
        self.ledCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'ledCycleOnValue', parent=self.workspace,
              pos=wx.Point(560, 608), size=wx.Size(48, 23), style=0, value='')
    
        self.ledCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'ledCycleOffValue', parent=self.workspace,
              pos=wx.Point(696, 608), size=wx.Size(48, 23), style=0, value='')
    
    
        self.cycleOnAirFIlterFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY,
              name=u'cycleOnAirFIlterFan', parent=self.workspace,
              pos=wx.Point(608, 336), size=wx.Size(56, 23), style=0)
        self.cycleOnAirFIlterFan.SetSelection(0)
    
        self.cycleOffAirFilterFan = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY,
              name=u'cycleOffAirFilterFan', parent=self.workspace,
              pos=wx.Point(736, 336), size=wx.Size(56, 23), style=0)
        self.cycleOffAirFilterFan.SetSelection(0)
    
        self.cycleOnLed = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOnLed',
              parent=self.workspace, pos=wx.Point(608, 608),
              size=wx.Size(56, 23), style=0)
        self.cycleOnLed.SetStringSelection(u'')
        self.cycleOnLed.SetSelection(0)
    
        self.cycleOffLed = wx.Choice(choices=['s', 'm', 'h'],
              id=wx.ID_ANY, name=u'cycleOffLed',
              parent=self.workspace, pos=wx.Point(744, 608),
              size=wx.Size(56, 23), style=0)
        self.cycleOffLed.SetSelection(0)

    def initRelayCheckBoxes(self):
        self.humidifierCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'humidifierCheckBox',
              parent=self.workspace, pos=wx.Point(472, 440),
              size=wx.Size(78, 15), style=0)
        self.humidifierCheckBox.SetValue(False)
    
        self.airHeaterCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'airHeaterCheckBox',
              parent=self.workspace, pos=wx.Point(472, 528),
              size=wx.Size(78, 15), style=0)
        self.airHeaterCheckBox.SetValue(False)
        self.airFilterFanCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'airFilterFanCheckBox',
              parent=self.workspace, pos=wx.Point(472, 336),
              size=wx.Size(78, 15), style=0)
        self.airFilterFanCheckBox.SetValue(False)
    
        self.ledCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'ledCheckBox', parent=self.workspace,
              pos=wx.Point(472, 608), size=wx.Size(78, 15), style=0)
        self.ledCheckBox.SetValue(False)
    
        self.mixToPlantCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'mixToPlantCheckBox',
              parent=self.workspace, pos=wx.Point(96, 160),
              size=wx.Size(78, 15), style=0)
        self.mixToPlantCheckBox.SetValue(False)

        self.planToMixCheckbox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'planToMixCheckbox',
              parent=self.workspace, pos=wx.Point(96, 256),
              size=wx.Size(84, 15), style=0)
        self.planToMixCheckbox.SetValue(False)
    
        self.mixToDrainCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'mixToDrainCheckBox',
              parent=self.workspace, pos=wx.Point(96, 360),
              size=wx.Size(84, 15), style=0)
        self.mixToDrainCheckBox.SetValue(False)
        
        


    def initElectronicImages(self):
        self.airFilterFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "airFilterFan.jpg", wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                   name=u'airFilterFanPicture', parent=self.workspace,
                                                   pos=wx.Point(408, 312),
                                                   size=wx.Size(50, 66), style=0)
        self.humidifierPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "humidifier.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'humidifierPicture', parent=self.workspace,
                                                 pos=wx.Point(400, 416), size=wx.Size(64, 56), style=0)

        self.ledPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "myLedLights.JPG",
                                                           wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                          name=u'ledPicture', parent=self.workspace, pos=wx.Point(400,
                                                                                        592), size=wx.Size(64, 56),
                                          style=0)
    def initPumpImages(self):
        self.mixToPlantPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'mixToPlantPicture', parent=self.workspace,
                                                 pos=wx.Point(32, 136), size=wx.Size(50, 66), style=0)

        self.airHeaterPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "heater.jpg",
                                                                 wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                name=u'airHeaterPicture', parent=self.workspace,
                                                pos=wx.Point(400, 512), size=wx.Size(64, 56), style=0)

        self.plantToMixPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'plantToMixPicture', parent=self.workspace,
                                                 pos=wx.Point(32, 232), size=wx.Size(50, 66), style=0)

        self.mixToDrainPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'mixToDrainPicture', parent=self.workspace,
                                                 pos=wx.Point(32, 336), size=wx.Size(50, 66), style=0)

    def initStaticPumpText(self):
        self.waterControlText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                              label=u'Water Control', name=u'waterControlText',
                                                              parent=self.workspace, pos=wx.Point(24, 8), size=wx.Size(100,
                                                                                                             16),
                                                              style=0)
        self.waterControlText.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL,
                                              wx.NORMAL, False, u'Lucida Handwriting'))
        self.waterControlText.SetToolTipString(u'')
        self.mixToPlantText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Mix to Plant', name=u'mixToPlantText',
                                                            parent=self.workspace, pos=wx.Point(16, 112),
                                                            size=wx.Size(82, 15), style=0)
        self.mixToPlantText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.mixToPlantText.SetToolTipString(u'')

        self.plantToMixText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Plant to Mix', name=u'plantToMixText',
                                                            parent=self.workspace, pos=wx.Point(16, 216),
                                                            size=wx.Size(82, 15), style=0)
        self.plantToMixText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.plantToMixText.SetToolTipString(u'')

        self.mixToDrainText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Mix to Drain', name=u'mixToDrainText',
                                                            parent=self.workspace, pos=wx.Point(16, 320),
                                                            size=wx.Size(84, 15), style=0)
        self.mixToDrainText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.mixToDrainText.SetToolTipString(u'')

    def initStaticElectronicText(self):
        self.humidifierText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Humifier', name=u'humidifierText',
                                                            parent=self.workspace, pos=wx.Point(400, 400),
                                                            size=wx.Size(61, 15), style=0)
        self.humidifierText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))

        self.airHeaterText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                           label=u'Air Heater', name=u'airHeaterText',
                                                           parent=self.workspace, pos=wx.Point(400, 496),
                                                           size=wx.Size(68, 15), style=0)
        self.airHeaterText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                           wx.NORMAL, False, u'Showcard Gothic'))

        self.airFilterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                              label=u'Air Filter Fan', name=u'airFilterFanText',
                                                              parent=self.workspace, pos=wx.Point(384, 296),
                                                              size=wx.Size(88, 15), style=0)
        self.airFilterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                              wx.NORMAL, False, u'Showcard Gothic'))
        self.ledText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                     label=u'LEDs', name=u'ledText', parent=self.workspace,
                                                     pos=wx.Point(416, 584), size=wx.Size(30, 15), style=0)
        self.ledText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
                                     False, u'Showcard Gothic'))
        self.cycleOffAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                      label=u'Cycle Off',
                                                                      name=u'cycleOffAirFIlterFanText',
                                                                      parent=self.workspace, pos=wx.Point(688, 320),
                                                                      size=wx.Size(104, 15), style=0)

        self.cycleOnAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
                                                                     parent=self.workspace, pos=wx.Point(560, 320),
                                                                     size=wx.Size(104, 15), style=0)

        self.cycleOnLedText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Cycle On', name=u'cycleOnLedText',
                                                            parent=self.workspace, pos=wx.Point(560, 592),
                                                            size=wx.Size(104, 15), style=0)

        self.cycleOffLedText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'Cycle Off', name=u'cycleOffLedText',
                                                             parent=self.workspace, pos=wx.Point(696, 592),
                                                             size=wx.Size(104, 15), style=0)

    def initStaticEnvironmentText(self):
        self.temperatureRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'Temperature Range',
                                                                  name=u'temperatureRangeText',
                                                                  parent=self.workspace, pos=wx.Point(32, 432),
                                                                  size=wx.Size(104, 15), style=0)
        self.temperatureRangeText.SetFont(wx.Font(12, wx.DECORATIVE, wx.NORMAL,
                                                  False))
        self.temperatureRangeText.SetToolTipString(u'in Fahrenheit')
        self.temperatureRangeText.SetHelpText(u'in Fahrenheit')

        self.humidityRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                               label=u'Humidity Range', name=u'humdiityRangeText',
                                                               parent=self.workspace, pos=wx.Point(32, 528),
                                                               size=wx.Size(86, 15), style=0)
        self.humidityRangeText.SetFont(wx.Font(12, wx.DECORATIVE, wx.NORMAL,
                                               False))

        self.humidityRangeStartValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                       name=u'humidityRangeStartValue', parent=self.workspace,
                                                                       pos=wx.Point(144, 512), size=wx.Size(40, 32),
                                                                       style=0, value='')
        self.genStaticText21 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText21', parent=self.workspace,
                                                             pos=wx.Point(216, 520), size=wx.Size(6, 15), style=0)
        self.genStaticText21.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                             wx.BOLD, False, u'Showcard Gothic'))
        self.genStaticText21.SetBackgroundColour(wx.Colour(143, 210, 250))

        self.humidityRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                     name=u'humidityRangeEndValue', parent=self.workspace,
                                                                     pos=wx.Point(240, 512), size=wx.Size(40, 32),
                                                                     style=0, value='')
        self.temperatureRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'Temperature Range',
                                                                  name=u'temperatureRangeText',
                                                                  parent=self.workspace, pos=wx.Point(32, 432),
                                                                  size=wx.Size(104, 15), style=0)
        self.temperatureRangeText.SetToolTipString(u'in Fahrenheit')
        self.temperatureRangeText.SetHelpText(u'in Fahrenheit')

        self.temperatureRangeStartValue = wx.TextCtrl(id=wx.ID_ANY,
                                                      name=u'temperatureRangeStartValue', parent=self.workspace,
                                                      pos=wx.Point(144, 424), size=wx.Size(40, 32), style=0, value=u'')
        self.temperatureTextStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'F', name=u'temperatureTextStart',
                                                                  parent=self.workspace, pos=wx.Point(184, 424),
                                                                  size=wx.Size(16, 36), style=0)
        self.temperatureTextStart.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
                                                  wx.NORMAL, False, u'Segoe Print'))
        self.genStaticText19 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText19', parent=self.workspace,
                                                             pos=wx.Point(216, 424), size=wx.Size(8, 25), style=0)
        self.genStaticText19.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
                                             False, u'Segoe UI'))
        self.genStaticText19.SetBackgroundColour(wx.Colour(167, 231, 252))

        self.temperatureRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'temperatureRangeEndValue', parent=self.workspace,
                                                                        pos=wx.Point(240, 424), size=wx.Size(40, 32),
                                                                        style=0, value='')
        self.pHRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                         label=u'PH Level Range', name=u'pHRangeText',
                                                         parent=self.workspace, pos=wx.Point(32, 640),
                                                         size=wx.Size(82, 15), style=0)

        self.pHLevelStartValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                 name=u'pHLevelStartValue', parent=self.workspace,
                                                                 pos=wx.Point(144, 624), size=wx.Size(40, 31), style=0,
                                                                 value='')
        self.genStaticText23 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText23', parent=self.workspace,
                                                             pos=wx.Point(208, 632), size=wx.Size(6, 15), style=0)
        self.genStaticText23.SetBackgroundColour(wx.Colour(159, 221, 251))
        self.genStaticText23.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                             wx.BOLD, False, u'Showcard Gothic'))

        self.phLevelEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                               name=u'phLevelEndValue', parent=self.workspace,
                                                               pos=wx.Point(232, 624), size=wx.Size(40, 32), style=0,
                                                               value='')
        self.temperatureRangeEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'F', name=u'temperatureRangeEndText',
                                                                     parent=self.workspace, pos=wx.Point(280, 424),
                                                                     size=wx.Size(16, 36), style=0)
        self.temperatureRangeEndText.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
                                                     wx.NORMAL, False, u'Segoe Print'))

        self.humidityPercentSignStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                      label=u'%', name=u'humidityPercentSignStart',
                                                                      parent=self.workspace, pos=wx.Point(184, 512),
                                                                      size=wx.Size(15, 36), style=0)
        self.humidityPercentSignStart.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
                                                      wx.NORMAL, False, u'Segoe Print'))

        self.humidityEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'%', name=u'humidityEndText', parent=self.workspace,
                                                             pos=wx.Point(280, 512), size=wx.Size(15, 36), style=0)
        self.humidityEndText.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
                                             wx.NORMAL, False, u'Segoe Print'))

    def initSliders(self):
        self.humidityRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                  maxValue=100, minValue=0, name=u'humidityRangeStartSlider',
                                                  parent=self.workspace, pos=wx.Point(16, 560),
                                                  size=wx.Size(360, 20), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeStartSlider.SetPageSize(1)
        self.humidityRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                maxValue=100, minValue=0, name=u'humidityRangeEndSlider',
                                                parent=self.workspace, pos=wx.Point(16, 600),
                                                size=wx.Size(360, 20), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeEndSlider.SetPageSize(1)
        self.temperatureRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                     maxValue=100, minValue=45, name=u'temperatureRangeStartSlider',
                                                     parent=self.workspace, pos=wx.Point(16, 456),
                                                     size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=45)
        self.temperatureRangeStartSlider.SetPageSize(1)

        self.temperatureRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                   maxValue=100, minValue=45, name=u'temperatureRangeEndSlider',
                                                   parent=self.workspace, pos=wx.Point(16, 488),
                                                   size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        self.temperatureRangeEndSlider.SetPageSize(1)
        self.pHRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                            maxValue=12, minValue=0, name=u'pHRangeStartSlider',
                                            parent=self.workspace, pos=wx.Point(16, 656),
                                            size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        self.pHRangeStartSlider.SetPageSize(1)

        self.pHRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                          maxValue=12, minValue=0, name=u'pHRangeEndSlider',
                                          parent=self.workspace, pos=wx.Point(16, 680),
                                          size=wx.Size(360, 32), style=wx.SL_HORIZONTAL, value=0)
        self.pHRangeEndSlider.SetPageSize(1)



