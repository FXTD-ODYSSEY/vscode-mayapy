"""
The overridden attribute manager is a singleton that observes the scene to
react to attribute changes.  If the attribute change is on an attribute
that is overridden by render setup, the attribute manager will attempt to
take the value change and reproduce it on the override itself.

This allows for convenient workflows like using direct manipulation on an
object with a value override, where the value is actually written back to
the override.

Apply value override nodes conditionally implement the passive output plug
behavior, through a chain of responsibility.  A passive output allows
setting its destination input.  If this destination input is connected to
an apply override node, the overridden attribute manager asks the
highest-priority apply override node to write the value to its
corresponding override, if it's enabled, else pass the request to the next
lower-priority apply override node.  The chain ends by writing into the
original.  If the highest-priority apply override node returns true from
isPassiveOutput(), this means that the overridden attribute write must
succeed, as one of the apply override nodes in the chain will accept the
write.

Autokey functionality is supported in this framework: in autokey mode, we
query the auto keyer to ask if an overridden attribute would be auto-keyed.
If so, we add the override attribute to the list of attributes the auto
keyer will add keys to.  See the autoKey render setup module and the
autoKeyframe command for more information.

Note that it is understood that changing the override value will cause all
overridden attributes to change.
"""

class OverriddenAttributeManager(object):
    """
    Observe and react to overridden attribute changes.
    
    The overridden attribute manager attempts to convert changes to
    overridden attributes to changes to overrides.  See the module
    documentation for more details.
    
    The overridden attribute manager is only active when a render layer
    other than the default (or master) layer is visible.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def aboutToDelete(self):
        """
        Final clean up before the manager is destroyed.
        """
    
        pass
    
    
    def addAttributeChangeObservation(self):
        """
        Start observing DG attribute changes.
        """
    
        pass
    
    
    def onAttributeChanged(self, msg, plg, otherPlug, clientData):
        pass
    
    
    def onRenderLayerChanged(self):
        """
        Called after the visible render layer has been changed.
        """
    
        pass
    
    
    def removeAttributeChangeObservation(self):
        """
        End observation of DG attribute changes.
        """
    
        pass
    
    
    def renderSetupAdded(self):
        """
        Called just after the render setup node has been added.
        """
    
        pass
    
    
    def renderSetupPreDelete(self):
        """
        Called just before the render setup node is deleted.
        
        Unregisters from visible render layer and attribute change
        observation.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def isDefaultRenderLayerVisible():
    pass


def initialize():
    pass


def finalize():
    pass


def instance():
    pass



_instance = OverriddenAttributeManager()


