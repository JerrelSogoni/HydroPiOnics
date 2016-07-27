

import wx
import wx.lib.masked.timectrl
import wx.lib.masked.combobox
import wx.lib.masked.textctrl
import wx.calendar
import wx.lib.stattext
import wx.lib.scrolledpanel
import wx.lib.buttons
import os
import sys
from gui.HydroPiOnicsView import HydroPiOnicsView
from data.HydroPiOnicsM import HydroPiOnicsM
from controller.HydroPiOnicsController import HydroPiOnicsController
from gui.MenuBarView import MenuBarView
from data.MenuBar import MenuBar
from controller.MenuBarController import MenuBarController
from gui.MonitorView import MonitorView
from data.Monitor import Monitor
from controller.MonitorController import MonitorController


def create(parent):
    return HydroPiOnics(parent)

# [wxID_HYDROPIONICS, wxID_HYDROPIONICSABOUTBUTTON,
#  wxID_HYDROPIONICSAIRFILTERFANCHECKBOX,
#  wxID_HYDROPIONICSAIRFILTERFANCYCLEOFFVALUE,
#  wxID_HYDROPIONICSAIRFILTERFANCYCLEONVALUE,
#  wxID_HYDROPIONICSAIRFILTERFANPICTURE, wxID_HYDROPIONICSAIRFILTERFANTEXT,
#  wxID_HYDROPIONICSAIRHEATERCHECKBOX, wxID_HYDROPIONICSAIRHEATERPICTURE,
#  wxID_HYDROPIONICSAIRHEATERTEXT, wxID_HYDROPIONICSAIRTEMP,
#  wxID_HYDROPIONICSCHECKPHCHECKBOX, wxID_HYDROPIONICSCUSTOMCONTROLTOGGLEBUTTON,
#  wxID_HYDROPIONICSCYCLEOFFAIRFILTERFAN,
#  wxID_HYDROPIONICSCYCLEOFFAIRFILTERFANTEXT,
#  wxID_HYDROPIONICSCYCLEOFFEXAUSTFAN, wxID_HYDROPIONICSCYCLEOFFINTAKEFAN,
#  wxID_HYDROPIONICSCYCLEOFFINTAKEFANTEXT, wxID_HYDROPIONICSCYCLEOFFLED,
#  wxID_HYDROPIONICSCYCLEOFFLEDTEXT, wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTTEXT,
#  wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTVALUE,
#  wxID_HYDROPIONICSCYCLEOFFPLANTMIXCYCLE, wxID_HYDROPIONICSCYCLEOFFVENTFAN,
#  wxID_HYDROPIONICSCYCLEOFFVENTFANTEXT,
#  wxID_HYDROPIONICSCYCLEOFFWATERAIRPUMPTEXT,
#  wxID_HYDROPIONICSCYCLEOFFWATERAIRPUMPVALUE,
#  wxID_HYDROPIONICSCYCLEOFFWATERPUMP, wxID_HYDROPIONICSCYCLEONAIRFILTERFAN,
#  wxID_HYDROPIONICSCYCLEONAIRFILTERFANTEXT, wxID_HYDROPIONICSCYCLEONEXAUSTFAN,
#  wxID_HYDROPIONICSCYCLEONINTAKEFAN, wxID_HYDROPIONICSCYCLEONINTAKEFANTEXT,
#  wxID_HYDROPIONICSCYCLEONLED, wxID_HYDROPIONICSCYCLEONLEDTEXT,
#  wxID_HYDROPIONICSCYCLEONMIXTOPLANTTEXT,
#  wxID_HYDROPIONICSCYCLEONMIXTOPLANTVALUE,
#  wxID_HYDROPIONICSCYCLEONPLANTMIXCYCLE, wxID_HYDROPIONICSCYCLEONVENTFAN,
#  wxID_HYDROPIONICSCYCLEONVENTFANTEXT,
#  wxID_HYDROPIONICSCYCLEONWATERAIRPUMPTEXT,
#  wxID_HYDROPIONICSCYCLEONWATERAIRPUMPVALUE, wxID_HYDROPIONICSCYCLEONWATERPUMP,
#  wxID_HYDROPIONICSDELAYSTARTCHECKBOX, wxID_HYDROPIONICSDELAYSTARTTIME,
#  wxID_HYDROPIONICSDRAINSYSTEMCHECKBOX,
#  wxID_HYDROPIONICSENVIRONMENTCONTROLTEXT,
#  wxID_HYDROPIONICSEXAUSTFANCYCLEOFFVALUE,
#  wxID_HYDROPIONICSEXAUSTFANCYCLEONTEXT,
#  wxID_HYDROPIONICSEXAUSTFANCYCLEONVALUE, wxID_HYDROPIONICSEXHAUSTFANCHECKBOX,
#  wxID_HYDROPIONICSEXHAUSTFANPICTURE, wxID_HYDROPIONICSEXHAUSTFANTEXT,
#  wxID_HYDROPIONICSGENBUTTON1, wxID_HYDROPIONICSGENSTATICTEXT19,
#  wxID_HYDROPIONICSGENSTATICTEXT21, wxID_HYDROPIONICSGENSTATICTEXT23,
#  wxID_HYDROPIONICSGENSTATICTEXT3, wxID_HYDROPIONICSHUMDIITYRANGETEXT,
#  wxID_HYDROPIONICSHUMIDIFIERCHECKBOX, wxID_HYDROPIONICSHUMIDIFIERPICTURE,
#  wxID_HYDROPIONICSHUMIDIFIERTEXT, wxID_HYDROPIONICSHUMIDITYENDTEXT,
#  wxID_HYDROPIONICSHUMIDITYPERCENTSIGNSTART,
#  wxID_HYDROPIONICSHUMIDITYRANGEENDSLIDER,
#  wxID_HYDROPIONICSHUMIDITYRANGEENDVALUE,
#  wxID_HYDROPIONICSHUMIDITYRANGESTARTSLIDER,
#  wxID_HYDROPIONICSHUMIDITYRANGESTARTVALUE, wxID_HYDROPIONICSHUMIDITYSENSOR,
#  wxID_HYDROPIONICSHUMIDITYTEXT, wxID_HYDROPIONICSINTAKEFANCHECKBOX,
#  wxID_HYDROPIONICSINTAKEFANCYCLEOFFVALUE,
#  wxID_HYDROPIONICSINTAKEFANCYCLEONVALUE, wxID_HYDROPIONICSINTAKEFANPICTURE,
#  wxID_HYDROPIONICSINTAKEFANTEXT, wxID_HYDROPIONICSLEDCHECKBOX,
#  wxID_HYDROPIONICSLEDCYCLEOFFVALUE, wxID_HYDROPIONICSLEDCYCLEONVALUE,
#  wxID_HYDROPIONICSLEDPICTURE, wxID_HYDROPIONICSLEDTEXT,
#  wxID_HYDROPIONICSMANUALTOGGLEBUTTON, wxID_HYDROPIONICSMENUPANE,
#  wxID_HYDROPIONICSMIXTODRAINCHECKBOX, wxID_HYDROPIONICSMIXTODRAINPICTURE,
#  wxID_HYDROPIONICSMIXTODRAINTEXT, wxID_HYDROPIONICSMIXTOPLANTCHECKBOX,
#  wxID_HYDROPIONICSMIXTOPLANTPICTURE, wxID_HYDROPIONICSMIXTOPLANTTEXT,
#  wxID_HYDROPIONICSPHLEVELENDVALUE, wxID_HYDROPIONICSPHLEVELSTARTVALUE,
#  wxID_HYDROPIONICSPHRANGEENDSLIDER, wxID_HYDROPIONICSPHRANGESTARTSLIDER,
#  wxID_HYDROPIONICSPHRANGETEXT, wxID_HYDROPIONICSPHSENSOR,
#  wxID_HYDROPIONICSPHTEXT, wxID_HYDROPIONICSPLANTOMIXCHECKBOX,
#  wxID_HYDROPIONICSPLANTTOMIXPICTURE, wxID_HYDROPIONICSPLANTTOMIXTEXT,
#  wxID_HYDROPIONICSSCROLLEDPANEL1, wxID_HYDROPIONICSSYSTEMSTATUS,
#  wxID_HYDROPIONICSSYSTEMSTATUSTEXT,
#  wxID_HYDROPIONICSTEMPERATURERANGEENDSLIDER,
#  wxID_HYDROPIONICSTEMPERATURERANGEENDTEXT,
#  wxID_HYDROPIONICSTEMPERATURERANGEENDVALUE,
#  wxID_HYDROPIONICSTEMPERATURERANGESTARTSLIDER,
#  wxID_HYDROPIONICSTEMPERATURERANGESTARTVALUE,
#  wxID_HYDROPIONICSTEMPERATURERANGETEXT, wxID_HYDROPIONICSTEMPERATURESENSOR,
#  wxID_HYDROPIONICSTEMPERATURETEXTSTART, wxID_HYDROPIONICSVENTFANCHECKBOX,
#  wxID_HYDROPIONICSVENTFANCYCLEOFFVALUE, wxID_HYDROPIONICSVENTFANCYCLEONVALUE,
#  wxID_HYDROPIONICSVENTFANPICTURE, wxID_HYDROPIONICSVENTFANTEXT,
#  wxID_HYDROPIONICSWATERAIRCHECKBOX, wxID_HYDROPIONICSWATERAIRPICTURE,
#  wxID_HYDROPIONICSWATERAIRPOWERSLIDER, wxID_HYDROPIONICSWATERAIRPOWERTEXT,
#  wxID_HYDROPIONICSWATERCONTROLTEXT, wxID_HYDROPIONICSWATERPUMPAIRTITLE,
#  wxID_HYDROPIONICSWATERTEMPERATURESENSOR,
#  wxID_HYDROPIONICSWATERTEMPERATURETEXT,
# ] = [wx.NewId() for _init_ctrls in range(122)]

class HydroPiOnics(wx.Frame):
    #Identify Operating System in order to direct image loading path
    #Mac OS or Linux
    DIRECTORY = os.getcwd()[:len(os.getcwd()) - 6]

    if(sys.platform.startswith('darwin') or sys.platform.startswith('linux')):
        IMG_LOCATION = DIRECTORY + "Image//"
    #Windows
    elif(sys.platform.startswith('win32')):
        IMG_LOCATION = DIRECTORY + "Image\\"
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        pass


        # self.manualToggleButton = wx.lib.buttons.GenToggleButton(id=wxID_HYDROPIONICSMANUALTOGGLEBUTTON,
        #       label=u'Manual', name=u'manualToggleButton', parent=self.MenuPane,
        #       pos=wx.Point(0, 0), size=wx.Size(112, 50), style=0)
        # self.manualToggleButton.SetBezelWidth(5)
        # self.manualToggleButton.SetToggle(True)
        # self.manualToggleButton.SetToolTipString(u'Mostly Used for Debugging')
        # self.manualToggleButton.SetHelpText(u'Gives Constant Power, Mostly Used for Debugging')
        # self.manualToggleButton.Bind(wx.EVT_LEFT_DCLICK,
        #       self.OnManualToggleButtonLeftDclick)
        #
        # self.customControlToggleButton = wx.lib.buttons.GenToggleButton(id=wxID_HYDROPIONICSCUSTOMCONTROLTOGGLEBUTTON,
        #       label=u'Custom Control', name=u'customControlToggleButton',
        #       parent=self.MenuPane, pos=wx.Point(112, 0), size=wx.Size(112, 50),
        #       style=0)
        # self.customControlToggleButton.SetBezelWidth(5)
        # self.customControlToggleButton.SetToggle(False)
        # self.customControlToggleButton.SetHelpText(u'Control Cycle and Enviroment')
        # self.customControlToggleButton.SetToolTipString(u'Control Cycle and Enviroment')
        #
        # self.genButton1 = wx.lib.buttons.GenButton(id=wxID_HYDROPIONICSGENBUTTON1,
        #       label='genButton1', name='genButton1', parent=self.MenuPane,
        #       pos=wx.Point(64, 168), size=wx.Size(112, 50), style=0)
        #
        # self.scrolledPanel1 = wx.lib.scrolledpanel.ScrolledPanel(id=wxID_HYDROPIONICSSCROLLEDPANEL1,
        #       name='scrolledPanel1', parent=self, pos=wx.Point(0, 50),
        #       size=wx.Size(950, 800), style=wx.TAB_TRAVERSAL)
        # self.scrolledPanel1.SetInitialSize(wx.Size(950, 800))
        # self.scrolledPanel1.SetBackgroundColour(wx.Colour(185, 242, 253))
        #
        # self.aboutButton = wx.lib.buttons.GenButton(id=wxID_HYDROPIONICSABOUTBUTTON,
        #       label=u'About', name=u'aboutButton', parent=self.MenuPane,
        #       pos=wx.Point(224, 0), size=wx.Size(112, 50), style=0)
        # self.aboutButton.SetBezelWidth(5)
        # self.aboutButton.SetHelpText(u'About this program')
        # self.aboutButton.SetToolTipString(u'About this program')
        #
        # self.exhaustFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSEXHAUSTFANCHECKBOX,
        #       label=u'On/Off', name=u'exhaustFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 56),
        #       size=wx.Size(78, 15), style=0)
        # self.exhaustFanCheckBox.Show(True)
        # self.exhaustFanCheckBox.Enable(False)
        # self.exhaustFanCheckBox.SetValue(True)
        # self.exhaustFanCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnExhaustFanCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSEXHAUSTFANCHECKBOX)
        #
        # self.ventFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "ventFan.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSVENTFANPICTURE,
        #       name=u'ventFanPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(400, 136), size=wx.Size(64, 56), style=0)
        #
        # self.waterAirPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "air&pump.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSWATERAIRPICTURE,
        #       name=u'waterAirPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(24, 48), size=wx.Size(64, 56), style=0)
        #
        # self.intakeFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "intakeFan.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSINTAKEFANPICTURE,
        #       name=u'intakeFanPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(400, 232), size=wx.Size(64, 56), style=0)
        #
        # self.airFilterFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "airFilterFan.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSAIRFILTERFANPICTURE,
        #       name=u'airFilterFanPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(408, 312), size=wx.Size(50, 66), style=0)
        #
        # self.humidifierPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "humidifier.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSHUMIDIFIERPICTURE,
        #       name=u'humidifierPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(400, 416), size=wx.Size(64, 56), style=0)
        #
        # self.mixToPlantPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "dcwaterPumps.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSMIXTOPLANTPICTURE,
        #       name=u'mixToPlantPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(32, 136), size=wx.Size(50, 66), style=0)
        # self.mixToPlantPicture.SetToolTipString(u'')
        #

        # self.humidityText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSHUMIDITYTEXT,
        #       label=u'Humidity:', name=u'humidityText', parent=self.MenuPane,
        #       pos=wx.Point(504, 16), size=wx.Size(56, 16), style=0)
        # self.humidityText.SetFont(wx.Font(9, wx.ROMAN, wx.NORMAL, wx.NORMAL,
        #       False, u'Modern No. 20'))
        #

        # self.TemperatureSensor = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSTEMPERATURESENSOR,
        #       label=u'', name=u'TemperatureSensor', parent=self.MenuPane,
        #       pos=wx.Point(434, 16), size=wx.Size(14, 16), style=0)
        # self.TemperatureSensor.SetMaxClientSize(wx.Size(65, 15))
        # self.TemperatureSensor.SetMinClientSize(wx.Size(40, 50))
        # self.TemperatureSensor.SetInitialSize(wx.Size(65, 15))
        # self.TemperatureSensor.SetSizeHints(-1, -1, -1, -1)
        # self.TemperatureSensor.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL, wx.BOLD,
        #       False, u'Lucida Handwriting'))
        # self.TemperatureSensor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        #
        # self.humiditySensor = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSHUMIDITYSENSOR,
        #       label=u'', name=u'humiditySensor', parent=self.MenuPane,
        #       pos=wx.Point(568, 16), size=wx.Size(65, 15), style=0)
        # self.humiditySensor.SetInitialSize(wx.Size(65, 50))
        # self.humiditySensor.SetMaxClientSize(wx.Size(65, 15))
        # self.humiditySensor.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL, wx.BOLD,
        #       False, u'Lucida Handwriting'))
        # self.humiditySensor.SetBackgroundColour(wx.Colour(255, 251, 251))
        # self.humiditySensor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        # self.humiditySensor.SetMinClientSize(wx.Size(65, 15))
        #
        # self.waterTemperatureSensor = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSWATERTEMPERATURESENSOR,
        #       label=u'', name=u'waterTemperatureSensor', parent=self.MenuPane,
        #       pos=wx.Point(752, 16), size=wx.Size(65, 15), style=0)
        # self.waterTemperatureSensor.SetInitialSize(wx.Size(65, 15))
        # self.waterTemperatureSensor.SetMaxClientSize(wx.Size(65, 15))
        # self.waterTemperatureSensor.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL,
        #       wx.NORMAL, False, u'Lucida Handwriting'))
        #
        # self.environmentControlText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSENVIRONMENTCONTROLTEXT,
        #       label=u'Environmental Control', name=u'environmentControlText',
        #       parent=self.scrolledPanel1, pos=wx.Point(464, 8),
        #       size=wx.Size(154, 16), style=0)
        # self.environmentControlText.SetLabelText(u'Environmental Control')
        # self.environmentControlText.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL,
        #       wx.NORMAL, False, u'Lucida Calligraphy'))
        #
        # self.airHeaterPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "heater.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSAIRHEATERPICTURE,
        #       name=u'airHeaterPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(400, 512), size=wx.Size(64, 56), style=0)
        #
        # self.pHText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSPHTEXT,
        #       label=u'PH Level:', name=u'pHText', parent=self.MenuPane,
        #       pos=wx.Point(824, 16), size=wx.Size(51, 15), style=0)
        # self.pHText.SetFont(wx.Font(9, wx.ROMAN, wx.NORMAL, wx.NORMAL, False,
        #       u'Modern No. 20'))
        #
        # self.pHSensor = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSPHSENSOR,
        #       label=u'', name=u'pHSensor', parent=self.MenuPane,
        #       pos=wx.Point(880, 16), size=wx.Size(30, 15), style=0)
        # self.pHSensor.SetInitialSize(wx.Size(30, 15))
        # self.pHSensor.SetMaxClientSize(wx.Size(30, 15))
        # self.pHSensor.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL, wx.NORMAL, False,
        #       u'Lucida Handwriting'))
        #
        # self.ventFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSVENTFANCHECKBOX,
        #       label=u'On/Off', name=u'ventFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 152),
        #       size=wx.Size(78, 15), style=0)
        # self.ventFanCheckBox.SetValue(True)
        #
        # self.waterAirCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSWATERAIRCHECKBOX,
        #       label=u'On/Off', name=u'waterAirCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 64), size=wx.Size(78,
        #       15), style=0)
        # self.waterAirCheckBox.SetValue(False)
        # self.waterAirCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnWaterAirCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSWATERAIRCHECKBOX)
        #
        # self.intakeFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSINTAKEFANCHECKBOX,
        #       label=u'On/Off', name=u'intakeFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 248),
        #       size=wx.Size(78, 15), style=0)
        # self.intakeFanCheckBox.SetValue(True)
        #
        # self.humidifierCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSHUMIDIFIERCHECKBOX,
        #       label=u'On/Off', name=u'humidifierCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 440),
        #       size=wx.Size(78, 15), style=0)
        # self.humidifierCheckBox.SetValue(True)
        #
        # self.airHeaterCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSAIRHEATERCHECKBOX,
        #       label=u'On/Off', name=u'airHeaterCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 528),
        #       size=wx.Size(78, 15), style=0)
        # self.airHeaterCheckBox.SetValue(True)
        #
        # self.exhaustFanPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "exaustFan.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSEXHAUSTFANPICTURE,
        #       name=u'exhaustFanPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(400, 40), size=wx.Size(64, 56), style=0)
        #
        # self.intakeFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSINTAKEFANTEXT,
        #       label=u'Intake Fan', name=u'intakeFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(400, 216),
        #       size=wx.Size(69, 15), style=0)
        # self.intakeFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        #
        # self.ventFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSVENTFANTEXT,
        #       label=u'Vent Fan', name=u'ventFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(400, 120),
        #       size=wx.Size(56, 15), style=0)
        # self.ventFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
        #       False, u'Showcard Gothic'))
        #
        # self.waterPumpAirTitle = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSWATERPUMPAIRTITLE,
        #       label=u'Water/Air Pump', name=u'waterPumpAirTitle',
        #       parent=self.scrolledPanel1, pos=wx.Point(8, 32), size=wx.Size(104,
        #       15), style=0)
        # self.waterPumpAirTitle.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        # self.waterPumpAirTitle.SetToolTipString(u'')
        #
        # self.exhaustFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSEXHAUSTFANTEXT,
        #       label=u'Exhaust Fan', name=u'exhaustFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(392, 24),
        #       size=wx.Size(80, 15), style=0)
        # self.exhaustFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        #
        # self.humidifierText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSHUMIDIFIERTEXT,
        #       label=u'Humifier', name=u'humidifierText',
        #       parent=self.scrolledPanel1, pos=wx.Point(400, 400),
        #       size=wx.Size(61, 15), style=0)
        # self.humidifierText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        #
        # self.airHeaterText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSAIRHEATERTEXT,
        #       label=u'Air Heater', name=u'airHeaterText',
        #       parent=self.scrolledPanel1, pos=wx.Point(400, 496),
        #       size=wx.Size(68, 15), style=0)
        # self.airHeaterText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        #
        # self.waterControlText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSWATERCONTROLTEXT,
        #       label=u'Water Control', name=u'waterControlText',
        #       parent=self.scrolledPanel1, pos=wx.Point(24, 8), size=wx.Size(100,
        #       16), style=0)
        # self.waterControlText.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL,
        #       wx.NORMAL, False, u'Lucida Handwriting'))
        # self.waterControlText.SetToolTipString(u'')
        #
        # self.airFilterFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSAIRFILTERFANTEXT,
        #       label=u'Air Filter Fan', name=u'airFilterFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(384, 296),
        #       size=wx.Size(88, 15), style=0)
        # self.airFilterFanText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        #
        # self.airFilterFanCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSAIRFILTERFANCHECKBOX,
        #       label=u'On/Off', name=u'airFilterFanCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(472, 336),
        #       size=wx.Size(78, 15), style=0)
        # self.airFilterFanCheckBox.SetValue(True)
        #
        # self.ledPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "myLedLights.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSLEDPICTURE,
        #       name=u'ledPicture', parent=self.scrolledPanel1, pos=wx.Point(400,
        #       592), size=wx.Size(64, 56), style=0)
        #
        # self.ledText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSLEDTEXT,
        #       label=u'LEDs', name=u'ledText', parent=self.scrolledPanel1,
        #       pos=wx.Point(416, 584), size=wx.Size(30, 15), style=0)
        # self.ledText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL,
        #       False, u'Showcard Gothic'))
        #
        # self.ledCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSLEDCHECKBOX,
        #       label=u'On/Off', name=u'ledCheckBox', parent=self.scrolledPanel1,
        #       pos=wx.Point(472, 608), size=wx.Size(78, 15), style=0)
        # self.ledCheckBox.SetValue(False)
        #
        # self.mixToPlantText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSMIXTOPLANTTEXT,
        #       label=u'Mix to Plant', name=u'mixToPlantText',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 112),
        #       size=wx.Size(82, 15), style=0)
        # self.mixToPlantText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        # self.mixToPlantText.SetToolTipString(u'')
        #
        # self.plantToMixText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSPLANTTOMIXTEXT,
        #       label=u'Plant to Mix', name=u'plantToMixText',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 216),
        #       size=wx.Size(82, 15), style=0)
        # self.plantToMixText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        # self.plantToMixText.SetToolTipString(u'')
        #
        # self.mixToDrainText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSMIXTODRAINTEXT,
        #       label=u'Mix to Drain', name=u'mixToDrainText',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 320),
        #       size=wx.Size(84, 15), style=0)
        # self.mixToDrainText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.NORMAL, False, u'Showcard Gothic'))
        # self.mixToDrainText.SetToolTipString(u'')
        #
        # self.plantToMixPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "dcwaterPumps.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSPLANTTOMIXPICTURE,
        #       name=u'plantToMixPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(32, 232), size=wx.Size(50, 66), style=0)
        # self.plantToMixPicture.SetToolTipString(u'')
        #
        # self.mixToDrainPicture = wx.StaticBitmap(bitmap=wx.Bitmap(self.IMG_LOCATION + "dcwaterPumps.jpg",
        #       wx.BITMAP_TYPE_JPEG), id=wxID_HYDROPIONICSMIXTODRAINPICTURE,
        #       name=u'mixToDrainPicture', parent=self.scrolledPanel1,
        #       pos=wx.Point(32, 336), size=wx.Size(50, 66), style=0)
        #
        # self.mixToPlantCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSMIXTOPLANTCHECKBOX,
        #       label=u'On/Off', name=u'mixToPlantCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 160),
        #       size=wx.Size(78, 15), style=0)
        # self.mixToPlantCheckBox.SetValue(True)
        # self.mixToPlantCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnMixToPlantCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSMIXTOPLANTCHECKBOX)
        #
        # self.planToMixCheckbox = wx.CheckBox(id=wxID_HYDROPIONICSPLANTOMIXCHECKBOX,
        #       label=u'On/Off', name=u'planToMixCheckbox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 256),
        #       size=wx.Size(84, 15), style=0)
        # self.planToMixCheckbox.SetValue(True)
        # self.planToMixCheckbox.Bind(wx.EVT_CHECKBOX,
        #       self.OnPlanToMixCheckboxCheckbox,
        #       id=wxID_HYDROPIONICSPLANTOMIXCHECKBOX)
        #
        # self.mixToDrainCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSMIXTODRAINCHECKBOX,
        #       label=u'On/Off', name=u'mixToDrainCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(96, 360),
        #       size=wx.Size(84, 15), style=0)
        # self.mixToDrainCheckBox.SetValue(True)
        # self.mixToDrainCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnMixToDrainCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSMIXTODRAINCHECKBOX)
        #
        # self.temperatureRangeText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSTEMPERATURERANGETEXT,
        #       label=u'Temperature Range', name=u'temperatureRangeText',
        #       parent=self.scrolledPanel1, pos=wx.Point(32, 432),
        #       size=wx.Size(104, 15), style=0)
        # self.temperatureRangeText.SetToolTipString(u'in Fahrenheit')
        # self.temperatureRangeText.SetHelpText(u'in Fahrenheit')
        #
        # self.temperatureRangeStartSlider = wx.Slider(id=wxID_HYDROPIONICSTEMPERATURERANGESTARTSLIDER,
        #       maxValue=100, minValue=45, name=u'temperatureRangeStartSlider',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 456),
        #       size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=45)
        # self.temperatureRangeStartSlider.SetMin(45)
        # self.temperatureRangeStartSlider.SetPageSize(1)
        # self.temperatureRangeStartSlider.SetThumbLength(25)
        # self.temperatureRangeStartSlider.SetLabel(u'')
        # self.temperatureRangeStartSlider.SetLabelText(u'')
        # self.temperatureRangeStartSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnTemperatureRangeStartSliderCommandScroll,
        #       id=wxID_HYDROPIONICSTEMPERATURERANGESTARTSLIDER)
        #
        # self.temperatureRangeStartValue = wx.TextCtrl(id=wxID_HYDROPIONICSTEMPERATURERANGESTARTVALUE,
        #       name=u'temperatureRangeStartValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(144, 424), size=wx.Size(40, 32), style=0, value=u'')
        # self.temperatureRangeStartValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnTemperatureRangeStartValueTextEnter,
        #       id=wxID_HYDROPIONICSTEMPERATURERANGESTARTVALUE)
        #
        # self.genStaticText19 = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSGENSTATICTEXT19,
        #       label=u'-', name='genStaticText19', parent=self.scrolledPanel1,
        #       pos=wx.Point(216, 424), size=wx.Size(8, 25), style=0)
        # self.genStaticText19.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
        #       False, u'Segoe UI'))
        # self.genStaticText19.SetBackgroundColour(wx.Colour(167, 231, 252))
        #
        # self.temperatureRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSTEMPERATURERANGEENDVALUE,
        #       name=u'temperatureRangeEndValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(240, 424), size=wx.Size(40, 32), style=0, value='')
        # self.temperatureRangeEndValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnTemperatureRangeEndValueTextEnter,
        #       id=wxID_HYDROPIONICSTEMPERATURERANGEENDVALUE)
        #
        # self.temperatureRangeEndSlider = wx.Slider(id=wxID_HYDROPIONICSTEMPERATURERANGEENDSLIDER,
        #       maxValue=100, minValue=45, name=u'temperatureRangeEndSlider',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 488),
        #       size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        # self.temperatureRangeEndSlider.SetPageSize(1)
        # self.temperatureRangeEndSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnTemperatureRangeEndSliderCommandScroll,
        #       id=wxID_HYDROPIONICSTEMPERATURERANGEENDSLIDER)
        #
        # self.humdiityRangeText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSHUMDIITYRANGETEXT,
        #       label=u'Humidity Range', name=u'humdiityRangeText',
        #       parent=self.scrolledPanel1, pos=wx.Point(32, 528),
        #       size=wx.Size(86, 15), style=0)
        #
        # self.humidityRangeStartValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSHUMIDITYRANGESTARTVALUE,
        #       name=u'humidityRangeStartValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(144, 512), size=wx.Size(40, 32), style=0, value='')
        # self.humidityRangeStartValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnHumidityRangeStartValueTextEnter,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGESTARTVALUE)
        #
        # self.genStaticText21 = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSGENSTATICTEXT21,
        #       label=u'-', name='genStaticText21', parent=self.scrolledPanel1,
        #       pos=wx.Point(216, 520), size=wx.Size(6, 15), style=0)
        # self.genStaticText21.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.BOLD, False, u'Showcard Gothic'))
        # self.genStaticText21.SetBackgroundColour(wx.Colour(143, 210, 250))
        #
        # self.humidityRangeEndValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSHUMIDITYRANGEENDVALUE,
        #       name=u'humidityRangeEndValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(240, 512), size=wx.Size(40, 32), style=0, value='')
        # self.humidityRangeEndValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnHumidityRangeEndValueTextEnter,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGEENDVALUE)
        #
        # self.humidityRangeStartSlider = wx.Slider(id=wxID_HYDROPIONICSHUMIDITYRANGESTARTSLIDER,
        #       maxValue=100, minValue=0, name=u'humidityRangeStartSlider',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 560),
        #       size=wx.Size(360, 32), style=wx.SL_HORIZONTAL, value=0)
        # self.humidityRangeStartSlider.SetPageSize(1)
        # self.humidityRangeStartSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnHumidityRangeStartSliderCommandScroll,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGESTARTSLIDER)
        #
        # self.humidityRangeEndSlider = wx.Slider(id=wxID_HYDROPIONICSHUMIDITYRANGEENDSLIDER,
        #       maxValue=100, minValue=0, name=u'humidityRangeEndSlider',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 600),
        #       size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        # self.humidityRangeEndSlider.SetPageSize(1)
        # self.humidityRangeEndSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnHumidityRangeEndSliderCommandScroll,
        #       id=wxID_HYDROPIONICSHUMIDITYRANGEENDSLIDER)
        #
        # self.pHRangeText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSPHRANGETEXT,
        #       label=u'PH Level Range', name=u'pHRangeText',
        #       parent=self.scrolledPanel1, pos=wx.Point(32, 640),
        #       size=wx.Size(82, 15), style=0)
        #
        # self.pHLevelStartValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSPHLEVELSTARTVALUE,
        #       name=u'pHLevelStartValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(144, 624), size=wx.Size(40, 31), style=0, value='')
        # self.pHLevelStartValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnPHLevelStartValueTextEnter,
        #       id=wxID_HYDROPIONICSPHLEVELSTARTVALUE)
        #
        # self.genStaticText23 = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSGENSTATICTEXT23,
        #       label=u'-', name='genStaticText23', parent=self.scrolledPanel1,
        #       pos=wx.Point(208, 632), size=wx.Size(6, 15), style=0)
        # self.genStaticText23.SetBackgroundColour(wx.Colour(159, 221, 251))
        # self.genStaticText23.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
        #       wx.BOLD, False, u'Showcard Gothic'))
        #
        # self.phLevelEndValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSPHLEVELENDVALUE,
        #       name=u'phLevelEndValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(232, 624), size=wx.Size(40, 32), style=0, value='')
        # self.phLevelEndValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnPhLevelEndValueTextEnter,
        #       id=wxID_HYDROPIONICSPHLEVELENDVALUE)
        #
        # self.pHRangeStartSlider = wx.Slider(id=wxID_HYDROPIONICSPHRANGESTARTSLIDER,
        #       maxValue=12, minValue=0, name=u'pHRangeStartSlider',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 656),
        #       size=wx.Size(360, 24), style=wx.SL_HORIZONTAL, value=0)
        # self.pHRangeStartSlider.SetPageSize(1)
        # self.pHRangeStartSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnPHRangeStartSliderCommandScroll,
        #       id=wxID_HYDROPIONICSPHRANGESTARTSLIDER)
        #
        # self.pHRangeEndSlider = wx.Slider(id=wxID_HYDROPIONICSPHRANGEENDSLIDER,
        #       maxValue=12, minValue=0, name=u'pHRangeEndSlider',
        #       parent=self.scrolledPanel1, pos=wx.Point(16, 680),
        #       size=wx.Size(360, 32), style=wx.SL_HORIZONTAL, value=0)
        # self.pHRangeEndSlider.SetPageSize(1)
        # self.pHRangeEndSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnPHRangeEndSliderCommandScroll,
        #       id=wxID_HYDROPIONICSPHRANGEENDSLIDER)
        #
        # self.waterAirPowerText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSWATERAIRPOWERTEXT,
        #       label=u'Water/Air Power', name=u'waterAirPowerText',
        #       parent=self.scrolledPanel1, pos=wx.Point(200, 32),
        #       size=wx.Size(87, 15), style=0)
        # self.waterAirPowerText.SetToolTipString(u'')
        #
        # self.waterAirPowerSlider = wx.Slider(id=wxID_HYDROPIONICSWATERAIRPOWERSLIDER,
        #       maxValue=255, minValue=100, name=u'waterAirPowerSlider',
        #       parent=self.scrolledPanel1, pos=wx.Point(168, 48),
        #       size=wx.Size(216, 24), style=wx.SL_HORIZONTAL, value=100)
        # self.waterAirPowerSlider.SetLabel(u'')
        # self.waterAirPowerSlider.SetMax(255)
        # self.waterAirPowerSlider.SetPageSize(1)
        # self.waterAirPowerSlider.SetMin(100)
        # self.waterAirPowerSlider.Bind(wx.EVT_COMMAND_SCROLL,
        #       self.OnWaterAirPowerSliderCommandScroll,
        #       id=wxID_HYDROPIONICSWATERAIRPOWERSLIDER)
        #
        # self.cycleOnWaterAirPumpText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONWATERAIRPUMPTEXT,
        #       label=u'Cycle On', name=u'cycleOnWaterAirPumpText',
        #       parent=self.scrolledPanel1, pos=wx.Point(176, 72),
        #       size=wx.Size(96, 15), style=0)
        # self.cycleOnWaterAirPumpText.SetToolTipString(u'')
        #
        # self.cycleOffWaterAirPumpText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFWATERAIRPUMPTEXT,
        #       label=u'Cycle Off', name=u'cycleOffWaterAirPumpText',
        #       parent=self.scrolledPanel1, pos=wx.Point(280, 72),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOnWaterAirPumpValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEONWATERAIRPUMPVALUE,
        #       name=u'cycleOnWaterAirPumpValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(176, 88), size=wx.Size(48, 23), style=0, value='')
        # self.cycleOnWaterAirPumpValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOnWaterAirPumpValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEONWATERAIRPUMPVALUE)
        #
        # self.cycleOffWaterAirPumpValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEOFFWATERAIRPUMPVALUE,
        #       name=u'cycleOffWaterAirPumpValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(280, 88), size=wx.Size(56, 23), style=0, value='')
        # self.cycleOffWaterAirPumpValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOffWaterAirPumpValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEOFFWATERAIRPUMPVALUE)
        #
        # self.cycleOnMixToPlantText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONMIXTOPLANTTEXT,
        #       label=u'Cycle On', name=u'cycleOnMixToPlantText',
        #       parent=self.scrolledPanel1, pos=wx.Point(176, 184),
        #       size=wx.Size(96, 15), style=0)
        #
        # self.cycleOffMixToPlantText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTTEXT,
        #       label=u'Cycle Off', name=u'cycleOffMixToPlantText',
        #       parent=self.scrolledPanel1, pos=wx.Point(280, 184),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOnMixToPlantValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEONMIXTOPLANTVALUE,
        #       name=u'cycleOnMixToPlantValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(176, 200), size=wx.Size(48, 24), style=0, value='')
        # self.cycleOnMixToPlantValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOnMixToPlantValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEONMIXTOPLANTVALUE)
        #
        # self.cycleOffMixToPlantValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTVALUE,
        #       name=u'cycleOffMixToPlantValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(280, 200), size=wx.Size(56, 24), style=0, value='')
        # self.cycleOffMixToPlantValue.Bind(wx.EVT_TEXT_ENTER,
        #       self.OnCycleOffMixToPlantValueTextEnter,
        #       id=wxID_HYDROPIONICSCYCLEOFFMIXTOPLANTVALUE)
        #
        # self.drainSystemCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSDRAINSYSTEMCHECKBOX,
        #       label=u'Drain System', name=u'drainSystemCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(192, 360),
        #       size=wx.Size(84, 15), style=0)
        # self.drainSystemCheckBox.SetValue(False)
        # self.drainSystemCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnDrainSystemCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSDRAINSYSTEMCHECKBOX)
        #
        # self.exaustFanCycleOnText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSEXAUSTFANCYCLEONTEXT,
        #       label=u'Cycle On', name=u'exaustFanCycleOnText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 40),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.genStaticText3 = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSGENSTATICTEXT3,
        #       label=u'Cycle Off', name='genStaticText3',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 40),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.exaustFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSEXAUSTFANCYCLEONVALUE,
        #       name=u'exaustFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 56), size=wx.Size(48, 23), style=0, value='')
        #
        # self.exaustFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSEXAUSTFANCYCLEOFFVALUE,
        #       name=u'exaustFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 56), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOnVentFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONVENTFANTEXT,
        #       label=u'Cycle On', name=u'cycleOnVentFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 128),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOffVentFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFVENTFANTEXT,
        #       label=u'Cycle Off', name=u'cycleOffVentFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 128),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.ventFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSVENTFANCYCLEONVALUE,
        #       name=u'ventFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 144), size=wx.Size(48, 23), style=0, value='')
        #
        # self.ventFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSVENTFANCYCLEOFFVALUE,
        #       name=u'ventFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 144), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOnIntakeFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONINTAKEFANTEXT,
        #       label=u'Cycle On', name=u'cycleOnIntakeFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 224),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOffIntakeFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFINTAKEFANTEXT,
        #       label=u'Cycle Off', name=u'cycleOffIntakeFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 224),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.intakeFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSINTAKEFANCYCLEONVALUE,
        #       name=u'intakeFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 240), size=wx.Size(48, 23), style=0, value='')
        #
        # self.intakeFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSINTAKEFANCYCLEOFFVALUE,
        #       name=u'intakeFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 240), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOnAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONAIRFILTERFANTEXT,
        #       label=u'Cycle On', name=u'cycleOnAirFIlterFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 320),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.airFilterFanCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSAIRFILTERFANCYCLEONVALUE,
        #       name=u'airFilterFanCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 336), size=wx.Size(48, 23), style=0, value='')
        #
        # self.airFilterFanCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSAIRFILTERFANCYCLEOFFVALUE,
        #       name=u'airFilterFanCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(688, 336), size=wx.Size(48, 23), style=0, value='')
        #
        # self.cycleOffAirFIlterFanText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFAIRFILTERFANTEXT,
        #       label=u'Cycle Off', name=u'cycleOffAirFIlterFanText',
        #       parent=self.scrolledPanel1, pos=wx.Point(688, 320),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOnLedText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEONLEDTEXT,
        #       label=u'Cycle On', name=u'cycleOnLedText',
        #       parent=self.scrolledPanel1, pos=wx.Point(560, 592),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.cycleOffLedText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSCYCLEOFFLEDTEXT,
        #       label=u'Cycle Off', name=u'cycleOffLedText',
        #       parent=self.scrolledPanel1, pos=wx.Point(696, 592),
        #       size=wx.Size(104, 15), style=0)
        #
        # self.ledCycleOnValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSLEDCYCLEONVALUE,
        #       name=u'ledCycleOnValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(560, 608), size=wx.Size(48, 23), style=0, value='')
        #
        # self.ledCycleOffValue = wx.lib.masked.textctrl.TextCtrl(id=wxID_HYDROPIONICSLEDCYCLEOFFVALUE,
        #       name=u'ledCycleOffValue', parent=self.scrolledPanel1,
        #       pos=wx.Point(696, 608), size=wx.Size(48, 23), style=0, value='')
        #
        # self.temperatureTextStart = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSTEMPERATURETEXTSTART,
        #       label=u'F', name=u'temperatureTextStart',
        #       parent=self.scrolledPanel1, pos=wx.Point(184, 424),
        #       size=wx.Size(16, 36), style=0)
        # self.temperatureTextStart.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
        #       wx.NORMAL, False, u'Segoe Print'))
        #
        # self.temperatureRangeEndText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSTEMPERATURERANGEENDTEXT,
        #       label=u'F', name=u'temperatureRangeEndText',
        #       parent=self.scrolledPanel1, pos=wx.Point(280, 424),
        #       size=wx.Size(16, 36), style=0)
        # self.temperatureRangeEndText.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
        #       wx.NORMAL, False, u'Segoe Print'))
        #
        # self.humidityPercentSignStart = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSHUMIDITYPERCENTSIGNSTART,
        #       label=u'%', name=u'humidityPercentSignStart',
        #       parent=self.scrolledPanel1, pos=wx.Point(184, 512),
        #       size=wx.Size(15, 36), style=0)
        # self.humidityPercentSignStart.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
        #       wx.NORMAL, False, u'Segoe Print'))
        #
        # self.humidityEndText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSHUMIDITYENDTEXT,
        #       label=u'%', name=u'humidityEndText', parent=self.scrolledPanel1,
        #       pos=wx.Point(280, 512), size=wx.Size(15, 36), style=0)
        # self.humidityEndText.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL,
        #       wx.NORMAL, False, u'Segoe Print'))
        #
        # self.cycleOnExaustFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONEXAUSTFAN, name=u'cycleOnExaustFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 56),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnExaustFan.SetStringSelection(u's')
        # self.cycleOnExaustFan.SetSelection(0)
        #
        # self.CycleOnWaterPump = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONWATERPUMP, name=u'CycleOnWaterPump',
        #       parent=self.scrolledPanel1, pos=wx.Point(224, 88),
        #       size=wx.Size(48, 23), style=0)
        # self.CycleOnWaterPump.SetSelection(0)
        # self.CycleOnWaterPump.Bind(wx.EVT_CHOICE, self.OnCycleOnWaterPumpChoice,
        #       id=wxID_HYDROPIONICSCYCLEONWATERPUMP)
        #
        # self.CycleOffWaterPump = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFWATERPUMP, name=u'CycleOffWaterPump',
        #       parent=self.scrolledPanel1, pos=wx.Point(336, 88),
        #       size=wx.Size(48, 23), style=0)
        # self.CycleOffWaterPump.SetSelection(0)
        # self.CycleOffWaterPump.Bind(wx.EVT_CHOICE,
        #       self.OnCycleOffWaterPumpChoice,
        #       id=wxID_HYDROPIONICSCYCLEOFFWATERPUMP)
        #
        # self.cycleOffPlantMixCycle = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFPLANTMIXCYCLE,
        #       name=u'cycleOffPlantMixCycle', parent=self.scrolledPanel1,
        #       pos=wx.Point(336, 200), size=wx.Size(48, 23), style=0)
        # self.cycleOffPlantMixCycle.SetSelection(0)
        # self.cycleOffPlantMixCycle.Bind(wx.EVT_CHOICE,
        #       self.OnCycleOffPlantMixCycleChoice,
        #       id=wxID_HYDROPIONICSCYCLEOFFPLANTMIXCYCLE)
        #
        # self.cycleOnPlantMixCycle = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONPLANTMIXCYCLE,
        #       name=u'cycleOnPlantMixCycle', parent=self.scrolledPanel1,
        #       pos=wx.Point(224, 200), size=wx.Size(48, 23), style=0)
        # self.cycleOnPlantMixCycle.SetSelection(0)
        # self.cycleOnPlantMixCycle.Bind(wx.EVT_CHOICE,
        #       self.OnCycleOnPlantMixCycleChoice,
        #       id=wxID_HYDROPIONICSCYCLEONPLANTMIXCYCLE)
        #
        # self.cycleOffExaustFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFEXAUSTFAN, name=u'cycleOffExaustFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(736, 56),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffExaustFan.SetSelection(0)
        #
        # self.cycleOnVentFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONVENTFAN, name=u'cycleOnVentFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 144),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnVentFan.SetSelection(0)
        #
        # self.cycleOffVentFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFVENTFAN, name=u'cycleOffVentFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(736, 144),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffVentFan.SetSelection(0)
        #
        # self.cycleOnIntakeFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONINTAKEFAN, name=u'cycleOnIntakeFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 240),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnIntakeFan.SetSelection(0)
        #
        # self.cycleOffIntakeFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFINTAKEFAN, name=u'cycleOffIntakeFan',
        #       parent=self.scrolledPanel1, pos=wx.Point(736, 240),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffIntakeFan.SetSelection(0)
        #
        # self.cycleOnAirFIlterFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONAIRFILTERFAN,
        #       name=u'cycleOnAirFIlterFan', parent=self.scrolledPanel1,
        #       pos=wx.Point(608, 336), size=wx.Size(56, 23), style=0)
        # self.cycleOnAirFIlterFan.SetSelection(0)
        #
        # self.cycleOffAirFilterFan = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFAIRFILTERFAN,
        #       name=u'cycleOffAirFilterFan', parent=self.scrolledPanel1,
        #       pos=wx.Point(736, 336), size=wx.Size(56, 23), style=0)
        # self.cycleOffAirFilterFan.SetSelection(0)
        #
        # self.cycleOnLed = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEONLED, name=u'cycleOnLed',
        #       parent=self.scrolledPanel1, pos=wx.Point(608, 608),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOnLed.SetStringSelection(u'')
        # self.cycleOnLed.SetSelection(0)
        #
        # self.cycleOffLed = wx.Choice(choices=['s', 'm', 'h'],
        #       id=wxID_HYDROPIONICSCYCLEOFFLED, name=u'cycleOffLed',
        #       parent=self.scrolledPanel1, pos=wx.Point(744, 608),
        #       size=wx.Size(56, 23), style=0)
        # self.cycleOffLed.SetSelection(0)
        #
        # self.delayStartCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSDELAYSTARTCHECKBOX,
        #       label=u'Delay Start', name=u'delayStartCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(408, 648),
        #       size=wx.Size(78, 23), style=0)
        # self.delayStartCheckBox.SetValue(False)
        # self.delayStartCheckBox.Bind(wx.EVT_CHECKBOX, self.OnCheckBox3Checkbox,
        #       id=wxID_HYDROPIONICSDELAYSTARTCHECKBOX)
        #
        # self.checkPHCheckBox = wx.CheckBox(id=wxID_HYDROPIONICSCHECKPHCHECKBOX,
        #       label=u'Check PH', name=u'checkPHCheckBox',
        #       parent=self.scrolledPanel1, pos=wx.Point(176, 256),
        #       size=wx.Size(88, 16), style=0)
        # self.checkPHCheckBox.SetValue(True)
        # self.checkPHCheckBox.Bind(wx.EVT_CHECKBOX,
        #       self.OnCheckPHCheckBoxCheckbox,
        #       id=wxID_HYDROPIONICSCHECKPHCHECKBOX)
        #
        # self.delayStartTime = wx.lib.masked.timectrl.TimeCtrl(display_seconds=True,
        #       fmt24hr=False, id=wxID_HYDROPIONICSDELAYSTARTTIME,
        #       name=u'delayStartTime', oob_color=wx.NamedColour('Yellow'),
        #       parent=self.scrolledPanel1, pos=wx.Point(488, 648),
        #       size=wx.Size(85, 23), style=0, useFixedWidthFont=True,
        #       value='12:00:00 AM')
        #
        # self.systemStatusText = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSSYSTEMSTATUSTEXT,
        #       label=u'System Status:', name=u'systemStatusText',
        #       parent=self.scrolledPanel1, pos=wx.Point(784, 688),
        #       size=wx.Size(78, 13), style=0)
        # self.systemStatusText.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
        #       False, u'Small Fonts'))
        #
        # self.systemStatus = wx.lib.stattext.GenStaticText(ID=wxID_HYDROPIONICSSYSTEMSTATUS,
        #       label=u'', name=u'systemStatus', parent=self.scrolledPanel1,
        #       pos=wx.Point(872, 688), size=wx.Size(12, 13), style=0)
        # self.systemStatus.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
        #       False, u'Small Fonts'))

    def __init__(self, parent):
        self.initFrameMVC()
        self.initMenuBarMVC()
        self.initMonitorMVC()

        self._init_ctrls(parent)
    def initFrameMVC(self):
        self.gui = HydroPiOnicsView(self)
        self.guiModel =  HydroPiOnicsM()
        self.guiController = HydroPiOnicsController(self.guiModel, self.gui, self)
    def initMenuBarMVC(self):
        self.menuView = MenuBarView()
        self.SetMenuBar(self.menuView)
        self.menuModel = MenuBar()
        self.menuController = MenuBarController(self.menuModel, self.menuView, self)
    def initMonitorMVC(self):
        self.monitorView = MonitorView(self)
        self.monitorModel = Monitor()
        self.monitorController = MonitorController(self.monitorModel, self.monitorView, self)
        pass
    def initMotorMVC(self):
        pass
    def initRelayMVC(self):
        pass
    def initWorkspaceMVC(self):
        pass
    def getGUIController(self):
        return self.guiController
    # def OnCheckBox12Checkbox(self, event):
    #     event.Skip()
    #
    # def OnManualToggleButtonLeftDclick(self, event):
    #     event.Skip()
    #
    # def OnCheckBox3Checkbox(self, event):
    #     event.Skip()
    #
    # def OnExhaustFanCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnWaterAirCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnMixToPlantCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnPlanToMixCheckboxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnMixToDrainCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnPHLevelStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnPhLevelEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnPHRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnPHRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnWaterAirPowerSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnCycleOnWaterAirPumpValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOffWaterAirPumpValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOnMixToPlantValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOffMixToPlantValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnDrainSystemCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnCycleOnWaterPumpChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOffWaterPumpChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOffPlantMixCycleChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOnPlantMixCycleChoice(self, event):
    #     event.Skip()
    #
    # def OnCheckPHCheckBoxCheckbox(self, event):
    #     event.Skip()
    # def initPage(self, parent):
    #     pass
    # def initMotor(self, parent):
    #     pass
    # def initRelay(self, parent):
    #     pass


if __name__ == '__main__':
    app = wx.App()
    frame = create(None)
    frame.Show()

    app.MainLoop()
