import wx
import os
import sys
class HydroPiOnicsView:
    def __init__(self, appGUI):
        self.appGUI = appGUI
        self.initFrame(self.appGUI)
    def initFrame(self, appGUI):
        # init frame
        wx.Frame.__init__(self.appGUI, id= wx.ID_ANY, name=u'HydroPiOnics',
                          parent=None, pos=wx.Point(636, 99), size=wx.Size(800, 800),
                          style=wx.DEFAULT_FRAME_STYLE, title=u'HydroPiOnics')

        self.appGUI.SetClientSize(wx.Size(800, 800))
        self.appGUI.SetBackgroundColour(wx.Colour(196, 233, 253))
        self.appGUI.SetMaxSize(wx.Size(800, 800))
        self.appGUI.SetInitialSize(wx.Size(800, 800))
        self.appGUI.Show(True)
        self.appGUI.Centre()
        self.appGUI.SetIcon(wx.Icon(self.imageAttachment("applicationicon.ico"),
                             wx.BITMAP_TYPE_ICO))

    def imageAttachment(self, object):
        # Identify Operating System in order to direct image loading path
        # Mac OS or Linux
        directory = os.getcwd()[:len(os.getcwd()) - 6]

        if (sys.platform.startswith('darwin') or sys.platform.startswith('linux')):
            imglocation = directory + "Image//" + object
        # Windows
        elif (sys.platform.startswith('win32')):
            imglocation = directory + "Image\\" + object
        return imglocation


