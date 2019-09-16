from flux.ui.core import pix
from PySide2.QtCore import Slot

import PySide2.QtWidgets as QtWidgets

class Contents(QtWidgets.QWidget):
    def __init__(self, parent):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class TabLayout(QtWidgets.QTabWidget):
    def __init__(self, parent):
        pass
    
    
    def addTabNamed(self, widget, name):
        pass
    
    
    def currentTabChanged(self, index):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class IconButton(QtWidgets.QPushButton):
    def __init__(self, buttonName, iconName, parent='None'):
        pass
    
    
    staticMetaObject = None


class StackedPage(QtWidgets.QWidget):
    def __init__(self, parent='None'):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


import flux.ui.core as fui

class ToolButton(fui.ImageButton):
    def __init__(self, imageName, **kwargs):
        pass
    
    
    staticMetaObject = None


class LayoutInterface(object):
    def addSpacing(self, value):
        pass
    
    
    def addStretch(self, factor='1'):
        pass
    
    
    def addWidget(self, widget, stretchFactor='0', alignment='0'):
        pass
    
    
    def getFullName(self):
        pass
    
    
    def resizeDownstream(self):
        pass
    
    
    def resizeUpstream(self):
        pass
    
    
    def setAsMelParent(self):
        pass
    
    
    def addMethod(obj, methodName):
        pass
    
    
    def wrap(obj, layoutType):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class RadioImageGroup(QtWidgets.QWidget):
    def __init__(self, icons, currentIndex='0', parent='None'):
        pass
    
    
    def radioClicked(self, index):
        pass
    
    
    def setIndex(self, index):
        pass
    
    
    clicked = None
    
    
    staticMetaObject = None


class Layout(QtWidgets.QWidget):
    """
    # Top Level Mandatory Layout
    """
    
    
    
    def __init__(self):
        pass
    
    
    def addWidgetToParent(self, parentName, widget):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def resizeEvent(self, e):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self, childHeight='None'):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class ZeroVBoxLayout(QtWidgets.QVBoxLayout):
    def __init__(self, parent='None'):
        pass
    
    
    staticMetaObject = None


class Tab(QtWidgets.QWidget):
    def __init__(self):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class StackedLayout(QtWidgets.QStackedWidget):
    def __init__(self, parent='None'):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def setIndex(self, i):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class HorizontalLayout(QtWidgets.QWidget):
    def __init__(self, offset='0', height='None', parent='None'):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class IndentLayout(QtWidgets.QWidget):
    def __init__(self, name="''", parent='None', autoStretch='True'):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def setEnabled(self, enabled):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class FrameLayout(fui.FrameWidget):
    def __init__(self, text, expanded='False'):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def setEnabled(self, enabled):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def switchMode(self):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None


class ZeroHBoxLayout(QtWidgets.QHBoxLayout):
    def __init__(self, parent='None'):
        pass
    
    
    staticMetaObject = None


class VerticalLayout(QtWidgets.QWidget):
    def __init__(self, offset='0', height='None', parent='None'):
        pass
    
    
    def hideEvent(self, e):
        pass
    
    
    def showEvent(self, e):
        pass
    
    
    def updateHeight(self):
        pass
    
    
    staticMetaObject = None
    
    
    visibilityChanged = None



def wrapInstance(*args, **kwargs):
    pass


def unwrapInstance(*args, **kwargs):
    pass



