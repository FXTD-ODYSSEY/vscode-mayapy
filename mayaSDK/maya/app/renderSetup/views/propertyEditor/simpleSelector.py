from maya.app.renderSetup.common.devtools import *
from maya.app.renderSetup.views.propertyEditor.collectionFilterLineEdit import *

from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QPushButton
from maya.app.renderSetup.views.propertyEditor.layout import Layout
from PySide2.QtWidgets import QComboBox
from maya.app.renderSetup.views.propertyEditor.expressionLabels import IncludeExpressionLabel
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QCheckBox
from PySide2.QtWidgets import QSizePolicy
from PySide2.QtGui import QFont
from maya.app.renderSetup.views.propertyEditor.collectionStaticSelectionWidget import CollectionStaticSelectionWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QHBoxLayout
from maya.app.renderSetup.views.renderSetupDelegate import RenderSetupDelegate

class SimpleSelector(object):
    def __init__(self, selector):
        pass
    
    
    def build(self, layout, populate='True'):
        pass
    
    
    def customFilterEntered(*args, **kwargs):
        """
        # See undo module for decorator comments.
        """
    
        pass
    
    
    def displayType(self):
        """
        Return the user-visible display type string.
        
        By default this is the same for all objects of a selector class.
        """
    
        pass
    
    
    def highlight(self, names):
        pass
    
    
    def includeExpressionChanged(self, text):
        pass
    
    
    def includeExpressionEntered(*args, **kwargs):
        """
        # See undo module for decorator comments.
        """
    
        pass
    
    
    def populateFields(*args, **kwargs):
        pass
    
    
    def selectIncludeExpression(self):
        pass
    
    
    def selectStaticEntries(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    CREATE_EXPRESSION_STRING = []
    
    
    DRAG_DROP_FILTER_STRING = []
    
    
    EXPRESSION_BUTTON_WIDTH = 100.0
    
    
    INVERSE_STRING = []
    
    
    LIST_BOX_HEIGHT = 200.0
    
    
    SELECT_STRING = []
    
    
    kModelType = 'simpleSelector'


class BasicSelector(SimpleSelector):
    def __init__(self, selector):
        pass
    
    
    def build(self, layout):
        pass
    
    
    def populateFields(*args, **kwargs):
        pass
    
    
    def setIncludeHierarchy(*args, **kwargs):
        """
        # See undo module for decorator comments.
        """
    
        pass
    
    
    kDisplayType = []
    
    
    kModelType = 'basicSelector'
    
    
    kUsage = []



def ifNotBlockChangeMessages(f):
    """
    Avoid calling the decorated function if change messages are blocked.
    """

    pass



