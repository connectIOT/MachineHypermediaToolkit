import MachineHypermediaToolkit.terms as v
from Links import Links
from HypermediaResource import ContentHandler

class SenmlHandler(ContentHandler):
        
    _contentFormat = v.senmlType
            
    def __postInit__(self):
        self._senml = Senml(baseName=self._resource._pathString)
        
    def _processRequest(self, request):
        
        if 0 == self._resource._unrouted :
            """ uri-path selects collection resource with SenML content format
                reference to local items or subresources using SenML names + query selection
                GET - query filter, return SenML items
                PUT, POST - name match with SenML "n" and query filter
                DELETE, remove resources selected by query filter
            """
            self._selectedLinks = Links(self._resource._linkArray.get(request[v.uriQuery]))
            """ if the query is empty, all links are returned """
            if [] == self._selectedLinks.get() :
                request[v.response][v.status] = v.NotFound
                return
            """ clear query parameters when consumed at the path endpoint """
            request[v.uriQuery] = {}
            
            if v.get == request[v.method]:
                """ get returns items associated with selected links as a senml multi-resource instance"""
                self._senml.configure()
                for self._link in self._selectedLinks.get({v._rel:v._item}) :
                    """ get items in local context and add to the result """
                    self._senml.addItems( self._resource._itemArray.getItemByName(self._link[v._href]) )
                for self._link in self._selectedLinks.get({v._rel:v._sub}) :
                    """ get the item at each subresource uri but not it's subresources or named items """
                    request[v.uriPath] = self._resource._uriPath + [self._link[v._href]]
                    request[v.uriQuery] = {v._href:v._null}
                    self._resource._subresources[self._link[v._href]].routeRequest(request)
                    """ send request and wait for response """
                    if v.Success == request[v.response][v.status]:
                        self._result = Senml()
                        self._result.load(request[v.response][v.payload])
                        self._updateItem = self._result._items.getItemByName(v._null)
                        if self._updateItem :
                            self._updateItem[v._n] = self._link[v._href]
                            self._result._items.updateItemByName(v._null, self._updateItem )
                            self._senml.addItems( self._result.items() )
                    else:
                        """ if there is any error, reuturn with the error status in the response """
                        return

                request[v.response][v.payload] = self._senml.serialize()                    
                request[v.response][v.status] = v.Success
                
            elif v.put == request[v.method]:
                """put updates the selected resources with the matching name items in the payload """ 
                self._senml.load(request[v.payload])
                for item in self._senml.items():
                    for self._link in self._selectedLinks.get({v._rel:v._item}) :
                        if self._link[v._href] == item[v._n]:
                            self._resource._itemArray.updateItemByName(self._link[v._href], item)
                    for self._link in self._selectedLinks.get({v._rel:v._sub}) :
                        """ route a request URI made from the collection path + resource name 
                            send the item with a zero length senml resource name """
                        request[v.uriPath] = self._resource._uriPath + [self._link[v._href]]
                        item[v._n] = ""
                        request[v.payload] = Senml(item).serialize()
                        request[v.uriQuery] = {v._href:v._null}
                        self._resource._subresources[self._link[v._href]].routeRequest(request)
                        if v.Success != request[v.response][v.status]:
                            return
                request[v.response][v.status] = v.Success
            else:
                request[v.response][v.status] = v.MethodNotAllowed

        elif 1 == self._resource._unrouted :
            """ Select and process item """
            if v.get == request[v.method]:
                self._senml.configure()
                self._senml.addItems(self._resource._itemArray.getItemByName(self._resource._resourceName))                 
                request[v.response][v.payload] = self._senml.serialize()
                request[v.response][v.status] = v.Success
            elif v.put == request[v.method]:
                self._senml.load(request[v.payload])
                self._resource._itemArray.updateItemByName(self._resource._resourceName, self._senml.items().pop())
                request[v.response][v.status] = v.Success
            else:
                request[v.response][v.status] = v.MethodNotAllowed
        else:
            request[v.response][v.status] = v.ServerError


from Items import SenmlItems
import json

class Senml():
    
    def __init__(self, items=None, baseName=None):
        self._senml = {}
        self._items = SenmlItems(items)
        self._senml[v._e] = self._items._items
        if None != baseName :
            self._baseName = baseName
            self._senml[v._bn] = baseName
        
    def configure(self, items=None):
        self.__init__(items, self._baseName)
        
    def addItems(self, items):
        if [] != items:
            self._items.add(items)
        
    def serialize(self):
        return json.dumps(self._senml, sort_keys=False, indent=2, separators=(',', ': '))
    
    def load(self, jsonString):
        self._loadObject = json.loads(jsonString)
        self.addItems(self._loadObject[v._e])
        
    def items(self):
        return self._items._items

