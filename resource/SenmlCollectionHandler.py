import terms as v
from HypermediaResource import ContentHandler
import json

class SenmlCollectionHandler(ContentHandler):
        
    _contentFormat = v.senmlCollectionType

    def _processRequest(self, request):
        pass