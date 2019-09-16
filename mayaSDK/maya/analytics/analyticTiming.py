"""
Gather basic scene timing information from the profiler,
with and without the invisibility evaluator active.
"""

from maya.analytics.decorators import makeAnalytic
from maya.debug.emModeManager import emModeManager
from maya.analytics.decorators import addHelp
from maya.analytics.BaseAnalytic import BaseAnalytic
from maya.analytics.decorators import addMethodDocs

class analyticTiming(BaseAnalytic):
    """
    Examine timing information for basic operations in different modes.
    The list of modes can be modified as needs change by altering the
    MODE_LIST value in the script.
    
    WARNING: Since this test gets timing for file-new you will lose your
             data if you run it on the current scene.
    
    It measures the following events for each of the modes, in microseconds. If
    multiple instances of the event are found then the last one found is used,
    under the assumption that the state is most steady by then.
    
        EvaluationGraphConstruction    : Graph build time
        EvaluationGraphPartitioning    : Graph partitioning time
        EvaluationGraphExecution       : Graph execution time
        Vp2SceneRender                 : Viewport 2 rendering time
        Vp1SceneRender                 : Legacy Viewport rendering time
        ClusterCount                   : Total number of custom evaluator clusters
        ClusterNodeCount               : Total number of nodes in custom evaluator clusters
        InvisibilityClusterCount       : Total number of invisibility clusters
        InvisibilityClusterNodeCount   : Total number of nodes in invisibility clusters
        InvisibilityCreateClusters     : Time taken by the invisibility evaluator to create its clusters
        InvisibilityDiscover           : Time taken by the invisibility evaluator to discover invisible nodes
        InvisibilityMarkNodes          : Time taken by the invisibility evaluator to mark its nodes
        InvisibilityCreatePartitioning : Time taken by the invisibility evaluator to create its partitions
    
    Note: InvisibilityCreateClusters is the parent of these three steps so don't add them:
        - InvisibilityDiscover
        - InvisibilityMarkNodes
        - InvisibilityCreatePartitioning
    
    and these, which are independent of the evaluator configuration:
        FileNew        : Time to empty the scene of the current file, in seconds
        CycleCount     : Total number of cycle clusters
        CycleNodeCount : Total number of nodes in cycle clusters
    
    Example output running in parallel mode both with and without the
    invisibility for a scene that uses VP2:
    
        "output" : {
            "emp-invisibility" : {
                "EvaluationGraphConstruction"    : 5632,
                "EvaluationGraphPartitioning"    : 392,
                "EvaluationGraphExecution"       : 2020211,
                "Vp2SceneRender"                 : 7152,
                "Vp1SceneRender"                 : 0,
                "ClusterCount"                   : 72,
                "ClusterNodeCount"               : 1230,
                "InvisibilityClusterCount"       : 0,
                "InvisibilityClusterNodeCount"   : 0,
                "InvisibilityDiscover"           : 0,
                "InvisibilityCreateClusters"     : 0,
                "InvisibilityMarkNodes"          : 0,
                "InvisibilityCreatePartitioning" : 0
            },
            "emp+invisibility" : {
                "EvaluationGraphConstruction"    : 7801,
                "EvaluationGraphPartitioning"    : 738,
                "EvaluationGraphExecution"       : 19374,
                "Vp2SceneRender"                 : 7326,
                "Vp1SceneRender"                 : 0,
                "ClusterCount"                   : 129,
                "ClusterNodeCount"               : 7183,
                "InvisibilityClusterCount"       : 11,
                "InvisibilityClusterNodeCount"   : 11,
                "InvisibilityDiscover"           : 12341,
                "InvisibilityCreateClusters"     : 123,
                "InvisibilityMarkNodes"          : 1110,
                "InvisibilityCreatePartitioning" : 84
            },
            "CycleCount"     : 3,
            "CycleNodeCount" : 14,
            "FileNew"        : 4.19238
        }
    """
    
    
    
    def run(self):
        """
        Run the analytic on the current scene.
        :return: JSON results as described in the class doc
        """
    
        pass
    
    
    def help():
        """
        Call this method to print the class documentation, including all methods.
        """
    
        pass
    
    
    ANALYTIC_DESCRIPTION_DETAILED = 'Examine timing information for basic operations in different modes.\nThe list of modes can be modified as needs change by altering the\nMODE_LIST value in the script.\n\nWARNING: Since this test gets timing for file-new you will lose your\n         data if you run it on the current scene.\n\nIt measures the following events for each of the modes, in microseconds. If\nmultiple instances of the event are found then the last one found is used,\nunder the assumption that the state is most steady by then.\n\n    EvaluationGraphConstruction    : Graph build time\n    EvaluationGraphPartitioning    : Graph partitioning time\n    EvaluationGraphExecution       : Graph execution time\n    Vp2SceneRender                 : Viewport 2 rendering time\n    Vp1SceneRender                 : Legacy Viewport rendering time\n    ClusterCount                   : Total number of custom evaluator clusters\n    ClusterNodeCount               : Total number of nodes in custom evaluator clusters\n    InvisibilityClusterCount       : Total number of invisibility clusters\n    InvisibilityClusterNodeCount   : Total number of nodes in invisibility clusters\n    InvisibilityCreateClusters     : Time taken by the invisibility evaluator to create its clusters\n    InvisibilityDiscover           : Time taken by the invisibility evaluator to discover invisible nodes\n    InvisibilityMarkNodes          : Time taken by the invisibility evaluator to mark its nodes\n    InvisibilityCreatePartitioning : Time taken by the invisibility evaluator to create its partitions\n\nNote: InvisibilityCreateClusters is the parent of these three steps so don\'t add them:\n    - InvisibilityDiscover\n    - InvisibilityMarkNodes\n    - InvisibilityCreatePartitioning\n\nand these, which are independent of the evaluator configuration:\n    FileNew        : Time to empty the scene of the current file, in seconds\n    CycleCount     : Total number of cycle clusters\n    CycleNodeCount : Total number of nodes in cycle clusters\n\nExample output running in parallel mode both with and without the\ninvisibility for a scene that uses VP2:\n\n    "output" : {\n        "emp-invisibility" : {\n            "EvaluationGraphConstruction"    : 5632,\n            "EvaluationGraphPartitioning"    : 392,\n            "EvaluationGraphExecution"       : 2020211,\n            "Vp2SceneRender"                 : 7152,\n            "Vp1SceneRender"                 : 0,\n            "ClusterCount"                   : 72,\n            "ClusterNodeCount"               : 1230,\n            "InvisibilityClusterCount"       : 0,\n            "InvisibilityClusterNodeCount"   : 0,\n            "InvisibilityDiscover"           : 0,\n            "InvisibilityCreateClusters"     : 0,\n            "InvisibilityMarkNodes"          : 0,\n            "InvisibilityCreatePartitioning" : 0\n        },\n        "emp+invisibility" : {\n            "EvaluationGraphConstruction"    : 7801,\n            "EvaluationGraphPartitioning"    : 738,\n            "EvaluationGraphExecution"       : 19374,\n            "Vp2SceneRender"                 : 7326,\n            "Vp1SceneRender"                 : 0,\n            "ClusterCount"                   : 129,\n            "ClusterNodeCount"               : 7183,\n            "InvisibilityClusterCount"       : 11,\n            "InvisibilityClusterNodeCount"   : 11,\n            "InvisibilityDiscover"           : 12341,\n            "InvisibilityCreateClusters"     : 123,\n            "InvisibilityMarkNodes"          : 1110,\n            "InvisibilityCreatePartitioning" : 84\n        },\n        "CycleCount"     : 3,\n        "CycleNodeCount" : 14,\n        "FileNew"        : 4.19238\n    }'
    
    
    ANALYTIC_DESCRIPTION_SHORT = []
    
    
    ANALYTIC_LABEL = []
    
    
    ANALYTIC_NAME = 'Timing'
    
    
    __fulldocs__ = 'Examine timing information for basic operations in different modes.\nThe list of modes can be modified as needs change by altering the\nMODE_LIST value in the script.\n\nWARNING: Since this test gets timing for file-new you will lose your\n         data if you run it on the current scene.\n\nIt measures the following events for each of the modes, in microseconds. If\nmultiple instances of the event are found then the last one found is used,\nunder the assumption that the state is most steady by then.\n\n    EvaluationGraphConstruction    : Graph build time\n    EvaluationGraphPartitioning    : Graph partitioning time\n    EvaluationGraphExecution       : Graph execution time\n    Vp2SceneRender                 : Viewport 2 rendering time\n    Vp1SceneRender                 : Legacy Viewport rendering time\n    ClusterCount                   : Total number of custom evaluator clusters\n    ClusterNodeCount               : Total number of nodes in custom evaluator clusters\n    InvisibilityClusterCount       : Total number of invisibility clusters\n    InvisibilityClusterNodeCount   : Total number of nodes in invisibility clusters\n    InvisibilityCreateClusters     : Time taken by the invisibility evaluator to create its clusters\n    InvisibilityDiscover           : Time taken by the invisibility evaluator to discover invisible nodes\n    InvisibilityMarkNodes          : Time taken by the invisibility evaluator to mark its nodes\n    InvisibilityCreatePartitioning : Time taken by the invisibility evaluator to create its partitions\n\nNote: InvisibilityCreateClusters is the parent of these three steps so don\'t add them:\n    - InvisibilityDiscover\n    - InvisibilityMarkNodes\n    - InvisibilityCreatePartitioning\n\nand these, which are independent of the evaluator configuration:\n    FileNew        : Time to empty the scene of the current file, in seconds\n    CycleCount     : Total number of cycle clusters\n    CycleNodeCount : Total number of nodes in cycle clusters\n\nExample output running in parallel mode both with and without the\ninvisibility for a scene that uses VP2:\n\n    "output" : {\n        "emp-invisibility" : {\n            "EvaluationGraphConstruction"    : 5632,\n            "EvaluationGraphPartitioning"    : 392,\n            "EvaluationGraphExecution"       : 2020211,\n            "Vp2SceneRender"                 : 7152,\n            "Vp1SceneRender"                 : 0,\n            "ClusterCount"                   : 72,\n            "ClusterNodeCount"               : 1230,\n            "InvisibilityClusterCount"       : 0,\n            "InvisibilityClusterNodeCount"   : 0,\n            "InvisibilityDiscover"           : 0,\n            "InvisibilityCreateClusters"     : 0,\n            "InvisibilityMarkNodes"          : 0,\n            "InvisibilityCreatePartitioning" : 0\n        },\n        "emp+invisibility" : {\n            "EvaluationGraphConstruction"    : 7801,\n            "EvaluationGraphPartitioning"    : 738,\n            "EvaluationGraphExecution"       : 19374,\n            "Vp2SceneRender"                 : 7326,\n            "Vp1SceneRender"                 : 0,\n            "ClusterCount"                   : 129,\n            "ClusterNodeCount"               : 7183,\n            "InvisibilityClusterCount"       : 11,\n            "InvisibilityClusterNodeCount"   : 11,\n            "InvisibilityDiscover"           : 12341,\n            "InvisibilityCreateClusters"     : 123,\n            "InvisibilityMarkNodes"          : 1110,\n            "InvisibilityCreatePartitioning" : 84\n        },\n        "CycleCount"     : 3,\n        "CycleNodeCount" : 14,\n        "FileNew"        : 4.19238\n    }\nBase class for output for analytics.\n\nThe default location for the anlaytic output is in a subdirectory\ncalled \'MayaAnalytics\' in your temp directory. You can change that\nat any time by calling set_output_directory().\n\nClass static member:\n     ANALYTIC_NAME : Name of the analytic\n\nClass members:\n     directory     : Directory the output will go to\n     is_static     : True means this analytic doesn\'t require a file to run\n     logger        : Logging object for errors, warnings, and messages\n     plug_namer    : Object creating plug names, possibly anonymous\n     node_namer    : Object creating node names, possibly anonymous\n     csv_output    : Location to store legacy CSV output\n     plug_namer    : Set by option \'anonymous\' - if True then make plug names anonymous\n     node_namer    : Set by option \'anonymous\' - if True then make node names anonymous\n     __options     : Dictionary of per-analytic options\n\n\tMethods\n\t-------\n\tdebug : Utility to standardize debug messages coming from analytics.\n\n\terror : Utility to standardize errors coming from analytics.\n\n\testablish_baseline : This is run on an empty scene, to give the analytic a chance to\n\t                     establish any baseline data it might need (e.g. the nodes in an\n\t                     empty scene could all be ignored by the analytic)\n\t                     \n\t                     Base implementation does nothing. Derived classes should call\n\t                     their super() method though, in case something does get added.\n\n\thelp : Call this method to print the class documentation, including all methods.\n\n\tjson_file : Although an analytic is free to create any set of output files it\n\t            wishes there will always be one master JSON file containing the\n\n\tlog : Utility to standardize logging messages coming from analytics.\n\n\tmarker_file : Returns the name of the marker file used to indicate that the\n\t              computation of an analytic is in progress. If this file remains\n\t              in a directory after the analytic has run that means it was\n\t              interrupted and the data is not up to date.\n\t              \n\t              This file provides a safety measure against machines going down\n\t              or analytics crashing.\n\n\tname : Get the name of this type of analytic\n\n\toption : Return TRUE if the option specified has been set on this analytic.\n\t         option: Name of option to check\n\n\toutput_files : This is used to get the list of files the analytic will generate.\n\t               There will always be a JSON file generated which contains at minimum\n\t               the timing information. An analytic should override this method only\n\t               if they are adding more output files (e.g. a .jpg file).\n\t               \n\t               This should only be called after the final directory has been set.\n\n\trun : Run the analytic on the current scene.\n\t      :return: JSON results as described in the class doc\n\n\tset_options : Modify the settings controlling the run operation of the analytic.\n\t              Override this method if your analytic has some different options\n\t              available to it, but be sure to call this parent version after since\n\t              it sets common options.\n\n\tset_output_directory : Call this method to set a specific directory as the output location.\n\t                       The special names \'stdout\' and \'stderr\' are recognized as the\n\t                       output and error streams respectively rather than a directory.\n\n\twarning : Utility to standardize warnings coming from analytics.\n'
    
    
    is_static = False



kAnalyticLabel = []

kAnalyticDescriptionShort = []

MODE_LIST = []


