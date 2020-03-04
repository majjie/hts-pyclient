from HtsPyClient.EngineClient import EngineClient
from HtsPyClient.DebugClient import DebugClient
from HtsPyClient.InstrumentationClient import InstrumentationClient
from HtsPyClient.DataClient import *

class ApiClient:
    def __init__(self, port: int):
        self.__debug = DebugClient(port)
        self.__engine = EngineClient(port)
        self.__instrumentation = InstrumentationClient(port)
        self.__data = DataClient(port)

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