import wx


class MonitorView(wx.Panel):
    def __init__(self, appGUI):
        self.appGUI = appGUI
        #init Panel
        super(self.__class__, self).__init__(id=wx.ID_ANY, name=u'MenuPane',
                                 parent=self.appGUI, pos=wx.Point(0, 0), size=wx.Size(900, 50),
                                 style=wx.TAB_TRAVERSAL)

        self.SetToolTipString(u'')
        self.SetBackgroundColour(wx.Colour(114, 151, 250))
        self.SetMaxSize(wx.Size(900,50))
        self.SetFont(wx.Font(9, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
                              u'Modern No. 20'))
        self.initAirTempMonitor()
        self.initHumidityMonitor()
        self.initWaterTempMonitor()
        self.initPHMonitor()
    def initAirTempMonitor(self):
        self.AirTemp = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,label=u'Air Temperature:', name=u'AirTemp',
                                                     parent= self,pos=wx.Point(0, 15), size=wx.Size(89, 15),
                                                     style=0)
        self.AirTemp.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
                u'Modern No. 20'))
        self.TemperatureSensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'', name=u'TemperatureSensor', parent=self,
               pos=wx.Point(140, 15), size=wx.Size(14, 16), style=0)
        self.TemperatureSensor.SetInitialSize(wx.Size(65, 15))
        self.TemperatureSensor.SetSizeHints(-1, -1, -1, -1)
        self.TemperatureSensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL, wx.BOLD,
               False, u'Lucida Handwriting'))
        self.TemperatureSensor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
    def initHumidityMonitor(self):
        self.humidityText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'Humidity:', name=u'humidityText', parent=self,
               pos=wx.Point(235, 15), size=wx.Size(56, 16), style=0)
        self.humidityText.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL, wx.NORMAL,
               False, u'Modern No. 20'))
        self.humiditySensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'', name=u'humiditySensor', parent=self,
               pos=wx.Point(317, 15), size=wx.Size(56, 15), style=0)
        self.humiditySensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL, wx.BOLD,
               False, u'Lucida Handwriting'))
        self.humiditySensor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
    def initWaterTempMonitor(self):
        self.waterTemperatureText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'Water Temperature:', name=u'waterTemperatureText',
               parent=self, pos=wx.Point(420, 15), size=wx.Size(105,
               16), style=0)
        self.waterTemperatureText.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL,
               wx.NORMAL, False, u'Modern No. 20'))

        self.waterTemperatureSensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'', name=u'waterTemperatureSensor', parent=self,
               pos=wx.Point(587, 15), size=wx.Size(65, 15), style=0)
        self.waterTemperatureSensor.SetInitialSize(wx.Size(65, 15))
        self.waterTemperatureSensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL,
                                            wx.BOLD, False, u'Lucida Handwriting'))
    def initPHMonitor(self):
        self.pHText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'PH Level:', name=u'pHText', parent=self,
               pos=wx.Point(680, 15), size=wx.Size(51, 15), style=0)
        self.pHText.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
               u'Modern No. 20'))
        self.pHSensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'', name=u'pHSensor', parent=self,
               pos=wx.Point(757, 15), size=wx.Size(30, 15), style=0)
        self.pHSensor.SetInitialSize(wx.Size(30, 15))
        self.pHSensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL, wx.BOLD, False,
               u'Lucida Handwriting'))
    def getPHText(self):
        return self.pHSensor
    def getWaterTempText(self):
        return self.waterTemperatureSensor
    def getHumidityText(self):
        return self.humiditySensor
    def getAirTemperatureText(self):
        return self.TemperatureSensor
    def setPHText(self,ph):
        self.pHSensor.SetLabel(ph)
    def setWaterTempText(self,temp):
        self.waterTemperatureSensor.SetLabel(temp)
    def setHumidityText(self,humidity):
        self.humiditySensor.SetLabel(humidity)
    def setAirTemperatureText(self,temp):
        self.TemperatureSensor.SetLabel(temp)













