"""
AOV information is encoded and decoded by 3rdParty renderers. These renderers
register AOV callbacks by deriving from or implementing an interface identical
to the AOVCallbacks interface located in the rendererCallbacks module. This
class is then registered by calling:

rendererCallbacks.registerCallbacks(rendererName, 
                                    rendererCallbacks.CALLBACKS_TYPE_AOVS
                                    callbacksClassImplementation)
"""

def encode():
    """
    Encode all the attribute values related to the AOVs of a specific renderer
    """

    pass


def _getCurrentRenderer():
    pass


def decode(*args, **kwargs):
    pass



kRendererMismatch = []


