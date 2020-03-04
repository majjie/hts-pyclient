from HtsPyClient.Common import get, post, createValuePayload, RoutineStatus

class EngineClient:
    def __init__(self, port: int):
        self.port = port

    def isCancelled(self) -> bool:
        json = get("Execution/IsCancelled")        
        return json["value"]
    
    def getRoutineStatus(self) -> RoutineStatus:
        json = get("Execution/Status")
        return RoutineStatus[json["value"]]

    def setRoutineStatus(self, status: RoutineStatus):
        post("Execution/Status", createValuePayload(status.name))
