import terms as v
from HypermediaResource import ContentHandler
from SenmlHandler import Senml
import json

class SenmlCollectionHandler(ContentHandler):
        
    _contentFormat = v.senmlCollectionType
    
    def __postInit__(self):
        self._senml = SenmlCollection()
        
    def _processRequest(self, request):
        self._selectedLinks = self._resource._linkArray.get(request[v.uriQuery])
        """ if the query is empty, all links are returned """
        if [] == self._selectedLinks :
            request[v.response][v.status] = v.NotFound
            return
        request[v.uriQuery] = {}
        if v.get == request[v.method]:
            """ return a representation of a senml instance with a links element"""
            self._senml.init()
            self._senml.addLinks(self._selectedLinks)
            for self._link in self._selectedLinks:
                if v._rel in self._link and v._item == self._link[v._rel] :
                    """ get item in local context and add to the result """
                    self._senml.addItems( self._itemArray.getItemByName(self._link[v._href]) )
                elif v._rel in self._link and v._sub == self._link[v._rel] :
                    """ get subresource item """
                    request[v.uriPath] = self._resource._uriPath + self._link[v._href]
                    self._subresources[self._link[v._href]].routeRequest(request)
                    """ send request and wait for response """
                    if v.Success == request[v.response][v.status]:
                        self._senml.addItems( json.loads(request[v.response][v.payload]) )
                    else:
                        """ if there is any error, reutrn with the error status in the response """
                        return
            request[v.response][v.payload] = self._senml.serialize()                    
            request[v.response][v.status] = v.Success
            
        elif v.post == request[v.method]:
            """ create new items in the collection. Takes a senml document with or without 
                a links element. If the links element is elided, default links are constructed """
            self._senml.load(request[v.payload])
            
from Links import Links
         
class SenmlCollection(Senml):
    
    def __init__(self, items=None, links=None):
        Senml.__init__(items)
        self._links = Links()
        self._senml[v._l] = self._links._links
        if links != None:
            self.addLinks(links)
                
    def addLinks(self, links):        
            self.links.add(links)  
            
    def links(self):
        return self._links._links

    def load(self, jsonString):
        Senml.load(jsonString)
        self._senml.addLinks(self._loadObject[v._l])

