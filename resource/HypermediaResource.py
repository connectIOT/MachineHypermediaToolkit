
import json
import terms as v
from Links import Links

class HypermediaResource(object) :
    
    def __init__(self):
        
        self._contentHandlers = {}
        LinkFormatHandler(self)
        LinkFormatPatchHandler(self)
        PlainTextHandler(self)
        SenmlValueHandler(self)

        self._value = {v._v:None}
        self._linkArray = Links({v._href: "", v._rel: v._self, v._rt: "resource"})
        
    def registerContentHandler(self, contentFormat, handler):
        self._contentHandlers[contentFormat] = handler
        
    def handleRequest(self, request):
        if request[v.contentFormat] in self._contentHandlers:
            self._contentHandlers[request[v.contentFormat]].handleRequest(request)        
        else:
            request[v.response][v.status] = v.UnsupportedType
        return

class ContentHandler:
    
    _contentFormat = None
        
    def __init__(self, resource):
        self._processors = []
        self._resource = resource
        self.addProcessor(self._processRequest)
        self._resource.registerContentHandler(self._contentFormat, self)
    
    def addPreProcessor(self, processor):
        self._processors.insert(0,processor)
        
    def addProcessor(self, processor):
        self._processors.append(processor)
        
    def handleRequest(self, request):
        for process in self._processors:
            if process(request):
                return
        return
      
    def _processRequest(self, request):
        request[v.response][v.status] = v.ServerError
        return 
        
class LinkFormatHandler(ContentHandler):
    
    _contentFormat = v.linkFormatJsonType
       
    def _processRequest(self, request):
        if request[v.method] == v.get:
            request[v.response][v.payload] = json.dumps(self._resource._linkArray.get(request[v.uriQuery]))
            request[v.response][v.status] = v.Success
        elif request[v.method] == v.post:
            self._resource._linkArray.add(json.loads(request[v.payload]))
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed
                    
class LinkFormatPatchHandler(ContentHandler):

    _contentFormat = v.linkFormatMergeType
    
    def _processRequest(self, request):
        if request[v.method] == v.patch:
            self._resource._linkArray.selectMerge( request[v.uriQuery], json.loads(request[v.payload]) )
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed
            
class PlainTextHandler(ContentHandler):
    
    _contentFormat = v.plainTextType

    def _processRequest(self, request):
        if request[v.method] == v.get:
            for key in self._resource._value:
                if key in (v._v, v._bv, v._sv, v._ov):
                    request[v.response][v.payload] = json.dumps(self._resource._value[key])
            request[v.response][v.status] = v.Success
        elif request[v.method] == v.put:
            self._newValue = (json.loads(request[v.payload]))
            if isinstance(self._newValue, str) or isinstance(self._newValue, unicode):
                self._resource._value[v._sv] = self._newValue
            elif isinstance(self._newValue, bool):
                self._resource._value[v._bv] = self._newValue
            elif isinstance(self._newValue, list) or isinstance(self._newValue, dict):
                self._resource._value[v._ov] = self._newValue
            else:
                self._resource._value[v._v] = self._newValue
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed

class SenmlValueHandler(ContentHandler):
    
    _contentFormat = v.senmlType

    def _processRequest(self, request):
        if request[v.method] == v.get:
            request[v.response][v.payload] = json.dumps(self._resource._value)
            request[v.response][v.status] = v.Success
        elif request[v.method] == v.put:
            self._resource._value = json.loads(request[v.payload])
            request[v.response][v.status] = v.Success
        else:
            request[v.response][v.status] = v.MethodNotAllowed

