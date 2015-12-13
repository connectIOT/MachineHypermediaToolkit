

import terms as v
from Links import Links

class HypermediaResource(object) :
    
    def __init__(self):
        self._contentFormats = {}
        self.linkArray = Links({v._href: "", v._rel: [v._self], v._rt: ["resource"]})
        
    def registerContentHandler(self, contentFormat, handler):
        self._contentFormats[contentFormat] = handler
        
        
class LinkFormatHandler:
    pass

class LinkFormatPatchHandler:
    pass

class PlainTextHandler:
    pass

class SemmlValueHandler:
    pass