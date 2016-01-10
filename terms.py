""" CCML Commom CRUD Interface mapping """
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

toStatus = {
          200: Success,
          201: Created,
          202: Success,
          204: Success,
          400: BadRequest,
          401: Unauthorized,
          403: Forbidden,
          404: NotFound,
          405: MethodNotAllowed,
          406: NotAcceptable,
          409: Conflict,
          412: PrecondFailed,
          415: UnsupportedType,
          500: ServerError
          }
""" Hypermedia Semantic layer definitions """
""" terms in link-format representations """
_href = "href"
_anchor = "anchor"
_rel = "rel"
_self = "self"
_sub = "sub"
_grp ="grp"
_boundTo = "boundTo"
_handledBy ="handledBy"
_item = "item"
_rt = "rt"
_ct = "ct"
_if = "if"
_sz = "sz"
_null = ""

""" terms in senml or hsml and extensions """
_e = "e" #entities
_l = "l" #links
_bn = "bn" #base name (base uri)
_n = "n" #name (uri)
_u = "u" #units
_v = "v" #numeric value
_bv = "bv" #boolean value
_sv = "sv" #string value
_ov = "ov" #object value
_ev = "ev" #element value
_fv = "fv" #form value

""" terms to be used in forms """
_action = "action"
_method = "method"
_params = "params"
_template = "template"
_returns = "returns"

"""Interaction model terms used in resource type (rt) attribute values"""
_index = "index"
_thing = "thing"
_capability = "capability"
_event = "event"
_action = "action"
_property = "property"
_actuation = "actuation"
_subscription = "subscription"
_notification = "notification"

""" content-formats """
plainTextType = "text/plain"
linkFormatJsonType = "application/link-format+json"
linkFormatType = linkFormatJsonType
senmlJsonType = "application/senml+json"
senmlType = senmlJsonType
senmlCollectionType = "application/collection+senml+json"
linkFormatMergeType = "application/merge-patch+json"
senmlFormType = "application/forms+senml+json"

""" hyper-senml content formats and extensions """
hsmlType = "application/hsml+json"
hsmlLinkType = "application/link-format+hsml+json"
hsmlCollectionType = "application/collection+hsml+json"
hsmlFormsType = "application/forms+hsml+json"

""" Terms for schemas and models """
_rdfResource = "rdfs:resource"
_rdfClass = "rdf:Class"
_rdfProperty = "rdf:Property"
_subClassOf = "rdfs:subClassOf"
_range = "rdfs:range"
_domain = "rdfs:domain"
_rdfType = "rdf:type"
_description = "rdfs:comment"
_comment = "rdfs:comment"
_label = "rdfs:label"

_value = "value"

_ts = "ts"
_mayHave = "ts:mayHave"
_usedBy = "ts:usedBy"
_schema = "schema"
_context = "@context"

_decimalType = "xs:decimal"
_floatType = "xs:float"
_integerType = "xs:integer"
_stringType = "xs:string"
_booleanType = "xs:boolean"
_dateTimeType = "xs:dateTime"

