"""
This module provides the collection class, as well as utility
functions to operate on collections.

The collection owns its associated selector node: on collection
delete, the collection is deleted as well.

Conceptually, a collection fulfills four roles in render setup:

1) It is a container of overrides.  If enabled, the collection will
   apply all its enabled overrides on nodes it selects (see (2)).
2) It selects nodes onto which overrides will be applied.  These nodes
   can be DAG or DG nodes.
3) It is a container of child collections.  Child collections always
   select nodes based on their parent's selected nodes (see (2)).
4) It defines render layer membership.  Members of a render layer can
   only be DAG nodes.  These are always a subset of the nodes selected
   by the collection (see (2)).  The members of the render layer are the
   union of the top-level collection members; children collections can
   exclude or re-include members.  See RenderLayer.getMembers for more
   details (including the effect of isolate select mode).

The application of overrides only obeys enabled / disabled status.

Render layer membership is determined from enabled / disabled, in
conjunction with isolate select.
"""

from . import nodeList
from . import childNode

class Collection(nodeList.ListBase, childNode.TreeOrderedItem, childNode.ChildNode):
    """
    Collection node.
    
    A collection has an ordered list of children, and a selector to
    determine nodes to which the children apply.
    
    MAYA-59277: 
      - When we start implementing proper hierarchical collections we 
        need to decide on the relationship between parent and child
        selectors. Do we always consider a parent collection to be the 
        union of its child collections, and propagate the selector 
        information upwards when a child collection is added or changed?
        Or do we go the opposite direction and restrict the child collection
        to use the intersection between its selector and its parent's selector?
    
      - Light child collections always have a single light source member.
        We should utilize this and create a specific selector for such
        use cases for better performance.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def acceptImport(self):
        pass
    
    
    def activate(self):
        """
        Called when this list item is inserted into the list.
        Override this method to do any scene specific initialization.
        """
    
        pass
    
    
    def ancestorCollections(self):
        """
        Return this collection's ancestors.
        
        Neither the collection itself, nor the render layer, are included
        in the ancestors.  Therefore, a top-level collection has no
        ancestors.
        """
    
        pass
    
    
    def appendChild(*args, **kwargs):
        pass
    
    
    def apply(*args, **kwargs):
        pass
    
    
    def attachChild(*args, **kwargs):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def createAbsoluteOverride(*args, **kwargs):
        pass
    
    
    def createCollection(self, collectionName):
        """
        Add a child collection to the Collection.
        """
    
        pass
    
    
    def createConnectionOverride(*args, **kwargs):
        pass
    
    
    def createOverride(*args, **kwargs):
        pass
    
    
    def createRelativeOverride(*args, **kwargs):
        pass
    
    
    def deactivate(self):
        """
        Called when this list item is removed from the list.
        Override this method to do any scene specific teardown.
        """
    
        pass
    
    
    def detachChild(*args, **kwargs):
        pass
    
    
    def enabledChanged(self):
        pass
    
    
    def findChild(self, predicate, creator='None'):
        """
        Find the child of this collection satisfying the predicate function or creates it
        with the creator function if not found and a creator function is specified.
        Function signatures are:
          predicate(childNode): returns boolean.
          creator(void) : returns the created node.
        """
    
        pass
    
    
    def getChild(self, childName, cls='"<class \'maya.app.renderSetup.model.childNode.ChildNode\'>"'):
        """
        Look for an existing child by name and optionally class.
        
        @type childName: string
        @param childName: Name of child to look for
        @type cls: class name
        @param cls: Class name for the type of class to look for
        @rtype: Child model instance
        @return: Found instance or throw an exception
        """
    
        pass
    
    
    def getChildren(self, cls='"<class \'maya.app.renderSetup.model.childNode.ChildNode\'>"'):
        """
        Get the list of all children. 
        Optionally only the children matching the given class.
        """
    
        pass
    
    
    def getCollectionByName(self, collectionName, nested='False'):
        pass
    
    
    def getCollections(self):
        pass
    
    
    def getLayerNumIsolatedChildren(self):
        pass
    
    
    def getNumIsolatedAncestors(self):
        pass
    
    
    def getNumIsolatedChildren(self, includeSelf='False'):
        pass
    
    
    def getOverrides(self):
        pass
    
    
    def getRenderLayer(self):
        pass
    
    
    def getSelector(self):
        """
        Return the selector user node for this collection.
        """
    
        pass
    
    
    def getSelectorType(self):
        pass
    
    
    def hasChildren(self):
        pass
    
    
    def hasIsolatedAncestors(self, dataBlock='None'):
        pass
    
    
    def hasIsolatedChildren(self, dataBlock='None'):
        pass
    
    
    def isAbstractClass(self):
        pass
    
    
    def isAcceptableChild(self, modelOrData):
        """
        Check if the model could be a child
        """
    
        pass
    
    
    def isEnabled(self, dataBlock='None'):
        pass
    
    
    def isIsolateSelected(self, dataBlock='None'):
        """
        Get if isolate selected. Will always return False in batch mode
        """
    
        pass
    
    
    def isSelfAcceptableChild(self):
        """
        Overridden instances that return False, prevent copy/paste of the collection type to itself.
        """
    
        pass
    
    
    def isSelfEnabled(self, dataBlock='None'):
        pass
    
    
    def isTopLevel(self):
        """
        Is the collection's parent a render layer?
        """
    
        pass
    
    
    def isolateSelectedChanged(self):
        pass
    
    
    def postApply(*args, **kwargs):
        pass
    
    
    def postConstructor(self):
        pass
    
    
    def pullEnabled(*args, **kwargs):
        pass
    
    
    def setIsolateSelected(self, val):
        pass
    
    
    def setSelectorType(self, typeName):
        """
        Sets the selector type of this collection.
        """
    
        pass
    
    
    def setSelfEnabled(self, value):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def unapply(*args, **kwargs):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    aSelector = None
    
    
    childHighest = None
    
    
    childLowest = None
    
    
    children = None
    
    
    enabled = None
    
    
    isolateSelected = None
    
    
    kDefaultSelectorTypeName = 'simpleSelector'
    
    
    kTypeId = None
    
    
    kTypeName = 'collection'
    
    
    layerNumIsolatedChildren = None
    
    
    numIsolatedAncestors = None
    
    
    numIsolatedChildren = None
    
    
    parentEnabled = None
    
    
    selfEnabled = None


class RenderSettingsChildCollection(Collection):
    """
    Render Settings Sub Collection node.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def appendChild(self, child):
        pass
    
    
    def attachChild(self, pos, child):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def createCollection(self, collectionName):
        """
        Add a child collection to the Collection.
        """
    
        pass
    
    
    def getRenderSettingsChildCollectionByName(self, renderSettingsChildCollectionName, nested='False'):
        pass
    
    
    def getRenderSettingsChildCollections(self):
        pass
    
    
    def isAcceptableChild(self, modelOrData):
        """
        Check if the argument can be a child of this collection.
        """
    
        pass
    
    
    def setSelectorType(self, typeName):
        pass
    
    
    def superTypeName(self):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def containsNodeName(nodeName):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kSelectorTypeName = 'simpleSelector'
    
    
    kTypeId = None
    
    
    kTypeName = 'renderSettingsChildCollection'


class RenderSettingsCollection(Collection):
    """
    Render Settings Collection node.
    
    This collection has an ordered list of children, and a static & const selector
    to determine nodes to which the children apply. The list of nodes is based
    on the selected renderer at the time of creation.
    
    MAYA-66757:
    - A base collection will be needed to factorize commonalities and segregate differences.
    - A static selector is needed which could be the existing static selection or an object set.
    - The name is read-only.
    - The selector content is read-only
    - The render name should be part of the collection so that the settings are clearly linked 
      to the used renderer, or linked using a plug
    """
    
    
    
    def __init__(self):
        pass
    
    
    def appendChild(self, child):
        pass
    
    
    def attachChild(self, pos, child):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def createCollection(self, collectionName):
        """
        Add a child collection to the Collection.
        """
    
        pass
    
    
    def isAcceptableChild(self, modelOrData):
        """
        Check if the argument can be a child of this collection.
        """
    
        pass
    
    
    def setSelectorType(self, typeName):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def containsNodeName(nodeName):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kSelectorTypeName = 'simpleSelector'
    
    
    kTypeId = None
    
    
    kTypeName = 'renderSettingsCollection'
    
    
    numIsolatedRenderSettingsChildren = None


class LightsChildCollection(Collection):
    """
    LightsChildCollection node.
    
    A child collection node specific for one single light source
    and overrides on this light source.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def isAcceptableChild(self, modelOrData):
        """
        Check if the argument can be a child of this collection.
        
        Pasting is prevented because the Light Editor considers only the 
        first override in the LightsChildCollection. Additionally dragging 
        is prevented between overrides in LightsChildCollections to prevent 
        dragging between incompatible LightsChildCollection types 
        (ie. point light, spot light)
        """
    
        pass
    
    
    def setSelectorType(self, typeName):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'lightsChildCollection'


class LightsCollection(Collection):
    """
    LightsCollection node.
    
    A collection node specific for grouping light sources
    and overrides on those light sources.
    
    This collection should have all light sources as member by default. All nodes 
    matching the light classification should be returned by the selector
    on this collection.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def createCollection(self, collectionName):
        """
        Add a lights child collection to the Collection.
        """
    
        pass
    
    
    def isAcceptableChild(self, modelOrData):
        """
        Check if the argument can be a child of this collection.
        
        We want to prevent copying LightsChildCollections in the same 
        LightsCollection at the expense of not being able to copy 
        LightsChildCollections between different LightsCollections.
        """
    
        pass
    
    
    def setSelectorType(self, typeName):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def containsNodeName(nodeName):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'lightsCollection'


class AOVChildCollection(Collection):
    """
    AOV (arbitrary output variable) Child Collection node.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def containsNodeName(self, nodeName):
        pass
    
    
    def isSelfAcceptableChild(self):
        """
        This code prevents copy/paste of AOV child collections to themselves/other AOV child collections.
        """
    
        pass
    
    
    def setSelectorType(self, typeName):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'aovChildCollection'


class AOVCollection(Collection):
    """
    AOV (arbitrary output variable) parent collection node.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def appendChild(self, child):
        pass
    
    
    def attachChild(self, pos, child):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def isAcceptableChild(self, modelOrData):
        """
        Check if the model could be a child
        """
    
        pass
    
    
    def setSelectorType(self, typeName):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def containsNodeName(nodeName):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'aovCollection'



def unapply(*args, **kwargs):
    pass


def collections(c):
    pass


def getAllCollectionClasses():
    """
    Returns the list of Collection subclasses
    """

    pass


def create(*args, **kwargs):
    pass


def delete(*args, **kwargs):
    pass



kChildDetached = []

kOverrideCreationFailed = []

kIncorrectChildType = []

_specialCollectionTypes = set()

kCollectionMissingSelector = []

kUnknownChild = []

kInvalidChildName = []

kChildAttached = []

kSet = []

_overrideTypes = set()

kRendererMismatch = []


