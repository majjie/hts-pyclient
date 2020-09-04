from HtsPyClient.EngineClient import EngineClient
from HtsPyClient.DebugClient import DebugClient
from HtsPyClient.FormsClient import FormsClient
from HtsPyClient.InstrumentationClient import InstrumentationClient
from HtsPyClient.DataClient import *
from HtsPyClient.UserInterfaceClient import *
from HtsPyClient.RoutineInfoClient import *

class ApiClient:
    def __init__(self, port: int):
        self.__debug = DebugClient(port)
        self.__engine = EngineClient(port)
        self.__instrumentation = InstrumentationClient(port)
        self.__data = DataClient(port)
        self.__ui = UserInterfaceClient(port)
        self.__routineInfo = RoutineInfoClient(port)
        self.__forms = FormsClient(port)

    @property
    def forms(self) -> FormsClient:
        return self.__forms

    @property
    def data(self) -> DataClient:
        return self.__data

    @property
    def debug(self) -> DebugClient:
        return self.__debug

    @property
    def engine(self) -> EngineClient:
        return self.__engine

    @property
    def instrumentation(self) -> InstrumentationClient:
        return self.__instrumentation

    @property
    def routineInfo(self) -> RoutineInfoClient:
        return self.__routineInfo

    @property
    def ui(self) -> UserInterfaceClient:
        return self.__ui