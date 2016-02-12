import MachineHypermediaToolkit.terms as v

""" An interaction model is a set of methods bound to a set of node types or resource types 
    in a Thing Object Model.
    
    configure() is called after the node is created and the interaction model is attached. This
    could also be a register operation to configure the node as needed besides adding methods
    
    This interaction model is based on the model being considered by the W3C Web of Things 
    (WoT) Interest Group. The relationship of things to their events, actions, and properties 
    is extended by adding capabilities. A capability is nothing more than a set of actions, 
    events, and properties. The actions, events, and properties of different elements within
    a complex thing can be represented by capabilities. A thing is itself a capability, allowing
    for the case of a simple thing that has events, actions, and capabilitits.
    
    Likewise the notion of an Index is added. Index allows elements to be grouped together. 
    Capabilities are derived classes of Index, and contain Events, Actions, and Properties.
    Indices can be created to point to other resources, for example to create an actuation
    group (GroupIndex) or simply to aid discovery and configuration.
"""

class InteractionModel:
    
    def __init__(self, node):
        self._node = node
        self.configure()
        self._node.ser = self.ser

    def configure(self):
        pass
    
    def ser(self):
        return self._node.serialize()


class Index(InteractionModel):
    pass

class Capability(Index):
    pass

class Thing(Capability):
    pass    

class Action(InteractionModel):
    pass

class Event(InteractionModel):
    pass

class Property(InteractionModel):
    def configure(self):
        self._node.get = self.get
        self._node.set = self.set
        self._server = self._node._server
        self._baseName = self._node._baseName

    def get(self):
        self._propertyValue = self._server.getItem(self._baseName)
        self._node._items.updateValueByName("", self._propertyValue)
        return self._node._items.getValueByName("")
        
    def set(self, newValue):
        self._propertyValue = newValue
        self._server.putItem(self._baseName, self._propertyValue)
        self._node._items.updateValueByName("", self._propertyValue)
        
class Actuation(InteractionModel):
    pass

class Subscription(InteractionModel):
    pass

class Notification(InteractionModel):
    pass

""" mapping of the resource types to classes in the interaction model """
rtToClass = {
            v._index: Index,
            v._thing: Thing,
            v._capability: Capability,
            v._action: Action,
            v._event: Event,
            v._property: Property,
            v._actuation: Actuation,
            v._subscription: Subscription,
            v._notification: Notification
            }

