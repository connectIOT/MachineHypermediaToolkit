
""" 
Thing Object Model provides an application layer extension of ResourceModel 

Application classes are mapped to resource instances based on matching resource type names
found in the "rt" link attribute

"""

from ResourceModel import ResourceModel, ResourceNode
import terms as v
import json
import WoTInteractionModel as im

class ThingObjectModel(ResourceModel):
    
    def __init__(self):
        ResourceModel.__init__(self)

    def discover(self):
        pass
    
    def lookup(self):
        pass
        
        
class TOMnode(ResourceNode):
        
    def __init__(self, nodeMap):
        ResourceNode.__init__(self, nodeMap)
        
        self._imClass = {
            v._index: im.Index,
            v._thing: im.Thing,
            v._capability: im.Capability,
            v._action: im.Action,
            v._event: im.Event,
            v._property: im.Property,
            v._actuation: im.Actuation,
            v._subscription: im.Subscription,
            v._notification: im.Notification
            }
        
        """ if there is a resource type matching one of the WoT Model classes or supporting classes, make 
            an instance of the support class which will add class-specific API methods and properties to the node
        """
        for linkAttr in self._imClass:
            if [] != self._links.get({v._rel: v._self, v._rt: linkAttr}) :
                self.im = self._imClass[linkAttr](self)


def selfTest():
    
    nodeMap = json.loads("""{ "bn": "/", "e": [{"n":"", "sv":"hello world"}], "l": [{"href": "", "rel": ["self", "item"], "rt": ["property", "greeting"]} ] }""")
    testNode = TOMnode(nodeMap)
    print testNode.get()
    testNode.set("goodbye")
    print testNode.get()
    
if __name__ == "__main__" :
    selfTest()
