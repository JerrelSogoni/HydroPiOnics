import wx

class MenuBarView(wx.MenuBar):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.menuFile = self.initFileTab()
        self.menuHelp = self.initHelpTab()
        self.Append(self.menuFile, '&File')
        self.Append(self.menuHelp, '&Help')
    def initFileTab(self):
        self.menuFile = wx.Menu()
        self.openItem = self.menuFile.Append(wx.ID_OPEN, 'Open')
        self.saveItem = self.menuFile.Append(wx.ID_SAVE, 'Save')
        self.saveAsItem = self.menuFile.Append(wx.ID_SAVEAS, 'Save as')
        self.exitItem = self.menuFile.Append(wx.ID_CLOSE, 'Quit')
        return self.menuFile
    def initHelpTab(self):
        self.menuHelp = wx.Menu()
        self.aboutMeItem = self.menuHelp.Append(wx.ID_HELP, 'About Me' )
        return self.menuHelp
    def setMenu(self, menu):
        self.menu = menu
    def getMenu(self):
        return self.menu
    def setFileTab(self, fileTab):
        self.menuFile = fileTab
    def getFileTab(self):
        return self.menuFile
    def setMenuFile(self, menuFile):
        self.menuFile = menuFile
    def getExitItem(self):
        return self.exitItem


