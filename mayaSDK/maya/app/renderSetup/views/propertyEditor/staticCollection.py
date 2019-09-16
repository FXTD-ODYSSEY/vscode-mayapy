from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QListWidget
from PySide2.QtWidgets import QHBoxLayout

from . import basicCollection

class StaticCollection(basicCollection.BasicCollection):
    """
    This class represents the property editor view of a static collection.
    A static selection is read-only and only contains a list of selected nodes.
    """
    
    
    
    def __init__(self, item, parent):
        pass
    
    
    def setupSelector(self, layout):
        pass
    
    
    LIST_BOX_HEIGHT = 200.0
    
    
    staticMetaObject = None



