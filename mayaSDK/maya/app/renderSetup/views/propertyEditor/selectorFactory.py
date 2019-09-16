"""
Each collection object has a selector that is responsible for determining
objects that:

o are members of the render layer, and
o will be overridden.

The property editor supports different UIs for different selector
types.  The property editor selector factory provides an extensible
mechanism to create the UI for various selector types.

To create a property editor UI for a selector class, a creator callable
is registered on the data model selector class type.  On creation, the
creator callable is given the data model selector object.

The return value of the creator is a builder object for the selector
property UI.  This object must have a build() method, whose argument is
the property editor UI layout for the selector.

The selector factory is a singleton.
"""

def entry(typeName):
    """
    Return the creator for the argument selector data model type.
    """

    pass


def unregister(typeName):
    """
    Unregister a property editor UI creator for selector data model type.
    
    Raises a KeyError if a creator had not already been registered.
    """

    pass


def create(selector):
    """
    Create a property editor UI for selector.
    
    The argument is the data model selector object
    
    The return object is the selector property UI builder.
    
    Raises a KeyError if a creator had not already been registered.
    """

    pass


def register(typeName, creator):
    """
    Register a property editor UI creator for selector data model type.
    
    Raises a RuntimeError if a creator had already been registered.
    """

    pass


def selectorTypes():
    pass



kAlreadyRegistered = []

_creators = {}


