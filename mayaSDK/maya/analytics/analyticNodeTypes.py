from maya.analytics.decorators import makeAnalytic
from maya.analytics.dg_utilities import node_type_hierarchy_list
from maya.analytics.dg_utilities import node_level_connections
from maya.analytics.dg_utilities import default_nodes_and_connections
from maya.analytics.decorators import addHelp
from maya.analytics.BaseAnalytic import BaseAnalytic
from maya.analytics.decorators import addMethodDocs

class analyticNodeTypes(BaseAnalytic):
    """
    This analytic collects the number of each node type in the scene.
    
    All of the persistent and default nodes are skipped unless they have a new
    connection. The way these two things are measured is different by necessity
    for the cases of analyzing a file that is read and analyzing the current scene.
    
    If the file is being read:
        - persistent and default nodes are defined as any node present before the
          file is loaded
        - exceptions are made if a new connection is formed to a persistent or
          default node after the file is loaded
    
    If the current scene is used:
        - persistent and default nodes are taken to be those marked as such by the
          Maya 'ls' command. This won't include any special persistent nodes
          created after-the-fact, such as those a newly loaded plug-in might create.
        - exceptions are made if there is any connection at all to these default
          or persistent nodes to a scene node.
    
    If the 'summary' option is used then the output includes a dictionary
    consisting of NODE_TYPE keys with value equal to the number of nodes of that
    type in the scene, not including default node types. Only node types with at
    least 1 node of that type are included.
    
        "summary" : {
            "transform" : 3,
            "mesh" : 1
        }
    
    For normal output the output is a dictionary whose keys are the node types and
    the values are a list of nodes of that type. The information is put into an
    object named "node_types". This avoids the potential for a name conflict
    between the object "summary" and a node type also named "summary".
    
        "nodeTypes" : {
            "transform" : ["transform1", "transform2", "group1"],
            "mesh" : ["cubeShape1"]
        }
    
    If the 'details' option is used then the output is arranged hierarchically by
    node type layers instead of a flat dictionary.
    
        "nodeTypeTree" : {
            "ROOT_NODE" : {
                "nodes" : [],
                "children" : {
                    "CHILD_NODE" : {
                        "nodes" : [],
                        "children" : {
                            "GRANDCHILD_NODE_TYPE1" : {
                                "nodes" : ["GC1_NODE_NAME],
                                "children" : []
                            },
                            "GRANDCHILD_NODE_TYPE2" : {
                                "nodes" : ["GC2_NODE_NAME],
                                "children" : []
                            }
                        }
                    }
                }
            }
        }
    
    If the analytic-specific option 'use_defaults' is used then the default nodes
    will be included in the output.
    """
    
    
    
    def __init__(self):
        """
        Initialize the persistent class members
        
        default_nodes:            Set of all default nodes
        default_node_connections: Set of (src,dst) pairs for all connections
                                  between default nodes.
        """
    
        pass
    
    
    def establish_baseline(self):
        """
        This is run on an empty scene, to find all of the nodes/node types
        present by default. They will all be ignored for the purposes of
        the analytic since they are not relevant to scene contents.
        """
    
        pass
    
    
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
    
    
    ANALYTIC_DESCRIPTION_DETAILED = 'This analytic collects the number of each node type in the scene.\n\nAll of the persistent and default nodes are skipped unless they have a new\nconnection. The way these two things are measured is different by necessity\nfor the cases of analyzing a file that is read and analyzing the current scene.\n\nIf the file is being read:\n    - persistent and default nodes are defined as any node present before the\n      file is loaded\n    - exceptions are made if a new connection is formed to a persistent or\n      default node after the file is loaded\n\nIf the current scene is used:\n    - persistent and default nodes are taken to be those marked as such by the\n      Maya \'ls\' command. This won\'t include any special persistent nodes\n      created after-the-fact, such as those a newly loaded plug-in might create.\n    - exceptions are made if there is any connection at all to these default\n      or persistent nodes to a scene node.\n\nIf the \'summary\' option is used then the output includes a dictionary\nconsisting of NODE_TYPE keys with value equal to the number of nodes of that\ntype in the scene, not including default node types. Only node types with at\nleast 1 node of that type are included.\n\n    "summary" : {\n        "transform" : 3,\n        "mesh" : 1\n    }\n\nFor normal output the output is a dictionary whose keys are the node types and\nthe values are a list of nodes of that type. The information is put into an\nobject named "node_types". This avoids the potential for a name conflict\nbetween the object "summary" and a node type also named "summary".\n\n    "nodeTypes" : {\n        "transform" : ["transform1", "transform2", "group1"],\n        "mesh" : ["cubeShape1"]\n    }\n\nIf the \'details\' option is used then the output is arranged hierarchically by\nnode type layers instead of a flat dictionary.\n\n    "nodeTypeTree" : {\n        "ROOT_NODE" : {\n            "nodes" : [],\n            "children" : {\n                "CHILD_NODE" : {\n                    "nodes" : [],\n                    "children" : {\n                        "GRANDCHILD_NODE_TYPE1" : {\n                            "nodes" : ["GC1_NODE_NAME],\n                            "children" : []\n                        },\n                        "GRANDCHILD_NODE_TYPE2" : {\n                            "nodes" : ["GC2_NODE_NAME],\n                            "children" : []\n                        }\n                    }\n                }\n            }\n        }\n    }\n\nIf the analytic-specific option \'use_defaults\' is used then the default nodes\nwill be included in the output.'
    
    
    ANALYTIC_DESCRIPTION_SHORT = []
    
    
    ANALYTIC_LABEL = []
    
    
    ANALYTIC_NAME = 'NodeTypes'
    
    
    KEY_CHILDREN = 'children'
    
    
    KEY_NODES = 'nodes'
    
    
    KEY_NODE_TYPES = 'nodeTypes'
    
    
    __fulldocs__ = 'This analytic collects the number of each node type in the scene.\n\nAll of the persistent and default nodes are skipped unless they have a new\nconnection. The way these two things are measured is different by necessity\nfor the cases of analyzing a file that is read and analyzing the current scene.\n\nIf the file is being read:\n    - persistent and default nodes are defined as any node present before the\n      file is loaded\n    - exceptions are made if a new connection is formed to a persistent or\n      default node after the file is loaded\n\nIf the current scene is used:\n    - persistent and default nodes are taken to be those marked as such by the\n      Maya \'ls\' command. This won\'t include any special persistent nodes\n      created after-the-fact, such as those a newly loaded plug-in might create.\n    - exceptions are made if there is any connection at all to these default\n      or persistent nodes to a scene node.\n\nIf the \'summary\' option is used then the output includes a dictionary\nconsisting of NODE_TYPE keys with value equal to the number of nodes of that\ntype in the scene, not including default node types. Only node types with at\nleast 1 node of that type are included.\n\n    "summary" : {\n        "transform" : 3,\n        "mesh" : 1\n    }\n\nFor normal output the output is a dictionary whose keys are the node types and\nthe values are a list of nodes of that type. The information is put into an\nobject named "node_types". This avoids the potential for a name conflict\nbetween the object "summary" and a node type also named "summary".\n\n    "nodeTypes" : {\n        "transform" : ["transform1", "transform2", "group1"],\n        "mesh" : ["cubeShape1"]\n    }\n\nIf the \'details\' option is used then the output is arranged hierarchically by\nnode type layers instead of a flat dictionary.\n\n    "nodeTypeTree" : {\n        "ROOT_NODE" : {\n            "nodes" : [],\n            "children" : {\n                "CHILD_NODE" : {\n                    "nodes" : [],\n                    "children" : {\n                        "GRANDCHILD_NODE_TYPE1" : {\n                            "nodes" : ["GC1_NODE_NAME],\n                            "children" : []\n                        },\n                        "GRANDCHILD_NODE_TYPE2" : {\n                            "nodes" : ["GC2_NODE_NAME],\n                            "children" : []\n                        }\n                    }\n                }\n            }\n        }\n    }\n\nIf the analytic-specific option \'use_defaults\' is used then the default nodes\nwill be included in the output.\nBase class for output for analytics.\n\nThe default location for the anlaytic output is in a subdirectory\ncalled \'MayaAnalytics\' in your temp directory. You can change that\nat any time by calling set_output_directory().\n\nClass static member:\n     ANALYTIC_NAME : Name of the analytic\n\nClass members:\n     directory     : Directory the output will go to\n     is_static     : True means this analytic doesn\'t require a file to run\n     logger        : Logging object for errors, warnings, and messages\n     plug_namer    : Object creating plug names, possibly anonymous\n     node_namer    : Object creating node names, possibly anonymous\n     csv_output    : Location to store legacy CSV output\n     plug_namer    : Set by option \'anonymous\' - if True then make plug names anonymous\n     node_namer    : Set by option \'anonymous\' - if True then make node names anonymous\n     __options     : Dictionary of per-analytic options\n\n\tMethods\n\t-------\n\tdebug : Utility to standardize debug messages coming from analytics.\n\n\terror : Utility to standardize errors coming from analytics.\n\n\testablish_baseline : This is run on an empty scene, to find all of the nodes/node types\n\t                     present by default. They will all be ignored for the purposes of\n\t                     the analytic since they are not relevant to scene contents.\n\n\thelp : Call this method to print the class documentation, including all methods.\n\n\tjson_file : Although an analytic is free to create any set of output files it\n\t            wishes there will always be one master JSON file containing the\n\n\tlog : Utility to standardize logging messages coming from analytics.\n\n\tmarker_file : Returns the name of the marker file used to indicate that the\n\t              computation of an analytic is in progress. If this file remains\n\t              in a directory after the analytic has run that means it was\n\t              interrupted and the data is not up to date.\n\t              \n\t              This file provides a safety measure against machines going down\n\t              or analytics crashing.\n\n\tname : Get the name of this type of analytic\n\n\toption : Return TRUE if the option specified has been set on this analytic.\n\t         option: Name of option to check\n\n\toutput_files : This is used to get the list of files the analytic will generate.\n\t               There will always be a JSON file generated which contains at minimum\n\t               the timing information. An analytic should override this method only\n\t               if they are adding more output files (e.g. a .jpg file).\n\t               \n\t               This should only be called after the final directory has been set.\n\n\trun : Run the analytic on the current scene.\n\t      :return: JSON results as described in the class doc\n\n\tset_options : Modify the settings controlling the run operation of the analytic.\n\t              Override this method if your analytic has some different options\n\t              available to it, but be sure to call this parent version after since\n\t              it sets common options.\n\n\tset_output_directory : Call this method to set a specific directory as the output location.\n\t                       The special names \'stdout\' and \'stderr\' are recognized as the\n\t                       output and error streams respectively rather than a directory.\n\n\twarning : Utility to standardize warnings coming from analytics.\n'
    
    
    is_static = False



OPTION_SUMMARY = 'summary'

OPTION_USE_DEFAULTS = 'use_defaults'

OPTION_DETAILS = 'details'

kAnalyticLabel = []

kAnalyticDescriptionShort = []


