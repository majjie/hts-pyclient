from HtsPyClient.NumericalBounds import NumericalBounds
from HtsPyClient.Common import get, post, createValuePayload, RoutineStatus

class InstrumentationClient:
    def __init__(self, port: int):
        self.port = port

    def add(self, key: str, userTitle: str, valueTemplate: str, status: RoutineStatus, value: float, numberBounds: NumericalBounds) -> bool:
        dto = {
            "key": key,
            "userTitle": userTitle,
            "valueTemplate": valueTemplate,
            "status": status.name,
            "value": value,
            "numberBounds": {
                "lowerFail": numberBounds.lowerFail,
                "lowerWarn": numberBounds.lowerWarn,
                "upperWarn": numberBounds.upperWarn,
                "upperFail": numberBounds.upperFail
            }
        }
        post("Instrumentation/Add", dto)
    
    def clear(self) -> RoutineStatus:
        get("Instrumentation/Clear")

    def delete(self, key: str, value: float) -> RoutineStatus:
        post("Instrumentation/Delete", { "key": key })

    def update(self, status: RoutineStatus):
        post("Instrumentation/Update", { "key": key, "value": value })