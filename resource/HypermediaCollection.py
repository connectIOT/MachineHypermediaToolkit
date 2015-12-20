
import terms as v
import json

from HypermediaResource import HypermediaResource, ContentHandler
from copy import deepcopy

class HypermediaCollection(HypermediaResource):

    def __init__(self, rootResource=None, uriPath=["/"]):
        HypermediaResource.__init__()
        self.SenmlHandler(self)
        self.SenmlCollectionHandler(self)

        self._itemArray = Items(self)
        self._subresources = {}
        self._uriPath = uriPath
        if "/" == uriPath :
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
            self._nextName = self._request[v.uriPath][self._pathLen]
            if [] != self._linkArray.get({v._href:self._nextName, v._rel:v._sub}):
                """ route request to subresource item"""
                self._subresources[self._nextName].routeRequest(self._request)
            elif [] != self.linkArray.get({v._href:self._nextName, v._rel:v._item}) and self._unrouted == 1:
                """ item in the local collection is selected, process content-format """
                self.handleRequest(self._request)
            else:
                """ nothing to route or process """
                self._request[v.response][v.status] = v.NotFound

    def _processGroup(self, request):
        """invoke a proxy or promise to forward the request to each resource marked with rel=grp """
        self._groupLinks = self._linkArray.get({v._rel:v._grp})
        self._requests = []
        self._responses = []
        if [] != self._groupLinks:
            """ make request instances """
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
                    self._rootResource.routeRequest(self._proxyRequest)
                else:
                    self.routeRequest(self._request)
                """ collect the results """
                self._requests.append(self._request)
            return self._requests
        else:
            return None
     
    def _createSubresource(self, resourceName):
        self._subresources[resourceName] = \
            HypermediaCollection( self._rootResource, self._uriPath.append(resourceName) ) 


class Items(object):
    def __init__(self, resource):
        self._items = []
        
    def add(self, items=[]):
        self._items.extend(items)
        
    def remove(self, items=[]):
        for removeName in items:
            for item in self._items:
                if removeName == item[v._n]:
                    self._items.remove(item)
    
    def getByName(self, itemName):
        if itemName in self._items:
            return self._items[itemName]
        else:
            return None
    
    def updateByName(self, itemName, itemValue):
        if itemName in self._items:
            self._items[itemName] = itemValue
        else:
            return None


class SenmlHandler(ContentHandler):
        
    _contentFormat = v.senmlType
            
    def _processRequest(self, request):
        if self._resource._unrouted == 1:
            """ process item """
            if v.get == request[v.method]:
                request[v.response][v.payload] = json.dumps(self._resource._items[self._resourceName])
                request[v.response][v.status] = v.Success
            elif v.put == request[v.method]:
                self._resource._items[self._resourceName] = json.loads(request[v.payload])
                request[v.response][v.status] = v.Success
            else:
                request[v.response][v.status] = v.MethodNotAllowed
        else:
            """ uri-path selects collection, use query parameters to select items 
            """
            request[v.response][v.status] = v.UnsupportedType


class SenmlCollectionHandler(ContentHandler):
        
    _contentFormat = v.senmlCollectionType

    def _processRequest(self, request):
        pass
