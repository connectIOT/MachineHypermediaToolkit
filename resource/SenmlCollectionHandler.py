import terms as v
from HypermediaResource import ContentHandler
import json

class SenmlCollectionHandler(ContentHandler):
        
    _contentFormat = v.senmlCollectionType

    def _processRequest(self, request):
        self._selectedLinks = self._resource._linkArray.get(request[v.uriQuery])
        """ if the query is empty, all links are returned """
        if [] == self._selectedLinks :
            request[v.response][v.status] = v.NotFound
            return
