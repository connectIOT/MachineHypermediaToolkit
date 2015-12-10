"""
HypermediaHttpServer extends the BaseHttpRequestHandler class in BaseHttpServer to create a dictionary driven interface
to http requesters and response handlers that allows the processing of requests in the order of path, content format, and method.

Requests and their associated responses are exposed in a dictionary interface for processing by proxies and resources
in a linked structure by passing references to the request and the associated response to resources at selected link
targets.

The server invokes a request handler callback when requests are received, and passes a reference to a structure
containing request and response elements used in processing the hypermedia.

REQUEST
URI
(query) parameters
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

{
    "uri": "/", 
    "contentFormat": "application/link-format+json",
    "options": null
    "method": "GET",
    "payload": null,
    "response": {
        "status": "Success",
        "code": "204",
        "reason": "No Content",
        "contentFormat": "application/link-format+json",
        "payload": "[{"href":null,"rel":"self","rt":"index"}]"
        }
}
    
Client fills request form and sends to server using selected protocol
Server processes request and fills in response and transmits back to client
Client processes the response and updates application state

"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import socket, sys

import terms as v

class HypermediaHTTPServer(HTTPServer):
    pass

class HypermediaHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def __init__(self, appRequestHandler, *args, **kwargs):
        self.handleRequest = appRequestHandler
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)
        
    def handle_one_request(self):
        """Handle a single HTTP request. Invokes self.handleRequest with the currentRequest object.
        """
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(414)
                return
            if not self.raw_requestline:
                self.close_connection = 1
                return
            if not self.parse_request():
                # An error code has been sent, just exit
                return
            self.mapRequest() #map and call handler
            self.wfile.flush() #actually send the response if not already done.
        except socket.timeout, e:
            #a read or a write timed out.  Discard this connection
            self.log_error("Request timed out: %r", e)
            self.close_connection = 1
            return
    
    def mapRequest(self):
        """fill out currentRequest map and call handleRequest()"""
        self.currentRequest = {}

        self.currentRequest[v.uriPath] = ["/"]
        for self.pathElement in self.path.split("?")[0].split("/"):
            if len(self.pathElement) >0:
                    self.currentRequest[v.uriPath].append(self.pathElement)
            
        self.currentRequest[v.uriQuery] = {}
        for self.queryElement in self.path.split("?")[1].split("&"):
            if self.queryElement.find("=") >0:
                (self.k, self.v) = self.queryElement.split("=")
                self.currentRequest[v.uriQuery][self.k] = self.v
            else: 
                self.currentRequest[v.uriQuery][self.queryElement] = ""
        
        """self.currentRequest[v.options] = {}
        for option in self.headers :
            self.currentRequest[v.options][option] = self.headers[option]
        """
        
        if self.command == v.get and "Accept" in self.headers: 
            self.currentRequest[v.contentFormat] = self.headers['Accept']
        elif "Content-Type" in self.headers:
            self.currentRequest[v.contentFormat] = self.headers['Content-Type']
        self.currentRequest[v.method] = self.command
        
        """check payload length and copy if there is a nonzero payload"""
        self.contentLength = 0
        if "Content-Length" in self.headers:
            self.contentLength = int(self.headers['Content-Length'])
            self.currentRequest[v.contentLength] = self.contentLength
            if (self.contentLength > 0): 
                self.payload = self.rfile.read(self.contentLength)
                self.currentRequest[v.payload] = self.payload
                
        """set up response map"""
        self.currentRequest[v.response] = {v.status:v.ServerError}
        
        """call hypermedia application handler"""
        self.handleRequest(self.currentRequest)
        
        """process response and headers"""
        self.send_response( v.toCode[ self.currentRequest[v.response][v.status] ] )
        self.contentLength = 0
        if v.payload in self.currentRequest[v.response]:
            self.contentLength = self.currentRequest[v.response][v.payload].len()
            self.payload = self.currentRequest[v.response][v.payload]
            self.send_header("Content-Length", str(self.contentLength))
            self.send_header("Content-Type", self.currentRequest[v.response][v.contentFormat])
        self.end_headers()
        
        """if there is a payload, send it"""
        if self.contentLength > 0:
            self.payload = self.currentRequest[v.response][v.payload]
            self.wfile.write("%s", self.payload)
        return
    
class TestAppHandler :
    def processRequest(self, currentRequest):
        self.currentRequest = currentRequest
        self.currentRequest[v.response][v.status] = v.NotFound
        print "\r\nRequest:\r\n"
        print self.currentRequest
        print "\r\n"
        return
    
def test(HandlerClass = HypermediaHTTPRequestHandler,
         ServerClass = HypermediaHTTPServer, protocol="HTTP/1.0"):
    """Test the HypermediaHTTP request handler class.

    This runs an HTTP server on port 8000 (or the first command line
    argument).

    """
    from functools import partial
        
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('', port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass( server_address, partial(HandlerClass, TestAppHandler().processRequest) )

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == '__main__':
    test()
    
    
    
    
    