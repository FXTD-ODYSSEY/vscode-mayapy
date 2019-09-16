"""
This module is used to notify of progress during layer switching, which
can be a lengthy operation.
"""

class _Context(object):
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, node='None'):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class RenderLayerSwitchObservable(object):
    def __init__(self):
        pass
    
    
    def addRenderLayerSwitchObserver(self, obsMethod):
        pass
    
    
    def info(self):
        """
        Returns a tuple containing the layer name (or None if switching to master) and the override name being applied/unapplied
        """
    
        pass
    
    
    def notifyRenderLayerSwitchObserver(self):
        pass
    
    
    def progress(self):
        """
        Returns the current progress of the switching process in range 0-1
        """
    
        pass
    
    
    def removeRenderLayerSwitchObserver(self, obsMethod):
        pass
    
    
    def getInstance():
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class ApplyApplyOverrideContext(_Context):
    def __exit__(self, type, value, traceback):
        pass


class SwitchLayerContext(_Context):
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, oldLayer, newLayer):
        pass


class UnapplyOverrideContext(_Context):
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, ovr):
        pass


class UnapplyApplyOverrideContext(_Context):
    def __exit__(self, type, value, traceback):
        pass


class ApplyOverrideContext(_Context):
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, ovr):
        pass



