from PySide2.QtGui import QPainter
from copy import deepcopy
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtGui import QBrush
from PySide2.QtWidgets import QLineEdit
from PySide2.QtGui import QPen
from PySide2.QtCore import QRect
from PySide2.QtGui import QFontMetrics

from . import baseDelegate

class RenderSetupDelegate(baseDelegate.BaseDelegate):
    """
    This class provides customization of the appearance of items in the Model.
    """
    
    
    
    def __init__(self, treeView):
        pass
    
    
    def createEditor(self, parent, option, index):
        """
        Creates the double-click editor for renaming render setup entries. The override entry is right aligned.
        """
    
        pass
    
    
    def getTextRect(self, rect, item):
        pass
    
    
    def updateEditorGeometry(self, editor, option, index):
        """
        Sets the location for the double-click editor for renaming render setup entries.
        """
    
        pass
    
    
    def getFilterIcon(filter):
        pass
    
    
    DISABLED_IMAGE = None
    
    
    DISCLOSURE_IMAGE = None
    
    
    HIGHLIGHTED_FILL_OFFSET = 1
    
    
    INFO_COLOR = None
    
    
    INVALID_IMAGE = None
    
    
    ISOLATE_IMAGE = None
    
    
    LEFT_NON_TEXT_OFFSET = 51.0
    
    
    RIGHT_NON_TEXT_OFFSET = 12.0
    
    
    kTooltips = {}
    
    
    staticMetaObject = None



def createFilterPixmaps():
    pass



