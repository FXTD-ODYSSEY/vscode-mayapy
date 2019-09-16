"""
This module provides the override base and concrete classes, as well as
utility functions to operate on overrides.
"""

from collections import namedtuple
from maya.app.renderSetup.model.renderSetupPrivate import PostApplyCmd

_Property = namedtuple('Property', ('name', 'encode', 'decode'))


class OverridePlugHandle(object):
    """
    Plug class that handles dynamic plug and missing dependencies.
    
    Has functions for finalization, encoding, decoding and handling missing dependencies.
    
    Finalization creates a dynamic attribute based on another plug. It has 3 available modes:
     - kModeClone clones the input plug
     - kModeMultiply will have the same arity as the input plug but has float scalar units
       (can be used to multiply input's plug type by a scalar)
     - kModeOffset clones the input plug but with more flexible min/max, softMin/softMax
       (can be used to offset input's plug type by some value in the same units)
       
    Encode/decode creates/read dictionary of attributes that defines the plug attributes.
    
    Handles missing dependency:
     If the plug is decoded and can't find the source plug it's supposed to connect to, then
     it has a missing dependency. It creates a dynamic string attribute containing the name of the
     missing dependency (this allows the "missing dependency" state to persist on file new) and it 
     starts listening to scene changes to find the missing dependency and connect to it if it's created.
    """
    
    
    
    def __init__(self, ovr, longName, shortName, mode='0'):
        pass
    
    
    def decode(self, dict):
        pass
    
    
    def encode(self, dict):
        pass
    
    
    def finalize(self, plg):
        pass
    
    
    def getMissingDependency(self):
        pass
    
    
    def getPlug(self):
        """
        Return the Plug object (plug.py). (this is not a MPlug)
        """
    
        pass
    
    
    def getSource(self):
        pass
    
    
    def hasMissingDependency(self):
        pass
    
    
    def isFinalized(self):
        pass
    
    
    def isValid(self):
        pass
    
    
    def name(self):
        pass
    
    
    def node(self):
        pass
    
    
    def setMissingDependency(self, source):
        pass
    
    
    def setSource(self, source):
        pass
    
    
    def update(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    attr = None
    
    attrDependency = None
    
    kModeClone = 0
    
    
    kModeMultiply = 2
    
    
    kModeOffset = 1


class _MPxCommand(object):
    """
    Base class for custom commands.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def doIt(*args, **kwargs):
        """
        Called by Maya to execute the command.
        """
    
        pass
    
    
    def hasSyntax(*args, **kwargs):
        """
        Called by Maya to determine if the command provides an MSyntax object describing its syntax.
        """
    
        pass
    
    
    def isUndoable(*args, **kwargs):
        """
        Called by Maya to determine if the command supports undo.
        """
    
        pass
    
    
    def redoIt(*args, **kwargs):
        """
        Called by Maya to redo a previously undone command.
        """
    
        pass
    
    
    def syntax(*args, **kwargs):
        """
        Returns the command's MSyntax object, if it has one.
        """
    
        pass
    
    
    def undoIt(*args, **kwargs):
        """
        Called by Maya to undo a previously executed command.
        """
    
        pass
    
    
    def appendToResult(*args, **kwargs):
        """
        Append a value to the result to be returned by the command.
        """
    
        pass
    
    
    def clearResult(*args, **kwargs):
        """
        Clears the command's result.
        """
    
        pass
    
    
    def currentResult(*args, **kwargs):
        """
        Returns the command's current result.
        """
    
        pass
    
    
    def currentResultType(*args, **kwargs):
        """
        Returns the type of the current result.
        """
    
        pass
    
    
    def displayError(*args, **kwargs):
        """
        Display an error message.
        """
    
        pass
    
    
    def displayInfo(*args, **kwargs):
        """
        Display an informational message.
        """
    
        pass
    
    
    def displayWarning(*args, **kwargs):
        """
        Display a warning message.
        """
    
        pass
    
    
    def isCurrentResultArray(*args, **kwargs):
        """
        Returns true if the command's current result is an array of values.
        """
    
        pass
    
    
    def setResult(*args, **kwargs):
        """
        Set the value of the result to be returned by the command.
        """
    
        pass
    
    
    commandString = None
    
    historyOn = None
    
    __new__ = None
    
    
    kDouble = 1
    
    
    kLong = 0
    
    
    kNoArg = 3
    
    
    kString = 2


class UniqueOverride(object):
    """
    Mixin class for override that applies to a unique node. This override 
    unconditionnaly applies to the node it was finalized on (if it exists).
    It doesn't care about the collection's content.
    """
    
    
    
    def finalize(*args, **kwargs):
        pass
    
    
    def setTargetNodeName(*args, **kwargs):
        pass
    
    
    def targetNodeName(self, dataBlock='None'):
        pass
    
    
    def addTargetAttribute(cls):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    kTargetNodeName = None


class LeafClass(object):
    """
    To be used by leaf classes only
    """
    
    
    
    def isAbstractClass(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


from . import childNode

class Override(childNode.TreeOrderedItem, childNode.ChildNode):
    """
    Override node base class.
    
    An override represents a non-destructive change to a scene property
    that can be reverted or disabled.  Render setup uses overrides to describe
    changes that apply in a single render layer, and are unapplied when
    switching to another render layer.  When working within a render layer, an
    override can be preserved but disabled, to remove its effect.
    
    The override node base class cannot be directly created in Maya.  It is
    derived from the ListItem base class, so that overrides can be inserted
    in a list.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def activate(self):
        pass
    
    
    def attrValuePlugName(self):
        pass
    
    
    def attributeName(self):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def deactivate(self):
        pass
    
    
    def enabledChanged(self):
        pass
    
    
    def getApplyOverrides(self):
        """
        Return the list of apply override nodes that correspond to this override.
        """
    
        pass
    
    
    def getRenderLayer(self):
        pass
    
    
    def isAbstractClass(self):
        pass
    
    
    def isAcceptableChild(self, model):
        """
        Check if the model could be a child
        """
    
        pass
    
    
    def isApplied(self):
        pass
    
    
    def isEnabled(self):
        pass
    
    
    def isLocalRender(self, dataBlock='None'):
        pass
    
    
    def isSelfEnabled(self, dataBlock='None'):
        pass
    
    
    def isValid(self):
        pass
    
    
    def postConstructor(self):
        pass
    
    
    def setAttributeName(self, attributeName):
        """
        Set the name of the attribute to be overridden.
        """
    
        pass
    
    
    def setLocalRender(self, value):
        pass
    
    
    def setSelfEnabled(self, value):
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def updateOnEnabledChanged(self):
        """
        Does this override need an update when its enabled output changes?
        
        The base class behavior is that overrides need no update.
        """
    
        pass
    
    
    def creator(cls):
        """
        # Awkwardly, abstract base classes seem to need a creator method.
        """
    
        pass
    
    
    def initializer():
        pass
    
    
    attrLocal = None
    
    
    attrName = None
    
    
    enabled = None
    
    
    kTypeId = None
    
    
    kTypeName = 'override'
    
    
    layerNumIsolatedChildren = None
    
    
    parentEnabled = None
    
    
    selfEnabled = None


class Property(_Property):
    """
    Namedtuple to hold what is needed to encode a property (name, encode function, decode function).
    'name' will be the name of the given attribute (MObject).
    """
    
    
    
    def __new__(cls, attr, encode, decode):
        pass
    
    
    __dict__ = None


class UnapplyCmd(_MPxCommand):
    """
    Command to unapply and reapply an override.
    
    This command is a private implementation detail of this module and should
    not be called otherwise.
    """
    
    
    
    def __init__(self, override):
        pass
    
    
    def doIt(self, args):
        pass
    
    
    def isUndoable(self):
        pass
    
    
    def redoIt(*args, **kwargs):
        pass
    
    
    def undoIt(*args, **kwargs):
        pass
    
    
    def creator():
        pass
    
    
    def execute(override):
        """
        Unapply the override, and add an entry to the undo queue.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    kCmdName = 'unapplyOverride'
    
    
    override = None


class ValueOverride(Override):
    """
    Override node base class for all value overrides.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def acceptsAttr(*args, **kwargs):
        pass
    
    
    def apply(*args, **kwargs):
        pass
    
    
    def applyInsertOne(self, node, attrName, nextOvr):
        """
        Apply this override to a single node at the given priority.
        
        - node is the name of the node (or DAG instance path), or an MObject.
        - attrName is the name of the attribute the override is applied to.
        - nextOvr is the next higher-priority override.  If None,
          the override is applied as highest priority (closest to the
          attribute).
        """
    
        pass
    
    
    def getOverridden(self):
        """
        Return the list of nodes being overridden.
        
        The items in the return list are triplets of (MObject, attrName, ovrNext).
        MObject is the object being overridden, attrName is the name of the attribute 
        being overridden and ovrNext is the override node in the position of the next 
        override in the apply override list.
        
        Returns an empty list if no attribute is being overridden.
        """
    
        pass
    
    
    def postApply(*args, **kwargs):
        pass
    
    
    def reapply(*args, **kwargs):
        pass
    
    
    def unapply(*args, **kwargs):
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'valueOverride'


class RelOverride(LeafClass, ValueOverride):
    """
    Relative override node to transform a attribute using:
    
    newValue = originalValue * multiply + offset
    
    This concrete override node type implements a relative override
    for a float scalar attribute.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def compute(self, plug, dataBlock):
        pass
    
    
    def finalize(*args, **kwargs):
        pass
    
    
    def getMultiply(self):
        pass
    
    
    def getOffset(self):
        pass
    
    
    def isFinalized(self):
        pass
    
    
    def isValid(self):
        pass
    
    
    def multiplyPlugName(self):
        pass
    
    
    def offsetPlugName(self):
        pass
    
    
    def postConstructor(self):
        pass
    
    
    def setMultiply(self, value):
        pass
    
    
    def setOffset(self, value):
        pass
    
    
    def status(self):
        """
        Returns a problem string if there is a problem with override or None otherwise.
        """
    
        pass
    
    
    def initializer():
        pass
    
    
    kMultiplyLong = 'multiply'
    
    
    kMultiplyShort = 'mul'
    
    
    kOffsetLong = 'offset'
    
    
    kOffsetShort = 'ofs'
    
    
    kTypeId = None
    
    
    kTypeName = 'relOverride'


class AbsOverride(LeafClass, ValueOverride):
    """
    Absolute override node.
    
    This concrete override node type implements an absolute override
    (replace value) for an attribute.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def compute(self, plg, dataBlock):
        pass
    
    
    def finalize(*args, **kwargs):
        pass
    
    
    def getAttrValue(self):
        """
        Returns the value of the override.
        
        This value is always in internal units.  See OpenMaya documentation for
        MAngle, MDistance, and MTime.  plug.toUiUnits and plug.toInternalUnits
        can be used to convert between units.
        """
    
        pass
    
    
    def hasMissingDependencies(self):
        pass
    
    
    def isFinalized(self):
        pass
    
    
    def isValid(self):
        pass
    
    
    def postConstructor(self):
        pass
    
    
    def setAttrValue(self, value):
        """
        Sets the value of the override.
        
        This value must be in internal units.  See OpenMaya documentation for
        MAngle, MDistance, and MTime.  plug.toUiUnits and plug.toInternalUnits
        can be used to convert between units.
        """
    
        pass
    
    
    def status(self):
        """
        Returns a problem string if there is a problem with override or None otherwise.
        """
    
        pass
    
    
    def initializer():
        pass
    
    
    kAttrValueLong = 'attrValue'
    
    
    kAttrValueShort = 'atv'
    
    
    kTypeId = None
    
    
    kTypeName = 'absOverride'


class AbsUniqueOverride(UniqueOverride, AbsOverride):
    def initializer():
        pass
    
    
    kTargetNodeName = None
    
    
    kTypeId = None
    
    
    kTypeName = 'absUniqueOverride'


class RelUniqueOverride(UniqueOverride, RelOverride):
    def initializer():
        pass
    
    
    kTargetNodeName = None
    
    
    kTypeId = None
    
    
    kTypeName = 'relUniqueOverride'



def valid(f):
    """
    Decorator that calls the decorated method if and only if self.isValid() evaluates to True.
    """

    pass


def delete(*args, **kwargs):
    pass


def finalizationChanged(f):
    """
    Decorator for functions that may change the finalization of an override (decode, finalize).
    This will ensure that if the layer in which this override lives is visible, then the override
    should be unapplied and reapplied with the new finalization.
    """

    pass


def create(*args, **kwargs):
    pass


def fillVector(value, dimension):
    """
    Return a list of specified dimension initialized with value.
    
    If dimension is 0, return the argument value as a scalar.
    """

    pass


def attributeToPlug(f):
    """
    Decorator that adds a node name to an attribute name, if not present. (attribute => plug)
    Using template node name of parent collection's selector.
    """

    pass



kUnfinalized = []

kUnapplyCmdPrivate = []

kMissingDependencies = []

kUnconnectableAttr = []


