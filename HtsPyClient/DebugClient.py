from HtsPyClient.Common import DebugLevel, post

class DebugClient:
    def __init__(self, port: int):
        self.port = port

    def sendError(self, message: str):
        self.send(message, DebugLevel.Error)

    def sendInfo(self, message: str):
        self.send(message, DebugLevel.Information)

    def sendWarning(self, message: str):
        self.send(message, DebugLevel.Warning)

    def sendVerbose(self, message: str):        
        self.send(message, DebugLevel.Verbose)
        
    def sendDebug(self, message: str):
        self.send(message, DebugLevel.Debug)
        
    def send(self, message: str, level: DebugLevel):
        post('Debug/Add', {
            "lvl": level.name,
            "msg": message
        })