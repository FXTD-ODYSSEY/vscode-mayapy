from PySide2.QtWidgets import QGroupBox
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from maya.app.renderSetup.views.propertyEditor.layout import Layout
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel
from functools import partial
from PySide2.QtWidgets import QVBoxLayout

class LightProperties(MayaQWidgetBaseMixin, QGroupBox):
    """
    This class represents the property editor view of a light editor light item.
    """
    
    
    
    def __init__(self, item, parent):
        pass
    
    
    staticMetaObject = None


class GroupProperties(MayaQWidgetBaseMixin, QGroupBox):
    """
    This class represents the property editor view of a light editor group item.
    """
    
    
    
    def __init__(self, item, parent):
        pass
    
    
    staticMetaObject = None



def getCppPointer(*args, **kwargs):
    pass


def _createControl(plg, attrLabel, connectable='True', enabled='True'):
    """
    Create a UI control for the given attribute, 
    matching its type and considering if it's connectable.
    """

    pass



kIsolate = []

kEnable = []


