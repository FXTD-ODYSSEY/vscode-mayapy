class Issue(object):
    """
    Class representing an issue that contains 
    - a description (a short string explaining what's the issue)
    - a type, mostly used for UI purpose (icon for the issue will be RS_<type>.png)
    - a callback to resolve the issue (assisted resolve).
    """
    
    
    
    def __eq__(self, o):
        pass
    
    
    def __hash__(self):
        pass
    
    
    def __init__(self, description, type="'warning'", resolveCallback='None'):
        pass
    
    
    def __str__(self):
        pass
    
    
    def resolve(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    description = None
    
    type = None



