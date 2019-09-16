import exceptions

from maya.app.renderSetup.model.selector import *
from maya.app.renderSetup.model.issue import *

class Issue2016R2Collection(Issue):
    def __init__(self, resolveCallback='None'):
        pass


class ConvertDialog:
    def __init__(self):
        pass
    
    
    def onHelp(self, *args):
        pass
    
    
    def onNo(self, *args):
        pass
    
    
    def onYes(self, *args):
        pass
    
    
    def prompt(self):
        pass


class ConversionFailed(exceptions.Exception):
    __weakref__ = None


class Observer2016R2(object):
    def __init__(self):
        pass
    
    
    def activate(self):
        pass
    
    
    def assistedResolve(self):
        pass
    
    
    def autoResolve(self):
        pass
    
    
    def deactivate(self):
        pass
    
    
    def resolve(self):
        pass
    
    
    def instance():
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def setAutoConvertFlag(value):
    pass


def convertCollection(collection):
    """
    Convert the encoded data of a collection of 2016 R2 (using a BasicSelector) into 
    a collection with a collection using a SimpleSelector.
    Creates subcollections to simulate the old "include hierarchy".
    Creates subcollections for shader overrides since they now apply to shading engines.
    """

    pass


def removeAutoConvertFlag():
    pass


def sceneHasBasicSelector():
    pass


def _splitOverrides(ovrs):
    pass


def convert2016R2(encodedData):
    """
    This is the function to call to convert any encodedData (partial or not).
    It will find all the collections in encodedData and convert them to use simpleSelector if they do not already.
    See convertCollection() for more details.
    """

    pass


def getAutoConvertFlag():
    pass


def hasAutoConvertFlag():
    pass


def _createSubCollection(name, filterType, customs, children):
    pass


def _findCollections(encodedData):
    """
    yields all the collection dictionary in the encodedData
    """

    pass



kIssueShortDescription = []

kConvertHelp = []

kConversionCompletedMessage = []

kConvertMessage = []

kConversionCompletedForMessage = 'Conversion successfully completed for collections: %s.'

kConvertBatchError = []

kRelativeHelpLink = 'RENDER_SETUP_COMPATIBLE'

kOptionVarAutoConvert = 'renderSetup_autoConvert2016R2Collections'

kConversionFailedTitle = []

kConversionFailedForMessage = 'Conversion failed for collections: %s.'

kConversionCompletedOk = []

DECODE_AND_MERGE = 1

kConversionCompletedTitle = []

kConversionCompletedWithErrorsMessage = []

kConvertTitle = []

kConvertYes = []

kConvertNo = []


