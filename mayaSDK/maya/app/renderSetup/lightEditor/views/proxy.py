from PySide2.QtCore import *

from PySide2.QtGui import QColor
from PySide2.QtGui import QGuiApplication
from PySide2.QtGui import QFontMetrics
from PySide2.QtGui import QFont
from PySide2.QtGui import QStandardItem
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QStandardItemModel

import maya.app.renderSetup.views.proxy.renderSetup as rsProxy

class LightEditorProxy(rsProxy.DataModelListObserver, QStandardItemModel):
    """
    The class provides the Qt model counterpart for the LightEditor model
    """
    
    
    
    def __eq__(self, o):
        pass
    
    
    def __init__(self, parent='None'):
        pass
    
    
    def __ne__(self, o):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def attachChild(self, child, pos):
        pass
    
    
    def child(self, row, column='0'):
        pass
    
    
    def createListItemProxy(self, listItem):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def dropMimeData(self, mimeData, action, row, column, parentIndex):
        pass
    
    
    def findProxyItem(self, name):
        pass
    
    
    def flags(self, index):
        pass
    
    
    def mimeData(self, indices):
        """
        This method builds the mimeData if the selection is correct
        """
    
        pass
    
    
    def mimeTypes(self):
        pass
    
    
    def refreshModel(self):
        pass
    
    
    def resetModel(self):
        pass
    
    
    def supportedDropActions(self):
        pass
    
    
    def type(self):
        pass
    
    
    def typeIdx(self):
        pass
    
    
    model = None
    
    staticMetaObject = None


import maya.app.renderSetup.views.pySide.standardItem as standardItem

class LightEditorItemProxy(standardItem.StandardItem):
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def data(self, role):
        pass
    
    
    def delete(self):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def equalsDragType(self, dragType):
        pass
    
    
    def findProxyItem(self, name):
        pass
    
    
    def genericTypeIdx(self):
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def handleDragMoveEvent(self, event):
        pass
    
    
    def handleDropEvent(self, event, sceneView):
        pass
    
    
    def headingWidth(self, heading):
        pass
    
    
    def isActive(self):
        pass
    
    
    def isCopyable(self):
        pass
    
    
    def isDropAllowed(self, destinationModel):
        pass
    
    
    def isModelDirty(self):
        """
        # The next function (isModelDirty) is a workaround.
        # It should not be necessary but it is currently because we set tooltips in the treeview
        # and that triggers emitDataChanged which triggers the rebuild or repopulate of the property editor.
        # The proper fix will be to use columns in the treeview where each column has its own static tooltip
        # and the tooltips should no longer be dynamically set by the delegate (views/renderSetupDelegate.py)
        # depending on the lastHitAction
        """
    
        pass
    
    
    def modelChanged(*args, **kwargs):
        pass
    
    
    def onClick(self, view):
        pass
    
    
    def onDoubleClick(self, view):
        pass
    
    
    def setData(self, value, role):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    model = None


class LightEditorGroupProxy(rsProxy.DataModelListObserver, LightEditorItemProxy):
    """
    The class provides the Qt model counterpart for the LightEditorGroup
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def acceptsDrops(self, attribute):
        pass
    
    
    def attachChild(self, override, pos):
        pass
    
    
    def createListItemProxy(self, listItem):
        pass
    
    
    def data(self, role):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def type(self):
        pass
    
    
    def typeIdx(self):
        pass


class LightEditorLightProxy(LightEditorItemProxy):
    """
    The class provides the Qt model counterpart for the LightEditorLight
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def acceptsDrops(self, attribute):
        pass
    
    
    def columnData(self, role, column):
        pass
    
    
    def data(self, role):
        pass
    
    
    def type(self):
        pass
    
    
    def typeIdx(self):
        pass



def getProxy(dataModel):
    pass



LIGHT_EDITOR_MIME_TYPE = 'application/lightEditor'

kCollectionWarningStr = []

LIGHT_TEXT_COLOR_LOCKED = None

kFiltersMenu = []

kRelativeType = []

kFilterTransformsShapesShaders = []

kCreateRelativeOverrideAction = []

kFilterAll = []

kDragAndDrop = []

LIGHT_TEXT_COLOR_ANIMATED = None

kDragAndDropFailed = []

kAbsolute = []

kCreateConnectionOverrideAction = []

kSetLocalRender = []

LIGHT_EDITOR_ITEM_TYPE = 1013

kCameras = []

kSetVisibilityAction = []

kCreateCollectionAction = []

LIGHT_EDITOR_TYPE = 1012

kOverrideWarningStr = []

kFilterCameras = []

kRenderLayerWarningStr = []

LIGHT_EDITOR_LIGHT_TYPE = 1014

kRenameAction = []

kCreateMaterialOverrideAction = []

kLights = []

LIGHT_EDITOR_ITEM_TYPE_IDX = 13

kAOVs = []

LIGHT_EDITOR_GROUP_TYPE = 1015

kFilterGeometry = []

kRenderSettings = []

kFilterShaders = []

kFilterLights = []

kFilterTransforms = []

kSetIsolateSelectedAction = []

kExpandCollapseAction = []

kRelative = []

kSelectionTypeError = []

kConnectionType = []

kFilterCustom = []

LIGHT_TEXT_COLOR_OVERRIDEN_BY_US = None

kAbsoluteType = []

kNewFilter = []

kMaterialType = []

kCreateShaderOverrideAction = []

LIGHT_EDITOR_GROUP_TYPE_IDX = 15

kShaderType = []

kSetRenderableAction = []

kCreateRenderSettingsChildCollectionAction = []

LIGHT_EDITOR_LIGHT_TYPE_IDX = 14

kFilterSets = []

kSetEnabledAction = []

LIGHT_TEXT_COLOR = None

kCreateAbsoluteOverrideAction = []

LIGHT_EDITOR_TYPE_IDX = 12

kNoOverride = []

kDeleteAction = []

kFilterTransformsAndShapes = []


