class AOVCallbacks(object):
    """
    Renderers should either extend this class or create a class with the same signature to provide additional AOV callbacks
    """
    
    
    
    def decode(self, aovsData, decodeType):
        """
        Decodes the AOV information from some format
        
        aovsData   - The AOV data to decode
        decodeType - Overwrite, Merge
        """
    
        pass
    
    
    def displayMenu(self):
        """
        Displays the AOV information for the current renderer
        """
    
        pass
    
    
    def encode(self):
        """
        Encodes the AOV information into some format
        """
    
        pass
    
    
    def getAOVName(self, aovNode):
        """
        From a given AOV node, returns the AOV name
        """
    
        pass
    
    
    def getChildCollectionSelector(self, selectorName, aovName):
        """
        Creates the selector for the AOV child collection
        """
    
        pass
    
    
    def getChildCollectionSelectorAOVNodeFromDict(self, d):
        """
        Returns the child selector AOV node name from the provided dictionary
        """
    
        pass
    
    
    def getCollectionSelector(self, selectorName):
        """
        Creates the selector for the AOV collection
        """
    
        pass
    
    
    def aovNodeTypes():
        """
        Return the AOV node types supported by this renderer.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    DECODE_TYPE_MERGE = 1
    
    
    DECODE_TYPE_OVERWRITE = 0


class RenderSettingsCallbacks(object):
    """
    Renderers should either extend this class or create a class with the same signature to provide additional render settings callbacks
    """
    
    
    
    def createDefaultNodes(self):
        """
        Create the default nodes for the specific renderer
        """
    
        pass
    
    
    def decode(self, rendererData):
        """
        Decodes any renderer specific render settings data
        """
    
        pass
    
    
    def encode(self):
        """
        Encodes any renderer specific render settings data
        """
    
        pass
    
    
    def getNodes(self):
        """
        Returns the default render settings nodes for the specific renderer
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class NodeExporter(object):
    """
    Helper exporter to encode/decode any nodes
    """
    
    
    
    def __init__(self):
        pass
    
    
    def decode(self, encodedData):
        pass
    
    
    def encode(self):
        pass
    
    
    def setPlugsToIgnore(self, plugsToIgnore):
        pass
    
    
    def warnPlugsToIgnore(self, value):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class BasicNodeExporter(NodeExporter):
    """
    Exporter that is used to export the nodes that have been set
    """
    
    
    
    def getNodes(self):
        pass
    
    
    def setNodes(self, nodes):
        pass



def unregisterCallbacks(renderer, callbacksType='None'):
    pass


def getCallbacks(*args):
    pass


def registerCallbacks(renderer, callbacksType, callbacks):
    pass



CALLBACKS_TYPE_RENDER_SETTINGS = 0

kDefaultNodeAttrMissing = []

kDefaultNodeMissing = []

kAttributesNotExportable = []

rendererCallbacks = {}

CALLBACKS_TYPE_AOVS = 1


