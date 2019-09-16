def isExistingClassification(t):
    pass


def getSrcNodeName(dst):
    """
    Get the name of the node connected to the argument dst plug.
    """

    pass


def getCollectionsRecursive(parent):
    pass


def disconnect(src, dst):
    pass


def findVolumeShader(shadingEngine, search='False'):
    """
    Returns the volume shader (as MObject) of the given shading engine (as MObject).
    """

    pass


def transferPlug(src, dst):
    """
    Transfer the connection or value set on plug 'src' on to the plug 'dst'.
    """

    pass


def findSurfaceShader(shadingEngine, search='False'):
    """
    Returns the surface shader (as MObject) of the given shading engine (as MObject).
    """

    pass


def findPlug(userNode, attr):
    """
    Return plug corresponding to attr on argument userNode.
    
    If the argument userNode is None, or the attribute is not found, None
    is returned.
    """

    pass


def disconnectSrc(src):
    """
    Disconnect a source (readable) plug from all its destinations.
    
    Note that a single plug can be both source and destination, so this
    interface makes the disconnection intent explicit.
    """

    pass


def isSurfaceShaderNode(obj):
    pass


def getSrcUserNode(dst):
    """
    Get the user node connected to the argument dst plug.
        Note: Only applies to MPxNode derived nodes
    
    If the dst plug is unconnected, None is returned.
    """

    pass


def plugSrc(dstPlug):
    """
    Return the source of a connected destination plug.
    
    If the destination is unconnected, returns None.
    """

    pass


def getOverridesRecursive(parent):
    pass


def nameToUserNode(name):
    pass


def isShadingType(typeName):
    pass


def canOverrideNode(node):
    pass


def createSrcMsgAttr(longName, shortName):
    """
    Create a source (a.k.a. output, or readable) message attribute.
    """

    pass


def deleteNode(node):
    """
    Remove the argument node from the graph.
    
    This function is undoable.
    """

    pass


def connect(src, dst):
    """
    Connect source plug to destination plug.
    
    If the dst plug is None, the src plug will be disconnected from all its
    destinations (if any).  If the src plug is None, the dst plug will be
    disconnected from its source (if any).  If both are None, this function
    does nothing.  If the destination is already connected, it will be
    disconnected.
    """

    pass


def isExistingType(t):
    pass


def getDstUserNodes(src):
    """
    Get the user nodes connected to the argument src plug.
        Note: Only applies to MPxNode derived nodes
    
    If the src plug is unconnected, None is returned.
    """

    pass


def plugDst(srcPlug):
    """
    Return the destinations of a connected source plug.
    
    If the source is unconnected, returns None.
    """

    pass


def _recursiveSearch(colList):
    """
    # Fonctions to compute the number of operations when layer are switched
    """

    pass


def getTotalNumberOperations(model):
    pass


def _isDestination(plug):
    """
    Returns True if the given plug is a destination plug, and False otherwise.
    
    If the plug is a compond attribute it returns True if any of it's children is a 
    destination plug.
    """

    pass


def isShadingNode(obj):
    pass


def disconnectDst(dst):
    """
    Disconnect a destination (writable) plug from its source.
    
    Note that a single plug can be both source and destination, so this
    interface makes the disconnection intent explicit.
    """

    pass


def findDisplacementShader(shadingEngine, search='False'):
    """
    Returns the displacement shader (as MObject) of the given shading engine (as MObject).
    """

    pass


def _findShader(shadingEngine, attribute, classification='None'):
    """
    Returns the shader connected to given attribute on given shading engine.
    Optionally search for nodes from input connections to the shading engines 
    satisfying classification if plug to attribute is not a destination and
    a classification string is specified.
    """

    pass


def isInheritedType(parentTypeName, childTypeName):
    pass


def getSrcNode(dst):
    """
    Get the node connected to the argument dst plug.
    """

    pass


def createGenericAttr(longName, shortName):
    pass


def nameToExistingUserNode(name):
    pass


def _transferConnectedPlug(src, dst):
    pass


def connectMsgToDst(userNode, dst):
    """
    Connect the argument userNode's message attribute to the
    argument dst plug.
    
    If the userNode is None the dst plug is disconnected
    from its sources.
    
    If the dst plug is None the userNode's message plug
    is disconnected from its destinations
    """

    pass


def isSurfaceShaderType(typeName):
    pass


def notUndoRedoing(f):
    """
    Decorator that will call the decorated method only if not currently in undoing or redoing.
    Particularly useful to prevent callbacks from generating commands since that would clear the redo stack.
    """

    pass


def createDstMsgAttr(longName, shortName):
    """
    Create a destination (a.k.a. input, or writable) message attribute.
    """

    pass



kNoSuchNode = []

kSupportedVectorTypes = set()

kSupportedSimpleTypes = set()

kPlugTypeMismatch = []


