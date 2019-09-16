"""
Helper class that allows scoping of changes to the current evaluation context.
Normal operation is to use it as a with() scoping object as follows:

    import maya.api.OpenMaya as om
    from maya.api.MDGContextGuard import MDGContextGuard

    ctx_100 = om.MDGContext( 100.0 )
    with MDGContextGuard(ctx_100) as guard:
        print plug.asMDistance() # Gets the value of the plug at time 100.0
    print plug.asMDistance() # Gets the value of the plug at the current time

You can also use it as a regular object when you want to extend the scope
beyond a single method:

    import maya.api.OpenMaya as om
    from maya.api.MDGContextGuard import MDGContextGuard

    def get_guard(time):
        ctx_time = om.MDGContext( time )
        guard = MDGContextGuard( ctx_time )

    guard = get_guard( 100.0 )
    print plug.asMDistance() # Gets the value of the plug at time 100.0
    guard.restore()
    print plug.asMDistance() # Gets the value of the plug at the current time
"""

class MDGContextGuard(object):
    """
    Scoping object to manage changes to the current evaluation context
    """
    
    
    
    def __enter__(self):
        """
        Begin the scope, the work is done in __init__
        """
    
        pass
    
    
    def __exit__(self, object_type, value, traceback):
        """
        Ensure the state is restored if this object goes out of scope
        """
    
        pass
    
    
    def __init__(self, context):
        """
        Initialize the object with a specific context
        """
    
        pass
    
    
    def context(self):
        """
        Return the context that was passed into this object on entry/construction
        """
    
        pass
    
    
    def original_context(self):
        """
        Return the context that was current when this object was entered/constructed
        """
    
        pass
    
    
    def restore(self):
        """
        Restore the context on entry/construction to be the current evaluation context
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



