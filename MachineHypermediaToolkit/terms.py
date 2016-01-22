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
_form = "form"
_rt = "rt"
_ct = "ct"
_if = "if"
_sz = "sz"
_null = ""

""" terms in senml or hsml and extensions """
_e = "e" #entities
_l = "l" #links
_f = "f" #forms
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
_resource = "resource"
_class = "class"
_property = "property"
_subClassOf = "subClassOf"
_range = "range"
_domain = "domain"
_type = "type"
_description = "comment"
_comment = "comment"
_label = "label"
_name = "name"
_resource = "resource"
_value = "value"
_links = "links"

_mayHave = "mayHave"
_usedBy = "usedBy"
_schema = "schema"
_context = "@context"

_decimalType = "decimal"
_floatType = "float"
_integerType = "integer"
_stringType = "string"
_booleanType = "boolean"
_dateTimeType = "dateTime"


BaseContext = """
  {
    "type": "@type",
    "id": "@id",
    "cat": "http://www.w3.org/ns/dcat#",
    "qb": "http://purl.org/linked-data/cube#",
    "grddl": "http://www.w3.org/2003/g/data-view#",
    "ma": "http://www.w3.org/ns/ma-ont#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfa": "http://www.w3.org/ns/rdfa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rif": "http://www.w3.org/2007/rif#",
    "rr": "http://www.w3.org/ns/r2rml#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "skosxl": "http://www.w3.org/2008/05/skos-xl#",
    "wdr": "http://www.w3.org/2007/05/powder#",
    "void": "http://rdfs.org/ns/void#",
    "wdrs": "http://www.w3.org/2007/05/powder-s#",
    "xhv": "http://www.w3.org/1999/xhtml/vocab#",
    "xml": "http://www.w3.org/XML/1998/namespace",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "prov": "http://www.w3.org/ns/prov#",
    "sd": "http://www.w3.org/ns/sparql-service-description#",
    "org": "http://www.w3.org/ns/org#",
    "gldp": "http://www.w3.org/ns/people#",
    "cnt": "http://www.w3.org/2008/content#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "earl": "http://www.w3.org/ns/earl#",
    "ht": "http://www.w3.org/2006/http#",
    "ptr": "http://www.w3.org/2009/pointers#",
    "cc": "http://creativecommons.org/ns#",
    "ctag": "http://commontag.org/ns#",
    "dc": "http://purl.org/dc/terms/",
    "dc11": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "gr": "http://purl.org/goodrelations/v1#",
    "ical": "http://www.w3.org/2002/12/cal/icaltzd#",
    "og": "http://ogp.me/ns#",
    "rev": "http://purl.org/stuff/rev#",
    "sioc": "http://rdfs.org/sioc/ns#",
    "v": "http://rdf.data-vocabulary.org/#",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "schema": "http://schema.org/",
    "describedby": "http://www.w3.org/2007/05/powder-s#describedby",
    "license": "http://www.w3.org/1999/xhtml/vocab#license",
    "role": "http://www.w3.org/1999/xhtml/vocab#role",
    "ts": "http://thingschema.org/schema#",
    "@vocab": "http://thingschema.org/",
    "type": "rdf:type",
    "property": "rdf:Property",
    "class": "rdfs:Class",
    "comment": "rdfs:comment",
    "subClassOf": "rdfs:subClassOf",
    "label": "rdfs:label",
    "resource": "rdfs:Resource",
    "range": "rdfs:range",
    "domain": "rdfs:domain",
    "mayHave": "ts:mayHave",
    "usedBy": "ts:usedBy",
    "decimal" = "xs:decimal",
    "float" = "xs:float",
    "integer" = "xs:integer",
    "string" = "xs:string",
    "boolean" = "xs:boolean",
    "dateTime" = "xs:dateTime"
  }
"""