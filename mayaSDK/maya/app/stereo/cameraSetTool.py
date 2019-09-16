"""
This is a dedicated editor for specifying camera set rigs.  It allows
the artist to preset a multi-rig type.  They can then use the
create menus for quickly creating complicated rigs.
"""

class BaseUI:
    """
    Each region of the editor UI is abstracted into a UI class that
    contains all of the widgets for that objects and relavant callbacks.
    This base class should not be instanced as this is only a container
    for common code.
    """
    
    
    
    def __init__(self, parent):
        """
        Class initialization. We simply hold onto the parent layout.
        """
    
        pass
    
    
    def control(self):
        """
        Return the master control for this UI.
        """
    
        pass
    
    
    def parent(self):
        """
        Return the parent instace of this UI. This can be None.
        """
    
        pass
    
    
    def setControl(self, control):
        """
        Set the pointer to the control handle for this UI.  This is
        the main control that parents or children can reference 
        for UI updates.
        """
    
        pass


class NewCameraSetUI(BaseUI):
    """
    UI for adding 'new' camera set.
    """
    
    
    
    def __init__(self, parent):
        """
        Class constructor
        """
    
        pass
    
    
    def buildLayout(self):
        """
        Construct the UI for this class.
        """
    
        pass
    
    
    def name(self):
        """
        Name of this UI component.
        """
    
        pass
    
    
    def newTemplate(self, *args):
        """
        Create a new template and adding the template to the
        UI layout for user manipulation.
        """
    
        pass
    
    
    def rebuild(self):
        """
        Rebuild the UI.  We find the parent class and tell it
        to kickstart the rebuild.
        """
    
        pass
    
    
    def resetSettings(self, *args):
        """
        Reset to the default settings and rebuild the UI.
        """
    
        pass
    
    
    def resetUI(self):
        """
        Tells all ui templates to reset their ui handles.  This
        is done because this UI templates hold onto some
        local data that must be cleared out before rebuilding
        """
    
        pass
    
    
    def saveSettings(self, *args):
        """
        Call the template manager to store its current settings
        """
    
        pass


class NamingTemplateUI(BaseUI):
    """
    This class encapsulates all of the UI around multi rig naming templates.
    """
    
    
    
    def __init__(self, parent, mgr, template):
        """
        Class initializer.
        """
    
        pass
    
    
    def addLayer(self, *args):
        """
        Add a new layer to this object.
        """
    
        pass
    
    
    def autoCreateCkboxChange(self, args, layer='0'):
        """
        Called when the check box is changed.
        """
    
        pass
    
    
    def buildLayout(self):
        """
        Build a new multi-rig template UI.
        """
    
        pass
    
    
    def cameraSetNameChanged(self, arg):
        pass
    
    
    def createIt(self, *args):
        """
        Function called when the user clicks the 'Create' button.
        This will force the creation of a new rig.
        """
    
        pass
    
    
    def deleteLayer(self, args, layer='0'):
        """
        Called when the delete layer button is clicked.
        """
    
        pass
    
    
    def layerCameraChanged(self, args, layer='0'):
        """
        Called when the option menu group changes.
        """
    
        pass
    
    
    def layerPrefixChanged(self, args, layer='0'):
        """
        Called when the prefix changes for a layer.
        """
    
        pass
    
    
    def layoutForLayer(self, layer):
        """
        Build the UI for the specified layer. We need to access the
        UI data later in callbacks. So we store the data inside
        a dictionary for reference layer.
        """
    
        pass
    
    
    def multiRigNameChanged(self, ui):
        """
        Called when the user changes the name of this multi-rig
        using the supplied text box.
        """
    
        pass
    
    
    def namingPrefixChanged(self, arg):
        """
        Called when the users changes the prefix name used for the
        multi-rig.
        """
    
        pass
    
    
    def removeDef(self, *args):
        """
        Remove this object from the list.
        """
    
        pass
    
    
    def resetUI(self):
        pass


class CameraSetEditor(BaseUI):
    """
    Main class for the camera set editor.
    """
    
    
    
    def __init__(self, parent='None'):
        """
        Class constructor.
        """
    
        pass
    
    
    def buildLayout(self):
        """
        Build the main layout for the class. This will kickstart all
        UI creation for the class. You should have a window instance
        created for the layouts to parent under.
        """
    
        pass
    
    
    def create(self):
        """
        Create a new instance of the window. If there is already a instance
        then show it instead of creating a new instance.
        """
    
        pass
    
    
    def name(self):
        """
        Return the name for this editor.
        """
    
        pass
    
    
    def rebuild(self):
        """
        Force the rebuild of the UI. This happens when
        users create new templates.
        """
    
        pass



def createIt():
    """
    Create a new window instance of the Camera Set Editor.
    """

    pass



gEditorWindowInstance = None


