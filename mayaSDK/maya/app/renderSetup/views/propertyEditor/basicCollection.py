from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QGroupBox
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2.QtWidgets import QVBoxLayout

class BasicCollection(MayaQWidgetBaseMixin, QGroupBox):
    """
    Empty collection property editor UI.
    
    This class provides a very simple property editor UI for a collection.
    It displays the "path" to the collection within the render setup data
    model tree.  It can be used as a base class for more complex collection
    property editor UIs.
    """
    
    
    
    def __init__(self, item, parent):
        pass
    
    
    def paintEvent(self, event):
        pass
    
    
    def preSelector(self):
        pass
    
    
    def setupSelector(self, layout):
        pass
    
    
    staticMetaObject = None



def getCppPointer(*args, **kwargs):
    pass



