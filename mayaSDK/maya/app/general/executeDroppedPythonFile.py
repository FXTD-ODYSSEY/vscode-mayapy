def executeDroppedPythonFile(droppedFile, obj):
    """
    Called by Maya when you Drag and Drop a Python (.py) file onto the viewport.
    
    Here we load the input python file and try and execute the function:
    onMayaDroppedPythonFile()
    
    Note: Any main code inside the Python file will also be executed, but since
          it's being imported into another module (__name__ != "__main__")
    
    Parameters:
        droppedFile - The Python file dropped onto the viewport
        obj - The object under the mouse
    
    eturn True if we sucessfully called function: onMayaDroppedPythonFile()
    
    Example:
    - An example of a DnD Python file would be:
    
    MayaDropPythonTest.py:
        import maya
    
        def onMayaDroppedPythonFile(obj):
            print('onMayaDroppedPythonFile(' + obj + ')')
            if obj:
                maya.mel.eval('createAndAssignShader blinn ' + obj)
    
        if __name__ == "__main__":
            print("MayaDropPythonTest.py is being run directly")
        else:
            print("MayaDropPythonTest.py is being imported into another module")
    
    When we DnD this file onto an object in the viewport the output would be:
        MayaDropPythonTest.py is being imported into another module
        onMayaDroppedPythonFile(pSphere1)
    """

    pass



MY_DROP_FUNC = 'onMayaDroppedPythonFile'


