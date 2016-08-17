
class WorkspaceController():
    def __init__(self, workspaceView, workspaceModel, appData):
        self.workspaceView = workspaceView
        self.workspaceModel = workspaceModel
        self.appData = appData


    def setSystemStatus(self, status):
        self.workspaceModel.systemStatus = status
    def updateSystemStatus(self):
        self.workspaceView.systemStatus.SetLabel(self.workspaceModel.systemStatus)
