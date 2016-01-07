"""
ResourceConstructor takes a base schema and model and constructs a Resource Model 

The base Schema classes are built by specialized classes in this module, and they 
are configured from the domain schema and domain model.

The domain schema describes all of the possible constructions and the domain model 
constrains the construction to the configured resources

The resulting resource model is used as a constructor to the class ResourceModel,
which can create resources on a server.

The generated resource types (rt) are used to select handlers for binding to the
resource instances on the server, and used in the client to bind Interaction Model 
classes to resource nodes in the TOM

"""

class ResourceModelConstructor:
    pass

class ResourceNodeConstructor:
    pass

class Index:
    pass

class Capability:
    pass

class Thing:
    pass

class Event:
    pass

class Action:
    pass

class Property:
    pass

class Subscription:
    pass

class Actuation:
    pass

class Notification:
    pass
