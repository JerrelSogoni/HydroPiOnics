import wx
import WorkspaceView

IMG_LOCATION = WorkspaceView.IMG_LOCATION

class ElectronicRelayEnviromentView:
    def __init__(self,workpace):
        self.workspace = workpace
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

        self.cycleOnAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
                                                                     parent=self.workspace, pos=wx.Point(560, 320),
                                                                     size=wx.Size(104, 15), style=0)
        self.cycleOnAirFIlterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))


        self.cycleOnLedText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Cycle On', name=u'cycleOnLedText',
                                                            parent=self.workspace, pos=wx.Point(560, 587),
                                                            size=wx.Size(104, 15), style=0)
        self.cycleOnLedText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))

        self.cycleOffLedText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'Cycle Off', name=u'cycleOffLedText',
                                                             parent=self.workspace, pos=wx.Point(696, 587),
                                                             size=wx.Size(104, 15), style=0)
        self.cycleOffLedText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.underwaterTitle = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                               label=u'Underwater Heater', name=u'underwaterHeaterTitle',
                                                               parent=self.workspace, pos=wx.Point(150, 32), size=wx.Size(104,
                                                                                                              15),
                                                               style=0)
        self.underwaterTitle.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
                                     False, u'Showcard Gothic'))

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

        self.ledCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                       label=u'On/Off', name=u'ledCheckBox', parent=self.workspace,
                                       pos=wx.Point(472, 608), size=wx.Size(78, 15), style=0)
        self.ledCheckBox.SetValue(False)

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

    def initRelayInputs(self):

        self.airFilterFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'airFilterFanCycleOnValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(560, 336), size=wx.Size(48, 23),
                                                                        style=0, value='')

        self.airFilterFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                         name=u'airFilterFanCycleOffValue',
                                                                         parent=self.workspace,
                                                                         pos=wx.Point(688, 336), size=wx.Size(48, 23),
                                                                         style=0, value='')

        self.ledCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                               name=u'ledCycleOnValue', parent=self.workspace,
                                                               pos=wx.Point(560, 603), size=wx.Size(48, 23), style=0,
                                                               value='')

        self.ledCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                name=u'ledCycleOffValue', parent=self.workspace,
                                                                pos=wx.Point(696, 603), size=wx.Size(48, 23), style=0,
                                                                value='')

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
                                    parent=self.workspace, pos=wx.Point(608, 603),
                                    size=wx.Size(56, 23), style=0)
        self.cycleOnLed.SetStringSelection(u'')
        self.cycleOnLed.SetSelection(0)

        self.cycleOffLed = wx.Choice(choices=['s', 'm', 'h'],
                                     id=wx.ID_ANY, name=u'cycleOffLed',
                                     parent=self.workspace, pos=wx.Point(744, 603),
                                     size=wx.Size(56, 23), style=0)
        self.cycleOffLed.SetSelection(0)



