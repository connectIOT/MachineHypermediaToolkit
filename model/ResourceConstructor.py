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

""" these terms should come from the base schema and domain schema """
_index = "index"
_capability = "capability"
_thing = "thing"
_action = "action"
_event = "event"
_property = "property"

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

_baseResource = {
                 v._bn: v._null,
                 v._l:[{v._href: v._null, v._rel:v._self}],
                 v._e:[]
                 }


class ResourceModelConstructor:
    def __init__(self, model=None):
        self._model = model
        self._resourceModel = ResourceModel()
        self._processModelNode(model[v._resource], "/")
        
    
    def _processModelNode(self, node, basePath):
        self._node = node
        currentBasePath = basePath
        for self._resource in self._node:
            self._name = self._resource[v._name]
            self._type = self._resource[v._type]
            if _domainType[self._resource[v._type]] in _WoTClass:
                self._class = _WoTClass[_domainType[self._resource[v._type]]]
                self._resourceModel.addNodes( self._class(currentBasePath, self._resource).getNode() )
            for self._property in self._resource:
                if self._property in _collections:
                    self._processModelNode(self._resource[self._property], currentBasePath+self._name+"/")

    def serialize(self):
        return self._resourceModel.serialize()
        
class ResourceType:
    def __init__(self, basePath, resource):
        self._basePath = basePath
        self._name = resource[v._name]
        self._type = resource[v._type] 
        self._nodeMap = _baseResource 
        self._nodeMap[v._bn] = self._basePath 
        self._node = ResourceNode(self._nodeMap)
        
    def getNode(self):
        return self._node
    
class Index(ResourceType):
    pass

class Capability(ResourceType):
    pass

class Thing(ResourceType):
    pass

class Event(ResourceType):
    pass

class Action(ResourceType):
    pass

class Property(ResourceType):
    pass

class Subscription(ResourceType):
    pass

class Actuation(ResourceType):
    pass

class Notification(ResourceType):
    pass

_WoTClass = {
           _index: Index,
           _capability: Capability,
           _thing: Thing,
           _action: Action,
           _event: Event,
           _property: Property
           }
           
def selfTest():
    from DomainModel import mylight
    print ResourceModelConstructor(mylight).serialize()
    
if __name__ == "__main__" :
    selfTest()
