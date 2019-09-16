from maya.app.edl.fcp import *

import maya.OpenMayaMPx as OpenMayaMPx

class ImportExport(OpenMayaMPx.MPxCommand):
    def __del__(self):
        pass
    
    
    def __init__(self):
        pass


class Exporter(ImportExport):
    def __init__(self):
        pass
    
    
    def doIt(self, fileName):
        pass
    
    
    def setAllowPlayblast(self, allow):
        """
        If true, will re-playblast of all shots whose clips are out of date
        or non-existent.
        """
    
        pass


class Importer(ImportExport):
    def __init__(self):
        pass
    
    
    def doIt(self, fileName):
        """
        Reads an EDL file into Maya. Will generate shots, tracks and audio in Maya that 
        corresponds to the tracks and clips in the EDL.
        """
    
        pass
    
    
    def setStartFrameOverride(self, frame):
        pass



def audioClipCompare(a, b):
    pass


def doMel(*args, **kwargs):
    """
    Takes as input a string containing MEL code, evaluates it, and returns the result.
    
    This function takes a string which contains MEL code and evaluates it using 
    the MEL interpreter. The result is converted into a Python data type and is 
    returned.
    
    If an error occurs during the execution of the MEL script, a Python exception
    is raised with the appropriate error message.
    """

    pass


def getTimeCode():
    pass


def _setTimeCode(timecode):
    pass


def doImport(fileName, useStartFrameOverride, startFrame):
    """
    Imports the specified file using the EDL Importer class.
    """

    pass


def _nameToNode(name):
    pass


def doExport(fileName, allowPlayblast):
    """
    Exports the Maya sequence using the EDL Exporter class.
    """

    pass


def getShotsResolution():
    """
    Returns the video resolution of the sequencer if all the shots have the same resolution 
    Otherwise it returns False, 0, 0
    """

    pass


def videoClipCompare(a, b):
    pass


def _getValidClipObjectName(clipName, isVideo):
    pass



mayaFrameRates = {}


