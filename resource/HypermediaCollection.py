"""
Hypermedia Collection extends the Hypermedia Resource class by adding  hypermedia based URI routing and 
senml modeling of items and subresources.


Routing uses link relations rel=grp, rel=sub and rel=item

routing is done by identifying subresources that match the next uri segment to be routed until the last
segment in the request uri is identified for resource selection. Each collection routes requests in a 
self contained way, using only knowledge of it's own uri path and it's direct subresources.

group links labeled grp will be processed by forwarding the request to the href uri of the group link

items are senml modeled values in the local context of the collection, stored in an array of objects.
items are processed locally using the SenmlItems class in the same way an instance of the Links class 
is used to store the collection's links.

subresources are sub-collections in the context of the collection. requests to subresources are routed 
to the subresources selected

items and subresources are selected by either matching the resource uri with the request uri, or matching 
the collection uri with the request uri and seleting the resource(s) using query filtering on the link 
attributes, or by selecting the collection uri and matching resource names with senml names "n" in the 
update body. 

routing and group forwarding is done in this class, and resource processing e.g. GET, POST, is done in 
the respective Content Handlers.

resource endpoints are subresource collections with a single item, the item being referenced using the 
name of the collection e.g. /a/b/c is the URI of a resource endpoint. The resource c is a collection 
with a single item that is referenced by the base name and returns representations like this: 

senml    { "bn": "/a/b/c", "e": {"sv": "test"} }

collection+senml    { "l": {"href": "", "rel": "item"}, "bn": "/a/b/c", "e": {"sv": "test"} }

Items and subresources are created by POSTing representations containing items and optionally links in
the senml+collection content-format. THe location of the created resource will consist of the collection 
uri and the resource name specified in the "href" link attribute or the "n" attribute of the corresponding
senml element.
    
Links that fail to select a resource are returned with a status code of 404 Not Found
"""

import terms as v

from HypermediaResource import HypermediaResource
from copy import deepcopy
from Items import SenmlItems
from PlainTextHandler import PlainTextHandler
from SenmlHandler import SenmlHandler
from SenmlCollectionHandler import SenmlCollectionHandler

class HypermediaCollection(HypermediaResource):

    def __init__(self, rootResource=None, uriPath=["/"], resourceItem=None ):
        HypermediaResource.__init__(self)
        self._uriPath = uriPath
        self._pathString = "/"
        for pathElement in uriPath[1:]:
            self._pathString += (pathElement + "/")
        self._pathLen = len(self._uriPath)
        if ["/"] == uriPath :
            self._rootResource = self
        else:
            self._rootResource = rootResource
        self._unrouted = 0
            
        self._itemArray = SenmlItems()
        self._subresources = {}
        
        """ if there is an item in the constructor, null the resource name and add it to items """
        if None != resourceItem :
            resourceItem[v._n] = v._null
            self._itemArray.add(resourceItem)
            self._linkArray.selectMerge({v._href:v._null},{ v._rel: v._item})

        PlainTextHandler(self)
        SenmlHandler(self)
        SenmlCollectionHandler(self)

    """ Route requests using hyperlinks. Link relations "item" and "sub" are used to identify 
        local items in the collection and sub resources, respectively."""        
    def routeRequest(self, request):  
        self._request = request
        self._unrouted = len(request[v.uriPath]) - self._pathLen
            
        if 0 == self._unrouted:
            """ this resource is selected, process content-format """
            self._processGroup(self._request)
            self.handleRequest(self._request)
        else:
            self._resourceName = self._request[v.uriPath][self._pathLen]
            if 1 == self._unrouted and [] != self._linkArray.get({v._href:self._resourceName, v._rel:v._item}) :
                """ item in the local collection is selected, handle content-format in this context"""
                self.handleRequest(self._request)
            elif [] != self._linkArray.get({v._href:self._resourceName, v._rel:v._sub}):
                """ route request to subresource item"""
                self._subresources[self._resourceName].routeRequest(self._request)
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

    def _createSubresource(self, resourceName, resourceItem=None):
        self._subresources[resourceName] = \
            HypermediaCollection( self._rootResource, self._uriPath + [resourceName], resourceItem) 
        return self._subresources[resourceName]
