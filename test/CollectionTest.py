from HypermediaHttpServer import HypermediaHTTPServer, HypermediaHTTPRequestHandler
from HypermediaCollection import HypermediaCollection
import sys

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
    resourceBase = HypermediaCollection()
    httpd = ServerClass(server_address, \
                partial(HandlerClass, resourceBase.routeRequest))

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == '__main__':
    test()
    
