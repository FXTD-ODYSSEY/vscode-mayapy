from PySide2.QtCore import Slot

import PySide2.QtWidgets as QtWidgets

class AnimTextQTreeWidgetExtend(QtWidgets.QTreeWidget):
    def __init__(self, node, parent='None'):
        pass
    
    
    def addItem(self, frame, name):
        pass
    
    
    def addItemAction(self):
        pass
    
    
    def deleteItems(self):
        pass
    
    
    def eventFilter(self, source, event):
        pass
    
    
    def mousePressEvent(self, event):
        pass
    
    
    def onChanged(self):
        pass
    
    
    def openMenu(self, point):
        pass
    
    
    def updateContent(self):
        pass
    
    
    staticMetaObject = None


class MyDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        pass
    
    
    def setEditorData(self, editor, index):
        pass
    
    
    def setModelData(self, editor, model, index):
        pass
    
    
    def sizeHint(self, option, index):
        pass
    
    
    staticMetaObject = None


class TypeAnimTextWidget(QtWidgets.QWidget):
    def __init__(self, node, parent='None'):
        pass
    
    
    def set_node(self, node):
        """
        #update connections
        """
    
        pass
    
    
    staticMetaObject = None



def update_qt_widget(layout, node):
    pass


def ByteToHex(byteStr):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """

    pass


def build_qt_widget(lay, node):
    pass


def unwrapInstance(*args, **kwargs):
    pass


def wrapInstance(*args, **kwargs):
    pass


def HexToUni(hexStr):
    pass



kFrame = []

kText = []


