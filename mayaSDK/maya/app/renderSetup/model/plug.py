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


class UnlockedGuard:
    """
    Safe way to unlock a plug in a block. 
    Lock state will be recovered back on exit of the block (for ancestors and children plugs).
    Example:
        with UnlockedGuard(aLockedPlug):
            someActionsOnThePlug()
    """
    
    
    
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, plg):
        pass


class Plug(object):
    """
    Helper class to allow seamless value assignment from one plug to another, 
    while correctly handling and abstracting away plug type.
    
    "self.type" returns the type of the plug.
        This is necessary to determine how to read and write the plug.
    "self.value" returns the value of the plug.
    "self.value = otherValue" will set the value of the plug to otherValue.
        This mutator assumes otherValue to be the same type as self.type
    
    "self.overrideType" returns the type of the override that should be created to override this plug.
    """
    
    
    
    def __init__(self, plugOrNode, attrName='None'):
        """
        Constructors:
        Plug(MPlug)
        Plug(string (full plug name))
        Plug(MObject, MObject)
        Plug(MObject, string (attribute name))
        Plug(string (node name), string (attribute name))
        """
    
        pass
    
    
    def __str__(self):
        pass
    
    
    def accepts(self, other):
        """
        Returns true if plug would accept a connection with other plug
        i.e. plug and other plug are type compatible for connection.
        """
    
        pass
    
    
    def acceptsOverrideType(self, typeId):
        pass
    
    
    def applyOverrideType(self, overType):
        pass
    
    
    def attribute(self):
        """
        Returns the attribute (MFnAttribute) of the plug
        """
    
        pass
    
    
    def availableOverrides(self):
        pass
    
    
    def children(self):
        pass
    
    
    def cloneAttribute(self, nodeObj, longName, shortName, undoable='1'):
        """
        Creates a new attribute on a node by cloning this plug's attribute.
        Undoable by default
        """
    
        pass
    
    
    def copyValue(self, other):
        """
        Sets the value of plug 'self' to the value contained in plug 'other' 
        The 'other' plug can be either a Plug or a MPlug.
        """
    
        pass
    
    
    def createAttributeFrom(self, nodeObj, longName, shortName, limits='None'):
        """
        Creates a new attribute on a node by cloning this plug's attribute. 
        
        Note: None for a limit value means that there is no limit. For example,
              if min is None, it means that there is no minimum limit.
        """
    
        pass
    
    
    def getAttributeLimits(self):
        """
        Get the limits of the plug
        """
    
        pass
    
    
    def isOvrSupported(self):
        pass
    
    
    def localizedTypeString(self):
        pass
    
    
    def node(self):
        pass
    
    
    def overrideType(self, overType):
        pass
    
    
    def parent(self):
        pass
    
    
    def setAttributeLimits(self, limits):
        pass
    
    
    def createAttribute(nodeObj, longName, shortName, dict, undoable='1'):
        """
        Create a new attribute on a node using the given names and properties dictionary. 
        Returns an MObject to the new attribute. By default, it uses the command 
        addDynamicAttribute (if it's not undoable, use MFnDependencyNode.addAttribute()) 
        to add the returned object as a new dynamic attribute on a node.
        """
    
        pass
    
    
    def getNames(plugName):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    attributeName = None
    
    hasLimits = None
    
    isConnectable = None
    
    isKeyable = None
    
    isLocked = None
    
    isNumeric = None
    
    isUnit = None
    
    isValid = None
    
    isVector = None
    
    name = None
    
    nodeName = None
    
    plug = None
    
    type = None
    
    uiUnitValue = None
    
    value = None
    
    kAngle = 12
    
    
    kArray = 14
    
    
    kBool = 5
    
    
    kByte = 4
    
    
    kColor = 6
    
    
    kDistance = 13
    
    
    kDouble = 2
    
    
    kEnum = 7
    
    
    kFilename = 15
    
    
    kFloat = 1
    
    
    kInt = 3
    
    
    kInvalid = 0
    
    
    kLast = 16
    
    
    kMessage = 10
    
    
    kObject = 9
    
    
    kString = 8
    
    
    kTime = 11


class AddDynamicAttribute(_MPxCommand):
    """
    Undoable command to add an attribute to a node
    
    This command is a private implementation detail of this module and should
    not be called otherwise.
    """
    
    
    
    def __init__(self, node, attribute, mdgModifier):
        pass
    
    
    def doIt(self, args):
        pass
    
    
    def isUndoable(self):
        pass
    
    
    def redoIt(self):
        pass
    
    
    def undoIt(self):
        pass
    
    
    def creator():
        pass
    
    
    def execute(node, attribute):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    attribute = None
    
    
    kCmdName = 'addDynamicAttribute'
    
    
    mdgModifier = None
    
    
    node = None



def _createFilenameAttr(longName, shortName):
    pass


def relatives(plg):
    """
    Returns relatives (ancestors, plug itself and descendant) of the given plug in deterministic order.
    Parents are guaranteed to come before children in generator.
    """

    pass


def toUiUnits(type, value):
    pass


def findPlug(node, attr='None'):
    """
    Return a Plug instance if the MPlug was found, None otherwise.
    """

    pass


def isSettable(plug):
    """
    Predicate that returns whether the MPlug argument can be set.
    """

    pass


def toInternalUnits(type, value):
    pass


def value(mPlug):
    """
    Convenience function to retrieve the value of an MPlug.
    """

    pass



kNotOverridablePlug = []

kPlugHasConnectedParent = []

kVectorTypeStr = []

kUndoable = 1

kAddAttributePrivate = []

kNotUndoable = 0

kUnsupportedAttribute = []

kPlugWithoutLimits = []

kArityMismatch = []

kPlugHasNotSettableChild = []

kUnknownType = []

kCompoundTypeStr = []


