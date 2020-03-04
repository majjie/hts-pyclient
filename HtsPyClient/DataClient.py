from HtsPyClient.Common import get, post, delete, createValuePayload, RoutineStatus, ColumnDataType
from HtsPyClient.Data import ColumnDefinition, KeyValuePair, TableDefinition, RowInsertion, tableDefinitionFromJson
from typing import List
import urllib

class DataClient:
    def __init__(self, port: int):
        self.port = port
    
    def createTable(self, definition: TableDefinition):
        post("RunData/CreateTable", definition.jsonFragment())
    
    def getTableSchema(self, tableName: str) -> TableDefinition:
        param = urllib.request.quote(key)
        path = "RunData/TableSchema?tableName=" + param
        json = get(path)
        return tableDefinitionFromJson(json)

    def setKeyValue(self, key: str, value: object):
        pair = KeyValuePair(key, value)
        post("RunData/KeyValue", pair.jsonFragment())
    
    def getKeyValue(self, key: str) -> object:
        param = urllib.request.quote(key)
        path = "RunData/KeyValue?key=" + param
        json = get(path)
        return json["value"]
    
    def clearKeyValue(self, key: str):
        param = urllib.request.quote(key)
        path = "RunData/KeyValue?key=" + param
        delete(path)
    
    def insertRow(self, insertion: RowInsertion):
        post("RunData/AddRow", insertion.jsonFragment())