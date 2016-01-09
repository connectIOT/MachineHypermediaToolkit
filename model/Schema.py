"""
schema for abstract resource models
"""

import terms as v
import json

BaseContext = { 
    v._context: "http://schema.org",
    v._schema: [
        { v._property: v._uses,
        v._description: """to point to a class that can be used by this class""",
        },
        { v._property: v._usedBy,
        v._description: """to point to a class that uses this class""",
        },
    ]
}


class Schema:
    def __init__(self, nodeArray=None):
        self._schema = []
        if nodeArray:
            for nodeMap in nodeArray :
                self.addNode( SchemaNode(nodeMap) ) 
        
    def addNode(self, node):
        self._schema.append(node)

    def serialize(self):
        objectArray = []
        for node in self._schema:
            objectArray.append(node._nodeMap)
        return json.dumps(objectArray)

class SchemaNode:
    def __init__(self, nodeMap):
        self._nodeMap = {}
        self._node = self.configure(nodeMap) if nodeMap else {}
        
    def configure(self, nodeMap):
        self._nodeMap = nodeMap
        self._class = nodeMap[v._class]
        self._subClassOf = nodeMap[v._subClassOf] 
        self._uses = nodeMap[v._uses]
        self._usedBy = nodeMap[v._usedBy]
        self._description = nodeMap[v._description]
        return self

    def serialize(self):
        return json.dumps(self._nodeMap)
    
def selfTest():
    from W3Cschema import W3Cschema
    print Schema(W3Cschema).serialize()
        
if __name__ == "__main__" :
    selfTest()
        