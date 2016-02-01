"""
ResourceConstructor takes a base schema and domain model, and constructs a 
Resource Model 

The base Schema classes are built by specialized classes in this module, and they 
are configured from the domain schema and domain model.

The domain schema describes all of the possible constructions and the domain model 
selects the construction of configured resources

The resulting resource model is used as a constructor to the class ResourceModel,
which can create resources on a server.

The generated resource types (rt) are used to select handlers for binding to the
resource instances on the server, and used in the client to bind Interaction Model 
classes to resource nodes in the TOM

"""
from ResourceModel import ResourceModel, ResourceNode
import MachineHypermediaToolkit.terms as v
import DomainTerms as d
import json


class ResourceModelConstructor:
    def __init__(self, model=None):
        self._model = model
        self._resourceModel = ResourceModel()
        self._processModelNode(model[v._resource], d._index, "/")
        
    """ a node in the domain model is a "collection" of events, actions, 
    properties, capabilities, etc.represented as an array of maps that
    describe name, type, etc. where type conforms to the domain schema
    
    This is a recurcive function that performs a depth-first selection.
    Each resource built produces a collection representation which is 
    POSTed to the base resource specfied in its "bn" element
    """    
    
    def _processModelNode(self, node, baseType, basePath):
        self._node = node
        currentBasePath = basePath
        currentBaseType = baseType
        for _resource in self._node:
            _name = _resource[v._name]
            _type = _resource[v._type]
            if d._domainType[_resource[v._type]] in _WoTClass:
                #print currentBasePath, _resource[v._name], _resource[v._type], d._domainType[_resource[v._type]]
                self._class = _WoTClass[d._domainType[_resource[v._type]]]
                self._newNode = self._class(currentBasePath, currentBaseType, _resource).getNode()
                #print self._newNode.serialize()
                self._resourceModel.addNodes( self._newNode )
            for self._property in _resource:
                if self._property in d._collections:
                    self._processModelNode(_resource[self._property], _type, currentBasePath + _name + "/")
                elif self._property in d._content:
                    self._processContentNode(_resource[self._property], self._property, currentBasePath + _name + "/")
                    
    def _processContentNode(self, _content, _type, basePath):
        self._contentClass = _WoTClass[_type]
        self._contentNode = self._contentClass(_content, basePath).getNode()
        self._resourceModel.addNodes( self._contentNode )
        

    def serialize(self):
        return self._resourceModel.serialize()
            
class ResourceContent:
    """ base class for constructing resource model content nodes from domain model elements """
    def __init__(self, _content, basePath):
        self._nodeMap = {
                 v._bn: v._null,
                 v._l:[],
                 v._e:[]
                 }
        self._basePath = basePath
        self._content = _content
        self._nodeMap[v._bn] = self._basePath 
        self._node = ResourceNode(self._nodeMap)
        self._node.load(json.dumps(self._contentTemplate))
        self.configure()
                
    def configure(self):
        pass

class LinkContent(ResourceContent):
    """ class for adding link content to an index type node """
    _contentTemplate = {
        v._l:[],
        v._e: []
    }
    def configure(self):
        self._node.addLinks(self._content)

    def getNode(self):
        return self._node
            
class ResourceType:
    """ base class for constructing resource model nodes from domain model elements """
    def __init__(self, basePath, baseType, resource):
        self._nodeMap = {
                 v._bn: v._null,
                 v._l:[],
                 v._e:[]
                 }
        self._basePath = basePath
        self._baseType = baseType
        self._name = resource[v._name]
        self._type = resource[v._type] 
        self._resource = resource
        self._nodeMap[v._bn] = self._basePath 
        """ Make an empty SenML Collection """
        self._node = ResourceNode(self._nodeMap)
        self._node.load(json.dumps(self._resourceTemplate))
        """ patch the type attribute link of the resource template """
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
        """ configure the form variables , getItemByName returns the entire
        item including name and value """
        self._form = self._node._resource._items.getItemByName(v._null)
        self._form[v._n] = self._name
        self._form[v._fv][v._type] = [self._type, self._form[v._fv][v._type]]
        """ if the name is specified in the update map as it is here, 
        the resource name will be changed """
        for template in d._templates:
            if self._baseType in template[v._rt] and self._type in template[v._rt]:
                self._form[v._fv][v._template] = template[v._template]
                    
        self._node._resource._items.updateItemByName(v._null, self._form)
        """ TBD look up the template from schema """
    
class Property(ResourceType):
    
    _resourceTemplate =  {
        v._l:[ {
            v._href: v._null, 
            v._rel: v._sub,
            v._rt: d._property
        } ],
        v._e: [{v._n: v._null, v._sv: v._null}]
    }

    def configure(self):
        """ TBD look up json type and default value from schema """
        self._dtype = d._propertyType[self._type][d._dtype]
        self._dval = d._propertyType[self._type][d._dval]
        self._node._resource._items.updateItemByName \
            (v._null, {v._n: self._name, self._dtype: self._dval})
    
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
           d._property: Property,
           v._links: LinkContent
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
