
import terms as v

from HypermediaResource import HypermediaResource
from copy import deepcopy
from Items import SenmlItems
from PlainTextHandler import PlainTextHandler
from SenmlHandler import SenmlHandler
from SenmlCollectionHandler import SenmlCollectionHandler

class HypermediaCollection(HypermediaResource):

    def __init__(self, rootResource=None, uriPath=["/"]):
        HypermediaResource.__init__()
        PlainTextHandler(self)
        SenmlHandler(self)
        SenmlCollectionHandler(self)

        self._itemArray = SenmlItems(self)
        self._subresources = {}
        self._uriPath = uriPath
        if ["/"] == uriPath :
            self._rootResource = self
        else:
            self._rootResource = rootResource
        self._unrouted = 0

    def routeRequest(self, request):  
        self._request = request
        self._pathLen = len(self._uriPath)
        self._unrouted = len(request[v.uriPath]) - self._pathLen  
            
        if 0 == self._unrouted:
            """ this resource is selected, process content-format """
            self._processGroup(self._request)
            self.handleRequest(self._request)
        else:
            self._resourceName = self._request[v.uriPath][self._pathLen]
            if [] != self._linkArray.get({v._href:self._resourceName, v._rel:v._sub}):
                """ route request to subresource item"""
                self._subresources[self._resourceName].routeRequest(self._request)
            elif [] != self.linkArray.get({v._href:self._resourceName, v._rel:v._item}) and self._unrouted == 1:
                """ item in the local collection is selected, process content-format """
                self.handleRequest(self._request)
            else:
                """ nothing to route or process """
                self._request[v.response][v.status] = v.NotFound

    def _processGroup(self, request):
        """invoke a proxy or promise to forward the request to each resource marked with rel=grp """
        self._groupLinks = self._linkArray.get({v._rel:v._grp})
        if [] != self._groupLinks:
            request[v.response][v.payload] = []
            request[v.response][v.code] = []
            """ make request instances """
            self._requests = []
            for self._link in self._groupLinks:
                print "group link: ", self._link
                self._requests.append( deepcopy(request) )
            for self._request in self._requests:
                """ overwrite uriPath """                
                self._request[v.uriPath] = ["/"]
                for self._pathElement in self._groupLinks.popleft()[v._href].split("/"):
                    if len(self._pathElement) > 0:
                        self._request[v.uriPath].append(self._pathElement)
                """ route request to root resource if path starts with /  """        
                if "/" == self._request[v.uriPath][0]:
                    self._rootResource.routeRequest(self._request)
                else:
                    self.routeRequest(self._request)
            """ collect the results """
            for self._request in self._requests:
                request[v.response][v.payload].append(self._request[v.response][v.payload])
                if v.Success != self._request[v.response][v.status] and \
                        v.Created != self._request[v.response][v.status]:
                    request[v.response][v.status] = v.BadRequest
                request[v.response][v.code].append(self._request[v.response][v.code]) 
            return self._requests
        else:
            return None

    def _createSubresource(self, resourceName):
        self._subresources[resourceName] = \
            HypermediaCollection( self._rootResource, self._uriPath + [resourceName] ) 
       
