import terms as v
from HypermediaResource import ContentHandler
import json

class PlainTextHandler(ContentHandler):
    
    _contentFormat = v.plainTextType

    def _processRequest(self, request):
        
        if 0 ==self._resource._unrouted:
            """ process collection URI, select by query parameters """
            self._selectedLinks = self._resource._linkArray.get(request[v.uriQuery])
            if 1 == len(self._selectedLinks):
                self._resourceName = self._selectedLinks[0][v._href]
            else:
                request[v.response][v.status] = v.NotFound
        else:
            self._resourceName = self._resource._resourceName
        """ process item, resourceName is from request URI or from query filtering """
        if v.get == request[v.method] :
            if v._rel in self._link and v._item == self._link[v._rel] :            
                """ get item in local context """
                request[v.response][v.payload] = \
                        json.dumps(self._resource._itemArray.getValueByName(self._resourceName) )
                request[v.response][v.status] = v.Success
            elif v._rel in self._link and v._sub == self._link[v._rel] :
                """ get subresource item """
                request[v.uriPath] = self._resource._uriPath + self._link[v._href]
                self._subresources[self._link[v._href]].routeRequest(request)
                """ send request and wait for response """                    
                return
        elif v.put == request[v.method] :
            if v._rel in self._link and v._item == self._link[v._rel] :            
                self._resource._itemArray.updateValueByName(self._resourceName, json.loads(request[v.payload]))
                request[v.response][v.status] = v.Success
            elif v._rel in self._link and v._sub == self._link[v._rel] :
                """ route a request URI made from the collection path + resource name """
                request[v.uriPath] = self._resource._uriPath + self._link[v._href]
                self._subresources[self._link[v._href]].routeRequest(request)
        else:
            request[v.response][v.status] = v.MethodNotAllowed
