import MachineHypermediaToolkit.terms as v
from HypermediaResource import ContentHandler
import json
from Links import Links

class PlainTextHandler(ContentHandler):
    
    _contentFormat = v.plainTextType

    def _processRequest(self, request):
        if 0 == self._resource._unrouted:
            """ process collection URI, select by query parameters, 
                require only one resource link, item or subresource, 
                is selected for text/plain format """
            self._itemLinks = Links(self._resource._linkArray.get(request[v.uriQuery])).get({v._rel:v._item})
            self._subLinks = Links(self._resource._linkArray.get(request[v.uriQuery])).get({v._rel:v._sub})
            if 1 == len(self._itemLinks) and 0 == len(self._subLinks) :
                self._resourceName = self._itemLinks[0][v._href]
            elif 1 == len(self._subLinks) and 0 == len(self._itemLinks) :
                self._resourceName = self._subLinks[0][v._href]
            else:
                request[v.response][v.status] = v.NotFound
            """ clear query parameters when consumed at the path endpoint """
            request[v.uriQuery] = {}
        elif 1 == self._resource._unrouted :
            """ a local context item matched the last path element, _resourceName is set in the resource """
            self._resourceName = self._resource._resourceName
        else:
            request[v.response][v.status] = v.ServerError
            
        """ process item, resourceName is from request URI or from query filtering """
        if v.get == request[v.method] :
            if 1 == len(self._itemLinks) :            
                """ get item in local context """
                request[v.response][v.payload] = \
                        json.dumps(self._resource._itemArray.getValueByName(self._resourceName) )
                request[v.response][v.status] = v.Success
            elif 1 == len(self._subLinks) :
                """ get subresource item """
                request[v.uriPath] = self._resource._uriPath + [self._resourceName]
                request[v.uriQuery] = {v._href:v._null}
                self._resource._subresources[self._resourceName].routeRequest(request)
                """ send request and wait for response """                    
            else:
                request[v.response][v.status] = v.NotFound
                
        elif v.put == request[v.method] :
            if 1 == len(self._itemLinks) :            
                self._resource._itemArray.updateValueByName(self._resourceName, json.loads(request[v.payload]))
                request[v.response][v.status] = v.Success
            elif 1 == len(self._subLinks) :
                """ route a request URI made from the collection path + resource name """
                request[v.uriPath] = self._resource._uriPath + [self._resourceName]
                request[v.uriQuery] = {v._href:v._null}
                self._resource._subresources[self._resourceName].routeRequest(request)
            else:
                request[v.response][v.status] = v.NotFound
        else:
            request[v.response][v.status] = v.MethodNotAllowed
