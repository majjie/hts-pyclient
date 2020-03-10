from HtsPyClient.Common import get, post, createValuePayload, RoutineType
import urllib

class RoutineInfoClient:
    def __init__(self, port: int):
        self.port = port

    def getParameter(self, param: str) -> object:
        param = urllib.request.quote(param)
        path = "Routine/Param?paramName=" + param
        json = get(path)
        return json["value"]
    
    def getRoutineName(self):
        json = get("Routine/Name")
        return json["value"]

    def getRoutineType(self) -> RoutineType:
        json = get("Routine/Type")
        return RoutineType[json["value"]]
        
    def getRoutineName(self):
        json = get("Routine/Id")
        return json["value"]