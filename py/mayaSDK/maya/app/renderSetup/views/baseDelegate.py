from copy import deepcopy
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QStyle
from PySide2.QtGui import QPen
from PySide2.QtCore import QPointF
from PySide2.QtWidgets import QStyledItemDelegate
from PySide2.QtCore import QRect
from PySide2.QtGui import QCursor
from PySide2.QtGui import QPalette

class BaseDelegate(QStyledItemDelegate):
    """
    This class provides customization of the appearance of items in a Model.
    """
    
    
    
    def __init__(self, treeView):
        pass
    
    
    def drawAction(self, painter, actionName, pixmap, left, top, highlightedColor, drawDisclosure, borderColor):
        pass
    
    
    def drawPixmap(self, painter, pixmap, left, top):
        pass
    
    
    def drawToolbarFrame(self, painter, rect, toolbarCount):
        pass
    
    
    def getTextRect(self, rect, item):
        pass
    
    
    def paint(self, painter, option, index):
        """
        Renders the delegate using the given painter and style option for the item specified by index.
        """
    
        pass
    
    
    ACTION_BORDER = 4.0
    
    
    ACTION_WIDTH = 48.0
    
    
    ARROW_COLOR = None
    
    
    BOTTOM_GAP_OFFSET = 4.0
    
    
    COLLAPSED_ARROW = ()
    
    
    COLLAPSED_ARROW_OFFSET = 12.0
    
    
    COLLECTION_TEXT_RIGHT_OFFSET = 180.0
    
    
    COLOR_BAR_WIDTH = 12.0
    
    
    DISABLED_BACKGROUND_IMAGE = None
    
    
    DISABLED_HIGHLIGHT_IMAGE = None
    
    
    EXPANDED_ARROW = ()
    
    
    EXPANDED_ARROW_OFFSET = 6.0
    
    
    ICON_TOP_OFFSET = 8.0
    
    
    ICON_WIDTH = 40.0
    
    
    LAST_ICON_RIGHT_OFFSET = 48.0
    
    
    LAYER_TEXT_RIGHT_OFFSET = 140.0
    
    
    RENDERABLE_IMAGE = None
    
    
    TEXT_LEFT_OFFSET = 44.0
    
    
    TEXT_RIGHT_OFFSET = 72.0
    
    
    VISIBILITY_IMAGE = None
    
    
    WARNING_ICON_WIDTH = 22.0
    
    
    WARNING_IMAGE = None
    
    
    staticMetaObject = None



def createPixmap(fileName):
    pass



