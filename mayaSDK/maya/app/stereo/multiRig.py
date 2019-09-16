"""
Multi-rigs are the collection of stereo camera rigs contained by a camera set.
This class provides a generic way of defining a multi-rig and creating them.
A multi-rig has 2 parts:

    - Naming information
    - Layer information

Each layer has information on how to populate that layer. It includes

    - Prefix the name of the layer
        - The type of stereo camera
    - Whether an object set should be created for that layer.
"""

class NamingTemplateManager:
    """
    This manages the list of naming templates used by the editor.  Users
    can create customized templates.  Any operation that changes a template:
       - New
       - Delete
       - Modify
    
    Will force the storage of that changed value back into the optionVar
    Thus the optionVar is always in-sync with the manager.  It is possible
    to create more than one template manager; however, multiple instances
    may stomp over each other and provide un-predictable results.
    """
    
    
    
    def __init__(self):
        """
        Class constructor.  Retreive the optionVar for the manager and read 
        the contents.  If the option var does not exist, we create it and
        populate the default values.
        """
    
        pass
    
    
    def addNew(self):
        """
        Create a new template from the default form.
        """
    
        pass
    
    
    def defaultTemplate(self):
        """
        Return the default template.
        """
    
        pass
    
    
    def deleteTemplate(self, template):
        """
        Remove the name template from the template manager.
        """
    
        pass
    
    
    def resetToDefault(self):
        """
        Reset to the default settings.
        """
    
        pass
    
    
    def retreive(self):
        """
        Retreives the template information from the option var that
        contains this data.
        """
    
        pass
    
    
    def store(self):
        """
        Store the template information back onto the option var.
        """
    
        pass
    
    
    def templates(self):
        """
        Return the list of templates.
        """
    
        pass


class NamingTemplate:
    """
    This class encapsulates the naming convension when creating new camera set
    multi rigs.
    """
    
    
    
    def __init__(self, mgr, template='None'):
        """
        Class initializer.
        """
    
        pass
    
    
    def addLayer(self):
        """
        Add a new layer to this object.
        """
    
        pass
    
    
    def autoCreateSet(self, layer):
        """
        Query the value for the auto create object set option by layer id.
        """
    
        pass
    
    
    def camSetPrefix(self):
        """
        Returns the naming prefix to append to new cameras & sets.
        """
    
        pass
    
    
    def cameraSetNodeType(self):
        """
        Return the node type for the camera set.  This information is used
        to create a new camera set.
        """
    
        pass
    
    
    def checkMultibyte(self):
        pass
    
    
    def create(self, *args):
        """
        Create the Maya nodes per the specification of this template.
        """
    
        pass
    
    
    def deleteLayer(self, layer='0'):
        """
        Remove the specified layer from this template.
        """
    
        pass
    
    
    def gatherFromString(self, sval):
        """
        Takes a string previously packed using 'stringify' and restores
        the state to variables on this class.
        """
    
        pass
    
    
    def layerPrefixForLayer(self, layer):
        """
        Query the value for the layer prefix using layer id.
        """
    
        pass
    
    
    def layers(self):
        """
        Returns the number of layers this template currently holds.
        """
    
        pass
    
    
    def rigName(self):
        """
        Returns the name of this multi rig.
        """
    
        pass
    
    
    def rigTypeForLayer(self, layer):
        """
        Query the name for the rigType for the specified layer.
        """
    
        pass
    
    
    def setAutoCreateSet(self, create='1', layer='0'):
        """
        Set the auto create flag.
        """
    
        pass
    
    
    def setCamSetPrefix(self, camSetPre):
        """
        Sets the prefix name.
        """
    
        pass
    
    
    def setCameraSetNodeType(self, nodeType):
        pass
    
    
    def setLayerCamera(self, camera, layer='0'):
        """
        Change the camera value for the specified layer.
        """
    
        pass
    
    
    def setLayerPrefix(self, prefix, layer):
        """
        Change the prefix value for the layer.
        """
    
        pass
    
    
    def setRigName(self, name):
        """
        Sets the name for this multi-rig.
        """
    
        pass
    
    
    def store(self):
        """
        Forces the storage of the changes the option var back into the
        optionVar.
        """
    
        pass
    
    
    def stringify(self):
        """
        Converts the data members of this class into a string format.
        This is so we can pack the data into a Maya optionVar
        """
    
        pass



def clearDefaultSwapOV():
    pass


def getDefaultRig():
    """
    # Makes sure the plug-in is loaded.
    """

    pass


def swapDefault(oldDefault, newDefault):
    pass



gDefaultTemplates = []

g3RigSetup = ()

SwapRigsOptionVar = 'StereoCameraAlwaysSwapForDefault'


