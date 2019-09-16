"""
This module defines proxy observables for receiving notifications from
Maya.  The proxy observables have an observer reference count that is used
to attach to the Maya notification when greater than zero, and detach from
the Maya notification when the reference count falls to zero.

In this way, no time is spent processing Maya notifications when no
observers are listening.
"""

from maya.app.renderSetup.model.observable import Observable

class ObservableProxy(Observable):
    """
    Base proxy observable class.
    
    This class provides a no-op implementation of activate() and deactivate().
    """
    
    
    
    def __del__(self):
        pass
    
    
    def activate(self):
        pass
    
    
    def deactivate(self):
        pass


class ObservableDGProxy(ObservableProxy):
    """
    Proxy observable class for DG callbacks.
    """
    
    
    
    def __init__(self, cbName, cb='None', cbArgs='None'):
        pass
    
    
    def activate(self):
        pass
    
    
    def addItemObserver(self, obs):
        pass
    
    
    def deactivate(self):
        pass
    
    
    def removeItemObserver(self, obs):
        pass


class ObservableDagProxy(ObservableDGProxy):
    """
    Proxy observable class for DAG callbacks.
    """
    
    
    
    def __init__(self, cbName, dagCbTypes, cb):
        pass
    
    
    def activate(self):
        pass
    
    
    def deactivate(self):
        pass



logger = None


