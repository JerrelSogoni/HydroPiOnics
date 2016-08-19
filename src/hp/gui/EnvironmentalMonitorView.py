import wx
import WorkspaceView
IMG_LOCATION = WorkspaceView.IMG_LOCATION
SLIDERSTARTWIDTH = 360
STARTTEXTX = 32
STARTSLIDERX = 16
STARTINPUTXSTATIC = 144
ENDINPUTXSTATIC = 240
STARTINPUTX = 205
STARTMIDDLETEXT = 225
STARTENDINPUTX = 300
STARTINPUTSIZEWIDTH = 60
class EvironmentalMonitorView:

    def __init__(self, workspace):
        self.workspace = workspace
        self.sliderArray = []
        self.environmentInputArray = []
        self.staticEnvironmentArray = []
        self.initStaticEnvironmentText()
        self.initSliders()
        self.initEnvironmentInput()
        self.environmentalMonitorC = None



    def initSliders(self):
        #Humidity
        self.humidityRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                  maxValue=100, minValue=0, name=u'humidityRangeStartSlider',
                                                  parent=self.workspace, pos=wx.Point(STARTSLIDERX, 470),
                                                  size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=50)
        self.humidityRangeStartSlider.SetPageSize(1)
        self.sliderArray.append(self.humidityRangeStartSlider)
        self.humidityRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                maxValue=100, minValue=0, name=u'humidityRangeEndSlider',
                                                parent=self.workspace, pos=wx.Point(STARTSLIDERX, 490),
                                                size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=50)
        self.humidityRangeEndSlider.SetPageSize(1)
        self.sliderArray.append(self.humidityRangeEndSlider)
        #airTemperature
        self.temperatureRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                     maxValue=100, minValue=45, name=u'temperatureRangeStartSlider',
                                                     parent=self.workspace, pos=wx.Point(STARTSLIDERX, 420),
                                                     size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=75)
        self.temperatureRangeStartSlider.SetPageSize(1)
        self.sliderArray.append(self.temperatureRangeStartSlider)
        self.temperatureRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                   maxValue=100, minValue=45, name=u'temperatureRangeEndSlider',
                                                   parent=self.workspace, pos=wx.Point(STARTSLIDERX, 440),
                                                   size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=75)
        self.temperatureRangeEndSlider.SetPageSize(1)
        self.sliderArray.append(self.temperatureRangeEndSlider)
        # ph Sensor
        self.pHRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                            maxValue=12, minValue=0, name=u'pHRangeStartSlider',
                                            parent=self.workspace, pos=wx.Point(STARTSLIDERX, 520),
                                            size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=6)
        self.pHRangeStartSlider.SetPageSize(1)
        self.sliderArray.append(self.pHRangeStartSlider)

        self.pHRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                          maxValue=12, minValue=0, name=u'pHRangeEndSlider',
                                          parent=self.workspace, pos=wx.Point(STARTSLIDERX, 540),
                                          size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=6)
        self.pHRangeEndSlider.SetPageSize(1)
        self.sliderArray.append(self.pHRangeEndSlider)
        #underwater
        self.underwaterTemperatureRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                     maxValue=100, minValue=45, name=u'temperatureRangeStartSlider',
                                                     parent=self.workspace, pos=wx.Point(STARTSLIDERX, 570),
                                                     size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=65)
        self.underwaterTemperatureRangeStartSlider.SetPageSize(1)
        self.sliderArray.append(self.underwaterTemperatureRangeStartSlider)

        self.underwaterTemperatureRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                   maxValue=100, minValue=45, name=u'temperatureRangeEndSlider',
                                                   parent=self.workspace, pos=wx.Point(STARTSLIDERX, 590),
                                                   size=wx.Size(SLIDERSTARTWIDTH, 24), style=wx.SL_HORIZONTAL, value=65)
        self.underwaterTemperatureRangeEndSlider.SetPageSize(1)
        self.sliderArray.append(self.underwaterTemperatureRangeEndSlider)

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
        self.staticEnvironmentArray.append(self.temperatureRangeText)

        self.temperatureTextStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'F', name=u'temperatureTextStart',
                                                                  parent=self.workspace, pos=wx.Point(STARTINPUTX, 405),
                                                                  size=wx.Size(16, 10), style=0)
        self.temperatureTextStart.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                  wx.NORMAL, False, u'Segoe Print'))
        self.staticEnvironmentArray.append(self.temperatureTextStart)
        self.temperatureRangeEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'F', name=u'temperatureRangeEndText',
                                                                     parent=self.workspace, pos=wx.Point(STARTENDINPUTX, 405),
                                                                     size=wx.Size(16, 10), style=0)
        self.temperatureRangeEndText.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                     wx.NORMAL, False, u'Segoe Print'))
        self.staticEnvironmentArray.append(self.temperatureRangeEndText)
        self.genStaticText19 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText19', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 405), size=wx.Size(8, 10), style=0)
        self.genStaticText19.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.BOLD,
                                             False, u'Segoe UI'))
        self.genStaticText19.SetBackgroundColour(wx.Colour(167, 231, 252))
        self.staticEnvironmentArray.append(self.genStaticText19)
        # humidity



        self.humidityRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                               label=u'Humidity Range', name=u'humdiityRangeText',
                                                               parent=self.workspace, pos=wx.Point(STARTTEXTX, 460),
                                                               size=wx.Size(86, 15), style=0)
        self.humidityRangeText.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                               False))
        self.staticEnvironmentArray.append(self.humidityRangeText)


        self.humidityPercentSignStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                      label=u'%', name=u'humidityPercentSignStart',
                                                                      parent=self.workspace, pos=wx.Point(STARTINPUTX, 460),
                                                                      size=wx.Size(15, 10), style=0)
        self.humidityPercentSignStart.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                      wx.NORMAL, False, u'Segoe Print'))
        self.staticEnvironmentArray.append(self.humidityPercentSignStart)

        self.humidityEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'%', name=u'humidityEndText', parent=self.workspace,
                                                             pos=wx.Point(STARTENDINPUTX, 460), size=wx.Size(15, 10), style=0)
        self.humidityEndText.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                             wx.NORMAL, False, u'Segoe Print'))
        self.staticEnvironmentArray.append(self.humidityEndText)


        self.genStaticText21 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText21', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 460), size=wx.Size(6, 10), style=0)
        self.genStaticText21.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                             wx.BOLD, False, u'Showcard Gothic'))
        self.genStaticText21.SetBackgroundColour(wx.Colour(143, 210, 250))
        self.staticEnvironmentArray.append(self.genStaticText21)


        # ph Sensor


        self.pHRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                         label=u'PH Level Range', name=u'pHRangeText',
                                                         parent=self.workspace, pos=wx.Point(STARTTEXTX, 510),
                                                         size=wx.Size(82, 15), style=0)
        self.pHRangeText.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                             wx.NORMAL, False, u'Showcard Gothic'))
        self.staticEnvironmentArray.append(self.pHRangeText)


        self.genStaticText23 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText23', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 510), size=wx.Size(6, 10), style=0)
        self.genStaticText23.SetBackgroundColour(wx.Colour(159, 221, 251))
        self.genStaticText23.SetFont(wx.Font(7, wx.DECORATIVE, wx.NORMAL,
                                             wx.BOLD, False, u'Showcard Gothic'))
        self.staticEnvironmentArray.append(self.genStaticText23)



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
        self.staticEnvironmentArray.append(self.underwaterTemperatureRangeText)


        self.underwaterTemperatureTextStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                  label=u'F', name=u'temperatureTextStart',
                                                                  parent=self.workspace, pos=wx.Point(STARTINPUTX, 560),
                                                                  size=wx.Size(16, 10), style=0)
        self.underwaterTemperatureTextStart.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                  wx.NORMAL, False, u'Segoe Print'))
        self.staticEnvironmentArray.append(self.underwaterTemperatureTextStart)
        self.underwaterTemperatureRangeEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                                     label=u'F', name=u'temperatureRangeEndText',
                                                                     parent=self.workspace, pos=wx.Point(STARTENDINPUTX, 560),
                                                                     size=wx.Size(16, 10), style=0)
        self.underwaterTemperatureRangeEndText.SetFont(wx.Font(7, wx.DEFAULT, wx.NORMAL,
                                                     wx.NORMAL, False, u'Segoe Print'))
        self.staticEnvironmentArray.append(self.underwaterTemperatureRangeEndText)
        self.genStaticText20 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                             label=u'-', name='genStaticText19', parent=self.workspace,
                                                             pos=wx.Point(STARTMIDDLETEXT, 560), size=wx.Size(8, 10), style=0)
        self.genStaticText20.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.BOLD,
                                             False, u'Segoe UI'))
        self.genStaticText20.SetBackgroundColour(wx.Colour(167, 231, 252))
        self.staticEnvironmentArray.append(self.genStaticText20)

    def initEnvironmentInput(self):
        #temp
        self.temperatureRangeStartValue = wx.TextCtrl(id=wx.ID_ANY,
                                                      name=u'temperatureRangeStartValue', parent=self.workspace,
                                                      pos=wx.Point(STARTINPUTXSTATIC, 400), size=wx.Size(STARTINPUTSIZEWIDTH, 25), style=0, value=u'75')
        self.temperatureRangeStartValue.SetEditable(False)
        self.environmentInputArray.append(self.temperatureRangeStartValue)
        self.temperatureRangeEndValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'temperatureRangeEndValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(ENDINPUTXSTATIC, 400), size=wx.Size(STARTINPUTSIZEWIDTH, 25),
                                                                        style=0, value='75')
        self.temperatureRangeStartValue.SetEditable(False)

        self.environmentInputArray.append(self.temperatureRangeEndValue)
        #humid
        self.humidityRangeStartValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                       name=u'humidityRangeStartValue',
                                                                       parent=self.workspace,
                                                                       pos=wx.Point(STARTINPUTXSTATIC, 455), size=wx.Size(STARTINPUTSIZEWIDTH, 25),
                                                                       style=0, value='50')
        self.humidityRangeStartValue.SetEditable(False)
        self.environmentInputArray.append(self.humidityRangeStartValue)
        self.humidityRangeEndValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                     name=u'humidityRangeEndValue',
                                                                     parent=self.workspace,
                                                                     pos=wx.Point(ENDINPUTXSTATIC, 455), size=wx.Size(STARTINPUTSIZEWIDTH, 25),
                                                                     style=0, value='50')
        self.humidityRangeEndValue.SetEditable(False)
        self.environmentInputArray.append(self.humidityRangeEndValue)
        #ph

        self.pHLevelStartValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                 name=u'pHLevelStartValue', parent=self.workspace,
                                                                 pos=wx.Point(STARTINPUTXSTATIC, 505), size=wx.Size(STARTINPUTSIZEWIDTH, 25), style=0,
                                                                 value='6')
        self.pHLevelStartValue.SetEditable(False)
        self.environmentInputArray.append(self.pHLevelStartValue)
        self.phLevelEndValue = wx.TextCtrl(id=wx.ID_ANY,
                                                               name=u'phLevelEndValue', parent=self.workspace,
                                                               pos=wx.Point(ENDINPUTXSTATIC, 505), size=wx.Size(STARTINPUTSIZEWIDTH, 25), style=0,
                                                               value='6')
        self.phLevelEndValue.SetEditable(False)
        self.environmentInputArray.append(self.phLevelEndValue)
        #underwater
        self.underwaterTemperatureRangeStartValue = wx.TextCtrl(id=wx.ID_ANY,
                                                      name=u'temperatureRangeStartValue', parent=self.workspace,
                                                      pos=wx.Point(STARTINPUTXSTATIC, 555), size=wx.Size(STARTINPUTSIZEWIDTH, 25), style=0, value=u'65')
        self.underwaterTemperatureRangeStartValue.SetEditable(False)
        self.environmentInputArray.append(self.underwaterTemperatureRangeStartValue)

        self.underwaterTemperatureRangeEndValue = wx.TextCtrl(id=wx.ID_ANY,
                                                                        name=u'temperatureRangeEndValue',
                                                                        parent=self.workspace,
                                                                        pos=wx.Point(ENDINPUTXSTATIC, 555), size=wx.Size(STARTINPUTSIZEWIDTH, 25),
                                                                        style=0, value='65')
        self.underwaterTemperatureRangeEndValue.SetEditable(False)
        self.environmentInputArray.append(self.underwaterTemperatureRangeEndValue)

    def initController(self, controller):
        self.environmentalMonitorC = controller

    def initListners(self):

        self.humidityRangeStartSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processHumidityStartValue)
        self.humidityRangeEndSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processHumidityEndValue)

        self.temperatureRangeStartSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processTemperatureStartValue)
        self.temperatureRangeEndSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processTemperatureEndValue)

        self.pHRangeStartSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processPHStartValue)
        self.pHRangeEndSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processPHEndValue)

        self.underwaterTemperatureRangeStartSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processUnderwaterStartValue)
        self.underwaterTemperatureRangeEndSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.environmentalMonitorC.processUnderwaterEndValue)



