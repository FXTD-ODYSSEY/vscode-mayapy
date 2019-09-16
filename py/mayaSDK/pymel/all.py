from pymel.core.modeling import *
from pymel.core.nodetypes import *
from pymel.core.uitypes import *
from pymel.core.animation import *
from pymel.core.other import *
from pymel.core.effects import *
from pymel.core.language import *
from pymel.core.windows import *
from pymel.core.context import *
from pymel.core.system import *
from pymel.util.arrays import *
from pymel.core.rendering import *
from pymel.core.general import *

class LazyLoader(object):
    """
    A data descriptor that delays instantiation of an object
    until it is first accessed.
    """
    
    
    
    def __get__(self, obj, objtype):
        pass
    
    
    def __init__(self, name, creator, *creatorArgs, **creatorKwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



doFinalize = True


