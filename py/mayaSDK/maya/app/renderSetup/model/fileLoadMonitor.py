"""
This module monitors file loads (including imports and reference load) and 
    displays warning messages if it discovers that new loaded files are not 
    compatible with the current renderSetup mode
    
    Implementation details:
    In order to determine if the loaded file is compatible with the current Maya state
    we first determine the type the loaded file based on its content. Then depending 
    on the current Maya RenderSetup mode error messages are displayed if incompatibilities
    are identified
"""

def onReadEnd(data):
    pass


def finalize():
    pass


def initialize():
    pass


def preLoadInventory():
    pass


def onReadStart(data):
    pass


def getLayerInventory():
    pass


def _getErrorSwitchToRenderLayerIfNeeded():
    pass



kErrorSwitchToRenderLayer = []

kErrorCombiningLegacyToNew = []

kErrorSwitchToRenderSetup = []

kErrorCombiningNewToLegacy = []

afterCallback = None

kWarningInactiveRenderSetup = []

beforeCallback = None


