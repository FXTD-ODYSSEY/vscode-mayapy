"""
This module provides the connection override classes.

An override for an attribute is created by adding an override for it to an OverrideManager.
The RenderLayer class derives from the OverrideManager class, so the currently active layer 
is the manager to add the overrides to.

The manager is responsible for creating override apply nodes that represents an override on an 
attribute for a particular object. See overrideManager module for more information.

From the user perspective there is always just a single override created per override node, 
for instance replacing a single surface shader or replacing material assignments 
with a single new material. However, internally this can result in multiple overrides.
For example when overriding a material (shading engine) there can be multiple connections 
that need to be overridden per member of the collection. A single mesh can have multiple 
per-instance and per-face assignments that all need to be overridden for the material to have 
effect on the whole mesh.

All the apply overrides are added to the manager when the override node is applied, and they
exists until the override node is unapplied. During this time the override can be disabled/enabled which 
will switch all the values or connections according to the "new" and "original" plugs specified by the 
override. The override manager handles all changes that needs to be done then something is disabled/enabled.
The apply overrides are removed from the manager and deleted when the override node is unapplied.
"""

from maya.app.renderSetup.model.renderSetupPrivate import PostApplyCmd

class DstConnectionHandle(object):
    """
    Plug class that handles and persists a destination connection.
    
    The source of a destination connection can be in a referenced file.  If
    so, the connection is recorded by this class as a string, and stored in
    a dynamic attribute.
    
    On connect, if the source is referenced, store the string
    representation of the source.  On disconnect, if we have a string
    representation, remove it.  On access, if disconnected, check if we
    have a string representation.  If so, use it and connect.
    """
    
    
    
    def __init__(self, node, aDst, srcStrAttrNameLong, srcStrAttrNameShort):
        """
        Create the handle on the argument MObject node, for the destination
        attribute aDst.
        
        If the source is referenced, store its string representation in the
        attribute named srcStrAttrNameLong, srcStrAttrNameShort.
        """
    
        pass
    
    
    def connect(self, src):
        """
        Connect this destination to the argument source MPlug.  If the
        source node is referenced, store a string representation of the
        source.
        """
    
        pass
    
    
    def disconnect(self):
        """
        Disconnect this destination from its source (if any).  If we
        have a string representation of the source, it is removed.
        """
    
        pass
    
    
    def dst(self):
        """
        Return the destination MPlug of this handle.
        
        If disconnected, we check if we have a string representation.  If
        so, we use it and try to re-connect to the source.
        """
    
        pass
    
    
    def src(self):
        """
        Convenience to return the source MPlug of this destination plug
        handle.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


from . import override

class ConnectionOverride(override.AbsOverride):
    """
    Attribute connection override node.
    
    This override node type implements an attribute override by setting a
    new value or connection on an attribute.
    
    A value attribute is used to let the user set a value or make a connection to
    the node to be used as override. This attribute is dynamic and created 
    with a type matching the target attribute. The override node is not valid 
    until such a dynamic attribute is created. An override that is not valid 
    will not be applied when its layer is made active. However an override that 
    later becomes valid (the user drag and drops a target attribute), will then 
    automatically be applied if the layer is active.
    
    Source connections to the value attribute is encoded/decoded for export/import
    using OverridePlugHandle (in override.py). This class handles missing dependencies
    on decode and remakes the connection when the dependency node is added.
    """
    
    
    
    def __del__(self):
        pass
    
    
    def __init__(self):
        pass
    
    
    def activate(self):
        pass
    
    
    def apply(*args, **kwargs):
        pass
    
    
    def attrChangedCB(self, msg, plg, otherPlug, clientData):
        """
        Update the connection override when attrValue changes.
        """
    
        pass
    
    
    def deactivate(self):
        pass
    
    
    def doAction(self, target, source):
        """
        This method performs the override action for a given target and source.
        """
    
        pass
    
    
    def doSaveOriginal(self, target, storage):
        """
        This method performs saving of original state for a given target
        and a storage plug for storing the state.
        """
    
        pass
    
    
    def enabledChanged(self):
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
    
    
    def isApplicable(self):
        pass
    
    
    def onFileOpened(self):
        pass
    
    
    def postApply(*args, **kwargs):
        pass
    
    
    def postConstructor(self):
        """
        Method running after the node is constructed. 
        All initialization that will access the MObject or other 
        methods of the MPxNode must be done here. Since the node 
        is not fully created until after the call to __init__
        """
    
        pass
    
    
    def reapply(*args, **kwargs):
        pass
    
    
    def setSource(self, attr):
        """
        Method used by import to set the new source attribute.
        """
    
        pass
    
    
    def unapply(*args, **kwargs):
        pass
    
    
    def update(*args, **kwargs):
        pass
    
    
    def updateOnEnabledChanged(self):
        """
        Connection overrides need to update their apply override nodes
        on enabled changed, so this method returns true.
        """
    
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'connectionOverride'


from . import applyOverride

class ApplyConnectionOverride(applyOverride.LeafClass, applyOverride.ApplyOverride):
    """
    Connection override apply class. 
    
    Class for applying all connection overrides. It is similar to apply nodes for value overrides, 
    but with some notable differences. Firstly, since it is generating connections it cannot be connected to 
    the target attribute like value apply nodes. Secondly, there is no numeric values flowing between these 
    nodes. Instead message attributes are used to chain the nodes together and the chain represents the order 
    of priority for the nodes.
    
    When an override needs updating, e.g. if the enabled state is changed, the chain of apply nodes is 
    traversed to find the highest priority enabled apply node. The override action from that node 
    is then executed on the target attribute to perform the override change.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def connectTarget(self, target):
        """
        Connect the argument MPlug source to this node's target plug
        destination, to store it.
        """
    
        pass
    
    
    def extract(self):
        """
        Removes self from the apply override chain. This will trigger an update of the chain.
        """
    
        pass
    
    
    def finalize(self, ovrValuePlug):
        pass
    
    
    def getNextPlug(self):
        pass
    
    
    def getOriginalPlug(self):
        pass
    
    
    def getPrevPlug(self):
        pass
    
    
    def getTarget(self):
        """
        Return the target's plug. This is held by the apply override with the highest priority.
        """
    
        pass
    
    
    def insert(self, target, nextOvr='None'):
        """
        Insert self in the override chain for given target, or start the chain if none exists.
        """
    
        pass
    
    
    def isApplicable(self):
        pass
    
    
    def isEnabled(self):
        pass
    
    
    def moveTargetTo(self, to):
        """
        Move the target of this ApplyConnectionOverride to the argument
        ApplyConnectionOverride.
        """
    
        pass
    
    
    def next(self):
        """
        Returns the next connection override in the chain (higher priority) if any, None otherwise.
        """
    
        pass
    
    
    def postConstructor(self):
        pass
    
    
    def prev(self):
        """
        Returns the previous connection override in the chain (lower priority) if any, None otherwise.
        """
    
        pass
    
    
    def typeId(self):
        pass
    
    
    def typeName(self):
        pass
    
    
    def update(self):
        pass
    
    
    def create(cls, name):
        pass
    
    
    def forwardGenerator(applyNode):
        """
        Generator to iterate on apply override nodes in the direction of
        higher-priority apply override nodes.
        
        See reverseGenerator() documentation. Moving down a chain of apply
        override nodes from lower priority to higher priority means traversing
        the connection from the 'next' plug (source) of the lower-priority
        node to the 'previous' plug (destination) of the higher-priority node.
        """
    
        pass
    
    
    def initializer():
        pass
    
    
    def reverseGenerator(applyNode):
        """
        Generator to iterate on apply override nodes in the direction of
        lower-priority apply override nodes.
        
        When more than one override applies to a single overridden attribute, a
        chain of apply override nodes is formed, with the highest priority
        apply override nodes directly connected to the overridden attribute,
        and previous overrides having lower priority.
        
        In such a case, the 'next' plug of a lower-priority apply override node
        is connected to the 'previous' plug of a higher-priority apply override
        node. Moving up a chain of apply override nodes from higher priority
        to lower priority therefore means traversing the connection from the
        'previous' plug (destination) of the higher-priority node to the 'next'
        plug (source) of the lower-priority node.
        """
    
        pass
    
    
    aNext = None
    
    
    aPrevious = None
    
    
    aTarget = None
    
    
    kOriginalLong = 'original'
    
    
    kOriginalShort = 'org'
    
    
    kTargetLong = 'target'
    
    
    kTargetNameLong = 'targetName'
    
    
    kTargetNameShort = 'tgn'
    
    
    kTargetShort = 'tg'
    
    
    kTypeId = None
    
    
    kTypeName = 'applyConnectionOverride'


class ShaderOverride(ConnectionOverride):
    """
    Shader override node.
    
    Specialization of connection override for surface shader replacement.
    
    This override node type implements a shader override
    (replace surface shader) for shadingEngines assigned to DAG nodes.
    
    The surfaceShader attribute on shadingEngine nodes holds the shader to 
    use as surface shader for that material. See MaterialOverride docstring
    for how the assignment to shadingEngine is handled.
    
    This class will override the connection to the surfaceShader attribute
    with another shader node specified by the user. Since it is just replacing
    surfaceShader connections and keeps all shadingEngine assignments it will
    preserve displacement and volume shader assignments.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def doAction(self, target, source):
        """
        This method performs the override action for a given target and source.
        """
    
        pass
    
    
    def doSaveOriginal(self, target, storage):
        """
        This method performs saving of original state for a given target
        and a storage plug for storing the state.
        """
    
        pass
    
    
    def isApplicable(self):
        pass
    
    
    def isValid(self):
        pass
    
    
    def postConstructor(self):
        """
        Method running after the node is constructed. 
        All initialization that will access the MObject or other 
        methods of the MPxNode must be done here. Since the node 
        is not fully created until after the call to __init__
        """
    
        pass
    
    
    def setShader(*args, **kwargs):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'shaderOverride'


class MaterialOverride(ConnectionOverride):
    """
    Material override node.
    
    Specialization of connection override for material (shading engine) assignments.
    
    This override node type implements a material override
    (replace shading engine assignments) for DAG nodes.
    
    Shading group assignments in Maya are represented by connections to the 
    instObjGroups attribute on the shape node. It's an array attribute that represents 
    per-instance assignments and per-face group assignments in the following way:
    
    myShape.instObjGroups[N] - connection to this represents material assignment to
    instance number N.
    
    myShape.instObjGroups[N].objectGroups[M] - connection to this represents assignment 
    to face group M of instance number N.
    
    The connections are made from myShape.instObjGroups[N] -> mySG.dagSetMembers[X],
    where mySG is a shadingEngine node, which represents that this shading engine is
    assigned to that instance of the shape. The dagSetMembers attribute is special and is
    using disconnectBehavior = kDelete which means its array elements are deleted as soon
    as they are disconnected. So we cannot save these element plugs explicitly. Instead we 
    use the message attribute to have a reference to the node. Then we override the
    doAction() and doSaveOriginal() methods to handle the shading engine set assignments.
    
    Since this override type is replacing the whole shadingEngine with a new one,
    it will not preserve any displacement or volume material set on the shadingEngine.
    
    Care must be taken when applying an override to shapes whose original
    material is from a referenced file.  In addition to preserving the
    state of the original material through a connection, we also save the
    name of the material in the apply override node as a string, if the
    material was referenced.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def doAction(self, target, source):
        """
        This method performs the override action for a given target and source.
        The target and source arguments are MPlug objects.
        """
    
        pass
    
    
    def doSaveOriginal(self, target, storage):
        """
        This method performs saving of original state for a given target
        and a storage plug for storing the state.
        """
    
        pass
    
    
    def isApplicable(self):
        pass
    
    
    def isValid(self):
        pass
    
    
    def postConstructor(self):
        """
        Method running after the node is constructed. 
        All initialization that will access the MObject or other 
        methods of the MPxNode must be done here. Since the node 
        is not fully created until after the call to __init__
        """
    
        pass
    
    
    def setMaterial(*args, **kwargs):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    def saveShadingEngine(shadingEngineObj, storagePlug):
        """
        Save a connection to the shading engine node in the storage plug.
        
        This function unconditionally connects the shading engine to the
        storage plug.  It also stores the name of the shading engine as a full
        name with the namespace path in the storage plug's node, if the shading
        engine is not in the main scene.
        """
    
        pass
    
    
    kShadingEngineNameLong = 'shadingEngineName'
    
    
    kShadingEngineNameShort = 'sen'
    
    
    kTypeId = None
    
    
    kTypeName = 'materialOverride'


class ConnectionUniqueOverride(override.UniqueOverride, ConnectionOverride):
    def initializer():
        pass
    
    
    kTargetNodeName = None
    
    
    kTypeId = None
    
    
    kTypeName = 'connectionUniqueOverride'



def setRestoringOriginal(restoringOriginal):
    pass


def dagPathToSEConnections(dagPath):
    """
    Returns an iterable over all the connections from an instance to a shading engine.
    There can be more than one when mesh has per-face shading.
    
    Connections are returned as tuples (srcPlug, destPlug)
    "srcPlug" belongs to the shape. "destPlug" belongs to the assigned shading engine.
    srcPlug ---> destPlug
    """

    pass


def plugsToSEConnection(plgs):
    pass


def handleRestoringOriginalCtx():
    """
    Create and return a context to properly set reference edits.
    
    The context turns reference edits on when restoring the original of a
    connection override.
    """

    pass


def isRestoringOriginal():
    pass


def _transferConnectedPlug(src, dst):
    """
    # Copy-pasted from utils._transferConnectedPlug, so that LEGB lookup will
    # find the transferPlug function in this module, which correctly handles
    # reference edits.
    """

    pass


def setSourceAndApply(override, srcNode, srcAttr):
    """
    Engine function for MaterialOverride.setMaterial and ShaderOverride.setShader.
    """

    pass


def transferPlug(src, dst):
    """
    Transfer the connection or value set on plug 'src' on to the plug 'dst'.
    """

    pass



kMaterialOverrideFailure = []

_restoringOriginal = False

kApplyNodeNoRenderLayerConnection = []

kAttrValueAlreadyCreated = []


