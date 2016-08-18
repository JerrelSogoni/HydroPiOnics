import wx
import WorkspaceView

IMG_LOCATION = WorkspaceView.IMG_LOCATION

class ElectronicRelayEnviromentView:
    def __init__(self,workpace):
        self.workspace = workpace
        self.objects = []
        self.cycleArray = []
        self.manualArray = []
        self.environmentalHideArray = []
        self.electronicRelayC = None
        self.initElectronicImages()
        self.initStaticElectronicText()
        self.initRelayInputs()
        self.initRelayCheckBoxes()




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
        self.cycleOffAirFIlterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOffAirFIlterFanText)
        self.objects.append(self.cycleOffAirFIlterFanText)

        self.cycleOnAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
                                                                     parent=self.workspace, pos=wx.Point(560, 320),
                                                                     size=wx.Size(104, 15), style=0)
        self.cycleOnAirFIlterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOnAirFIlterFanText)
        self.objects.append(self.cycleOnAirFIlterFanText)


        self.cycleOnLedText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Cycle On', name=u'cycleOnLedText',
                                                            parent=self.workspace, pos=wx.Point(560, 587),
                                                            size=wx.Size(104, 15), style=0)
        self.cycleOnLedText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOnLedText)
        self.objects.append(self.cycleOnLedText)

        self.cycleOffLedText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'Cycle Off', name=u'cycleOffLedText',
                                                             parent=self.workspace, pos=wx.Point(696, 587),
                                                             size=wx.Size(104, 15), style=0)
        self.cycleOffLedText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOffLedText)
        self.objects.append(self.cycleOffLedText)
        self.underwaterTitle = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                               label=u'Underwater Heater', name=u'underwaterHeaterTitle',
                                                               parent=self.workspace, pos=wx.Point(150, 32), size=wx.Size(104,
                                                                                                              15),
                                                               style=0)
        self.underwaterTitle.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
                                     False, u'Showcard Gothic'))

        self.cycleOffAirHeaterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                      label=u'Cycle Off',
                                                                      name=u'cycleOffAirFIlterFanText',
                                                                      parent=self.workspace, pos=wx.Point(688, 520),
                                                                      size=wx.Size(104, 15), style=0)
        self.cycleOffAirHeaterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOffAirHeaterFanText)
        self.objects.append(self.cycleOffAirHeaterFanText)
        self.environmentalHideArray.append(self.cycleOffAirHeaterFanText)

        self.cycleOnAirHeaterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
                                                                     parent=self.workspace, pos=wx.Point(560, 520),
                                                                     size=wx.Size(104, 15), style=0)
        self.cycleOnAirHeaterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOnAirHeaterFanText)
        self.objects.append(self.cycleOnAirHeaterFanText)
        self.environmentalHideArray.append(self.cycleOnAirHeaterFanText)

        self.cycleOffAirHumidFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                      label=u'Cycle Off',
                                                                      name=u'cycleOffAirFIlterFanText',
                                                                      parent=self.workspace, pos=wx.Point(688, 424),
                                                                      size=wx.Size(104, 15), style=0)
        self.cycleOffAirHumidFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOffAirHumidFanText)
        self.objects.append(self.cycleOffAirHumidFanText)
        self.environmentalHideArray.append(self.cycleOffAirHumidFanText)

        self.cycleOnAirHumidFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
                                                                     parent=self.workspace, pos=wx.Point(560, 424),
                                                                     size=wx.Size(104, 15), style=0)
        self.cycleOnAirHumidFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOnAirHumidFanText)
        self.objects.append(self.cycleOnAirHumidFanText)
        self.environmentalHideArray.append(self.cycleOnAirHumidFanText)

        self.cycleOffUnderwaterText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                      label=u'Cycle Off',
                                                                      name=u'cycleOffAirFIlterFanText',
                                                                      parent=self.workspace, pos=wx.Point(278, 90),
                                                                      size=wx.Size(104, 15), style=0)
        self.cycleOffUnderwaterText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOffUnderwaterText)
        self.objects.append(self.cycleOffUnderwaterText)
        self.environmentalHideArray.append(self.cycleOffUnderwaterText)

        self.cycleOnUnderwaterText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
                                                                     parent=self.workspace, pos=wx.Point(150, 90),
                                                                     size=wx.Size(104, 15), style=0)
        self.cycleOnUnderwaterText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.cycleArray.append(self.cycleOnUnderwaterText)
        self.objects.append(self.cycleOnUnderwaterText)
        self.environmentalHideArray.append(self.cycleOnUnderwaterText)

    def initElectronicImages(self):
        self.airFilterFanPicture = wx.StaticBitmap(
            bitmap=wx.Bitmap(IMG_LOCATION + "airFilterFan.jpg", wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
            name=u'airFilterFanPicture', parent=self.workspace,
            pos=wx.Point(400, 312),
            size=wx.Size(50, 66), style=0)

        self.airHeaterPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "heater.jpg",
                                                                 wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                name=u'airHeaterPicture', parent=self.workspace,
                                                pos=wx.Point(400, 512), size=wx.Size(64, 56), style=0)


        self.ledPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "myLedLights.JPG",
                                                           wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                          name=u'ledPicture', parent=self.workspace, pos=wx.Point(400,
                                                                                                  592),
                                          size=wx.Size(64, 56),
                                          style=0)
        self.humidifierPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "humidifier.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'humidifierPicture', parent=self.workspace,
                                                 pos=wx.Point(400, 416), size=wx.Size(64, 56), style=0)
        self.waterHeaterPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "underwaterTemperature.jpg",
                                                                wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                               name=u'waterHeaterPicutre', parent=self.workspace,
                                               pos=wx.Point(180, 48), size=wx.Size(64, 56), style=0)

    def initRelayCheckBoxes(self):

        self.airFilterFanCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                                label=u'On/Off', name=u'airFilterFanCheckBox',
                                                parent=self.workspace, pos=wx.Point(472, 336),
                                                size=wx.Size(78, 15), style=0)
        self.airFilterFanCheckBox.SetValue(False)
        self.objects.append(self.airFilterFanCheckBox)
        self.manualArray.append(self.airFilterFanCheckBox)

        self.ledCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                       label=u'On/Off', name=u'ledCheckBox', parent=self.workspace,
                                       pos=wx.Point(472, 608), size=wx.Size(78, 15), style=0)
        self.ledCheckBox.SetValue(False)

        self.objects.append(self.ledCheckBox)
        self.manualArray.append(self.ledCheckBox)

        self.humidifierCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                              label=u'On/Off', name=u'humidifierCheckBox',
                                              parent=self.workspace, pos=wx.Point(472, 440),
                                              size=wx.Size(78, 15), style=0)
        self.humidifierCheckBox.SetValue(False)

        self.objects.append(self.humidifierCheckBox)
        self.manualArray.append(self.humidifierCheckBox)

        self.airHeaterCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                             label=u'On/Off', name=u'airHeaterCheckBox',
                                             parent=self.workspace, pos=wx.Point(472, 528),
                                             size=wx.Size(78, 15), style=0)
        self.airHeaterCheckBox.SetValue(False)

        self.objects.append(self.airHeaterCheckBox)
        self.manualArray.append(self.airHeaterCheckBox)

        self.underwaterHeaterCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'On/Off', name=u'waterAirCheckBox',
              parent=self.workspace, pos=wx.Point(250, 64), size=wx.Size(78,
              15), style=0)
        self.underwaterHeaterCheckBox.SetValue(False)

        self.objects.append(self.underwaterHeaterCheckBox)
        self.manualArray.append(self.underwaterHeaterCheckBox)

    def initRelayInputs(self):

        self.airFilterFanCycleOnValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'airFilterFanCycleOnValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(560, 336), size=wx.Size(48, 23),
                                                                        style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.airFilterFanCycleOnValue)
        self.objects.append(self.airFilterFanCycleOnValue)

        self.airFilterFanCycleOffValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                         name=u'airFilterFanCycleOffValue',
                                                                         parent=self.workspace,
                                                                         pos=wx.Point(688, 336), size=wx.Size(48, 23),
                                                                         style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.airFilterFanCycleOffValue)
        self.objects.append(self.airFilterFanCycleOffValue)

        self.airHeaterFanCycleOnValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'airHeaterFanCycleOnValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(560, 536), size=wx.Size(48, 23),
                                                                        style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.airHeaterFanCycleOnValue)
        self.objects.append(self.airHeaterFanCycleOnValue)
        self.environmentalHideArray.append(self.airHeaterFanCycleOnValue)

        self.airHeaterFanCycleOffValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                         name=u'airHeaterFanCycleOffValue',
                                                                         parent=self.workspace,
                                                                         pos=wx.Point(688, 536), size=wx.Size(48, 23),
                                                                         style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.airHeaterFanCycleOffValue)
        self.objects.append(self.airHeaterFanCycleOffValue)
        self.environmentalHideArray.append(self.airHeaterFanCycleOffValue)

        self.airHeaterHumidOnValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'airFilterHumidOnValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(560, 440), size=wx.Size(48, 23),
                                                                        style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.airHeaterHumidOnValue)
        self.objects.append(self.airHeaterHumidOnValue)
        self.environmentalHideArray.append(self.airHeaterHumidOnValue)

        self.airHeaterHumidOffValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                         name=u'airFilterHumidOffValue',
                                                                         parent=self.workspace,
                                                                         pos=wx.Point(688, 440), size=wx.Size(48, 23),
                                                                         style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.airHeaterHumidOffValue)
        self.objects.append(self.airHeaterHumidOffValue)

        self.environmentalHideArray.append(self.airHeaterHumidOffValue)
        self.underwaterOnValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'airFilterHumidOnValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(150, 106), size=wx.Size(48, 23),
                                                                        style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.underwaterOnValue)
        self.objects.append(self.underwaterOnValue)
        self.environmentalHideArray.append(self.underwaterOnValue)

        self.underwaterOffValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                         name=u'airFilterHumidOffValue',
                                                                         parent=self.workspace,
                                                                         pos=wx.Point(278, 106), size=wx.Size(48, 23),
                                                                         style=wx.TE_PROCESS_ENTER, value='0')
        self.cycleArray.append(self.underwaterOffValue)
        self.objects.append(self.underwaterOffValue)
        self.environmentalHideArray.append(self.underwaterOffValue)

        self.ledCycleOnValue = wx.TextCtrl(id=wx.ID_ANY,
                                                               name=u'ledCycleOnValue', parent=self.workspace,
                                                               pos=wx.Point(560, 603), size=wx.Size(48, 23), style=wx.TE_PROCESS_ENTER,
                                                               value='0')
        self.cycleArray.append(self.ledCycleOnValue)
        self.objects.append(self.ledCycleOnValue)

        self.ledCycleOffValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                name=u'ledCycleOffValue', parent=self.workspace,
                                                                pos=wx.Point(696, 603), size=wx.Size(48, 23), style=wx.TE_PROCESS_ENTER,
                                                                value='0')
        self.cycleArray.append(self.ledCycleOffValue)
        self.objects.append(self.ledCycleOffValue)

        self.cycleOnAirFIlterFan = wx.Choice(choices=['s', 'm', 'h'],
                                             id=wx.ID_ANY,
                                             name=u'cycleOnAirFIlterFan', parent=self.workspace,
                                             pos=wx.Point(608, 336), size=wx.Size(56, 23), style= wx.TE_PROCESS_ENTER, value= '0')
        self.cycleOnAirFIlterFan.SetSelection(0)
        self.cycleArray.append(self.cycleOnAirFIlterFan)
        self.objects.append(self.cycleOnAirFIlterFan)

        self.cycleOffAirHeaterFan = wx.Choice(choices=['s', 'm', 'h'],
                                              id=wx.ID_ANY,
                                              name=u'cycleOffAirFilterFan', parent=self.workspace,
                                              pos=wx.Point(736, 536), size=wx.Size(56, 23), style= wx.TE_PROCESS_ENTER, value = '0')
        self.cycleOffAirHeaterFan.SetSelection(0)
        self.cycleArray.append(self.cycleOffAirHeaterFan)
        self.objects.append(self.cycleOffAirHeaterFan)
        self.environmentalHideArray.append(self.cycleOffAirHeaterFan)

        self.cycleOnAirHeaterFan = wx.Choice(choices=['s', 'm', 'h'],
                                             id=wx.ID_ANY,
                                             name=u'cycleOnAirFIlterFan', parent=self.workspace,
                                             pos=wx.Point(608, 536), size=wx.Size(56, 23), style=0)
        self.cycleOnAirHeaterFan.SetSelection(0)
        self.cycleArray.append(self.cycleOnAirHeaterFan)
        self.objects.append(self.cycleOnAirHeaterFan)
        self.environmentalHideArray.append(self.cycleOnAirHeaterFan)

        self.cycleOffAirHumidFan = wx.Choice(choices=['s', 'm', 'h'],
                                              id=wx.ID_ANY,
                                              name=u'cycleOffAirFilterFan', parent=self.workspace,
                                              pos=wx.Point(736, 440), size=wx.Size(56, 23), style=0)
        self.cycleOffAirHumidFan.SetSelection(0)
        self.cycleArray.append(self.cycleOffAirHumidFan)
        self.objects.append(self.cycleOffAirHumidFan)
        self.environmentalHideArray.append(self.cycleOffAirHumidFan)

        self.cycleOnAirHumidFan = wx.Choice(choices=['s', 'm', 'h'],
                                             id=wx.ID_ANY,
                                             name=u'cycleOnAirFIlterFan', parent=self.workspace,
                                             pos=wx.Point(608, 440), size=wx.Size(56, 23), style=0)
        self.cycleOnAirHeaterFan.SetSelection(0)
        self.cycleArray.append(self.cycleOnAirHumidFan)
        self.objects.append(self.cycleOnAirHumidFan)
        self.environmentalHideArray.append(self.cycleOnAirHumidFan)

        self.cycleOffunderwater = wx.Choice(choices=['s', 'm', 'h'],
                                             id=wx.ID_ANY,
                                             name=u'cycleOffAirFilterFan', parent=self.workspace,
                                             pos=wx.Point(326, 106), size=wx.Size(56, 23), style=0)
        self.cycleOffunderwater.SetSelection(0)
        self.cycleArray.append(self.cycleOffunderwater)
        self.objects.append(self.cycleOffunderwater)
        self.environmentalHideArray.append(self.cycleOffunderwater)

        self.cycleOnunderwater = wx.Choice(choices=['s', 'm', 'h'],
                                            id=wx.ID_ANY,
                                            name=u'cycleOnAirFIlterFan', parent=self.workspace,
                                            pos=wx.Point(198, 106), size=wx.Size(56, 23), style=0)
        self.cycleOnunderwater.SetSelection(0)
        self.cycleArray.append(self.cycleOnunderwater)
        self.objects.append(self.cycleOnunderwater)
        self.environmentalHideArray.append(self.cycleOnunderwater)

        self.cycleOffAirFilterFan = wx.Choice(choices=['s', 'm', 'h'],
                                              id=wx.ID_ANY,
                                              name=u'cycleOffAirFilterFan', parent=self.workspace,
                                              pos=wx.Point(736, 336), size=wx.Size(56, 23), style=0)
        self.cycleOffAirFilterFan.SetSelection(0)
        self.cycleArray.append(self.cycleOffAirFilterFan)
        self.objects.append(self.cycleOffAirFilterFan)

        self.cycleOnLed = wx.Choice(choices=['s', 'm', 'h'],
                                    id=wx.ID_ANY, name=u'cycleOnLed',
                                    parent=self.workspace, pos=wx.Point(608, 603),
                                    size=wx.Size(56, 23), style=0)
        self.cycleOnLed.SetSelection(0)
        self.cycleArray.append(self.cycleOnLed)
        self.objects.append(self.cycleOnLed)

        self.cycleOffLed = wx.Choice(choices=['s', 'm', 'h'],
                                     id=wx.ID_ANY, name=u'cycleOffLed',
                                     parent=self.workspace, pos=wx.Point(744, 603),
                                     size=wx.Size(56, 23), style=0)
        self.cycleOffLed.SetSelection(0)
        self.cycleArray.append(self.cycleOffLed)
        self.objects.append(self.cycleOffLed)

    def initController(self,controller):
        self.electronicRelayC = controller

    def initListeners(self):
        self.airFilterFanCheckBox.Bind(wx.EVT_CHECKBOX, self.electronicRelayC.processAirFilterFanCheckbox)
        self.airFilterFanCycleOnValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processAirFilterCycleOn)
        self.airFilterFanCycleOffValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processAirFilterCycleOff)
        self.cycleOnAirFIlterFan.Bind(wx.EVT_CHOICE, self.electronicRelayC.processAirFilterCycleOnUnits)
        self.cycleOffAirFilterFan.Bind(wx.EVT_CHOICE, self.electronicRelayC.processAirFilterCycleOffUnits)
        
        self.airHeaterCheckBox.Bind(wx.EVT_CHECKBOX, self.electronicRelayC.processAirHeaterCheckbox)
        self.airHeaterFanCycleOnValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processAirHeaterCycleOn)
        self.airHeaterFanCycleOffValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processAirHeaterCycleOff)
        self.cycleOnAirHeaterFan.Bind(wx.EVT_CHOICE, self.electronicRelayC.processAirHeaterCycleOnUnits)
        self.cycleOffAirHeaterFan.Bind(wx.EVT_CHOICE, self.electronicRelayC.processAirHeaterCycleOffUnits)

        self.ledCheckBox.Bind(wx.EVT_CHECKBOX, self.electronicRelayC.processLedCheckbox)
        self.ledCycleOnValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processLedCycleOn)
        self.ledCycleOffValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processLedCycleOff)
        self.cycleOnLed.Bind(wx.EVT_CHOICE, self.electronicRelayC.processLedCycleOnUnits)
        self.cycleOffLed.Bind(wx.EVT_CHOICE, self.electronicRelayC.processLedCycleOffUnits)

        self.underwaterHeaterCheckBox.Bind(wx.EVT_CHECKBOX, self.electronicRelayC.processUnderwaterHeaterCheckbox)
        self.underwaterOnValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processUnderwaterHeaterCycleOn)
        self.underwaterOffValue.Bind(wx.EVT_TEXT_ENTER, self.electronicRelayC.processUnderwaterHeaterCycleOff)
        self.cycleOnunderwater.Bind(wx.EVT_CHOICE, self.electronicRelayC.processUnderwaterHeaterCycleOnUnits)
        self.cycleOffunderwater.Bind(wx.EVT_CHOICE, self.electronicRelayC.processUnderwaterHeaterCycleOffUnits)



