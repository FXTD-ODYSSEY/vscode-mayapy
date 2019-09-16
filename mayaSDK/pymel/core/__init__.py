from pymel.core.modeling import *
from pymel.core.rendering import *
from pymel.core.effects import *
from pymel.core.animation import *
from pymel.core.language import *
from pymel.core.windows import *
from pymel.core.context import *
from pymel.core.system import *
from pymel.core.other import *
from pymel.core.general import *

def _addPluginNode(pluginName, mayaType):
    pass


def _pluginUnloaded(*args):
    pass


def _addPluginCommand(pluginName, funcName):
    pass


def _installCallbacks():
    """
    install the callbacks that trigger new nodes and commands to be added to pymel when a
    plugin loads.  This is called from pymel.__init__
    """

    pass


def _removePluginCommand(pluginName, command):
    pass


def _pluginLoaded(*args):
    pass


def _removePluginNode(pluginName, node):
    pass



_pluginLoadedCB = True

_logger = None

_pluginData = {}


