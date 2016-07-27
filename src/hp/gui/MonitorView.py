import wx


class MonitorView(wx.Panel):
    def __init__(self, appGUI):
        self.appGUI = appGUI
        #init Panel
        super(self.__class__, self).__init__(id=wx.ID_ANY, name=u'MenuPane',
                                 parent=self.appGUI, pos=wx.Point(0, 0), size=wx.Size(950, 50),
                                 style=wx.TAB_TRAVERSAL)

        self.SetToolTipString(u'')
        self.SetBackgroundColour(wx.Colour(114, 151, 250))
        self.SetInitialSize(wx.Size(950, 50))
        self.SetFont(wx.Font(9, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
                              u'Modern No. 20'))

        self.initAirTempMonitor()
        self.initWaterTempMonitor()
    def initAirTempMonitor(self):
        self.AirTemp = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,label=u'Air Temperature:', name=u'AirTemp',
                                                     parent= self,pos=wx.Point(0, 17), size=wx.Size(89, 15),
                                                     style=0)
        self.AirTemp.SetFont(wx.Font(13, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
                u'Modern No. 20'))
        self.TemperatureSensor = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'3', name=u'TemperatureSensor', parent=self,
               pos=wx.Point(90, 15), size=wx.Size(14, 16), style=0)
        self.TemperatureSensor.SetInitialSize(wx.Size(65, 15))
        self.TemperatureSensor.SetSizeHints(-1, -1, -1, -1)
        self.TemperatureSensor.SetFont(wx.Font(13, wx.SCRIPT, wx.NORMAL, wx.BOLD,
               False, u'Lucida Handwriting'))
        self.TemperatureSensor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
    def initWaterTempMonitor(self):
        pass


