from maya.app.renderSetup.views.propertyEditor.override import Override
from PySide2.QtWidgets import QWidgetItem
from PySide2.QtGui import QStandardItem
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QSize
from PySide2.QtCore import QTimer
from maya.app.renderSetup.views.propertyEditor.renderLayer import RenderLayer
from maya.app.renderSetup.views.frameLayout import FrameLayout
from PySide2.QtCore import QPersistentModelIndex
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide2.QtCore import Slot
from functools import partial
from PySide2.QtWidgets import QScrollArea
from PySide2.QtCore import QItemSelection
from maya.app.renderSetup.lightEditor.views.properties import LightProperties
from PySide2.QtWidgets import QVBoxLayout
from maya.app.renderSetup.lightEditor.views.properties import GroupProperties

class PropertyEditorScrollArea(QScrollArea):
    def sizeHint(self):
        pass
    
    
    STARTING_SIZE = None
    
    
    staticMetaObject = None


class PropertyEditor(MayaQWidgetDockableMixin, QWidget):
    """
    This class represents the property editor which displays the selected render setup item's property information.
    
    
    Note: The Qt should never called any 'deferred' actions because all the design is based on synchronous notifications
          and any asynchronous events will change the order of execution of these events.
    
          For example when the selection in the Render Setup Window is changed (so the Property Editor must be updated). 
          The delete must be synchronous on the 'unselected' layouts otherwise they will be updated along with selected ones. 
          The two main side effects are that lot of unnecessary processings are triggered (those one the deleted layouts) 
          and the infamous 'C++ already deleted' issue appears because the Data Model & Qt Model objects were deleted 
          but not their corresponding Layout (instance used by the Property Editor to display a render setup object).
    """
    
    
    
    def __del__(self):
        """
        This is a workaround for a runtime error raised when the window is closed.
        'Internal C++ object (PropertyEditor) already deleted.
        See MAYA-82966 for details.
        """
    
        pass
    
    
    def __init__(self, treeView, parent):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def highlight(self, names):
        pass
    
    
    def itemChanged(self, item):
        """
        When an item in the model changes, update the control and 
        frameLayout that make use of that item (if one exists).
        """
    
        pass
    
    
    def minimumSizeHint(self):
        pass
    
    
    def populateFields(self, item):
        pass
    
    
    def rebuild(self):
        """
        regenerate our collection/override/layer controls.
        """
    
        pass
    
    
    def renderSetupAdded(self):
        """
        RenderSetup node was created
        """
    
        pass
    
    
    def renderSetupPreDelete(self):
        """
        RenderSetup node is about to be deleted
        """
    
        pass
    
    
    def selectionChanged(self, selected, deselected):
        """
        On selection changed we lazily regenerate our collection/override/layer 
        controls.
        """
    
        pass
    
    
    def setSizeHint(self, size):
        pass
    
    
    def sizeHint(self):
        pass
    
    
    def triggerRebuild(self):
        pass
    
    
    def triggerRepopulate(self, item):
        pass
    
    
    MINIMUM_SIZE = None
    
    
    PREFERRED_SIZE = None
    
    
    staticMetaObject = None
    
    
    width = 460



