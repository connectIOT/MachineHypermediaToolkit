
import json
import terms as v
from Links import Links

class HypermediaResource(object) :
    
    def __init__(self):
        
        self._contentFormats = {}
        LinkFormatHandler(self)
        LinkFormatPatchHandler(self)
        PlainTextHandler(self)
        SenmlValueHandler(self)

        self._value = {v._n:None}
        self._linkArray = Links({v._href: "", v._rel: [v._self], v._rt: ["resource"]})
        
    def registerContentHandler(self, contentFormat, handler):
        self._contentFormats[contentFormat] = handler
        
    def handleRequest(self, request):
        if request[v.contentFormat] in self._contentFormats:
            self._contentFormats[request[v.contentFormat]](request)        
        else:
            request[v.response][v.status] = v.UnsupportedType

            
class LinkFormatHandler:
    
    def __init__(self, resource):
        self._resource = resource
        self._resource.registerContentHandler(v.linkFormatJsonType, self._handleRequest)
       
    def _handleRequest(self, request):
        if request[v.method] == v.get:
            request[v.response][v.payload] = json.dumps(self._resource._linkArray.get())
            request[v.response][v.status] = v.Success
        elif request[v.method] == v.post:
            self._resource._linkArray.add(json.loads(request[v.payload]))
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed

                    
class LinkFormatPatchHandler:
    
    def __init__(self, resource):
        self._resource = resource
        self._resource.registerContentHandler(v.linkFormatMergeType, self._handleRequest)
        
    def _handleRequest(self, request):
        if request[v.method] == v.patch:
            self._resource._linkArray.selectMerge( json.loads(request[v.uriQuery]), json.loads(request[v.payload]) )
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed
            

class PlainTextHandler:
    
    def __init__(self, resource):
        self._resource = resource
        self._resource.registerContentHandler(v.plainTextType, self._handleRequest)

    def _handleRequest(self, request):
        if request[v.method] == v.get:
            request[v.response][v.payload] = json.dumps(self._resource._value[v._v])
            request[v.response][v.status] = v.Success
        elif request[v.method] == v.put:
            self._resource._value[v._v] = (json.loads(request[v.payload]))
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed


class SenmlValueHandler:
    
    def __init__(self, resource):
        self._resource = resource
        self._resource.registerContentHandler(v.senmlType, self._handleRequest)

    def _handleRequest(self, request):
        if request[v.method] == v.get:
            request[v.response][v.payload] = json.dumps(self._resource._value)
            request[v.response][v.status] = v.Success
        elif request[v.method] == v.put:
            self._resource._value = json.loads(request[v.payload])
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed


