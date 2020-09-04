from HtsPyClient.Common import get, post, delete, createValuePayload, RoutineStatus, ColumnDataType
from HtsPyClient.Data import FieldValue
from typing import List
import urllib

class FormsClient:
    def __init__(self, port: int):
        self.port = port
    
    def getFieldValue(self, key: str) -> FieldValue:
        param = urllib.request.quote(key)
        path = "FormData/FieldValue?key=" + param
        json = get(path)
        return FieldValue(
            json["key"],
            json["value"],
            json["fieldStatus"],
            json["exists"]
        )
        