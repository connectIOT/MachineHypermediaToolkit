
""" ResourceModel class is a list of resource nodes that can be used to 
    construct a resource set at a server location or to inspect resources
    at a server location. The model can be populated by loading a 
    constructor in the collection+senml+json content format, and an 
    existing model can likewise be serialized to the same content format.
    
    TODO. For this and content handlers in the resource layer, we could
    separate the model handling from the serialization and for example 
    an alternate collection+senml+xml format could be easily supported.
"""
from SenmlCollectionHandler import SenmlCollection
from Links import Links
from Items import SenmlItems
import json
import terms as v

class ResourceModel():
    def __init__(self):
        """ nodes will always be sorted in path length order """
        self._resourceNodeArray = []
        
    def serialize(self):
        self._result = []
        for node in self._resourceNodeArray :
            self._result.append(node.getModel())
        return json.dumps(self._result)
    
    def load(self, jsonString):
        self._loadObject = json.loads(jsonString)
        if isinstance(list, self._loadObject):
            for nodeMap in self._loadObject:
                self.addNode(ResourceNode(nodeMap))
    
    def createOnServer(self):
        pass
    
    def loadFromServer(self):
        pass
    
    def addNode(self, node):
        self._resourceNodeArray.append(node)
    
    def removeNode(self, path, selectMap):
        """ remove the selected node and all subresource nodes """
        pass
    
class ResourceNode():
    def __init__(self, nodeMap):
        
        self._links = Links(nodeMap[v._l])
        self._items = SenmlItems(nodeMap[v._e])
        self._baseName = nodeMap[v._bn]
        self._resource = SenmlCollection(self._links, self._items, self._baseName)

    def serialize(self):
        return self._resource.serialize()
    
    def load(self, jsonString):
        self._resource.load(jsonString)
        
    def getModel(self):
        return self._resource._senml
    
    
def selfTest():
    model = ResourceModel
    model.load("""[ {"bn": "/", "e": [], "l": [{"href": "", "rel": ["self"]}, {"href": "test", "rel": "sub"}]} ]""")
    print model.serialize()
    
if __name__ == "__main__" :
    selfTest()
    
    
    
    