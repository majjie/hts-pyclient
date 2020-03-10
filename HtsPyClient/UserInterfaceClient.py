from HtsPyClient.Common import get, post, createValuePayload, RoutineStatus

class UserInterfaceClient:
    def __init__(self, port: int):
        self.port = port

    def setProgress(self, progress: float, message: str):
        post("UI/Progress", {
            "progress": progress,
            "message": message
        })
    
    def hideProgress(self):
        get("UI/HideProgress")