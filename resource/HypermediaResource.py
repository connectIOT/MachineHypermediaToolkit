

import terms as v

class HypermediaResource(object) :
    
    def __init__(self):
        self._contentFormats = {}
        self.linkArray = Links({v._href: "", v._rel: [v._self], v._rt: ["resource"]})
        
    def registerContentHandler(self, contentFormat, handler):
        self._contentFormats[contentFormat] = handler
    
class Links(object):
    
    def __init__(self, links=None):
        """initialize with a set of links default to none"""
        self._links = []
        self._links.append(links)
        
    def add(self, links):
        """links contains a map or array of maps in link-format"""
        self._links.append(links)
    
    def select(self, selectMap):
        """selectMap contains a selection map in query filter format"""
        """returns a list of links that match the query filter"""
        pass

    def patch(self, selectMap, mergeMap):
        """patch contains a selection map and merge map in JSON merge-patch format"""
        pass
    
class LinkFormatHandler:
    pass

class LinkFormatPatchHandler:
    pass

class PlainTextHandler:
    pass

class SemmlValueHandler:
    pass