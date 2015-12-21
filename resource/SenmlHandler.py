import terms as v
from HypermediaResource import ContentHandler
import json

class SenmlHandler(ContentHandler):
        
    _contentFormat = v.senmlType
            
    def __postInit__(self):
        self._senml = Senml()
        
    def _processRequest(self, request):
        
        if 0 == self._resource._unrouted :
            """ uri-path selects collection resource with SenML content format
                reference to local items or subresources using SenML names + query selection
                GET - query filter, return SenML items
                PUT, POST - name match with SenML "n" and query filter
                DELETE, remove resources selected by query filter
            """
            self._selectedLinks = self._resource._linkArray.get(request[v.uriQuery])
            """ if the query is empty, all links are returned """
            if [] == self._selectedLinks :
                request[v.response][v.status] = v.NotFound
                return
            """ clear query parameters when consumed at the path endpoint """
            request[v.uriQuery] = {}
            if v.get == request[v.method]:
                """ get returns items associated with selected links as a senml multi-resource instance"""
                self._senml.init()
                for self._link in self._selectedLinks :
                    if v._rel in self._link and v._item == self._link[v._rel] :
                        """ get item in local context and add to the result """
                        self._senml.addItem( self._itemArray.getItemByName(self._link[v._href]) )
                    elif v._rel in self._link and v._sub == self._link[v._rel] :
                        """ get subresource item """
                        request[v.uriPath] = self._resource._uriPath + self._link[v._href]
                        self._subresources[self._link[v._href]].routeRequest(request)
                        """ send request and wait for response """
                        if v.Success == request[v.response][v.status]:
                            self._senml.addItem( json.loads(request[v.response][v.payload]) )
                        else:
                            """ if there is any error, reutrn with the error status in the response """
                            return
                request[v.response][v.payload] = self._senml.serialize()                    
                request[v.response][v.status] = v.Success
                
            elif v.put == request[v.method]:
                """ put updates the selected resources with the items in the payload  """ 
                self._senml.load(request[v.payload])
                for item in self._senml.items():
                    for self._link in self._selectedLinks :
                        if self._link[v._href] == item[v._n]:
                            if v._rel in self._link and v._item == self._link[v._rel] :
                                self._itemArray.updateItemByName(self._link[v._href], item)
                            elif v._rel in self._link and v._sub == self._link[v._rel] :
                                """ route a request URI made from the collection path + resource name 
                                    send the item with a zero length senml resource name """
                                request[v.uriPath] = self._resource._uriPath + self._link[v._href]
                                item[v._n] = ""
                                request[v.payload] = Senml(item).serialize()
                                self._subresources[self._link[v._href]].routeRequest(request)
                                if v.Success != request[v.response][v.status]:
                                    return
 
        elif 1 == self._resource._unrouted :
            """ Select and process item """
            if v.get == request[v.method]:
                request[v.response][v.payload] = \
                        json.dumps( self._resource._itemArray.getItemByName(self._resource._resourceName) )
                request[v.response][v.status] = v.Success
            elif v.put == request[v.method]:
                self._resource._itemArray.updateItemByName( self._resource._resourceName, json.loads(request[v.payload]) )
                request[v.response][v.status] = v.Success
            else:
                request[v.response][v.status] = v.MethodNotAllowed
        else:
            request[v.response][v.status] = v.BadRequest

from Items import SenmlItems

class Senml():
    
    def __init__(self, items=None):
        self._senml = {}
        self._items = SenmlItems()
        self._senml[v._e] = self._items._items
        if items != None:
            self.addItems(items)
        
    def init(self):
        self.__init__()
        
    def addItems(self, items):
        self._items.add(items)
        
    def serialize(self):
        return json.dumps(self._senml)
    
    def load(self, jsonString):
        self._loadObject = json.loads(jsonString)
        self._senml.addItems(self._loadObject[v._e])
        
    def items(self):
        return self._items._items

