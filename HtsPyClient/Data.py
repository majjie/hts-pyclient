from typing import List
from HtsPyClient.Common import ColumnDataType, RoutineStatus

class ColumnDefinition:
    def __init__(self, name: str, nullable: bool, dataType: ColumnDataType):
        self.name = name
        self.nullable = nullable
        self.dataType = dataType

    def jsonFragment(self):
        return {
            "name": self.name,
            "nullable": self.nullable,
            "dataType": self.dataType.name
        }

def columnDefinitionFromJson(json) -> ColumnDefinition:
    return ColumnDefinition(
        json["name"],
        json["nullable"],
        ColumnDataType[json["dataType"]]
    )


class TableDefinition:
    def __init__(self, name: str, columns: List[ColumnDefinition]):
        self.name = name
        self.columns = columns
    
    def jsonFragment(self):
        return {
            "name": self.name,
            "columns": [x.jsonFragment() for x in self.columns]
        }

def tableDefinitionFromJson(json) -> TableDefinition:
    if json is None:
        return None

    return TableDefinition(
        json["name"],
        [columnDefinitionFromJson(json) for c in json["columns"]]
    )

class KeyValuePair:
    def __init__(self, key: str, value: object):
        self.key = key
        self.value = value
    
    def jsonFragment(self):
        return {
            "key": self.key,
            "value": self.value
        }

class RowInsertion:
    def __init__(self, table: str, cells: List[KeyValuePair]):
        self.table = table
        self.cells = cells
    
    def jsonFragment(self):
        return {
            "table": self.table,
            "cells": [c.jsonFragment() for c in self.cells]
        }

class FieldValue:
    def __init__(self, key: str, value: object, status: RoutineStatus, exists: bool):
        self.key = key
        self.value = value
        self.status = status
        self.exists = exists