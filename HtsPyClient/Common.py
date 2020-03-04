import requests
from enum import Enum

#API Endpoint
ApiRoot = "http://localhost:8081/api/"

def createValuePayload(value):
    return { "value": value }

def delete(relativePath: str):
    url = ApiRoot + relativePath
    requests.delete(url)

def get(relativePath: str):
    url = ApiRoot + relativePath
    response = requests.get(url)
    return response.json()

def post(relativePath: str, payload: dict):
    url = ApiRoot + relativePath
    requests.post(url, json=payload)

class ColumnDataType(Enum):
    Integer = 0,
    Real = 1,
    String = 2,
    DateTime = 3,
    Guid = 4,
    RoutineStatus = 5,
    Boolean = 6

class RoutineStatus(Enum):
    Unknown = 0,
    Pass = 1,
    Warning = 2,
    Fail = 3,
    Errored = 4,
    Running = 5,
    Paused = 6,
    Skipped = 7,
    NeverRun = 8,
    NotSet = 9,
    Cancelled = 10

class DebugLevel(Enum):
    Verbose = 0,
    Debug = 1,
    Information = 2,
    Warning = 3,
    Error = 4