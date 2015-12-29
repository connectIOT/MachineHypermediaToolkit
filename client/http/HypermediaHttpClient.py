"""
HypermediaHttpSClient uses the HTTPConnection class in httplib to create a dictionary driven interface
to http requesters and response handlers to be used by clients for the HttpHypermediaServer

Requests and their associated responses are exposed in a dictionary interface for processing by proxies and resources
in a linked structure by passing references to the request and the associated response to resources at selected link
targets.

The server invokes a request handler callback when requests are received, and passes a reference to a structure
containing request and response elements used in processing the hypermedia.

REQUEST
URI
content-format
method
payload

RESPONSE
status (code and reason)
content-format
payload

Hypermedia handlers will process the URI and query parameters first in order to select a set of resources for processing, 
then apply the content format and method along with any supplementary options to the resources.

The terms used in the request and response elements are semantically aligned with the vocabularies used in links and
forms to describe hypermedia state exchanges, and are abstracted across different protocols like http and CoAP.

Common abstractions are needed to support multiple protocols. Initially there are HTTP and CoAP bindings to a 
common set of terms.

URI and Query parameters are the same in http and CoAP

methods use the following mappings

GET
PUT
POST
PATCH
DELETE

Mappings to CoAP content-format identifiers:

22001    application/collection+senml+json
22002    application/senml+json
22003    application/link-format+json
22004    application/forms+link-format+json

responseTypes are a common subset of http and CoAP response codes

Success           200, 202, 204    2.02, 2.03, 2.04, 2.05
Created           201              2.01
BadRequest        400              4.00, 4.02
Unauthorized      401              4.01
Forbidden         403              4.03
NotFound          404              4.04
MethodNotAllowed  405              4.05
NotAcceptable     406              4.06
Conflict          409              4.09
PrecondFailed     412              4.12
UnsupportedType   415              4.15
ServerError       500              5.00

JSON keys to the request-response interface are described in the example below.
This is the common CRUD interface between HTTP and CoAP, and can be used as a 
generic REST proxy.

{
    "uriPath": ["/","a", "b"], 
    "uriQuery": {"rt": "test", "obs": "", "if": "core.b"}
    "contentFormat": "application/link-format+json",
    "options": {}
    "method": "GET",
    "payload": null,
    "response": {
        "status": "Success",
        "code": "204",
        "reason": "No Content",
        "contentFormat": "application/link-format+json",
        "payload": "[{"href":"","rel":"self","rt":"index"}]"
        }
}
    
Client fills request form and sends to server using selected protocol
Server processes request and fills in response and transmits back to client
Client processes the response and updates application state

"""
__version__ = "0.1"

from httplib import HTTPConnection
import terms as v

class HypermediaHttpRequest():
    
    def __init__(self, host, port):
        self._host = host
        self._port = port
    
    def send(self, requestMap, host = None, port = None):
        if host:
            self._host = host
        if port:
            self._port = port    
            
        self._requestMap = requestMap
        
        self._method = requestMap[v.method]
        
        self._url = ""
        for pathElement in requestMap[v.uriPath] :
            self._url += pathElement

        if v.uriQuery in requestMap and 0 < len(requestMap[v.uriQuery]) :
            self._queryString = "?"
            for queryElement in requestMap[v.uriQuery] :
                self._queryString += ( "&" + queryElement + "=" + queryElement[self._requestMap[v.uriQuery][queryElement]] )
            self._url += self._queryString
                
        self._payload = None    
        if v.payload in requestMap:
            self._payload = requestMap[v.payload]
        
        requestMap[v.options] = {}
        requestMap[v.options][v.contentFormat] = requestMap[v.contentFormat]
        
        self._headers = {}
        for option in requestMap[v.options]:
            if v.contentFormat == option:
                self._headers["Content-Type"] = requestMap[v.options][v.contentFormat]
            else:
                self._headers[option] = requestMap[option]
        
        self._connection = HTTPConnection(self._host, self._port)
        print "connection: ", self._host, self._port
        self._connection.request(self._method, self._url, self._payload, self._headers)
        
    def getResponse(self):
        self._response = self._connection.getresponse()
        self._responseHeaders = self._response.getheaders()
        for header in self._responseHeaders:
            (key, value) = header
            self._requestMap[v.options][key] = value
        self._requestMap[v.response] = {}
        self._requestMap[v.response][v.code] = self._response.status
        self._requestMap[v.response][v.reason] = self._response.reason
        self._requestMap[v.response][v.status] = v.toStatus[self._response.status]
        self._requestMap[v.response][v.payload] = self._response.read()


def selfTest():
    """
    """
        
    host = "localhost"
    port = 8000
    
    requestMap = {v.uriPath:["/"], v.method:v.get, v.contentFormat:v.senmlType }
    request = HypermediaHttpRequest(host,port)
    request.send(requestMap)
    request.getResponse()
    print requestMap[v.response][v.payload]

if __name__ == '__main__':
    selfTest()
    
    
    
    
    