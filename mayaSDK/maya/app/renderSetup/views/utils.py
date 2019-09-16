from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QSizePolicy
from maya.app.renderSetup.model.renderLayerSwitchObservable import RenderLayerSwitchObservable
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QMouseEvent
from functools import partial
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QFrame

class LabelFieldButtonGrp(QWidget):
    """
    Same as cmds.textFieldButtonGrp, but with better controls on each different widgets.
    (ex: more control on callbacks, tooltips and such).
    """
    
    
    
    def __init__(self, label='None', text='None', placeholder='None', tooltip='None', button='None'):
        pass
    
    
    button = None
    
    field = None
    
    label = None
    
    layout = None
    
    staticMetaObject = None


class NodeListView:
    def __init__(self, title):
        pass
    
    
    def buildViewObjects(self, names):
        pass
    
    
    def onOKButton(self, data, msg):
        pass
    
    
    def onSelectAllButton(self, data, treeView, names):
        pass
    
    
    def selectTreeCallBack(self, *args):
        pass
    
    
    def show(self, names):
        pass


class Separator(QWidget):
    """
    Same as cmds.separator(), except it allows to add a text in the middle of the separator.
    Ex: -------------- My Section --------------
    """
    
    
    
    def __init__(self, text='None'):
        pass
    
    
    staticMetaObject = None


class ProgressBar(object):
    def __init__(self):
        pass
    
    
    def createProgressBar(self):
        pass
    
    
    def endProgressBar(self):
        pass
    
    
    def stepProgressBar(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def dpiScale(value):
    pass


def wrapInstance(*args, **kwargs):
    pass


def setExpandedState(node, value):
    """
    Sets an attribute on the node storing the expanded state of
    this node in the view. Creates it if it doesn't exist
    """

    pass


def updateMouseEvent(event):
    pass


def createIcon(iconName):
    pass


def browse(fileNameAttr):
    pass


def getExpandedState(node):
    """
    Retrieves the expanded state attribute of the node
    """

    pass


def createPixmap(imageName, width='0', height='0'):
    pass



kSelectAll = []

kOK = []

kUnapplyOverride = []

kApplyOverride = []

kUnapplyLayer = []

kApplyLayer = []

_DPI_SCALE = 2.0

kExpandedStateString = 'expandedState'

kNbObjects = []


