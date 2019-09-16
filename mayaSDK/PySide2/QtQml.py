from PySide2.QtCore import QObject as _QObject

class _Object(object):
    __dict__ = None


class VolatileBool(object):
    """
    VolatileBool objects contain a C++ volatile bool
    """
    
    
    
    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
    
        pass
    
    
    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
    
        pass
    
    
    def get(*args, **kwargs):
        """
        B.get() -> Bool. Returns the value of the volatile boolean
        """
    
        pass
    
    
    def set(*args, **kwargs):
        """
        B.set(a) -> None. Sets the value of the volatile boolean
        """
    
        pass
    
    
    __new__ = None


class _Property(object):
    def __call__(*args, **kwargs):
        """
        x.__call__(...) <==> x(...)
        """
    
        pass
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def getter(*args, **kwargs):
        pass
    
    
    def read(*args, **kwargs):
        pass
    
    
    def setter(*args, **kwargs):
        pass
    
    
    def write(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlContext(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def baseUrl(*args, **kwargs):
        pass
    
    
    def contextObject(*args, **kwargs):
        pass
    
    
    def contextProperty(*args, **kwargs):
        pass
    
    
    def engine(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def nameForObject(*args, **kwargs):
        pass
    
    
    def parentContext(*args, **kwargs):
        pass
    
    
    def resolvedUrl(*args, **kwargs):
        pass
    
    
    def setBaseUrl(*args, **kwargs):
        pass
    
    
    def setContextObject(*args, **kwargs):
        pass
    
    
    def setContextProperty(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QQmlImageProviderBase(_Object):
    def flags(*args, **kwargs):
        pass
    
    
    def imageType(*args, **kwargs):
        pass
    
    
    Flag = None
    
    
    Flags = None
    
    
    ForceAsynchronousImageLoading = None
    
    
    Image = None
    
    
    ImageResponse = None
    
    
    ImageType = None
    
    
    Invalid = None
    
    
    Pixmap = None
    
    
    Texture = None
    
    
    __new__ = None


class QQmlDebuggingEnabler(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def connectToLocalDebugger(*args, **kwargs):
        pass
    
    
    def startTcpDebugServer(*args, **kwargs):
        pass
    
    
    DoNotWaitForClient = None
    
    
    StartMode = None
    
    
    WaitForClient = None
    
    
    __new__ = None


class QQmlProperty(_Object):
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
    
    
    def __getattribute__(*args, **kwargs):
        """
        x.__getattribute__('name') <==> x.name
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
    
    
    def connectNotifySignal(*args, **kwargs):
        pass
    
    
    def hasNotifySignal(*args, **kwargs):
        pass
    
    
    def index(*args, **kwargs):
        pass
    
    
    def isDesignable(*args, **kwargs):
        pass
    
    
    def isProperty(*args, **kwargs):
        pass
    
    
    def isResettable(*args, **kwargs):
        pass
    
    
    def isSignalProperty(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def isWritable(*args, **kwargs):
        pass
    
    
    def method(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def needsNotifySignal(*args, **kwargs):
        pass
    
    
    def object(*args, **kwargs):
        pass
    
    
    def property(*args, **kwargs):
        pass
    
    
    def propertyType(*args, **kwargs):
        pass
    
    
    def propertyTypeCategory(*args, **kwargs):
        pass
    
    
    def propertyTypeName(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def read(*args, **kwargs):
        pass
    
    
    def write(*args, **kwargs):
        pass
    
    
    Invalid = None
    
    
    InvalidCategory = None
    
    
    List = None
    
    
    Normal = None
    
    
    Object = None
    
    
    Property = None
    
    
    PropertyTypeCategory = None
    
    
    SignalProperty = None
    
    
    Type = None
    
    
    __new__ = None


class QQmlIncubationController(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def engine(*args, **kwargs):
        pass
    
    
    def incubateFor(*args, **kwargs):
        pass
    
    
    def incubateWhile(*args, **kwargs):
        pass
    
    
    def incubatingObjectCount(*args, **kwargs):
        pass
    
    
    def incubatingObjectCountChanged(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlPropertyValueSource(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def setTarget(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlNetworkAccessManagerFactory(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlExtensionInterface(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def initializeEngine(*args, **kwargs):
        pass
    
    
    __new__ = None


class QJSValue(_Object):
    def __copy__(*args, **kwargs):
        pass
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __nonzero__(*args, **kwargs):
        """
        x.__nonzero__() <==> x != 0
        """
    
        pass
    
    
    def call(*args, **kwargs):
        pass
    
    
    def callAsConstructor(*args, **kwargs):
        pass
    
    
    def callWithInstance(*args, **kwargs):
        pass
    
    
    def deleteProperty(*args, **kwargs):
        pass
    
    
    def engine(*args, **kwargs):
        pass
    
    
    def equals(*args, **kwargs):
        pass
    
    
    def hasOwnProperty(*args, **kwargs):
        pass
    
    
    def hasProperty(*args, **kwargs):
        pass
    
    
    def isArray(*args, **kwargs):
        pass
    
    
    def isBool(*args, **kwargs):
        pass
    
    
    def isCallable(*args, **kwargs):
        pass
    
    
    def isDate(*args, **kwargs):
        pass
    
    
    def isError(*args, **kwargs):
        pass
    
    
    def isNull(*args, **kwargs):
        pass
    
    
    def isNumber(*args, **kwargs):
        pass
    
    
    def isObject(*args, **kwargs):
        pass
    
    
    def isQObject(*args, **kwargs):
        pass
    
    
    def isRegExp(*args, **kwargs):
        pass
    
    
    def isString(*args, **kwargs):
        pass
    
    
    def isUndefined(*args, **kwargs):
        pass
    
    
    def isVariant(*args, **kwargs):
        pass
    
    
    def property(*args, **kwargs):
        pass
    
    
    def prototype(*args, **kwargs):
        pass
    
    
    def setProperty(*args, **kwargs):
        pass
    
    
    def setPrototype(*args, **kwargs):
        pass
    
    
    def strictlyEquals(*args, **kwargs):
        pass
    
    
    def toBool(*args, **kwargs):
        pass
    
    
    def toDateTime(*args, **kwargs):
        pass
    
    
    def toInt(*args, **kwargs):
        pass
    
    
    def toNumber(*args, **kwargs):
        pass
    
    
    def toQObject(*args, **kwargs):
        pass
    
    
    def toString(*args, **kwargs):
        pass
    
    
    def toUInt(*args, **kwargs):
        pass
    
    
    def toVariant(*args, **kwargs):
        pass
    
    
    NullValue = None
    
    
    SpecialValue = None
    
    
    UndefinedValue = None
    
    
    __new__ = None


class QJSEngine(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def collectGarbage(*args, **kwargs):
        pass
    
    
    def evaluate(*args, **kwargs):
        pass
    
    
    def globalObject(*args, **kwargs):
        pass
    
    
    def installExtensions(*args, **kwargs):
        pass
    
    
    def installTranslatorFunctions(*args, **kwargs):
        pass
    
    
    def newArray(*args, **kwargs):
        pass
    
    
    def newObject(*args, **kwargs):
        pass
    
    
    def newQObject(*args, **kwargs):
        pass
    
    
    def toScriptValue(*args, **kwargs):
        pass
    
    
    AllExtensions = None
    
    
    ConsoleExtension = None
    
    
    Extension = None
    
    
    Extensions = None
    
    
    GarbageCollectionExtension = None
    
    
    TranslationExtension = None
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QQmlError(_Object):
    def __copy__(*args, **kwargs):
        pass
    
    
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
    
    
    def column(*args, **kwargs):
        pass
    
    
    def description(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def line(*args, **kwargs):
        pass
    
    
    def object(*args, **kwargs):
        pass
    
    
    def setColumn(*args, **kwargs):
        pass
    
    
    def setDescription(*args, **kwargs):
        pass
    
    
    def setLine(*args, **kwargs):
        pass
    
    
    def setObject(*args, **kwargs):
        pass
    
    
    def setUrl(*args, **kwargs):
        pass
    
    
    def toString(*args, **kwargs):
        pass
    
    
    def url(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlParserStatus(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def classBegin(*args, **kwargs):
        pass
    
    
    def componentComplete(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlFileSelector(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def setExtraSelectors(*args, **kwargs):
        pass
    
    
    def setSelector(*args, **kwargs):
        pass
    
    
    def get(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QQmlAbstractUrlInterceptor(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def intercept(*args, **kwargs):
        pass
    
    
    DataType = None
    
    
    JavaScriptFile = None
    
    
    QmlFile = None
    
    
    QmldirFile = None
    
    
    UrlString = None
    
    
    __new__ = None


class QQmlExpression(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def clearError(*args, **kwargs):
        pass
    
    
    def columnNumber(*args, **kwargs):
        pass
    
    
    def context(*args, **kwargs):
        pass
    
    
    def engine(*args, **kwargs):
        pass
    
    
    def error(*args, **kwargs):
        pass
    
    
    def evaluate(*args, **kwargs):
        pass
    
    
    def expression(*args, **kwargs):
        pass
    
    
    def hasError(*args, **kwargs):
        pass
    
    
    def lineNumber(*args, **kwargs):
        pass
    
    
    def notifyOnValueChanged(*args, **kwargs):
        pass
    
    
    def scopeObject(*args, **kwargs):
        pass
    
    
    def setExpression(*args, **kwargs):
        pass
    
    
    def setNotifyOnValueChanged(*args, **kwargs):
        pass
    
    
    def setSourceLocation(*args, **kwargs):
        pass
    
    
    def sourceFile(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None
    
    
    valueChanged = None


class QQmlComponent(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __nonzero__(*args, **kwargs):
        """
        x.__nonzero__() <==> x != 0
        """
    
        pass
    
    
    def beginCreate(*args, **kwargs):
        pass
    
    
    def completeCreate(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def creationContext(*args, **kwargs):
        pass
    
    
    def errorString(*args, **kwargs):
        pass
    
    
    def errors(*args, **kwargs):
        pass
    
    
    def isError(*args, **kwargs):
        pass
    
    
    def isLoading(*args, **kwargs):
        pass
    
    
    def isNull(*args, **kwargs):
        pass
    
    
    def isReady(*args, **kwargs):
        pass
    
    
    def loadUrl(*args, **kwargs):
        pass
    
    
    def progress(*args, **kwargs):
        pass
    
    
    def setData(*args, **kwargs):
        pass
    
    
    def status(*args, **kwargs):
        pass
    
    
    def url(*args, **kwargs):
        pass
    
    
    Asynchronous = None
    
    
    CompilationMode = None
    
    
    Error = None
    
    
    Loading = None
    
    
    Null = None
    
    
    PreferSynchronous = None
    
    
    Ready = None
    
    
    Status = None
    
    
    __new__ = None
    
    
    progressChanged = None
    
    
    staticMetaObject = None
    
    
    statusChanged = None


class QQmlIncubator(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __nonzero__(*args, **kwargs):
        """
        x.__nonzero__() <==> x != 0
        """
    
        pass
    
    
    def clear(*args, **kwargs):
        pass
    
    
    def errors(*args, **kwargs):
        pass
    
    
    def forceCompletion(*args, **kwargs):
        pass
    
    
    def incubationMode(*args, **kwargs):
        pass
    
    
    def isError(*args, **kwargs):
        pass
    
    
    def isLoading(*args, **kwargs):
        pass
    
    
    def isNull(*args, **kwargs):
        pass
    
    
    def isReady(*args, **kwargs):
        pass
    
    
    def object(*args, **kwargs):
        pass
    
    
    def setInitialState(*args, **kwargs):
        pass
    
    
    def status(*args, **kwargs):
        pass
    
    
    def statusChanged(*args, **kwargs):
        pass
    
    
    Asynchronous = None
    
    
    AsynchronousIfNested = None
    
    
    Error = None
    
    
    IncubationMode = None
    
    
    Loading = None
    
    
    Null = None
    
    
    Ready = None
    
    
    Status = None
    
    
    Synchronous = None
    
    
    __new__ = None


class QQmlTypesExtensionInterface(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def registerTypes(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlPropertyMap(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def clear(*args, **kwargs):
        pass
    
    
    def contains(*args, **kwargs):
        pass
    
    
    def count(*args, **kwargs):
        pass
    
    
    def insert(*args, **kwargs):
        pass
    
    
    def isEmpty(*args, **kwargs):
        pass
    
    
    def keys(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    def updateValue(*args, **kwargs):
        pass
    
    
    def value(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None
    
    
    valueChanged = None


class QQmlScriptString(_Object):
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
    
    
    def booleanLiteral(*args, **kwargs):
        pass
    
    
    def isEmpty(*args, **kwargs):
        pass
    
    
    def isNullLiteral(*args, **kwargs):
        pass
    
    
    def isUndefinedLiteral(*args, **kwargs):
        pass
    
    
    def numberLiteral(*args, **kwargs):
        pass
    
    
    def stringLiteral(*args, **kwargs):
        pass
    
    
    __new__ = None


class QJSValueIterator(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def hasNext(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def next(*args, **kwargs):
        pass
    
    
    def value(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlListReference(_Object):
    def __copy__(*args, **kwargs):
        pass
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def append(*args, **kwargs):
        pass
    
    
    def at(*args, **kwargs):
        pass
    
    
    def canAppend(*args, **kwargs):
        pass
    
    
    def canAt(*args, **kwargs):
        pass
    
    
    def canClear(*args, **kwargs):
        pass
    
    
    def canCount(*args, **kwargs):
        pass
    
    
    def clear(*args, **kwargs):
        pass
    
    
    def count(*args, **kwargs):
        pass
    
    
    def isManipulable(*args, **kwargs):
        pass
    
    
    def isReadable(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def listElementType(*args, **kwargs):
        pass
    
    
    def object(*args, **kwargs):
        pass
    
    
    __new__ = None


class QQmlFile(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def __nonzero__(*args, **kwargs):
        """
        x.__nonzero__() <==> x != 0
        """
    
        pass
    
    
    def clear(*args, **kwargs):
        pass
    
    
    def connectDownloadProgress(*args, **kwargs):
        pass
    
    
    def connectFinished(*args, **kwargs):
        pass
    
    
    def data(*args, **kwargs):
        pass
    
    
    def dataByteArray(*args, **kwargs):
        pass
    
    
    def error(*args, **kwargs):
        pass
    
    
    def isError(*args, **kwargs):
        pass
    
    
    def isLoading(*args, **kwargs):
        pass
    
    
    def isNull(*args, **kwargs):
        pass
    
    
    def isReady(*args, **kwargs):
        pass
    
    
    def load(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    def status(*args, **kwargs):
        pass
    
    
    def url(*args, **kwargs):
        pass
    
    
    def isLocalFile(*args, **kwargs):
        pass
    
    
    def isSynchronous(*args, **kwargs):
        pass
    
    
    def urlToLocalFileOrQrc(*args, **kwargs):
        pass
    
    
    Error = None
    
    
    Loading = None
    
    
    Null = None
    
    
    Ready = None
    
    
    Status = None
    
    
    __new__ = None


class ListProperty(_Property):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass


class QQmlEngine(QJSEngine):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def addImageProvider(*args, **kwargs):
        pass
    
    
    def addImportPath(*args, **kwargs):
        pass
    
    
    def addNamedBundle(*args, **kwargs):
        pass
    
    
    def addPluginPath(*args, **kwargs):
        pass
    
    
    def baseUrl(*args, **kwargs):
        pass
    
    
    def clearComponentCache(*args, **kwargs):
        pass
    
    
    def event(*args, **kwargs):
        pass
    
    
    def imageProvider(*args, **kwargs):
        pass
    
    
    def importPathList(*args, **kwargs):
        pass
    
    
    def importPlugin(*args, **kwargs):
        pass
    
    
    def incubationController(*args, **kwargs):
        pass
    
    
    def networkAccessManager(*args, **kwargs):
        pass
    
    
    def networkAccessManagerFactory(*args, **kwargs):
        pass
    
    
    def offlineStoragePath(*args, **kwargs):
        pass
    
    
    def outputWarningsToStandardError(*args, **kwargs):
        pass
    
    
    def pluginPathList(*args, **kwargs):
        pass
    
    
    def removeImageProvider(*args, **kwargs):
        pass
    
    
    def rootContext(*args, **kwargs):
        pass
    
    
    def setBaseUrl(*args, **kwargs):
        pass
    
    
    def setImportPathList(*args, **kwargs):
        pass
    
    
    def setIncubationController(*args, **kwargs):
        pass
    
    
    def setNetworkAccessManagerFactory(*args, **kwargs):
        pass
    
    
    def setOfflineStoragePath(*args, **kwargs):
        pass
    
    
    def setOutputWarningsToStandardError(*args, **kwargs):
        pass
    
    
    def setPluginPathList(*args, **kwargs):
        pass
    
    
    def setUrlInterceptor(*args, **kwargs):
        pass
    
    
    def trimComponentCache(*args, **kwargs):
        pass
    
    
    def urlInterceptor(*args, **kwargs):
        pass
    
    
    def contextForObject(*args, **kwargs):
        pass
    
    
    def objectOwnership(*args, **kwargs):
        pass
    
    
    def setContextForObject(*args, **kwargs):
        pass
    
    
    def setObjectOwnership(*args, **kwargs):
        pass
    
    
    CppOwnership = None
    
    
    JavaScriptOwnership = None
    
    
    ObjectOwnership = None
    
    
    __new__ = None
    
    
    quit = None
    
    
    staticMetaObject = None
    
    
    warnings = None


class QQmlExtensionPlugin(_QObject, QQmlExtensionInterface):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def baseUrl(*args, **kwargs):
        pass
    
    
    def initializeEngine(*args, **kwargs):
        pass
    
    
    def registerTypes(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QQmlApplicationEngine(QQmlEngine):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def load(*args, **kwargs):
        pass
    
    
    def loadData(*args, **kwargs):
        pass
    
    
    def rootObjects(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    objectCreated = None
    
    
    staticMetaObject = None



def qmlRegisterType(*args, **kwargs):
    pass



QML_HAS_ATTACHED_PROPERTIES = 1


