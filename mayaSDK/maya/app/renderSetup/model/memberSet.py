import exceptions

class MemberSet(object):
    """
    Class for creating a set of layer members that will handle explicit 
    inclusion and exclusion of dag paths.
    """
    
    
    
    def __init__(self, paths='()'):
        pass
    
    
    def exclude(self, path):
        pass
    
    
    def include(self, path):
        pass
    
    
    def paths(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class AlreadyHasStatus(exceptions.Exception):
    __weakref__ = None


class Node(object):
    """
    Node in the MemberSet structure. This should only be used by the MemberSet.
    MemberSet should be the only instance to ever create a node.
    """
    
    
    
    def __contains__(self, child):
        pass
    
    
    def __eq__(self, other):
        pass
    
    
    def __hash__(self):
        pass
    
    
    def __init__(self, path="'<OpenMaya.MDagPath object>'", status='0'):
        pass
    
    
    def add(self, child):
        pass
    
    
    def get(self, child):
        """
        # children accessors, mutators, queries
        """
    
        pass
    
    
    def remove(self, child):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



NEUTRAL = 0

INCLUDE = 1

EXCLUDE = -1


