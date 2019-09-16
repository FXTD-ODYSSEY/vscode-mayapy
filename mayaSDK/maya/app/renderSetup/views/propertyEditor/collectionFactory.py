"""
The property editor supports different UIs for different collection
types.  The property editor collection factory provides an extensible
mechanism to create the UI for various collection types.

To create a property editor UI for a collection class, a creator
callable is registered on the data model collection class type.
On creation, the creator callable is given a weak reference to the
corresponding proxy item, and the UI parent.  It must return an instance
of a class derived from MayaQWidgetBaseMixin and QGroupBox.

The collection factory is a singleton.
"""

def register(typeName, creator):
    """
    Register a property editor UI creator for collection type.
    
    Raises a RuntimeError if a creator had already been registered.
    """

    pass


def unregister(typeName):
    """
    Unregister a property editor UI creator for collection type.
    
    Raises a KeyError if a creator had not already been registered.
    """

    pass


def create(proxyItem, parent):
    """
    Create a property editor UI for collection type.
    
    Raises a KeyError if a creator had not already been registered.
    """

    pass



_creators = {}

kAlreadyRegistered = []


