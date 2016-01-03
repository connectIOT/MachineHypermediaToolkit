import terms as v

class InteractionModel:
    
    def __init__(self, node):
        self._node = node
        self.init()
        self._node.ser = self.ser

    def init(self):
        pass
    
    def ser(self):
        return self._node.serialize()


class Index(InteractionModel):
    pass

class Thing(InteractionModel):
    pass
    
class Capability(InteractionModel):
    pass

class Action(InteractionModel):
    pass

class Event(InteractionModel):
    pass

class Property(InteractionModel):
    def init(self):
        self._node.get = self.get
        self._node.set = self.set

    def get(self):
        return self._node._items.getValueByName("")
        
    def set(self, newValue):
        self._node._items.updateValueByName("", newValue)
        
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

