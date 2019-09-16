from flux.ae.Custom import Custom
from flux.ui.core import pix
from PySide2.QtCore import Slot
from flux.ae.Template import Template

class MyCustom(Custom):
    def alignChanged(self, *args):
        pass
    
    
    def alignClicked(self, index):
        pass
    
    
    def backBevelEnabledChanged(self):
        pass
    
    
    def bevelStyleChanged(self):
        pass
    
    
    def buildUI(self, nodeName):
        pass
    
    
    def clearManipClicked(self):
        pass
    
    
    def clearVectorOffsetAttributes(self):
        pass
    
    
    def createCurveClicked(self):
        pass
    
    
    def createCustomWidgets(self):
        pass
    
    
    def createFalloffCurve(self, attr):
        pass
    
    
    def createLocalPivotBtn(self, axis):
        pass
    
    
    def deformableTypeChanged(self):
        pass
    
    
    def disableAllBevels(self):
        pass
    
    
    def editFalloffCurve(self, attr):
        pass
    
    
    def enableBevelClicked(self):
        pass
    
    
    def enableBevelStyle(self):
        pass
    
    
    def enableDisableBevels(self):
        pass
    
    
    def extrudeEnableChanged(self):
        pass
    
    
    def getAdjustNode(self):
        pass
    
    
    def getAnimationNode(self):
        pass
    
    
    def getExtrudeNode(self):
        """
        # Utilities
        """
    
        pass
    
    
    def getRemeshNode(self):
        pass
    
    
    def getShader(self, index):
        pass
    
    
    def getVectorOffsetAttributes(self):
        """
        #same as above, but this refreshes the sliders when you change selection in the AE
        """
    
        pass
    
    
    def isBevelEnabled(self):
        pass
    
    
    def manipVisibilityChanged(self, visible):
        pass
    
    
    def materialJoinClicked(self):
        pass
    
    
    def materialSplitClicked(self):
        pass
    
    
    def nodeChanged(self):
        pass
    
    
    def offsetFieldChanged(self, *args):
        pass
    
    
    def offsetFieldEditingFinished(self, *args):
        pass
    
    
    def pasteClicked(self):
        pass
    
    
    def pasteRadioClicked(self):
        pass
    
    
    def pathClicked(self):
        pass
    
    
    def pathEdited(self):
        pass
    
    
    def pathNamesChanged(self, *args):
        pass
    
    
    def pathRadioClicked(self):
        pass
    
    
    def pathSelectionChanged(self):
        pass
    
    
    def pivotLocationClicked(self, axis):
        pass
    
    
    def pivotLocationMenuClicked(self, cmd):
        pass
    
    
    def populatePaths(self):
        pass
    
    
    def refreshClicked(self):
        pass
    
    
    def setVectorOffset(*args, **kwargs):
        pass
    
    
    def setVectorOffsetAttributes(self):
        """
        #this sets the manipulation offsets (z position and extrusion scale)
        """
    
        pass
    
    
    def setupNavigationControls(self, navigations):
        pass
    
    
    def shellAnimationClicked(self):
        pass
    
    
    def showLocalPivotMenu(self, axis, rpChecked, spChecked):
        pass
    
    
    def strRes(self, name):
        pass
    
    
    def stringResourceFunction(self, name):
        pass
    
    
    def svgModeChanged(self):
        pass
    
    
    def svg_catchPaste(self):
        pass
    
    
    def switchBackBevel(self):
        pass
    
    
    def switchFrontBevel(self):
        pass
    
    
    def updateAnimateEnabled(self):
        pass
    
    
    def updateBevelVisibility(self):
        pass
    
    
    def updateErrorIndicator(self):
        pass
    
    
    def updateInfoLabel(self):
        pass
    
    
    def updateMaterialSplitBtn(self):
        pass
    
    
    def updatePreviewPanel(self):
        pass
    
    
    staticMetaObject = None


class AEsvgToPolyTemplate(Template):
    def buildUI(self, nodeName):
        pass


import PySide2.QtCore as QtCore

class MyEventFilterer(QtCore.QObject):
    def eventFilter(self, widget, event):
        pass
    
    
    staticMetaObject = None



def joinTypeMaterials(meshShape, typeNode, shaderType):
    pass


def wrapInstance(*args, **kwargs):
    pass


def getShaderFromArray(GrpMessageConections):
    """
    #given a list of nodes, find the shading engine, and it's material
    """

    pass


def unwrapInstance(*args, **kwargs):
    pass


def getShaderFromObject(mesh):
    """
    #get the shader attribute attached to an object
    #this and the next function are VERY similar, but they go about their task in different ways - which only work in different situations.
    """

    pass


def getVectorShadingGroups(mesh, extrudeNode):
    """
    #given the group nodes, get the associated materials
    """

    pass


def splitTypeMaterials(extrudeNode, meshShape, typeNode, shaderType):
    """
    #assign materials to the type tool
    """

    pass


def getShadingGroupsFromObject(mesh):
    """
    #get the shaders attached to an object
    """

    pass



