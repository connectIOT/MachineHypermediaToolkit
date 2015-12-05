"""
HypermediaHttpServer extends the BaseHttpRequestHandler class in BaseHttpServer to create a dictionary driven interface
to http requests and responsed that allows the processing of requests in the order of path, content format, and method.

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
(header) options
payload

RESPONSE
response type (code)
content-format
(header) options
payload

It is expected that hypermedia handlers will process the URI and query parameters first in order to select a set of
resources for processing, then apply the content format and method along with any supplementary options to the
resources.

The terms used in the request and response elements are semantically aligned with the vocabularies used in links and
forms to describe hypermedia state exchanges, and are abstracted across different protocols like http and CoAP.

Common abstractions are needed to support multiple protocols. At least HTTP and CoAP are supported with the following
mapping binding.

URI
"""

from BaseHTTPServer import BaseHTTPRequestHandler


class HypermediaHTTPRequestHandler(BaseHTTPRequestHandler):


    pass

