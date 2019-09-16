"""
This module provides a context manager to have a convenient
wait cursor guard mechanism.  It ensures that the wait cursor is started
and stopped at expected time.
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication

class WaitCursorMgr(object):
    """
    Safe way to manage wait cursors
    
    Example:
        with WaitCursorMgr():
            doSomeHeavyOperation()
    """
    
    
    
    def __enter__(self):
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def waitCursor():
    """
    wait cursor decorator to manage the cursor scope
    
    Example:
        @waitCursor()
        def doSomeHeavyOperation():
    """

    pass



