"""
This module encapsulates functions to use the autoKeyframe command to
support auto keying of overrides.

If an overridden attribute is written to, and it is overridden by a value
override, the apply override chain is traversed, and the appropriate
override attribute is written to (see the applyOverride module
documentation for details).

If this override attribute satisfies the autoKeyframe requirements, which
include among others:

- Have at least one keyframe set
- Support the keyable property (see plug.Plug.isKeyable documentation for
  semantics)

Then the override attribute will be keyframed.

Using the autoKeyframe command has the following desirable properties:

- The autoKeyframe code fully encapsulates what attributes are interesting
  to auto key.
- The autoKeyframe code correctly handles undo / redo so that any key
  frame addition is undone atomically with the corresponding set value command.
"""

def setValue(mPlug, value, autoKey):
    """
    Set the argument value on the argument plug, setting an
    autoKeyframe on that attribute, if autoKey is True.
    
    The plug argument must be an MPlug.
    """

    pass


def isEnabled():
    pass


def autoKeyed():
    """
    Returns the attribute(s) that the autoKeyframe command will set.
    
    The attribute(s) is returned in a set.  If autoKeyframe is off, an
    empty set is returned.
    """

    pass



