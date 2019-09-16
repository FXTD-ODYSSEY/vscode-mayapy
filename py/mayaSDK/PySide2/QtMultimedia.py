from PySide2.QtCore import QObject as _QObject

class _Object(object):
    __dict__ = None


class QAudio(_Object):
    ActiveState = None
    
    
    AudioInput = None
    
    
    AudioOutput = None
    
    
    Error = None
    
    
    FatalError = None
    
    
    IOError = None
    
    
    IdleState = None
    
    
    Mode = None
    
    
    NoError = None
    
    
    OpenError = None
    
    
    State = None
    
    
    StoppedState = None
    
    
    SuspendedState = None
    
    
    UnderrunError = None


class QAbstractAudioDeviceInfo(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def deviceName(*args, **kwargs):
        pass
    
    
    def isFormatSupported(*args, **kwargs):
        pass
    
    
    def preferredFormat(*args, **kwargs):
        pass
    
    
    def supportedByteOrders(*args, **kwargs):
        pass
    
    
    def supportedChannelCounts(*args, **kwargs):
        pass
    
    
    def supportedCodecs(*args, **kwargs):
        pass
    
    
    def supportedSampleRates(*args, **kwargs):
        pass
    
    
    def supportedSampleSizes(*args, **kwargs):
        pass
    
    
    def supportedSampleTypes(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    staticMetaObject = None


class QAbstractAudioInput(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def bufferSize(*args, **kwargs):
        pass
    
    
    def bytesReady(*args, **kwargs):
        pass
    
    
    def elapsedUSecs(*args, **kwargs):
        pass
    
    
    def error(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def notifyInterval(*args, **kwargs):
        pass
    
    
    def periodSize(*args, **kwargs):
        pass
    
    
    def processedUSecs(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def resume(*args, **kwargs):
        pass
    
    
    def setBufferSize(*args, **kwargs):
        pass
    
    
    def setFormat(*args, **kwargs):
        pass
    
    
    def setNotifyInterval(*args, **kwargs):
        pass
    
    
    def setVolume(*args, **kwargs):
        pass
    
    
    def start(*args, **kwargs):
        pass
    
    
    def state(*args, **kwargs):
        pass
    
    
    def stop(*args, **kwargs):
        pass
    
    
    def suspend(*args, **kwargs):
        pass
    
    
    def volume(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    errorChanged = None
    
    
    notify = None
    
    
    stateChanged = None
    
    
    staticMetaObject = None


class QAbstractAudioOutput(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def bufferSize(*args, **kwargs):
        pass
    
    
    def bytesFree(*args, **kwargs):
        pass
    
    
    def category(*args, **kwargs):
        pass
    
    
    def elapsedUSecs(*args, **kwargs):
        pass
    
    
    def error(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def notifyInterval(*args, **kwargs):
        pass
    
    
    def periodSize(*args, **kwargs):
        pass
    
    
    def processedUSecs(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def resume(*args, **kwargs):
        pass
    
    
    def setBufferSize(*args, **kwargs):
        pass
    
    
    def setCategory(*args, **kwargs):
        pass
    
    
    def setFormat(*args, **kwargs):
        pass
    
    
    def setNotifyInterval(*args, **kwargs):
        pass
    
    
    def setVolume(*args, **kwargs):
        pass
    
    
    def start(*args, **kwargs):
        pass
    
    
    def state(*args, **kwargs):
        pass
    
    
    def stop(*args, **kwargs):
        pass
    
    
    def suspend(*args, **kwargs):
        pass
    
    
    def volume(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    errorChanged = None
    
    
    notify = None
    
    
    stateChanged = None
    
    
    staticMetaObject = None


class QAudioFormat(_Object):
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
    
    
    def byteOrder(*args, **kwargs):
        pass
    
    
    def bytesForDuration(*args, **kwargs):
        pass
    
    
    def bytesForFrames(*args, **kwargs):
        pass
    
    
    def bytesPerFrame(*args, **kwargs):
        pass
    
    
    def channelCount(*args, **kwargs):
        pass
    
    
    def codec(*args, **kwargs):
        pass
    
    
    def durationForBytes(*args, **kwargs):
        pass
    
    
    def durationForFrames(*args, **kwargs):
        pass
    
    
    def framesForBytes(*args, **kwargs):
        pass
    
    
    def framesForDuration(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def sampleRate(*args, **kwargs):
        pass
    
    
    def sampleSize(*args, **kwargs):
        pass
    
    
    def sampleType(*args, **kwargs):
        pass
    
    
    def setByteOrder(*args, **kwargs):
        pass
    
    
    def setChannelCount(*args, **kwargs):
        pass
    
    
    def setCodec(*args, **kwargs):
        pass
    
    
    def setSampleRate(*args, **kwargs):
        pass
    
    
    def setSampleSize(*args, **kwargs):
        pass
    
    
    def setSampleType(*args, **kwargs):
        pass
    
    
    BigEndian = None
    
    
    Endian = None
    
    
    Float = None
    
    
    LittleEndian = None
    
    
    SampleType = None
    
    
    SignedInt = None
    
    
    UnSignedInt = None
    
    
    Unknown = None
    
    
    __new__ = None


class QAbstractVideoBuffer(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def handle(*args, **kwargs):
        pass
    
    
    def handleType(*args, **kwargs):
        pass
    
    
    def mapMode(*args, **kwargs):
        pass
    
    
    def release(*args, **kwargs):
        pass
    
    
    def unmap(*args, **kwargs):
        pass
    
    
    m_type = None
    
    CoreImageHandle = None
    
    
    EGLImageHandle = None
    
    
    GLTextureHandle = None
    
    
    HandleType = None
    
    
    MapMode = None
    
    
    NoHandle = None
    
    
    NotMapped = None
    
    
    QPixmapHandle = None
    
    
    ReadOnly = None
    
    
    ReadWrite = None
    
    
    UserHandle = None
    
    
    WriteOnly = None
    
    
    XvShmImageHandle = None
    
    
    __new__ = None


class QVideoSurfaceFormat(_Object):
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
    
    
    def frameHeight(*args, **kwargs):
        pass
    
    
    def frameRate(*args, **kwargs):
        pass
    
    
    def frameSize(*args, **kwargs):
        pass
    
    
    def frameWidth(*args, **kwargs):
        pass
    
    
    def handleType(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def pixelAspectRatio(*args, **kwargs):
        pass
    
    
    def pixelFormat(*args, **kwargs):
        pass
    
    
    def property(*args, **kwargs):
        pass
    
    
    def propertyNames(*args, **kwargs):
        pass
    
    
    def scanLineDirection(*args, **kwargs):
        pass
    
    
    def setFrameRate(*args, **kwargs):
        pass
    
    
    def setFrameSize(*args, **kwargs):
        pass
    
    
    def setPixelAspectRatio(*args, **kwargs):
        pass
    
    
    def setProperty(*args, **kwargs):
        pass
    
    
    def setScanLineDirection(*args, **kwargs):
        pass
    
    
    def setViewport(*args, **kwargs):
        pass
    
    
    def setYCbCrColorSpace(*args, **kwargs):
        pass
    
    
    def sizeHint(*args, **kwargs):
        pass
    
    
    def viewport(*args, **kwargs):
        pass
    
    
    def yCbCrColorSpace(*args, **kwargs):
        pass
    
    
    BottomToTop = None
    
    
    Direction = None
    
    
    TopToBottom = None
    
    
    YCbCrColorSpace = None
    
    
    YCbCr_BT601 = None
    
    
    YCbCr_BT709 = None
    
    
    YCbCr_CustomMatrix = None
    
    
    YCbCr_JPEG = None
    
    
    YCbCr_Undefined = None
    
    
    YCbCr_xvYCC601 = None
    
    
    YCbCr_xvYCC709 = None
    
    
    __new__ = None


class QAudioOutput(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def bufferSize(*args, **kwargs):
        pass
    
    
    def bytesFree(*args, **kwargs):
        pass
    
    
    def category(*args, **kwargs):
        pass
    
    
    def elapsedUSecs(*args, **kwargs):
        pass
    
    
    def error(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def notifyInterval(*args, **kwargs):
        pass
    
    
    def periodSize(*args, **kwargs):
        pass
    
    
    def processedUSecs(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def resume(*args, **kwargs):
        pass
    
    
    def setBufferSize(*args, **kwargs):
        pass
    
    
    def setCategory(*args, **kwargs):
        pass
    
    
    def setNotifyInterval(*args, **kwargs):
        pass
    
    
    def setVolume(*args, **kwargs):
        pass
    
    
    def start(*args, **kwargs):
        pass
    
    
    def state(*args, **kwargs):
        pass
    
    
    def stop(*args, **kwargs):
        pass
    
    
    def suspend(*args, **kwargs):
        pass
    
    
    def volume(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    notify = None
    
    
    stateChanged = None
    
    
    staticMetaObject = None


class QVideoFrame(_Object):
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
    
    
    def availableMetaData(*args, **kwargs):
        pass
    
    
    def bits(*args, **kwargs):
        pass
    
    
    def bytesPerLine(*args, **kwargs):
        pass
    
    
    def endTime(*args, **kwargs):
        pass
    
    
    def fieldType(*args, **kwargs):
        pass
    
    
    def handle(*args, **kwargs):
        pass
    
    
    def handleType(*args, **kwargs):
        pass
    
    
    def height(*args, **kwargs):
        pass
    
    
    def isMapped(*args, **kwargs):
        pass
    
    
    def isReadable(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def isWritable(*args, **kwargs):
        pass
    
    
    def map(*args, **kwargs):
        pass
    
    
    def mapMode(*args, **kwargs):
        pass
    
    
    def mappedBytes(*args, **kwargs):
        pass
    
    
    def metaData(*args, **kwargs):
        pass
    
    
    def pixelFormat(*args, **kwargs):
        pass
    
    
    def planeCount(*args, **kwargs):
        pass
    
    
    def setEndTime(*args, **kwargs):
        pass
    
    
    def setFieldType(*args, **kwargs):
        pass
    
    
    def setMetaData(*args, **kwargs):
        pass
    
    
    def setStartTime(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    def startTime(*args, **kwargs):
        pass
    
    
    def unmap(*args, **kwargs):
        pass
    
    
    def width(*args, **kwargs):
        pass
    
    
    def imageFormatFromPixelFormat(*args, **kwargs):
        pass
    
    
    def pixelFormatFromImageFormat(*args, **kwargs):
        pass
    
    
    BottomField = None
    
    
    FieldType = None
    
    
    Format_ARGB32 = None
    
    
    Format_ARGB32_Premultiplied = None
    
    
    Format_ARGB8565_Premultiplied = None
    
    
    Format_AYUV444 = None
    
    
    Format_AYUV444_Premultiplied = None
    
    
    Format_AdobeDng = None
    
    
    Format_BGR24 = None
    
    
    Format_BGR32 = None
    
    
    Format_BGR555 = None
    
    
    Format_BGR565 = None
    
    
    Format_BGRA32 = None
    
    
    Format_BGRA32_Premultiplied = None
    
    
    Format_BGRA5658_Premultiplied = None
    
    
    Format_CameraRaw = None
    
    
    Format_IMC1 = None
    
    
    Format_IMC2 = None
    
    
    Format_IMC3 = None
    
    
    Format_IMC4 = None
    
    
    Format_Invalid = None
    
    
    Format_Jpeg = None
    
    
    Format_NV12 = None
    
    
    Format_NV21 = None
    
    
    Format_RGB24 = None
    
    
    Format_RGB32 = None
    
    
    Format_RGB555 = None
    
    
    Format_RGB565 = None
    
    
    Format_UYVY = None
    
    
    Format_User = None
    
    
    Format_Y16 = None
    
    
    Format_Y8 = None
    
    
    Format_YUV420P = None
    
    
    Format_YUV444 = None
    
    
    Format_YUYV = None
    
    
    Format_YV12 = None
    
    
    InterlacedFrame = None
    
    
    PixelFormat = None
    
    
    ProgressiveFrame = None
    
    
    TopField = None
    
    
    __new__ = None


class QAudioDeviceInfo(_Object):
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
    
    
    def __nonzero__(*args, **kwargs):
        """
        x.__nonzero__() <==> x != 0
        """
    
        pass
    
    
    def deviceName(*args, **kwargs):
        pass
    
    
    def isFormatSupported(*args, **kwargs):
        pass
    
    
    def isNull(*args, **kwargs):
        pass
    
    
    def nearestFormat(*args, **kwargs):
        pass
    
    
    def preferredFormat(*args, **kwargs):
        pass
    
    
    def supportedByteOrders(*args, **kwargs):
        pass
    
    
    def supportedChannelCounts(*args, **kwargs):
        pass
    
    
    def supportedCodecs(*args, **kwargs):
        pass
    
    
    def supportedSampleRates(*args, **kwargs):
        pass
    
    
    def supportedSampleSizes(*args, **kwargs):
        pass
    
    
    def supportedSampleTypes(*args, **kwargs):
        pass
    
    
    def availableDevices(*args, **kwargs):
        pass
    
    
    def defaultInputDevice(*args, **kwargs):
        pass
    
    
    def defaultOutputDevice(*args, **kwargs):
        pass
    
    
    __new__ = None


class QAudioInput(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def bufferSize(*args, **kwargs):
        pass
    
    
    def bytesReady(*args, **kwargs):
        pass
    
    
    def elapsedUSecs(*args, **kwargs):
        pass
    
    
    def error(*args, **kwargs):
        pass
    
    
    def format(*args, **kwargs):
        pass
    
    
    def notifyInterval(*args, **kwargs):
        pass
    
    
    def periodSize(*args, **kwargs):
        pass
    
    
    def processedUSecs(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def resume(*args, **kwargs):
        pass
    
    
    def setBufferSize(*args, **kwargs):
        pass
    
    
    def setNotifyInterval(*args, **kwargs):
        pass
    
    
    def setVolume(*args, **kwargs):
        pass
    
    
    def start(*args, **kwargs):
        pass
    
    
    def state(*args, **kwargs):
        pass
    
    
    def stop(*args, **kwargs):
        pass
    
    
    def suspend(*args, **kwargs):
        pass
    
    
    def volume(*args, **kwargs):
        pass
    
    
    __new__ = None
    
    
    notify = None
    
    
    stateChanged = None
    
    
    staticMetaObject = None


class QAbstractVideoSurface(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def error(*args, **kwargs):
        pass
    
    
    def isActive(*args, **kwargs):
        pass
    
    
    def isFormatSupported(*args, **kwargs):
        pass
    
    
    def nativeResolution(*args, **kwargs):
        pass
    
    
    def nearestFormat(*args, **kwargs):
        pass
    
    
    def present(*args, **kwargs):
        pass
    
    
    def setError(*args, **kwargs):
        pass
    
    
    def setNativeResolution(*args, **kwargs):
        pass
    
    
    def start(*args, **kwargs):
        pass
    
    
    def stop(*args, **kwargs):
        pass
    
    
    def supportedPixelFormats(*args, **kwargs):
        pass
    
    
    def surfaceFormat(*args, **kwargs):
        pass
    
    
    Error = None
    
    
    IncorrectFormatError = None
    
    
    NoError = None
    
    
    ResourceError = None
    
    
    StoppedError = None
    
    
    UnsupportedFormatError = None
    
    
    __new__ = None
    
    
    activeChanged = None
    
    
    nativeResolutionChanged = None
    
    
    staticMetaObject = None
    
    
    supportedFormatsChanged = None
    
    
    surfaceFormatChanged = None



