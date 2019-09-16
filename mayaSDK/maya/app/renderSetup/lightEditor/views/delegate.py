from PySide2.QtGui import QPen
from PySide2.QtGui import QBrush
from PySide2.QtWidgets import QLineEdit
from PySide2.QtGui import QIcon
from PySide2.QtGui import QColor
from copy import deepcopy
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter
from PySide2.QtGui import QFontMetrics
from PySide2.QtGui import QCursor
from PySide2.QtCore import QRect

import maya.app.renderSetup.views.renderSetupDelegate as renderSetupDelegate

class LightEditorDelegate(renderSetupDelegate.RenderSetupDelegate):
    """
    This class provides customization of the appearance of items in the model.
    """
    
    
    
    def __init__(self, treeView):
        pass
    
    
    def getTextRect(self, rect, item):
        pass
    
    
    def updateEditorGeometry(self, editor, option, index):
        """
        Sets the location for the double-click editor for renaming light editor entries.
        """
    
        pass
    
    
    LIGHT_ATTR_WIDTH = 180.0
    
    
    LIGHT_ICON_OFFSET_X = 20.0
    
    
    LIGHT_ICON_OFFSET_Y = 8.0
    
    
    LIGHT_ICON_SIZE = 40.0
    
    
    TEXT_LEFT_OFFSET = 30.0
    
    
    TEXT_RIGHT_OFFSET = 60.0
    
    
    dataDelegates = {}
    
    
    kTooltips = {}
    
    
    staticMetaObject = None


class DataDelegate(object):
    def draw(self, painter, rect, data, mapped):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class BoolDelegate(DataDelegate):
    def draw(self, painter, rect, data, mapped):
        pass


class FloatDelegate(DataDelegate):
    def draw(self, painter, rect, data, mapped):
        pass


class IntDelegate(DataDelegate):
    def draw(self, painter, rect, data, mapped):
        pass


class ColorDelegate(DataDelegate):
    def draw(self, painter, rect, data, mapped):
        pass
    
    
    COLOR_SWATCH_WIDTH = 50.0



