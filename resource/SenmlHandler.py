import terms as v
from HypermediaResource import ContentHandler
import json

class SenmlHandler(ContentHandler):
        
    _contentFormat = v.senmlType
            
    def _processRequest(self, request):
        if self._resource._unrouted == 0:
            """ uri-path selects collection resource with SenML content format
                reference to local items or subresources using SenML names + query selection
                GET - query filter, return SenML items
                PUT, POST - name match with SenML "n" and query filter
                DELETE, remove resources selected by query filter
            """
            self._selectedLinks = self._resource._linkArray.get(request[v.uriQuery])
            if [] == self._selectedLinks :
                request[v.response][v.status] = v.NotFound
                return
            else:
                request[v.uriQuery] = {}
                if v.get == request[v.method]:
                    """ get returns items associated with selected links """
                    self._selectedItems = []
                    for self._link in self._selectedLinks :
                        if v._rel in self._link and v._item == self._link[v._rel] :
                            self._selectedItems.append( self._itemArray.getItemByName(self._link[v._href]) )
                        elif v._rel in self._link and v._sub == self._link[v._rel] :
                            request[v.uriPath] = self._resource._uriPath + self._link[v._href]
                            self._subresources[self._link[v._href]].routeRequest(request)
                            if v.Success == request[v.response][v.status]:
                                self._selectedItems.append( request[v.response][v.payload] )
                            else:
                                return
                    request[v.response][v.payload] = json.dumps(self._selectedItems)                    
                    request[v.response][v.status] = v.Success
                    
                elif v.put == request[v.method]:
                    """ put updates the selected resources with the items in the payload  """ 
                    for item in json.loads(request[v.payload]):
                        for self._link in self._selectedLinks :
                            if self._link[v._href] == item[v._n]:
                                if v._rel in self._link and v._item == self._link[v._rel] :
                                    self._itemArray.updateItemByName(self._link[v._href], self._link)
                                elif v._rel in self._link and v._sub == self._link[v._rel] :
                                    """ route a request URI made from the collection path + resource name """
                                    request[v.uriPath] = self._resource._uriPath + self._link[v._href]
                                    self._subresources[self._link[v._href]].routeRequest(request)
                                    if v.Success != request[v.response][v.status]:
                                        return
 
        elif self._resource._unrouted == 1:
            """ Select and process item """
            if v.get == request[v.method]:
                request[v.response][v.payload] = json.dumps( self._resource._itemArray.getItemByName(self._resource._resourceName) )
                request[v.response][v.status] = v.Success
            elif v.put == request[v.method]:
                self._resource._itemArray.updateItemByName( self._resource._resourceName, json.loads(request[v.payload]) )
                request[v.response][v.status] = v.Success
            else:
                request[v.response][v.status] = v.MethodNotAllowed
        else:
            request[v.response][v.status] = v.BadRequest
