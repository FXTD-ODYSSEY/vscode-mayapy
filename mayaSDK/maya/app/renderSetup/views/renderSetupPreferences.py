def setDefaultPreset(*args, **kwargs):
    pass


def _selectPath(userTextField, option, title):
    pass


def getGlobalPresets(renderer):
    """
    # Returns the list of presets in the global presets directory.
    """

    pass


def getUserPresets(renderer):
    """
    # Returns the list of presets in the user presets directory.
    """

    pass


def deleteUserPreset(preset, warn='True'):
    """
    # Deletes a user preset. Note: for testing purposes, noWarn can be set to True
    # to prevent a warning popup box on delete, this should only be used for 
    # testing!
    """

    pass


def _getPresets(renderer, basePath):
    """
    # Returns the list of presets in the specified base path.
    """

    pass


def addRenderSetupPreferences():
    pass


def savePreset(filePath='None'):
    """
    # Saves a preset to a user specified location. Note: for testing purposes, a
    # filename can be passed in, this should only be used for testing!
    """

    pass


def loadGlobalPreset(*args, **kwargs):
    pass


def _syncOptionVarWithTextField(userTextField, option):
    pass


def _loadPreset(preset, basePath):
    """
    # Loads the specified preset from the specified directory
    """

    pass


def loadUserPreset(*args, **kwargs):
    pass



kCancel = []

kInvalidPresetFound = []

kGlobalTemplatesLocation = []

kGlobalPresetsLocation = []

kDeletePreset = []

kSavePreset = []

kSelectUserPresetsLocation = []

kUserPresetsLocation = []

kSelectUserTemplatesLocation = []

kSelectGlobalTemplatesLocation = []

kRenderSetupTemplatesTitle = []

kRenderSettingsPresetsTitle = []

kDeletePresetMsg = []

kUserTemplatesLocation = []

kDelete = []

kSelectGlobalPresetsLocation = []


