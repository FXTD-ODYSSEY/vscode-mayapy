"""
Class for storing apiVersions, which are the best method for comparing versions. ::

    >>> from pymel import versions
    >>> if versions.current() >= versions.v2008:
    ...     print "The current version is later than Maya 2008"
    The current version is later than Maya 2008
"""

from maya.OpenMaya import MGlobal as _MGlobal

def isRenderNode():
    pass


def installName():
    pass


def isComplete():
    """
    Whether this instance of Maya is 'Unlimited' (deprecated)
    
    :rtype: bool
    """

    pass


def bitness():
    """
    The bitness of python running inside Maya as an int.
    """

    pass


def isUnlimited():
    """
    Whether this instance of Maya is 'Unlimited' (deprecated)
    
    :rtype: bool
    """

    pass


def shortName():
    pass


def fullName():
    pass


def current():
    """
    Get the current version of Maya
    
    :rtype: int
    """

    pass


def is64bit():
    """
    Whether this instance of Maya is 64-bit
    
    :rtype: bool
    """

    pass


def parseVersionStr(versionStr, extension='False'):
    """
    Parse a verbose version string (like the one displayed in the Maya title
    bar) and return the base version.
    
    :Parameters:
        extension : `bool`
            if True, leave the -x64 tag
    
    >>> from pymel.all import *
    >>> versions.parseVersionStr('2008 Service Pack1 x64')
    '2008'
    >>> versions.parseVersionStr('2008 Service Pack1 x64', extension=True)
    '2008-x64'
    >>> versions.parseVersionStr('2008x64', extension=True)
    '2008-x64'
    >>> versions.parseVersionStr('8.5', extension=True)
    '8.5'
    >>> versions.parseVersionStr('2008 Extension 2')
    '2008'
    >>> versions.parseVersionStr('/Applications/Autodesk/maya2009/Maya.app/Contents', extension=True)
    '2009'
    >>> versions.parseVersionStr('C:\Program Files (x86)\Autodesk\Maya2008', extension=True)
    '2008'
    """

    pass


def flavor():
    """
    The 'flavor' of this instance of Maya
    
    Requires ``maya.cmds``.
    
    :rtype: str
    """

    pass


def isEval():
    """
    Whether this instance of Maya is an evaluation edition
    
    Requires ``maya.cmds``.
    
    :rtype: bool
    """

    pass



v2012_HOTFIX3 = 201203

v20165 = 201650

v2012_HOTFIX4 = 201204

v2012_HOTFIX2 = 201202

v2015_SP1 = 201501

_fullName = []

v2014_SP2 = 201404

v2015_SP2 = 201502

v2011_SP1 = 201104

v85 = 200700

v2015_EXT1 = 201506

_is64 = True

v2013 = 201300

v2015_EXT1SP5 = 201507

v2009_EXT1 = 200904

v2015_SP3 = 201505

v2011_HOTFIX1 = 201101

v2011_HOTFIX3 = 201103

v2011 = 201100

v2015 = 201500

v2014_SP3 = 201406

v2014_SP1 = 201402

v2008 = 200800

v2009_SP1A = 200906

v2016 = 201600

v2008_EXT2 = 200806

v2014_EXT1 = 201450

v2016_EXT1SP4 = 201607

v2012_SAP1SP1 = 201217

v2012_SAP1 = 201209

v2017 = 201700

v2012 = 201200

v2014_EXT1SP1 = 201451

v2011_HOTFIX2 = 201102

v2009 = 200900

v2016_EXT1 = 201605

v85_SP1 = 200701

v2012_HOTFIX1 = 201201

v2014_EXT1SP2 = 201459

v2014 = 201400

_current = 20180000

v2010 = 201000

v2018 = 201800


