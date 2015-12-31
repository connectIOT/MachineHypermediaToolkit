""" ThingObjectModel extends the ApplicationModel class to construct a dynamic
    data structure analogous to the document object model (DOM) of a web browser.
    ThingObjectModel provides a dictionary interface for interaction between
    application scripts and resources linked into the Thing Object Model
    
    Discovery uses an Application Model to filter resource catalogs and indices
    according to the application requirements and creates or populates an 
    instance of a TOM with a Resource Model containing references to the 
    selected resources.
    
    The TOM may also provide a resource state caching layer to enable scripts 
    to reuse resource state without having to reissue GET instructions to the 
    server each time.
    
    Application scripts and higher level interaction models use resource paths 
    and semantic queries using the Link.selectMap interface to select resource 
    links and values for interaction.
    
    A set of proxy methods with optional max-age caching may be provided for
    scripts to use to indirectly interact with selected resources through the 
    TOM.
    
    The TOM may be extended with the WoT interaction model abstraction of
    Events, Actions, and Properties + Model Driven Discovery
    
    Methods may be provided to handle properties and forms, allowing the
    higher layer interaction model abstractions to be built on underlying
    HATEOAS state machines
    
"""

from ApplicationModel import ApplicationModel

class ThingObjectModel(ApplicationModel):
    pass