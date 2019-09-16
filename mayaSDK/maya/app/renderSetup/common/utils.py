import exceptions

class ReportableException(exceptions.Exception):
    def __init__(self, text):
        pass
    
    
    def __str__(self):
        pass
    
    
    __weakref__ = None
    
    text = None



def nameToNode(name):
    """
    Returns the MObject matching given name or None if not found.
    Raises RuntimeError if name is ambiguous.
    """

    pass


def nameToDagPath(name):
    """
    Returns the MDagPath matching given name or None if not found.
    Raises RuntimeError if name is ambiguous.
    """

    pass


def nameToPlug(name):
    """
    Returns the MPlug matching given name or None if not found.
    Raises RuntimeError if name is ambiguous.
    """

    pass


def isNodeInstance(node, nodeType):
    pass


def removeDuplicates(seq):
    """
    Removes all duplicated elements from a list.
    Note that order is not preserved.
    """

    pass


def _selectPlug(name):
    pass


def nodeToLongName(node):
    """
    Returns the full name of the node, 
    i.e. the absolute path for dag nodes and name for dependency (non-dag) nodes.
    """

    pass


def findPlug(node, attr):
    """
    Return the MPlug corresponding to attr on argument node or None if not found.
    The node argument can be an MObject or a node string name.
    The attr argument can be an MObject or a attr string name.
    Raises RuntimeError if plug is ambiguous.
    """

    pass


def nodeToShortName(node):
    """
    Returns the minimum name string necessary to uniquely identify the node.
    """

    pass


def getSubClasses(classType):
    pass



kNameToNodeTypeMismatch = []

kAmbiguousName = []


