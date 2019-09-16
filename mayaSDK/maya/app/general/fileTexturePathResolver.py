"""
##############################################################################
#
# Utility functions for resolving file paths for Maya's file texture node.
# These utilities are used for dealing with UV tiling and frame numbering in
# the file name and can be used to get the current pattern/preset and list
# of matching files.
#
##############################################################################
"""

def getFilePatternString(filePath, useFrameExtension, uvTilingMode):
    """
    Given a path to a file and hints about UV tiling and frame extension usage,
    convert the path to a version with appropriate tags marking the UV tile
    and frame number.
    """

    pass


def _splitPath(filePath):
    """
    ##############################################################################
    # Private Utilities
    ##############################################################################
    """

    pass


def _patternToRegex(pattern):
    pass


def computeUVForFile(filePath, filePattern):
    """
    Given a path to a file and the UV pattern it matches compute the 0-based UV
    tile indicated by the file name. If the filePath or pattern are poorly
    formed then (0,0) is returned.
    """

    pass


def findAllFilesForPattern(pattern, frameNumber):
    """
    Given a path, possibly containing tags in the file name, find all files in
    the same directory that match the tags. If none found, just return pattern
    that we looked for.
    """

    pass


def computeUVForFiles(filePaths, filePattern):
    """
    Given a collection of paths to a file and the UV pattern it matches compute
    the 0-based UV tile indicated by the file name. If a filePath or the pattern
    are poorly formed then (0,0) is returned for that path.
    """

    pass



_zeroBasedRegex = None

_frameExtensionRegex = None

_taggedZeroBasedRegex = None

_frameTag = '<f>'

_uTag = '<u>'

_udimRegex = None

_taggedOneBasedRegex = None

_oneBasedRegex = None

_UTag = '<U>'

_udimTag = '<UDIM>'

_vTag = '<v>'

_VTag = '<V>'


