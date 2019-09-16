"""
RenderLayers, Collections and Overrides are DG nodes they should technically be well-behaved, 
i.e. they should depend only on their local input attributes to compute consistently the same outputs.
In practice, they don't because some collections are traversing connections to populate their content and yet these connections 
may change because of previously applied overrides that will insert nodes in the unique global graph and/or edit connections in it.
This module is tracking apply/unapply/connection override update in a global way (context) to insure that collection's content are correctly
evaluated when they are applied.

Example: if we have something like this:

renderLayer1
  - collection1 with pSphere1
    - collection1_shaders1 gathering shaders assigned to pSphere1 (lambert1)
      - abs override color to yellow
    - materialOverride1 assigning blinn1 to pSphere1
    - collection1_shaders2 gathering shaders assigned to pSphere1 (blinn1 if materialOverrides is enabled, lambert1 otherwise)
      - abs override color to green

On apply, collection1_shaders2 must reevaluate its content depending on wheter or not materialOverride1 is enabled.
On the other hand, collection1_shaders1 remains unchanged because it is evaluated before materialOverride1.

This context module ensures that collection1_shaders1 doesn't listen to materialOverride1 
(on apply, on enable/disable, on connection change) but collection1_shaders2 does. 

On apply: 
 > apply renderLayer1 
   > evaluate collection1 content
   > deactivate collection1's selector
   > apply collection1
     > evaluate collection1_shader1 content
     > deactivate collection1_shaders1's selector
     > apply collection1_shaders1
       > override lambert1's color to yellow
     > assign blinn1 to pSphere1
     > evaluate collection1_shader2 content
     > deactivate collection1_shaders2's selector
     > apply collection1_shaders2
       > override blinn1's color to green
   > reactivate all selectors from the first applied element (i.e. renderLayer1)
   
On materialOverride1 update (enable/disable/connection changed, when renderLayer1 is visible):
 > create a PivotGuard on materialOverride1. This will deactivate all the selectors BEFORE materialOverride1
   but let the ones after activated.
 > update materialOverride1
 > look if there's a collection AFTER that materialOverride1 to see if any is dirty 
   (i.e. they may need to reevaluate their content due to the connection change). collection1_shaders2 will be.
   It will then create a PivotGuard around collection1_shaders2 and reapply the layer.
   The PivotGuard guaranties that collection1 and collection1_shaders1 selectors and protect these collections 
   from being unapplied/reapplied, since they would remain unchanged anyway.
"""

class StackContext(object):
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, element):
        pass
    
    
    def empty():
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    stack = []


class PivotGuard:
    """
    Protects every override that is before the pivot in application order from
    being unapplied or applied. Also deactivate all the selectors before pivot.
    The pivot can be either a collection or an override.
    This is useful for partially reapplying a layer from a certain point.
    """
    
    
    
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, pivot):
        pass
    
    
    def accepts(override):
        pass
    
    
    lockedNames = set()


class ApplyContext(StackContext):
    def __exit__(self, type, value, traceback):
        pass
    
    
    def conclude(self):
        pass


class ApplyCollectionContext(ApplyContext):
    def conclude(self):
        pass


class ApplyLayerContext(ApplyContext):
    def conclude(self):
        pass



def _getCollectionsBefore(pivot):
    pass


def applyOverride(f):
    pass


def _getRoot(element):
    pass


def updateConnectionOverride(f):
    pass


def stateGuards(ignoreReferenceEdit='True', enableSceneObservers='False'):
    pass


def unapplyLayer(f):
    pass


def unapplyCollection(f):
    pass


def applyLayer(f):
    """
    # decorators for keeping track of application, unapplication and update context
    """

    pass


def applyCollection(f):
    pass


def unapplyOverride(f):
    pass



