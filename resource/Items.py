import terms as v

class SenmlItems(object):
    def __init__(self, items=None):
        self._items = []
        if None != items:
            self.add(items)
        
    def add(self, items=[]):
        if isinstance(items, list) :
            self._items.extend(items)   
        else :
            self._items.append(items)   
        
    def remove(self, items=[]):
        for removeName in items:
            for item in self._items:
                if removeName == item[v._n]:
                    self._items.remove(item)
    
    def getItemByName(self, itemName):
        for item in self._items:
            if itemName == item[v._n]:
                return item
        else:
            return None
    
    def updateItemByName(self, itemName, updateItem):
        for item in self._items:
            if item[v._n] == itemName:
                updateItem[v._n] = itemName
                item = updateItem
                return item
        else:
            return False
        
    def getValueByName(self, itemName):
        for item in self._items:
            if itemName == item[v._n]:
                if v._v in item:
                    return item[v._v]
                elif v._bv in item:
                    return item[v._bv]
                elif v._sv in item:
                    return item[v._sv]
                elif v._ev in item:
                    return item[v._ev]
                else:
                    return None
        
    def updateValueByName(self, itemName, itemValue):
        for item in self._items:
            if itemName == item[v._n]:
                if v._v in item:
                    item[v._v] = itemValue
                elif v._bv in item:
                    item[v._bv] = itemValue
                elif v._sv in item:
                    item[v._sv] = itemValue
                elif v._ev in item:
                    item[v._ev] = itemValue
                else:
                    return False
                return True
        else:
            return False
        