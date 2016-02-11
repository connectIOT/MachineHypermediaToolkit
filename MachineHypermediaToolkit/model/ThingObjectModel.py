
""" 
Thing Object Model provides an application layer extension of ResourceModel 

The TOM is a set of graphs where the nodes are models of discovered resources.
Resource discovery uses a filter template to select resources at a server location based on
terms chosen from a hypermedia vocabulary.
The filter is a nested dictionary that specifies resource type values and included resource 
type values, for example, a resource type "light" includes, or "has" a "brightness" resource
for dimming control.

Discovery is driven forward by a chain of included resource types, for example:
light => brightness => currentbrightness in order to discover the current brightness property
of the brightness capability of the light thing.

As each resource is discovered, a TOM node is created and, if a label is provided in the 
filter, an entry is made in an index allowing reference to a TOM node or set of nodes by label.

Application classes that implement type-specific script APIs are bound to TOM nodes based 
on matching resource types found in the "rt" link attribute. The currentbrightness resource
has a resource type value of "property" which will bind the Property interface to that node. 
The Property interface has get and set methods that allow applications to interact with the
property value.

"""

import json
from urlparse import urlparse
from ResourceModel import ResourceModel, ResourceNode
import MachineHypermediaToolkit.terms as v
import InteractionModel as im

class ThingObjectModel(object):
    def __init__(self, baseURL=None, _filter=[], verbose=False):
        self._TOMgraphs = []
        self._TOMgraphs.append(TOMgraph(baseURL, _filter, verbose))
        
    def serialize(self):
        for graph in self._TOMgraphs:
            return graph.serialize()
        
    def byLabel(self, label):
        for _graph in self._TOMgraphs:
            if label in _graph._index:
                return(_graph._index[label])
    
class TOMgraph(ResourceModel):
    
    def __init__(self, baseURL=None, _filter=[], verbose=False):
        (self._scheme, self._netloc, self._path, _params, _query, _fragment ) = urlparse(baseURL) 
        self._baseURL = baseURL
        self._filter = _filter
        self._verbose = verbose
        self._anchorURI = self._scheme + "://" + self._netloc
        self._index = {}
        """ make anchor node """
        self._anchorTemplate = {
            v._bn: self._anchorURI,
            v._l: [
                {
                    v._href: v._null,
                    v._rel: v._anchor 
                },
                {
                    v._href: self._path,
                    v._rel: v._base
                }
            ],
            v._e: [
            ]
        }
        ResourceModel.__init__(self, self._anchorURI, json.dumps(self._anchorTemplate))
        if [] != self._filter:
            self._baseNodeList = self.getNodes({v._rel:v._base})
            self.discover(self._baseNodeList[0], _filter)

    def discover(self, baseNode, _filter, verbose=False):
        
        """ invoked from a base node, recursively interprets a discovery
        filter and processes linked network resources until all potential 
        routes are exhausted. Discovery should attampt to determine the 
        anchor URI of the base node for relative references and should 
        create a new base node and graph instance when a full URL 
        reference is found in an index, i.e. the anchor URI changes. 
        The "server" instance is configured with the anchor URI and 
        takes relative references. The structure of the filter is a 
        recursive array of maps and is interpreted depth first."""
        
        startpath = baseNode._links.get({v._rel: v._base})[0][v._href]
        self._discover(startpath, _filter)
        
    def _discover(self, nextpath, _filter):
        if self._verbose:
            print "discover:", nextpath
        nextNode = self._server._getResource(nextpath)
        """ returns an instance of ResourceNode
        see if it is an index node  """
        if [] != nextNode._links.get({v._rel: v._self, v._rt: v._index}):
            """ add the index node to the graph """
            self.addNodes(TOMnode(nextNode))
            if self._verbose:
                print "node:", nextpath
            """ recursively discover sub index nodes using the current filter rank """
            for link in nextNode._links.get():
                if v._null != link[v._href]:
                    linkpath = link[v._href] # index nodes should have path relative to anchor
                    self._discover(linkpath, _filter)
        else:
            """ discover items that satisfy the current filter rank """
            for item in _filter:
                """ recursively discover nodes in this index which satisfy the current filter item """
                for link in nextNode._links.get({v._rt: item[v._rt] }):
                    linkpath = nextNode._baseName + link[v._href] # non-index nodes have path relative to bn
                    """ add selected nodes one at a time with the TOM function wrapper """
                    newNode = TOMnode(self._server._getResource(linkpath) )
                    self.addNodes(newNode)
                    if self._verbose:
                        print "node:", linkpath
                    """ if there is a label in the filter node, make an entry in the index. If the label
                    is already in the index, add another instance, convert to an array if necessary """
                    if v._label in item:
                        if item[v._label] not in self._index:
                            self._index[item[v._label]] = newNode
                        elif isinstance(self._index[item[v._label]], list):
                            self._index[item[v._label]].append(newNode)
                        else:
                            self._index[item[v._label]] = [self._index[item[v._label]], newNode]
                    """ drive state machine forward, recursively discover using the next filter rank"""
                    if v._has in item:
                        self._discover(linkpath, item[v._has])
                                        
    def lookup(self):
        """ invoked from a starting node, interprets a discovery
        filter and processes linked TOM nodes until all 
        potential routes are exhausted"""
        pass        
        
    def getNodes(self, selectMap):
        """ returns a list of nodes that have matching link attribute values """
        resultSet = []
        for node in self._nodeArray:
            if [] !=  node._links.get(selectMap):
                resultSet.append(node)
        return resultSet
        
        
class TOMnode(ResourceNode):
    """ Build TOMnode from a ResourceNode instance to add a function wrapper for type-specific API methods """
    def __init__(self, node):
        """ getModel returns the representation of the resource in collection+senml internal format """
        ResourceNode.__init__(self, node.getModel())
                
        """ if there is a resource type matching one of the WoT Model classes or supporting classes, make 
            an instance of the support class which will bind class-specific API methods and properties to the node
        """
        for linkAttr in im.rtToClass:
            if [] != self._links.get({v._rel: v._self, v._rt: linkAttr}) :
                im.rtToClass[linkAttr](self)


def selfTest():
    from DiscoveryFilter import _filter
    print "discovering"
    model = ThingObjectModel("http://162.243.62.216:8000/index/", _filter, verbose=True)
    #model = ThingObjectModel("http://localhost:8000/index/", _filter, verbose=True)
    print "completed"
    
    #print model.serialize()
    #print model.byLabel("mylight").serialize()
    
    """ current-level is type Property so will have get and set methods bound to it.
        Currently only values in the model are used. 
        The next version TOM will enable get/set server resource"""
        
    print "starting level:", model.byLabel("current-level").get()
    model.byLabel("current-level").set(50)
    print "new level:", model.byLabel("current-level").get()
    
    
if __name__ == "__main__" :
    selfTest()
