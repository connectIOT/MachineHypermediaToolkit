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
import json

""" these terms should come from the base schema and domain schema """
_index = "index"
_capability = "capability"
_thing = "thing"
_action = "action"
_event = "event"
_property = "property"
_actuation = "actuation"
_subscription = "subscription"
_notification = "notification"

""" these terms are from the domain schema """
_light = "light"
_onoff = "onoff"
_brightness = "brightness"
_colorhs = "colorhs"
_change = "change"
_move = "move" 
_step = "step"
_stop = "stop"

""" this table is a stub for using the appropriate application schema 
    to determine the WoT resource type of a particular domain type """
_domainType = {
           _index: _index,
           _light: _thing,
           _onoff: _capability,
           _brightness: _capability,
           _colorhs: _capability,
           _change: _action,
           _move: _action,
           _step: _action,
           _stop: _action
           }

""" this list replaces lookup of the domain model property "hasEvent, etc. """
_collections = [
                "events",
                "actions",
                "properties",
                "capabilities",
                ]

_rootNode = {v._name: v._null,
             v._type: _index}

class ResourceModelConstructor:
    def __init__(self, model=None):
        self._model = model
        self._resourceModel = ResourceModel()
        self._root = _rootNode
        self._processModelNode(model[v._resource], "/")
        
    def _processModelNode(self, node, basePath):
        self._node = node
        currentBasePath = basePath
        for self._resource in self._node:
            self._name = self._resource[v._name]
            self._type = self._resource[v._type]
            if _domainType[self._resource[v._type]] in _WoTClass:
                #print currentBasePath, self._resource[v._name], self._resource[v._type], _domainType[self._resource[v._type]]
                self._class = _WoTClass[_domainType[self._resource[v._type]]]
                self._newNode = self._class(currentBasePath, self._resource).getNode()
                #print self._newNode.serialize()
                self._resourceModel.addNodes( self._newNode )
            for self._property in self._resource:
                if self._property in _collections:
                    self._processModelNode(self._resource[self._property], currentBasePath+self._name+ "/")

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
            v._rt: _index
        } ],
        v._e: []
    }
    
class Capability(Index):
    
    _resourceTemplate = {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: _capability
        } ],
        v._e: []
    }
    
class Thing(Capability):
    
    _resourceTemplate = {
        v._l: [ {
            v._href: v._null, 
            v._rel: v._sub, 
            v._rt: _thing
        } ],
        v._e: []
    }
    
class Event(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: [v._form, v._item],
            v._rt: _event
        } ],
        v._e: [ {
            v._n: v._null,
            v._fv: {
                v._rel: _event,
                v._type: _event,
                v._method: v.post,
                v._href: _subscription,
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
            v._rt: _action
        } ],
        v._e: [ {
            v._n: v._null,
            v._fv: {
                v._rel: _action,
                v._type: _action,
                v._method: v.post,
                v._href: _actuation,
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
            v._rt: _property
        } ],
        v._e: []
    }
    
class Subscription(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: _subscription
        } ],
        v._e: []
    }

class Actuation(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: _actuation
        } ],
        v._e: []
    }

class Notification(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: _notification
        } ],
        v._e: []
    }

_WoTClass = {
           _index: Index,
           _capability: Capability,
           _thing: Thing,
           _action: Action,
           _event: Event,
           _property: Property
           }
           
def selfTest():
    from DomainModel import light
    print ResourceModelConstructor(light).serialize()
    
if __name__ == "__main__" :
    selfTest()
