import terms as v
from HypermediaResource import ContentHandler
import json

class SenmlHandler(ContentHandler):
        
    _contentFormat = v.senmlType
            
    def _processRequest(self, request):
        if self._resource._unrouted == 1:
            """ process item """
            if v.get == request[v.method]:
                request[v.response][v.payload] = \
                        json.dumps( self._resource._itemArray.getByName(self._resource._resourceName) )
                request[v.response][v.status] = v.Success
            elif v.put == request[v.method]:
                self._resource._itemArray.updateByName( self._resource._resourceName, json.loads(request[v.payload]) )
                request[v.response][v.status] = v.Success
            else:
                request[v.response][v.status] = v.MethodNotAllowed
        else:
            """ uri-path selects collection, use query parameters to select Items 
            """
            request[v.response][v.status] = v.UnsupportedType

