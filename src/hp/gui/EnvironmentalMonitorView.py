import wx
import WorkspaceView
IMG_LOCATION = WorkspaceView.IMG_LOCATION
SLIDERSTARTX = 360
STARTTEXTX = 32
STARTINPUTX = 185
STARTMIDDLETEXT = 220
STARTENDINPUTX = 290
STARTINPUTSIZEWIDTH = 60
class EvironmentalMonitorView:

    def __init__(self, workspace):
        self.workspace = workspace
        self.initStaticEnvironmentText()
        self.initSliders()

    def initSliders(self):
        #Humidity
        self.humidityRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                  maxValue=100, minValue=0, name=u'humidityRangeStartSlider',
                                                  parent=self.workspace, pos=wx.Point(16, 470),
                                                  size=wx.Size(SLIDERSTARTX, 24), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeStartSlider.SetPageSize(1)
        self.humidityRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                maxValue=100, minValue=0, name=u'humidityRangeEndSlider',
                                                parent=self.workspace, pos=wx.Point(16, 490),
                                                size=wx.Size(SLIDERSTARTX, 24), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeEndSlider.SetPageSize(1)
        #airTemperature
        self.temperatureRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                     maxValue=100, minValue=45, name=u'temperatureRangeStartSlider',
                                                     parent=self.workspace, pos=wx.Point(16, 420),
                                                     size=wx.Size(SLIDERSTARTX, 24), style=wx.SL_HORIZONTAL, value=45)
        self.temperatureRangeStartSlider.SetPageSize(1)

        self.temperatureRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                   maxValue=100, minValue=45, name=u'temperatureRangeEndSlider',
                                                   parent=self.workspace, pos=wx.Point(16, 440),
                                                   size=wx.Size(SLIDERSTARTX, 24), style=wx.SL_HORIZONTAL, value=0)
        self.temperatureRangeEndSlider.SetPageSize(1)
        # ph Sensor
        self.pHRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                            maxValue=12, minValue=0, name=u'pHRangeStartSlider',
                                            parent=self.workspace, pos=wx.Point(16, 520),
                                            size=wx.Size(SLIDERSTARTX, 24), style=wx.SL_HORIZONTAL, value=0)
        self.pHRangeStartSlider.SetPageSize(1)

        self.pHRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                          maxValue=12, minValue=0, name=u'pHRangeEndSlider',
                                          parent=self.workspace, pos=wx.Point(16, 540),
                                          size=wx.Size(SLIDERSTARTX, 24), style=wx.SL_HORIZONTAL, value=0)
        self.pHRangeEndSlider.SetPageSize(1)

    def initStaticEnvironmentText(self):
        self.temperatureRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'Temperature Range',
                                                                  name=u'temperatureRangeText',
                                                                  parent=self.workspace, pos=wx.Point(STARTTEXTX, 410),
                                                                  size=wx.Size(104, 13), style=0)
        self.temperatureRangeText.SetToolTipString(u'in Fahrenheit')
        self.temperatureRangeText.SetHelpText(u'in Fahrenheit')
        self.temperatureRangeText.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                               False))

        self.temperatureTextStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'F', name=u'temperatureTextStart',
                                                                  parent=self.workspace, pos=wx.Point(STARTINPUTX, 405),
                                                                  size=wx.Size(16, 10), style=0)
        self.temperatureTextStart.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                  wx.NORMAL, False, u'Segoe Print'))
        self.temperatureRangeEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'F', name=u'temperatureRangeEndText',
                                                                     parent=self.workspace, pos=wx.Point(STARTENDINPUTX, 405),
                                                                     size=wx.Size(16, 10), style=0)
        self.temperatureRangeEndText.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                     wx.NORMAL, False, u'Segoe Print'))
        self.genStaticText19 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText19', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 405), size=wx.Size(8, 10), style=0)
        self.genStaticText19.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.BOLD,
                                             False, u'Segoe UI'))
        self.genStaticText19.SetBackgroundColour(wx.Colour(167, 231, 252))
        # humidity



        self.humidityRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                               label=u'Humidity Range', name=u'humdiityRangeText',
                                                               parent=self.workspace, pos=wx.Point(STARTTEXTX, 460),
                                                               size=wx.Size(86, 15), style=0)
        self.humidityRangeText.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                               False))




        self.humidityPercentSignStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                      label=u'%', name=u'humidityPercentSignStart',
                                                                      parent=self.workspace, pos=wx.Point(STARTINPUTX, 460),
                                                                      size=wx.Size(15, 10), style=0)
        self.humidityPercentSignStart.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                      wx.NORMAL, False, u'Segoe Print'))

        self.humidityEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'%', name=u'humidityEndText', parent=self.workspace,
                                                             pos=wx.Point(STARTENDINPUTX, 460), size=wx.Size(15, 10), style=0)
        self.humidityEndText.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                             wx.NORMAL, False, u'Segoe Print'))





        self.genStaticText21 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText21', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 460), size=wx.Size(6, 10), style=0)
        self.genStaticText21.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                             wx.BOLD, False, u'Showcard Gothic'))
        self.genStaticText21.SetBackgroundColour(wx.Colour(143, 210, 250))


        # ph Sensor


        self.pHRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                         label=u'PH Level Range', name=u'pHRangeText',
                                                         parent=self.workspace, pos=wx.Point(STARTTEXTX, 510),
                                                         size=wx.Size(82, 15), style=0)
        self.pHRangeText.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                             wx.NORMAL, False, u'Showcard Gothic'))


        self.genStaticText23 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText23', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 505), size=wx.Size(6, 10), style=0)
        self.genStaticText23.SetBackgroundColour(wx.Colour(159, 221, 251))
        self.genStaticText23.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                             wx.BOLD, False, u'Showcard Gothic'))



        # underwater temp
        self.underwaterTemperatureRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'Water Temperature Rg.',
                                                                  name=u'temperatureRangeText',
                                                                  parent=self.workspace, pos=wx.Point(32, 560),
                                                                  size=wx.Size(104, 13), style=0)
        self.underwaterTemperatureRangeText.SetToolTipString(u'in Fahrenheit')
        self.underwaterTemperatureRangeText.SetHelpText(u'in Fahrenheit')
        self.underwaterTemperatureRangeText.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                               False))


        self.underwaterTemperatureTextStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'F', name=u'temperatureTextStart',
                                                                  parent=self.workspace, pos=wx.Point(STARTINPUTX, 600),
                                                                  size=wx.Size(16, 10), style=0)
        self.underwaterTemperatureTextStart.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                  wx.NORMAL, False, u'Segoe Print'))
        self.underwaterTemperatureRangeEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'F', name=u'temperatureRangeEndText',
                                                                     parent=self.workspace, pos=wx.Point(STARTENDINPUTX, 600),
                                                                     size=wx.Size(16, 10), style=0)
        self.underwaterTemperatureRangeEndText.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                     wx.NORMAL, False, u'Segoe Print'))
        self.genStaticText20 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText19', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 600), size=wx.Size(8, 10), style=0)
        self.genStaticText20.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.BOLD,
                                             False, u'Segoe UI'))
        self.genStaticText20.SetBackgroundColour(wx.Colour(167, 231, 252))

    def initEnvironmentInput(self):
        #temp
        self.temperatureRangeStartValue = wx.TextCtrl(id=wx.ID_ANY,
                                                      name=u'temperatureRangeStartValue', parent=self.workspace,
                                                      pos=wx.Point(144, 400), size=wx.Size(40, 25), style=0, value=u'')
        self.temperatureRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'temperatureRangeEndValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(240, 400), size=wx.Size(40, 25),
                                                                        style=0, value='')
        #humid
        self.humidityRangeStartValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                       name=u'humidityRangeStartValue',
                                                                       parent=self.workspace,
                                                                       pos=wx.Point(144, 455), size=wx.Size(40, 25),
                                                                       style=0, value='')
        self.humidityRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                     name=u'humidityRangeEndValue',
                                                                     parent=self.workspace,
                                                                     pos=wx.Point(240, 455), size=wx.Size(40, 25),
                                                                     style=0, value='')
        #ph

        self.pHLevelStartValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                 name=u'pHLevelStartValue', parent=self.workspace,
                                                                 pos=wx.Point(144, 505), size=wx.Size(40, 25), style=0,
                                                                 value='')
        self.phLevelEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                               name=u'phLevelEndValue', parent=self.workspace,
                                                               pos=wx.Point(240, 505), size=wx.Size(40, 25), style=0,
                                                               value='')
        #underwater
        self.underwaterTemperatureRangeStartValue = wx.TextCtrl(id=wx.ID_ANY,
                                                      name=u'temperatureRangeStartValue', parent=self.workspace,
                                                      pos=wx.Point(144, 555), size=wx.Size(40, 25), style=0, value=u'')
        self.underwaterTemperatureRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'temperatureRangeEndValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(240, 555), size=wx.Size(40, 25),
                                                                        style=0, value='')

