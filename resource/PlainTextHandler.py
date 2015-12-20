import terms as v
from HypermediaResource import ContentHandler
import json

class PlainTextHandler(ContentHandler):
    
    _contentFormat = v.plainTextType

    def _processRequest(self, request):
        if self._resource._unrouted == 0:
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
            """ also check subresources """
            request[v.response][v.payload] = json.dumps(self._resource._itemArray.getValueByName(self._resourceName) )
            request[v.response][v.status] = v.Success
        elif v.put == request[v.method] :
            """ check for subresources """
            self._resource._itemArray.updateValueByName(self._resourceName, json.loads(request[v.payload]))
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed

