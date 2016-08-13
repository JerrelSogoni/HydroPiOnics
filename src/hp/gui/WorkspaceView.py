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

        self.ledPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "myLedLights.jpg",
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

