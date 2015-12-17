
import terms as v

from HypermediaResource import HypermediaResource, ContentHandler

class HypermediaCollection(HypermediaResource):
    
    def __init__(self):
        HypermediaResource.__init__()
        self.SenmlItemHandler(self)
        self.SenmlCollectionHandler(self)
        
        self._linkArray = self.Links()
        self._items = []
    
    def routeRequest(self, request):
        pass
    
class SenmlItemHandler(ContentHandler):
        
        _contentFormat = v.senmlCollectionType
    
class SenmlCollectionHandler(ContentHandler):
        
        _contentFormat = v.senmlType