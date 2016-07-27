import wx


class MonitorView(wx.Panel):
    def __init__(self, appGUI):
        self.appGUI = appGUI
        #init Panel
        super(self.__class__, self).__init__(id=wx.ID_ANY, name=u'MenuPane',
                                 parent=self.appGUI, pos=wx.Point(0, 0), size=wx.Size(700, 50),
                                 style=wx.TAB_TRAVERSAL)

        self.SetToolTipString(u'')
        self.SetBackgroundColour(wx.Colour(114, 151, 250))
        self.SetMaxSize(wx.Size(700,50))
        self.SetFont(wx.Font(9, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
                              u'Modern No. 20'))
        self.initAirTempMonitor()
        self.initHumidityMonitor()
        self.initWaterTempMonitor()
    def initAirTempMonitor(self):
        self.AirTemp = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,label=u'Air Temperature:', name=u'AirTemp',
                                                     parent= self,pos=wx.Point(0, 15), size=wx.Size(89, 15),
                                                     style=0)
        self.AirTemp.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
                u'Modern No. 20'))
        self.TemperatureSensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'103.0 F', name=u'TemperatureSensor', parent=self,
               pos=wx.Point(140, 15), size=wx.Size(14, 16), style=0)
        self.TemperatureSensor.SetInitialSize(wx.Size(65, 15))
        self.TemperatureSensor.SetSizeHints(-1, -1, -1, -1)
        self.TemperatureSensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL, wx.BOLD,
               False, u'Lucida Handwriting'))
        self.TemperatureSensor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
    def initHumidityMonitor(self):
        self.humidityText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'Humidity:', name=u'humidityText', parent=self,
               pos=wx.Point(225, 15), size=wx.Size(56, 16), style=0)
        self.humidityText.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL, wx.NORMAL,
               False, u'Modern No. 20'))
        self.humiditySensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'100.0 %', name=u'humiditySensor', parent=self,
               pos=wx.Point(307, 15), size=wx.Size(56, 15), style=0)
        self.humiditySensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL, wx.BOLD,
               False, u'Lucida Handwriting'))
        self.humiditySensor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
    def initWaterTempMonitor(self):
        self.waterTemperatureText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'Water Temperature:', name=u'waterTemperatureText',
               parent=self, pos=wx.Point(360, 15), size=wx.Size(105,
               16), style=0)
        self.waterTemperatureText.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL,
               wx.NORMAL, False, u'Modern No. 20'))

        self.waterTemperatureSensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'100.0 F', name=u'waterTemperatureSensor', parent=self,
               pos=wx.Point(500, 15), size=wx.Size(65, 15), style=0)
        self.waterTemperatureSensor.SetInitialSize(wx.Size(65, 15))
        self.waterTemperatureSensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL,
               wx.NORMAL, False, u'Lucida Handwriting'))





