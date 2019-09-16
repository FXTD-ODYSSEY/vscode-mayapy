from PySide2.QtGui import QWindow as _QWindow
from PySide2.QtQml import QQmlImageProviderBase as _QQmlImageProviderBase
from PySide2.QtCore import QObject as _QObject
from PySide2.QtQml import QQmlParserStatus as _QQmlParserStatus

class _Object(object):
    __dict__ = None


class QQuickTextDocument(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def textDocument(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QSGEngine(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def createRenderer(*args, **kwargs):
        pass
    
    
    def createTextureFromId(*args, **kwargs):
        pass
    
    
    def createTextureFromImage(*args, **kwargs):
        pass
    
    
    def initialize(*args, **kwargs):
        pass
    
    
    def invalidate(*args, **kwargs):
        pass
    
    
    CreateTextureOption = None
    
    
    CreateTextureOptions = None
    
    
    TextureCanUseAtlas = None
    
    
    TextureHasAlphaChannel = None
    
    
    TextureIsOpaque = None
    
    
    TextureOwnsGLTexture = None
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QQuickWindow(_QWindow):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def accessibleRoot(*args, **kwargs):
        pass
    
    
    def activeFocusItem(*args, **kwargs):
        pass
    
    
    def clearBeforeRendering(*args, **kwargs):
        pass
    
    
    def color(*args, **kwargs):
        pass
    
    
    def contentItem(*args, **kwargs):
        pass
    
    
    def createTextureFromId(*args, **kwargs):
        pass
    
    
    def createTextureFromImage(*args, **kwargs):
        pass
    
    
    def effectiveDevicePixelRatio(*args, **kwargs):
        pass
    
    
    def event(*args, **kwargs):
        pass
    
    
    def exposeEvent(*args, **kwargs):
        pass
    
    
    def focusInEvent(*args, **kwargs):
        pass
    
    
    def focusObject(*args, **kwargs):
        pass
    
    
    def focusOutEvent(*args, **kwargs):
        pass
    
    
    def grabWindow(*args, **kwargs):
        pass
    
    
    def hideEvent(*args, **kwargs):
        pass
    
    
    def incubationController(*args, **kwargs):
        pass
    
    
    def isPersistentOpenGLContext(*args, **kwargs):
        pass
    
    
    def isPersistentSceneGraph(*args, **kwargs):
        pass
    
    
    def isSceneGraphInitialized(*args, **kwargs):
        pass
    
    
    def keyPressEvent(*args, **kwargs):
        pass
    
    
    def keyReleaseEvent(*args, **kwargs):
        pass
    
    
    def mouseDoubleClickEvent(*args, **kwargs):
        pass
    
    
    def mouseGrabberItem(*args, **kwargs):
        pass
    
    
    def mouseMoveEvent(*args, **kwargs):
        pass
    
    
    def mousePressEvent(*args, **kwargs):
        pass
    
    
    def mouseReleaseEvent(*args, **kwargs):
        pass
    
    
    def openglContext(*args, **kwargs):
        pass
    
    
    def releaseResources(*args, **kwargs):
        pass
    
    
    def renderTarget(*args, **kwargs):
        pass
    
    
    def renderTargetId(*args, **kwargs):
        pass
    
    
    def renderTargetSize(*args, **kwargs):
        pass
    
    
    def resetOpenGLState(*args, **kwargs):
        pass
    
    
    def resizeEvent(*args, **kwargs):
        pass
    
    
    def scheduleRenderJob(*args, **kwargs):
        pass
    
    
    def sendEvent(*args, **kwargs):
        pass
    
    
    def setClearBeforeRendering(*args, **kwargs):
        pass
    
    
    def setColor(*args, **kwargs):
        pass
    
    
    def setPersistentOpenGLContext(*args, **kwargs):
        pass
    
    
    def setPersistentSceneGraph(*args, **kwargs):
        pass
    
    
    def setRenderTarget(*args, **kwargs):
        pass
    
    
    def showEvent(*args, **kwargs):
        pass
    
    
    def update(*args, **kwargs):
        pass
    
    
    def wheelEvent(*args, **kwargs):
        pass
    
    
    def hasDefaultAlphaBuffer(*args, **kwargs):
        pass
    
    
    def setDefaultAlphaBuffer(*args, **kwargs):
        pass
    
    
    AfterRenderingStage = None
    
    
    AfterSwapStage = None
    
    
    AfterSynchronizingStage = None
    
    
    BeforeRenderingStage = None
    
    
    BeforeSynchronizingStage = None
    
    
    ContextNotAvailable = None
    
    
    CreateTextureOption = None
    
    
    CreateTextureOptions = None
    
    
    NoStage = None
    
    
    RenderStage = None
    
    
    SceneGraphError = None
    
    
    TextureCanUseAtlas = None
    
    
    TextureHasAlphaChannel = None
    
    
    TextureHasMipmaps = None
    
    
    TextureIsOpaque = None
    
    
    TextureOwnsGLTexture = None
    
    
    __new__ = None
    
    
    activeFocusItemChanged = None
    
    
    afterAnimating = None
    
    
    afterRendering = None
    
    
    afterSynchronizing = None
    
    
    beforeRendering = None
    
    
    beforeSynchronizing = None
    
    
    closing = None
    
    
    colorChanged = None
    
    
    frameSwapped = None
    
    
    openglContextCreated = None
    
    
    sceneGraphAboutToStop = None
    
    
    sceneGraphError = None
    
    
    sceneGraphInitialized = None
    
    
    sceneGraphInvalidated = None
    
    
    staticMetaObject = None


class QQuickTextureFactory(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def createTexture(*args, **kwargs):
        pass
    
    
    def image(*args, **kwargs):
        pass
    
    
    def textureByteCount(*args, **kwargs):
        pass
    
    
    def textureSize(*args, **kwargs):
        pass
    
    
    def textureFactoryForImage(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    destroyed = None
    
    
    objectNameChanged = None
    
    
    staticMetaObject = None


class QQuickTransform(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def appendToItem(*args, **kwargs):
        pass
    
    
    def applyTo(*args, **kwargs):
        pass
    
    
    def prependToItem(*args, **kwargs):
        pass
    
    
    def update(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QQuickImageResponse(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def cancel(*args, **kwargs):
        pass
    
    
    def errorString(*args, **kwargs):
        pass
    
    
    def textureFactory(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    finished = None
    
    
    staticMetaObject = None


class QSGTexture(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def bind(*args, **kwargs):
        pass
    
    
    def convertToNormalizedSourceRect(*args, **kwargs):
        pass
    
    
    def filtering(*args, **kwargs):
        pass
    
    
    def hasAlphaChannel(*args, **kwargs):
        pass
    
    
    def hasMipmaps(*args, **kwargs):
        pass
    
    
    def horizontalWrapMode(*args, **kwargs):
        pass
    
    
    def isAtlasTexture(*args, **kwargs):
        pass
    
    
    def mipmapFiltering(*args, **kwargs):
        pass
    
    
    def normalizedTextureSubRect(*args, **kwargs):
        pass
    
    
    def removedFromAtlas(*args, **kwargs):
        pass
    
    
    def setFiltering(*args, **kwargs):
        pass
    
    
    def setHorizontalWrapMode(*args, **kwargs):
        pass
    
    
    def setMipmapFiltering(*args, **kwargs):
        pass
    
    
    def setVerticalWrapMode(*args, **kwargs):
        pass
    
    
    def textureId(*args, **kwargs):
        pass
    
    
    def textureSize(*args, **kwargs):
        pass
    
    
    def updateBindOptions(*args, **kwargs):
        pass
    
    
    def verticalWrapMode(*args, **kwargs):
        pass
    
    
    ClampToEdge = None
    
    
    Filtering = None
    
    
    Linear = None
    
    
    Nearest = None
    
    
    locals()['None'] = None
    
    
    Repeat = None
    
    
    WrapMode = None
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QQuickRenderControl(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def grab(*args, **kwargs):
        pass
    
    
    def initialize(*args, **kwargs):
        pass
    
    
    def invalidate(*args, **kwargs):
        pass
    
    
    def polishItems(*args, **kwargs):
        pass
    
    
    def prepareThread(*args, **kwargs):
        pass
    
    
    def render(*args, **kwargs):
        pass
    
    
    def renderWindow(*args, **kwargs):
        pass
    
    
    def sync(*args, **kwargs):
        pass
    
    
    def renderWindowFor(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    renderRequested = None
    
    
    sceneChanged = None
    
    
    staticMetaObject = None


class QSGMaterialType(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    __new__ = None


class QQuickImageProvider(_QQmlImageProviderBase):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def flags(*args, **kwargs):
        pass
    
    
    def imageType(*args, **kwargs):
        pass
    
    
    def requestImage(*args, **kwargs):
        pass
    
    
    def requestPixmap(*args, **kwargs):
        pass
    
    
    def requestTexture(*args, **kwargs):
        pass
    
    
    __new__ = None


class QSGGeometry(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def allocate(*args, **kwargs):
        pass
    
    
    def attributeCount(*args, **kwargs):
        pass
    
    
    def attributes(*args, **kwargs):
        pass
    
    
    def indexCount(*args, **kwargs):
        pass
    
    
    def indexData(*args, **kwargs):
        pass
    
    
    def indexDataAsUInt(*args, **kwargs):
        pass
    
    
    def indexDataAsUShort(*args, **kwargs):
        pass
    
    
    def indexDataPattern(*args, **kwargs):
        pass
    
    
    def indexType(*args, **kwargs):
        pass
    
    
    def lineWidth(*args, **kwargs):
        pass
    
    
    def markIndexDataDirty(*args, **kwargs):
        pass
    
    
    def markVertexDataDirty(*args, **kwargs):
        pass
    
    
    def setIndexDataPattern(*args, **kwargs):
        pass
    
    
    def setLineWidth(*args, **kwargs):
        pass
    
    
    def setVertexDataPattern(*args, **kwargs):
        pass
    
    
    def sizeOfIndex(*args, **kwargs):
        pass
    
    
    def sizeOfVertex(*args, **kwargs):
        pass
    
    
    def vertexCount(*args, **kwargs):
        pass
    
    
    def vertexData(*args, **kwargs):
        pass
    
    
    def vertexDataAsColoredPoint2D(*args, **kwargs):
        pass
    
    
    def vertexDataAsPoint2D(*args, **kwargs):
        pass
    
    
    def vertexDataAsTexturedPoint2D(*args, **kwargs):
        pass
    
    
    def vertexDataPattern(*args, **kwargs):
        pass
    
    
    def defaultAttributes_ColoredPoint2D(*args, **kwargs):
        pass
    
    
    def defaultAttributes_Point2D(*args, **kwargs):
        pass
    
    
    def defaultAttributes_TexturedPoint2D(*args, **kwargs):
        pass
    
    
    def updateRectGeometry(*args, **kwargs):
        pass
    
    
    def updateTexturedRectGeometry(*args, **kwargs):
        pass
    
    
    AlwaysUploadPattern = None
    
    
    Attribute = None
    
    
    AttributeSet = None
    
    
    ColoredPoint2D = None
    
    
    DataPattern = None
    
    
    DynamicPattern = None
    
    
    Point2D = None
    
    
    StaticPattern = None
    
    
    StreamPattern = None
    
    
    TexturedPoint2D = None
    
    
    __new__ = None


class QSGNode(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
    
        pass
    
    
    def appendChildNode(*args, **kwargs):
        pass
    
    
    def childAtIndex(*args, **kwargs):
        pass
    
    
    def childCount(*args, **kwargs):
        pass
    
    
    def clearDirty(*args, **kwargs):
        pass
    
    
    def dirtyState(*args, **kwargs):
        pass
    
    
    def firstChild(*args, **kwargs):
        pass
    
    
    def flags(*args, **kwargs):
        pass
    
    
    def insertChildNodeAfter(*args, **kwargs):
        pass
    
    
    def insertChildNodeBefore(*args, **kwargs):
        pass
    
    
    def isSubtreeBlocked(*args, **kwargs):
        pass
    
    
    def lastChild(*args, **kwargs):
        pass
    
    
    def markDirty(*args, **kwargs):
        pass
    
    
    def nextSibling(*args, **kwargs):
        pass
    
    
    def parent(*args, **kwargs):
        pass
    
    
    def prependChildNode(*args, **kwargs):
        pass
    
    
    def preprocess(*args, **kwargs):
        pass
    
    
    def previousSibling(*args, **kwargs):
        pass
    
    
    def removeAllChildNodes(*args, **kwargs):
        pass
    
    
    def removeChildNode(*args, **kwargs):
        pass
    
    
    def reparentChildNodesTo(*args, **kwargs):
        pass
    
    
    def setFlag(*args, **kwargs):
        pass
    
    
    def setFlags(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    BasicNodeType = None
    
    
    ClipNodeType = None
    
    
    DirtyForceUpdate = None
    
    
    DirtyGeometry = None
    
    
    DirtyMaterial = None
    
    
    DirtyMatrix = None
    
    
    DirtyNodeAdded = None
    
    
    DirtyNodeRemoved = None
    
    
    DirtyOpacity = None
    
    
    DirtyPropagationMask = None
    
    
    DirtyState = None
    
    
    DirtyStateBit = None
    
    
    DirtySubtreeBlocked = None
    
    
    DirtyUsePreprocess = None
    
    
    Flag = None
    
    
    Flags = None
    
    
    GeometryNodeType = None
    
    
    IsVisitableNode = None
    
    
    NodeType = None
    
    
    OpacityNodeType = None
    
    
    OwnedByParent = None
    
    
    OwnsGeometry = None
    
    
    OwnsMaterial = None
    
    
    OwnsOpaqueMaterial = None
    
    
    RenderNodeType = None
    
    
    RootNodeType = None
    
    
    TransformNodeType = None
    
    
    UsePreprocess = None
    
    
    __new__ = None


class QSGTextureProvider(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def texture(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None
    
    
    textureChanged = None


class QSGAbstractRenderer(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def clearColor(*args, **kwargs):
        pass
    
    
    def clearMode(*args, **kwargs):
        pass
    
    
    def deviceRect(*args, **kwargs):
        pass
    
    
    def nodeChanged(*args, **kwargs):
        pass
    
    
    def projectionMatrix(*args, **kwargs):
        pass
    
    
    def renderScene(*args, **kwargs):
        pass
    
    
    def setClearColor(*args, **kwargs):
        pass
    
    
    def setClearMode(*args, **kwargs):
        pass
    
    
    def setDeviceRect(*args, **kwargs):
        pass
    
    
    def setProjectionMatrix(*args, **kwargs):
        pass
    
    
    def setProjectionMatrixToRect(*args, **kwargs):
        pass
    
    
    def setViewportRect(*args, **kwargs):
        pass
    
    
    def viewportRect(*args, **kwargs):
        pass
    
    
    ClearColorBuffer = None
    
    
    ClearDepthBuffer = None
    
    
    ClearMode = None
    
    
    ClearModeBit = None
    
    
    ClearStencilBuffer = None
    
    
    __new__ = None
    
    
    sceneGraphChanged = None
    
    
    staticMetaObject = None


class QQuickItem(_QObject, _QQmlParserStatus):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def acceptHoverEvents(*args, **kwargs):
        pass
    
    
    def acceptedMouseButtons(*args, **kwargs):
        pass
    
    
    def activeFocusOnTab(*args, **kwargs):
        pass
    
    
    def antialiasing(*args, **kwargs):
        pass
    
    
    def baselineOffset(*args, **kwargs):
        pass
    
    
    def boundingRect(*args, **kwargs):
        pass
    
    
    def childAt(*args, **kwargs):
        pass
    
    
    def childItems(*args, **kwargs):
        pass
    
    
    def childMouseEventFilter(*args, **kwargs):
        pass
    
    
    def childrenRect(*args, **kwargs):
        pass
    
    
    def classBegin(*args, **kwargs):
        pass
    
    
    def clip(*args, **kwargs):
        pass
    
    
    def clipRect(*args, **kwargs):
        pass
    
    
    def componentComplete(*args, **kwargs):
        pass
    
    
    def contains(*args, **kwargs):
        pass
    
    
    def cursor(*args, **kwargs):
        pass
    
    
    def dragEnterEvent(*args, **kwargs):
        pass
    
    
    def dragLeaveEvent(*args, **kwargs):
        pass
    
    
    def dragMoveEvent(*args, **kwargs):
        pass
    
    
    def dropEvent(*args, **kwargs):
        pass
    
    
    def event(*args, **kwargs):
        pass
    
    
    def filtersChildMouseEvents(*args, **kwargs):
        pass
    
    
    def flags(*args, **kwargs):
        pass
    
    
    def focusInEvent(*args, **kwargs):
        pass
    
    
    def focusOutEvent(*args, **kwargs):
        pass
    
    
    def forceActiveFocus(*args, **kwargs):
        pass
    
    
    def geometryChanged(*args, **kwargs):
        pass
    
    
    def grabMouse(*args, **kwargs):
        pass
    
    
    def grabToImage(*args, **kwargs):
        pass
    
    
    def grabTouchPoints(*args, **kwargs):
        pass
    
    
    def hasActiveFocus(*args, **kwargs):
        pass
    
    
    def hasFocus(*args, **kwargs):
        pass
    
    
    def height(*args, **kwargs):
        pass
    
    
    def heightValid(*args, **kwargs):
        pass
    
    
    def hoverEnterEvent(*args, **kwargs):
        pass
    
    
    def hoverLeaveEvent(*args, **kwargs):
        pass
    
    
    def hoverMoveEvent(*args, **kwargs):
        pass
    
    
    def implicitHeight(*args, **kwargs):
        pass
    
    
    def implicitWidth(*args, **kwargs):
        pass
    
    
    def inputMethodEvent(*args, **kwargs):
        pass
    
    
    def inputMethodQuery(*args, **kwargs):
        pass
    
    
    def isComponentComplete(*args, **kwargs):
        pass
    
    
    def isEnabled(*args, **kwargs):
        pass
    
    
    def isFocusScope(*args, **kwargs):
        pass
    
    
    def isTextureProvider(*args, **kwargs):
        pass
    
    
    def isUnderMouse(*args, **kwargs):
        pass
    
    
    def isVisible(*args, **kwargs):
        pass
    
    
    def itemTransform(*args, **kwargs):
        pass
    
    
    def keepMouseGrab(*args, **kwargs):
        pass
    
    
    def keepTouchGrab(*args, **kwargs):
        pass
    
    
    def keyPressEvent(*args, **kwargs):
        pass
    
    
    def keyReleaseEvent(*args, **kwargs):
        pass
    
    
    def mapFromItem(*args, **kwargs):
        pass
    
    
    def mapFromScene(*args, **kwargs):
        pass
    
    
    def mapRectFromItem(*args, **kwargs):
        pass
    
    
    def mapRectFromScene(*args, **kwargs):
        pass
    
    
    def mapRectToItem(*args, **kwargs):
        pass
    
    
    def mapRectToScene(*args, **kwargs):
        pass
    
    
    def mapToItem(*args, **kwargs):
        pass
    
    
    def mapToScene(*args, **kwargs):
        pass
    
    
    def mouseDoubleClickEvent(*args, **kwargs):
        pass
    
    
    def mouseMoveEvent(*args, **kwargs):
        pass
    
    
    def mousePressEvent(*args, **kwargs):
        pass
    
    
    def mouseReleaseEvent(*args, **kwargs):
        pass
    
    
    def mouseUngrabEvent(*args, **kwargs):
        pass
    
    
    def nextItemInFocusChain(*args, **kwargs):
        pass
    
    
    def opacity(*args, **kwargs):
        pass
    
    
    def parentItem(*args, **kwargs):
        pass
    
    
    def polish(*args, **kwargs):
        pass
    
    
    def position(*args, **kwargs):
        pass
    
    
    def releaseResources(*args, **kwargs):
        pass
    
    
    def resetAntialiasing(*args, **kwargs):
        pass
    
    
    def resetHeight(*args, **kwargs):
        pass
    
    
    def resetWidth(*args, **kwargs):
        pass
    
    
    def rotation(*args, **kwargs):
        pass
    
    
    def scale(*args, **kwargs):
        pass
    
    
    def scopedFocusItem(*args, **kwargs):
        pass
    
    
    def setAcceptHoverEvents(*args, **kwargs):
        pass
    
    
    def setAcceptedMouseButtons(*args, **kwargs):
        pass
    
    
    def setActiveFocusOnTab(*args, **kwargs):
        pass
    
    
    def setAntialiasing(*args, **kwargs):
        pass
    
    
    def setBaselineOffset(*args, **kwargs):
        pass
    
    
    def setClip(*args, **kwargs):
        pass
    
    
    def setCursor(*args, **kwargs):
        pass
    
    
    def setEnabled(*args, **kwargs):
        pass
    
    
    def setFiltersChildMouseEvents(*args, **kwargs):
        pass
    
    
    def setFlag(*args, **kwargs):
        pass
    
    
    def setFlags(*args, **kwargs):
        pass
    
    
    def setFocus(*args, **kwargs):
        pass
    
    
    def setHeight(*args, **kwargs):
        pass
    
    
    def setImplicitHeight(*args, **kwargs):
        pass
    
    
    def setImplicitSize(*args, **kwargs):
        pass
    
    
    def setImplicitWidth(*args, **kwargs):
        pass
    
    
    def setKeepMouseGrab(*args, **kwargs):
        pass
    
    
    def setKeepTouchGrab(*args, **kwargs):
        pass
    
    
    def setOpacity(*args, **kwargs):
        pass
    
    
    def setParentItem(*args, **kwargs):
        pass
    
    
    def setPosition(*args, **kwargs):
        pass
    
    
    def setRotation(*args, **kwargs):
        pass
    
    
    def setScale(*args, **kwargs):
        pass
    
    
    def setSize(*args, **kwargs):
        pass
    
    
    def setSmooth(*args, **kwargs):
        pass
    
    
    def setState(*args, **kwargs):
        pass
    
    
    def setTransformOrigin(*args, **kwargs):
        pass
    
    
    def setTransformOriginPoint(*args, **kwargs):
        pass
    
    
    def setVisible(*args, **kwargs):
        pass
    
    
    def setWidth(*args, **kwargs):
        pass
    
    
    def setX(*args, **kwargs):
        pass
    
    
    def setY(*args, **kwargs):
        pass
    
    
    def setZ(*args, **kwargs):
        pass
    
    
    def smooth(*args, **kwargs):
        pass
    
    
    def stackAfter(*args, **kwargs):
        pass
    
    
    def stackBefore(*args, **kwargs):
        pass
    
    
    def state(*args, **kwargs):
        pass
    
    
    def textureProvider(*args, **kwargs):
        pass
    
    
    def touchEvent(*args, **kwargs):
        pass
    
    
    def touchUngrabEvent(*args, **kwargs):
        pass
    
    
    def transformOrigin(*args, **kwargs):
        pass
    
    
    def transformOriginPoint(*args, **kwargs):
        pass
    
    
    def ungrabMouse(*args, **kwargs):
        pass
    
    
    def ungrabTouchPoints(*args, **kwargs):
        pass
    
    
    def unsetCursor(*args, **kwargs):
        pass
    
    
    def update(*args, **kwargs):
        pass
    
    
    def updateInputMethod(*args, **kwargs):
        pass
    
    
    def updatePaintNode(*args, **kwargs):
        pass
    
    
    def updatePolish(*args, **kwargs):
        pass
    
    
    def wheelEvent(*args, **kwargs):
        pass
    
    
    def width(*args, **kwargs):
        pass
    
    
    def widthValid(*args, **kwargs):
        pass
    
    
    def window(*args, **kwargs):
        pass
    
    
    def windowDeactivateEvent(*args, **kwargs):
        pass
    
    
    def x(*args, **kwargs):
        pass
    
    
    def y(*args, **kwargs):
        pass
    
    
    def z(*args, **kwargs):
        pass
    
    
    Bottom = None
    
    
    BottomLeft = None
    
    
    BottomRight = None
    
    
    Center = None
    
    
    Flag = None
    
    
    Flags = None
    
    
    ItemAcceptsDrops = None
    
    
    ItemAcceptsInputMethod = None
    
    
    ItemActiveFocusHasChanged = None
    
    
    ItemAntialiasingHasChanged = None
    
    
    ItemChange = None
    
    
    ItemChildAddedChange = None
    
    
    ItemChildRemovedChange = None
    
    
    ItemClipsChildrenToShape = None
    
    
    ItemDevicePixelRatioHasChanged = None
    
    
    ItemHasContents = None
    
    
    ItemIsFocusScope = None
    
    
    ItemOpacityHasChanged = None
    
    
    ItemParentHasChanged = None
    
    
    ItemRotationHasChanged = None
    
    
    ItemSceneChange = None
    
    
    ItemVisibleHasChanged = None
    
    
    Left = None
    
    
    Right = None
    
    
    Top = None
    
    
    TopLeft = None
    
    
    TopRight = None
    
    
    TransformOrigin = None
    
    
    UpdatePaintNodeData = None
    
    
    __new__ = None
    
    
    activeFocusChanged = None
    
    
    activeFocusOnTabChanged = None
    
    
    antialiasingChanged = None
    
    
    baselineOffsetChanged = None
    
    
    childrenChanged = None
    
    
    childrenRectChanged = None
    
    
    clipChanged = None
    
    
    enabledChanged = None
    
    
    focusChanged = None
    
    
    heightChanged = None
    
    
    implicitHeightChanged = None
    
    
    implicitWidthChanged = None
    
    
    opacityChanged = None
    
    
    parentChanged = None
    
    
    rotationChanged = None
    
    
    scaleChanged = None
    
    
    smoothChanged = None
    
    
    stateChanged = None
    
    
    staticMetaObject = None
    
    
    transformOriginChanged = None
    
    
    visibleChanged = None
    
    
    visibleChildrenChanged = None
    
    
    widthChanged = None
    
    
    windowChanged = None
    
    
    xChanged = None
    
    
    yChanged = None
    
    
    zChanged = None


class QQuickItemGrabResult(_QObject):
    def event(*args, **kwargs):
        pass
    
    
    def image(*args, **kwargs):
        pass
    
    
    def saveToFile(*args, **kwargs):
        pass
    
    
    def url(*args, **kwargs):
        pass
    
    
    ready = None
    
    
    staticMetaObject = None


class QQuickPaintedItem(QQuickItem):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def antialiasing(*args, **kwargs):
        pass
    
    
    def contentsBoundingRect(*args, **kwargs):
        pass
    
    
    def contentsScale(*args, **kwargs):
        pass
    
    
    def contentsSize(*args, **kwargs):
        pass
    
    
    def fillColor(*args, **kwargs):
        pass
    
    
    def isTextureProvider(*args, **kwargs):
        pass
    
    
    def mipmap(*args, **kwargs):
        pass
    
    
    def opaquePainting(*args, **kwargs):
        pass
    
    
    def paint(*args, **kwargs):
        pass
    
    
    def performanceHints(*args, **kwargs):
        pass
    
    
    def releaseResources(*args, **kwargs):
        pass
    
    
    def renderTarget(*args, **kwargs):
        pass
    
    
    def resetContentsSize(*args, **kwargs):
        pass
    
    
    def setAntialiasing(*args, **kwargs):
        pass
    
    
    def setContentsScale(*args, **kwargs):
        pass
    
    
    def setContentsSize(*args, **kwargs):
        pass
    
    
    def setFillColor(*args, **kwargs):
        pass
    
    
    def setMipmap(*args, **kwargs):
        pass
    
    
    def setOpaquePainting(*args, **kwargs):
        pass
    
    
    def setPerformanceHint(*args, **kwargs):
        pass
    
    
    def setPerformanceHints(*args, **kwargs):
        pass
    
    
    def setRenderTarget(*args, **kwargs):
        pass
    
    
    def setTextureSize(*args, **kwargs):
        pass
    
    
    def textureProvider(*args, **kwargs):
        pass
    
    
    def textureSize(*args, **kwargs):
        pass
    
    
    def update(*args, **kwargs):
        pass
    
    
    def updatePaintNode(*args, **kwargs):
        pass
    
    
    FastFBOResizing = None
    
    
    FramebufferObject = None
    
    
    Image = None
    
    
    InvertedYFramebufferObject = None
    
    
    PerformanceHint = None
    
    
    PerformanceHints = None
    
    
    RenderTarget = None
    
    
    __new__ = None
    
    
    contentsScaleChanged = None
    
    
    contentsSizeChanged = None
    
    
    fillColorChanged = None
    
    
    renderTargetChanged = None
    
    
    staticMetaObject = None
    
    
    textureSizeChanged = None


class QQuickFramebufferObject(QQuickItem):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def createRenderer(*args, **kwargs):
        pass
    
    
    def geometryChanged(*args, **kwargs):
        pass
    
    
    def isTextureProvider(*args, **kwargs):
        pass
    
    
    def mirrorVertically(*args, **kwargs):
        pass
    
    
    def releaseResources(*args, **kwargs):
        pass
    
    
    def setMirrorVertically(*args, **kwargs):
        pass
    
    
    def setTextureFollowsItemSize(*args, **kwargs):
        pass
    
    
    def textureFollowsItemSize(*args, **kwargs):
        pass
    
    
    def textureProvider(*args, **kwargs):
        pass
    
    
    def updatePaintNode(*args, **kwargs):
        pass
    
    
    Renderer = None
    
    
    __new__ = None
    
    
    mirrorVerticallyChanged = None
    
    
    staticMetaObject = None
    
    
    textureFollowsItemSizeChanged = None


class QSGDynamicTexture(QSGTexture):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def updateTexture(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QSGTransformNode(QSGNode):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
    
        pass
    
    
    def combinedMatrix(*args, **kwargs):
        pass
    
    
    def matrix(*args, **kwargs):
        pass
    
    
    def setCombinedMatrix(*args, **kwargs):
        pass
    
    
    def setMatrix(*args, **kwargs):
        pass
    
    
    __new__ = None


class QSGOpacityNode(QSGNode):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
    
        pass
    
    
    def combinedOpacity(*args, **kwargs):
        pass
    
    
    def isSubtreeBlocked(*args, **kwargs):
        pass
    
    
    def opacity(*args, **kwargs):
        pass
    
    
    def setCombinedOpacity(*args, **kwargs):
        pass
    
    
    def setOpacity(*args, **kwargs):
        pass
    
    
    __new__ = None


class QSGBasicGeometryNode(QSGNode):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def clipList(*args, **kwargs):
        pass
    
    
    def geometry(*args, **kwargs):
        pass
    
    
    def matrix(*args, **kwargs):
        pass
    
    
    def setGeometry(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQuickView(QQuickWindow):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def engine(*args, **kwargs):
        pass
    
    
    def errors(*args, **kwargs):
        pass
    
    
    def initialSize(*args, **kwargs):
        pass
    
    
    def keyPressEvent(*args, **kwargs):
        pass
    
    
    def keyReleaseEvent(*args, **kwargs):
        pass
    
    
    def mouseMoveEvent(*args, **kwargs):
        pass
    
    
    def mousePressEvent(*args, **kwargs):
        pass
    
    
    def mouseReleaseEvent(*args, **kwargs):
        pass
    
    
    def resizeEvent(*args, **kwargs):
        pass
    
    
    def resizeMode(*args, **kwargs):
        pass
    
    
    def rootContext(*args, **kwargs):
        pass
    
    
    def rootObject(*args, **kwargs):
        pass
    
    
    def setContent(*args, **kwargs):
        pass
    
    
    def setResizeMode(*args, **kwargs):
        pass
    
    
    def setSource(*args, **kwargs):
        pass
    
    
    def sizeHint(*args, **kwargs):
        pass
    
    
    def source(*args, **kwargs):
        pass
    
    
    def status(*args, **kwargs):
        pass
    
    
    def timerEvent(*args, **kwargs):
        pass
    
    
    Error = None
    
    
    Loading = None
    
    
    Null = None
    
    
    Ready = None
    
    
    ResizeMode = None
    
    
    SizeRootObjectToView = None
    
    
    SizeViewToRootObject = None
    
    
    Status = None
    
    
    __new__ = None
    
    
    staticMetaObject = None
    
    
    statusChanged = None


class QQuickAsyncImageProvider(QQuickImageProvider):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def requestImageResponse(*args, **kwargs):
        pass
    
    
    __new__ = None


class QSGGeometryNode(QSGBasicGeometryNode):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
    
        pass
    
    
    def inheritedOpacity(*args, **kwargs):
        pass
    
    
    def renderOrder(*args, **kwargs):
        pass
    
    
    def setInheritedOpacity(*args, **kwargs):
        pass
    
    
    def setRenderOrder(*args, **kwargs):
        pass
    
    
    __new__ = None


class QSGClipNode(QSGBasicGeometryNode):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def clipRect(*args, **kwargs):
        pass
    
    
    def isRectangular(*args, **kwargs):
        pass
    
    
    def setClipRect(*args, **kwargs):
        pass
    
    
    def setIsRectangular(*args, **kwargs):
        pass
    
    
    __new__ = None


class QSGSimpleRectNode(QSGGeometryNode):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def color(*args, **kwargs):
        pass
    
    
    def rect(*args, **kwargs):
        pass
    
    
    def setColor(*args, **kwargs):
        pass
    
    
    def setRect(*args, **kwargs):
        pass
    
    
    __new__ = None


class QSGSimpleTextureNode(QSGGeometryNode):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def filtering(*args, **kwargs):
        pass
    
    
    def ownsTexture(*args, **kwargs):
        pass
    
    
    def rect(*args, **kwargs):
        pass
    
    
    def setFiltering(*args, **kwargs):
        pass
    
    
    def setOwnsTexture(*args, **kwargs):
        pass
    
    
    def setRect(*args, **kwargs):
        pass
    
    
    def setSourceRect(*args, **kwargs):
        pass
    
    
    def setTexture(*args, **kwargs):
        pass
    
    
    def setTextureCoordinatesTransform(*args, **kwargs):
        pass
    
    
    def sourceRect(*args, **kwargs):
        pass
    
    
    def texture(*args, **kwargs):
        pass
    
    
    def textureCoordinatesTransform(*args, **kwargs):
        pass
    
    
    MirrorHorizontally = None
    
    
    MirrorVertically = None
    
    
    NoTransform = None
    
    
    TextureCoordinatesTransformFlag = None
    
    
    TextureCoordinatesTransformMode = None
    
    
    __new__ = None



