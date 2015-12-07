
"""terms for methods"""
get = "GET"
put = "PUT"
post = "POST"
delete = "DELETE"
patch = "PATCH"

"""terms for request mapping"""
uri = "uri"
params = "params"
method = "method"
contentFormat = "contentFormat"
contentLength = "contentLength"
options = "options"
payload = "payload"
response = "response"
status = "status"
code = "code"
reason = "reason"

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

