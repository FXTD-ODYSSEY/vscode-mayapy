from maya.analytics.decorators import addHelp
from maya.analytics.BaseAnalytic import BaseAnalytic
from maya.analytics.decorators import makeAnalytic
from maya.analytics.decorators import addMethodDocs

class analyticAnimation(BaseAnalytic):
    """
    Examine the animation in the system and gather some basic statistics
    about it. There are two types of animation to find:
    
        1) Anim curves, which animate in the usual manner
           Care is taken to make sure either time is either an explicit or
           implicit input since anim curves could be used for reasons
           other than animation (e.g. setDrivenKey)
        2) Any other node which has the time node as input
           Since these are pretty generic we can only take note of how
           many of these there are, and how many output connections they
           have.
    
    The summary data consists of a count of the static and non-static
    param curves. Any curve with an input to the time parameter is
    considered non-static since the time may warp and it's more difficult
    than it's worth to figure out if this is the case.
    
    Example of a normal dump for a simple scene:
    
    "output" : {
        "static"      : { "animCurveTL" : 4, "animCurveTA" : 1 },
        "nonStatic"   : { "animCurveTL" : 126, "animCurveTA" : 7 },
        "maybeStatic" : { "expression" : 1 },
        "keys"        : { "animCurveTL" : 7200, "animCurveTA" : 43 }
        "driven"      : { "animCurveTL" : { 1 : 7200 },
                          "animCurveTA" : { 1 : 42, 2 : 1 }
                          "expression"  : { 1 : 1 } }
    }
    
        "static"      : Count of animation nodes with the same value at all times
        "nonStatic"   : Count of animation nodes with differing values at some times
        "maybeStatic" : Count of animation nodes whose values could not be ascertained
        "keys"        : Count of keyframes, where appropriate.
        "driven"      : Count of number of nodes driving various numbers of outputs
                        e.g. { 1 : 7, 2 : 1 } means 7 nodes driving a single output and
                             1 node driving 2 outputs
    
    and the same scene with the 'summary' option enabled:
    
    "output" : {
        "summary" :
        {
            "static"       : 5,
            "nonStatic"    : 133,
            "maybeStatic"  : 1,
            "keys"         : 7243,
            "animCurveTL"  : 130,
            "animCurveTA"  : 8,
            "multiDriven"  : 1,
            "noDriven"     : 0,
            "expression"   : 1
        },
        "static"      : { "animCurveTL" : 4, "animCurveTA" : 1 },
        "nonStatic"   : { "animCurveTL" : 126, "animCurveTA" : 7 }
        "maybeStatic" : { "expression" : 1 }
        "keyframes"   : { "animCurveTL" : 7200, "animCurveTA" : 43 }
        "driven"      : { "animCurveTL" : { 1 : 7200 },
                          "animCurveTA" : { 1 : 42, 2 : 1 }
                          "expression"  : { 1 : 1 } }
    }
    
    For the summary the "multiDriven" value means "the number of
    animation nodes driving more than one outputs", and "noDriven" means
    "the number of animation nodes not driving any outputs".
    
    The additional NODE_TYPE counts indicate the number of nodes of each
    animation node type in the scene. The other summary values are a count
    of the data of that type. All of the summary information is available
    within the normal data, this is just a convenient method of accessing.
    
    When the 'details' option is on then the fully detailed information about
    all animation curves is added. Here is a sample for one curve:
    
        "static" :
        {
            "animCurveTL" :
            {
                "nurbsCone1_translateX" :
                {
                    "keyframes" : [ [1.0,1.0], [10.0,10.0] ],
                    "driven"    : {"group1.tx" : "transform"}
                }
            }
        },
        "nonStatic" :
        {
            ...
        },
        "maybeStatic" :
        {
            ...
        }
    
        The data is nested as "type of animation" over "type of animation
        node" over "animation node name". Inside each node are these
        fields:
    
        "driven"    : Keyed on plugs on the destination end of the animation,
                      values are the type of said node
        "keyframes" : [Key,Value] pairs for the animation keyframes.
                      an animCurve. For expressions et. al. the member
                      will be omitted.
    """
    
    
    
    def run(self):
        """
        Run the analytic on the currently loaded file.
        :return: Animation data as described in the class doc
        """
    
        pass
    
    
    def help():
        """
        Call this method to print the class documentation, including all methods.
        """
    
        pass
    
    
    ANALYTIC_DESCRIPTION_DETAILED = 'Examine the animation in the system and gather some basic statistics\nabout it. There are two types of animation to find:\n\n    1) Anim curves, which animate in the usual manner\n       Care is taken to make sure either time is either an explicit or\n       implicit input since anim curves could be used for reasons\n       other than animation (e.g. setDrivenKey)\n    2) Any other node which has the time node as input\n       Since these are pretty generic we can only take note of how\n       many of these there are, and how many output connections they\n       have.\n\nThe summary data consists of a count of the static and non-static\nparam curves. Any curve with an input to the time parameter is\nconsidered non-static since the time may warp and it\'s more difficult\nthan it\'s worth to figure out if this is the case.\n\nExample of a normal dump for a simple scene:\n\n"output" : {\n    "static"      : { "animCurveTL" : 4, "animCurveTA" : 1 },\n    "nonStatic"   : { "animCurveTL" : 126, "animCurveTA" : 7 },\n    "maybeStatic" : { "expression" : 1 },\n    "keys"        : { "animCurveTL" : 7200, "animCurveTA" : 43 }\n    "driven"      : { "animCurveTL" : { 1 : 7200 },\n                      "animCurveTA" : { 1 : 42, 2 : 1 }\n                      "expression"  : { 1 : 1 } }\n}\n\n    "static"      : Count of animation nodes with the same value at all times\n    "nonStatic"   : Count of animation nodes with differing values at some times\n    "maybeStatic" : Count of animation nodes whose values could not be ascertained\n    "keys"        : Count of keyframes, where appropriate.\n    "driven"      : Count of number of nodes driving various numbers of outputs\n                    e.g. { 1 : 7, 2 : 1 } means 7 nodes driving a single output and\n                         1 node driving 2 outputs\n\nand the same scene with the \'summary\' option enabled:\n\n"output" : {\n    "summary" :\n    {\n        "static"       : 5,\n        "nonStatic"    : 133,\n        "maybeStatic"  : 1,\n        "keys"         : 7243,\n        "animCurveTL"  : 130,\n        "animCurveTA"  : 8,\n        "multiDriven"  : 1,\n        "noDriven"     : 0,\n        "expression"   : 1\n    },\n    "static"      : { "animCurveTL" : 4, "animCurveTA" : 1 },\n    "nonStatic"   : { "animCurveTL" : 126, "animCurveTA" : 7 }\n    "maybeStatic" : { "expression" : 1 }\n    "keyframes"   : { "animCurveTL" : 7200, "animCurveTA" : 43 }\n    "driven"      : { "animCurveTL" : { 1 : 7200 },\n                      "animCurveTA" : { 1 : 42, 2 : 1 }\n                      "expression"  : { 1 : 1 } }\n}\n\nFor the summary the "multiDriven" value means "the number of\nanimation nodes driving more than one outputs", and "noDriven" means\n"the number of animation nodes not driving any outputs".\n\nThe additional NODE_TYPE counts indicate the number of nodes of each\nanimation node type in the scene. The other summary values are a count\nof the data of that type. All of the summary information is available\nwithin the normal data, this is just a convenient method of accessing.\n\nWhen the \'details\' option is on then the fully detailed information about\nall animation curves is added. Here is a sample for one curve:\n\n    "static" :\n    {\n        "animCurveTL" :\n        {\n            "nurbsCone1_translateX" :\n            {\n                "keyframes" : [ [1.0,1.0], [10.0,10.0] ],\n                "driven"    : {"group1.tx" : "transform"}\n            }\n        }\n    },\n    "nonStatic" :\n    {\n        ...\n    },\n    "maybeStatic" :\n    {\n        ...\n    }\n\n    The data is nested as "type of animation" over "type of animation\n    node" over "animation node name". Inside each node are these\n    fields:\n\n    "driven"    : Keyed on plugs on the destination end of the animation,\n                  values are the type of said node\n    "keyframes" : [Key,Value] pairs for the animation keyframes.\n                  an animCurve. For expressions et. al. the member\n                  will be omitted.'
    
    
    ANALYTIC_DESCRIPTION_SHORT = []
    
    
    ANALYTIC_LABEL = []
    
    
    ANALYTIC_NAME = 'Animation'
    
    
    KEY_DRIVEN = 'driven'
    
    
    KEY_KEYFRAMES = 'keyframes'
    
    
    KEY_MAYBE_STATIC = 'maybeStatic'
    
    
    KEY_MULTI_DRIVEN = 'multiDriven'
    
    
    KEY_NON_STATIC = 'nonStatic'
    
    
    KEY_NO_DRIVEN = 'noDriven'
    
    
    KEY_STATIC = 'static'
    
    
    ZERO_TOLERANCE = 0.001
    
    
    __fulldocs__ = 'Examine the animation in the system and gather some basic statistics\nabout it. There are two types of animation to find:\n\n    1) Anim curves, which animate in the usual manner\n       Care is taken to make sure either time is either an explicit or\n       implicit input since anim curves could be used for reasons\n       other than animation (e.g. setDrivenKey)\n    2) Any other node which has the time node as input\n       Since these are pretty generic we can only take note of how\n       many of these there are, and how many output connections they\n       have.\n\nThe summary data consists of a count of the static and non-static\nparam curves. Any curve with an input to the time parameter is\nconsidered non-static since the time may warp and it\'s more difficult\nthan it\'s worth to figure out if this is the case.\n\nExample of a normal dump for a simple scene:\n\n"output" : {\n    "static"      : { "animCurveTL" : 4, "animCurveTA" : 1 },\n    "nonStatic"   : { "animCurveTL" : 126, "animCurveTA" : 7 },\n    "maybeStatic" : { "expression" : 1 },\n    "keys"        : { "animCurveTL" : 7200, "animCurveTA" : 43 }\n    "driven"      : { "animCurveTL" : { 1 : 7200 },\n                      "animCurveTA" : { 1 : 42, 2 : 1 }\n                      "expression"  : { 1 : 1 } }\n}\n\n    "static"      : Count of animation nodes with the same value at all times\n    "nonStatic"   : Count of animation nodes with differing values at some times\n    "maybeStatic" : Count of animation nodes whose values could not be ascertained\n    "keys"        : Count of keyframes, where appropriate.\n    "driven"      : Count of number of nodes driving various numbers of outputs\n                    e.g. { 1 : 7, 2 : 1 } means 7 nodes driving a single output and\n                         1 node driving 2 outputs\n\nand the same scene with the \'summary\' option enabled:\n\n"output" : {\n    "summary" :\n    {\n        "static"       : 5,\n        "nonStatic"    : 133,\n        "maybeStatic"  : 1,\n        "keys"         : 7243,\n        "animCurveTL"  : 130,\n        "animCurveTA"  : 8,\n        "multiDriven"  : 1,\n        "noDriven"     : 0,\n        "expression"   : 1\n    },\n    "static"      : { "animCurveTL" : 4, "animCurveTA" : 1 },\n    "nonStatic"   : { "animCurveTL" : 126, "animCurveTA" : 7 }\n    "maybeStatic" : { "expression" : 1 }\n    "keyframes"   : { "animCurveTL" : 7200, "animCurveTA" : 43 }\n    "driven"      : { "animCurveTL" : { 1 : 7200 },\n                      "animCurveTA" : { 1 : 42, 2 : 1 }\n                      "expression"  : { 1 : 1 } }\n}\n\nFor the summary the "multiDriven" value means "the number of\nanimation nodes driving more than one outputs", and "noDriven" means\n"the number of animation nodes not driving any outputs".\n\nThe additional NODE_TYPE counts indicate the number of nodes of each\nanimation node type in the scene. The other summary values are a count\nof the data of that type. All of the summary information is available\nwithin the normal data, this is just a convenient method of accessing.\n\nWhen the \'details\' option is on then the fully detailed information about\nall animation curves is added. Here is a sample for one curve:\n\n    "static" :\n    {\n        "animCurveTL" :\n        {\n            "nurbsCone1_translateX" :\n            {\n                "keyframes" : [ [1.0,1.0], [10.0,10.0] ],\n                "driven"    : {"group1.tx" : "transform"}\n            }\n        }\n    },\n    "nonStatic" :\n    {\n        ...\n    },\n    "maybeStatic" :\n    {\n        ...\n    }\n\n    The data is nested as "type of animation" over "type of animation\n    node" over "animation node name". Inside each node are these\n    fields:\n\n    "driven"    : Keyed on plugs on the destination end of the animation,\n                  values are the type of said node\n    "keyframes" : [Key,Value] pairs for the animation keyframes.\n                  an animCurve. For expressions et. al. the member\n                  will be omitted.\nBase class for output for analytics.\n\nThe default location for the anlaytic output is in a subdirectory\ncalled \'MayaAnalytics\' in your temp directory. You can change that\nat any time by calling set_output_directory().\n\nClass static member:\n     ANALYTIC_NAME : Name of the analytic\n\nClass members:\n     directory     : Directory the output will go to\n     is_static     : True means this analytic doesn\'t require a file to run\n     logger        : Logging object for errors, warnings, and messages\n     plug_namer    : Object creating plug names, possibly anonymous\n     node_namer    : Object creating node names, possibly anonymous\n     csv_output    : Location to store legacy CSV output\n     plug_namer    : Set by option \'anonymous\' - if True then make plug names anonymous\n     node_namer    : Set by option \'anonymous\' - if True then make node names anonymous\n     __options     : Dictionary of per-analytic options\n\n\tMethods\n\t-------\n\tdebug : Utility to standardize debug messages coming from analytics.\n\n\terror : Utility to standardize errors coming from analytics.\n\n\testablish_baseline : This is run on an empty scene, to give the analytic a chance to\n\t                     establish any baseline data it might need (e.g. the nodes in an\n\t                     empty scene could all be ignored by the analytic)\n\t                     \n\t                     Base implementation does nothing. Derived classes should call\n\t                     their super() method though, in case something does get added.\n\n\thelp : Call this method to print the class documentation, including all methods.\n\n\tjson_file : Although an analytic is free to create any set of output files it\n\t            wishes there will always be one master JSON file containing the\n\n\tlog : Utility to standardize logging messages coming from analytics.\n\n\tmarker_file : Returns the name of the marker file used to indicate that the\n\t              computation of an analytic is in progress. If this file remains\n\t              in a directory after the analytic has run that means it was\n\t              interrupted and the data is not up to date.\n\t              \n\t              This file provides a safety measure against machines going down\n\t              or analytics crashing.\n\n\tname : Get the name of this type of analytic\n\n\toption : Return TRUE if the option specified has been set on this analytic.\n\t         option: Name of option to check\n\n\toutput_files : This is used to get the list of files the analytic will generate.\n\t               There will always be a JSON file generated which contains at minimum\n\t               the timing information. An analytic should override this method only\n\t               if they are adding more output files (e.g. a .jpg file).\n\t               \n\t               This should only be called after the final directory has been set.\n\n\trun : Run the analytic on the currently loaded file.\n\t      :return: Animation data as described in the class doc\n\n\tset_options : Modify the settings controlling the run operation of the analytic.\n\t              Override this method if your analytic has some different options\n\t              available to it, but be sure to call this parent version after since\n\t              it sets common options.\n\n\tset_output_directory : Call this method to set a specific directory as the output location.\n\t                       The special names \'stdout\' and \'stderr\' are recognized as the\n\t                       output and error streams respectively rather than a directory.\n\n\twarning : Utility to standardize warnings coming from analytics.\n'
    
    
    is_static = False



kAnalyticDescriptionShort = []

OPTION_SUMMARY = 'summary'

OPTION_DETAILS = 'details'

kAnalyticLabel = []


