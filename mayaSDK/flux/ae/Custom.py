from PySide2.QtCore import Slot
from contextlib import contextmanager

import PySide2.QtCore as QtCore

class Custom(QtCore.QObject):
    def __init__(self, nodeName, *args, **kwargs):
        pass
    
    
    def addCheckbox(self, attr, **kwargs):
        pass
    
    
    def addColor(self, attr, **kwargs):
        pass
    
    
    def addEnum(self, attr, **kwargs):
        pass
    
    
    def addNavigation(self, attr="''", **kwargs):
        pass
    
    
    def addRadio(self, attr, **kwargs):
        pass
    
    
    def addSlider(self, attr, **kwargs):
        pass
    
    
    def addSpacing(self, value):
        pass
    
    
    def addStretch(self, factor='1'):
        pass
    
    
    def addTextField(self, attr, **kwargs):
        pass
    
    
    def addVector(self, attr, **kwargs):
        pass
    
    
    def addWidget(self, widget, stetchFactor='0', alignment='0'):
        pass
    
    
    def createAttributeListener(self, attr, func, node="''"):
        pass
    
    
    def createContextListener(self, func):
        pass
    
    
    def currentLayout(self):
        pass
    
    
    def eventFilter(self, widget, event):
        """
        # Event filter for injecting drag data into controls
        """
    
        pass
    
    
    def frameLayout(*args, **kwds):
        pass
    
    
    def horizontalLayout(*args, **kwds):
        pass
    
    
    def indentLayout(*args, **kwds):
        pass
    
    
    def melDeferred(self, cmd):
        pass
    
    
    def newTab(*args, **kwds):
        pass
    
    
    def onClose(self):
        pass
    
    
    def onCreate(self, node):
        pass
    
    
    def onLayoutVisibilityChange(self, func):
        pass
    
    
    def onReplace(self, node):
        pass
    
    
    def page(*args, **kwds):
        pass
    
    
    def registerExternalNode(self, name, func):
        pass
    
    
    def setControlAttr(self, key, attr, **kwargs):
        pass
    
    
    def setControlEnabled(self, key, enabled):
        pass
    
    
    def setControlLabel(self, key, label):
        pass
    
    
    def setIndex(self, ref, index):
        pass
    
    
    def setLayoutEnabled(self, ref, enabled):
        pass
    
    
    def setLayoutHidden(self, ref, hidden):
        pass
    
    
    def stackedLayout(*args, **kwds):
        pass
    
    
    def supress(self, *attrs):
        pass
    
    
    def tabLayout(*args, **kwds):
        pass
    
    
    def textFieldAttrChanged(self, key):
        pass
    
    
    def textFieldEditingFinished(self, key):
        pass
    
    
    def verticalLayout(*args, **kwds):
        pass
    
    
    staticMetaObject = None



def wrapInstance(*args, **kwargs):
    pass


def unwrapInstance(*args, **kwargs):
    pass



start = None


