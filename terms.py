
"""terms for methods"""
get = "GET"
put = "PUT"
post = "POST"
delete = "DELETE"
patch = "PATCH"

"""terms for request mapping"""
uri = "uri"
uriPath = "uriPath"
uriQuery = "uriQuery"
params = "params"
method = "method"
accept = "accept"
contentFormat = "contentFormat"
contentLength = "contentLength"
options = "options"
payload = "payload"
response = "response"
status = "status"
code = "code"
reason = "reason"
location = "location"

"""terms used in response status abstraction"""
Success = "Success"       
Created = "Created"         
BadRequest = "BadRequest"
Unauthorized = "Unauthorized"
Forbidden = "Forbidden"
NotFound = "NotFound"
MethodNotAllowed = "MethodNotAllowed"
NotAcceptable = "NotAcceptable"
Conflict = "Conflict"
PrecondFailed = "PrecondFailed"
UnsupportedType = "UnsupportedType"
ServerError = "ServerError"

"""Mapping of abstract status to http codes"""
toCode = {
          Success: 200,
          Created: 201,
          BadRequest: 400,
          Unauthorized: 401,
          Forbidden: 403,
          NotFound: 404,
          MethodNotAllowed: 405,
          NotAcceptable: 406,
          Conflict: 409,
          PrecondFailed: 412,
          UnsupportedType: 415,
          ServerError: 500
          }

"""terms in link-format representations"""
_href = "href"
_anchor = "anchor"
_rel = "rel",
_self = "self"
_sub = "sub"
_item = "item"
_rt = "rt"
_ct = "ct"
_if = "if"
_sz = "sz"
_null = ""

"""terms in senml and extensions"""
_e = "e" #entities
_l = "l" #links
_bn = "bn" #base name (base uri)
_n = "n" #name (uri)
_u = "u" #units
_v = "v" #numeric value
_bv = "bv" #boolean value
_sv = "sv" #string value
_ov = "ov" #object value

plainTextType = "text/plain"
linkFormatJsonType = "application/link-format+json"
senmlType = "application/senml+json"
senmlCollectionType = "application/collection+senml+json"
linkFormatMergeType = "application/merge-patch+json"
linkFormatFormType = "application/forms+link-format+json"
