import wx
import WorkspaceView
IMG_LOCATION = WorkspaceView.IMG_LOCATION
class EvironmentalMonitorView:
    def __init__(self, workspace):
        self.workspace = workspace
        self.initStaticEnvironmentText()
        self.initSliders()

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
                                                                       name=u'humidityRangeStartValue',
                                                                       parent=self.workspace,
                                                                       pos=wx.Point(144, 512), size=wx.Size(40, 32),
                                                                       style=0, value='')
        self.genStaticText21 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText21', parent=self.workspace,
                                                             pos=wx.Point(216, 520), size=wx.Size(6, 15), style=0)
        self.genStaticText21.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                             wx.BOLD, False, u'Showcard Gothic'))
        self.genStaticText21.SetBackgroundColour(wx.Colour(143, 210, 250))

        self.humidityRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                     name=u'humidityRangeEndValue',
                                                                     parent=self.workspace,
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
                                                                        name=u'temperatureRangeEndValue',
                                                                        parent=self.workspace,
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


        self.underwaterRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                         label=u'underwater Range', name=u'underwaterRangeText',
                                                         parent=self.workspace, pos=wx.Point(32, 640),
                                                         size=wx.Size(82, 15), style=0)
        self.underwaterStartValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                 name=u'underwaterStartValue', parent=self.workspace,
                                                                 pos=wx.Point(144, 624), size=wx.Size(40, 31), style=0,
                                                                 value='')
        self.underwaterEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                               name=u'underwaterEndValue', parent=self.workspace,
                                                               pos=wx.Point(232, 624), size=wx.Size(40, 32), style=0,
                                                               value='')

