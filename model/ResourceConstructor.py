"""
ResourceConstructor takes a base schema and model and constructs a Resource Model 

The base Schema classes are built by specialized classes in this module, and they 
are configured from the domain schema and domain model.

The domain schema describes all of the possible constructions and the domain model 
constrains the construction to the configured resources

The resulting resource model is used as a constructor to the class ResourceModel,
which can create resources on a server.

The generated resource types (rt) are used to select handlers for binding to the
resource instances on the server, and used in the client to bind Interaction Model 
classes to resource nodes in the TOM

"""
from ResourceModel import ResourceModel, ResourceNode
import terms as v
import DomainTerms as d
import json


class ResourceModelConstructor:
    def __init__(self, model=None):
        self._model = model
        self._resourceModel = ResourceModel()
        self._processModelNode(model[v._resource], "/")
        
    def _processModelNode(self, node, basePath):
        self._node = node
        currentBasePath = basePath
        for _resource in self._node:
            _name = _resource[v._name]
            _type = _resource[v._type]
            if d._domainType[_resource[v._type]] in _WoTClass:
                #print currentBasePath, _resource[v._name], _resource[v._type], d._domainType[_resource[v._type]]
                self._class = _WoTClass[d._domainType[_resource[v._type]]]
                self._newNode = self._class(currentBasePath, _resource).getNode()
                #print self._newNode.serialize()
                self._resourceModel.addNodes( self._newNode )
            for self._property in _resource:
                if self._property in d._collections:
                    self._processModelNode(_resource[self._property], currentBasePath + _name+ "/")

    def serialize(self):
        return self._resourceModel.serialize()
            
class ResourceType:
    
    def __init__(self, basePath, resource):
        self._nodeMap = {
                 v._bn: v._null,
                 v._l:[],
                 v._e:[]
                 }
        self._basePath = basePath
        self._name = resource[v._name]
        self._type = resource[v._type] 
        self._resource = resource
        self._nodeMap[v._bn] = self._basePath 
        """ Make an empty SenML Collection """
        self._node = ResourceNode(self._nodeMap)
        self._node.load(json.dumps(self._resourceTemplate))
        self.getNode()._resource._links.selectMerge( {}, {v._rt: self._type} )
        """ remove and replace href """
        self.getNode()._resource._links.selectMerge( {}, {v._href: None} )
        self.getNode()._resource._links.selectMerge( {}, {v._href: self._name} )
        """ Class-specific override to configure the node """
        self.configure()
        
    def configure(self):
        pass
    
    def getNode(self):
        return self._node
    
class Index(ResourceType):
    
    _resourceTemplate = {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: d._index
        } ],
        v._e: []
    }
    
class Capability(Index):
    
    _resourceTemplate = {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: d._capability
        } ],
        v._e: []
    }
    
class Thing(Capability):
    
    _resourceTemplate = {
        v._l: [ {
            v._href: v._null, 
            v._rel: v._sub, 
            v._rt: d._thing
        } ],
        v._e: []
    }
    
class Event(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: [v._form, v._item],
            v._rt: d._event
        } ],
        v._e: [ {
            v._n: v._null,
            v._fv: {
                v._rel: d._event,
                v._type: d._event,
                v._method: v.post,
                v._href: d._subscription,
                v._ct: v.senmlCollectionType,
                v._template: [
                ]
            }   
        }]
    }
    
class Action(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: [v._form, v._item],
            v._rt: d._action
        } ],
        v._e: [ {
            v._n: v._null,
            v._fv: {
                v._rel: d._action,
                v._type: d._action,
                v._method: v.post,
                v._href: d._actuation,
                v._ct: v.senmlCollectionType,
                v._template: [
                ]
            }   
        } ]
    }
    
    def configure(self):
        """ configure the form variables """
        self._form = self._node._resource._items.getItemByName(v._null)
        self._form[v._n] = self._name
        self._form[v._fv][v._type] = [self._type, self._form[v._fv][v._type]]
        self._node._resource._items.updateItemByName(v._null, self._form)
    
class Property(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: d._property
        } ],
        v._e: []
    }
    
class Subscription(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: d._subscription
        } ],
        v._e: []
    }

class Actuation(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: d._actuation
        } ],
        v._e: []
    }

class Notification(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: d._notification
        } ],
        v._e: []
    }

_WoTClass = {
           d._index: Index,
           d._capability: Capability,
           d._thing: Thing,
           d._action: Action,
           d._event: Event,
           d._property: Property
           }
           
def selfTest():
    from DomainModel import light
    resourceModelString = ResourceModelConstructor(light).serialize()
    #print resourceModelString
    
    serverAddress = "http://localhost:8000"
    
    print "creating on server: ", ResourceModel().load(resourceModelString).createOnServer(serverAddress).serialize()
    print "model from server: ", ResourceModel().loadFromServer(serverAddress).serialize()
    
if __name__ == "__main__" :
    selfTest()
