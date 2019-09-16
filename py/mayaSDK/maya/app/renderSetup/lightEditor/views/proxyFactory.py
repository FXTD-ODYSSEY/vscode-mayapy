"""
This factory creates Qt proxy items from render setup data model nodes.
It provides an extensible mechanism to create Qt proxy items for various
render setup data model types.

To create a Qt proxy item for a data model class, a creator callable is
registered on the data model class type.  On creation, the creator
callable is given the data model node.  It must return an instance of a
class derived from ModelProxyItem.

The proxy factory is a singleton.
"""

def register(typeName, creator):
    """
    Register a Qt proxy item creator for data model type.
    
    Raises a RuntimeError if a creator had already been registered.
    """

    pass


def create(node):
    """
    Create a Qt proxy item for data model node.
    
    Raises a KeyError if a creator had not already been registered.
    """

    pass


def unregister(typeName):
    """
    Unregister a Qt proxy item creator for data model type.
    
    Raises a KeyError if a creator had not already been registered.
    """

    pass



kAlreadyRegistered = []

_creators = {}


