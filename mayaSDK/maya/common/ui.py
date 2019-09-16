from functools import partial

class LayoutManager(object):
    """
    This class is a simple manager that is responsible for returning to the
    parent layout when exiting.
    
    It should be used when layering several layouts to make it easier to track
    which layout is currently being populated.  It makes code easier to read by
    grouping all UI creation under a given layout within the same indentation
    level.
    """
    
    
    
    def __enter__(self):
        """
        When entering the ``with`` statement, this object returns the
        handled layout.
        """
    
        pass
    
    
    def __exit__(self, type, value, traceback):
        pass
    
    
    def __init__(self, name):
        """
        Simple constructor that just remembers the name of the given layout.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def showMessageBox(title, message, icon='None'):
    """
    This method pops up a Maya message box with the given title and the given
    message.
    
    It also accepts an optional icon parameter which can receive the same
    values as the confirmDialog command does.
    """

    pass


def scrollableMessageBox(title, messageCallback):
    """
    Use showMessageBox for simple messages. This one is for longer, possibly
    externally generated, ones that may need periodic refreshing.
    
    Pops up a Maya message box with the given title and the given
    message with scrolling capabilities for longer messages and extra
    controls:
    
        Refresh   : Call the provided method that will reload the window content
        Copy      : Copy the current highlighted text to the clipboard, all if no highlights
        Highlight : Color any text matching the highlight string, for easy viewing
    
    :param title: Window title for the message box
    :param messageCallback: Method called that will supply the output text on demand
    :return: The name of the output text control (for reading back)
    """

    pass


def unix_cmd_exists(cmd):
    """
    Simple utility to see if a command is accessible in the current shell path
    """

    pass


def showConfirmationDialog(title, message):
    """
    This method pops up a Maya confirmation dialog with the given title and the
    given message.
    
    It returns True if the user accepted, False otherwise.
    """

    pass


def getClipboardData():
    """
    Retrieve data from the clipboard.
    """

    pass


def uiCallbackWrapper(*args, **kwargs):
    """
    This method is a wrapper in the form expected by UI elements.
    
    Its signature allows it to be flexible with regards to what UI elements
    expects.  Then it simply calls the given functor.
    
    Sample use:
        reload_functor = partial(THE_RELOAD_CALLBACK_METHOD, reload_arg=SOME_RELOAD_ARGUMENT)
        reload_command = partial(uiCallbackWrapper, functor=reload_functor)
    """

    pass


def copyScrollableMessageBox(output_field):
    """
    Copy the highlighted output from the scrollable text area. If nothing
    is highlighted then copy everything.
    
    :param output_field:    Scrollable text field control containing the output
    """

    pass


def setClipboardData(data):
    """
    Set data onto the clipboard.
    """

    pass


def reloadScrollableMessageBox(messageCallback, output_field, filter_field):
    """
    Reload the output into the scrollable text area, using the filter
    information to highlight sections of interest where needed.
    
    :param messageCallback: Method to call that will provide the text as an
                            array, one line per array entry or a single string
                            with embedded linefeeds.
    :param output_field:    Scrollable text field control containing the output
    :param filter_field:    Text field containing the highlight filter
    """

    pass



FAKE_CLIPBOARD = None


