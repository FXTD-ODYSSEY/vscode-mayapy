"""
This file contains all the classes which implement the Qt Model needed to benefit from the
Model/View design from Qt.

The design intent is that these classes only be used to implement Qt views.
They should be used as proxies to the underlying render setup data model
objects only by Qt views code, and in such cases only with as little code
as is required to interface with Qt.

All other uses, by any other code, should use the render setup data
model interface directly.  It already provides an encapsulation of the
underlying Maya objects, as well as observation and notification
capability.  There is no need to duplicate render setup data model
interfaces and services in Qt model interfaces and services: this
is a maintenance burden, introduces the possibility of error, and
requires additional testing, for no gain.  Similarly, Qt model code
should not perform any render setup data model computation or abstraction;
such services must be implemented in the render setup data model layer.
"""

from PySide2.QtCore import *

from functools import partial
from PySide2.QtGui import QColor
from PySide2.QtGui import QFontMetrics
from PySide2.QtGui import QGuiApplication
from PySide2.QtGui import QFont
from PySide2.QtGui import QStandardItem
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QStandardItemModel

class DataModelListObserver(object):
    """
    Mixin class for proxy items so they can observe their underlying
    data model list.
    """
    
    
    
    def __init__(self, *args, **kwargs):
        """
        # As per
        # 
        # https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
        #
        # the signature of __init__() callee methods needs to match the caller.
        # We therefore use the most generic parameter list to accomodate the
        # needs of any other base class in the list of base classes.
        """
    
        pass
    
    
    def addActiveLayerObserver(self):
        pass
    
    
    def addListObserver(self, model):
        pass
    
    
    def ignoreListItemAdded(self):
        pass
    
    
    def listItemAdded(self, listItem):
        """
        React to list item addition to the data model.
        
        If a list item is added to the data model, we create a
        list item proxy and insert it at the proper position.
        """
    
        pass
    
    
    def listItemRemoved(self, listItem):
        """
        React to list item removal from the data model.
        
        If a list item is removed from the data model, we remove the row
        corresponding to its list item proxy.
        """
    
        pass
    
    
    def removeActiveLayerObserver(self):
        pass
    
    
    def removeListObserver(self, model):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class UniqueOverrideProxy(object):
    def isUniqueOverride(self):
        pass
    
    
    def targetNodeName(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class Template(object):
    """
    Base class for all the proxy classes to offer the template file import
    """
    
    
    
    def acceptableDictionaries(self, templateDirectory):
        """
        Find the list of template files applicable to a specific proxy
        """
    
        pass
    
    
    def findAllTemplateFiles(self, templateDirectory):
        """
        Find the list of all template files
        """
    
        pass
    
    
    def templateActions(self, templateDirectory):
        """
        Build the list of all possible template actions
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


import maya.app.renderSetup.views.pySide.standardItem as standardItem

class ModelProxyItem(Template, standardItem.StandardItem):
    """
    # Because of MAYA-60799, QStandardItem must appear last in the list of
    # base classes.
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def data(self, role):
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
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def getWarning(self):
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
    
    
    def paste(*args, **kwargs):
        pass
    
    
    def setData(self, value, role):
        pass
    
    
    model = None


class RenderSetupProxy(DataModelListObserver, Template, QStandardItemModel):
    """
    # Because of MAYA-60799, QStandardItemModel must appear last in the list of
    # base classes.
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
    
    
    def acceptImport(self):
        pass
    
    
    def attachChild(self, renderLayer, pos):
        pass
    
    
    def child(self, row, column='0'):
        pass
    
    
    def copyForClipboard(self, proxies):
        """
        Export the selected proxies to a JSON string, for clipboard use.
        
        Render setup data model classes may implement copyForClipboard
        in a special way.  For example, render layers are unconditionally
        set to be not visible, which avoids two problems:
        - It avoids a potentially costly render layer switch operation on paste.
        - Pasting a layer shouldn't change the currently-visible layer.
        """
    
        pass
    
    
    def createListItemProxy(self, renderLayer):
        pass
    
    
    def createRenderLayer(self, renderLayerName):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def dropMimeData(self, mimeData, action, row, column, parentIndex):
        pass
    
    
    def exportSelectedToFile(self, filePath, notes, proxies):
        """
        Export the selected proxies to the file
        """
    
        pass
    
    
    def findProxyItem(self, name):
        pass
    
    
    def flags(self, index):
        pass
    
    
    def importAllFromFile(self, filePath, behavior, prependToName):
        """
        Import a complete render setup from that file
        """
    
        pass
    
    
    def importTemplate(*args, **kwargs):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        """
        Find if the selected filename is a template for the render setup
        """
    
        pass
    
    
    def mimeData(self, indices):
        """
        This method builds the mimeData if the selection is correct
        """
    
        pass
    
    
    def mimeTypes(self):
        pass
    
    
    def paste(*args, **kwargs):
        pass
    
    
    def refreshModel(self):
        pass
    
    
    def renderSetupAdded(self):
        pass
    
    
    def renderSetupPreDelete(self):
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


class BaseCollectionProxy(DataModelListObserver, ModelProxyItem):
    """
    # Because of MAYA-60799, PySide base classes must appear last in the list of
    # base classes.
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def attachChild(self, override, pos):
        pass
    
    
    def attachOverrideProxy(*args, **kwargs):
        pass
    
    
    def createListItemProxy(self, override):
        pass
    
    
    def createOverride(self, overrideTypeId):
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
    
    
    def genericTypeIdx(self):
        pass
    
    
    def getWarning(self):
        pass
    
    
    def importTemplate(*args, **kwargs):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        """
        Only collections and overrides could be imported in a collection
        """
    
        pass
    
    
    def isSortingEnabled(self):
        pass
    
    
    def listItemAdded(self, listItem):
        pass
    
    
    def listItemRemoved(self, listItem):
        pass
    
    
    def setData(self, value, role):
        pass
    
    
    def setSortingEnabled(self, enabled):
        pass
    
    
    def type(self):
        pass


class SceneItemProxy(DataModelListObserver, ModelProxyItem):
    def __init__(self, model):
        pass
    
    
    def data(self, role):
        pass


class OverrideProxy(ModelProxyItem):
    """
    The class provides the Qt model counterpart for the Override
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def acceptsDrops(self, attribute):
        pass
    
    
    def data(self, role):
        pass
    
    
    def delete(self):
        pass
    
    
    def finalizeOverrideCreation(self, plugName):
        pass
    
    
    def genericTypeIdx(self):
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def getWarning(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        pass
    
    
    def isLocalRender(self):
        pass
    
    
    def isUniqueOverride(self):
        pass
    
    
    def setData(self, value, role):
        pass
    
    
    def setLocalRender(self, value):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def type(self):
        pass
    
    
    def typeIdx(self):
        pass


class RenderLayerProxy(DataModelListObserver, ModelProxyItem):
    """
    # Because of MAYA-60799, PySide base classes must appear last in the list of
    # base classes.
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def attachChild(self, collection, pos):
        pass
    
    
    def createCollection(self, collectionName, nodeType):
        pass
    
    
    def createListItemProxy(self, collection):
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
    
    
    def importTemplate(*args, **kwargs):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        """
        Find if the selected filename is a template for a render layer
        """
    
        pass
    
    
    def isDropAllowed(self, destinationModel):
        pass
    
    
    def setData(self, value, role):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def type(self):
        pass
    
    
    def typeIdx(self):
        pass


class CollectionProxy(BaseCollectionProxy):
    def __init__(self, model):
        pass
    
    
    def createCollection(self, collectionName, nodeType):
        pass
    
    
    def data(self, role):
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        """
        Only collections and overrides could be imported in a collection
        """
    
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def typeIdx(self):
        pass
    
    
    ABSOLUTE_OVERRIDE = []
    
    
    NO_OVERRIDE = []
    
    
    RELATIVE_OVERRIDE = []


class LightsChildCollectionProxy(BaseCollectionProxy):
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def data(self, role):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def typeIdx(self):
        pass


class RelOverrideProxy(OverrideProxy):
    def __init__(self, model):
        pass
    
    
    def createAttributeUI(self, attribute):
        pass


class AOVChildCollectionProxy(BaseCollectionProxy):
    """
    # Can simplify this with a common base class
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def data(self, role):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def typeIdx(self):
        pass


class LightsProxy(BaseCollectionProxy):
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def data(self, role):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def equalsDragType(self, dragType):
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        pass
    
    
    def onDoubleClick(self, view):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def typeIdx(self):
        pass


class ConnectionOverrideProxy(OverrideProxy):
    def __init__(self, model):
        pass
    
    
    def acceptsDrops(self, attribute):
        pass
    
    
    def createAttributeUI(self, attribute):
        pass


class RenderSettingsCollectionProxy(BaseCollectionProxy):
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def createCollection(self, collectionName, nodeType):
        pass
    
    
    def data(self, role):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def equalsDragType(self, dragType):
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        """
        Only render settings child collections and overrides can be imported into a render settings collection
        """
    
        pass
    
    
    def isActive(self):
        pass
    
    
    def onDoubleClick(self, view):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def typeIdx(self):
        pass


class AbsOverrideProxy(OverrideProxy):
    def __init__(self, model):
        pass
    
    
    def createAttributeUI(self, attribute):
        pass


class CamerasProxy(SceneItemProxy):
    def __init__(self, model):
        pass
    
    
    def data(self, role):
        pass
    
    
    def equalsDragType(self, dragType):
        pass
    
    
    def type(self):
        pass
    
    
    def typeIdx(self):
        pass


class AOVCollectionProxy(BaseCollectionProxy):
    """
    # Can simplify this with a common base class
    """
    
    
    
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def data(self, role):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def equalsDragType(self, dragType):
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        pass
    
    
    def isActive(self):
        pass
    
    
    def onDoubleClick(self, view):
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def typeIdx(self):
        pass


class AOVsProxy(SceneItemProxy):
    def __init__(self, model):
        pass
    
    
    def data(self, role):
        pass
    
    
    def equalsDragType(self, dragType):
        pass
    
    
    def type(self):
        pass
    
    
    def typeIdx(self):
        pass


class AbsUniqueOverrideProxy(UniqueOverrideProxy, AbsOverrideProxy):
    def __init__(self, model):
        pass


class RenderSettingsChildCollectionProxy(CollectionProxy):
    def __init__(self, model):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def createCollection(self, collectionName, nodeType):
        pass
    
    
    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def equalsDragType(self, dragType):
        pass
    
    
    def getActionButton(self, column):
        pass
    
    
    def getActionButtonCount(self):
        pass
    
    
    def isAcceptableTemplate(self, objList):
        """
        Only render settings child collections and overrides can be imported into a render settings child collection
        """
    
        pass
    
    
    def supportsAction(self, action, numIndexes):
        pass
    
    
    def typeIdx(self):
        pass


class RelUniqueOverrideProxy(UniqueOverrideProxy, RelOverrideProxy):
    def __init__(self, model):
        pass


class ConnectionUniqueOverrideProxy(UniqueOverrideProxy, ConnectionOverrideProxy):
    def __init__(self, model):
        pass


class MaterialOverrideProxy(ConnectionOverrideProxy):
    def __init__(self, model):
        pass
    
    
    def acceptsDrops(self, attribute):
        pass
    
    
    def createAttributeUI(self, attribute):
        pass


class ShaderOverrideProxy(ConnectionOverrideProxy):
    def __init__(self, model):
        pass
    
    
    def acceptsDrops(self, attribute):
        pass
    
    
    def createAttributeUI(self, attribute):
        pass



def _createControlForAttribute(attr, attrLabel, connectable='True'):
    """
    Create a UI control for the given attribute, 
    matching its type and considering if it's connectable.
    """

    pass


def getProxy(dataModel):
    """
    # Returns the UI proxy associated with the given data model object. Note that
    # the proxy opaque data is a weakref, thus the () used to access the value.
    """

    pass



FILTER_MENU = []

RENDER_SETTINGS_TYPE = 1004

AOVS_CHILD_COLLECTION_TYPE = 1009

kRelativeType = []

TM_SHAPES_SHADERSFILTER_ACTION = []

RENDER_SETTINGS_CHILD_COLLECTION_TYPE = 1010

AOVS_CHILD_COLLECTION_TYPE_IDX = 9

SHADERSFILTER_ACTION = []

CREATE_RELATIVE_OVERRIDE_ACTION = []

LIGHTS_TYPE = 1006

SET_ENABLED_ACTION = []

LIGHTS_CHILD_COLLECTION_TYPE_IDX = 8

kCollectionWarningStr = []

PROXY_OPAQUE_DATA = 'ProxyOpaqueData'

CREATE_CONNECTION_OVERRIDE_ACTION = []

RENDER_SETTINGS_STR = []

SET_LOCAL_RENDER_ACTION = []

kAbsolute = []

CAMERAS_TYPE = 1005

CAMERAS_STR = []

SET_VISIBILITY_ACTION = []

CAMERAS_TYPE_IDX = 5

CREATE_SHADER_OVERRIDE_ACTION = []

CAMERASFILTER_ACTION = []

AOVS_TYPE = 1007

RENDER_OVERRIDE_TYPE = 1003

LIGHTS_STR = []

RENDER_OVERRIDE_TYPE_IDX = 3

CREATE_MATERIAL_OVERRIDE_ACTION = []

LIGHTS_TYPE_IDX = 6

LIGHTSFILTER_ACTION = []

kDragAndDrop = []

AOVS_STR = []

RENDER_SETTINGS_CHILD_COLLECTION_TYPE_IDX = 10

RENDER_LAYER_TYPE = 1001

RENDER_LAYER_TYPE_IDX = 1

RENDER_SETUP_MIME_TYPE = 'application/renderSetup'

RENDER_SETUP_TYPE = 1000

SHAPESFILTER_ACTION = []

kShaderType = []

RENDER_SETUP_TYPE_IDX = 0

COLLECTION_TYPE_IDX = 2

CREATE_COLLECTION_ACTION = []

LIGHTS_CHILD_COLLECTION_TYPE = 1008

kRenderLayerWarningStr = []

EXPAND_COLLAPSE_ACTION = []

SET_ISOLATE_SELECTED_ACTION = []

kRelative = []

CUSTOMFILTER_ACTION = []

COLLECTION_TYPE = 1002

kSelectionTypeError = []

CREATE_RENDER_SETTINGS_CHILD_COLLECTION_ACTION = []

PARENT_TYPE_NAME = 'parentTypeName'

AOVS_TYPE_IDX = 7

NEWFILTER_ACTION = []

kAbsoluteType = []

kMaterialType = []

TRANSFORMSFILTER_ACTION = []

kDragAndDropFailed = []

SET_RENDERABLE_ACTION = []

ALLFILTER_ACTION = []

RENAME_ACTION = []

kConnectionType = []

SETSFILTER_ACTION = []

kOverrideWarningStr = []

CREATE_ABSOLUTE_OVERRIDE_ACTION = []

DELETE_ACTION = []

kNoOverride = []

RENDER_SETTINGS_TYPE_IDX = 4

TM_SHAPESFILTER_ACTION = []

MAX_TYPE_IDX = 11


