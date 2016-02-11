
""" ResourceModel class is a list of resource nodes that can be used to 
    construct a resource set at a server location or to inspect resources
    at a server location. The model can be populated by loading a 
    constructor in the collection+senml+json content format, and an 
    existing model can likewise be serialized to the same content format.
    
    TODO. For this and content handlers in the resource layer, we could
    separate the model handling from the serialization and for example 
    an alternate collection+senml+xml format could be easily supported.
"""
from MachineHypermediaToolkit.client.http.HypermediaHttpRequest import HypermediaHttpRequest
from MachineHypermediaToolkit.resource.SenmlCollectionHandler import SenmlCollection
from MachineHypermediaToolkit.resource.Links import Links
from MachineHypermediaToolkit.resource.Items import SenmlItems
import json
import MachineHypermediaToolkit.terms as v

class ResourceModel:
    def __init__(self, serverAddress=None, model=None):
        self._nodeArray = []
        if model:
            self.load(model)   
        if serverAddress:
            self._server = Server(serverAddress)
        else:
            self._server = Server()
        
    def serialize(self):
        self._result = []
        for node in self._nodeArray :
            self._result.append(node.getModel())
        return json.dumps(self._result, sort_keys=True, indent=2, separators=(',', ': '))
    
    def load(self, jsonString):
        self._loadObject = json.loads(jsonString)
        if isinstance(self._loadObject, list):
            for nodeMap in self._loadObject:
                self.addNodes(ResourceNode(nodeMap))
        elif isinstance(self._loadObject, dict):
            self.addNodes(ResourceNode(self._loadObject))
        return self
            
    def createOnServer(self, serverAddress=None):
        if serverAddress:
            self._server._server = serverAddress
        for node in self._nodeArray:
            self._server.createResourceNode(node)
        return self
    
    def loadFromServer(self, serverAddress=None):
        if serverAddress:
            self._server._server = serverAddress
        self._server.getResources("/", self._nodeArray)
        return self
    
    def addNodes(self, nodes):
        if isinstance(nodes,list) :
            self._nodeArray.extend(nodes)
        else:
            self._nodeArray.append(nodes)
    
    def removeNodes(self, path, selectMap):
        """ remove the selected nodes and all subresource nodes """
        pass
    
class ResourceNode:
    def __init__(self, nodeMap):
        """ Make a Resource Node from either a collection or a plain senml """
        if v._l in nodeMap:
            self._links = Links(nodeMap[v._l])
        else:
            self._links = Links()          
        self._items = SenmlItems(nodeMap[v._e])
        self._baseName = nodeMap[v._bn]
        self._resource = SenmlCollection(self._links.get(), self._items._items, self._baseName)
        
    def addLinks(self, links):
        self._resource.addLinks(links)
        
    def addItems(self, items):
        self._resource.addItems(items)

    def serialize(self):
        return self._resource.serialize()
    
    def load(self, jsonString):
        self._resource.load(jsonString)
        return self
        
    def getModel(self):
        return self._resource._senml

class Server:
    def __init__(self, server=None):
        if server:
            self._server = server
        
    def createResourceNode(self, node):
        # this is a bit inelegant because it's not using a hypermedia form
        self._url = self._server + node.getModel()[v._bn]
        #print "payload: ", node._resource.serialize()
        self._request = HypermediaHttpRequest(self._url, \
                {v.method: v.post, v.contentFormat: v.senmlCollectionType, v.payload: node._resource.serialize() })
        self._request.send()
        self._request.getResponse()
        # print "Status: ", self._request._requestMap[v.response][v.status],
        # if v.location in self._request._requestMap[v.options] :
            # print "Location: ", self._request._requestMap[v.options][v.location],
        
    def getResources(self, uriPath, resourceArray):
        self._getResourceRecursive(uriPath, resourceArray)
    
    def _getResourceRecursive(self, uriPath, resourceArray):
        #print "subresource link: ", uriPath
        resourceNode = self._getResource(uriPath)
        resourceArray.append(resourceNode)
        for link in resourceNode._links.get({v._rel:v._sub}) :
            self._getResourceRecursive(resourceNode._baseName + link[v._href], resourceArray)

    def _getResource(self, uriPath="/"):
        self._url = self._server + uriPath
        self._request = HypermediaHttpRequest(self._url, \
                {v.method:v.get, v.contentFormat:v.senmlCollectionType })
        self._request.send()
        self._request.getResponse()
        #print "payload: ", self._request._requestMap[v.response][v.payload]
        return ResourceNode( json.loads(self._request._requestMap[v.response][v.payload] ) )


def selfTest():
    jsonString = """
                    [ {
                    "bn": "/", 
                    "l": [
                        {"href": "", 
                        "rel": ["self"]}, 
                        {"href": "test", 
                        "rel": "sub"}
                        ],
                    "e": [
                        {"n":"test",
                        "sv":"testValue"}
                        ]
                    } ]
                """
                    
    serverAddress = "http://localhost:8000"
    
    print "creating on server: ", ResourceModel().load(jsonString).createOnServer(serverAddress).serialize()
    print "model from server: ", ResourceModel().loadFromServer(serverAddress).serialize()
    
if __name__ == "__main__" :
    selfTest()
    
    