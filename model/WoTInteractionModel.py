
class InteractionModel():
    
    def __init__(self, node):
        self._node = node
        self.init()
    
    def init(self):
        self._node.ser = self.ser
        
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
