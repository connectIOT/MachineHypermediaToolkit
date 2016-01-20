"""
schema for abstract resource models
"""

import MachineHypermediaToolkit.terms as v
import json


class Schema:
    def __init__(self, schema=None):
        self._schema = {}
        self._nodeArray = []
        if schema:
            self._schema = schema
            self._elementArray = schema[v._resource]
            if [] != self._elementArray:
                for nodeMap in self._elementArray :
                    self.addNode( SchemaNode(nodeMap) ) 
        
    def addNode(self, node):
        self._nodeArray.append(node)

    def serialize(self):
        objectArray = []
        for node in self._nodeArray:
            objectArray.append(node._nodeMap)
        return json.dumps(objectArray, sort_keys=True, indent=4, separators=(',', ': '))

class SchemaNode:
    def __init__(self, nodeMap):
        self._nodeMap = {}
        self._node = self.configure(nodeMap) if nodeMap else {}
        
    def configure(self, nodeMap):
        self._nodeMap = nodeMap
        self._class = nodeMap[v._class]
        self._subClassOf = nodeMap[v._subClassOf] 
        self._mayHave = nodeMap[v._mayHave]
        self._usedBy = nodeMap[v._usedBy]
        self._description = nodeMap[v._description]
        return self

    def serialize(self):
        return json.dumps(self._nodeMap, sort_keys=True, indent=4, separators=(',', ': '))
    
def selfTest():
    from WoTschema import WoTschema
    print Schema(WoTschema).serialize()
        
if __name__ == "__main__" :
    selfTest()
        