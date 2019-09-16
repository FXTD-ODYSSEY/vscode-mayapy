"""
This module centralizes type IDs for all render setup nodes.  The
range of reserved node type IDs for render setup is 0x58000370 to
0x580003FF, inclusive.  See file Maya/src/Plugins/NodeIdList.txt.
"""

def isRenderSetupType(typeID):
    """
    Args:
        typeID: the MTypeId to test
    
    Returns: True if it is in the range of reserved RenderSetup class types otherwise False
    """

    pass



materialOverride = None

connectionOverride = None

aovCollection = None

applyAbs3FloatsOverride = None

applyAbsOverride = None

applyRelOverride = None

relOverride = None

applyRelIntOverride = None

applyAbsEnumOverride = None

basicSelector = None

simpleSelector = None

aovChildCollection = None

relUniqueOverride = None

shaderOverride = None

renderLayer = None

applyAbsStringOverride = None

listItem = None

connectionUniqueOverride = None

applyRel3FloatsOverride = None

lightEditorLight = None

override = None

selector = None

applyAbsBoolOverride = None

collection = None

applyConnectionOverride = None

applyRel2FloatsOverride = None

lightsChildCollection = None

renderSettingsCollection = None

applyOverride = None

applyAbs2FloatsOverride = None

renderSetup = None

applyAbsFloatOverride = None

arnoldAOVChildSelector = None

lightsCollection = None

valueOverride = None

applyRelFloatOverride = None

absUniqueOverride = None

absOverride = None

applyAbsIntOverride = None

lightEditor = None

renderSettingsChildCollection = None

childNode = None

lightEditorItem = None

lightEditorGroup = None


