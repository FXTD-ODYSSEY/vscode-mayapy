from maya.OpenMayaRender import *
from maya.OpenMayaUI import *
from maya.OpenMaya import *
from maya.OpenMayaMPx import *

from maya.OpenMayaFX import MFnField
from maya.OpenMayaFX import MHairSystem
from maya.OpenMayaAnim import MFnKeyframeDeltaScale
from maya.OpenMayaFX import MDynSweptLine
from maya.OpenMayaAnim import MFnKeyframeDeltaAddRemove
from maya.OpenMayaAnim import MFnKeyframeDeltaInfType
from maya.OpenMayaFX import MnParticle
from maya.OpenMayaAnim import MFnCharacter
from maya.OpenMayaAnim import MFnKeyframeDeltaWeighted
from maya.OpenMayaFX import MnCloth
from maya.OpenMayaAnim import MAnimCurveClipboardItem
from maya.OpenMayaFX import MFnTurbulenceField
from maya.OpenMayaAnim import MFnWeightGeometryFilter
from maya.OpenMayaAnim import MFnBlendShapeDeformer
from maya.OpenMayaFX import MFnGravityField
from maya.OpenMayaFX import MFnVortexField
from maya.OpenMayaFX import MFnRadialField
from maya.OpenMayaAnim import MIkHandleGroup
from maya.OpenMayaAnim import MFnKeyframeDelta
from maya.OpenMayaFX import MDynamicsUtil
from maya.OpenMayaAnim import MFnMotionPath
from maya.OpenMayaFX import MRenderLine
from maya.OpenMayaFX import MFnVolumeAxisField
from maya.OpenMayaAnim import MFnClip
from maya.OpenMayaFX import MnSolver
from maya.OpenMayaAnim import MFnLattice
from maya.OpenMayaFX import MFnNIdData
from maya.OpenMayaAnim import MFnGeometryFilter
from maya.OpenMayaFX import MFnNObjectData
from maya.OpenMayaAnim import MIkSystem
from maya.OpenMayaAnim import MAnimCurveChange
from maya.OpenMayaFX import MnRigid
from maya.OpenMayaFX import MFnDynSweptGeometryData
from maya.OpenMayaFX import MFnUniformField
from maya.OpenMayaAnim import MFnHikEffector
from maya.OpenMayaAnim import MAnimMessage
from maya.OpenMayaAnim import MFnKeyframeDeltaBlockAddRemove
from maya.OpenMayaAnim import MFnKeyframeDeltaBreakdown
from maya.OpenMayaFX import MDynSweptTriangle
from maya.OpenMayaAnim import MItKeyframe
from maya.OpenMayaFX import MFnNewtonField
from maya.OpenMayaFX import MFnInstancer
from maya.OpenMayaAnim import MFnIkEffector
from maya.OpenMayaFX import MFnParticleSystem
from maya.OpenMayaFX import MnObject
from maya.OpenMayaAnim import MFnSkinCluster
from maya.OpenMayaFX import MFnFluid
from maya.OpenMayaAnim import MFnAnimCurve
from maya.OpenMayaFX import MFnPfxGeometry
from maya.OpenMayaAnim import MAnimUtil
from maya.OpenMayaAnim import MAnimControl
from maya.OpenMayaAnim import MFnKeyframeDeltaTangent
from maya.OpenMayaFX import MFnAirField
from maya.OpenMayaAnim import MAnimCurveClipboard
from maya.OpenMayaAnim import MFnIkHandle
from maya.OpenMayaAnim import MFnLatticeDeformer
from maya.OpenMayaFX import MFnDragField
from maya.OpenMayaAnim import MFnKeyframeDeltaMove
from maya.OpenMayaAnim import MFnIkJoint
from maya.OpenMayaAnim import MFnIkSolver
from maya.OpenMayaAnim import MAnimCurveClipboardItemArray
from maya.OpenMayaAnim import MFnWireDeformer
from maya.OpenMayaFX import MRenderLineArray

class SafeApiPtr(object):
    """
    A wrapper for api pointers which also contains a reference
    to the MScriptUtil which contains the storage. This helps
    ensure that the 'storage' for the pointer doesn't get
    wiped out before the pointer does. Pass the SafeApiPtr
    around in place of the 'true' pointer - then, when
    the 'true' pointer is needed (ie, immediately
    before feeding it into an api function), 'call'
    the SafeApiPtr object to return the 'true'
    pointer.
    
    Examples
    --------
    >>> from pymel.api.allapi import *
    >>> sel = MSelectionList()
    >>> sel.add('perspShape')
    >>> dag = MDagPath()
    >>> sel.getDagPath(0, dag)
    >>> cam = MFnCamera(dag)
    
    >>> aperMin = SafeApiPtr('double')
    >>> aperMax = SafeApiPtr('double')
    >>> cam.getFilmApertureLimits(aperMin(), aperMax())
    >>> print '%.5f, %.5f' % (aperMin.get(), aperMax.get())
    0.01378, 20.28991
    """
    
    
    
    def __call__(self):
        pass
    
    
    def __getitem__(self, index):
        pass
    
    
    def __init__(self, valueType, scriptUtil='None', size='1', asTypeNPtr='False'):
        """
        :Parameters:
        valueType : `string`
            The name of the maya pointer type you would like
            returned - ie, 'int', 'short', 'float'.
        scriptUtil : `MScriptUtil`
            If you wish to use an existing MScriptUtil as
            the 'storage' for the value returned, specify it
            here - otherwise, a new MScriptUtil object is
            created.
        size : `int`
            If we want a pointer to an array, size indicates
            the number of items the array holds.  If we are
            creating an MScriptUtil, it will be initialized
            to hold this many items - if we are fed an
            MScriptUtil, then it is your responsibility to
            make sure it can hold the necessary number of items,
            or else maya will crash!
        asTypeNPtr : `bool`
            If we want a call to this SafeApiPtr to return a pointer
            for an argument such as:
               int2 &myArg;
            then we need to set asTypeNPtr to True:
               SafeApiPtr('int', size=2, asTypeNPtr=True)
            Otherwise, it is assumed that calling the object returns array
            ptrs:
               int myArg[2];
        """
    
        pass
    
    
    def __len__(self):
        pass
    
    
    def __setitem__(self, index, value):
        pass
    
    
    def get(self):
        """
        Dereference the pointer - ie, get the actual value we're pointing to.
        """
    
        pass
    
    
    def set(self, value):
        """
        Store the actual value we're pointing to.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def MnSolver_swigregister(*args, **kwargs):
    pass


def MDynSweptTriangle_className(*args, **kwargs):
    pass


def MRenderLine_className(*args, **kwargs):
    pass


def isValidMPlug(obj):
    pass


def MFnKeyframeDeltaInfType_swigregister(*args, **kwargs):
    pass


def MFnParticleSystem_className(*args, **kwargs):
    pass


def MFnUniformField_className(*args, **kwargs):
    pass


def MFnField_className(*args, **kwargs):
    pass


def MAnimControl_setGlobalInTangentType(*args, **kwargs):
    pass


def isValidMNodeOrPlug(obj):
    pass


def MAnimControl_animationEndTime(*args, **kwargs):
    pass


def MFnGeometryFilter_className(*args, **kwargs):
    pass


def MAnimControl_setAnimationStartEndTime(*args, **kwargs):
    pass


def MAnimControl_globalInTangentType(*args, **kwargs):
    pass


def MAnimCurveChange_swigregister(*args, **kwargs):
    pass


def toMObject(nodeName):
    """
    Get the API MObject given the name of an existing node
    """

    pass


def MFnIkEffector_swigregister(*args, **kwargs):
    pass


def MHairSystem_setRegisteringCallableScript(*args, **kwargs):
    pass


def MAnimUtil_findAnimationLayers(*args, **kwargs):
    pass


def MDynamicsUtil_removeNodeTypeFromRunup(*args, **kwargs):
    pass


def MFnDynSweptGeometryData_swigregister(*args, **kwargs):
    pass


def MAnimControl_setMinTime(*args, **kwargs):
    pass


def MObjectName(obj):
    """
    Get the name of an existing MPlug, MDagPath or MObject representing a dependency node
    """

    pass


def MAnimMessage_addAnimKeyframeEditedCallback(*args, **kwargs):
    pass


def MFnVolumeAxisField_swigregister(*args, **kwargs):
    pass


def MIkSystem_isGlobalSolve(*args, **kwargs):
    pass


def MFnKeyframeDeltaBreakdown_swigregister(*args, **kwargs):
    pass


def MHairSystem_unregisterCollisionSolverCollide(*args, **kwargs):
    pass


def getPlugValue(plug):
    """
    given an MPlug, get its value
    """

    pass


def MDynamicsUtil_evalDynamics2dTexture(*args, **kwargs):
    pass


def MFnCharacter_className(*args, **kwargs):
    pass


def MAnimControl_playbackBy(*args, **kwargs):
    pass


def MAnimControl_globalOutTangentType(*args, **kwargs):
    pass


def MFnKeyframeDeltaScale_swigregister(*args, **kwargs):
    pass


def MRenderLineArray_swigregister(*args, **kwargs):
    pass


def MAnimControl_setGlobalOutTangentType(*args, **kwargs):
    pass


def MFnField_swigregister(*args, **kwargs):
    pass


def MAnimControl_setWeightedTangents(*args, **kwargs):
    pass


def MIkSystem_findSolver(*args, **kwargs):
    pass


def MFnBlendShapeDeformer_className(*args, **kwargs):
    pass


def MAnimMessage_flushAnimKeyframeEditedCallbacks(*args, **kwargs):
    pass


def MFnRadialField_swigregister(*args, **kwargs):
    pass


def MFnLatticeDeformer_swigregister(*args, **kwargs):
    pass


def MAnimControl_currentTime(*args, **kwargs):
    pass


def MFnClip_swigregister(*args, **kwargs):
    pass


def MRenderLine_swigregister(*args, **kwargs):
    pass


def MAnimControl_playbackMode(*args, **kwargs):
    pass


def MFnVortexField_className(*args, **kwargs):
    pass


def isValidMDagNode(obj):
    pass


def MFnKeyframeDeltaAddRemove_className(*args, **kwargs):
    pass


def MAnimControl_weightedTangents(*args, **kwargs):
    pass


def MAnimCurveChange_className(*args, **kwargs):
    pass


def MFnMotionPath_className(*args, **kwargs):
    pass


def MFnRadialField_className(*args, **kwargs):
    pass


def MDynamicsUtil_hasValidDynamics2dTexture(*args, **kwargs):
    pass


def toMPlug(plugName):
    """
    Get the API MObject given the name of an existing plug (node.attribute)
    """

    pass


def MIkSystem_swigregister(*args, **kwargs):
    pass


def MFnNObjectData_className(*args, **kwargs):
    pass


def MFnGravityField_className(*args, **kwargs):
    pass


def MFnDragField_className(*args, **kwargs):
    pass


def MFnDragField_swigregister(*args, **kwargs):
    pass


def MHairSystem_registeringCallableScript(*args, **kwargs):
    pass


def MAnimControl_autoKeyMode(*args, **kwargs):
    pass


def MAnimUtil_className(*args, **kwargs):
    pass


def MFnWireDeformer_className(*args, **kwargs):
    pass


def MItGraph(nodeOrPlug, *args, **kwargs):
    """
    Iterate over MObjects of Dependency Graph (DG) Nodes or Plugs starting at a specified root Node or Plug,
    If a list of types is provided, then only nodes of these types will be returned,
    if no type is provided all connected nodes will be iterated on.
    Types are specified as Maya API types.
    The following keywords will affect order and behavior of traversal:
    upstream: if True connections will be followed from destination to source,
              if False from source to destination
              default is False (downstream)
    breadth: if True nodes will be returned as a breadth first traversal of the connection graph,
             if False as a preorder (depth first)
             default is False (depth first)
    plug: if True traversal will be at plug level (no plug will be traversed more than once),
          if False at node level (no node will be traversed more than once),
          default is False (node level)
    prune : if True will stop the iteration on nodes than do not fit the types list,
            if False these nodes will be traversed but not returned
            default is False (do not prune)
    """

    pass


def MAnimControl_setMaxTime(*args, **kwargs):
    pass


def MFnKeyframeDeltaTangent_swigregister(*args, **kwargs):
    pass


def MAnimMessage_addNodeAnimKeyframeEditedCallback(*args, **kwargs):
    pass


def MAnimControl_stop(*args, **kwargs):
    pass


def MIkSystem_setGlobalSolve(*args, **kwargs):
    pass


def MFnIkSolver_swigregister(*args, **kwargs):
    pass


def MnParticle_swigregister(*args, **kwargs):
    pass


def MFnIkEffector_className(*args, **kwargs):
    pass


def MHairSystem_unregisterCollisionSolverPreFrame(*args, **kwargs):
    pass


def MAnimControl_playBackward(*args, **kwargs):
    pass


def MAnimUtil_findSetDrivenKeyAnimation(*args, **kwargs):
    pass


def MDynamicsUtil_inRunup(*args, **kwargs):
    pass


def MAnimControl_setPlaybackBy(*args, **kwargs):
    pass


def MAnimCurveClipboardItem_className(*args, **kwargs):
    pass


def MFnKeyframeDeltaBreakdown_className(*args, **kwargs):
    pass


def MFnSkinCluster_className(*args, **kwargs):
    pass


def isValidMDagPath(obj):
    pass


def MIkSystem_getSolvers(*args, **kwargs):
    pass


def MDynSweptLine_className(*args, **kwargs):
    pass


def MAnimControl_setAnimationEndTime(*args, **kwargs):
    pass


def MFnVortexField_swigregister(*args, **kwargs):
    pass


def MAnimControl_setCurrentTime(*args, **kwargs):
    pass


def MAnimMessage_swigregister(*args, **kwargs):
    pass


def MFnNIdData_swigregister(*args, **kwargs):
    pass


def MFnBlendShapeDeformer_swigregister(*args, **kwargs):
    pass


def MFnDynSweptGeometryData_className(*args, **kwargs):
    pass


def MItNodes(*args, **kwargs):
    """
    Iterator on MObjects of nodes of the specified types in the Maya scene,
    if a list of tyes is passed as args, then all nodes of a type included in the list will be iterated on,
    if no types are specified, all nodes of the scene will be iterated on
    the types are specified as Maya API types
    """

    pass


def MAnimControl_setPlaybackMode(*args, **kwargs):
    pass


def toApiObject(nodeName, dagPlugs='True'):
    """
    Get the API MPlug, MObject or (MObject, MComponent) tuple given the name
    of an existing node, attribute, components selection
    
    Parameters
    ----------
    dagPlugs : bool
        if True, plug result will be a tuple of type (MDagPath, MPlug)
    
    If we were unable to retrieve the node/attribute/etc, returns None
    """

    pass


def MFnKeyframeDeltaBlockAddRemove_swigregister(*args, **kwargs):
    pass


def MFnAnimCurve_className(*args, **kwargs):
    pass


def MAnimControl_setAnimationStartTime(*args, **kwargs):
    pass


def MFnIkSolver_className(*args, **kwargs):
    pass


def nameToMObject(*args):
    """
    Get the API MObjects given names of existing nodes
    """

    pass


def MFnSkinCluster_swigregister(*args, **kwargs):
    pass


def MItKeyframe_className(*args, **kwargs):
    pass


def MFnKeyframeDeltaScale_className(*args, **kwargs):
    pass


def MFnAnimCurve_swigregister(*args, **kwargs):
    pass


def MFnNewtonField_swigregister(*args, **kwargs):
    pass


def MFnLattice_swigregister(*args, **kwargs):
    pass


def MFnClip_className(*args, **kwargs):
    pass


def MFnPfxGeometry_swigregister(*args, **kwargs):
    pass


def MHairSystem_className(*args, **kwargs):
    pass


def MFnKeyframeDelta_swigregister(*args, **kwargs):
    pass


def MAnimControl_setMinMaxTime(*args, **kwargs):
    pass


def MAnimMessage_addAnimKeyframeEditCheckCallback(*args, **kwargs):
    pass


def isValidMObject(obj):
    pass


def MIkSystem_className(*args, **kwargs):
    pass


def MnRigid_swigregister(*args, **kwargs):
    pass


def MFnWeightGeometryFilter_className(*args, **kwargs):
    pass


def MFnNewtonField_className(*args, **kwargs):
    pass


def MFnKeyframeDeltaBlockAddRemove_className(*args, **kwargs):
    pass


def MFnCharacter_swigregister(*args, **kwargs):
    pass


def MFnPfxGeometry_className(*args, **kwargs):
    pass


def MHairSystem_getCollisionObject(*args, **kwargs):
    pass


def MFnKeyframeDelta_className(*args, **kwargs):
    pass


def MAnimUtil_findConstraint(*args, **kwargs):
    pass


def MDynamicsUtil_runupIfRequired(*args, **kwargs):
    pass


def MFnWeightGeometryFilter_swigregister(*args, **kwargs):
    pass


def MAnimControl_minTime(*args, **kwargs):
    pass


def MnCloth_swigregister(*args, **kwargs):
    pass


def MAnimCurveClipboardItem_swigregister(*args, **kwargs):
    pass


def MFnAirField_swigregister(*args, **kwargs):
    pass


def MAnimCurveClipboardItemArray_className(*args, **kwargs):
    pass


def MAnimControl_playForward(*args, **kwargs):
    pass


def MAnimMessage_addPostBakeResultsCallback(*args, **kwargs):
    pass


def MFnVolumeAxisField_className(*args, **kwargs):
    pass


def MIkSystem_isGlobalSnap(*args, **kwargs):
    pass


def MFnNIdData_className(*args, **kwargs):
    pass


def MAnimMessage_addDisableImplicitControlCallback(*args, **kwargs):
    pass


def MFnWireDeformer_swigregister(*args, **kwargs):
    pass


def MDynSweptLine_swigregister(*args, **kwargs):
    pass


def isValidMObjectHandle(obj):
    """
    # fast convenience tests on API objects
    """

    pass


def MAnimControl_setPlaybackSpeed(*args, **kwargs):
    pass


def MAnimControl_playbackSpeed(*args, **kwargs):
    pass


def MAnimUtil_isAnimated(*args, **kwargs):
    pass


def MAnimControl_setAutoKeyMode(*args, **kwargs):
    pass


def toComponentMObject(dagPath):
    """
    get an MObject representing all components of the passed dagPath
    
    The component type that will be returned depends on the exact type of
    object passed in - for instance, a poly mesh will return a component
    representing all the kMeshVertComponents.
    
    The exact choice of component type is determined by MItGeometry.
    """

    pass


def MAnimControl_viewMode(*args, **kwargs):
    pass


def MFnFluid_swigregister(*args, **kwargs):
    pass


def MFnMotionPath_swigregister(*args, **kwargs):
    pass


def MFnTurbulenceField_swigregister(*args, **kwargs):
    pass


def MFnKeyframeDeltaMove_className(*args, **kwargs):
    pass


def MIkHandleGroup_className(*args, **kwargs):
    pass


def MAnimUtil_findAnimation(*args, **kwargs):
    pass


def MFnIkHandle_className(*args, **kwargs):
    pass


def MFnIkHandle_swigregister(*args, **kwargs):
    pass


def MFnParticleSystem_swigregister(*args, **kwargs):
    pass


def MItDag(root='None', *args, **kwargs):
    """
    Iterate over the hierarchy under a root dag node, if root is None, will iterate on whole Maya scene
    If a list of types is provided, then only nodes of these types will be returned,
    if no type is provided all dag nodes under the root will be iterated on.
    Types are specified as Maya API types.
    The following keywords will affect order and behavior of traversal:
    breadth: if True nodes Mobjects will be returned as a breadth first traversal of the hierarchy tree,
             if False as a preorder (depth first)
             default is False (depth first)
    underworld: if True traversal will include a shape's underworld (dag object parented to the shape),
          if False underworld will not be traversed,
          default is False (do not traverse underworld )
    depth : if True will return depth of each node.
    prune : if True will stop the iteration on nodes than do not fit the types list,
            if False these nodes will be traversed but not returned
            default is False (do not prune)
    """

    pass


def MAnimMessage_className(*args, **kwargs):
    pass


def MFnIkJoint_className(*args, **kwargs):
    pass


def MItKeyframe_swigregister(*args, **kwargs):
    pass


def MFnKeyframeDeltaWeighted_className(*args, **kwargs):
    pass


def MAnimCurveClipboard_theAPIClipboard(*args, **kwargs):
    pass


def MFnInstancer_className(*args, **kwargs):
    pass


def MDynSweptTriangle_swigregister(*args, **kwargs):
    pass


def MAnimUtil_swigregister(*args, **kwargs):
    pass


def MDynamicsUtil_swigregister(*args, **kwargs):
    pass


def MFnFluid_className(*args, **kwargs):
    pass


def MAnimControl_animationStartTime(*args, **kwargs):
    pass


def MFnIkJoint_swigregister(*args, **kwargs):
    pass


def MHairSystem_swigregister(*args, **kwargs):
    pass


def MAnimControl_isPlaying(*args, **kwargs):
    pass


def MFnKeyframeDeltaMove_swigregister(*args, **kwargs):
    pass


def MFnKeyframeDeltaInfType_className(*args, **kwargs):
    pass


def MHairSystem_getFollicle(*args, **kwargs):
    pass


def MAnimControl_isScrubbing(*args, **kwargs):
    pass


def MAnimUtil_findAnimatablePlugs(*args, **kwargs):
    pass


def MDynamicsUtil_addNodeTypeToRunup(*args, **kwargs):
    pass


def MAnimControl_maxTime(*args, **kwargs):
    pass


def MFnHikEffector_swigregister(*args, **kwargs):
    pass


def MAnimMessage_addAnimCurveEditedCallback(*args, **kwargs):
    pass


def toMDagPath(nodeName):
    """
    Get an API MDagPAth to the node, given the name of an existing dag node
    """

    pass


def MFnKeyframeDeltaTangent_className(*args, **kwargs):
    pass


def MAnimCurveClipboardItemArray_swigregister(*args, **kwargs):
    pass


def MFnHikEffector_className(*args, **kwargs):
    pass


def MFnAirField_className(*args, **kwargs):
    pass


def MIkSystem_setGlobalSnap(*args, **kwargs):
    pass


def MAnimCurveClipboard_swigregister(*args, **kwargs):
    pass


def MFnLatticeDeformer_className(*args, **kwargs):
    pass


def MFnNObjectData_swigregister(*args, **kwargs):
    pass


def MAnimControl_swigregister(*args, **kwargs):
    pass


def MFnTurbulenceField_className(*args, **kwargs):
    pass


def MFnLattice_className(*args, **kwargs):
    pass


def MFnGravityField_swigregister(*args, **kwargs):
    pass


def MHairSystem_registerCollisionSolverPreFrame(*args, **kwargs):
    pass


def MHairSystem_registerCollisionSolverCollide(*args, **kwargs):
    pass


def MAnimUtil_findAnimatedPlugs(*args, **kwargs):
    pass


def MFnKeyframeDeltaWeighted_swigregister(*args, **kwargs):
    pass


def MAnimControl_setViewMode(*args, **kwargs):
    pass


def isValidMNode(obj):
    pass


def MFnGeometryFilter_swigregister(*args, **kwargs):
    pass


def MRenderLineArray_className(*args, **kwargs):
    pass


def MAnimMessage_addPreBakeResultsCallback(*args, **kwargs):
    pass


def MFnKeyframeDeltaAddRemove_swigregister(*args, **kwargs):
    pass


def MFnUniformField_swigregister(*args, **kwargs):
    pass


def MIkHandleGroup_swigregister(*args, **kwargs):
    pass


def MFnInstancer_swigregister(*args, **kwargs):
    pass


def MnObject_swigregister(*args, **kwargs):
    pass



