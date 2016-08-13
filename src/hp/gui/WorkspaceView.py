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
        self.environmentControlText.SetLabelText(u'Environmental Control')
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
        self.temperatureRangeText.SetToolTipString(u'in Fahrenheit')
        self.temperatureRangeText.SetHelpText(u'in Fahrenheit')

        self.humdiityRangeText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'Humidity Range', name=u'humdiityRangeText',
              parent=self, pos=wx.Point(32, 528),
              size=wx.Size(86, 15), style=0)

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

        self.humidityRangeStartSlider = wx.Slider(id=wx.ID_ANY,
              maxValue=100, minValue=0, name=u'humidityRangeStartSlider',
              parent=self, pos=wx.Point(16, 560),
              size=wx.Size(360, 32), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeStartSlider.SetPageSize(1)
        # self.humidityRangeStartSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnHumidityRangeStartSliderCommandScroll,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGESTARTSLIDER)

        self.humidityRangeEndSlider = wx.Slider(id=wx.ID_ANY,
              maxValue=100, minValue=0, name=u'humidityRangeEndSlider',
              parent=self, pos=wx.Point(16, 600),
              size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        self.humidityRangeEndSlider.SetPageSize(1)
        # self.humidityRangeEndSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnHumidityRangeEndSliderCommandScroll,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGEENDSLIDER)


