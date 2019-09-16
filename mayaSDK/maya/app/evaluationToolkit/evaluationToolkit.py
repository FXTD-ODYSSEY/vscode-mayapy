"""
This module contains the UI code for the Evaluation Toolkit.

It also holds several utility methods that are used by the tool.

import maya.app.evaluationToolkit.evaluationToolkit as et
et.OpenEvaluationToolkitUI()
"""

from maya.debug.TODO import TODO
from maya.debug.frozenUtilities import unfreeze_nodes
from maya.debug.frozenUtilities import FrozenOptionsManager
from maya.debug.frozenUtilities import list_frozen_in_scheduling
from functools import partial
from maya.debug.emCorrectnessTest import emCorrectnessTest
from functools import wraps
from maya.debug.frozenUtilities import freeze_nodes
from maya.debug.emModeManager import emModeManager
from maya.debug.frozenUtilities import list_frozen
from maya.common.ui import showMessageBox
from maya.common.ui import scrollableMessageBox
from maya.common.ui import LayoutManager
from maya.debug.emPerformanceTest import emPerformanceOptions
from maya.debug.emPerformanceTest import emPerformanceTest
from maya.debug.cacheCorrectnessTest import cacheCorrectnessTest

class EvaluationToolkit(object):
    """
    This is the main UI class for the Evaluation Toolkit.
    
    It handles creation of the UI and provides various callbacks to handle
    user interactions.
    """
    
    
    
    def __init__(self, windowName="'evaluationToolkitWindowId'"):
        """
        Simple constructor.
        
        It does not create the UI.  UI creation is deferred until create() is
        called
        """
    
        pass
    
    
    def create(self):
        """
        This method completely builds the UI.  It shows the resulting window
        when it is fully created.
        """
    
        pass
    
    
    def updateUI(self):
        """
        This method performs a full UI refresh.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class dotFormatting(object):
    """
    Helper class to provide DOT language output support.
    """
    
    
    
    def __init__(self):
        """
        Initialize the allowed cluster color list and current color index.
        """
    
        pass
    
    
    def subgraphHeader(self, label):
        """
        Create a DOT subgraph with the given format information
        """
    
        pass
    
    
    def colorFormat(color):
        """
        Returns a string with DOT formatting information for a colored shape
        """
    
        pass
    
    
    def connection(srcNode, dstNode, connectionFormat="''", indent='1'):
        """
        Mark a connection between two DOT nodes
        """
    
        pass
    
    
    def ellipseFormat():
        """
        Returns a string with DOT formatting information for a simple ellipse shape
        """
    
        pass
    
    
    def filledFormat(color='(0.0, 0.5, 1.0)'):
        """
        Returns a string with DOT formatting information for a simple filled greenish-blue shape
        """
    
        pass
    
    
    def footer():
        """
        Closes out the body section
        """
    
        pass
    
    
    def header():
        """
        Print out a header defining the basic sizing information
        """
    
        pass
    
    
    def node(node, nodeFormat="''", indent='1'):
        """
        Creates a DOT node with the given format information
        """
    
        pass
    
    
    def subgraphFooter():
        """
        Close out the subgraph section
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def getEvaluationGraph(attributes, allObjects='False'):
    """
    Get the evaluation graph, if any.
    
        attributes: Attributes to retrieve from the evaluation graph.
                    Can be 'nodes', 'plugs', 'connections' or a list of those.
                    See the documentation for graph operator in dbpeek command.
        allObjects: True to force to get all objects instead of selection.
    """

    pass


def printDeformerClusters():
    """
    Print out any clusters of nodes captured by the deformer evaluator.
    """

    pass


def processDynamicExtraConnections(nodes, disconnect):
    """
    Returns the connections corresponding to dynamic attributes (first element
    of the returned tuple) along with a list of skipped attributes not to be
    disconnected (second element of the returned tuple).
    """

    pass


def setCacheHUDActive(state):
    """
    This method activates or deactivates the cache HUD.
    """

    pass


def callback_13_UpdateMemoryManagement(tool):
    pass


def callback_09_GetContextMonitorDetails(tool):
    """
    Callback function to get the detailed results from the context monitor
    """

    pass


def isGPUOverrideActive():
    """
    This method returns True if the OpenCL evaluator is active, False
    otherwise.
    """

    pass


def setTraceActive(trace, state):
    """
    This method activates or deactivates the given trace.
    """

    pass


def runCacheTestDBM(verbose):
    """
    Run the caching test using Datablock Transform and Mesh caching
    :param verbose: True means add more detail to the output
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def require_evaluation_graph(func):
    """
    This decorator makes sure that the given function will have a valid
    evaluation graph.
    """

    pass


def getGraphvizCommand(commandName, useSystemGraphviz):
    """
    Build a string for the Graphviz command to run.
    """

    pass


def callback_03_UpdateTraceEnable(tool, trace):
    pass


def callback_03_UpdateTraceOutput(tool, trace):
    pass


def callback_03_LaunchAnalyticsWindow(tool):
    pass


def callback_08_RefreshCycleClusters(*args, **kwargs):
    pass


def callback_03_SelectMinimalScene(*args, **kwargs):
    pass


def runGraphvizCommand(commandArgv, stdin='None', stdout='None'):
    """
    Run a Graphviz command and handle errors.
    """

    pass


def callback_11_UnfreezeAllFrozenNodes(tool):
    """
    Print frozen nodes in the scene
    """

    pass


def runEMCorrectnessTest():
    """
    Run the emCorrectnessTest on the current scene. The resulting
    output will be shown in the script editor window.
    """

    pass


def dumpDependenciesBetweenToDot(fileName, upstreamNodes, downstreamNodes):
    """
    Take all the dependencies between a set of upstream nodes and downstream
    nodes and dump them out in a DOT graph format to the named file.
    
        fileName        : Name of output file
        upstreamNodes   : Set of upstream nodes in the evaluation graph
        downstreamNodes : Set of downstream nodes in the evaluation graph
    """

    pass


def callback_08_GenerateCycleGraph(*args, **kwargs):
    pass


def callback_09_RunCacheCorrectnessTest(tool, test_type):
    """
    Called when the user clicks on one of the buttons that runs the cache correctness tests
    """

    pass


def callback_scriptJob_customEvaluatorChanged(tool):
    """
    Update the UI since the list or state of custom evaluators may have changed
    """

    pass


def callback_01_UpdateControllerPrepopulate(tool):
    pass


def callback_09_ResetContextMonitor(tool):
    """
    Callback when the context monitor error count reset button is pressed
    """

    pass


def setEvaluationHUDActive(state):
    """
    This method activates or deactivates the evaluation HUD.
    """

    pass


def isControllerPrepopulateActive():
    """
    This method returns True if the controllers are set to prepopulate the
    graph, False otherwise.
    """

    pass


def getSchedulingTypeOverride(nodeType):
    """
    Return a string describing the scheduling type override for this node type.
    """

    pass


def callback_01_UpdateManipulation(tool):
    pass


def setEvaluatorActive(evaluator, state):
    """
    This method activates or deactivates the given evaluator.
    """

    pass


def callback_11_PrintFrozenNodes(tool):
    """
    Print frozen nodes in the scene
    """

    pass


def runCacheTestDBTM(verbose):
    """
    Run the caching test using Datablock Transform and Mesh caching
    :param verbose: True means add more detail to the output
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def printReportExpressions():
    """
    This method prints a report about expression nodes in the scene.
    """

    pass


def setGPUOverrideActive(state):
    """
    This method activates or deactivates the OpenCL evaluator.
    """

    pass


def callback_03_PrintDirtyPlugs(*args, **kwargs):
    pass


def callback_03_LaunchProfiler(tool):
    pass


def callback_09_UpdateContextMonitor(tool):
    """
    Callback when the context monitor update count button is pressed
    """

    pass


def callback_06_PrintSelected(*args, **kwargs):
    pass


def runEMPerformanceTest():
    """
    Run the emPerformanceTest on the current scene. The resulting
    output will be shown in the script editor window.
    
    The raw performance data consists of two rows, the first containing the
    names of the data collected and the second consisting of the values
    for each data collection item.
    
    This raw list is filtered so that only the most useful data is shown.
    This includes the frames per second for playback in each of DG, EMS,
    and EMP modes. For the unfiltered results see the emPerformanceTest
    script.
    """

    pass


def callback_13_UpdateMemory(tool):
    pass


def callback_09_ShowCacheTestDetails(tool, test_type):
    """
    Called when the user clicks the info button to show cache correctness test details
    """

    pass


def callback_12_SetSchedulingForTypes(tool):
    pass


def getCustomEvaluatorClusters(evaluator):
    """
    Get the clusters for a given custom evaluator, if any.
    """

    pass


def callback_12_SetSchedulingForTypesOfNodes(tool):
    pass


def callback_11_UpdateFreezeInvisibleDisplayLayers(tool):
    """
    Update the freeze invisible display layer option to match the new value
    """

    pass


def isManipulationActive():
    """
    This method returns True if the evaluation manager is used for
    manipulation, False otherwise.
    """

    pass


def nonVP2ViewportExists():
    """
    Return True if a viewport that does not use Viewport 2.0 exists.
    """

    pass


def printNodesAndConnections(print_all):
    """
    Scan selected nodes or the entire evaluation graph if none selected
    and print out the list of all evaluation nodes and the connections
    they have within the evaluation graph.
    
    Print a more compact output than the raw JSON provides.
    
    print_all: If set ignore the selection list and dump all plugs
    """

    pass


def isEvaluatorActive(evaluatorName):
    """
    This method returns True if the given evaluator is active, False otherwise.
    """

    pass


def callback_scriptJob_freezeOptionsChanged(tool):
    """
    Update the UI since the state of freeze options may have changed
    """

    pass


def setFrameRateHUDActive(state):
    """
    This method activates or deactivates the frame rate HUD.
    """

    pass


def runCacheTestVP2M(verbose):
    """
    Run the caching test using VP2 Transform and Mesh caching
    :param verbose: True means add more detail to the output
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def callback_05_UpdateDynamicsOptions(tool, option):
    pass


def callback_07_SelectNodesUnderEvaluationManagerControl(*args, **kwargs):
    pass


def getUpstreamSet_Fast(startingNodes):
    pass


def callback_13_FlushCache(tool):
    pass


def convertDOTtoPDF(inputDotFileName, outputDotFileName, transitiveReduction, useSystemGraphviz):
    """
    Convert a DOT file to PDF using Graphviz.
    """

    pass


def updateUI_01_Mode(self):
    pass


def callback_10_RunReports(tool):
    pass


def callback_08_SelectNodes(tool, textScrollList):
    pass


def callback_02_UpdateEvaluationHUD(tool):
    pass


def callback_09_UpdateContextMonitorOutput(tool):
    """
    Callback when the output folder for the context monitor changes.
    Since the context monitor is actively using the output it has to
    be disabled first, if necessary, then re-enabled with the new output.
    If not enabled then nothing is done yet.
    """

    pass


def callback_scriptJob_dbTraceChanged(tool):
    """
    Update the UI since the list or state of available trace objects may have changed
    """

    pass


def callback_07_SelectDownStreamNodes(*args, **kwargs):
    pass


def callback_13_UpdateHybridGPUCache(tool):
    pass


def isCacheHUDActive():
    """
    This method returns True if the cache HUD is active, False otherwise.
    """

    pass


def setCacheMode(mode):
    """
    Configure cache evaluator and its caching point according to the given
    cache mode description.
    
    The mode parameter is an object matching the description from getCacheMode().
    """

    pass


def updateUI_04_CustomEvaluators(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def callback_02_UpdateCacheHUD(tool):
    pass


def updateUI_03_Debugging(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def get_default_directory():
    """
    Get a reasonable default directory for temporary output.
    """

    pass


def setEvaluationManagerMode(mode):
    """
    This method sets the current evaluation mode.
    """

    pass


def callback_11_UpdateFreezeExplicitPropagation(tool):
    """
    Update the freeze explicit propagation option to match the new value
    """

    pass


def callback_09_RunPerformanceTest(tool):
    pass


def runCacheTestVP2TM(verbose):
    """
    Run the caching test using VP2 Transform and Mesh caching
    :param verbose: True means add more detail to the output
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def getMinimalSceneObjectsFrom(input_side):
    pass


def updateUI_11_FreezeOptions(self):
    """
    Update the UI configuration for the freeze options based on current state
    """

    pass


def printDirtyPlugs(print_all):
    """
    Scan selected nodes or the entire evaluation graph if none selected
    and print out the list of all evaluation nodes and the dirty plugs
    they are controlling.
    
    Print a more compact output than the raw JSON provides.
    
    print_all: If set ignore the selection list and dump all plugs
    """

    pass


def callback_03_PrintExtraConnections(*args, **kwargs):
    pass


def getShortestPaths(nodes, startNode, endNode='None'):
    """
    Return a dictionary which associates each node with its previous node in the shortest path from startNode.
    
    If endNode is specified, the algorithm will stop when the shortest path to endNode is found.
    Then the dictionary is only guaranteed to hold nodes on this path.
    
        nodes     : the list of allowed nodes in which the search can be performed.
        startNode : the node from which to start looking for the shortest path.
        endNode   : the node for which to stop the search, or None to search for all nodes.
    """

    pass


def dumpEvaluationGraphToDot(fileName):
    """
    Take all of the nodes in the evaluation graph and dump them out in
    a DOT graph format to the named file.
    
        fileName : Name of output file
    """

    pass


def runCacheTestBGCISA(verbose):
    """
    Run the Background Context Isolation test for Static and Animated data.
    :param verbose: True means add more detail to the output
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def callback_08_GenerateFullGraph(*args, **kwargs):
    pass


def callback_scriptJob_uiDeleted(tool):
    """
    Remove all of the scriptJobs being used by this window
    """

    pass


def callback_01_UpdateGPUOverride(tool):
    pass


def getEvaluationManagerNodes():
    """
    Get the nodes under evaluation manager control.
    """

    pass


def selectNodesUnderEvaluationManagerControl():
    """
    Scan the entire evaluation graph and select all DG nodes appearing in it.
    """

    pass


def runCacheTestBGCIAN(verbose):
    """
    Run the Background Context Isolation test for Animated Nodes.
    :param verbose: True means add more detail to the output
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def updateUI_08_Cycles(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def isEvaluationHUDActive():
    """
    This method returns True if the evaluation HUD is active, False otherwise.
    """

    pass


def callback_05_UpdateDynamicsMode(tool):
    pass


def callback_CFG_PrintGraphvizVersion(tool):
    pass


def expandToShapes(inputList):
    pass


def callback_04_PrintEvaluatorInfo(tool, evaluator):
    pass


def clear_09_Validation(tool):
    """
    Clear out all of the current results; should only happen when a new file is loaded
    """

    pass


def callback_03_RemoveAllButMinimalScene(tool):
    """
    # No need to mark this one "@require_evaluation_graph"
    # because its first task is to call another callback that does.
    """

    pass


def openFile(fileName):
    """
    Open up an output file with the application assigned to it by the OS.
    
        fileName : File to be opened up (usually a PDF)
    """

    pass


def callback_13_RebuildCache(*args, **kwargs):
    pass


def setSchedulingTypeOverride(nodeType, schedulingInfo):
    """
    Set the scheduling type override of the given node type.
    
    The scheduling info is an array of flags for scheduling type to set to true.
    """

    pass


def callback_04_PrintEvaluatorConfiguration(tool, evaluator):
    pass


def callback_09_ChooseContextMonitorOutput(tool):
    """
    Callback when the output folder browser button is hit. If not canceled
    then the context monitor is disabled, then re-enabled with the new
    file selected as output.
    """

    pass


def callback_03_PrintNodesAndConnections(*args, **kwargs):
    pass


def printScheduling(verbose, print_as_pdf, print_all, use_system_graphviz):
    """
    Scan selected nodes or the entire evaluation graph if none selected
    and print out the list of all evaluation nodes and the connections
    they have within the evaluation graph.
    
    verbose:             True means expand clusters
    print_as_pdf:        If True then dump a .dot format and convert to PDF,
                         otherwise dump the JSON format to the script editor
    print_all:           True means dump the entire graph, else only the part
                         related to selected nodes.
    use_system_graphviz: True means don't use a path to find Graphviz
    """

    pass


def callback_12_PrintSchedulingForTypesOfNodes(tool):
    pass


def updateUI_05_Dynamics(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def callback_11_UpdateFreezeInvisibleNodes(tool):
    """
    Update the freeze invisible option to match the new value
    """

    pass


def callback_scriptJob_deleteAll(tool):
    """
    Update the UI since all objects have been deleted
    """

    pass


def callback_09_GetTestDetails(tool, test_type):
    """
    Callback function to get the detailed contents of the test output
    """

    pass


def getCycleClusters(nodes):
    """
    Get the clusters for cycles, if any.
    
        nodes: Nodes to test for cycles
    """

    pass


def selectNextNodes(upstream='True'):
    """
    Select all nodes upstream or downstream from the current selection that are
    currently under evaluation manager control.
    """

    pass


def callback_04_ShowHelpEvaluator(tool, evaluator):
    pass


def isFrameRateHUDActive():
    """
    This method returns True if the frame rate HUD is active, False otherwise.
    """

    pass


def runCacheTestBGCIAA(verbose):
    """
    Run the Background Context Isolation test for Animated Attributes.
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def setControllerPrepopulateActive(state):
    """
    This method activates or deactivates the controller prepopulation of the
    graph.
    """

    pass


def getCacheOption(types, option):
    """
    Return a list of 0 or 1 values describing cache state for the
    given type and option.
    
    1 is returned if evaluation cache is active, 0 otherwise.
    """

    pass


def callback_08_SelectNode(tool, textfield):
    pass


def updateUI_13_Caching(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def callback_09_RunCorrectnessTest(tool):
    pass


def getEvaluationManagerMode():
    """
    This method returns the current evaluation manager mode.
    """

    pass


def callback_03_ShowHelpTrace(tool, trace):
    pass


def callback_13_UpdateCacheMode(tool):
    pass


def getReports():
    """
    Return a list of reports.
    """

    pass


def callback_12_PrintSchedulingForTypes(tool):
    pass


def updateUI_07_Selection(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def updateUI_00_Viewport(self):
    pass


def callback_13_PrintSafeModeMessages(tool):
    pass


def callback_09_ShowContextMonitorResults(tool):
    """
    Callback when the context monitor Details button is pressed
    """

    pass


def callback_11_UpdateFreezeRuntimePropagation(tool):
    """
    Update the freeze runtime propagation option to match the new value
    """

    pass


def callback_06_PrintChains(*args, **kwargs):
    pass


def OpenEvaluationToolkitUI():
    """
    This method is the entry point of the Evaluation Toolkit.
    
    It creates the Evaluation Toolkit window and brings it up.
    """

    pass


def updateUI_10_Reports(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def callback_12_RefreshNodeTypes(tool):
    pass


def updateUI_06_GPUOverride(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def getCycleCluster(name):
    """
    Find the cycle cluster a node is involved in, if any.
    
        name: Name of node to check
    """

    pass


def callback_08_GenerateDependenciesGraph(*args, **kwargs):
    pass


def getAllCustomEvaluatorsClusters():
    """
    Get the clusters for all custom evaluators, if any.
    """

    pass


def getShortestPath(nodes, startNode, endNode):
    """
    Return the chain of nodes forming the shortest path between two nodes.
    
        nodes     : the list of allowed nodes in which the search can be performed.
        startNode : the node from which to start looking for the shortest path.
        endNode   : the node to which the shortest path must go.
    """

    pass


def expandToUpstreamHierarchy(inputList):
    """
    # The following methods are used to get the minimal dependencies.
    """

    pass


def isTraceActive(trace):
    """
    This method returns True if the given trace is active, False otherwise.
    """

    pass


def callback_11_UpdateUpstreamFreezeMode(tool):
    """
    Update the upstream freeze option to match the new value
    """

    pass


def setManipulationActive(state):
    """
    This method activates or deactivates manipulation using the evaluation
    manager.
    """

    pass


def getCacheMode():
    """
    Return an object representing the current caching mode.
    
    The object is a list of boolean values:
    - First one is True if 'transform' nodes are cached.
    - Second one is True if 'mesh' nodes are cached.
    - Third one is True if 'nurbsCurve' nodes are cached.
    - Fourth one is True if 'bezierCurve' nodes are cached.
    - Fifth one is True if 'nurbsSurface' nodes are cached.
    - Sixth one is True if 'subdiv' nodes are cached.
    - Seventh one is True if 'lattice' nodes are cached.
    - Eighth one is True if 'baseLattice' nodes are cached.
    - Ninth one is True if 'locator' nodes are cached.
    - Tenth one is True if VP2 format is used.
    - Eleventh one is True if VP2 cache is in hardware mode.
    
    If caching is disabled (i.e. the cache evaluator is not loaded, if it is
    not loaded or if no node type is enabled for caching), None is returned.
    """

    pass


def runCacheTestBGCC(verbose):
    """
    Run the Background cache correctness test
    :param verbose: True means add more detail to the output
    :return: a tuple with the number of errors found and the JSON error details
    """

    pass


def getGraphvizVersion(useSystemGraphviz):
    """
    Return the output of "dot -V" command.
    """

    pass


def updateUI_09_Validation(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def callback_06_PrintDeformerClusters(*args, **kwargs):
    pass


def callback_12_PrintSchedulingUsedForNodes(*args, **kwargs):
    pass


def callback_13_InvalidateCache(tool):
    pass


def callback_11_UpdateDownstreamFreezeMode(tool):
    """
    Update the downstream freeze option to match the new value
    """

    pass


def callback_09_UpdateContextMonitorState(tool):
    """
    Update the context monitor state based on the current settings
    """

    pass


def updateUI_12_Scheduling(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def callback_11_SelectFrozenNodes(tool):
    """
    Select frozen nodes in the scene
    """

    pass


def callback_06_PrintMeshes(*args, **kwargs):
    pass


def dumpClusterToDot(fileName, nodesInCycle, nodesToMark, shortestPathInfo):
    """
    Take all of the nodes in a cycle cluster and dump them out in
    a DOT graph format to the named file.
    
        nodesInCycle     : List of the nodes involved in the cycle
        fileName         : Name of output file
        shortestPathInfo : A tuple with a source and destination node between
                           which to highlight the shortest path, or None not
                           to highlight.
                           The first element of the tuple is a (source,
                           destination) node pair; the second element is a
                           boolean to indicate if only the shortest path should
                           be in the graph.
    """

    pass


def callback_03_RemoveExtraConnections(*args, **kwargs):
    pass


def convertExceptionToUnicode(exception):
    """
    Return a string representing the exception, in Unicode format.
    
    It handles cases such as when WindowsError exceptions contain Unicode
    characters encoded in a regular string in the OS encoding.  It does
    so in a slightly more generic and robust way by also trying the
    system's locale encoding.
    """

    pass


def updateUI_02_HUD(self):
    """
    # ----------------------------------------------------------------------
    """

    pass


def callback_02_UpdateFrameRateHUD(tool):
    pass


def callback_04_setEvaluatorActive(tool, evaluator, state):
    pass


def callback_03_PrintScheduling(*args, **kwargs):
    pass


def callback_01_UpdateEvaluationMode(tool):
    pass


def callback_07_SelectUpStreamNodes(*args, **kwargs):
    pass



kCSpacing = 10

kRemoveLabel = []

kShowLabel = []

kTestNotRun = []

kPrintLabel = []

kFileTextFieldWidth = 150

kVP2CachableNodeTypes = []

kDynamicsModes = []

kGroupLabelWidth = 140

kCacheModesSupportedCount = 4

kDebuggingTraces = []

kCacheModes = []

kFrameMarginWidth = 25

kActionOptions = []

kSetLabel = []

kPerformanceModeNames = []

kOptionVarResourceGuardMode = 'kResourceGuardMode'

kSchedulingTypes = []

kFreezeUpstreamModes = []

kFrameParamClosed = {}

kEvaluationManagerModes = []

kButtonWidth = 100

kCacheCorrectnessTests = []

kSelectLabel = []

kUseVerboseCorrectnessTests = False

kCachableNodeTypes = []

kRunLabel = []

kFreezeDownstreamModes = []

kDynamicsOptions = []

kOptionVarVirtualMemoryThreshold = 'kResourceGuardVirtualMemoryThreshold'

kCorrectnessModeNames = {}

kNodeOptions = []

kFrameParam = {}

kGenerateLabel = []

kProcessTypes = []

kOpenLabel = []


