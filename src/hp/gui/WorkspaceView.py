import wx
import sys
import os
import wx.lib.stattext
import wx.lib.masked.timectrl

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

        self.initWorkspaceStaticText()
        self.initWorkspaceCheckboxes()
        self.initWorkspaceClock()
        
    
    def initWorkspaceCheckboxes(self):
        self.delayStartCheckBox = wx.CheckBox(id=wx.ID_ANY,
              label=u'Delay Start', name=u'delayStartCheckBox',
              parent=self, pos=wx.Point(800, 530),
              size=wx.Size(100, 20), style=0)
        self.delayStartCheckBox.SetValue(False)




    def initWorkspaceStaticText(self):
        self.systemStatusText = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,label=u'System Status:', name=u'systemStatusText',
              parent=self, pos=wx.Point(803, 587),
              size=wx.Size(78, 13), style=0)
        self.systemStatusText.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Small Fonts'))

        self.systemStatus = wx.lib.stattext.GenStaticText(ID=wx.ID_ANY,
              label=u'', name=u'systemStatus', parent=self,
              pos=wx.Point(820, 600), size=wx.Size(12, 13), style=0)
        self.systemStatus.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Small Fonts'))
    def initWorkspaceClock(self):

        self.delayStartTime = wx.lib.masked.timectrl.TimeCtrl(display_seconds=True,
              fmt24hr=False, id=wx.ID_ANY,
              name=u'delayStartTime', oob_color=wx.NamedColour('Yellow'),
              parent=self, pos=wx.Point(800, 580),
              size=wx.Size(50, 15), style=0, useFixedWidthFont=True,
              value='12:00:00 AM')


















