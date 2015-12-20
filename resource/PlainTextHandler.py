import terms as v
from HypermediaResource import ContentHandler
import json

class PlainTextHandler(ContentHandler):
    
    _contentFormat = v.plainTextType

    def _processRequest(self, request):
        if request[v.method] == v.get:
            self._itemArray.getValueByName(self._resourceName)
            request[v.response][v.payload] = json.dumps(self._resource._itemArray.getValueByName(self._resourceName) )
            request[v.response][v.status] = v.Success
        elif request[v.method] == v.put:
            self._newValue = (json.loads(request[v.payload]))
            self._resource._itemArray.updateValueByName(self._resourceName, self._newValue)
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed
