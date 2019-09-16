from PySide2.QtWidgets import QWidget as _QWidget
from PySide2.QtGui import QPaintDevice as _QPaintDevice
from PySide2.QtCore import QObject as _QObject

class _Object(object):
    __dict__ = None


class QGLFramebufferObject(_QPaintDevice):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def attachment(*args, **kwargs):
        pass
    
    
    def bind(*args, **kwargs):
        pass
    
    
    def devType(*args, **kwargs):
        pass
    
    
    def drawTexture(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def handle(*args, **kwargs):
        pass
    
    
    def isBound(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def metric(*args, **kwargs):
        pass
    
    
    def paintEngine(*args, **kwargs):
        pass
    
    
    def release(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    def texture(*args, **kwargs):
        pass
    
    
    def toImage(*args, **kwargs):
        pass
    
    
    def bindDefault(*args, **kwargs):
        pass
    
    
    def blitFramebuffer(*args, **kwargs):
        pass
    
    
    def hasOpenGLFramebufferBlit(*args, **kwargs):
        pass
    
    
    def hasOpenGLFramebufferObjects(*args, **kwargs):
        pass
    
    
    Attachment = None
    
    
    CombinedDepthStencil = None
    
    
    Depth = None
    
    
    NoAttachment = None
    
    
    __new__ = None


class QGLWidget(_QWidget):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def autoBufferSwap(*args, **kwargs):
        pass
    
    
    def bindTexture(*args, **kwargs):
        pass
    
    
    def colormap(*args, **kwargs):
        pass
    
    
    def context(*args, **kwargs):
        pass
    
    
    def deleteTexture(*args, **kwargs):
        pass
    
    
    def doneCurrent(*args, **kwargs):
        pass
    
    
    def doubleBuffer(*args, **kwargs):
        pass
    
    
    def drawTexture(*args, **kwargs):
        pass
    
    
    def event(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def glDraw(*args, **kwargs):
        pass
    
    
    def glInit(*args, **kwargs):
        pass
    
    
    def grabFrameBuffer(*args, **kwargs):
        pass
    
    
    def initializeGL(*args, **kwargs):
        pass
    
    
    def initializeOverlayGL(*args, **kwargs):
        pass
    
    
    def isSharing(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def makeCurrent(*args, **kwargs):
        pass
    
    
    def makeOverlayCurrent(*args, **kwargs):
        pass
    
    
    def overlayContext(*args, **kwargs):
        pass
    
    
    def paintEngine(*args, **kwargs):
        pass
    
    
    def paintEvent(*args, **kwargs):
        pass
    
    
    def paintGL(*args, **kwargs):
        pass
    
    
    def paintOverlayGL(*args, **kwargs):
        pass
    
    
    def qglClearColor(*args, **kwargs):
        pass
    
    
    def qglColor(*args, **kwargs):
        pass
    
    
    def renderPixmap(*args, **kwargs):
        pass
    
    
    def renderText(*args, **kwargs):
        pass
    
    
    def resizeEvent(*args, **kwargs):
        pass
    
    
    def resizeGL(*args, **kwargs):
        pass
    
    
    def resizeOverlayGL(*args, **kwargs):
        pass
    
    
    def setAutoBufferSwap(*args, **kwargs):
        pass
    
    
    def setColormap(*args, **kwargs):
        pass
    
    
    def swapBuffers(*args, **kwargs):
        pass
    
    
    def updateGL(*args, **kwargs):
        pass
    
    
    def updateOverlayGL(*args, **kwargs):
        pass
    
    
    def convertToGLFormat(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QGLFormat(_Object):
    def __copy__(*args, **kwargs):
        pass
    
    
    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
    
        pass
    
    
    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
    
        pass
    
    
    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
    
        pass
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
    
        pass
    
    
    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
    
        pass
    
    
    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
    
        pass
    
    
    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
    
        pass
    
    
    def accum(*args, **kwargs):
        pass
    
    
    def accumBufferSize(*args, **kwargs):
        pass
    
    
    def alpha(*args, **kwargs):
        pass
    
    
    def alphaBufferSize(*args, **kwargs):
        pass
    
    
    def blueBufferSize(*args, **kwargs):
        pass
    
    
    def depth(*args, **kwargs):
        pass
    
    
    def depthBufferSize(*args, **kwargs):
        pass
    
    
    def directRendering(*args, **kwargs):
        pass
    
    
    def doubleBuffer(*args, **kwargs):
        pass
    
    
    def greenBufferSize(*args, **kwargs):
        pass
    
    
    def hasOverlay(*args, **kwargs):
        pass
    
    
    def majorVersion(*args, **kwargs):
        pass
    
    
    def minorVersion(*args, **kwargs):
        pass
    
    
    def plane(*args, **kwargs):
        pass
    
    
    def profile(*args, **kwargs):
        pass
    
    
    def redBufferSize(*args, **kwargs):
        pass
    
    
    def rgba(*args, **kwargs):
        pass
    
    
    def sampleBuffers(*args, **kwargs):
        pass
    
    
    def samples(*args, **kwargs):
        pass
    
    
    def setAccum(*args, **kwargs):
        pass
    
    
    def setAccumBufferSize(*args, **kwargs):
        pass
    
    
    def setAlpha(*args, **kwargs):
        pass
    
    
    def setAlphaBufferSize(*args, **kwargs):
        pass
    
    
    def setBlueBufferSize(*args, **kwargs):
        pass
    
    
    def setDepth(*args, **kwargs):
        pass
    
    
    def setDepthBufferSize(*args, **kwargs):
        pass
    
    
    def setDirectRendering(*args, **kwargs):
        pass
    
    
    def setDoubleBuffer(*args, **kwargs):
        pass
    
    
    def setGreenBufferSize(*args, **kwargs):
        pass
    
    
    def setOption(*args, **kwargs):
        pass
    
    
    def setOverlay(*args, **kwargs):
        pass
    
    
    def setPlane(*args, **kwargs):
        pass
    
    
    def setProfile(*args, **kwargs):
        pass
    
    
    def setRedBufferSize(*args, **kwargs):
        pass
    
    
    def setRgba(*args, **kwargs):
        pass
    
    
    def setSampleBuffers(*args, **kwargs):
        pass
    
    
    def setSamples(*args, **kwargs):
        pass
    
    
    def setStencil(*args, **kwargs):
        pass
    
    
    def setStencilBufferSize(*args, **kwargs):
        pass
    
    
    def setStereo(*args, **kwargs):
        pass
    
    
    def setSwapInterval(*args, **kwargs):
        pass
    
    
    def setVersion(*args, **kwargs):
        pass
    
    
    def stencil(*args, **kwargs):
        pass
    
    
    def stencilBufferSize(*args, **kwargs):
        pass
    
    
    def stereo(*args, **kwargs):
        pass
    
    
    def swapInterval(*args, **kwargs):
        pass
    
    
    def testOption(*args, **kwargs):
        pass
    
    
    def defaultFormat(*args, **kwargs):
        pass
    
    
    def defaultOverlayFormat(*args, **kwargs):
        pass
    
    
    def fromSurfaceFormat(*args, **kwargs):
        pass
    
    
    def hasOpenGL(*args, **kwargs):
        pass
    
    
    def hasOpenGLOverlays(*args, **kwargs):
        pass
    
    
    def openGLVersionFlags(*args, **kwargs):
        pass
    
    
    def setDefaultFormat(*args, **kwargs):
        pass
    
    
    def setDefaultOverlayFormat(*args, **kwargs):
        pass
    
    
    def toSurfaceFormat(*args, **kwargs):
        pass
    
    
    CompatibilityProfile = None
    
    
    CoreProfile = None
    
    
    NoProfile = None
    
    
    OpenGLContextProfile = None
    
    
    OpenGLVersionFlag = None
    
    
    OpenGLVersionFlags = None
    
    
    OpenGL_ES_CommonLite_Version_1_0 = None
    
    
    OpenGL_ES_CommonLite_Version_1_1 = None
    
    
    OpenGL_ES_Common_Version_1_0 = None
    
    
    OpenGL_ES_Common_Version_1_1 = None
    
    
    OpenGL_ES_Version_2_0 = None
    
    
    OpenGL_Version_1_1 = None
    
    
    OpenGL_Version_1_2 = None
    
    
    OpenGL_Version_1_3 = None
    
    
    OpenGL_Version_1_4 = None
    
    
    OpenGL_Version_1_5 = None
    
    
    OpenGL_Version_2_0 = None
    
    
    OpenGL_Version_2_1 = None
    
    
    OpenGL_Version_3_0 = None
    
    
    OpenGL_Version_3_1 = None
    
    
    OpenGL_Version_3_2 = None
    
    
    OpenGL_Version_3_3 = None
    
    
    OpenGL_Version_4_0 = None
    
    
    OpenGL_Version_4_1 = None
    
    
    OpenGL_Version_4_2 = None
    
    
    OpenGL_Version_4_3 = None
    
    
    OpenGL_Version_None = None
    
    
    __new__ = None


class QGLContext(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def bindTexture(*args, **kwargs):
        pass
    
    
    def chooseContext(*args, **kwargs):
        pass
    
    
    def colorIndex(*args, **kwargs):
        pass
    
    
    def contextHandle(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def deleteTexture(*args, **kwargs):
        pass
    
    
    def device(*args, **kwargs):
        pass
    
    
    def deviceIsPixmap(*args, **kwargs):
        pass
    
    
    def doneCurrent(*args, **kwargs):
        pass
    
    
    def drawTexture(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def initialized(*args, **kwargs):
        pass
    
    
    def isSharing(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def makeCurrent(*args, **kwargs):
        pass
    
    
    def moveToThread(*args, **kwargs):
        pass
    
    
    def overlayTransparentColor(*args, **kwargs):
        pass
    
    
    def requestedFormat(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def setDevice(*args, **kwargs):
        pass
    
    
    def setFormat(*args, **kwargs):
        pass
    
    
    def setInitialized(*args, **kwargs):
        pass
    
    
    def setValid(*args, **kwargs):
        pass
    
    
    def setWindowCreated(*args, **kwargs):
        pass
    
    
    def swapBuffers(*args, **kwargs):
        pass
    
    
    def windowCreated(*args, **kwargs):
        pass
    
    
    def areSharing(*args, **kwargs):
        pass
    
    
    def currentContext(*args, **kwargs):
        pass
    
    
    def fromOpenGLContext(*args, **kwargs):
        pass
    
    
    def setTextureCacheLimit(*args, **kwargs):
        pass
    
    
    def textureCacheLimit(*args, **kwargs):
        pass
    
    
    BindOption = None
    
    
    BindOptions = None
    
    
    CanFlipNativePixmapBindOption = None
    
    
    DefaultBindOption = None
    
    
    InternalBindOption = None
    
    
    InvertedYBindOption = None
    
    
    LinearFilteringBindOption = None
    
    
    MemoryManagedBindOption = None
    
    
    MipmapBindOption = None
    
    
    NoBindOption = None
    
    
    PremultipliedAlphaBindOption = None
    
    
    TemporarilyCachedBindOption = None
    
    
    __new__ = None


class QGLShader(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def compileSourceCode(*args, **kwargs):
        pass
    
    
    def compileSourceFile(*args, **kwargs):
        pass
    
    
    def isCompiled(*args, **kwargs):
        pass
    
    
    def log(*args, **kwargs):
        pass
    
    
    def shaderId(*args, **kwargs):
        pass
    
    
    def shaderType(*args, **kwargs):
        pass
    
    
    def sourceCode(*args, **kwargs):
        pass
    
    
    def hasOpenGLShaders(*args, **kwargs):
        pass
    
    
    Fragment = None
    
    
    Geometry = None
    
    
    ShaderType = None
    
    
    ShaderTypeBit = None
    
    
    Vertex = None
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QGLBuffer(_Object):
    def __getattribute__(*args, **kwargs):
        """
        x.__getattribute__('name') <==> x.name
        """
    
        pass
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def allocate(*args, **kwargs):
        pass
    
    
    def bind(*args, **kwargs):
        pass
    
    
    def bufferId(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def destroy(*args, **kwargs):
        pass
    
    
    def isCreated(*args, **kwargs):
        pass
    
    
    def map(*args, **kwargs):
        pass
    
    
    def read(*args, **kwargs):
        pass
    
    
    def setUsagePattern(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def unmap(*args, **kwargs):
        pass
    
    
    def usagePattern(*args, **kwargs):
        pass
    
    
    def write(*args, **kwargs):
        pass
    
    
    def release(*args, **kwargs):
        pass
    
    
    Access = None
    
    
    DynamicCopy = None
    
    
    DynamicDraw = None
    
    
    DynamicRead = None
    
    
    IndexBuffer = None
    
    
    PixelPackBuffer = None
    
    
    PixelUnpackBuffer = None
    
    
    ReadOnly = None
    
    
    ReadWrite = None
    
    
    StaticCopy = None
    
    
    StaticDraw = None
    
    
    StaticRead = None
    
    
    StreamCopy = None
    
    
    StreamDraw = None
    
    
    StreamRead = None
    
    
    Type = None
    
    
    UsagePattern = None
    
    
    VertexBuffer = None
    
    
    WriteOnly = None
    
    
    __new__ = None


class QGLPixelBuffer(_QPaintDevice):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def bindTexture(*args, **kwargs):
        pass
    
    
    def bindToDynamicTexture(*args, **kwargs):
        pass
    
    
    def context(*args, **kwargs):
        pass
    
    
    def deleteTexture(*args, **kwargs):
        pass
    
    
    def devType(*args, **kwargs):
        pass
    
    
    def doneCurrent(*args, **kwargs):
        pass
    
    
    def drawTexture(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def generateDynamicTexture(*args, **kwargs):
        pass
    
    
    def handle(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def makeCurrent(*args, **kwargs):
        pass
    
    
    def metric(*args, **kwargs):
        pass
    
    
    def paintEngine(*args, **kwargs):
        pass
    
    
    def releaseFromDynamicTexture(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    def toImage(*args, **kwargs):
        pass
    
    
    def updateDynamicTexture(*args, **kwargs):
        pass
    
    
    def hasOpenGLPbuffers(*args, **kwargs):
        pass
    
    
    __new__ = None


class QGLFramebufferObjectFormat(_Object):
    def __copy__(*args, **kwargs):
        pass
    
    
    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
    
        pass
    
    
    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
    
        pass
    
    
    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
    
        pass
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
    
        pass
    
    
    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
    
        pass
    
    
    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
    
        pass
    
    
    def attachment(*args, **kwargs):
        pass
    
    
    def internalTextureFormat(*args, **kwargs):
        pass
    
    
    def mipmap(*args, **kwargs):
        pass
    
    
    def samples(*args, **kwargs):
        pass
    
    
    def setAttachment(*args, **kwargs):
        pass
    
    
    def setInternalTextureFormat(*args, **kwargs):
        pass
    
    
    def setMipmap(*args, **kwargs):
        pass
    
    
    def setSamples(*args, **kwargs):
        pass
    
    
    def setTextureTarget(*args, **kwargs):
        pass
    
    
    def textureTarget(*args, **kwargs):
        pass
    
    
    __new__ = None


class QGL(_Object):
    AccumBuffer = None
    
    
    AlphaChannel = None
    
    
    ColorIndex = None
    
    
    DebugContext = None
    
    
    DeprecatedFunctions = None
    
    
    DepthBuffer = None
    
    
    DirectRendering = None
    
    
    DoubleBuffer = None
    
    
    FormatOption = None
    
    
    FormatOptions = None
    
    
    HasOverlay = None
    
    
    IndirectRendering = None
    
    
    NoAccumBuffer = None
    
    
    NoAlphaChannel = None
    
    
    NoDebugContext = None
    
    
    NoDeprecatedFunctions = None
    
    
    NoDepthBuffer = None
    
    
    NoOverlay = None
    
    
    NoSampleBuffers = None
    
    
    NoStencilBuffer = None
    
    
    NoStereoBuffers = None
    
    
    Rgba = None
    
    
    SampleBuffers = None
    
    
    SingleBuffer = None
    
    
    StencilBuffer = None
    
    
    StereoBuffers = None


class QGLColormap(_Object):
    def __copy__(*args, **kwargs):
        pass
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def entryColor(*args, **kwargs):
        pass
    
    
    def entryRgb(*args, **kwargs):
        pass
    
    
    def find(*args, **kwargs):
        pass
    
    
    def findNearest(*args, **kwargs):
        pass
    
    
    def handle(*args, **kwargs):
        pass
    
    
    def isEmpty(*args, **kwargs):
        pass
    
    
    def setEntry(*args, **kwargs):
        pass
    
    
    def setHandle(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    __new__ = None


class QGLShaderProgram(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def addShader(*args, **kwargs):
        pass
    
    
    def addShaderFromSourceCode(*args, **kwargs):
        pass
    
    
    def addShaderFromSourceFile(*args, **kwargs):
        pass
    
    
    def attributeLocation(*args, **kwargs):
        pass
    
    
    def bind(*args, **kwargs):
        pass
    
    
    def bindAttributeLocation(*args, **kwargs):
        pass
    
    
    def disableAttributeArray(*args, **kwargs):
        pass
    
    
    def enableAttributeArray(*args, **kwargs):
        pass
    
    
    def geometryInputType(*args, **kwargs):
        pass
    
    
    def geometryOutputType(*args, **kwargs):
        pass
    
    
    def geometryOutputVertexCount(*args, **kwargs):
        pass
    
    
    def isLinked(*args, **kwargs):
        pass
    
    
    def link(*args, **kwargs):
        pass
    
    
    def log(*args, **kwargs):
        pass
    
    
    def maxGeometryOutputVertices(*args, **kwargs):
        pass
    
    
    def programId(*args, **kwargs):
        pass
    
    
    def release(*args, **kwargs):
        pass
    
    
    def removeAllShaders(*args, **kwargs):
        pass
    
    
    def removeShader(*args, **kwargs):
        pass
    
    
    def setAttributeArray2D(*args, **kwargs):
        pass
    
    
    def setAttributeArray3D(*args, **kwargs):
        pass
    
    
    def setAttributeArray4D(*args, **kwargs):
        pass
    
    
    def setAttributeBuffer(*args, **kwargs):
        pass
    
    
    def setAttributeValue(*args, **kwargs):
        pass
    
    
    def setGeometryInputType(*args, **kwargs):
        pass
    
    
    def setGeometryOutputType(*args, **kwargs):
        pass
    
    
    def setGeometryOutputVertexCount(*args, **kwargs):
        pass
    
    
    def setUniformValue(*args, **kwargs):
        pass
    
    
    def setUniformValueArray2D(*args, **kwargs):
        pass
    
    
    def setUniformValueArray2x2(*args, **kwargs):
        pass
    
    
    def setUniformValueArray2x3(*args, **kwargs):
        pass
    
    
    def setUniformValueArray2x4(*args, **kwargs):
        pass
    
    
    def setUniformValueArray3D(*args, **kwargs):
        pass
    
    
    def setUniformValueArray3x2(*args, **kwargs):
        pass
    
    
    def setUniformValueArray3x3(*args, **kwargs):
        pass
    
    
    def setUniformValueArray3x4(*args, **kwargs):
        pass
    
    
    def setUniformValueArray4D(*args, **kwargs):
        pass
    
    
    def setUniformValueArray4x2(*args, **kwargs):
        pass
    
    
    def setUniformValueArray4x3(*args, **kwargs):
        pass
    
    
    def setUniformValueArray4x4(*args, **kwargs):
        pass
    
    
    def setUniformValueArrayInt(*args, **kwargs):
        pass
    
    
    def setUniformValueArrayUint(*args, **kwargs):
        pass
    
    
    def shaders(*args, **kwargs):
        pass
    
    
    def uniformLocation(*args, **kwargs):
        pass
    
    
    def hasOpenGLShaderPrograms(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None



