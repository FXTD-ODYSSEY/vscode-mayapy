from maya.app.renderSetup.lightEditor.model.group import LightEditorGroup

class LightEditor(LightEditorGroup):
    """
    Singleton group item that is the root of the light editor items.
    
    The light editor node is a singleton: at most one can exist in a scene.
    It is not implemented as a default node, and therefore is not created
    on file new, but rather created on demand.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def ancestors(self):
        """
        Returns a single-element deque with the render setup node itself.
        """
    
        pass
    
    
    def createGroupItem(*args, **kwargs):
        pass
    
    
    def createLightItem(*args, **kwargs):
        pass
    
    
    def findEditorItem(self, obj):
        pass
    
    
    def isAbstractClass(self):
        pass
    
    
    def parent(self):
        """
        Returns None, as the render setup node is the root of the hierarchy.
        """
    
        pass
    
    
    def postConstructor(self):
        pass
    
    
    def rebuildScene(self):
        pass
    
    
    def creator():
        pass
    
    
    def initializer():
        pass
    
    
    kTypeId = None
    
    
    kTypeName = 'lightEditor'



def instance():
    """
    Return the light editor singleton node, creating it if required.
    """

    pass


def hasInstance():
    """
    Return true if the light editor node exists
    """

    pass


def _createInstance(*args, **kwargs):
    pass



_LIGHT_EDITOR_NODE_NAME = ':lightEditor'

kLightEditorNodeNameMismatch = []

_LIGHT_EDITOR_NODE_TYPE = 'lightEditor'


