
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
                
        """ if there is a resource type matching one of the WoT Model classes or supporting classes, make 
            an instance of the support class which will add class-specific API methods and properties to the node
        """
        for linkAttr in im.rtToClass:
            if [] != self._links.get({v._rel: v._self, v._rt: linkAttr}) :
                im.rtToClass[linkAttr](self)


def selfTest():
    
    jsonString = """{ 
                    "bn": 
                        "/", 
                    "l": [ 
                        {"href": "", 
                        "rel": ["self", "item"], 
                        "rt": ["property", "greeting"]} 
                        ],
                    "e": [ 
                        {"n":"", 
                        "sv":"hello world"} 
                        ]
                    }"""
    nodeMap = json.loads(jsonString)
    testNode = TOMnode(nodeMap)
    """ the interface fo rthe property resource type has get and set methods """
    print testNode.get()
    testNode.set("hola mundo")
    print testNode.get()
    
if __name__ == "__main__" :
    selfTest()
