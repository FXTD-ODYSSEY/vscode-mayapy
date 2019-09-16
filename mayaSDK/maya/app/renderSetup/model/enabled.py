"""
Render setup overrides and collections can be enabled and disabled.

Disabling an override removes its effect, but keeps the override itself.

Disabling a collection disables all the overrides in its list, as well
as disabling any child (nested) collection it may have.

To implement this behavior, overrides and collections have three
attributes:

1) An enabled attribute.  This attribute is readable only (output), and
   is (trivially) computed from the two following attributes.
2) A self enabled attribute.  This writable attribute determines whether
   the override or collection itself is enabled.
3) A parent enabled attribute.  This writable attribute is connected to
   its parent's enabled output attribute, unless it is a collection
   immediately under a render layer.

The enabled output boolean value is the logical and of the self enabled
attribute and the parent enabled attribute.
"""

def isPulling():
    pass


def createIntAttribute(longName, shortName, defaultValue):
    """
    Helper method to create an input (writable) int attribute
    """

    pass


def compute(node, plug, dataBlock):
    """
    Computes the enabled plug with the basic conditions (selfEnabled and parentEnabled).
    Do not use if 'enabled' depends on other attributes.
    """

    pass


def initializeAttributes(cls):
    pass


def addChangeCallbacks(node):
    """
    Add callbacks to indicate the argument node's enabled attribute changed.
    
    A list of callback IDs is returned.
    """

    pass


def setPulling(value):
    pass


def createHiddenIntAttribute(longName, shortName):
    """
    Helper method to create a hidden, readable, non-keyable, and
    writable integer attribute.
    """

    pass


def setEnabledOutput(node, dataBlock, value):
    pass


def createBoolOutputAttribute(longName, shortName, defaultValue):
    """
    Helper method to create an output (readable) boolean attribute
    """

    pass


def createBoolAttribute(longName, shortName, defaultValue):
    """
    Helper method to create an input (writable) boolean attribute
    """

    pass


def computeParentEnabled(node, dataBlock):
    """
    Compute the parent enabled input while avoiding DG cycle check warnings.
    """

    pass


def createNumIsolatedChildrenAttribute():
    """
    Helper method to create the number of isolated children attribute.
    
    This renderLayer and collection attribute is a count of the number
    of isolate selected children in the subtree of the render layer
    or collection.
    """

    pass


def computeEnabled(node, dataBlock):
    """
    Returns the enabled state based on the basic conditions (selfEnabled and parentEnabled).
    """

    pass



_pulling = False


