
""" ResourceModel class is a list of resource nodes that can be used to 
    construct a resource set at a server location or to inspect resources
    at a server location. The model can be populated by loading a 
    constructor in the collection+senml+json content format, and an 
    existing model can likewise be serialized to the same content format.
    
    TODO. For this and content handlers in the resource layer, we could
    separate the model handling from the serialization and for example 
    an alternate collection+senml+xml format could be easily supported.
"""
from Links import Links
from Items import SenmlItems

class ResourceModel():
    def __init__(self):
        """ nodes will always be sorted in path length order """
        self._resourceNodeArray = []
        
    def serialize(self):
        pass
    
    def load(self):
        pass
    
    def createOnServer(self):
        pass
    
    def loadFromServer(self):
        pass
    
    def addNode(self, node):
        """ find the correct place in the node array to insert the node """
        pass
    
    def removeNode(self, path, selectMap):
        """ remove the selected node and all subresource nodes """
        pass
    
class ResourceNode():
    def __init__(self):
        self._items = SenmlItems()
        self._links = Links()
