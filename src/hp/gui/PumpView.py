
import wx
import WorkspaceView
IMG_LOCATION = WorkspaceView.IMG_LOCATION

class PumpView:
    def __init__(self,workspace):
        self.workspace = workspace
        self.initPumpImages()
        self.initStaticPumpText()
        self.initPumpCheckbox()

    def initPumpImages(self):
        self.mixToPlantPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'mixToPlantPicture', parent=self.workspace,
                                                 pos=wx.Point(32, 136), size=wx.Size(50, 66), style=0)

        self.airHeaterPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "heater.jpg",
                                                                 wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                name=u'airHeaterPicture', parent=self.workspace,
                                                pos=wx.Point(400, 512), size=wx.Size(64, 56), style=0)

        self.plantToMixPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'plantToMixPicture', parent=self.workspace,
                                                 pos=wx.Point(32, 232), size=wx.Size(50, 66), style=0)

        self.mixToDrainPicture = wx.StaticBitmap(bitmap=wx.Bitmap(IMG_LOCATION + "dcwaterPumps.jpg",
                                                                  wx.BITMAP_TYPE_JPEG), id=wx.ID_ANY,
                                                 name=u'mixToDrainPicture', parent=self.workspace,
                                                 pos=wx.Point(32, 336), size=wx.Size(50, 66), style=0)


    def initStaticPumpText(self):
        self.waterControlText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                              label=u'Water Control', name=u'waterControlText',
                                                              parent=self.workspace, pos=wx.Point(24, 8), size=wx.Size(100,
                                                                                                                       16),
                                                              style=0)
        self.waterControlText.SetFont(wx.Font(9, wx.SCRIPT, wx.NORMAL,
                                              wx.NORMAL, False, u'Lucida Handwriting'))
        self.waterControlText.SetToolTipString(u'')
        self.mixToPlantText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Mix to Plant', name=u'mixToPlantText',
                                                            parent=self.workspace, pos=wx.Point(16, 112),
                                                            size=wx.Size(82, 15), style=0)
        self.mixToPlantText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.mixToPlantText.SetToolTipString(u'')

        self.plantToMixText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Plant to Mix', name=u'plantToMixText',
                                                            parent=self.workspace, pos=wx.Point(16, 216),
                                                            size=wx.Size(82, 15), style=0)
        self.plantToMixText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.plantToMixText.SetToolTipString(u'')

        self.mixToDrainText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
                                                            label=u'Mix to Drain', name=u'mixToDrainText',
                                                            parent=self.workspace, pos=wx.Point(16, 320),
                                                            size=wx.Size(84, 15), style=0)
        self.mixToDrainText.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL,
                                            wx.NORMAL, False, u'Showcard Gothic'))
        self.mixToDrainText.SetToolTipString(u'')
    def initPumpCheckbox(self):
        self.mixToPlantCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                              label=u'On/Off', name=u'mixToPlantCheckBox',
                                              parent=self.workspace, pos=wx.Point(96, 160),
                                              size=wx.Size(78, 15), style=0)
        self.mixToPlantCheckBox.SetValue(False)

        self.planToMixCheckbox = wx.CheckBox(id=wx.ID_ANY,
                                             label=u'On/Off', name=u'planToMixCheckbox',
                                             parent=self.workspace, pos=wx.Point(96, 256),
                                             size=wx.Size(84, 15), style=0)
        self.planToMixCheckbox.SetValue(False)

        self.mixToDrainCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                              label=u'On/Off', name=u'mixToDrainCheckBox',
                                              parent=self.workspace, pos=wx.Point(96, 360),
                                              size=wx.Size(84, 15), style=0)
        self.mixToDrainCheckBox.SetValue(False)

        self.drainSystemCheckBox = wx.CheckBox(id=wx.ID_ANY,
                                               label=u'Drain System', name=u'drainSystemCheckBox',
                                               parent=self.workspace, pos=wx.Point(192, 360),
                                               size=wx.Size(84, 15), style=0)
        self.drainSystemCheckBox.SetValue(False)




