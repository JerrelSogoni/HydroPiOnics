import wx

class WorkspaceView(wx.ScrolledPanel):
    def __init__(self, appGUI):
        self.appGUI = appGUI
        super(WorkspaceView, self).__init__(id.wx_ANY, name =u'workspace', parent = self.appGUI,
                                            pos = wx.Point(0,50), size = wx.Size(950,800), style=wx.Tab_TRAVERSAL)
        self.SetInitalSize(wx.Size(950,800))
        self.SetBackgroundColour(wx.Colour(185, 242, 253))
