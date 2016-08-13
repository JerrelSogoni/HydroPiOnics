import wx
import sys
import os

# Identify Operating System in order to direct image loading path
# Mac OS or Linux
DIRECTORY = os.getcwd()[:len(os.getcwd()) - 6]

if (sys.platform.startswith('darwin') or sys.platform.startswith('linux')):
    IMG_LOCATION = DIRECTORY + "Image//"
# Windows
elif (sys.platform.startswith('win32')):
    IMG_LOCATION = DIRECTORY + "Image\\"
class WorkspaceView(wx.Panel):
    def __init__(self, appGUI):
        self.appGUI = appGUI
        super(WorkspaceView, self).__init__(id=wx.ID_ANY, name =u'workspace', parent = self.appGUI,
                                            pos = wx.Point(0,50), size = wx.Size(950,800), style=wx.TAB_TRAVERSAL)
        self.SetMaxSize(wx.Size(950,800))
        self.SetBackgroundColour(wx.Colour(185, 242, 253))

        self.initGUIImages()
        self.initStaticText()
        self.initSliders()

    def initMotor(self):
        pass
    def initRelay(self):
        pass
    def initGUIImages(self):
        self.ventFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "ventFan.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'ventFanPicture', parent=self,
               pos=wx.Point(400, 136), size=wx.Size(64, 56), style=0)
        self.waterAirPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "air&pump.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'waterAirPicture', parent=self,
               pos=wx.Point(24, 48), size=wx.Size(64, 56), style=0)
        self.intakeFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "intakeFan.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'intakeFanPicture', parent=self,
               pos=wx.Point(400, 232), size=wx.Size(64, 56), style=0)

        self.airFilterFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "airFilterFan.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'airFilterFanPicture', parent=self,
               pos=wx.Point(408, 312), size=wx.Size(50, 66), style=0)

        self.humidifierPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "humidifier.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'humidifierPicture', parent=self,
               pos=wx.Point(400, 416), size=wx.Size(64, 56), style=0)

        self.mixToPlantPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'mixToPlantPicture', parent=self,
               pos=wx.Point(32, 136), size=wx.Size(50, 66), style=0)

        self.airHeaterPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "heater.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'airHeaterPicture', parent=self,
               pos=wx.Point(400, 512), size=wx.Size(64, 56), style=0)

        self.exhaustFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "exaustFan.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'exhaustFanPicture', parent=self,
               pos=wx.Point(400, 40), size=wx.Size(64, 56), style=0)

        self.ledPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "myLedLights.JPG",
              wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'ledPicture', parent=self, pos=wx.Point(400,
               592), size=wx.Size(64, 56), style=0)

        self.plantToMixPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'plantToMixPicture', parent=self,
               pos=wx.Point(32, 232), size=wx.Size(50, 66), style=0)

        self.mixToDrainPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
               wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
               name=u'mixToDrainPicture', parent=self,
               pos=wx.Point(32, 336), size=wx.Size(50, 66), style=0)

    def initStaticText(self):

        self.environmentControlText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'Environmental Control', name=u'environmentControlText',
               parent=self, pos=wx.Point(464, 8),
               size=wx.Size(154, 16), style=0)
        self.environmentControlText.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL,
               wx.NORMAL, False, u'Lucida Calligraphy'))

        self.intakeFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'Intake Fan', name=u'intakeFanText',
               parent=self, pos=wx.Point(400, 216),
               size=wx.Size(69, 15), style=0)
        self.intakeFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
               wx.NORMAL, False, u'Showcard Gothic'))

        self.ventFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
               label=u'Vent Fan', name=u'ventFanText',
               parent=self, pos=wx.Point(400, 120),
               size=wx.Size(56, 15), style=0)
        self.ventFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
               False, u'Showcard Gothic'))
        self.waterPumpAirTitle = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Water/Air Pump', name=u'waterPumpAirTitle',
              parent=self, pos=wx.Point(8, 32), size=wx.Size(104,
              15), style=0)
        self.waterPumpAirTitle.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))
        self.waterPumpAirTitle.SetToolTipString(u'')

        self.exhaustFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Exhaust Fan', name=u'exhaustFanText',
              parent=self, pos=wx.Point(392, 24),
              size=wx.Size(80, 15), style=0)
        self.exhaustFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))

        self.humidifierText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Humifier', name=u'humidifierText',
              parent=self, pos=wx.Point(400, 400),
              size=wx.Size(61, 15), style=0)
        self.humidifierText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))

        self.airHeaterText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Air Heater', name=u'airHeaterText',
              parent=self, pos=wx.Point(400, 496),
              size=wx.Size(68, 15), style=0)
        self.airHeaterText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))

        self.waterControlText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Water Control', name=u'waterControlText',
              parent=self, pos=wx.Point(24, 8), size=wx.Size(100,
              16), style=0)
        self.waterControlText.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL,
              wx.NORMAL, False, u'Lucida Handwriting'))
        self.waterControlText.SetToolTipString(u'')

        self.airFilterFanText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Air Filter Fan', name=u'airFilterFanText',
              parent=self, pos=wx.Point(384, 296),
              size=wx.Size(88, 15), style=0)
        self.airFilterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))

        self.mixToPlantText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Mix to Plant', name=u'mixToPlantText',
              parent=self, pos=wx.Point(16, 112),
              size=wx.Size(82, 15), style=0)
        self.mixToPlantText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))
        self.mixToPlantText.SetToolTipString(u'')

        self.plantToMixText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Plant to Mix', name=u'plantToMixText',
              parent=self, pos=wx.Point(16, 216),
              size=wx.Size(82, 15), style=0)
        self.plantToMixText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))
        self.plantToMixText.SetToolTipString(u'')

        self.mixToDrainText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Mix to Drain', name=u'mixToDrainText',
              parent=self, pos=wx.Point(16, 320),
              size=wx.Size(84, 15), style=0)
        self.mixToDrainText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.NORMAL, False, u'Showcard Gothic'))
        self.mixToDrainText.SetToolTipString(u'')

        self.temperatureRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Temperature Range', name=u'temperatureRangeText',
              parent=self, pos=wx.Point(32, 432),
              size=wx.Size(104, 15), style=0)
        self.temperatureRangeText.SetFont(wx.Font(5, wx.DECORATIVE, wx.NORMAL,
                    False))
        self.temperatureRangeText.SetToolTipString(u'in Fahrenheit')
        self.temperatureRangeText.SetHelpText(u'in Fahrenheit')

        self.humidityRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Humidity Range', name=u'humdiityRangeText',
              parent=self, pos=wx.Point(32, 528),
              size=wx.Size(86, 15), style=0)
        self.humidityRangeText.SetFont(wx.Font(5, wx.DECORATIVE, wx.NORMAL,
                    False))

        self.humidityRangeStartValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'humidityRangeStartValue', parent=self,
              pos=wx.Point(144, 512), size=wx.Size(40, 32), style=0, value='')
        # #self.humidityRangeStartValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnHumidityRangeStartValueTextEnter,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGESTARTVALUE)

        self.genStaticText21 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'-', name='genStaticText21', parent=self,
              pos=wx.Point(216, 520), size=wx.Size(6, 15), style=0)
        self.genStaticText21.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.BOLD, False, u'Showcard Gothic'))
        self.genStaticText21.SetBackgroundColour(wx.Colour(143, 210, 250))

        self.humidityRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'humidityRangeEndValue', parent=self,
              pos=wx.Point(240, 512), size=wx.Size(40, 32), style=0, value='')
        # self.humidityRangeEndValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnHumidityRangeEndValueTextEnter,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGEENDVALUE)


        self.ledText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'LEDs', name=u'ledText', parent=self,
              pos=wx.Point(416, 584), size=wx.Size(30, 15), style=0)
        self.ledText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
              False, u'Showcard Gothic'))
        self.temperatureRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Temperature Range', name=u'temperatureRangeText',
              parent=self, pos=wx.Point(32, 432),
              size=wx.Size(104, 15), style=0)
        self.temperatureRangeText.SetToolTipString(u'in Fahrenheit')
        self.temperatureRangeText.SetHelpText(u'in Fahrenheit')


        self.temperatureRangeStartValue = wx.TextCtrl(id=wx.ID_ANY,
              name=u'temperatureRangeStartValue', parent=self,
              pos=wx.Point(144, 424), size=wx.Size(40, 32), style=0, value=u'')
        # self.temperatureRangeStartValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnTemperatureRangeStartValueTextEnter,
        #       id=wxID_HYDROPIONICSTEMPERATURERANGESTARTVALUE)
        self.temperatureTextStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'F', name=u'temperatureTextStart',
              parent=self.scrolledPanel1, pos=wx.Point(184, 424),
              size=wx.Size(16, 36), style=0)
        self.temperatureTextStart.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
              wx.NORMAL, False, u'Segoe Print'))


        self.genStaticText19 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'-', name='genStaticText19', parent=self,
              pos=wx.Point(216, 424), size=wx.Size(8, 25), style=0)
        self.genStaticText19.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Segoe UI'))
        self.genStaticText19.SetBackgroundColour(wx.Colour(167, 231, 252))

        self.temperatureRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'temperatureRangeEndValue', parent=self,
              pos=wx.Point(240, 424), size=wx.Size(40, 32), style=0, value='')
        # self.temperatureRangeEndValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnTemperatureRangeEndValueTextEnter,
        #       id=wxID_HYDROPIONICSTEMPERATURERANGEENDVALUE)


        self.pHRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'PH Level Range', name=u'pHRangeText',
              parent=self, pos=wx.Point(32, 640),
              size=wx.Size(82, 15), style=0)

        self.pHLevelStartValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'pHLevelStartValue', parent=self,
              pos=wx.Point(144, 624), size=wx.Size(40, 31), style=0, value='')
        # self.pHLevelStartValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnPHLevelStartValueTextEnter,
        #       id=wxID_HYDROPIONICSPHLEVELSTARTVALUE)

        self.genStaticText23 = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'-', name='genStaticText23', parent=self,
              pos=wx.Point(208, 632), size=wx.Size(6, 15), style=0)
        self.genStaticText23.SetBackgroundColour(wx.Colour(159, 221, 251))
        self.genStaticText23.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
              wx.BOLD, False, u'Showcard Gothic'))

        self.phLevelEndValue = wx.lib.masked.textctrl.TextCtrl(id=wx.ID_ANY,
              name=u'phLevelEndValue', parent=self,
              pos=wx.Point(232, 624), size=wx.Size(40, 32), style=0, value='')
        # self.phLevelEndValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnPhLevelEndValueTextEnter,
        #       id=wxID_HYDROPIONICSPHLEVELENDVALUE)


        self.cycleOnWaterAirPumpText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Cycle On', name=u'cycleOnWaterAirPumpText',
              parent=self, pos=wx.Point(176, 72),
              size=wx.Size(96, 15), style=0)
        self.cycleOnWaterAirPumpText.SetToolTipString(u'')

        self.cycleOffWaterAirPumpText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Cycle Off', name=u'cycleOffWaterAirPumpText',
              parent=self, pos=wx.Point(280, 72),
              size=wx.Size(104, 15), style=0)

        self.temperatureRangeEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'F', name=u'temperatureRangeEndText',
              parent=self, pos=wx.Point(280, 424),
              size=wx.Size(16, 36), style=0)
        self.temperatureRangeEndText.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
              wx.NORMAL, False, u'Segoe Print'))

        self.humidityPercentSignStart = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'%', name=u'humidityPercentSignStart',
              parent=self, pos=wx.Point(184, 512),
              size=wx.Size(15, 36), style=0)
        self.humidityPercentSignStart.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
              wx.NORMAL, False, u'Segoe Print'))

        self.humidityEndText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'%', name=u'humidityEndText', parent=self,
              pos=wx.Point(280, 512), size=wx.Size(15, 36), style=0)
        self.humidityEndText.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
              wx.NORMAL, False, u'Segoe Print'))

    def initSliders(self):
        self.humidityRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                  maxValue=100, minValue=0, name=u'humidityRangeStartSlider',
                                                  parent=self, pos=wx.Point(16, 560),
                                                  size=wx.Size(360, 20), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeStartSlider.SetPageSize(1)
        # self.humidityRangeStartSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnHumidityRangeStartSliderCommandScroll,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGESTARTSLIDER)

        self.humidityRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                maxValue=100, minValue=0, name=u'humidityRangeEndSlider',
                                                parent=self, pos=wx.Point(16, 600),
                                                size=wx.Size(360, 20), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeEndSlider.SetPageSize(1)
        # self.humidityRangeEndSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnHumidityRangeEndSliderCommandScroll,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGEENDSLIDER)


        self.temperatureRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                                     maxValue=100, minValue=45, name=u'temperatureRangeStartSlider',
                                                     parent=self, pos=wx.Point(16, 456),
                                                     size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=45)
        self.temperatureRangeStartSlider.SetPageSize(1)
        # self.temperatureRangeStartSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #                                       self.OnTemperatureRangeStartSliderCommandScroll,
        #                                       id=wxID_HYDROPIONICSTEMPERATURERANGESTARTSLIDER)
        self.temperatureRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                                   maxValue=100, minValue=45, name=u'temperatureRangeEndSlider',
                                                   parent=self, pos=wx.Point(16, 488),
                                                   size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        self.temperatureRangeEndSlider.SetPageSize(1)
        # self.temperatureRangeEndSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #                                     self.OnTemperatureRangeEndSliderCommandScroll,
        #                                     id=wxID_HYDROPIONICSTEMPERATURERANGEENDSLIDER)

        self.pHRangeStartSlider = wx.Slider(id=wx.ID_ANY,
                                            maxValue=12, minValue=0, name=u'pHRangeStartSlider',
                                            parent=self, pos=wx.Point(16, 656),
                                            size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        self.pHRangeStartSlider.SetPageSize(1)
        # self.pHRangeStartSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #                              self.OnPHRangeStartSliderCommandScroll,
        #                              id=wxID_HYDROPIONICSPHRANGESTARTSLIDER)

        self.pHRangeEndSlider = wx.Slider(id=wx.ID_ANY,
                                          maxValue=12, minValue=0, name=u'pHRangeEndSlider',
                                          parent=self, pos=wx.Point(16, 680),
                                          size=wx.Size(360, 32), style=wx.SL_HORIZONTAL, value=0)
        self.pHRangeEndSlider.SetPageSize(1)
        # self.pHRangeEndSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #                            self.OnPHRangeEndSliderCommandScroll,
        #                            id=wxID_HYDROPIONICSPHRANGEENDSLIDER)







