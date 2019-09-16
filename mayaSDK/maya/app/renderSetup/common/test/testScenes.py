from collections import namedtuple

Instance = namedtuple('Instance', ('transform', 'shape', 'generator', 'materials'))


Material = namedtuple('Material', ('shadingEngine', 'surfaceShader', 'displacementShader', 'volumeShader'))



def createSphereWithAllShaders():
    """
    Creates a poly sphere (pSphere1) with the following material.
     
    place2dTexture1 ----> noise1 ----> bump1 ----> lambert1 ----\ 
                                        displacementShader1 ----- initialShadingGroup
                                                 volumeFog1 ----/
    You can see it with: 
    import maya.app.renderSetup.common.test.testScenes as scenes; scenes.createSphereWithAllShaders()
    """

    pass


def createSurfaceShader(color):
    """
    Creates a Surface Shader with the specified color.
    Returns a tuple (shaderName, shadingEngineName)
    """

    pass


def createAllShaders():
    """
    place2dTexture# ----> noise# ----> bump# ----> blinn# ----\ 
                                      displacementShader# ----- shadingGroup#
                                               volumeFog# ----/
    """

    pass


def assignShadingEngine(shape, shadingEngine, components='None'):
    """
    Assign shading engine to shape.
    "components" is an optional list of mesh face indices or nurbs surface patch indices
    that can be used to specify per-face shading engine assignment.
    A mesh index is given by an integer >= 0.
    A surface patch is given by a tuple (span, section) where span and section are integers >= 0.
    """

    pass


def createSceneWithMaterials():
    """
    Create a test scene composed of
    - 2 polySphere (instances of the same shape)
    - 2 nurbsSphere (instances of the same shape)
    First instance has whole shape material assignment.
    Second instance has per-face shape material assignment.
    - 1 polyCube without any per-face
    - 1 directionalLight
    
    Returns a set of Instance (named tuples) containing these 6 objects.
    
    To see it in maya, just run python script:
    import maya.app.renderSetup.common.test.testScenes as scenes; scenes.createSceneWithMaterials()
    """

    pass



DefaultMaterial = ()


