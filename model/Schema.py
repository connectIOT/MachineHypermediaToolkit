"""
schema for W3C WoT Interaction Model
"""
import terms as v
import json

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
        self._className = nodeMap[v._className]
        self._subClassOf = nodeMap[v._subClassOf] 
        self._range = nodeMap[v._range]
        self._domain = nodeMap[v._domain]
        self._description = nodeMap[v._description]
        return self

    def serialize(self):
        return json.dumps(self._nodeMap)
    
def selfTest():
    from W3Cschema import W3Cschema
    print Schema(W3Cschema).serialize()
        
if __name__ == "__main__" :
    selfTest()
        