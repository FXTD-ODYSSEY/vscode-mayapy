def animCurveEditor(q=1,e=1,acs=1,af="string",aft="string",cm=1,ct="string",cd="uint",ctl=1,cs=1,csf=1,dt="string",dcc="string",dat="string",dak="string",di="string",dk="string",dn=1,dtn="string",dv="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",kt="string",lck=1,la="string",mlc="string",m="script",ncc="string",o="string",pnl="string",p="string",psh=1,rnc=1,rs="time",rss="int",ru="string",slc="string",acn=1,sb="string",scn=1,sr="string",suc=1,s="string",st="string",sv="string",sc=1,scx="float",scm="float",scs="float",sts=1,up=1,ulk=1,upd=1,ut="string",vlt="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/animCurveEditor.html



-----------------------------------------

animCurveEditor is undoable, queryable, and editable.

Edit a characteristic of a graph editor


-----------------------------------------


Return Value:

string  Editor name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

acs   : areCurvesSelected [boolean] ['query']
    Returns a boolean to know if at least one curve is selected in the graph editor.

-----------------------------------------

af    : autoFit         [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view.

-----------------------------------------

aft   : autoFitTime     [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view along the time axis, as well.

-----------------------------------------

cm    : classicMode     [boolean] ['query', 'edit']
    When on, the graph editor is displayed in "Classic Mode", otherwise "Suites Mode" is used.

-----------------------------------------

ct    : clipTime        [string] ['query', 'edit']
    Valid values: "on" "off"   Display the clips with their offset and scale applied to the anim curves in the clip.

-----------------------------------------

cd    : constrainDrag   [uint] ['query', 'edit']
    Constrains all Graph Editor animation curve drag operations to either the X-axis, the Y-axis, or to neither of those axes. Values to supply are: 0 for not constraining any axis, 1 for constraing the X-axis, or 2 for constraining the Y-axis. When used in queries, this flag returns the latter values and these values have the same interpretation as above. Note: when the shift key is pressed before dragging the animation curve, the first mouse movement will instead determine (and override) any prior set constrained axis.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

cs    : curvesShown     [boolean] ['query']
    Returns a string array containing the names of the animCurve nodes currently displayed in the graph editor.

-----------------------------------------

csf   : curvesShownForceUpdate [boolean] ['query']
    Returns a string array containing the names of the animCurve nodes currently displayed in the graph editor. Unlike the curvesShown flag, this will force an update of the graph editor for the case where the mainListConnection has been modified since the last refresh.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dcc   : denormalizeCurvesCommand [string] ['edit']
    Sets the script that is run to denormalize curves in the graph editor. This is intended for internal use only.

-----------------------------------------

dat   : displayActiveKeyTangents [string] ['edit']
    on | off | tgl Display active key tangents in the editor.

-----------------------------------------

dak   : displayActiveKeys [string] ['edit']
    on | off | tgl Display active keys in the editor.

-----------------------------------------

di    : displayInfinities [string] ['edit']
    on | off | tgl Display infinities in the editor.

-----------------------------------------

dk    : displayKeys     [string] ['edit']
    on | off | tgl Display keyframes in the editor.

-----------------------------------------

dn    : displayNormalized [boolean] ['query', 'edit']
    When on, display all curves normalized to the range -1 to +1.

-----------------------------------------

dtn   : displayTangents [string] ['edit']
    on | off | tgl Display tangents in the editor.

-----------------------------------------

dv    : displayValues   [string] ['edit']
    on | off | tgl Display active keys and tangents values in the editor.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

kt    : keyingTime      [string] ['query']
    The current time in the given curve to be keyed in the graph editor.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

la    : lookAt          [string] ['edit']
    all | selected | currentTime FitView helpers.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

m     : menu            [script] []
    Specify a script to be run when the editor is created. The function will be passed one string argument which is the new editor's name.

-----------------------------------------

ncc   : normalizeCurvesCommand [string] ['edit']
    Sets the script that is run to normalize curves in the graph editor. This is intended for internal use only.

-----------------------------------------

o     : outliner        [string] ['query', 'edit']
    The name of the outliner that is associated with the graph editor.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

psh   : preSelectionHighlight [boolean] ['query', 'edit']
    When on, the curve/key/tangent under the mouse pointer is highlighted to ease selection.

-----------------------------------------

rnc   : renormalizeCurves [boolean] ['edit']
    This flag causes the curve normalization factors to be recalculated.

-----------------------------------------

rs    : resultSamples   [time] ['query', 'edit']
    Specify the sampling for result curves   Note: the smaller this number is, the longer it will take to update the display.

-----------------------------------------

rss   : resultScreenSamples [int] ['query', 'edit']
    Specify the screen base result sampling for result curves. If 0, then results are sampled in time.

-----------------------------------------

ru    : resultUpdate    [string] ['query', 'edit']
    Valid values: "interactive" "delayed"   Controls how changes to animCurves are reflected in the result curves (if results are being shown). If resultUpdate is "interactive", then as interactive changes are being made to the animCurve, the result curves will be updated. If modelUpdate is delayed (which is the default setting), then result curves are updated once the final change to an animCurve has been made.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

acn   : showActiveCurveNames [boolean] ['query', 'edit']
    Display the active curve(s)'s name.

-----------------------------------------

sb    : showBufferCurves [string] ['query', 'edit']
    Valid values: "on" "off" "tgl"   Display buffer curves.

-----------------------------------------

scn   : showCurveNames  [boolean] ['query', 'edit']
    Display the curves's name.

-----------------------------------------

sr    : showResults     [string] ['query', 'edit']
    Valid values: "on" "off" "tgl"   Display result curves from expression or other non-keyed action.

-----------------------------------------

suc   : showUpstreamCurves [boolean] ['query', 'edit']
    If true, the dependency graph is searched upstream for all curves that drive the selected plugs (showing multiple curves for example in a typical driven key setup, where first the driven key curve is encountered, followed by the actual animation curve that drives the source object). If false, only the first curves encountered will be shown. Note that, even if false, multiple curves can be shown if e.g. a blendWeighted node is being used to combine multiple curves.

-----------------------------------------

s     : smoothness      [string] ['query', 'edit']
    Valid values: "coarse" "rough" "medium" "fine"   Specify the display smoothness of animation curves.

-----------------------------------------

st    : snapTime        [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in time.

-----------------------------------------

sv    : snapValue       [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in values.

-----------------------------------------

sc    : stackedCurves   [boolean] ['query', 'edit']
    Switches the display mode between normal (all curves sharing one set of axes) to stacked (each curve on its own value axis, stacked vertically).

-----------------------------------------

scx   : stackedCurvesMax [float] ['query', 'edit']
    Sets the maximum value on the per-curve value axis when in stacked mode.

-----------------------------------------

scm   : stackedCurvesMin [float] ['query', 'edit']
    Sets the minimum value on the per-curve value axis when in stacked mode.

-----------------------------------------

scs   : stackedCurvesSpace [float] ['query', 'edit']
    Sets the spacing between curves when in stacked mode.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

vlt   : valueLinesToggle [string]
    on | off | tgl Display the value lines for high/low/zero of selected curves in the editor

    """

def animDisplay(q=1,e=1,upd="string",rae=1,tc="string",tco="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/animDisplay.html



-----------------------------------------

animDisplay is undoable, queryable, and editable.

This command changes certain display options used by animation windows.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

upd   : modelUpdate     [string] ['query', 'edit']
    Controls how changes to animCurves are propagated through the dependency graph. Valid modes are "none", "interactive" or "delayed". If modelUpdate is "none" then changing an animCurve will not cause the model to be updated (change currentTime in order to update the model). If modelUpdate is "interactive" (which is the default setting), then as interactive changes are being made to the animCurve, the model will be updated. If modelUpdate is delayed, then the model is updated once the final change to an animCurve has been made. With modelUpdate set to either "interactive" or "delayed", changes to animCurves made via commands will also cause the model to be updated.

-----------------------------------------

rae   : refAnimCurvesEditable [boolean] ['query', 'edit']
    Specify if animation curves from referenced files are editable.

-----------------------------------------

tc    : timeCode        [string] ['query', 'edit']
    Controls how time value are display. Valid values are "frame", "timecode", "fulltimecode". If the value is "frame" maya will display time in frame everywhere. If the value is "timecode" maya will display time in timecode in time slider, graph editor and dope sheet. If the value is "fulltimecode" maya will display time in timecode everywhere.

-----------------------------------------

tco   : timeCodeOffset  [string]
    This flag has now been deprecated. It still exists to not break legacy scripts, but it will now do nothing. See the new timeCode command to set and query timeCodes.

    """

def animLayer(q=1,e=1,akg=1,aso=1,afl=1,anc=1,at="string",bac=1,blr=1,bl=1,bld=1,c="string",col=1,cp="string",ca="string",cna="string",ebl=1,edn=1,een=1,ert=1,esc=1,etr=1,evs=1,ex=1,ea="string",fcv="string",fur=1,uir=1,lp="string",l=1,ml=1,mva="string",mvb="string",m=1,o=1,p="string",pth=1,prf=1,raa=1,ra="string",r="string",sel=1,s=1,w="float",wbd=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/animLayer.html



-----------------------------------------

animLayer is undoable, queryable, and editable.

This command creates and edits animation layers.


-----------------------------------------


Return Value:

string  Return values currently not documented.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

akg   : addRelatedKG    [boolean] ['query', 'edit']
    Used adding attributes to a layer. Determines if associated keying groups should be added or not to the layer.

-----------------------------------------

aso   : addSelectedObjects [boolean] ['query', 'edit']
    Adds selected object(s) to the layer.

-----------------------------------------

afl   : affectedLayers  [boolean] ['query']
    Return the layers that the currently selected object(s) are members of

-----------------------------------------

anc   : animCurves      [boolean] ['query', 'edit']
    In query mode returns the anim curves associated with this layer

-----------------------------------------

at    : attribute       [string] ['query', 'edit']
    Adds a specific attribute on a object to the layer.

-----------------------------------------

bac   : baseAnimCurves  [boolean] ['query', 'edit']
    In query mode returns the base layer anim curves associated with this layer, if any.

-----------------------------------------

blr   : bestAnimLayer   [boolean] ['query', 'edit']
    In query mode returns the best anim layers for keying for the selected objects. If used in conjunction with -at, will return the best anim layers for keying for the specific plugs (attributes) specified.

-----------------------------------------

bl    : bestLayer       [boolean] ['query']
    Return the layer that will be keyed for specified attribute.

-----------------------------------------

bld   : blendNodes      [boolean] ['query', 'edit']
    In query mode returns the blend nodes associated with this layer

-----------------------------------------

c     : children        [string] ['query']
    Get the list of children layers. Return value is a string array.

-----------------------------------------

col   : collapse        [boolean] ['query', 'edit']
    Determine if a layer is collapse in the layer editor.

-----------------------------------------

cp    : copy            [string] ['edit']
    Copy from layer.

-----------------------------------------

ca    : copyAnimation   [string] ['edit']
    Copy animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.

-----------------------------------------

cna   : copyNoAnimation [string] ['edit']
    Copy from layer without the animation curves.

-----------------------------------------

ebl   : excludeBoolean  [boolean] ['query', 'edit']
    When adding selected object(s) to the layer, excludes any boolean attributes.

-----------------------------------------

edn   : excludeDynamic  [boolean] ['query', 'edit']
    When adding selected object(s) to the layer, excludes any dynamic attributes.

-----------------------------------------

een   : excludeEnum     [boolean] ['query', 'edit']
    When adding selected object(s) to the layer, excludes any enum attributes.

-----------------------------------------

ert   : excludeRotate   [boolean] ['query', 'edit']
    When adding selected object(s) to the layer, exclude the rotate attribute.

-----------------------------------------

esc   : excludeScale    [boolean] ['query', 'edit']
    When adding selected object(s) to the layer, exclude the scale attribute.

-----------------------------------------

etr   : excludeTranslate [boolean] ['query', 'edit']
    When adding selected object(s) to the layer, excludes the translate attribute.

-----------------------------------------

evs   : excludeVisibility [boolean] ['query', 'edit']
    When adding selected object(s) to the layer, exclude the visibility attribute.

-----------------------------------------

ex    : exists          [boolean] ['query']
    Determine if an layer exists.

-----------------------------------------

ea    : extractAnimation [string] ['edit']
    Transfer animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.

-----------------------------------------

fcv   : findCurveForPlug [string] ['query', 'edit']
    Finds the parameter curve containing the animation data for the specified plug on the given layer.  In query mode, this flag needs a value.

-----------------------------------------

fur   : forceUIRebuild  [boolean] []
    Rebuilds the animation layers user interface.

-----------------------------------------

uir   : forceUIRefresh  [boolean] []
    Refreshes the animation layers user interface.

-----------------------------------------

lp    : layeredPlug     [string] ['query']
    Returns the plug on the blend node corresponding to the specified layer  In query mode, this flag needs a value.

-----------------------------------------

l     : lock            [boolean] ['query', 'edit']
    Set the lock state of the specified layer. A locked layer cannot receive key. Default is false.

-----------------------------------------

ml    : maxLayers       [boolean] ['query']
    Returns the maximum number of anim layers supported by this product.

-----------------------------------------

mva   : moveLayerAfter  [string] ['edit']
    Move layer after the specified layer

-----------------------------------------

mvb   : moveLayerBefore [string] ['edit']
    Move layer before the specified layer

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    Set the mute state of the specified layer. Default is false.

-----------------------------------------

o     : override        [boolean] ['query', 'edit']
    Set the overide state of the specified layer. Default is false.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Set the parent of the specified layer. Default is the animation layer root.

-----------------------------------------

pth   : passthrough     [boolean] ['query', 'edit']
    Set the passthrough state of the specified layer. Default is true.

-----------------------------------------

prf   : preferred       [boolean] ['query', 'edit']
    Determine if a layer is a preferred layer, the best layer algorithm will try to set keyframe in preferred layer first.

-----------------------------------------

raa   : removeAllAttributes [boolean] ['edit']
    Remove all objects from layer.

-----------------------------------------

ra    : removeAttribute [string] ['edit']
    Remove object from layer.

-----------------------------------------

r     : root            [string] ['query']
    Return the base layer if it exist

-----------------------------------------

sel   : selected        [boolean] ['query', 'edit']
    Determine if a layer is selected, a selected layer will be show in the timecontrol, graph editor.

-----------------------------------------

s     : solo            [boolean] ['query', 'edit']
    Set the solo state of the specified layer. Default is false.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Set the weight of the specified layer between 0.0 and 1.0. Default is 1.

-----------------------------------------

wbd   : writeBlendnodeDestinations [boolean]
    In edit mode writes the destination plugs of the blend nodes that belong to the layer into the blend node. This is used for layer import/export purposes and is not for general use.

    """

def animView(q=1,e=1,et="time",max="float",min="float",nv=1,pv=1,st="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/animView.html



-----------------------------------------

animView is undoable, queryable, and editable.

This command allows you to specify the current view range within an animation
editor.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

et    : endTime         [time] []
    End time to display within the editor

-----------------------------------------

max   : maxValue        [float] []
    Upper value to display within the editor

-----------------------------------------

min   : minValue        [float] []
    Lower value to display within the editor

-----------------------------------------

nv    : nextView        [boolean] ['edit']
    Switches to the next view.

-----------------------------------------

pv    : previousView    [boolean] ['edit']
    Switches to the previous view.

-----------------------------------------

st    : startTime       [time]
    Start time to display within the editor

    """

def autoKeyframe(q=1,e=1,aa="name",co="string",lsa=1,nr=1,st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/autoKeyframe.html



-----------------------------------------

autoKeyframe is undoable, queryable, and editable.

With no flags, this command will set keyframes on all attributes that have
been modified since an "autoKeyframe -state on" command was issued. To stop
keeping track of modified attributes, use "autoKeyframe -state off"

autoKeyframe does not create new animation curves. An attribute must have
already been keyframed (with the setKeyframe command) for autoKeyframe to add
new keyframes for modified attributes.

You can also query the current state of autoKeyframing with "autoKeyframe
-query -state".


-----------------------------------------


Return Value:

int  Number of keyframes set.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aa    : addAttr         [name] ['edit']
    Add to the list of plugs (node.attribute) that autoKeyframe is currently considering for auto keying. This list is transient and short-lived, and is reset as soon as autoKeyframe sets the keyframe or decides that no keyframe is to be set, on completion of the next set attribute.

-----------------------------------------

co    : characterOption [string] ['query', 'edit']
    Valid options are: "standard", "all". Dictates whether when auto-keying characters the auto-key works as usual or whether it keys all of the character attributes. Default is "standard".

-----------------------------------------

lsa   : listAttr        [boolean] ['query']
    Returns the list of plugs (node.attribute) that autoKeyframe is currently considering for auto keying. This list is transient and short-lived, and is reset as soon as autoKeyframe sets the keyframe or decides that no keyframe is to be set, on completion of the next set attribute.

-----------------------------------------

nr    : noReset         [boolean] ['edit']
    Must be used in conjunction with the state/st flag. When noReset/nr is specified, the list of plugs to be autokeyed is not cleared when the state changes

-----------------------------------------

st    : state           [boolean]
    turns on/off remembering of modified attributes

    """

def backgroundEvaluationManager(q=1,i=1,m="string",p=1,r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/backgroundEvaluationManager.html



-----------------------------------------

backgroundEvaluationManager is NOT undoable, queryable, and NOT editable.

Allows user to pause and restart background evaluations.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

i     : interrupt       [boolean] ['query']
    Enable or disable fast interrupt of background execution during interactive workflow.

-----------------------------------------

m     : mode            [string] ['query']
    Changes the current evaluation mode in the evaluation manager. Supported values are "serial" and "parallel".

-----------------------------------------

p     : pause           [boolean] ['query']
    Pause background evaluation. Will block till background evaluation is fully stopped. Can be queried to get the current state.

-----------------------------------------

r     : resume          [boolean]
    Resume background evaluation. Will start suspended evaluations unless someones else requested it.

    """

def bakeClip(b="[uint, uint]",ci="uint",k=1,n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bakeClip.html



-----------------------------------------

bakeClip is undoable, NOT queryable, and NOT editable.

This command is used to bake clips and blends into a single clip.


-----------------------------------------


Return Value:

string  clip name


-----------------------------------------


Flags:

-----------------------------------------

b     : blend           [[uint, uint]] []
    Specify the indices of the clips being blended.

-----------------------------------------

ci    : clipIndex       [uint] []
    Specify the index of the clip to bake.

-----------------------------------------

k     : keepOriginals   [boolean] []
    Keep original clips in the trax editor and place the merged clip into the visor. The default is to schedule the merged clip, and to keep the original clips in the visor.

-----------------------------------------

n     : name            [string]
    Specify the name of the new clip to create.

    """

def bakeResults(q=1,e=1,an="string",at="string",bol=1,cp=1,dl="string",dic=1,f="floatrange",hi="string",iub=1,index="uint",mr=1,osr="uint",pok=1,rba=1,ral=1,rwl="string",sb="time",s=1,sm=1,sr="[[, boolean, float, ]]",sac=1,t="timerange"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bakeResults.html



-----------------------------------------

bakeResults is undoable, queryable, and editable.

This command allows the user to replace a chain of dependency nodes which
define the value for an attribute with a single animation curve. Command
allows the user to specify the range and frequency of sampling.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, do not do anything. 

  * objects: Only act on specified objects. If there are no objects specified, do not do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices should be specified as a range, as shown below.

  * -time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
  * -index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.


-----------------------------------------


Return Value:

int  \- The number of channels baked    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." See command description for details.

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

bol   : bakeOnOverrideLayer [boolean] []
    If true, all layered and baked attribute will be added as a top override layer.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

dl    : destinationLayer [string] []
    This flag can be used to specify an existing layer where the baked results should be stored. Use this flag with caution. If the destination layer already has animation on it that contributes to the final result, it will be replaced by the output of the bake. As a result, it is possible that the combined animation visible in the scene is different before / after the baking process.

-----------------------------------------

dic   : disableImplicitControl [boolean] []
    Whether to disable implicit control after the anim curves are obtained as the result of this command. An implicit control to an attribute is some function that affects the attribute without using an explicit dependency graph connection. The control of IK, via ik handles, is an example.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. Note: when used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

mr    : minimizeRotation [boolean] []
    Specify whether to minimize the local Euler component from key to key during baking of rotation channels.

-----------------------------------------

osr   : oversamplingRate [uint] []
    Amount of samples per sampleBy period. Default is 1.

-----------------------------------------

pok   : preserveOutsideKeys [boolean] []
    Whether to preserve keys that are outside the bake range when there are directly connected animation curves or a pairBlend node which has an animation curve as its direct input. The default (false) is to remove frames outside the bake range. If the channel that you are baking is not controlled by a single animation curve, then a new animation curve will be created with keys only in the bake range. In the case of pairBlend-driven channels, setting pok to true will retain both the pairBlend and its input animCurve. The blended values will be baked onto the animCurve and the weight of the pairBlend weight will be keyed to the animCurve during the baked range.

-----------------------------------------

rba   : removeBakedAnimFromLayer [boolean] []
    If true, all baked animation will be removed from the layer. Otherwise all layer associated with the baked animation will be muted.

-----------------------------------------

ral   : removeBakedAttributeFromLayer [boolean] []
    If true, all baked attribute will be removed from the layer. Otherwise all layer associated with the baked attribute will be muted.

-----------------------------------------

rwl   : resolveWithoutLayer [string] []
    This flag can be used to specify a list of layers to be merged together during the bake process. This is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines the proper value to key on the destination layer to achieve the same result as the merged layers.

-----------------------------------------

sb    : sampleBy        [time] []
    Amount to sample by. Default is 1.0 in current timeUnit.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

sm    : simulation      [boolean] []
    Using this flag instructs the command to preform a simulation instead of just evaluating each attribute separately over the range of time. The simulation flag is required to bake animation that that depends on the whole scene being evaluated at each time step such as dynamics. The default is false.

-----------------------------------------

sr    : smart           [[[, boolean, float, ]]] []
    Specify whether to enable smart bake and the optional smart bake tolerance.

-----------------------------------------

sac   : sparseAnimCurveBake [boolean] []
    When this is true and anim curves are being baked, do not insert any keys into areas of the curve where animation is defined. And, use as few keys as possible to bake the pre and post infinity behavior. When this is false, one key will be inserted at each time step. The default is false.

-----------------------------------------

t     : time            [timerange]
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

    """

def bakeSimulation(q=1,e=1,an="string",at="string",bol=1,cp=1,dl="string",dic=1,f="floatrange",hi="string",iub=1,index="uint",mr=1,pok=1,rba=1,ral=1,rwl="string",sb="time",s=1,sm=1,sr="[[, boolean, float, ]]",sac=1,t="timerange"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bakeSimulation.html



-----------------------------------------

bakeSimulation is undoable, queryable, and editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

The bakeSimulation command is obsolete. Instead, "bakeResults -simulation
true" should be used. The bakeSimulation command has retained for backwards
compatibility.

This command allows the user to replace a chain of dependency nodes, or
implicit relationship, such as those between joints and IK handles, which
define the value of an attribute, with a single animation curve. Command
allows the user to specify the range and frequency of sampling. Unlike the
bakeResults command, this command will actually set the time of the current
scene to all the times, in sequence, inside the given time interval before it
sets the time back to when it is started. As a result, it may modify the
scene.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

bol   : bakeOnOverrideLayer [boolean] []
    If true, all layered and baked attributes will be added as a top override layer.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

dl    : destinationLayer [string] []
    This flag can be used to specify an existing layer where the baked results should be stored.

-----------------------------------------

dic   : disableImplicitControl [boolean] []
    Whether to disable implicit control after the anim curves are obtained as the result of this command. An implicit control to an attribute is some function that affects the attribute without using an explicit dependency graph connection. The control of IK, via ik handles, is an example.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

mr    : minimizeRotation [boolean] []
    Specify whether to minimize the local euler component from key to key during baking of rotation channels.

-----------------------------------------

pok   : preserveOutsideKeys [boolean] []
    Whether to preserve keys that are outside the bake range when there are directly connected animation curves. The default (false) is to remove frames outside the bake range. If the channel that you are baking is not controlled by a single animation curve, then a new animation curve will be created with keys only in the bake range.

-----------------------------------------

rba   : removeBakedAnimFromLayer [boolean] []
    If true, all baked animation will be removed from the layer.

-----------------------------------------

ral   : removeBakedAttributeFromLayer [boolean] []
    If true, all baked attributes will be removed from the layer.

-----------------------------------------

rwl   : resolveWithoutLayer [string] []
    This flag can be used to specify a list of layers to be merged together during the bake process. This is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines the proper value to key on the destination layer to achieve the same result as the merged layers.

-----------------------------------------

sb    : sampleBy        [time] []
    Amount to sample by. Default is 1.0 in current timeUnit

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

sm    : simulation      [boolean] []
    Using this flag instructs the command to preform a simulation instead of just evaluating each attribute separately over the range of time. The simulation flag is required to bake animation that that depends on the whole scene being evaluated at each time step such as dynamics. The default is true.

-----------------------------------------

sr    : smart           [[[, boolean, float, ]]] []
    Specify whether to enable smart bake and the optional smart bake tolerance.

-----------------------------------------

sac   : sparseAnimCurveBake [boolean] []
    When baking anim curves, do not insert any keys into areas of the curve where animation is defined. And, use as few keys as possible to bake the pre and post infinity behaviors. When this is false, one key will be inserted at each time step. The default is false.

-----------------------------------------

t     : time            [timerange]
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

    """

def blendTwoAttr(q=1,e=1,at="string",at0="name",at1="name",bl="name",cp=1,d="int",n="string",s=1,t="timerange"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/blendTwoAttr.html



-----------------------------------------

blendTwoAttr is undoable, queryable, and editable.

A blendTwoAttr nodes takes two inputs, and blends the values of the inputs
from one to the other, into an output value. The blending of the two inputs
uses a blending function, and the following formula:  

    
    
         (1 - blendFunction) * input[0]  +  blendFunction * input[1] 

The blendTwoAttr command can be used to blend the animation of an object to
transition smoothly between the animation of two other objects.

When the blendTwoAttr command is issued, it creates a blendTwoAttr node on the
specified attributes, and reconnects whatever was previously connected to the
attributes to the new blend nodes. You may also specify which two attributes
should be used to blend together.

The driver is used when you want to keyframe an object after it is being
animated by a blend node. The current driver index specifies which of the two
blended attributes should be keyframed.


-----------------------------------------


Return Value:

string[]  The names of the blendTwoAttr dependency nodes that were created.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    A list of attributes for the selected nodes for which a blendTwoAttr node will be created.  In query mode, this flag needs a value.

-----------------------------------------

at0   : attribute0      [name] ['query', 'edit']
    The attribute that should be connected to the first input of the new blendTwoAttr node. When queried, it returns a string.

-----------------------------------------

at1   : attribute1      [name] ['query', 'edit']
    The attribute that should be connected to the second input of the new blendTwoAttr node. When queried, it returns a string.

-----------------------------------------

bl    : blender         [name] ['query', 'edit']
    The blender attribute. This is the attribute that will be connected to the newly created blendTwoAttr node(s) blender attribute. This attribute controls how much of each of the two attributes to use in the blend. If this flag is not specified, a new animation curve is created whose value goes from 1 to 0 throughout the time range specified by the -t flag. If -t is not specified, an abrupt change from the value of the first to the value of the second attribute will occur at the current time when this command is issued.

-----------------------------------------

cp    : controlPoints   [boolean] []
    Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.

-----------------------------------------

d     : driver          [int] ['query', 'edit']
    The index of the driver attribute for this blend node (0 or 1) When queried, it returns an integer.

-----------------------------------------

n     : name            [string] ['query']
    name for the new blend node(s)

-----------------------------------------

s     : shape           [boolean] []
    Consider all attributes of shapes below transforms as well, except "controlPoints". Default: true

-----------------------------------------

t     : time            [timerange]
    The time range between which the blending between the 2 attributes should occur. If a single time is specified, then the blend will cause an abrupt change from the first to the second attribute at that time. If a range is specified, a smooth blending will occur over that time range. The default is to make a sudden transition at the current time.

    """

def bufferCurve(q=1,an="string",at="string",cp=1,ex=1,f="floatrange",hi="string",iub=1,index="uint",ov=1,s=1,sw=1,t="timerange",urc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bufferCurve.html



-----------------------------------------

bufferCurve is undoable, queryable, and NOT editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command helps manage buffer curve for animated objects


-----------------------------------------


Return Value:

int  Number of buffer curves    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

ex    : exists          [boolean] ['query']
    Returns true if a buffer curve currently exists on the specified attribute; false otherwise.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

ov    : overwrite       [boolean] []
    Create a buffer curve. "true" means create a buffer curve whether or not one already existed. "false" means if a buffer curve exists already then leave it alone. If no flag is specified, then the command defaults to -overwrite false

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

sw    : swap            [boolean] []
    For animated attributes which have buffer curves, swap the buffer curve with the current animation curve

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

urc   : useReferencedCurve [boolean]
    In create mode, sets the buffer curve to the referenced curve. Curves which are not from file references will ignore this flag. In query mode, returns true if the selected keys are displaying their referenced curve as the buffer curve, and false if they are not.

    """

def buildBookmarkMenu(ed="string",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/buildBookmarkMenu.html



-----------------------------------------

buildBookmarkMenu is undoable, NOT queryable, and NOT editable.

This command handles building the "dynamic" Bookmark menu, to show all
bookmarks ("sets") of a specified type ("sets -text")

menuName is the string returned by the "menu" command.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

ed    : editor          [string] []
    Name of the editor which this menu belongs to

-----------------------------------------

typ   : type            [string]
    Type of bookmark (sets -text) to display

    """

def buildKeyframeMenu():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/buildKeyframeMenu.html



-----------------------------------------

buildKeyframeMenu is undoable, NOT queryable, and NOT editable.

This command handles building the "dynamic" Keyframe menu, to show attributes
of currently selected objects, filtered by the current manipulator.

menuName is the string returned by the "menu" command. The target menu will
entries appended to it (and deleted from it) to always show what's currently
keyframable.


-----------------------------------------


Return Value:

None
    """

def cacheEvaluator(q=1,e=1,cfm="string",cfo="string",ci="timerange",cn="string",cps=1,cp=1,fc="string",fcr="[timerange, boolean]",fcs=1,fcw=1,lcn=1,lcd=1,lvn=1,na="string",nap="string",nf="string",nfp="string",nr="string",nrp="string",pi=1,pfs=1,rr=1,ru=1,ri=1,sf=1,sfm=1,sft=1,vn="string",wfc="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cacheEvaluator.html



-----------------------------------------

cacheEvaluator is NOT undoable, queryable, and editable.

This command controls caching configuration. It allows interaction with the
caching system.

Caching configuration is done through a set of rules. Most rules are composed
of a "filter", which is the test to be perform in order to determine if the
rule should be applied, and an "action", which is the effect that the rule
application should have on nodes that satisfy the criteria.

A caching mode is therefore a set of rules that determines which nodes are
being cached. This mode can be serialized to a JSON string using the
"creationParameters" flag in query mode.

## Built-in Cache Configuration Modes

A few cache configuration rules, filters and actions are provided in order to
support the built-in default caching modes.

### Built-in Filters

  * evaluationCacheNodes
    This filter matches all nodes for which the node type is in the default supported list for evaluation cache. See the code example below for the current list of supported types. 
  * nodeTypes
    This filter matches all nodes for which the node type is in the list provided with the newFilterParam flag. The parameter string is a list of comma-separated node types, prefixed with either '-' or '+'. The filter will go through the list in order and will stop if the node is of the given node type (or any derived node type). If the prefix is '-', the filter will return that the node did not match and stop processing. If the prefix is '+', the filter will return a match and stop processing. 
  * downstreamNodeTypes
    This filter matches all nodes for which the node type is in the list provided with the newFilterParam flag if they also have immediate downstream nodes of the right node type(s). The parameter string is in the form "type=+type1,+type2 downstreamTypes=+type3,+type3", where the list of node types uses the same semantic as the nodeTypes filter. 
  * vp2CacheNodes
    This filter matches all nodes for which the node type is in the list of node types supported by VP2 caching. Enabling VP2 caching for other node types will have no effect. See the comments in the code example below for the current list of supported types. 
  * vp2FallbackNodes
    This filter matches all nodes for which VP2 caching should revert to evaluation caching because of unsupported features. Namely, it matches nodes for which VP2 caching is enabled but which have animated visibility or animated topology (potentially changing number of vertices, edges, faces, etc.). It also matches nodes with static geometry, i.e. for which nothing needs to be cached in VP2 format for each frame. 

### Built-in Actions

  * enableEvaluationCache
    This action enables evaluation cache on the matched node. If the evaluation cache is already enabled, it has no effect. 
  * disableEvaluationCache
    This action disables evaluation cache on the matched node. If the evaluation cache is already disabled, it has no effect. 
  * disableAllCache
    This action disables all types of caching on the matched node. 
  * enableVP2Cache
    This action enables VP2 cache on the matched node. "useHardware=1" can be passed to the newActionParam in order to enable the VP2 hardware cache, while "useHardware=0" will use the VP2 software cache. This action disables the evaluation cache (to only keep VP2 cache) on the matched node to save memory. Specifying "useEvaluation=1" to turn on evaluation cache (along with VP2 cache). For example, NURBS surfaces keep the evaluation cache to make the selection highlighting more efficient. This action also automatically applies the fallback to evaluation cache rule for safety if required. This fallback will be applied if the node matches the criteria from the "vp2FallbackNodes" filter and will then apply the action from the "fallbackFromVP2CacheToEvaluationCache" action. "fallback=0" can be used to disable this fallback, but doing so can cause correctness issues,instabilities and even crashes. "useEvaluation=0" does not affect the fallback behavior. To use multiple parameters, separate them with ' ' like "useHardware=1 fallback=0 useEvaluation=1". 
  * disableVP2Cache
    This action disables the VP2 cache on the matched node. If the VP2 cache is already disabled, it has no effect. 
  * fallbackFromVP2CacheToEvaluationCache
    This action disables the VP2 cache on the matched node and enables the evaluation cache instead. 

### Built-in Rules

  * evaluationCache
    This rule has the same effect as using the evaluationCacheNodes filter with the enableEvaluationCache action. 
  * customEvaluators
    This rule ensures proper behavior for nodes claimed by a custom evaluator of a higher priority than the cache evaluator. First, it makes sure that caching is disabled for nodes claimed by a custom evaluator of a higher priority. Secondly, it makes sure input nodes to clusters belonging to a custom evaluator of a higher priority are marked as evaluation caching points if the evaluator needs data. This prevents pull evaluation from happening when the evaluator is evaluated. 

Note that any combination of cache configuration rules other than the default
modes is considered unsupported and to be used at one's own risk. The default
modes are "Evaluation cache", "VP2 software cache" and "VP2 hardware cache".
The sets of rules used to enable each mode are listed in the code examples.

## Querying Cache Configuration Values

In order to get a cache configuration value for a given node or list of nodes,
the cacheName flag can be used in query mode. Without any additional
parameters, this query is the same as if the valueName flag was set to
"active", i.e. it queries whether the given cache is active or not.

If the queried node is not a caching point, there will be no caching
configuration information associated with it and the query will return an
empty string (which is basically the same as all cache modes being inactive).
If the queried node is a caching point, the returned string will be the
requested information from the given cache. For example, querying the "active"
value can return "0" or "1".


-----------------------------------------


Return Value:

string  The state of whether the memory limit has been reached or not ('out',
'okay', 'low', or 'unlimited' with the 'resourceUsage' flag)    
boolean  The state of whether the safe mode is enabled (with the 'safeMode'
flag)  
boolean  The state of whether the safe mode was triggered (with the
'safeModeTriggered' flag)  
boolean  The state of whether prevent frame skipping is enabled (with the
'preventFrameSkip' flag)  
boolean  The state of whether cache in background was calculated (with the
'waitForCache' flag)  
string[]  The available cache names (with the 'listCacheNames' flag)  
string  The list of nodes currently cached by the cache evaluator (with the
'listCachedNodes' flag).  
string[]  The available value names (with the 'listValueNames' flag)  
string[]  The parameter value for the requested node(s) (with the 'cacheName'
flag)  
string  The creation parameters for the current mode as a JSON array (with the
'creationParameters' flag)  
string[]  The list of nodes marked as caching point (with the 'cachingPoints'
flag)  
string  The current cache fill mode (with the 'cacheFillMode' flag)  
string  The current cache fill order (with the 'cacheFillOrder' flag)  
string  The list of all the safe mode messages (with the 'safeModeMessages'
flag)  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cfm   : cacheFillMode   [string] ['query']
    Specifies the cache fill mode. Valid values are: "syncOnly" to fill cache during playback, "syncAsync" to cache during playback and in background, and "asyncOnly" to fill cache only in background. Query returns current mode.

-----------------------------------------

cfo   : cacheFillOrder  [string] ['query']
    Specifies in which order the cache fills the timeline. Valid values are: "forward" to fill cache in forward direction, "backward" to fill cache backwards, "bidirectional" to fill cache in forward and backward directions simultaneously, and "forwardFromBegin" to fill cache in forward direction from animation start. Query returns current cache fill mode.

-----------------------------------------

ci    : cacheInvalidate [timerange] []
    Specifies the frame range in which cache should be invalidated. The range should be specified as a pair of positive integers.  Usage examples:    * -ci "10:20"{Python equivalent: ('10','20')} means all frames in the range from 10 to 20, inclusive, in the current time unit.      Omitting one end of a range means using either end of the animation range (or both), as in the following examples:    * -ci "10:" means all frames from time 10 (in the current time unit) onwards to the maximum time in the animation range (on the timeline).    * -ci ":10" means all frames from the minimum time on the animation range (on the timeline) up to (and including) time 10 (in the current time unit).    * -ci ":" is a short form to specify all frames, from minimum to maximum time on the current animation range.

-----------------------------------------

cn    : cacheName       [string] ['query']
    Specifies the name of the cache from which to query a value.  In query mode, this flag needs a value.

-----------------------------------------

cps   : cachingPoints   [boolean] ['query']
    Get list of nodes marked as caching points, i.e. nodes with at least one type of cache active.

-----------------------------------------

cp    : creationParameters [boolean] ['query']
    Get the current mode creation parameters. The result is a JSON string which represents an array with an element for each rule. Each element is an association between the parameter name and its value when creating the rule.

-----------------------------------------

fc    : flushCache      [string] []
    Specifies to flush the current cache. Valid values are: "keep" to store the existing cache as backup, and "destroy" to delete the current cache.

-----------------------------------------

fcr   : flushCacheRange [[timerange, boolean]] []
    Specifies the frame range in which cache should be flushed. By default it will destroy the cache - if the 'flushCache' is also set then it will define what to do with the cache range being flushed. The range should be specified as a pair of positive integers and a boolean.  Usage examples:    * -flushCacheRange "10:20" on {Python equivalent: ('10','20',True)} means all frames in the range from 10 to 20, inclusive, in the current time unit.    * -flushCacheRange "12:18" off {Python equivalent: ('12','18',False)} means all frames before 12 and after 18, not inclusive, in the current time unit.      Omitting one end of a range means using either end of the animation range (or both), as in the following examples:    * -flushCacheRange "10:" on means all frames from time 10 (in the current time unit) onwards to the maximum time in the animation range (on the timeline).    * -flushCacheRange ":10" on means all frames from the minimum time on the animation range (on the timeline) up to (and including) time 10 (in the current time unit).    * -flushCacheRange ":" on is a short form to specify all frames, from minimum to maximum time on the current animation range.

-----------------------------------------

fcs   : flushCacheSync  [boolean] ['query']
    Specifies how to flush the cache: synchronously or asynchronously. True for synchronous, False for asynchronous.

-----------------------------------------

fcw   : flushCacheWait  [boolean] []
    Wait for the cache destruction to be completed.

-----------------------------------------

lcn   : listCacheNames  [boolean] ['query']
    Return the list of existing cache names.

-----------------------------------------

lcd   : listCachedNodes [boolean] ['query']
    Returns the list of cached nodes.

-----------------------------------------

lvn   : listValueNames  [boolean] ['query']
    Return the list of value names that can be queried for the given cache.

-----------------------------------------

na    : newAction       [string] []
    Specifies the name of the new action to create in the new filter/action rule.

-----------------------------------------

nap   : newActionParam  [string] []
    Specifies the parameter string to pass to the new action to create in the new filter/action rule.

-----------------------------------------

nf    : newFilter       [string] []
    Specifies the name of the new filter to create in the new filter/action rule.

-----------------------------------------

nfp   : newFilterParam  [string] []
    Specifies the parameter string to pass to the new filter to create in the new filter/action rule.

-----------------------------------------

nr    : newRule         [string] []
    Specifies the name of the new rule to create.

-----------------------------------------

nrp   : newRuleParam    [string] []
    Specifies the parameter string to pass to the new rule to create.

-----------------------------------------

pi    : pauseInvalidation [boolean] ['query']
    Pause all incoming invalidation of the cache. Work in symmetry with resumeInvalidation flag. PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation. If queried it will return how much time caching is paused, 0 means it is resumed.

-----------------------------------------

pfs   : preventFrameSkip [boolean] ['query']
    Specifies if frame skipping is enabled. Following behavior is seen when frame skipping is enabled, and playback is set to play in real-time.    * If cache can't be filled at real-time frame rate, frames will NOT be skipped.   * Once all frames have been looped over(and therefore all frames are cached), and if playing back from cache still can't be done at real-time frame rate; frames WILL be skipped.   * If memory limit is reached before all frames are cached, frames WILL be skipped.   * If cache is invalidated will playing(like flushing it), frames will NOT be skipped(until the cache is full again).

-----------------------------------------

rr    : resetRules      [boolean] []
    Reset the cache configuration rules to an empty set of rules.

-----------------------------------------

ru    : resourceUsage   [boolean] ['query']
    Returns the current state of the resource usage as a string. 'unlimited' = the resource limits are being ignored, 'out' = the memory limit has been reached, 'low' = the memory usage is at 90% of the specified limit, 'okay' = memory usage is under 90% of the specified limit.

-----------------------------------------

ri    : resumeInvalidation [boolean] ['query']
    Resume all incoming invalidation of the cache. Work in symmetry with pauseInvalidation flag. PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation. If queried it will return true if cache is resumed, false otherwise.

-----------------------------------------

sf    : safeMode        [boolean] ['query']
    Turns safe mode on or off. In query mode, it returns the status of the safe mode for cache evaluator.

-----------------------------------------

sfm   : safeModeMessages [boolean] ['query']
    Prints the safe mode messages to the console.

-----------------------------------------

sft   : safeModeTriggered [boolean] ['query']
    Returns if the safe mode was triggered for cache evaluator.

-----------------------------------------

vn    : valueName       [string] ['query']
    Specifies the name of the parameter for which to query the value.  In query mode, this flag needs a value.

-----------------------------------------

wfc   : waitForCache    [float]
    Specifies to wait for cache to fill in background, with [Time to wait in seconds] timeout.

    """

def character(q=1,e=1,add="name",aoo="string",cp=1,cl="name",em=1,ed=1,er=1,es=1,et=1,ev=1,fl="name",fe="name",include="name",int="name",ii="name",im="name",lib=1,mi="uint",n="string",nw=1,no=1,ofs=1,rm="name",roo="string",rt="string",sc=1,sp="name",sub="name",t="string",un="name",ua="name"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/character.html



-----------------------------------------

character is undoable, queryable, and editable.

This command is used to manage the membership of a character. Characters are a
type of set that gathers together the attributes of a node or nodes that a
user wishes to animate as a single entity.


-----------------------------------------


Return Value:

string  For creation operations (name of the character that was created or
edited)    
string[]  For query operation (names of items in the character)  
boolean  For isMember operation  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addElement      [name] ['edit']
    Adds the list of items to the given character. If some of the items cannot be added to the character because they are in another character, the command will fail. When another character is passed to to -addElement, is is added as a sub character. When a node is passed in, it is expanded into its keyable attributes, which are then added to the character.

-----------------------------------------

aoo   : addOffsetObject [string] ['query', 'edit']
    Indicates that the selected character member objects should be used when calculating and applying offsets. The flag argument is used to specify the character.

-----------------------------------------

cp    : characterPlug   [boolean] ['query']
    Returns the plug on the character that corresponds to the specified character member.

-----------------------------------------

cl    : clear           [name] ['edit']
    An operation which removes all items from the given character.

-----------------------------------------

em    : empty           [boolean] []
    Indicates that the character to be created should be empty. (i.e. it ignores any arguments identifying objects to be added to the character.

-----------------------------------------

ed    : excludeDynamic  [boolean] []
    When creating the character, exclude dynamic attributes.

-----------------------------------------

er    : excludeRotate   [boolean] []
    When creating the character, exclude rotate attributes from transform- type nodes.

-----------------------------------------

es    : excludeScale    [boolean] []
    When creating the character, exclude scale attributes from transform- type nodes.

-----------------------------------------

et    : excludeTranslate [boolean] []
    When creating the character, exclude translate attributes from transform-type nodes. For example, if your character contains joints only, perhaps you only want to include rotations in the character.

-----------------------------------------

ev    : excludeVisibility [boolean] []
    When creating the character, exclude visibility attribute from transform-type nodes.

-----------------------------------------

fl    : flatten         [name] ['edit']
    An operation that flattens the structure of the given character. That is, any characters contained by the given character will be replaced by its members so that the character no longer contains other characters but contains the other characters' members.

-----------------------------------------

fe    : forceElement    [name] ['edit']
    For use in edit mode only. Forces addition of the items to the character. If the items are in another character which is in the character partition, the items will be removed from the other character in order to keep the characters in the character partition mutually exclusive with respect to membership.

-----------------------------------------

include : include         [name] ['edit']
    Adds the list of items to the given character. If some of the items cannot be added to the character, a warning will be issued. This is a less strict version of the -add/addElement operation.

-----------------------------------------

int   : intersection    [name] ['query']
    An operation that returns a list of items which are members of all the character in the list. In general, characters should be mutually exclusive.

-----------------------------------------

ii    : isIntersecting  [name] ['query']
    An operation which tests whether or not the characters in the list have common members. In general, characters should be mutually exclusive, so this should always return false.

-----------------------------------------

im    : isMember        [name] ['query']
    An operation which tests whether or not all the given items are members of the given character.

-----------------------------------------

lib   : library         [boolean] ['query']
    Returns the clip library associated with this character, if there is one. A clip library will only exist if you have created clips on your character.

-----------------------------------------

mi    : memberIndex     [uint] ['query']
    Returns the memberIndex of the specified character member if used after the query flag. Or if used before the query flag, returns the member that corresponds to the specified index.

-----------------------------------------

n     : name            [string] []
    Assigns string as the name for a new character. Valid for operations that create a new character.

-----------------------------------------

nw    : noWarnings      [boolean] []
    Indicates that warning messages should not be reported such as when trying to add an invalid item to a character. (used by UI)

-----------------------------------------

no    : nodesOnly       [boolean] ['query']
    This flag modifies the results of character membership queries. When listing the attributes (e.g. sphere1.tx) contained in the character, list only the nodes. Each node will only be listed once, even if more than one attribute or component of the node exists in the character.

-----------------------------------------

ofs   : offsetNode      [boolean] ['query']
    Returns the name of the characterOffset node used to add offsets to the root of the character.

-----------------------------------------

rm    : remove          [name] ['edit']
    Removes the list of items from the given character.

-----------------------------------------

roo   : removeOffsetObject [string] ['edit']
    Indicates that the selected character offset objects should be removed as offsets. The flag argument is used to specify the character.

-----------------------------------------

rt    : root            [string] []
    Specifies the transform node which will act as the root of the character being created. This creates a characterOffset node in addition to the character node, which can be used to add offsets to the character to change the direction of the character's animtion without inserting additional nodes in its hierarchy.

-----------------------------------------

sc    : scheduler       [boolean] ['query']
    Returns the scheduler associated with this character, if there is one. A scheduler will only exist if you have created clips on your character.

-----------------------------------------

sp    : split           [name] []
    Produces a new set with the list of items and removes each item in the list of items from the given set.

-----------------------------------------

sub   : subtract        [name] ['query']
    An operation between two characters which returns the members of the first character that are not in the second character. In general, characters should be mutually exclusive.

-----------------------------------------

t     : text            [string] ['query', 'edit']
    Defines an annotation string to be stored with the character.

-----------------------------------------

un    : union           [name] ['query']
    An operation that returns a list of all the members of all characters listed.

-----------------------------------------

ua    : userAlias       [name]
    Returns the user defined alias for the given attribute on the character or and empty string if there is not one. Characters automatically alias the attributes where character animation data is stored. A user alias will exist when the automatic aliases are overridden using the aliasAttr command.

    """

def characterMap(q=1,e=1,ma="[string, string]",mm="string",mn="[string, string]",m="string",pm=1,ua="[string, string]",umn="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/characterMap.html



-----------------------------------------

characterMap is undoable, queryable, and editable.

This command is used to create a correlation between the attributes of 2 or
more characters.


-----------------------------------------


Return Value:

string  characterMap name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ma    : mapAttr         [[string, string]] ['query', 'edit']
    In query mode, this flag can be used to query the mapping stored by the specified map node. It returns an array of strings. In non-query mode, this flag can be used to create a mapping between the specified character members. Any previous mapping on the attributes is removed in favor of the newly specified mapping.

-----------------------------------------

mm    : mapMethod       [string] []
    This is is valid in create mode only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", and "byAttrOrder". "byAttrOrder" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence.

-----------------------------------------

mn    : mapNode         [[string, string]] ['query']
    This flag can be used to map all the attributes on the source node to their matching attributes on the destination node.

-----------------------------------------

m     : mapping         [string] ['query']
    This flag is valid in query mode only. It must be used before the query flag with a string argument. It is used for querying the mapping for a particular attribute. A string array is returned.

-----------------------------------------

pm    : proposedMapping [boolean] ['query']
    This flag is valid in query mode only. It is used to get an array of the mapping that the character map would prvide if called with the specified characters and the (optional) specified mappingMethod. If a character map exists on the characters, the map is not affected by the query operation. A string array is returned.

-----------------------------------------

ua    : unmapAttr       [[string, string]] ['edit']
    This flag can be used to unmap the mapping stored by the specified map node.

-----------------------------------------

umn   : unmapNode       [[string, string]]
    This flag can be used to unmap all the attributes on the source node to their matching attributes on the destination node. Note that mapped attributes which do not have matching names, will not be unmapped.

    """

def choice(q=1,e=1,at="string",cp=1,index="uint",n="string",sl="name",s=1,sa="name",t="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/choice.html



-----------------------------------------

choice is undoable, queryable, and editable.

The choice command provides a mechanism for changing the inputs to an
attribute based on some (usually time-based) criteria. For example, an object
could be animated from frames 1 to 30 by a motion path, then from frames 30 to
50 it follows keyframe animation, and after frame 50 it returns to the motion
path. Or, a revolve surface could change its input curve depending on some
transform's rotation value.

The choice command creates a choice node (if one does not already exist) on
all specified attributes of the selected objects. If the attribute was already
connected to something, that something is now reconnected to the i'th index of
the choice node's input (or the next available input if the -in/index flag is
not specified). If a source attribute is specified, then that attribute is
connected to the choice node's i'th input instead.

The choice node operates by using the value of its selector attribute to
determine which of its input attributes to pass through to its output. The
input attributes can be of any type. For example, if the selector attribute
was connected by an animation curve with keyframes at (1,1), (30,2) and
(50,1), then that would mean that the choice node would pass on the data from
input[1] from time 1 to 30, and after time 50, and the data from input[2]
between times 30 and 50.

This command returns the names of the created or modified choice nodes, and if
a keyframe was added to the animation curve, it specifies the index (or value
on the animation curve).


-----------------------------------------


Return Value:

string[]  The newly created and/or modified choice nodes, with the attribute
for which a selector keyframe was created.  
For example: choice1.input[3] choice2.input[3]    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    specifies the attributes onto which choice node(s) should be created. The default is all keyable attributes of the given objects. Note that although this flag is not queryable, it can be used to qualify which attributes of the given objects to query.  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.

-----------------------------------------

index : index           [uint] ['query']
    specifies the multi-input index of the choice node to connect the source attribute to. When queried, returns a list of integers one per specified -t/time that indicates the multi-index of the choice node to use at that time.

-----------------------------------------

n     : name            [string] ['query']
    the name to give to any newly created choice node(s). When queried, returns a list of strings.

-----------------------------------------

sl    : selector        [name] ['query']
    specifies the attribute to be used as the choice node's selector. The value of the selector at a given time determines which of the choice node's multi-indices should be used as the output of the choice node at that time. This flag is only editable (it cannot be specified at creation time). When queried, returns a list of strings.

-----------------------------------------

s     : shape           [boolean] []
    Consider all attributes of shapes below transforms as well, except "controlPoints". Default: true

-----------------------------------------

sa    : sourceAttribute [name] []
    specifies the attribute to connect to the choice node that will be selected at the given time(s) specified by -t/time.

-----------------------------------------

t     : time            [time]
    specifies the time at which the choice should use the given source attribute, or the currently connected attribute if source attribute is not specified. The default is the curren time. Note that although this flag is not queryable, it can be used to qualify the times at which to query the other attributes.  In query mode, this flag needs a value.

    """

def clip(q=1,e=1,abs=1,abr=1,a="string",at=1,aa=1,ac=1,ar=1,asc=1,acr=1,ch=1,cn=1,c=1,da=1,d=1,end="time",ex=1,ignoreSubcharacters=1,i=1,lo=1,mm="string",n="string",nn="string",p=1,pi=1,rm=1,rt=1,rof="[float, float, float]",ra=1,sc=1,scn=1,sp="time",s="time",tof="[float, float, float]",uc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/clip.html



-----------------------------------------

clip is undoable, queryable, and editable.

This command is used to create, edit and query character clips.


-----------------------------------------


Return Value:

string[]  clip names    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

abs   : absolute        [boolean] []
    This flag is now deprecated. Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead. This flag controls whether the clip follows its keyframe values or whether they are offset by a value to maintain a smooth path. Default is true.

-----------------------------------------

abr   : absoluteRotations [boolean] []
    This flag is now deprecated. Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead. If true, this overrides the -absolute flag so that rotation channels are always calculated with absolute offsets. This allows you to have absolute offsets on rotations and relative offsets on all other channels.

-----------------------------------------

a     : active          [string] ['query', 'edit']
    Query or edit the active clip. This flag is not valid in create mode. Making a clip active causes its animCurves to be hooked directly to the character attributes in addition to being attached to the clip library node. This makes it easier to access the animCurves if you want to edit, delete or add additional animCruves to the clip.

-----------------------------------------

at    : addTrack        [boolean] []
    This flag is now obsolete. Use the insertTrack flag on the clipSchedule command instead.

-----------------------------------------

aa    : allAbsolute     [boolean] []
    Set all channels to be calculated with absolute offsets. This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.

-----------------------------------------

ac    : allClips        [boolean] ['query']
    This flag is used to query all the clips in the scene. Nodes of type "animClip" that are storing poses, are not returned by this command.

-----------------------------------------

ar    : allRelative     [boolean] []
    Set all channels to be calculated with relative offsets. This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.

-----------------------------------------

asc   : allSourceClips  [boolean] ['query']
    This flag is used to query all the source clips in the scene. Nodes of type "animClip" that are storing poses or clip instances, are not returned by this command.

-----------------------------------------

acr   : animCurveRange  [boolean] []
    This flag can be used at the time you create the clip instead of the startTime and endTime flags. It specifies that you want the range of the clip to span the range of keys in the clips associated animCurves.

-----------------------------------------

ch    : character       [boolean] ['query']
    This is a query only flag which operates on the specified clip. It returns the names of any characters that a clip is associated with.

-----------------------------------------

cn    : constraint      [boolean] []
    This creates a clip out of any constraints on the character. The constraint will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.

-----------------------------------------

c     : copy            [boolean] ['query']
    This flag is used to copy a clip or clips to the clipboard. It should be used in conjunction with the name flag to copy the named clips on the specified character and its subcharacters. In query mode, this flag allows you to query what, if anything, has been copied into the clip clipboard.

-----------------------------------------

da    : defaultAbsolute [boolean] []
    Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified. This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.

-----------------------------------------

d     : duplicate       [boolean] ['query']
    Duplicate the clip specified by the name flag. The start time of the new clip should be specified with the startTime flag.

-----------------------------------------

end   : endTime         [time] ['query', 'edit']
    Specify the clip end

-----------------------------------------

ex    : expression      [boolean] []
    This creates a clip out of any expressions on the character. The expression will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.

-----------------------------------------

ignoreSubcharacters : ignoreSubcharacters [boolean] []
    During clip creation, duplication and isolation, subcharacters are included by default. If you want to create a clip on the top level character only, or you want to duplicate the clip on the top level character without including subCharacters, use the ignoreSubcharacters flag.

-----------------------------------------

i     : isolate         [boolean] []
    This flag should be used in conjunction with the name flag to specify that a clip or clips should be copied to a new clip library. The most common use of this flag is for export, when you want to only export certain clips from the character, without exporting all of the clips.

-----------------------------------------

lo    : leaveOriginal   [boolean] []
    This flag is used when creating a clip to specify that the animation curves should be copied to the clip library, and left on the character.

-----------------------------------------

mm    : mapMethod       [string] []
    This is is valid with the paste and pasteInstance flags only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", "byCharacterMap", "byAttrOrder", "byMapOrAttrName" and "byMapOrNodeName". "byAttrName" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence, "byCharacterMap" uses the existing characterMap node to do the mapping. "byMapOrAttrName" uses a character map if one exists, otherwise uses the attribute name. "byMapOrNodeName" uses a character map if one exists, otherwise uses the attribute name.

-----------------------------------------

n     : name            [string] ['query']
    In create mode, specify the clip name. In query mode, return a list of all the clips. In duplicate mode, specify the clip to be duplicated. In copy mode, specify the clip to be copied. This flag is multi-use, but multiple use is only supported with the copy flag. For use during create and with all other flags, only the first instance of the name flag will be utilized.  In query mode, this flag can accept a value.

-----------------------------------------

nn    : newName         [string] []
    Rename a clip. Must be used in conjunction with the clip name flag, which is used to specify the clip to be renamed.

-----------------------------------------

p     : paste           [boolean] []
    This flag is used to paste a clip or clips from the clipboard to a character. Clips are added to the clipboard using the c/copy flag.

-----------------------------------------

pi    : pasteInstance   [boolean] []
    This flag is used to paste an instance of a clip or clips from the clipboard to a character. Unlike the p/paste flag, which duplicates the animCurves from the original source clip, the pi/pasteInstance flag shares the animCurves from the source clip.

-----------------------------------------

rm    : remove          [boolean] ['query']
    Remove the clip specified by the name flag. The clip will be permanently removed from the library and deleted from any times where it has been scheduled.

-----------------------------------------

rt    : removeTrack     [boolean] []
    This flag is now obsolete. Use removeTrack flag on the clipSchedule command instead.

-----------------------------------------

rof   : rotationOffset  [[float, float, float]] ['query']
    Return the channel offsets used to modify the clip's rotation.

-----------------------------------------

ra    : rotationsAbsolute [boolean] []
    Set all channels except rotations to be calculated with relative offsets. Rotation channels will be calculated with absolute offsets. This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.

-----------------------------------------

sc    : scheduleClip    [boolean] []
    This flag is used when creating a clip to specify whether or not the clip should immediately be scheduled at the current time. If the clip is not scheduled, the clip will be placed in the library for future use, but will not be placed on the timeline. This flag is for use only when creating a new clip or duplicating an existing. The default is true.

-----------------------------------------

scn   : sourceClipName  [boolean] ['query']
    This flag is for query only. It returns the name of the source clip that controls an instanced clip.

-----------------------------------------

sp    : split           [time] ['edit']
    Split an existing clip into two clips. The split occurs around the specified time.

-----------------------------------------

s     : startTime       [time] ['query', 'edit']
    Specify the clip start

-----------------------------------------

tof   : translationOffset [[float, float, float]] ['query']
    Return the channel offsets used to modify the clip's translation.

-----------------------------------------

uc    : useChannel      [string]
    Specify which channels should be acted on. This flag is valid only in conjunction with clip creation, and the isolate flag. The specified channels must be members of the character.

    """

def clipEditor(q=1,e=1,th="int",af="string",aft="string",cd="string",cs="int",ctl=1,dt="string",dc="string",da=1,dat="string",dak="string",di="string",dk="string",dtn="string",dv="string",dtg="string",ex=1,f="string",fmc="string",fa=1,fr="[float, float]",hlc="string",hb="[string, string]",hc="[string, string]",it=1,lac=1,lc=1,lck=1,la="string",mlc="string",ms=1,mc="string",pnl="string",p="string",sb="[string, string, string]",sc="[string, string]",slc="string",st="string",sv="string",sts=1,up=1,ulk=1,upd=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/clipEditor.html



-----------------------------------------

clipEditor is undoable, queryable, and editable.

Create a clip editor with the given name.


-----------------------------------------


Return Value:

string  Editor name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

th    : allTrackHeights [int] []
    OBSOLETE flag. Use clipStyle instead.

-----------------------------------------

af    : autoFit         [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view.

-----------------------------------------

aft   : autoFitTime     [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view along the time axis, as well.

-----------------------------------------

cd    : clipDropCmd     [string] ['edit']
    Command executed when clip node is dropped on the TraX editor

-----------------------------------------

cs    : clipStyle       [int] ['query', 'edit']
    Set/return the clip track style in the specified editor. Default is 2. Valid values are 1-3.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dc    : deleteCmd       [string] ['edit']
    Command executed when backspace key is pressed

-----------------------------------------

da    : deselectAll     [boolean] ['edit']
    Deselect all clips and blends in the editor.

-----------------------------------------

dat   : displayActiveKeyTangents [string] ['edit']
    on | off | tgl Display active key tangents in the editor.

-----------------------------------------

dak   : displayActiveKeys [string] ['edit']
    on | off | tgl Display active keys in the editor.

-----------------------------------------

di    : displayInfinities [string] ['edit']
    on | off | tgl Display infinities in the editor.

-----------------------------------------

dk    : displayKeys     [string] ['edit']
    on | off | tgl Display keyframes in the editor.

-----------------------------------------

dtn   : displayTangents [string] ['edit']
    on | off | tgl Display tangents in the editor.

-----------------------------------------

dv    : displayValues   [string] ['edit']
    on | off | tgl Display active keys and tangents values in the editor.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

fa    : frameAll        [boolean] ['edit']
    Frame view around all clips in the editor.

-----------------------------------------

fr    : frameRange      [[float, float]] ['query', 'edit']
    The editor's current frame range.

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

hb    : highlightedBlend [[string, string]] ['query']
    Returns the highlighted blend, listed as scheduler and index

-----------------------------------------

hc    : highlightedClip [[string, string]] ['query']
    Returns the highlighted clip, listed as scheduler and index

-----------------------------------------

it    : initialized     [boolean] ['query']
    Returns whether the clip editor is fully initialized, and has a port to draw through. If not, the -frameRange and -frameAll flags will fail.

-----------------------------------------

lac   : listAllCharacters [boolean] ['edit']
    List all characters in the editor and outliner.

-----------------------------------------

lc    : listCurrentCharacters [boolean] ['edit']
    List only the characters in the editor and outliner.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

la    : lookAt          [string] ['edit']
    all | selected | currentTime FitView helpers.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

ms    : manageSequencer [boolean] ['query', 'edit']
    Sets/returns whether the clip editor should manage sequencer nodes. If so, animation clips and characters are not represented.

-----------------------------------------

mc    : menuContext     [string] ['query']
    Returns a string array denoting the type of data object the cursor is over. Returned values are: {"timeSlider"} {"nothing"} {"track", "track index", "character node name", "group name"} {"clip", "clip node name"}

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

sb    : selectBlend     [[string, string, string]] ['query', 'edit']
    Select the blends specified by the scheduler name and the indicies of the two clips used in the blend. When queried, a string containing the scheduler name and the two clip indicies for all of the selected blends is returned.

-----------------------------------------

sc    : selectClip      [[string, string]] ['query', 'edit']
    Selects the clip specified by the scheduler name and the clip index. When queried, a string containing the scheduler and clip index of all of the selected clips is returned.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

st    : snapTime        [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in time.

-----------------------------------------

sv    : snapValue       [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in values.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def clipMatching(cd="[string, float]",cs="[string, float]",mr="uint",mt="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/clipMatching.html



-----------------------------------------

clipMatching is undoable, NOT queryable, and NOT editable.

This command is used to compute an offset to apply on a source clip in order
to automatically align it to a destination clip at a specified match element.
For this command to work, offset objects must be specified for the character.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cd    : clipDst         [[string, float]] []
    The clip to match so that the source clip can be offsetted correctly. This flag takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order to have the source clip match at a certain time in the destination clip.

-----------------------------------------

cs    : clipSrc         [[string, float]] []
    The clip to offset so that it aligns with the destination clip. This flag takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order to have it match at a certain time in the clip.

-----------------------------------------

mr    : matchRotation   [uint] []
    This flag sets the rotation match type. By default, it is set to not match the rotation. 0 - None 1 - Match full rotation 2 - Match projected rotation on ground plane

-----------------------------------------

mt    : matchTranslation [uint]
    This flag sets the translation match type. By default, it is set to not match the translation. 0 - None 1 - Match full translation 2 - Match projected translation on ground plane

    """

def clipSchedule(q=1,e=1,aa=1,ar=1,b="[uint, uint]",bn="[uint, uint]",bun="string",ch=1,ci="uint",c="float",da=1,en=1,grp=1,gri="uint",gn="string",ph="time",it="uint",instance="string",lc=1,lp=1,l=1,m=1,n="string",poc="float",prc="float",rm=1,rb="[uint, uint]",ret=1,rt="uint",ra=1,sc="float",sh="int",shi="uint",so=1,scn=1,se="time",ss="time",s="time",t="uint",w="float",ws="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/clipSchedule.html



-----------------------------------------

clipSchedule is undoable, queryable, and editable.

This command is used to create, edit and query clips and blends in the Trax
editor. It operates on the clipScheduler node attached to the character. In
query mode, if no flags are specified, returns an array of strings in this
form:
(clipName,clipIndex,clipStart,clipSourceStart,clipSourceEnd,clipScale,clipPreCycle,clipPostCycle,clipHold)


-----------------------------------------


Return Value:

string  Clip name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aa    : allAbsolute     [boolean] ['query', 'edit']
    Set all channels to be calculated with absolute offsets. This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.

-----------------------------------------

ar    : allRelative     [boolean] ['query', 'edit']
    Set all channels to be calculated with relative offsets. This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.

-----------------------------------------

b     : blend           [[uint, uint]] ['query']
    This flag is used to blend two clips, whose indices are provided as flag arguments.

-----------------------------------------

bn    : blendNode       [[uint, uint]] ['query']
    This query only flag list all of the blend nodes associated with the blend defined by the two clip indices. This flag returns a string array.  In query mode, this flag can accept a value.

-----------------------------------------

bun   : blendUsingNode  [string] []
    This flag is used to blend using an existing blend node. It is used in conjunction with the blend flag. The blend flag specifies the clip indices for the blend. The name of an existing animBlend node should be supplied supplied as an argument for the blendUsingNode flag.

-----------------------------------------

ch    : character       [boolean] ['query']
    This flag is used to query which characters this scheduler controls. It returns an array of strings.

-----------------------------------------

ci    : clipIndex       [uint] ['query']
    Specify the index of the clip to schedule. In query mode, returns an array of strings in this form: (clipName,index,start,sourceStart,sourceEnd,scale,preCycle,postCycle)  In query mode, this flag can accept a value.

-----------------------------------------

c     : cycle           [float] ['query']
    This flag is now obsolete. Use the postCycle flag instead.

-----------------------------------------

da    : defaultAbsolute [boolean] ['query', 'edit']
    Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified. This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.

-----------------------------------------

en    : enable          [boolean] ['query']
    This flag is used to enable or disable a clip. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be enabled or disabled.

-----------------------------------------

grp   : group           [boolean] []
    This flag is used to add (true) or remove (false) a list of clips (specified with groupIndex) into a group.

-----------------------------------------

gri   : groupIndex      [uint] []
    This flag specifies a multiple number of clips to be added or removed from a group.

-----------------------------------------

gn    : groupName       [string] ['query']
    This flag is used to specify the group that should be added to. If no group by that name exists and new group is created with that name. By default if this is not specified a new group will be created.

-----------------------------------------

ph    : hold            [time] ['query']
    Specify how long to hold the last value of the clip after its normal or cycled end.

-----------------------------------------

it    : insertTrack     [uint] []
    This flag is used to insert a new empty track at the track index specified.

-----------------------------------------

instance : instance        [string] []
    Create an instanced copy of the named clip. An instanced clip is one that is linked to an original clip. Thus, changes to the animation curve of the original curve will also modify all instanced clips. The name of the instanced clip is returned as a string.

-----------------------------------------

lc    : listCurves      [boolean] ['query']
    This flag is used to list the animation curves associated with a clip. It should be used in conjunction with the clipIndex flag, which specifies the clip of interest.

-----------------------------------------

lp    : listPairs       [boolean] ['query']
    This query only flag returns a string array containing the channels in a character that are used by a clip and the names of the animation curves that drive the channels. Each string in the string array consists of the name of a channel, a space, and the name of the animation curve animating that channel. This flag must be used with the ci/clipIndex flag.

-----------------------------------------

l     : lock            [boolean] ['query', 'edit']
    This flag specifies whether clips on a track are to be locked or not. Must be used in conjuction with the track flag.

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    This flag specifies whether clips on a track are to be muted or not. Must be used in conjuction with the track flag.

-----------------------------------------

n     : name            [string] ['query']
    This flag is used to query the name of the clip node associated with the specified clip index, or to specify the name of the instanced clip during instancing.  In query mode, this flag can accept a value.

-----------------------------------------

poc   : postCycle       [float] ['query']
    Specify the number of times to repeat the clip after its normal end.

-----------------------------------------

prc   : preCycle        [float] ['query']
    Specify the number of times to repeat the clip before its normal start.

-----------------------------------------

rm    : remove          [boolean] []
    This flag is used to remove a clip from the timeline. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be removed from the timeline, but will still exist in the library and any instanced clips will remain in the timeline. To permanently remove a clip from the scene, the clip command should be used instead.

-----------------------------------------

rb    : removeBlend     [[uint, uint]] []
    This flag is used to remove an existing blend between two clips, whose indices are provided as flag arguments.

-----------------------------------------

ret   : removeEmptyTracks [boolean] []
    This flag is used to remove all tracks that have no clips.

-----------------------------------------

rt    : removeTrack     [uint] []
    This flag is used to remove the track with the specified index. The track must have no clips on it before it can be removed.

-----------------------------------------

ra    : rotationsAbsolute [boolean] ['query', 'edit']
    Set all channels except rotations to be calculated with relative offsets. Rotation channels will be calculated with absolute offsets. This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.

-----------------------------------------

sc    : scale           [float] ['query']
    Specify the amount to scale the clip. Values must be greater than 0.

-----------------------------------------

sh    : shift           [int] []
    This flag allows multiple clips to be shifted by a certain number of tracks and works in conjunction with the shiftIndex flag. The flag specifies the number of tracks to shift the associated clips. Positive values shift the clips down an negative values shift the clips up.

-----------------------------------------

shi   : shiftIndex      [uint] []
    This flag allows multiple clips to be shifted by a certain number of tracks and works in conjunction with the shiftAmount flag. The flag specifies the index of the clip to shift. This flag can be used multiple times on the command line to specify a number of clips to shift.

-----------------------------------------

so    : solo            [boolean] ['query', 'edit']
    This flag specifies whether clips on a track are to be soloed or not. Must be used in conjuction with the track flag.

-----------------------------------------

scn   : sourceClipName  [boolean] ['query']
    This flag is used to query the name of the source clip node associated with the specified clip index.

-----------------------------------------

se    : sourceEnd       [time] ['query']
    Specify where to end in the source clip's animation curves

-----------------------------------------

ss    : sourceStart     [time] ['query']
    Specify where to start in the source clip's animation curves

-----------------------------------------

s     : start           [time] ['query']
    Specify the placement of the start of the clip

-----------------------------------------

t     : track           [uint] ['query']
    Specify the track to operate on. For example, which track to place a clip on, which track to mute/lock/solo. In query mode, it may be used in conjuction with the clipIndex flag to return the track number of a clip, where track 1 is the first track of the character.  In query mode, this flag can accept a value.

-----------------------------------------

w     : weight          [float] ['query']
    This flag is used in to set or query the weight of the clip associated with the specified clip index.

-----------------------------------------

ws    : weightStyle     [uint]
    This flag is used to set or query the weightStyle attribute of the clip associated with the specified clip index.

    """

def clipSchedulerOutliner(q=1,e=1,ann="string",bgc="[float, float, float]",cs="string",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,npm=1,p="string",pma=1,po=1,sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/clipSchedulerOutliner.html



-----------------------------------------

clipSchedulerOutliner is undoable, queryable, and editable.

This command creates/edits/queries a clip scheduler outliner control.


-----------------------------------------


Return Value:

string  The name of the outliner control.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ann   : annotation      [string] ['query', 'edit']
    Annotate the control with an extra string value.

-----------------------------------------

bgc   : backgroundColor [[float, float, float]] ['query', 'edit']
    The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.   When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.

-----------------------------------------

cs    : clipScheduler   [string] ['edit']
    Name of the clip scheduler for which to display information.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Add a documentation flag to the control. The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)

-----------------------------------------

dgc   : dragCallback    [script] ['edit']
    Adds a callback that is called when the middle mouse button is pressed. The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type. Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback. The recommended way is to pass a Python function object as the argument. In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed. In that case, the string will have the values substituted into it via the standard Python format operator. The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers". The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

-----------------------------------------

dpc   : dropCallback    [script] ['edit']
    Adds a callback that is called when a drag and drop operation is released above the drop site. The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback. The recommended way is to pass a Python function object as the argument. In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed. In that case, the string will have the values substituted into it via the standard Python format operator. The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type". The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

-----------------------------------------

en    : enable          [boolean] ['query', 'edit']
    The enable state of the control. By default, this flag is set to true and the control is enabled. Specify false and the control will appear dimmed or greyed-out indicating it is disabled.

-----------------------------------------

ebg   : enableBackground [boolean] ['query', 'edit']
    Enables the background color of the control.

-----------------------------------------

ekf   : enableKeyboardFocus [boolean] ['query', 'edit']
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard. If not, the user can only use the mouse. This flag would typically be used to turn off keyboard focus support from controls that get it by default, like Edit and List controls

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

fpn   : fullPathName    [boolean] ['query']
    Return the full path name of the widget, which includes all the parents.

-----------------------------------------

h     : height          [int] ['query', 'edit']
    The height of the control. The control will attempt to be this size if it is not overruled by parent layout conditions.

-----------------------------------------

hlc   : highlightColor  [[float, float, float]] ['query', 'edit']
    The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.

-----------------------------------------

io    : isObscured      [boolean] ['query']
    Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.

-----------------------------------------

m     : manage          [boolean] ['query', 'edit']
    Manage state of the control. An unmanaged control is not visible, nor does it take up any screen real estate. All controls are created managed by default.

-----------------------------------------

nbg   : noBackground    [boolean] ['edit']
    Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn. The state of this flag is inherited by children of this control.

-----------------------------------------

npm   : numberOfPopupMenus [boolean] ['query']
    Return the number of popup menus attached to this control.

-----------------------------------------

p     : parent          [string] ['query']
    The parent layout for this control.

-----------------------------------------

pma   : popupMenuArray  [boolean] ['query']
    Return the names of all the popup menus attached to this control.

-----------------------------------------

po    : preventOverride [boolean] ['query', 'edit']
    If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.

-----------------------------------------

sbm   : statusBarMessage [string] ['edit']
    Extra string to display in the status bar when the mouse is over the control.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

vis   : visible         [boolean] ['query', 'edit']
    The visible state of the control. A control is created visible by default. Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).

-----------------------------------------

vcc   : visibleChangeCommand [script] ['query', 'edit']
    Command that gets executed when visible state of the control changes.

-----------------------------------------

w     : width           [int]
    The width of the control. The control will attempt to be this size if it is not overruled by parent layout conditions.

    """

def controller(q=1,e=1,ac=1,cld=1,g=1,idx="int",ic="string",p=1,pwd=1,pwl=1,pwr=1,pwu=1,unp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/controller.html



-----------------------------------------

controller is undoable, queryable, and editable.

Commands for managing animation sources


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : allControllers  [boolean] ['query', 'edit']
    When this flag is queried, returns all dependNode attached to a controller in the scene.

-----------------------------------------

cld   : children        [boolean] ['query', 'edit']
    Return true if the specified dependNode is a controller.

-----------------------------------------

g     : group           [boolean] ['query', 'edit']
    Create a controller that is not associated with any object. This new controller will be the parent of all the selected objects.

-----------------------------------------

idx   : index           [int] ['query', 'edit']
    In query mode, returns the index of the controller in the parent controller's list of children. In edit mode, reorder the parent controller's children connections so that the current controller is assigned the given index.

-----------------------------------------

ic    : isController    [string] ['query', 'edit']
    Returns true if the specified dependNode is a controller.

-----------------------------------------

p     : parent          [boolean] ['query', 'edit']
    Set or query the parent controller of the selected controller node.

-----------------------------------------

pwd   : pickWalkDown    [boolean] ['query', 'edit']
    Return the first child.

-----------------------------------------

pwl   : pickWalkLeft    [boolean] ['query', 'edit']
    Return the previous sibling.

-----------------------------------------

pwr   : pickWalkRight   [boolean] ['query', 'edit']
    Return the next sibling.

-----------------------------------------

pwu   : pickWalkUp      [boolean] ['query', 'edit']
    Return the parent.

-----------------------------------------

unp   : unparent        [boolean]
    Unparent all selected controller objects from their respective parent.

    """

def copyKey(al="string",an="string",at="string",cb="string",cp=1,f="floatrange",fea=1,hi="string",iub=1,index="uint",o="string",s=1,t="timerange"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/copyKey.html



-----------------------------------------

copyKey is undoable, NOT queryable, and NOT editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command copies curve segments's hierarchies from specified targets and
puts them in the clipboard. Source curves are unchanged. The pasteKey command
applies these curves to other objects.

The shape of the copied curve placed in the clipboard depends on the copyKey
"-option" specified. Each of these options below will be explained using an
example. For all the explanations, let us assume that the source animation
curve (from which keys will be copied) has 5 keyframes at times 10, 15, 20,
25, and 30.

  * copyKey -t "12:22" -option keys
    * A 5-frame animation curve with one key at 15 and another key at 20 is placed into the keyset clipboard.
  * copyKey -t "12:22" -option curve
    * A 10-frame animation is placed into the clipboard. The curve contains the original source-curve keys at times 15 and 20, as well as new keys inserted at times 12 and 22 to preserve the shape of the curve at the given time segment.

TbaseKeySetCmd.h


-----------------------------------------


Return Value:

int  Number of animation curves copied.


-----------------------------------------


Flags:

-----------------------------------------

al    : animLayer       [string] []
    Specifies that the keys getting copied should come from this specified animation layer. If no keys on the object exist on this layer, then no keys are copied.

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cb    : clipboard       [string] []
    Specifies the clipboard to which animation is copied. Valid clipboards are "api" and "anim". The default clipboard is: anim

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

fea   : forceIndependentEulerAngles [boolean] []
    Specifies that the rotation curves should always be placed on the clipboard as independent Euler Angles. The default value is false.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

o     : option          [string] []
    The option to use when performing the copyKey operation. Valid options are "keys," and "curve." The default copy option is: keys

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

t     : time            [timerange]
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

    """

def currentTime(q=1,e=1,u=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/currentTime.html



-----------------------------------------

currentTime is NOT undoable, queryable, and editable.

When given a time argument (with or without the -edit flag) this command sets
the current global time. The model updates and displays at the new time,
unless "-update off" is present on the command line.


-----------------------------------------


Return Value:

time  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

u     : update          [boolean]
    change the current time, but do not update the world. Default value is true.

    """

def curveRGBColor(q=1,hsv=1,l=1,ln=1,r=1,rf=1,rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveRGBColor.html



-----------------------------------------

curveRGBColor is undoable, queryable, and NOT editable.

This command creates, changes or removes custom curve colors, which are used
to draw the curves in the Graph Editor. The custom curve names may contain the
wildcards "?", which marches a single character, and "*", which matches any
number of characters. These colors are part of the UI and not part of the
saved data for a model. This command is not undoable.


-----------------------------------------


Return Value:

float[]  HSV values from querying the hsv flag    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

hsv   : hueSaturationValue [boolean] ['query']
    Indicates that rgb values are really hsv values.

-----------------------------------------

l     : list            [boolean] []
    Writes out a list of all curve color names and their values.

-----------------------------------------

ln    : listNames       [boolean] []
    Returns an array of all curve color names.

-----------------------------------------

r     : remove          [boolean] []
    Removes the named curve color.

-----------------------------------------

rf    : resetToFactory  [boolean] []
    Resets all the curve colors to their factory defaults.

-----------------------------------------

rs    : resetToSaved    [boolean]
    Resets all the curve colors to their saved values.

    """

def cutKey(an="string",at="string",cl=1,cp=1,f="floatrange",hi="string",iub=1,index="uint",o="string",sl=1,s=1,t="timerange"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cutKey.html



-----------------------------------------

cutKey is undoable, NOT queryable, and NOT editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

The cutKey command cuts curve segment hierarchies from specified targets and
puts them in the clipboard. The pasteKey command applies these curves to other
objects.

The shape of the cut curve placed in the clipboard, and the effect of the
cutKey command on the source animation curve depends on the cutKey "-option"
specified. Each of these options below will be explained using an example. For
all the explanations, let us assume that the source animation curve (from
which keys will be cut) has 5 keyframes at times 10, 15, 20, 25, and 30.

TbaseKeySetCmd.h

  * cutKey -t "12:22" -option keys
    * Keyframes at times 15 and 20 are removed. All other keys are unchanged.
    * A 5-frame animation curve is placed into the keyset clipboard.
  * cutKey -t "12:22" -option keysCollapse
    * Keyframes at times 15 and 20 are removed. Shift all keys after time 20 to the left by 5 frames, preserving all their values.
    * A 5-frame animation curve is placed into the keyset clipboard.
  * cutKey -t "12:22" -option keysConnect
    * Keyframes at times 15 and 20 are removed. Shift all keys after time 20 to the left by 5 frames, and place the key that used to be at time 25 at the value of the key that used to be at time 15.
    * A 5-frame animation curve is placed into the keyset clipboard.
  * cutKey -t "12:22" -option curve
    * Keyframes at times 15 and 20 are removed. Keys are inserted at times 12 and 22.
    * A 10-frame animation curve is placed into the keyset clipboard.
  * cutKey -t "12:22" -option curveCollapse
    * Keyframes at times 15 and 20 are removed. Keys are inserted at times 12 and 22. Shift all keys from time 22 to the left by 10 frames, preserving their values.
    * A 10-frame animation curve is placed into the keyset clipboard.
  * cutKey -t "12:22" -option curveConnect
    * Keyframes at times 15 and 20 are removed. Keys are inserted at times 12 and 22. Shift all keys from time 22 to the left by 10 frames, and replace the key inserted at time 12 with the newly inserted key at time 22.
    * A 10-frame animation curve is placed into the keyset clipboard.
  * cutKey -t "12:22" -option areaCollapse
    * Keyframes at times 15 and 20 are removed. Shift all keys from time 22 to the left by 10 frames, preserving their values.
    * A 10-frame animation curve is placed into the keyset clipboard.


-----------------------------------------


Return Value:

int  Number of animation curves cut.


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cl    : clear           [boolean] []
    Just remove the keyframes (i.e. do not overwrite the clipboard)

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

o     : option          [string] []
    Option for how to perform the cutKey operation. Valid values for this flag are "keys", "curve", "curveCollapse", "curveConnect", "areaCollapse". The default cut option is: keys

-----------------------------------------

sl    : selectKey       [boolean] []
    Select the keyframes of curves which have had keys removed

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

t     : time            [timerange]
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

    """

def deformerEvaluator(q=1,c=1,m=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deformerEvaluator.html



-----------------------------------------

deformerEvaluator is NOT undoable, queryable, and NOT editable.

Print debug information about deformer evaluator status. In query mode the
debug information is returned as a string[], otherwise the information is
displayed in the script editor.


-----------------------------------------


Return Value:

string[]  the debug information when query mode is used.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : chains          [boolean] ['query']
    Print information about all supported deformation chains.

-----------------------------------------

m     : meshes          [boolean]
    Print information about all meshes.

    """

def dopeSheetEditor(q=1,e=1,af="string",aft="string",ctl=1,dt="string",dat="string",dak="string",di="string",dk="string",dtn="string",dv="string",dtg="string",ex=1,f="string",fmc="string",hb=1,hlc="string",lck=1,la="string",mlc="string",o="string",pnl="string",p="string",slc="string",sel="[float, float, float, float]",sc=1,ss=1,stk=1,st="string",sv="string",sts=1,up=1,ulk=1,upd=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dopeSheetEditor.html



-----------------------------------------

dopeSheetEditor is undoable, queryable, and editable.

Edit a characteristic of a dope sheet editor


-----------------------------------------


Return Value:

string  Editor name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : autoFit         [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view.

-----------------------------------------

aft   : autoFitTime     [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view along the time axis, as well.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dat   : displayActiveKeyTangents [string] ['edit']
    on | off | tgl Display active key tangents in the editor.

-----------------------------------------

dak   : displayActiveKeys [string] ['edit']
    on | off | tgl Display active keys in the editor.

-----------------------------------------

di    : displayInfinities [string] ['edit']
    on | off | tgl Display infinities in the editor.

-----------------------------------------

dk    : displayKeys     [string] ['edit']
    on | off | tgl Display keyframes in the editor.

-----------------------------------------

dtn   : displayTangents [string] ['edit']
    on | off | tgl Display tangents in the editor.

-----------------------------------------

dv    : displayValues   [string] ['edit']
    on | off | tgl Display active keys and tangents values in the editor.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

hb    : hierarchyBelow  [boolean] ['query', 'edit']
    display animation for objects hierarchically

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

la    : lookAt          [string] ['edit']
    all | selected | currentTime FitView helpers.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

o     : outliner        [string] ['query', 'edit']
    the name of the outliner which is associated with the dope sheet

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

sel   : selectionWindow [[float, float, float, float]] ['query', 'edit']
    The selection area specified as left, right, bottom, top respectively.

-----------------------------------------

sc    : showScene       [boolean] ['query', 'edit']
    display the scene summary object

-----------------------------------------

ss    : showSummary     [boolean] ['query', 'edit']
    display the summary object

-----------------------------------------

stk   : showTicks       [boolean] ['query', 'edit']
    display per animation tick divider in channel

-----------------------------------------

st    : snapTime        [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in time.

-----------------------------------------

sv    : snapValue       [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in values.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def evaluationManager(q=1,ccl="string",di="string",mt=1,enabled=1,ia="int",ib=1,inv=1,man=1,mr=1,m="string",dst="string",ntg=1,ntp=1,nts=1,ntu=1,ust="string",sfm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/evaluationManager.html



-----------------------------------------

evaluationManager is NOT undoable, queryable, and NOT editable.

Handles turning on and off the evaluation manager method of evaluating the DG.
Query the 'mode' flag to see all available evaluation modes. The special mode
'off' disables the evaluation manager. The scheduling override flags
'nodeTypeXXX' force certain node types to use specific scheduling types, even
though the node descriptions might indicate otherwise. Use with caution;
certain nodes may not react well to alternative scheduling types. Only one
scheduling type override will be in force at a time, the most restrictive one.
In order, they are untrusted, globally serialized, locally serialized, and
parallel. The node types will however remember all overrides. For example, if
you set a node type override to be untrusted, then to be parallel it will
continue to use the untrusted override. If you then turn off the untrusted
override, the scheduling will advance to the parallel one. The actual node
scheduling type is always superceded by the overrides. For example, a serial
node will still be considered as parallel if the node type has the parallel
override set, even though 'serial' is a more restrictive scheduling type. See
the 'dbpeek' command 'graph' operation with arguments 'evaluationGraph' and
'scheduling' to see what scheduling type any particular node will end up using
after the hierarchy of overrides and native scheduling types is applied.


-----------------------------------------


Return Value:

string[]  The names of all evaluation manager modes (querying without flags)    
string[]  The names of all nodes involved in a cycle cluster with the selected
one.  
boolean  The success of activating of deactivating manipulation (with the
'manipulation' flag)  
boolean  The manipulation active or inactive state (querying the
'manipulation' flag)  
boolean  The manipulation allowed or disallowed state (querying the
'manipulationReady' flag)  
boolean  The success of setting the evaluation manager mode (with the 'mode'
flag)  
boolean  The success of setting the evaluation manager idle action (with the
'idleAction' flag)  
boolean  False if there are any nodes in the evaluation graph (with the
'empty' flag)  
Int  The Evaluation Manager idle action (querying with the 'idleAction' flag)  
boolean  Is the evaluation graph currently valid? (querying with the
'invalidate' flag)  
boolean  The success of setting the node type parallel scheduling mode (with
the 'nodeTypeParallel' flag)  
boolean[]  The parallel scheduling states of specified node types (querying
the 'nodeTypeParallel' flag with object(s))  
string[]  The names of all node types in parallel scheduling mode (querying
the 'nodeTypeParallel' flag alone)  
boolean  The success of setting the node type serialized mode (with the
'nodeTypeSerialize' flag)  
boolean[]  The serialized states of specified node types (querying the
'nodeTypeSerialize' flag with object(s))  
string[]  The names of all node types in serial scheduling mode (querying the
'nodeTypeSerialize' flag alone)  
boolean  The success of setting the node type globally serialized mode (with
the 'nodeTypeGloballySerialize' flag)  
boolean[]  The globally serialized states of specified node types (querying
the 'nodeTypeGloballySerialize' flag with object(s))  
string[]  The names of all node types in globally serialized scheduling mode
(querying the 'nodeTypeGloballySerialize' flag alone)  
boolean  The success of setting the node type untrusted mode (with the
'nodeTypeUntrusted' flag)  
boolean[]  The untrusted of specified node types (querying the
'nodeTypeUntrusted' flag with object(s))  
string[]  The names of all node types in untrusted scheduling mode (querying
the 'nodeTypeUntrusted' flag alone)  
string  The evaluation manager mode (querying with the 'mode' flag)  
string[]  The names of all nodes immediately downstream/upstream of the named
one(s) (with the 'upstreamFrom' or 'downstreamFrom' flags)  
string[]  The list of reasons the evaluation manager has been disabled
(querying the 'disableInfo' flag)  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ccl   : cycleCluster    [string] ['query']
    Returns a list of nodes that are stored together with the given one in a cycle cluster. The list will be empty when the evaluation mode is not active or the node is not in a cycle.

-----------------------------------------

di    : disableInfo     [string] ['query']
    Returns a list of strings that contain the reasons that the evaluation manager has been disabled (as distinct from it being deliberately turned off, e.g. because an unsupported node type or attribute value was encountered). If the list is empty then the evaluation manager is operating normally.

-----------------------------------------

mt    : empty           [boolean] ['query']
    Valid in query mode only. Checks to see if the evaluation graph has any nodes in it. This is independent of the current mode.

-----------------------------------------

e     : enabled         [boolean] ['query']
    Valid in query mode only. Checks to see if the evaluation manager is currently enabled. This is independent of the current mode.

-----------------------------------------

ia    : idleAction      [int] ['query']
    This flag sets the actions EM will perform on idle. It accepts the following values:    * 0 - No action   * 1 - Graph Rebuild   * 2 - EM Manipulation Preparation   * 3 - Graph Rebuild and EM Manipulation Preparation     Where:    * Graph Rebuild will rebuild the evaluation graph on an idle event as soon as it is able to do so.   * EM ManipulationPreparation will get the evaluation manager to perform all the steps necessary for EM manipulation to be available after the next idle event.     Note: These idle actions only apply to the graph attached to the normal context. All other graphs will be built according to their own rules.      The disadvantage of enabling idle actions is that for some workflows that are changing the graph frequently, or very large graphs, the graph build and manipulation preparation time may impact the workflow. If workflows are impacted it is suggested to turn idle actions off by passing this flag a value of 0.

-----------------------------------------

ib    : idleBuild       [boolean] ['query']
    This flag is obsolete. Please use the -idleAction flag with a value of 1 in order to activate evaluation graph rebuild on idle.

-----------------------------------------

inv   : invalidate      [boolean] ['query']
    This flag invalidates the graph. Value is used to control auto rebuilding on idle (false) or forced (true). This command should be used as a last resort. In query mode it checks to see if the graph is valid.

-----------------------------------------

man   : manipulation    [boolean] ['query']
    This flag is used to activate evaluation manager manipulation support.

-----------------------------------------

mr    : manipulationReady [boolean] ['query']
    Valid in query mode only. Checks to see if the evaluation manager manipulation is currently ready/allowed. This is independent of the current mode.

-----------------------------------------

m     : mode            [string] ['query']
    Changes the current evaluation mode in the evaluation manager. Supported values are "off", "serial" and "parallel".

-----------------------------------------

dst   : downstreamFrom  [string] ['query']
    Find the DG nodes that are immediately downstream of the named one in the evaluation graph. Note that the connectivity is via evaluation mode connections, not DG connections. In query mode the graph is walked and any nodes downstream of the named one are returned. The return type is alternating pairs of values that represent the graph level and the node name, e.g. if you walk downstream from A in the graph A -> B -> C then the return will be the array of strings ("0","A","1","B","2","C"). Scripts can deconstruct this information into something more visually recognizable. Note that cycles are likely to be present so any such scripts would have to handle them.  In query mode, this flag needs a value.

-----------------------------------------

ntg   : nodeTypeGloballySerialize [boolean] ['query']
    This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force global serial scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the global serial scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.

-----------------------------------------

ntp   : nodeTypeParallel [boolean] ['query']
    This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force parallel scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the parallel scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.

-----------------------------------------

nts   : nodeTypeSerialize [boolean] ['query']
    This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force local serial scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the local serial scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.

-----------------------------------------

ntu   : nodeTypeUntrusted [boolean] ['query']
    This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force untrusted scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the untrusted scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types. Untrusted scheduling will allow nodes to be evaluated in a critical section, separately from any other node evaluation. It should be used only as a last resort since the lost parallelism caused by untrusted nodes can greatly reduce performance.

-----------------------------------------

ust   : upstreamFrom    [string] ['query']
    Find the DG nodes that are immediately upstream of the named one in the evaluation graph. Note that the connectivity is via evaluation mode connections, not DG connections. In query mode the graph is walked and any nodes upstream of the named one are returned. The return type is alternating pairs of values that represent the graph level and the node name, e.g. if you walk upstream from C in the graph A -> B -> C then the return will be the array of strings ("0","C","1","B","2","A"). Scripts can deconstruct this information into something more visually recognizable. Note that cycles are likely to be present so any such scripts would have to handle them.  In query mode, this flag needs a value.

-----------------------------------------

sfm   : safeMode        [boolean]
    This flag activates/deactivates parallel evaluation safe mode. When enabled, parallel execution will fall back to serial when evaluation graph is missing dependencies. Detection is happening on scheduling of parallel evaluation, which means potential fallback will happen at the next evaluation. WARNING: This mode should be disabled with extreme caution. It will prevent parallel mode from falling back to serial mode when an invalid evaluation is detected. Sometimes the evaluation will still work correctly in those situations and use of this flag will keep the peak parallel performance running. However since the safe mode is used to catch invalid evaluation disabling it may also cause problems with evaluation, anything from invalid values, missing evaluation, or even crashes.

    """

def evaluator(q=1,cl=1,c="string",en=1,i=1,n="string",nt="string",ntc=1,p="int",vn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/evaluator.html



-----------------------------------------

evaluator is NOT undoable, queryable, and NOT editable.

Handles turning on and off custom evaluation overrides used by the evaluation
manager. Query no flag to see all available custom evaluators. Query the
'enable' flag to check if an evaluator is currently enabled. If the 'name'
flag isn't used then return all modes and their current active state.


-----------------------------------------


Return Value:

string[]  the list of available evaluators (querying with no evaluator flag or
invalid evaluator name)    
boolean  the previous active state of the named evaluator (with 'name' and
'enable' flags)  
boolean  the active state of the named evaluator (query with 'name' and
'enable' flags)  
string[]  the list of evaluators in the requested active state (query 'enable'
flag alone)  
string[]  the list of nodes for which the evaluator was activated or
deactivated (with 'nodeType' or 'nodeTypeChildren' flags)  
string  the queried value for the evaluator (with 'name' and 'valueName'
flags)  
boolean  true if the configuration request was accepted by the evaluator (with
'name' flag and 'configuration' flag)  
string[]  the list of configuration parameters accepted by the evaluator
(query mode with 'name' flag and 'configuration' flag)  
string[]  the list of clusters currently assigned to the evaluator with
intervening sublist sizes (query mode with 'name' flag and 'clusters' flag)  
string  the help information supplied by the evaluator (query mode with 'name'
flag and 'info' flag)  
int  the priority value of the evaluator (query mode with 'name' flag and
'priority' flag)  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cl    : clusters        [boolean] ['query']
    This flag queries the list of clusters currently assigned to the named custom evaluator. The return value will be an array of strings where the array consists of a set of (number, string[]) groups. e.g. If an evaluator has 2 clusters with 2 and 3 nodes in them respectively the output would be something like: (2, 'transform2', 'transform3', 3, 'joint1', 'joint2', 'joint3')

-----------------------------------------

c     : configuration   [string] ['query']
    Sends configuration information to a custom evaluator. It's up to the evaluator to understand what they mean. Multiple configuration messages can be sent in a single command. Query this flag for a given evaluator to find out what configuration messages it accepts.

-----------------------------------------

en    : enable          [boolean] ['query']
    Enables or disables a specific graph evaluation runtime, depending on the state of the flag. In order to use this flag you must also specify the name in the 'name' argument. When the 'enable' flag is used in conjunction with the 'nodeType' flag then it is used to selectively turn on or off the ability of the given evaluator to handle nodes of the given type (i.e. it no longer toggles the evaluator enabled state). When the 'enable' flag is used in conjunction with the 'configuration' flag then it is passed along with the configuration message interpreted by the custom evaluator.

-----------------------------------------

i     : info            [boolean] ['query']
    Queries the evaluator information. Only valid in query mode since the information is generated by the evaluator's internal state and cannot be changed. In order to use this flag, the 'name' argument must also be specified.

-----------------------------------------

n     : name            [string] ['query']
    Names a particular DG evaluation override evaluator. Evaluators are registered automatically by name. Query this flag to get a list of available runtimes. When a runtime is registered it is enabled by default. Use the 'enable' flag to change its enabled state.  In query mode, this flag can accept a value.

-----------------------------------------

nt    : nodeType        [string] ['query']
    Names a particular node type to be passed to the evaluator request. Evaluators can either use or ignore the node type information as passed.  In query mode, this flag can accept a value.

-----------------------------------------

ntc   : nodeTypeChildren [boolean] ['query']
    If enabled when using the 'nodeType' flag then handle all of the node types derived from the given one as well. Default is to only handle the named node type.

-----------------------------------------

p     : priority        [int] ['query']
    Query or set the evaluator priority. Custom evaluator with highest priority order will get the chance to claim the nodes first. Evaluators must have unique priority values. In order to use this flag you must also specify the name in the 'name' argument.

-----------------------------------------

vn    : valueName       [string]
    Queries a value from a given evaluator. Evaluators can define a set of values for which they answer.  In query mode, this flag can accept a value.

    """

def filterCurve(cof="float",endTime="time",f="string",kof=1,ker="string",ks=1,mxs="float",mns="float",per="float",pre="float",pm="int",pkt="string",sr="float",sk=1,s="time",tto="float",tol="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filterCurve.html



-----------------------------------------

filterCurve is undoable, NOT queryable, and NOT editable.

The filterCurve command takes a list of anim curve and filters them using a
specified filter. The following filters are supported: butterworth euler
keyReducer keySync resample simplify


-----------------------------------------


Return Value:

int  The number of filtered curves


-----------------------------------------


Flags:

-----------------------------------------

cof   : cutoffFrequency [float] []
    Defines the cutoff frequency (in Hz) for the Butterworth filter.

-----------------------------------------

e     : endTime         [time] []
    Specify the end time of the section to filter. If not specified, the last key of the animation curve is used to define the end time.

-----------------------------------------

f     : filter          [string] []
    Specifies the filter type to use. The avalible filters are: butterworth euler (default) keyReducer keySync resample simplify

-----------------------------------------

kof   : keepKeysOnFrame [boolean] []
    When specified, a secondary filter pass is applied to position keys on whole frames. This flag is only supported by the Butterworth filter.

-----------------------------------------

ker   : kernel          [string] []
    The resample kernel is a decimation resampling filter used to resample dense data. It works on the keyframes and may not produce the desired results when used with sparse data.  The resample filter converts from either uniform or non-uniform timestep input data samples to the specified uniform timeStep. Various time domain filters are available and are specified with the kernel flag which selects the resampling kernel applied to the keyframes on the animation curves.  Kernel Values | closest |  Closest sample to output timestamp

-----------------------------------------

ks    : keySync         [boolean] []
    When specified, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered. This flag is only supported by the Key Reducer filter.

-----------------------------------------

mxs   : maxTimeStep     [float] []
    Simplify filter.

-----------------------------------------

mns   : minTimeStep     [float] []
    Simplify filter.

-----------------------------------------

per   : period          [float] []
    Resample filter

-----------------------------------------

pre   : precision       [float] []
    Defines the precision parameter. For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.

-----------------------------------------

pm    : precisionMode   [int] []
    Defines whether the precision value should be treated as: 0: An absolute value 1: A percentage.

-----------------------------------------

pkt   : preserveKeyTangent [string] []
    When specified, keys whose in or out tangent type match the specified type are preserved. Supported tangent types: fixed linear flat smooth step clamped plateau stepnext auto This flag is only supported by the Key Reducer filter.

-----------------------------------------

sr    : samplingRate    [float] []
    Defines the rate at which keys are added to the Butterworth filtered curve in frames per second (FPS).

-----------------------------------------

sk    : selectedKeys    [boolean] []
    When specified, the filter is only applied to selected keys. This flag supercedes the startTime/endTime specification.

-----------------------------------------

s     : startTime       [time] []
    Specify the start time to filter. If not specified, then the first key in the animation curve is used to get the start time.

-----------------------------------------

tto   : timeTolerance   [float] []
    Simplify filter.

-----------------------------------------

tol   : tolerance       [float]
    Simplify filter.

    """

def findKeyframe(an="string",at="string",cp=1,c=1,f="floatrange",hi="string",iub=1,index="uint",s=1,t="timerange",ts=1,w="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/findKeyframe.html



-----------------------------------------

findKeyframe is undoable, NOT queryable, and NOT editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command will return the time (in current units) of the requested key. For
the relative direction methods (next, previous) if -time is NOT specified they
will use current time. If the specified object is not animated the command
will return the current time.


-----------------------------------------


Return Value:

time  Command result


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

c     : curve           [boolean] []
    Return a list of the existing curves driving the selected object or attributes. The which, index, floatRange, timeRange, and includeUpperBound flags are ignored when this flag is used.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

ts    : timeSlider      [boolean] []
    Get the next key time from the ticks displayed in the time slider. If this flag is set, then the -an/animation flag is ignored.

-----------------------------------------

w     : which           [string]
    next | previous | first | last How to find the key

    """

def flow(q=1,e=1,dv="[uint, uint, uint]",lc=1,ld="[uint, uint, uint]",oc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/flow.html



-----------------------------------------

flow is undoable, queryable, and editable.

The flow command creates a deformation lattice to `bend' the object that is
animated along a curve of a motion path animation. The motion path animation
has to have the follow option set to be on.


-----------------------------------------


Return Value:

string[]  The names of the created flow node and associated lattice nodes.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dv    : divisions       [[uint, uint, uint]] ['query']
    This flag specifies the number of lattice slices in x,y,z.   The default values are 2 5 2.   When queried, it returns the uint32_t uint32_t uint32_t

-----------------------------------------

lc    : localCompute    [boolean] ['query']
    This flag specifies whether or not to have local control over the object deformation.   Default value: is on when the lattice is around the curve, and is off when the lattice is around the object.   When queried, it returns a boolean

-----------------------------------------

ld    : localDivisions  [[uint, uint, uint]] ['query']
    This flag specifies the extent of the region of effect.   Default values are 2 2 2.   When queried, it returns the uint32_t uint32_t uint32_t

-----------------------------------------

oc    : objectCentered  [boolean]
    This flag specifies whether to create the lattice around the selected object at its center, or to create the lattice around the curve.   Default value is true.   When queried, it returns a boolean

    """

def freeze(q=1,all=1,dl=1,dn=1,fd=1,f=1,i=1,n=1,uf=1,up=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/freeze.html



-----------------------------------------

freeze is undoable, queryable, and NOT editable.

When a node is frozen none of its inputs will be requested when they change,
the node will use the inputs that existed at the time of freezing until the
node is unfrozen. A node can be frozen in one of two ways; either directly,
via setting the "frozen" attribute on the node to be true, or indirectly, via
setting the "frozenAffected" extension attribute on the node to be true. This
command lets you freeze nodes based on various criteria. See the flags for the
types of criteria the command uses to decide what to freeze or unfreeze. The
nodes that are selected are frozen directly. The nodes affected by directly
frozen nodes, considering the argument settings, are frozen indirectly. If the
frozen attribute, visibililty, or display layer mode has an input connection
then the frozen state will not propagate because the node could be unfrozen or
become visible at playback time. In query mode this command will find the
nodes with each of the frozen states set (frozen, frozenAffected, and
neither).


-----------------------------------------


Return Value:

string[]  In query mode the list of currently frozen or unfrozen nodes. The
list is in three parts separated by an empty string; nodes with frozen state
(un)set, nodes with frozenAffected state (un)set, and the rest of the selected
nodes    
string[]  the list of nodes whose frozen state was set by the command. The
list is in two parts separated by an empty string; nodes with frozen state
set, and nodes with frozenAffected state set  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : allNodes        [boolean] ['query']
    Select which nodes are to be used for the operation. If it is not set then the selection list will be used. If nothing is selected all nodes in the scene will be used. This flag can be used in query mode to find the set of frozen nodes in the scene. It can also be used in create mode with filters (displayLayers, invisible, or frozen) to target a specific subset of nodes in the scene.

-----------------------------------------

dl    : displayLayers   [boolean] ['query']
    If this flag is enabled then the display layers on the list to be processed will be walked. Any nodes they control will be added to the processing list, providing the display layer visibility control is off and not connected. Note: Animated visibility or enabled states will be treated as matches to be thorough. No attempt is made to check for static animation.

-----------------------------------------

dn    : downstream      [boolean] ['query']
    If this flag is enabled then the frozen state will attempt to propagate downstream from the selected nodes. e.g. the mesh shape deformations being controlled by a skeleton rig.

-----------------------------------------

fd    : forceDownstream [boolean] ['query']
    If this flag is enabled then the frozen state will attempt to propagate downstream from the selected nodes. e.g. the mesh shape deformations being controlled by a skeleton rig. Unlike the downstream flag though this one will freeze downstream nodes even if they have other, unfrozen, inputs.

-----------------------------------------

f     : frozen          [boolean] ['query']
    If this flag is enabled then the list of nodes to be processed will be filtered out so that only nodes with the frozen attribute already set are included. Otherwise all nodes being processed will first have their frozen attribute set before propagating the frozen state. This flag would only be used if nodes were previously frozen and the command is used to propagate the frozen state through the graph.

-----------------------------------------

i     : invisible       [boolean] ['query']
    If this flag is enabled then the invisible nodes on the list to be processed will be walked. Any nodes below them in the DAG hierarchy will be added to the processing list, providing the visibility attribute is not connected. Note: Animated visibility states will be treated as a match to be thorough. No attempt is made to check for static animation.

-----------------------------------------

n     : noFreeze        [boolean] ['query']
    This flag previews the nodes that will be frozen without actually freezing them.

-----------------------------------------

uf    : unfreeze        [boolean] ['query']
    If this flag is enabled then the nodes being processed will have their frozen state turned off instead of on. All of the same filtering and propagating will be done when deciding which nodes to modify. In query mode this flag switches from returning the already-frozen nodes to returning the unfrozen nodes.

-----------------------------------------

up    : upstream        [boolean]
    If this flag is enabled then the frozen state will attempt to propagate upstream through the selected nodes. e.g. the param curves feeding into a frozen transform. Heuristics are applied to this propagation to ensure that upstream nodes that are still used by unfrozen nodes will stay unfrozen themselves.

    """

def freezeOptions(q=1,dl=1,dn="string",ep=1,inv=1,rn=1,rt=1,up="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/freezeOptions.html



-----------------------------------------

freezeOptions is NOT undoable, queryable, and NOT editable.

This command provides access to the options used by the evaluation manager to
handle propagation and recognition of when a node is in a frozen state. See
the individual flags for the different options available. These values are all
stored as user preferences and persist across sessions.


-----------------------------------------


Return Value:

string  Current value of the option if querying the downstream or upstream
flags    
boolean  Current value of the option if querying the displayLayers, invisible,
referencedNodes, explicitPropagation, or runtimePropagaton flags  
boolean  In creation mode returns true if all options were successfully set  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dl    : displayLayers   [boolean] ['query']
    If this option is enabled then any nodes that are in an enabled, invisible display layer will be considered to be frozen, and the frozen state will propagate accordingly.

-----------------------------------------

dn    : downstream      [string] ['query']
    Controls how frozen state is propagated downstream from currently frozen nodes. Valid values are "none" for no propagation, "safe" for propagation downstream only when all upstream nodes are frozen, and "force" for propagation downstream when any upstream node is frozen.

-----------------------------------------

ep    : explicitPropagation [boolean] ['query']
    When turned on this will perform an extra pass when the evaluation graph is constructed to perform intelligent propagation of the frozen state to related nodes as specified by the currently enabled options of the evaluation graph. See also "runtimePropagation". This option performs more thorough propagation of the frozen state, but requires extra time for recalculating the evaluation graph.

-----------------------------------------

inv   : invisible       [boolean] ['query']
    If this option is enabled then any nodes that are invisible, either directly or via an invisible parent node, will be considered to be frozen, and the frozen state will propagate accordingly.

-----------------------------------------

rn    : referencedNodes [boolean] ['query']
    If this option is enabled then any nodes that are referenced in from a frozen referenced node will also be considered to be frozen, and the frozen state will propagate accordingly.

-----------------------------------------

rt    : runtimePropagation [boolean] ['query']
    When turned on this will allow the frozen state to propagate during execution of the evaluation graph. See also "explicitPropagation". This option allows frozen nodes to be scheduled for evaluation, but once it discovers a node that is frozen it will prune the evaluation based on the current set of enabled options. It only works in the downstream direction.

-----------------------------------------

up    : upstream        [string]
    Controls how frozen state is propagated upstream from currently frozen nodes. Valid values are "none" for no propagation, "safe" for propagation upstream only when all downstream nodes are frozen, and "force" for propagation upstream when any downstream node is frozen.

    """

def hikGlobals(q=1,e=1,rap=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hikGlobals.html



-----------------------------------------

hikGlobals is undoable, queryable, and editable.

Sets global HumanIK flags for the application.


-----------------------------------------


Return Value:

boolean  Giving the state of the option    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

rap   : releaseAllPinning [boolean]
    Sets the global release all pinning hik flag. When this flag is set, all pinning states are ignored.

    """

def keyframe(q=1,e=1,a=1,abd=1,an="string",at="string",bd=1,ct="[time, time, float]",cp=1,ev=1,f="floatrange",fc="float",hi="string",iub=1,index="uint",iv=1,kc=1,lsl=1,n=1,o="string",r=1,sl=1,s=1,tds=1,t="timerange",tc="time",vc="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframe.html



-----------------------------------------

keyframe is undoable, queryable, and editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command edits the time and/or value of keys of specified objects and/or
parameter curves

Unless otherwise specified by the -query flag, the command defaults to editing
keyframes.


-----------------------------------------


Return Value:

int  (except where noted below) Number of curves on which keys were modified.
In -query mode, the command can return a variety of things, as described with
each queryable flag below.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    Move amounts are absolute.

-----------------------------------------

abd   : adjustBreakdown [boolean] []
    When false, moving keys will not preserve breakdown timing, when true (the default) breakdowns will be adjusted to preserve their timing relationship.

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

bd    : breakdown       [boolean] ['query', 'edit']
    Sets the breakdown state for the key. Returns an integer. Default is false. The breakdown state of a key cannot be set in the same command as it is moved (i.e., via the -tc or -fc flags).

-----------------------------------------

ct    : clipTime        [[time, time, float]] []
    Modifies the final time where a key is inserted using an offset, pivot, and scale.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

ev    : eval            [boolean] ['query']
    Returns the value(s) of the animCurves when evaluated (without regard to input connections) at the times given by the -t/time or -f/float flags. Cannot be used in combination with other query flags, and cannot be used with time ranges (-t "5:10"). When no -t or -f flags appear on the command line, the evals are queried at the current time. Query returns a float[].

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

fc    : floatChange     [float] ['query', 'edit']
    How much (with -relative) or where (with -absolute) to move keys (on non-time-input animation curves) along the x (float) axis. Returns float[] when queried.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

iv    : indexValue      [boolean] ['query']
    Query-only flag that returns an int for the key's index.

-----------------------------------------

kc    : keyframeCount   [boolean] ['query']
    Returns an int for the number of keys found for the targets.

-----------------------------------------

lsl   : lastSelected    [boolean] ['query']
    When used in queries, this flag returns requested values for the last selected key.

-----------------------------------------

n     : name            [boolean] ['query']
    Returns the names of animCurves of specified nodes, attributes or keys.

-----------------------------------------

o     : option          [string] ['edit']
    Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.

-----------------------------------------

r     : relative        [boolean] []
    Move amounts are relative to a key's current position.

-----------------------------------------

sl    : selected        [boolean] ['query']
    When used in queries, this flag returns requested values for any active keys.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

tds   : tickDrawSpecial [boolean] ['edit']
    Sets the special drawing state for this key when it is drawn as a tick in the timeline.

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

tc    : timeChange      [time] ['query', 'edit']
    How much (with -relative) or where (with -absolute) to move keys (on time-input animation curves) along the x (time) axis. Returns float[] when queried.

-----------------------------------------

vc    : valueChange     [float]
    How much (with -relative) or where (with -absolute) to move keys along the y (value) axis. Returns float[] when queried.

    """

def keyframeOutliner(q=1,e=1,ac="string",ann="string",bgc="[float, float, float]",dt="string",dsp="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,npm=1,p="string",pma=1,po=1,sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeOutliner.html



-----------------------------------------

keyframeOutliner is undoable, queryable, and editable.

This command creates/edits/queries a keyframe outliner control.


-----------------------------------------


Return Value:

string  The name of the outliner control.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : animCurve       [string] ['edit']
    Name of the animation curve for which to display keyframes.

-----------------------------------------

ann   : annotation      [string] ['query', 'edit']
    Annotate the control with an extra string value.

-----------------------------------------

bgc   : backgroundColor [[float, float, float]] ['query', 'edit']
    The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.   When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dsp   : display         [string] ['query', 'edit']
    narrow | wide What columns to display. When "narrow", time and value will be displayed, when "wide" tangent information will be displayed as well

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Add a documentation flag to the control. The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)

-----------------------------------------

dgc   : dragCallback    [script] ['edit']
    Adds a callback that is called when the middle mouse button is pressed. The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type. Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback. The recommended way is to pass a Python function object as the argument. In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed. In that case, the string will have the values substituted into it via the standard Python format operator. The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers". The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

-----------------------------------------

dpc   : dropCallback    [script] ['edit']
    Adds a callback that is called when a drag and drop operation is released above the drop site. The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback. The recommended way is to pass a Python function object as the argument. In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed. In that case, the string will have the values substituted into it via the standard Python format operator. The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type". The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

-----------------------------------------

en    : enable          [boolean] ['query', 'edit']
    The enable state of the control. By default, this flag is set to true and the control is enabled. Specify false and the control will appear dimmed or greyed-out indicating it is disabled.

-----------------------------------------

ebg   : enableBackground [boolean] ['query', 'edit']
    Enables the background color of the control.

-----------------------------------------

ekf   : enableKeyboardFocus [boolean] ['query', 'edit']
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard. If not, the user can only use the mouse. This flag would typically be used to turn off keyboard focus support from controls that get it by default, like Edit and List controls

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

fpn   : fullPathName    [boolean] ['query']
    Return the full path name of the widget, which includes all the parents.

-----------------------------------------

h     : height          [int] ['query', 'edit']
    The height of the control. The control will attempt to be this size if it is not overruled by parent layout conditions.

-----------------------------------------

hlc   : highlightColor  [[float, float, float]] ['query', 'edit']
    The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.

-----------------------------------------

io    : isObscured      [boolean] ['query']
    Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.

-----------------------------------------

m     : manage          [boolean] ['query', 'edit']
    Manage state of the control. An unmanaged control is not visible, nor does it take up any screen real estate. All controls are created managed by default.

-----------------------------------------

nbg   : noBackground    [boolean] ['edit']
    Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn. The state of this flag is inherited by children of this control.

-----------------------------------------

npm   : numberOfPopupMenus [boolean] ['query']
    Return the number of popup menus attached to this control.

-----------------------------------------

p     : parent          [string] ['query']
    The parent layout for this control.

-----------------------------------------

pma   : popupMenuArray  [boolean] ['query']
    Return the names of all the popup menus attached to this control.

-----------------------------------------

po    : preventOverride [boolean] ['query', 'edit']
    If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.

-----------------------------------------

sbm   : statusBarMessage [string] ['edit']
    Extra string to display in the status bar when the mouse is over the control.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

vis   : visible         [boolean] ['query', 'edit']
    The visible state of the control. A control is created visible by default. Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).

-----------------------------------------

vcc   : visibleChangeCommand [script] ['query', 'edit']
    Command that gets executed when visible state of the control changes.

-----------------------------------------

w     : width           [int]
    The width of the control. The control will attempt to be this size if it is not overruled by parent layout conditions.

    """

def keyframeStats(q=1,e=1,adj="int",ad2="int",ad3="int",ad4="int",ad5="int",ad6="int",ae="string",ann="string",bgc="[float, float, float]",cm=1,cal="[int, string]",cl2="[string, string]",cl3="[string, string, string]",cl4="[string, string, string, string]",cl5="[string, string, string, string, string]",cl6="[string, string, string, string, string, string]",cat="[int, string, int]",ct2="[string, string]",ct3="[string, string, string]",ct4="[string, string, string, string]",ct5="[string, string, string, string, string]",ct6="[string, string, string, string, string, string]",co2="[int, int]",co3="[int, int, int]",co4="[int, int, int, int]",co5="[int, int, int, int, int]",co6="[int, int, int, int, int, int]",cw="[int, int]",cw1="int",cw2="[int, int]",cw3="[int, int, int]",cw4="[int, int, int, int]",cw5="[int, int, int, int, int]",cw6="[int, int, int, int, int, int]",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,npm=1,p="string",pma=1,pre="int",po=1,rat="[int, string, int]",sbm="string",tan="string",ut="string",van="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeStats.html



-----------------------------------------

keyframeStats is undoable, queryable, and editable.

All of the group commands position their individual controls in columns
starting at column 1. The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach,
-cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are
left aligned with no offset and are 100 pixels wide. Only one column in any
group can be adjustable.

This command creates, edits, queries a keyframe stats control.


-----------------------------------------


Return Value:

string  The name of the stats control.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

adj   : adjustableColumn [int] ['edit']
    Specifies which column has an adjustable size that changes with the sizing of the layout. The column value is a 1-based index. Passing 0 as argument turns off the previous adjustable column.

-----------------------------------------

ad2   : adjustableColumn2 [int] ['edit']
    Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly two columns.

-----------------------------------------

ad3   : adjustableColumn3 [int] ['edit']
    Specifies that the column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly three columns.

-----------------------------------------

ad4   : adjustableColumn4 [int] ['edit']
    Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly four columns.

-----------------------------------------

ad5   : adjustableColumn5 [int] ['edit']
    Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly five columns.

-----------------------------------------

ad6   : adjustableColumn6 [int] ['edit']
    Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly six columns.

-----------------------------------------

ae    : animEditor      [string] ['query', 'edit']
    The name of the animation editor which is associated with the control

-----------------------------------------

ann   : annotation      [string] ['query', 'edit']
    Annotate the control with an extra string value.

-----------------------------------------

bgc   : backgroundColor [[float, float, float]] ['query', 'edit']
    The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.   When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.

-----------------------------------------

cm    : classicMode     [boolean] ['query', 'edit']
    Edit display mode. True means stats only, otherwise show time value.

-----------------------------------------

cal   : columnAlign     [[int, string]] ['edit']
    Arguments are : column number, alignment type. Possible alignments are: left | right | center. Specifies alignment type for the specified column.

-----------------------------------------

cl2   : columnAlign2    [[string, string]] ['edit']
    Sets the text alignment of both columns. Ignored if there are not exactly two columns. Valid values are "left", "right", and "center".

-----------------------------------------

cl3   : columnAlign3    [[string, string, string]] ['edit']
    Sets the text alignment for all three columns. Ignored if there are not exactly three columns. Valid values are "left", "right", and "center".

-----------------------------------------

cl4   : columnAlign4    [[string, string, string, string]] ['edit']
    Sets the text alignment for all four columns. Ignored if there are not exactly four columns. Valid values are "left", "right", and "center".

-----------------------------------------

cl5   : columnAlign5    [[string, string, string, string, string]] ['edit']
    Sets the text alignment for all five columns. Ignored if there are not exactly five columns. Valid values are "left", "right", and "center".

-----------------------------------------

cl6   : columnAlign6    [[string, string, string, string, string, string]] ['edit']
    Sets the text alignment for all six columns. Ignored if there are not exactly six columns. Valid values are "left", "right", and "center".

-----------------------------------------

cat   : columnAttach    [[int, string, int]] ['edit']
    Arguments are : column number, attachment type, and offset. Possible attachments are: left | right | both. Specifies column attachment types and offets.

-----------------------------------------

ct2   : columnAttach2   [[string, string]] ['edit']
    Sets the attachment type of both columns. Ignored if there are not exactly two columns. Valid values are "left", "right", and "both".

-----------------------------------------

ct3   : columnAttach3   [[string, string, string]] ['edit']
    Sets the attachment type for all three columns. Ignored if there are not exactly three columns. Valid values are "left", "right", and "both".

-----------------------------------------

ct4   : columnAttach4   [[string, string, string, string]] ['edit']
    Sets the attachment type for all four columns. Ignored if there are not exactly four columns. Valid values are "left", "right", and "both".

-----------------------------------------

ct5   : columnAttach5   [[string, string, string, string, string]] ['edit']
    Sets the attachment type for all five columns. Ignored if there are not exactly five columns. Valid values are "left", "right", and "both".

-----------------------------------------

ct6   : columnAttach6   [[string, string, string, string, string, string]] ['edit']
    Sets the attachment type for all six columns. Ignored if there are not exactly six columns. Valid values are "left", "right", and "both".

-----------------------------------------

co2   : columnOffset2   [[int, int]] ['edit']
    This flag is used in conjunction with the -columnAttach2 flag. If that flag is not used then this flag will be ignored. It sets the offset for the two columns. The offsets applied are based on the attachments specified with the -columnAttach2 flag. Ignored if there are not exactly two columns.

-----------------------------------------

co3   : columnOffset3   [[int, int, int]] ['edit']
    This flag is used in conjunction with the -columnAttach3 flag. If that flag is not used then this flag will be ignored. It sets the offset for the three columns. The offsets applied are based on the attachments specified with the -columnAttach3 flag. Ignored if there are not exactly three columns.

-----------------------------------------

co4   : columnOffset4   [[int, int, int, int]] ['edit']
    This flag is used in conjunction with the -columnAttach4 flag. If that flag is not used then this flag will be ignored. It sets the offset for the four columns. The offsets applied are based on the attachments specified with the -columnAttach4 flag. Ignored if there are not exactly four columns.

-----------------------------------------

co5   : columnOffset5   [[int, int, int, int, int]] ['edit']
    This flag is used in conjunction with the -columnAttach5 flag. If that flag is not used then this flag will be ignored. It sets the offset for the five columns. The offsets applied are based on the attachments specified with the -columnAttach5 flag. Ignored if there are not exactly five columns.

-----------------------------------------

co6   : columnOffset6   [[int, int, int, int, int, int]] ['edit']
    This flag is used in conjunction with the -columnAttach6 flag. If that flag is not used then this flag will be ignored. It sets the offset for the six columns. The offsets applied are based on the attachments specified with the -columnAttach6 flag. Ignored if there are not exactly six columns.

-----------------------------------------

cw    : columnWidth     [[int, int]] ['edit']
    Arguments are : column number, column width. Sets the width of the specified column where the first parameter specifies the column (1 based index) and the second parameter specifies the width.

-----------------------------------------

cw1   : columnWidth1    [int] ['edit']
    Sets the width of the first column. Ignored if there is not exactly one column.

-----------------------------------------

cw2   : columnWidth2    [[int, int]] ['edit']
    Sets the column widths of both columns. Ignored if there are not exactly two columns.

-----------------------------------------

cw3   : columnWidth3    [[int, int, int]] ['edit']
    Sets the column widths for all 3 columns. Ignored if there are not exactly 3 columns.

-----------------------------------------

cw4   : columnWidth4    [[int, int, int, int]] ['edit']
    Sets the column widths for all 4 columns. Ignored if there are not exactly 4 columns.

-----------------------------------------

cw5   : columnWidth5    [[int, int, int, int, int]] ['edit']
    Sets the column widths for all 5 columns. Ignored if there are not exactly 5 columns.

-----------------------------------------

cw6   : columnWidth6    [[int, int, int, int, int, int]] ['edit']
    Sets the column widths for all 6 columns. Ignored if there are not exactly 6 columns.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Add a documentation flag to the control. The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)

-----------------------------------------

dgc   : dragCallback    [script] ['edit']
    Adds a callback that is called when the middle mouse button is pressed. The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type. Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback. The recommended way is to pass a Python function object as the argument. In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed. In that case, the string will have the values substituted into it via the standard Python format operator. The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers". The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

-----------------------------------------

dpc   : dropCallback    [script] ['edit']
    Adds a callback that is called when a drag and drop operation is released above the drop site. The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback. The recommended way is to pass a Python function object as the argument. In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed. In that case, the string will have the values substituted into it via the standard Python format operator. The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type". The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

-----------------------------------------

en    : enable          [boolean] ['query', 'edit']
    The enable state of the control. By default, this flag is set to true and the control is enabled. Specify false and the control will appear dimmed or greyed-out indicating it is disabled.

-----------------------------------------

ebg   : enableBackground [boolean] ['query', 'edit']
    Enables the background color of the control.

-----------------------------------------

ekf   : enableKeyboardFocus [boolean] ['query', 'edit']
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard. If not, the user can only use the mouse. This flag would typically be used to turn off keyboard focus support from controls that get it by default, like Edit and List controls

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

fpn   : fullPathName    [boolean] ['query']
    Return the full path name of the widget, which includes all the parents.

-----------------------------------------

h     : height          [int] ['query', 'edit']
    The height of the control. The control will attempt to be this size if it is not overruled by parent layout conditions.

-----------------------------------------

hlc   : highlightColor  [[float, float, float]] ['query', 'edit']
    The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.

-----------------------------------------

io    : isObscured      [boolean] ['query']
    Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.

-----------------------------------------

m     : manage          [boolean] ['query', 'edit']
    Manage state of the control. An unmanaged control is not visible, nor does it take up any screen real estate. All controls are created managed by default.

-----------------------------------------

nbg   : noBackground    [boolean] ['edit']
    Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn. The state of this flag is inherited by children of this control.

-----------------------------------------

npm   : numberOfPopupMenus [boolean] ['query']
    Return the number of popup menus attached to this control.

-----------------------------------------

p     : parent          [string] ['query']
    The parent layout for this control.

-----------------------------------------

pma   : popupMenuArray  [boolean] ['query']
    Return the names of all the popup menus attached to this control.

-----------------------------------------

pre   : precision       [int] ['query', 'edit']
    Controls the number of digits to the right of the decimal point that will be displayed for float-valued channels. Default is 3. Queried, returns an int.

-----------------------------------------

po    : preventOverride [boolean] ['query', 'edit']
    If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.

-----------------------------------------

rat   : rowAttach       [[int, string, int]] ['edit']
    Arguments are : column, attachment type, offset. Possible attachments are: top | bottom | both. Specifies attachment types and offsets for the entire row.

-----------------------------------------

sbm   : statusBarMessage [string] ['edit']
    Extra string to display in the status bar when the mouse is over the control.

-----------------------------------------

tan   : timeAnnotation  [string] ['query', 'edit']
    Annotate the time field with an extra string value.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

van   : valueAnnotation [string] ['query', 'edit']
    Annotate the value field with an extra string value.

-----------------------------------------

vis   : visible         [boolean] ['query', 'edit']
    The visible state of the control. A control is created visible by default. Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).

-----------------------------------------

vcc   : visibleChangeCommand [script] ['query', 'edit']
    Command that gets executed when visible state of the control changes.

-----------------------------------------

w     : width           [int]
    The width of the control. The control will attempt to be this size if it is not overruled by parent layout conditions.

    """

def keyingGroup(q=1,e=1,act="name",add="name",af=1,cat="string",cl="name",co="int",cp="name",eg=1,ep=1,em=1,ed=1,er=1,es=1,et=1,ev=1,fc=1,fl="name",fe="name",include="name",int="name",ii="name",im="name",l=1,mr=1,n="string",nss=1,nw=1,no=1,rm="name",rac="name",r=1,fil="string",s=1,sp="name",sub="name",t="string",un="name",v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyingGroup.html



-----------------------------------------

keyingGroup is undoable, queryable, and editable.

This command is used to manage the membership of a keying group. Keying groups
allow users to effectively manage related keyframe data, allowing keys on
attributes in the keying group to be set and edited as a single entity.


-----------------------------------------


Return Value:

string  For creation operations (name of the keying group that was created or
edited)    
string[]  For query operation (names of items in the keying group)  
boolean  For isMember operation  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

act   : activator       [name] ['query', 'edit']
    Sets the selected node(s) as activators for the given keying group. In query mode, returns list of objects that activate the given keying group

-----------------------------------------

add   : addElement      [name] ['edit']
    Adds the list of items to the given set. If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.

-----------------------------------------

af    : afterFilters    [boolean] ['edit']
    Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.

-----------------------------------------

cat   : category        [string] ['query', 'edit']
    Sets the keying group's category. This is what the global, active keying group filter will use to match.

-----------------------------------------

cl    : clear           [name] ['edit']
    An operation which removes all items from the given set making the set empty.

-----------------------------------------

co    : color           [int] ['query', 'edit']
    Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors). -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this color.

-----------------------------------------

cp    : copy            [name] []
    Copies the members of the given set to a new set. This flag is for use in creation mode only.

-----------------------------------------

eg    : edges           [boolean] ['query']
    Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.

-----------------------------------------

ep    : editPoints      [boolean] ['query']
    Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.

-----------------------------------------

em    : empty           [boolean] []
    Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.

-----------------------------------------

ed    : excludeDynamic  [boolean] []
    When creating the keying group, exclude dynamic attributes.

-----------------------------------------

er    : excludeRotate   [boolean] []
    When creating the keying group, exclude rotate attributes from transform-type nodes.

-----------------------------------------

es    : excludeScale    [boolean] []
    When creating the keying group, exclude scale attributes from transform- type nodes.

-----------------------------------------

et    : excludeTranslate [boolean] []
    When creating the keying group, exclude translate attributes from transform-type nodes. For example, if your keying group contains joints only, perhaps you only want to include rotations in the keying group.

-----------------------------------------

ev    : excludeVisibility [boolean] []
    When creating the keying group, exclude visibility attribute from transform-type nodes.

-----------------------------------------

fc    : facets          [boolean] ['query']
    Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.

-----------------------------------------

fl    : flatten         [name] ['edit']
    An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.

-----------------------------------------

fe    : forceElement    [name] ['edit']
    For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition mutually exclusive with respect to membership.

-----------------------------------------

include : include         [name] ['edit']
    Adds the list of items to the given set. If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.

-----------------------------------------

int   : intersection    [name] []
    An operation that returns a list of items which are members of all the sets in the list.

-----------------------------------------

ii    : isIntersecting  [name] []
    An operation which tests whether the sets in the list have common members.

-----------------------------------------

im    : isMember        [name] []
    An operation which tests whether all the given items are members of the given set.

-----------------------------------------

l     : layer           [boolean] []
    OBSOLETE. DO NOT USE.

-----------------------------------------

mr    : minimizeRotation [boolean] ['query', 'edit']
    This flag only affects the attribute contained in the immediate keyingGroup. It does not affect attributes in sub-keyingGroups. Those will need to set minimizeRotation on their respective keyingGroups

-----------------------------------------

n     : name            [string] []
    Assigns string as the name for a new set. This flag is only valid for operations that create a new set.

-----------------------------------------

nss   : noSurfaceShader [boolean] []
    If set is renderable, do not connect it to the default surface shader. Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.

-----------------------------------------

nw    : noWarnings      [boolean] []
    Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)

-----------------------------------------

no    : nodesOnly       [boolean] ['query']
    This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.

-----------------------------------------

rm    : remove          [name] ['edit']
    Removes the list of items from the given set.

-----------------------------------------

rac   : removeActivator [name] ['edit']
    Removes the selected node(s) as activators for the given keying group.

-----------------------------------------

r     : renderable      [boolean] ['query']
    This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use in creation or query mode only. The default value is false which means a normal set is created.

-----------------------------------------

fil   : setActiveFilter [string] ['query', 'edit']
    Sets the global, active keying group filter, which will affect activation of keying groups. Only keying groups with categories that match the filter will be activated. If the setActiveFilter is set to "NoKeyingGroups", keying groups will not be activated at all. If the setActiveFilter is set to "AllKeyingGroups", we will activate any keying group rather than just those with matching categories.

-----------------------------------------

s     : size            [boolean] ['query']
    Use the size flag to query the length of the set.

-----------------------------------------

sp    : split           [name] []
    Produces a new set with the list of items and removes each item in the list of items from the given set.

-----------------------------------------

sub   : subtract        [name] []
    An operation between two sets which returns the members of the first set that are not in the second set.

-----------------------------------------

t     : text            [string] ['query', 'edit']
    Defines an annotation string to be stored with the set.

-----------------------------------------

un    : union           [name] []
    An operation that returns a list of all the members of all sets listed.

-----------------------------------------

v     : vertices        [boolean]
    Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.

    """

def keyTangent(q=1,e=1,a=1,an="string",at="string",cp=1,f="floatrange",g=1,hi="string",ia="angle",itt="string",iw="float",iub=1,index="uint",ix="float",iy="float",l=1,oa="angle",ott="string",ow="float",ox="float",oy="float",ptt="string",r=1,s=1,sa=1,t="timerange",uni=1,wl=1,wt=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyTangent.html



-----------------------------------------

keyTangent is undoable, queryable, and editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command edits or queries tangent properties of keyframes in a keyset. It
is also used to edit or query the default tangent type of newly created
keyframes (see the setKeyframe command for more information on how to override
this default).

Tangents help manage the shape of the animation curve and affect the
interpolation between keys. The tangent angle specifies the direction the
curve will take as it leaves (or enters) a key. The tangent weight specifies
how much influence the tangent angle has on the curve before the curve starts
towards the next key.

Maya internally represents tangents as x and y values. Refer to the API
documentation for MFnAnimCurve for a description of the relationship between
tangent angle and weight and the internal x and y values.


-----------------------------------------


Return Value:

int  Number of curves on which tangents were modified.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] ['edit']
    Changes to tangent positions are NOT relative to the current position.

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

g     : g               [boolean] []
    Required for all operations on the global tangent type. The global tangent type is used by the setKeyframe command when tangent types have not been specifically applied, except in combination with flags such as 'i/insert' which preserve the shape of the curve. It is also used when keys are set from the menu. The only flags that can appear on a keyTangent command with the 'g/global' flag are 'itt/inTangentType', 'ott/outTangentType' and 'wt/weightedTangents'.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

ia    : inAngle         [angle] ['query', 'edit']
    New value for the angle of the in-tangent. Returns a float[] when queried.

-----------------------------------------

itt   : inTangentType   [string] ['query', 'edit']
    Specify the in-tangent type. Valid values are "spline," "linear," "fast," "slow," "flat," "step," "stepnext," "fixed," "clamped," "plateau" and "auto". Returns a string[] when queried.

-----------------------------------------

iw    : inWeight        [float] ['query', 'edit']
    New value for the weight of the in-tangent. Returns a float[] when queried.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

ix    : ix              [float] ['query', 'edit']
    New value for the x-component of the in-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.

-----------------------------------------

iy    : iy              [float] ['query', 'edit']
    New value for the y-component of the in-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.

-----------------------------------------

l     : lock            [boolean] ['query', 'edit']
    Lock a tangent so in and out tangents move together. Returns an int[] when queried.

-----------------------------------------

oa    : outAngle        [angle] ['query', 'edit']
    New value for the angle of the out-tangent. Returns a float[] when queried.

-----------------------------------------

ott   : outTangentType  [string] ['query', 'edit']
    Specify the out-tangent type. Valid values are "spline," "linear," "fast," "slow," "flat," "step," "stepnext," "fixed," "clamped," "plateau" and "auto". Returns a string[] when queried.

-----------------------------------------

ow    : outWeight       [float] ['query', 'edit']
    New value for the weight of the out-tangent. Returns a float[] when queried.

-----------------------------------------

ox    : ox              [float] ['query', 'edit']
    New value for the x-component of the out-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.

-----------------------------------------

oy    : oy              [float] ['query', 'edit']
    New value for the y-component of the out-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.

-----------------------------------------

ptt   : pluginTangentTypes [string] ['query']
    Returns a list of the plug-in tangent types that have been loaded. Return type is a string array.

-----------------------------------------

r     : relative        [boolean] ['edit']
    Changes to tangent positions are relative to the current position.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

sa    : stepAttributes  [boolean] ['edit']
    The setKeyframe command will automatically set tangents for boolean and enumerated attributes to step. This flag mirrors this behavior for the keyTangent command. When set to false, tangents for these attributes will not be edited. When set to true (the default) tangents for these attributes will be edited.

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

uni   : unify           [boolean] ['edit']
    Unify a tangent so in and out tangents are equal and move together.

-----------------------------------------

wl    : weightLock      [boolean] ['query', 'edit']
    Lock the weight of a tangent so it is fixed. Returns an int[] when queried. Note: weightLock is only obeyed within the graph editor. It is not obeyed when -inWeight/-outWeight are issued from a command.

-----------------------------------------

wt    : weightedTangents [boolean]
    Specify whether or not the tangents on the animCurve are weighted Note: switching a curve from weightedTangents true to false and back to true again will not preserve fixed tangents properly. Use undo instead.

    """

def listAnimatable(act=1,m=1,mh=1,s=1,typ=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listAnimatable.html



-----------------------------------------

listAnimatable is undoable, NOT queryable, and NOT editable.

This command list the animatable attributes of a node. Command flags allow
filtering by the current manipulator, or node type.


-----------------------------------------


Return Value:

string[]  All animatable attributes found


-----------------------------------------


Flags:

-----------------------------------------

act   : active          [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

m     : manip           [boolean] []
    Return only those attributes affected by the current manip. If there is no manip active and any other flags are specified, output is the same as if the "-manip" flag were not present.

-----------------------------------------

mh    : manipHandle     [boolean] []
    Return only those attributes affected by the current manip handle. If there is no manip handle active and any other flags are specified, output is the same as if the "-manipHandle" flag were not present.

-----------------------------------------

s     : shape           [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

typ   : type            [boolean]
    Instead of returning attributes, Return the types of nodes that are currently animatable.

    """

def marker(q=1,e=1,a=1,d=1,ft="angle",om=1,pm=1,st="angle",t="time",ut="angle",u="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/marker.html



-----------------------------------------

marker is undoable, queryable, and editable.

The marker command creates one or two markers, on a motion path curve, at the
specified time and location. The optionnal string argument is the parent
object name.  

One can specify "-pm -om" option to create both, a position marker and an
orientation marker.  

Since there is only one keyframe for each marker of the same type, no more
than one marker of the same type with the same time value can exist.  

The default marker type is the position marker. The default time is the
current time.


-----------------------------------------


Return Value:

string[]  (name of the created markers)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : attach          [boolean] []
    This flag specifies to attach the selected 3D position markers to their parent geometry.

-----------------------------------------

d     : detach          [boolean] []
    This flag specifies to detach the selected position markers from their parent geometry to the 3D space.

-----------------------------------------

ft    : frontTwist      [angle] ['query']
    This flag specifies the amount of twist angle about the front vector for the marker.   Default is 0.   When queried, this flag returns a angle.

-----------------------------------------

om    : orientationMarker [boolean] ['query']
    This flag specifies creation of an orientation marker.   Default is not set..   When queried, this flag returns a boolean.

-----------------------------------------

pm    : positionMarker  [boolean] ['query']
    This flag specifies creation of a position marker.   Default is set.   When queried, this flag returns a boolean.

-----------------------------------------

st    : sideTwist       [angle] ['query']
    This flag specifies the amount of twist angle about the side vector for the marker.   Default is 0.   When queried, this flag returns a angle.

-----------------------------------------

t     : time            [time] ['query']
    This flag specifies the time for the marker.   Default is the current time.   When queried, this flag returns a time.

-----------------------------------------

ut    : upTwist         [angle] ['query']
    This flag specifies the amount of twist angle about the up vector for the marker.   Default is 0.   When queried, this flag returns a angle.

-----------------------------------------

u     : valueU          [float]
    This flag specifies the location of the position marker w.r.t. the parent geometry u parameterization.   Default is the value at current time.   When queried, this flag returns a linear.

    """

def movieInfo(cn=1,df=1,f=1,fd=1,h=1,mt=1,nt=1,nf=1,qt=1,tc=1,tt=1,ts=1,tf=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/movieInfo.html



-----------------------------------------

movieInfo is NOT undoable, NOT queryable, and NOT editable.

movieInfo provides a mechanism for querying information about movie files.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cn    : counter         [boolean] []
    Query the 'counter' flag of the movie's timecode format. If this is true, the timecode returned by the -timeCode flag will be a simple counter. If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).

-----------------------------------------

df    : dropFrame       [boolean] []
    Query the 'drop frame' flag of the movie's timecode format.

-----------------------------------------

f     : frameCount      [boolean] []
    Query the number of frames in the movie file

-----------------------------------------

fd    : frameDuration   [boolean] []
    Query the frame duration of the movie's timecode format.

-----------------------------------------

h     : height          [boolean] []
    Query the height of the movie

-----------------------------------------

mt    : movieTexture    [boolean] []
    If set, the string argument is interpreted as the name of a movie texture node, and the command then operates on the movie loaded by that node.

-----------------------------------------

nt    : negTimesOK      [boolean] []
    Query the 'neg times OK' flag of the movie's timecode format.

-----------------------------------------

nf    : numFrames       [boolean] []
    Query the whole number of frames per second of the movie's timecode format.

-----------------------------------------

qt    : quickTime       [boolean] []
    Query whether the movie is a QuickTime movie.

-----------------------------------------

tc    : timeCode        [boolean] []
    Query the timecode of the current movie frame.

-----------------------------------------

tt    : timeCodeTrack   [boolean] []
    Query whether the movie has a timecode track.

-----------------------------------------

ts    : timeScale       [boolean] []
    Query the timescale of the movie's timecode format.

-----------------------------------------

tf    : twentyFourHourMax [boolean] []
    Query the '24 hour max' flag of the movie's timecode format.

-----------------------------------------

w     : width           [boolean]
    Query the width of the movie

    """

def mute(q=1,d=1,f=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/mute.html



-----------------------------------------

mute is undoable, queryable, and NOT editable.

The mute command is used to disable and enable playback on a channel. When a
channel is muted, it retains the value that it was at prior to being muted.


-----------------------------------------


Return Value:

string[]  Name(s) of the mute node(s)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : disable         [boolean] []
    Disable muting on the channels

-----------------------------------------

f     : force           [boolean]
    Forceable disable of muting on the channels. If there are keys on the mute channel, the animation and mute node will both be removed. If this flag is not set, then mute nodes with animation will only be disabled.

    """

def pairBlend(q=1,e=1,at="string",i1=1,i2=1,nd="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pairBlend.html



-----------------------------------------

pairBlend is undoable, queryable, and editable.

The pairBlend node allows a weighted combinations of 2 inputs to be blended
together. It is created automatically when keying or constraining an attribute
which is already connected.

Alternatively, the pairBlend command can be used to connect a pairBlend node
to connected attributes of a node. The previously existing connections are
rewired to input1 of the pairBlend node. Additional connections can then be
made manually to input2 of the pairBlend node.

The pairBlend command can also be used to query the inputs to an existing
pairBlend node.


-----------------------------------------


Return Value:

string  name of pairBlend node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    The name of the attribute(s) which the blend will drive. This flag is required when creating the blend.

-----------------------------------------

i1    : input1          [boolean] ['query']
    Returns a string array of the node(s) connected to input 1.

-----------------------------------------

i2    : input2          [boolean] ['query']
    Returns a string array of the node(s) connected to input 2.

-----------------------------------------

nd    : node            [string]
    The name of the node which the blend will drive. This flag is required when creating the blend.

    """

def pasteKey(q=1,e=1,al="string",an="string",at="string",cb="string",c=1,cp="uint",f="floatrange",fo="float",iub=1,index="uint",mn=1,o="string",t="timerange",to="time",vo="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pasteKey.html



-----------------------------------------

pasteKey is undoable, queryable, and editable.

The pasteKey command pastes curve segment hierarchies from the clipboard onto
other objects or curves. If the object hierarchy from which the curve segments
were copied or cut does not match the object hierarchy being pasted to,
pasteKey will paste as much as it can match in the hierarchy. If animation
from only one object is on the clipboard, it will be pasted to each of the
target objects. If animation from more than one object is on the clipboard,
selection list order determines what animation is pasted to which object.

Valid operations include:

  * One attribute to one or more attributes (Clipboard animation is pasted onto all target attributes.

  * One attribute to one or more objects (Clipboard animation pasted onto target object, when attribute names match.)

  * Many attributes to one or more objects

  * Clipboard animation pasted onto targets when attribute names match.

TbaseKeySetCmd.h

The way the keyset clipboard will be pasted to the specified object's
attributes depends on the paste "-option" specified. Each of these options
below will be explained using an example. For all the explanations, let us
assume that there is a curve segment with 20 frames of animation on the keyset
clipboard (you can put curve segments onto the clipboard using the cutKey or
copyKey commands). We will call the animation curve that we are pasting to the
target curve:

  * pasteKey -time 5 -option insert  
1\. Shift all keyframes on the target curve after time 5 to the right by 20
frames (to make room for the 20-frame clipboard segment).  
2\. Paste the 20-frame clipboard segment starting at time 5.

  * pasteKey -time "5:10" -option replace   
1\. Remove all keys on the target curve from 5 to 10.  
2\. Paste the 20-frame clipboard curve at time 5. Keys from frame 11-25 will
be overridden if a key is present on the clipboard curve.

  * pasteKey -option replaceCompletely   
1\. Remove all keys on the target curve.  
2\. Paste the 20-frame clipboard curve, preserving the clipboard curve's
original keyframe times.

  * pasteKey -time 5 -option merge   
1.The clipboard curve segment will be pasted starting at time 5 for its full
20-frame range until frame 25.  
2\. If a keyframe on the target curve has the same time as a keyframe on the
clipboard curve, it is overwritten. Otherwise, any keys that existed in the
5:25 range before the paste, will remain untouched

  * pasteKey -time "3:10" -option scaleInsert   
1\. Shift all keyframes on the target curve after time 3 to the right by 7
frames (to clear the range 3:10 to paste in)  
2\. The clipboard curve segment will be scaled to fit the specified time range
(i.e. the 20 frames on the clipboard will be scaled to fit into 7 frames), and
then pasted into the range 3:10.

  * pasteKey -time "3:10" -option scaleReplace   
1\. Any existing keyframes in the target curve in the range 3:10 are removed.  
2\. The clipboard curve segment will be scaled to fit the specified time range
(i.e. the 20 frames on the clipboard will be scaled to fit into 7 frames), and
then pasted into the range 3:10.

  * pasteKey -time "3:10" -option scaleMerge   
1\. The clipboard curve segment will be scaled to fit the specified time range
(i.e. the 20 frames on the clipboard will be scaled to fit into 7 frames).  
2\. If there are keys on the target curve at the same time as keys on the
clipboard curve, they are overwritten. Otherwise, keyframes on the target
curve that existed in the 3:10 range before the paste, will remain untouched.

  * pasteKey -time "3:10" -option fitInsert   
1\. Shift all the keyframes on the target curve after time 3 to the right by 7
frames (to clear the range 3:10 to paste in)  
2\. The first 7 frames of the clipboard curve segment will be pasted into the
range 3:10.

  * pasteKey -time "3:10" -option fitReplace   
1\. Any existing frames in the target curve in the range 3:10 are removed.  
2\. The first 7 frames of the clipboard curve segment will be pasted into the
range 3:10.

  * pasteKey -time "3:10" -option fitMerge   
1\. The first 7 frames of the clipboard curve segment will be pasted into the
range 3:10.  
2\. If there are keys on the target curve at the same time as keys on the
clipboard curve, they are overwritten. Otherwise, keyframes on the target
curve that existed in the 3:10 range before the paste, will remain untouched.


-----------------------------------------


Return Value:

int  The number of curves pasted    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : animLayer       [string] []
    Specifies that the keys getting pasted should be pasted onto curves on the specified animation layer.If that layer doesn't exist for the specified objects or attributes then the keys won't get pasted.

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cb    : clipboard       [string] []
    Specifies the clipboard from which animation is pasted. Valid clipboards are "api" and "anim". The default clipboard is: anim

-----------------------------------------

c     : connect         [boolean] []
    When true, connect the source curve with the destination curve's value at the paste time. (This has the effect of shifting the clipboard curve in value to connect with the destination curve.) False preserves the source curve's original keyframe values. Default is false.

-----------------------------------------

cp    : copies          [uint] []
    The number of times to paste the source curve.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

fo    : floatOffset     [float] []
    How much to offset the pasted keys in time (for non-time-input animation curves).

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

mn    : matchByName     [boolean] []
    When true, we will only paste onto items in the scene whose node and attribute names match up exactly with a corresponding item in the clipboard. No hierarchy information is used. Default is false, and in this case the usual matching by hierarchy occurs.

-----------------------------------------

o     : option          [string] []
    Valid values are "insert", "replace", "replaceCompletely", "merge", "scaleInsert," "scaleReplace", "scaleMerge", "fitInsert", "fitReplace", and "fitMerge". The default paste option is: "insert".

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

to    : timeOffset      [time] []
    How much to offset the pasted keys in time (for time-input animation curves).

-----------------------------------------

vo    : valueOffset     [float]
    How much to offset the pasted keys in value.

    """

def pathAnimation(q=1,e=1,b=1,bs="float",bt="angle",c="string",etu="time",eu="float",f=1,fa="string",fm=1,inverseFront=1,iu=1,n="string",stu="time",su="float",ua="string",un=1,wuo="name",wut="string",wu="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pathAnimation.html



-----------------------------------------

pathAnimation is undoable, queryable, and editable.

The pathAnimation command constructs the necessary graph nodes and their
interconnections for a motion path animation. Motion path animation requires a
curve and one or more other objects. During the animation, the objects will be
moved along the 3D curve or the curveOnSurface.

There are two ways to specify the moving objects:

  1. by explicitly specifying their names in the command line, or
  2. by making the objects selected (interactively, or through a MEL command).

Likewise, there are two ways to specify a motion curve:

  1. by explicitly specifying the name of the motion curve in the command line (i.e. using the -c curve_name option), or
  2. by selecting the moving objects first before selecting the motion curve. I.e. if the name of the motion curve is not provided in the command line, the curve will be taken to be the last selected object in the selection list.

When the end time is not specified: only one keyframe will be created either
at the current time, or at the specified start time.


-----------------------------------------


Return Value:

string  (name of the created motionPath node)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : bank            [boolean] ['query']
    If on, enable alignment of the up axis of the moving object(s) to the curvature of the path geometry.   Default is false.   When queried, this flag returns a boolean.

-----------------------------------------

bs    : bankScale       [float] ['query']
    This flag specifies a factor to scale the amount of bank angle.   Default is 1.0   When queried, this flag returns a float.

-----------------------------------------

bt    : bankThreshold   [angle] ['query']
    This flag specifies the limit of the bank angle.   Default is 90 degrees   When queried, this flag returns an angle.

-----------------------------------------

c     : curve           [string] ['query']
    This flag specifies the name of the curve for the path.   Default is NONE   When queried, this flag returns a string.

-----------------------------------------

etu   : endTimeU        [time] ['query']
    This flag specifies the ending time of the animation for the u parameter.   Default is NONE.   When queried, this flag returns a time.

-----------------------------------------

eu    : endU            [float] ['query']
    This flag specifies the ending value of the u parameterization for the animation.   Default is the end parameterization value of the curve.   When queried, this flag returns a linear.

-----------------------------------------

f     : follow          [boolean] ['query']
    If on, enable alignment of the front axis of the moving object(s).   Default is false.   When queried, this flag returns a boolean.

-----------------------------------------

fa    : followAxis      [string] ['query']
    This flag specifies which object local axis to be aligned to the tangent of the path curve.   Default is y   When queried, this flag returns a string.

-----------------------------------------

fm    : fractionMode    [boolean] ['query']
    If on, evaluation on the path is based on the fraction of length of the path curve.   Default is false.   When queried, this flag returns a boolean.

-----------------------------------------

inverseFront : inverseFront    [boolean] ['query']
    This flag specifies whether or not to align the front axis of the moving object(s) to the opposite direction of the tangent vector of the path geometry.   Default is false.   When queried, this flag returns a boolean.

-----------------------------------------

iu    : inverseUp       [boolean] ['query']
    This flag specifies whether or not to align the up axis of the moving object(s) to the opposite direction of the normal vector of the path geometry.   Default is false.   When queried, this flag returns a boolean.

-----------------------------------------

n     : name            [string] ['query']
    This flag specifies the name for the new motion path node. (instead of the default name)   When queried, this flag returns a string.

-----------------------------------------

stu   : startTimeU      [time] ['query']
    This flag specifies the starting time of the animation for the u parameter.   Default is the the current time.   When queried, this flag returns a time.

-----------------------------------------

su    : startU          [float] ['query']
    This flag specifies the starting value of the u parameterization for the animation.   Default is the start parameterization value of the curve.   When queried, this flag returns a linear.

-----------------------------------------

ua    : upAxis          [string] ['query']
    This flag specifies which object local axis to be aligned a computed up direction.   Default is z   When queried, this flag returns a string.

-----------------------------------------

un    : useNormal       [boolean] ['query', 'edit']
    This flag is now obsolete. Use -wut/worldUpType instead.

-----------------------------------------

wuo   : worldUpObject   [name] ['query', 'edit']
    Set the DAG object to use for worldUpType "object" and "objectrotation". See -wut/worldUpType for greater detail. The default value is no up object, which is interpreted as world space.

-----------------------------------------

wut   : worldUpType     [string] ['query', 'edit']
    Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "normal". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpObject is ignored. Finally, if the value is "normal" the upVector is aligned to the path geometry. The default worldUpType is "vector".

-----------------------------------------

wu    : worldUpVector   [[float, float, float]]
    Set world up vector. This is the vector in world coordinates that up vector should align with. See -wut/worldUpType for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.

    """

def play(q=1,f=1,ps=1,rec=1,s="string",st=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/play.html



-----------------------------------------

play is undoable, queryable, and NOT editable.

This command starts and stops playback. In order to change the frame range of
playback, see the playbackOptions command.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

f     : forward         [boolean] ['query']
    When true, play back the animation from the currentTime to the maximum of the playback range. When false, play back from the currentTime to the minimum of the playback range. When queried, returns an int.

-----------------------------------------

ps    : playSound       [boolean] ['query']
    Specify whether or not sound should be used during playback

-----------------------------------------

rec   : record          [boolean] ['query']
    enable the recording system and start one playback loop

-----------------------------------------

s     : sound           [string] ['query']
    Specify the sound node to be used during playback

-----------------------------------------

st    : state           [boolean] ['query']
    start or stop playing back

-----------------------------------------

w     : wait            [boolean]
    Wait till completion before returning control to command Window.

    """

def playbackOptions(q=1,e=1,aet="time",ast="time",ba=1,by="float",fps=1,l="string",mps="float",max="time",min="time",ps="float",v="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/playbackOptions.html



-----------------------------------------

playbackOptions is undoable, queryable, and editable.

This command sets/queries certain values associated with playback: looping
style, start/end times, etc. Only commands modifying the -minTime/maxTime, the
-animationStartTime/animationEndTime, or the -by value are undoable.


-----------------------------------------


Return Value:

string  or float Query of edited option.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aet   : animationEndTime [time] ['query', 'edit']
    Sets the end time of the animation. Query returns a float.

-----------------------------------------

ast   : animationStartTime [time] ['query', 'edit']
    Sets the start time of the animation. Query returns a float.

-----------------------------------------

ba    : blockingAnim    [boolean] ['query']
    All tangents playback as stepped so that animation can be viewed in pure pose-to-pose form

-----------------------------------------

by    : by              [float] ['query', 'edit']
    Increment between times viewed during playback. (Default 1.0)

-----------------------------------------

fps   : framesPerSecond [boolean] ['query']
    Queries the actual playback rate. Query returns a float.

-----------------------------------------

l     : loop            [string] ['query', 'edit']
    Controls if and how playback repeats. Valid values are "once," "continuous," and "oscillate." Query returns string.

-----------------------------------------

mps   : maxPlaybackSpeed [float] ['query', 'edit']
    Sets the desired maximum playback speed. Query returns a float. The maxPlaybackSpeed is only used by Maya when your playbackSpeed is 0 (play every frame). The maxPlaybackSpeed will clamp the maximum playback rate to prevent it from going more than a certain amount. A maxPlaybackSpeed of 0 will give free (unclamped) playback.

-----------------------------------------

max   : maxTime         [time] ['query', 'edit']
    Sets the end of the playback time range. Query returns a float.

-----------------------------------------

min   : minTime         [time] ['query', 'edit']
    Sets the start of the playback time range. Query returns a float.

-----------------------------------------

ps    : playbackSpeed   [float] ['query', 'edit']
    Sets the desired playback speed. Query returns a float.

-----------------------------------------

v     : view            [string]
    Controls how many modelling views update during playback. Valid values are "all" and "active". Query returns a string.

    """

def playblast(ae=1,cs="[string, string]",cc=1,co=1,csd=1,cf="string",c="string",epn="string",et="time",f="string",fo=1,fmt="string",fr="time",fp="int",h="int",ifz=1,os=1,osv=1,o=1,p="int",qlt="int",rfn=1,rao=1,ret="time",rf="string",rst="time",sqt=1,orn=1,s="string",st="time",toe=1,uts=1,v=1,w="int",wh="[int, int]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/playblast.html



-----------------------------------------

playblast is undoable, NOT queryable, and NOT editable.

This command playblasts the current playback range. Sound is optional.

Note that the playblast command registers a condition called "playblasting" so
that users can monitor whether playblasting is occurring. You may monitor the
condition using the API (MConditionMessage) or a script (scriptJob and
condition commands).


-----------------------------------------


Return Value:

string  Name of moviefile created.


-----------------------------------------


Flags:

-----------------------------------------

ae    : activeEditor    [boolean] []
    This flag will return the current model editor that would be used for playblast. It does not invoke playblast itself.

-----------------------------------------

cs    : cameraSetup     [[string, string]] []
    Information about camera setup. The first string defines a camera setup MEL procedure. The camera setup procedure will be invoked before executing a playblast. The second string argument which is used as a camera identifier and is appended to the root file name to specify the final output file name(s). The command will fail there is not a pair of strings supplied to the argument.

-----------------------------------------

cc    : clearCache      [boolean] []
    When true, all previous temporary playblast files will be deleted before the new playblast files are created and the remaining temporary playblast files will be deleted when the application quits. Any playblast files that were explicitly given a name by the user will not be deleted.

-----------------------------------------

co    : codecOptions    [boolean] []
    Brings up the OS specific dialog for setting playblast codec options, and does not run the playblast.

-----------------------------------------

csd   : combineSound    [boolean] []
    Combine the trax sounds into a single track. This might force a resampling of the sound if the sound paramters don't match up.

-----------------------------------------

cf    : completeFilename [string] []
    When set, this string specifies the exact name of the output image. In contrast with the -f/filename flag, -cf/completeFilename does not append any frame number or extension string at the end of the filename. Additionally, playblast will not delete the image from disk after it is displayed. This flag should not be used in conjunction with -f/filename.

-----------------------------------------

c     : compression     [string] []
    Specify the compression to use for the movie file. To determine which settings are available on your system, use the `playblast -options` command. This will display a system-specific dialog with supported compression formats.   When the 'format' flag is 'image', this flag is used to pass in the desired image format. If the format is 'image' and the compression flag is ommitted, the output format specified via the Render Globals preference (see -format) will be used. If compression is set to 'none', the iff image format will be used.

-----------------------------------------

epn   : editorPanelName [string] []
    This optional flag specifies the name of the model editor or panel, which is to be used for playblast. The current model editor or panel won't be used for playblast unless its name is specified. Flag usage is specific to invoking playblast.

-----------------------------------------

et    : endTime         [time] []
    Specify the end time of the playblast. Default is the end time of the playback range displayed in the Time Slider. Overridden by -frame.

-----------------------------------------

f     : filename        [string] []
    The filename to use for the output of this playblast. If the file already exists, a confirmation box will be displayed if playblast is performed interactively. If playblast is executed from the command line and the file already exists, it will abort.

-----------------------------------------

fo    : forceOverwrite  [boolean] []
    Overwrite existing playblast files which may have the the same name as the one specified with the "-f" flag

-----------------------------------------

fmt   : format          [string] []
    The format for the playblast output.   | Value| Description

-----------------------------------------

fr    : frame           [time] []
    List of frames to blast. One frame specified per flag. The frames can be specified in any order but will be output in an ordered sequence. When specified this flag will override any start/end range

-----------------------------------------

fp    : framePadding    [int] []
    Number of zeros used to pad file name. Typically set to 4 to support fcheck.

-----------------------------------------

h     : height          [int] []
    Height of the final image. This value will be clamped if larger than the width of the active window.   Windows: If not using fcheck, the width and height must each be divisible by 4.

-----------------------------------------

ifz   : indexFromZero   [boolean] []
    Output frames starting with file.0000.ext and incrementing by one. Typically frames use the Maya time as their frame number. This option can only be used for frame based output formats.

-----------------------------------------

os    : offScreen       [boolean] []
    When set, this toggle allow playblast to use an offscreen buffer to render the view. This allows playblast to work when the application is iconified, or obscured.

-----------------------------------------

osv   : offScreenViewportUpdate [boolean] []
    When set, this toggle allows playblast to update the viewport while rendering with the offscreen buffer.

-----------------------------------------

o     : options         [boolean] []
    Brings up a dialog for setting playblast options, and does not run the playblast.

-----------------------------------------

p     : percent         [int] []
    Percentage of current view size to use during blasting. Accepted values are integers between 10 and 100. All other values are clamped to be within this range. A value of 25 means 1/4 of the current view size; a value of 50 means half the current view size; a value of 100 means full size. (Default is 50.)

-----------------------------------------

qlt   : quality         [int] []
    Specify the compression quality factor to use for the movie file. Value should be in the 0-100 range

-----------------------------------------

rfn   : rawFrameNumbers [boolean] []
    Playblast typically numbers its frames sequentially, starting at zero. This flag will override the default action and frames will be numbered using the actual frames specified by the -frame or -startFrame/-endFrame flags.

-----------------------------------------

rao   : replaceAudioOnly [boolean] []
    When set, this string dictates that only the audio will be replaced when the scene is re-playblasted.

-----------------------------------------

ret   : replaceEndTime  [time] []
    Specify the end time of a replayblast of an existing playblast. Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.

-----------------------------------------

rf    : replaceFilename [string] []
    When set, this string specifies the name of an input playblast file which will have frames replaced according to the replace start and end times.

-----------------------------------------

rst   : replaceStartTime [time] []
    Specify the start time of a replayblast of an existing playblast. Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.

-----------------------------------------

sqt   : sequenceTime    [boolean] []
    Use sequence time

-----------------------------------------

orn   : showOrnaments   [boolean] []
    Sets whether or not model view ornaments (e.g. the axis icon) should be displayed

-----------------------------------------

s     : sound           [string] []
    Specify the sound node to be used during playblast

-----------------------------------------

st    : startTime       [time] []
    Specify the start time of the playblast. Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.

-----------------------------------------

toe   : throwOnError    [boolean] []
    Playblast is tolerant of failures in most situations. When set, this toggle allows playblast to throw an error on these failures.

-----------------------------------------

uts   : useTraxSounds   [boolean] []
    Use sounds from TRAX.

-----------------------------------------

v     : viewer          [boolean] []
    Specify whether a viewer should be launched for the playblast. Default is "true". Runs "fcheck" when -fmt is "image". The player for movie files depends on the OS: Windows uses Microsoft Media Player, Irix uses movieplayer, OSX uses QuickTime.

-----------------------------------------

w     : width           [int] []
    Width of the final image. This value will be clamped if larger than the width of the active window.   Windows: If not using fcheck, the width and height must each be divisible by 4.

-----------------------------------------

wh    : widthHeight     [[int, int]]
    Final image's width and height. Values larger than the dimensions of the active window are clamped. A width and height of 0 means to use the window's current size.   Windows: If not using fcheck, the width and height must each be divisible by 4.

    """

def pose(q=1,e=1,ap=1,a=1,n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pose.html



-----------------------------------------

pose is undoable, queryable, and editable.

This command is used to create character poses.


-----------------------------------------


Return Value:

string  Pose name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : allPoses        [boolean] ['query']
    This flag is used to query all the poses in the scene.

-----------------------------------------

a     : apply           [boolean] []
    This flag is used in conjunction with the name flag to specify a pose should be applied to the character.

-----------------------------------------

n     : name            [string]
    In create mode, specify the pose name. In query mode, return a list of all the poses for the character. In apply mode, specify the pose to be applied.

    """

def rotationInterpolation(q=1,c="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rotationInterpolation.html



-----------------------------------------

rotationInterpolation is undoable, queryable, and NOT editable.

The rotationInterpolation command converts the rotation curves to the desired
rotation interpolation representation. For example, an Euler-angled
representation can be converted to Quaternion.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : convert         [string]
    Specifies the rotation interpolation mode for the curves after converting. Possible choices are "none" (unsynchronized Euler-angled curves which are compatible with pre-4.0 Maya curves), "euler" (Euler-angled curves with keyframes kept synchronized), "quaternion" (quaternion curves with keyframes kept synchronized, but the exact interpolation depends on individual tangents), "quaternionSlerp" (applies quaternion slerp interpolation to the curve, ignoring tangent settings), "quaternionSquad" (applied cubic interpolation to the curve in quaternion space, ignoring tangent settings)

    """

def scaleKey(an="string",at="string",cp=1,f="floatrange",fp="float",fs="float",hi="string",iub=1,index="uint",nef="float",net="time",nsf="float",nst="time",ssk=1,s=1,t="timerange",tp="time",ts="float",vp="float",vs="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scaleKey.html



-----------------------------------------

scaleKey is undoable, NOT queryable, and NOT editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command takes keyframes at (or within) the specified times (or time
ranges) and scales them. If no times are specified, the scale is applied to
active keyframes or (if no keys are active) all keys of active objects.


-----------------------------------------


Return Value:

int  Number of curves on which scale was performed


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

fp    : floatPivot      [float] []
    Scale pivot along the x-axis for float-input animCurves

-----------------------------------------

fs    : floatScale      [float] []
    Amount of scale along the x-axis for float-input animCurves

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

nef   : newEndFloat     [float] []
    The end of the float range to which the float-input targets should be scaled.

-----------------------------------------

net   : newEndTime      [time] []
    The end of the time range to which the targets should be scaled.

-----------------------------------------

nsf   : newStartFloat   [float] []
    The start of the float range to which the float-input targets should be scaled.

-----------------------------------------

nst   : newStartTime    [time] []
    The start of the time range to which the time-input targets should be scaled.

-----------------------------------------

ssk   : scaleSpecifiedKeys [boolean] []
    Determines if only the specified keys are affected by the scale. If false, other keys may be adjusted with the scale. The default is true.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

tp    : timePivot       [time] []
    Scale pivot along the time-axis for time-input animCurves

-----------------------------------------

ts    : timeScale       [float] []
    Amount of scale along the time-axis for time-input animCurves

-----------------------------------------

vp    : valuePivot      [float] []
    Scale pivot along the value-axis

-----------------------------------------

vs    : valueScale      [float]
    Amount of scale along the value-axis

    """

def sequenceManager(q=1,e=1,asa="string",ata="string",cs="string",ct="time",lsa="string",lsh=1,mp="string",nd="string",ws="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sequenceManager.html



-----------------------------------------

sequenceManager is undoable, queryable, and editable.

The sequenceManager command manages sequences, shots, and their related
scenes.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

asa   : addSequencerAudio [string] []
    Add an audio clip to the sequencer by specifying a filename

-----------------------------------------

ata   : attachSequencerAudio [string] []
    Add an audio clip to the sequencer by specifying an audio node

-----------------------------------------

cs    : currentShot     [string] ['query']
    Returns the shot that is being used at the current sequence time.

-----------------------------------------

ct    : currentTime     [time] ['query']
    Set the current sequence time

-----------------------------------------

lsa   : listSequencerAudio [string] []
    List the audio clips added to the sequencer

-----------------------------------------

lsh   : listShots       [boolean] []
    List all the currently defined shots across all scene segments

-----------------------------------------

mp    : modelPanel      [string] ['query']
    Sets a dedicated modelPanel to be used as the panel that the sequencer will control.

-----------------------------------------

nd    : node            [string] ['query']
    Returns the SequenceManager node, of which there is only ever one.

-----------------------------------------

ws    : writableSequencer [string]
    Get the writable sequencer node. Create it if it doesn't exist.

    """

def setDrivenKeyframe(q=1,e=1,at="string",cp=1,cd="string",dn=1,dr=1,dv="float",hi="string",itt="string",i=1,ib=1,ott="string",s=1,v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setDrivenKeyframe.html



-----------------------------------------

setDrivenKeyframe is undoable, queryable, and editable.

This command sets a driven keyframe. A driven keyframe is similar to a regular
keyframe. However, while a standard keyframe always has an x-axis of time in
the graph editor, for a drivenkeyframe the user may choose any attribute as
the x-axis of the graph editor.  
  
For example, you can keyframe the emission of a faucet so that so that it
emits whenever the faucet handle is rotated around y. The faucet emission in
this example is called the driven attribute. The handle rotation is called the
driver. Once you have used setDrivenKeyframe to set up the relationship
between the emission and the rotation, you can go to the graph editor and
modify the relationship between the attributes just as you would modify the
animation curve on any keyframed object.  
  
In the case of an attribute driven by a single driver, the dependency graph is
connected like this:  
  
driver attribute ---> animCurve ---> driven attribute  
  
You can set driven keyframes with more than a single driver. The effects of
the multiple drivers are combined together by a blend node.


-----------------------------------------


Return Value:

int  Number of keyframes set.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    Attribute name to set keyframes on.

-----------------------------------------

cp    : controlPoints   [boolean] []
    Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.

-----------------------------------------

cd    : currentDriver   [string] ['query']
    Set the driver to be used for the current driven keyframe to the attribute passed as an argument.

-----------------------------------------

dn    : driven          [boolean] ['query']
    Returns list of driven attributes for the selected item.

-----------------------------------------

dr    : driver          [boolean] ['query']
    Returns list of available drivers for the attribute.

-----------------------------------------

dv    : driverValue     [float] []
    Value of the driver to use for this keyframe. Default value is the current value.

-----------------------------------------

hi    : hierarchy       [string] []
    Controls the objects this command acts on, relative to the specified (or active) target objects. Valid values are "above," "below," "both," and "none." Default is "hierarchy -query"

-----------------------------------------

itt   : inTangentType   [string] []
    The in tangent type for keyframes set by this command. Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext" Default is "keyTangent -q -g -inTangentType"

-----------------------------------------

i     : insert          [boolean] []
    Insert keys at the given time(s) and preserve the shape of the animation curve(s). Note: the tangent type on inserted keys will be fixed so that the curve shape can be preserved.

-----------------------------------------

ib    : insertBlend     [boolean] []
    If true, a pairBlend node will be inserted for channels that have nodes other than animCurves driving them, so that such channels can have blended animation. If false, these channels will not have keys inserted. If the flag is not specified, the blend will be inserted based on the global preference for blending animation.

-----------------------------------------

ott   : outTangentType  [string] []
    The out tangent type for keyframes set by this command. Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext". Default is "keyTangent -q -g -outTangentType"

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true

-----------------------------------------

v     : value           [float]
    Value to set the keyframe at. Default is the current value.

    """

def setInfinity(q=1,e=1,at="string",cp=1,hi="string",poi="string",pri="string",s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setInfinity.html



-----------------------------------------

setInfinity is undoable, queryable, and editable.

Set the infinity type before (after) a paramCurve's first (last) keyframe.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

poi   : postInfinite    [string] ['query']
    Set the infinity type after a paramCurve's last keyframe. Valid values are "constant", "linear", "cycle", "cycleRelative", "oscillate".

-----------------------------------------

pri   : preInfinite     [string] ['query']
    Set the infinity type before a paramCurve's first keyframe. Valid values are "constant", "linear", "cycle", "cycleRelative", "oscillate".

-----------------------------------------

s     : shape           [boolean]
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

    """

def setKeyframe(q=1,e=1,al="string",an=1,at="string",bd=1,c="string",cp=1,dd=1,f="float",hi="string",id=1,itt="string",i=1,ib=1,mr=1,nr=1,ott="string",rk=1,s=1,t="time",lw=1,v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setKeyframe.html



-----------------------------------------

setKeyframe is undoable, queryable, and editable.

This command creates keyframes for the specified objects, or the active
objects if none are specified on the command line.

The default time for the new keyframes is the current time. Override this
behavior with the "-t" flag on the command line.

The default value for the keyframe is the current value of the attribute for
which a keyframe is set. Override this behavior with the "-v" flag on the
command line.

When setting keyframes on animation curves that do not have "time" as an input
attribute (ie, they are unitless animation curves), use "-f/-float" to specify
the unitless value at which to set a keyframe.

The -time and -float flags may be combined in one command.

This command sets up Dependency Graph relationships for proper evaluation of a
given attribute at a given time.


-----------------------------------------


Return Value:

int  Number of keyframes set by this command.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : animLayer       [string] []
    Specifies that the new key should be placed in the specified animation layer. Note that if the objects being keyframed are not already part of the layer, this flag will be ignored.

-----------------------------------------

an    : animated        [boolean] []
    Add the keyframe only to the attribute(s) that have already a keyframe on. Default: false

-----------------------------------------

at    : attribute       [string] []
    Attribute name to set keyframes on.

-----------------------------------------

bd    : breakdown       [boolean] ['query', 'edit']
    Sets the breakdown state for the key. Default is false

-----------------------------------------

c     : clip            [string] []
    Specifies that the new key should be placed in the specified clip. Note that if the objects being keyframed are not already part of the clip, this flag will be ignored.

-----------------------------------------

cp    : controlPoints   [boolean] []
    Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.

-----------------------------------------

dd    : dirtyDG         [boolean] []
    Allow dirty messages to be sent out when a keyframe is set.

-----------------------------------------

f     : float           [float] []
    Float time at which to set a keyframe on float-based animation curves.

-----------------------------------------

hi    : hierarchy       [string] []
    Controls the objects this command acts on, relative to the specified (or active) target objects. Valid values are "above," "below," "both," and "none." Default is "hierarchy -query"

-----------------------------------------

id    : identity        [boolean] []
    Sets an identity key on an animation layer. An identity key is one that nullifies the effect of the anim layer. This flag has effect only when the attribute being keyed is being driven by animation layers.

-----------------------------------------

itt   : inTangentType   [string] []
    The in tangent type for keyframes set by this command. Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext" Default is "keyTangent -q -g -inTangentType"

-----------------------------------------

i     : insert          [boolean] []
    Insert keys at the given time(s) and preserve the shape of the animation curve(s). Note: the tangent type on inserted keys will be fixed so that the curve shape can be preserved.

-----------------------------------------

ib    : insertBlend     [boolean] []
    If true, a pairBlend node will be inserted for channels that have nodes other than animCurves driving them, so that such channels can have blended animation. If false, these channels will not have keys inserted. If the flag is not specified, the blend will be inserted based on the global preference for blending animation.

-----------------------------------------

mr    : minimizeRotation [boolean] []
    For rotations, ensures that the key that is set is a minimum distance away from the previous key. Default is false

-----------------------------------------

nr    : noResolve       [boolean] []
    When used with the -value flag, causes the specified value to be set directly onto the animation curve, without attempting to resolve the value across animation layers.

-----------------------------------------

ott   : outTangentType  [string] []
    The out tangent type for keyframes set by this command. Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext". Default is "keyTangent -q -g -outTangentType"

-----------------------------------------

rk    : respectKeyable  [boolean] []
    When used with the -attribute flag, prevents the keying of the non keyable attributes.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true

-----------------------------------------

t     : time            [time] []
    Time at which to set a keyframe on time-based animation curves.

-----------------------------------------

lw    : useCurrentLockedWeights [boolean] []
    If we are setting a key over an existing key, use that key tangent's locked weight value for the new locked weight value. Default is false

-----------------------------------------

v     : value           [float]
    Value at which to set the keyframe. Using the value flag will not cause the keyed attribute to change to the specified value until the scene re- evaluates. Therefore, if you want the attribute to update to the new value immediately, use the setAttr command in addition to setting the key.

    """

def setKeyframeBlendshapeTargetWts():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setKeyframeBlendshapeTargetWts.html



-----------------------------------------

setKeyframeBlendshapeTargetWts is undoable, NOT queryable, and NOT editable.

This command can be used to keyframe per-point blendshape target weights. It
operates on the currently selected objects as follows. When the base object is
selected, then the target weights are keyed for all targets. When only target
shapes are selected, then the weights for thoses targets are keyframed.


-----------------------------------------


Return Value:

int  number of vertices for which the targets weights are keyed
    """

def setKeyPath():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setKeyPath.html



-----------------------------------------

setKeyPath is undoable, NOT queryable, and NOT editable.

The setKeyPath command either creates or edits the path (a nurbs curve) based
on the current position of the selected object at the current time.


-----------------------------------------


Return Value:

string[]  (Names of the created curve node and motionPath node)
    """

def shot(q=1,e=1,aud="string",cl="string",cd="time",co="float",css=1,czo="time",c=1,cca=1,cc="string",ca=1,dca=1,dt=1,et="time",fav=1,f1=1,f10=1,f11=1,f12=1,f2=1,f3=1,f4=1,f5=1,f6=1,f7=1,f8=1,f9=1,hcs=1,hsc=1,ipv=1,la="string",lck=1,m=1,p=1,pi=1,pst="time",prt="time",s="float",sm=1,sqd="time",set="time",sst="time",sn="string",sd="time",st="time",trk="int",til="time",tit="int",tol="time",tot="int",ula=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shot.html



-----------------------------------------

shot is undoable, queryable, and editable.

Use this command to create a shot node or manipulate that node.


-----------------------------------------


Return Value:

string  Shot name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aud   : audio           [string] ['query', 'edit']
    Specify the audio clip for this shot. Audio can be linked to a shot to allow playback of specific sounds when that shot is being displayed in the Sequencer. Refer to the shot node's documentation for details on how audio is used by shots and the Sequencer.

-----------------------------------------

cl    : clip            [string] ['query', 'edit']
    The clip associated with this shot. This clip will be posted to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.

-----------------------------------------

cd    : clipDuration    [time] ['query', 'edit']
    Length of clip. This is used for the display of the clip indicator bar in the Sequencer.

-----------------------------------------

co    : clipOpacity     [float] ['query', 'edit']
    Opacity for the shot's clip, this value is assigned to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.

-----------------------------------------

css   : clipSyncState   [boolean] ['query', 'edit']
    The viewport synchronization status of the clip associated with this shot. Return values are, 0 = no clip associated with this shot 1 = clip is fully in sync with viewport, and frames are 1:1 with sequencer 2 = clip is partially in sync with viewport, movie may be scaled to match sequencer 3 = clip not in sync with viewport (i.e. could have scale/time/camera differences)

-----------------------------------------

czo   : clipZeroOffset  [time] ['query', 'edit']
    Specify which time of the clip corresponds to the beginning of the shot. This is used to properly align splitted clips.

-----------------------------------------

c     : copy            [boolean] ['query', 'edit']
    This flag is used to copy a shot to the clipboard. In query mode, this flag allows you to query what, if anything, has been copied into the shot clipboard.

-----------------------------------------

cca   : createCustomAnim [boolean] ['edit']
    Creates an animation layer and links the shot node's customAnim attr to the weight attr of the animation layer

-----------------------------------------

cc    : currentCamera   [string] ['query', 'edit']
    The camera associated with this shot. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.

-----------------------------------------

ca    : customAnim      [boolean] ['query']
    Returns the name of the animation layer node linked to this shot node's customAnim attr

-----------------------------------------

dca   : deleteCustomAnim [boolean] ['edit']
    Disconnects the animation layer from this shot's customAnim attr and deletes the animation layer node

-----------------------------------------

dt    : determineTrack  [boolean] ['query', 'edit']
    Determines an available track for the shot. Returns a new track number or the existing track number if the current track is available.

-----------------------------------------

et    : endTime         [time] ['query', 'edit']
    The shot end time in the Maya timeline. Changing the startTime will extend the duration of a shot.

-----------------------------------------

fav   : favorite        [boolean] ['query', 'edit']
    Make the shot a favorite. This is a UI indicator only to streamline navigation in the Sequencer panel

-----------------------------------------

f1    : flag1           [boolean] ['query', 'edit']
    User specified state flag 1/12 for this shot

-----------------------------------------

f10   : flag10          [boolean] ['query', 'edit']
    User specified state flag 10/12 for this shot

-----------------------------------------

f11   : flag11          [boolean] ['query', 'edit']
    User specified state flag 11/12 for this shot

-----------------------------------------

f12   : flag12          [boolean] ['query', 'edit']
    User specified state flag 12/12 for this shot

-----------------------------------------

f2    : flag2           [boolean] ['query', 'edit']
    User specified state flag 2/12 for this shot

-----------------------------------------

f3    : flag3           [boolean] ['query', 'edit']
    User specified state flag 3/12 for this shot

-----------------------------------------

f4    : flag4           [boolean] ['query', 'edit']
    User specified state flag 4/12 for this shot

-----------------------------------------

f5    : flag5           [boolean] ['query', 'edit']
    User specified state flag 5/12 for this shot

-----------------------------------------

f6    : flag6           [boolean] ['query', 'edit']
    User specified state flag 6/12 for this shot

-----------------------------------------

f7    : flag7           [boolean] ['query', 'edit']
    User specified state flag 7/12 for this shot

-----------------------------------------

f8    : flag8           [boolean] ['query', 'edit']
    User specified state flag 8/12 for this shot

-----------------------------------------

f9    : flag9           [boolean] ['query', 'edit']
    User specified state flag 9/12 for this shot

-----------------------------------------

hcs   : hasCameraSet    [boolean] ['query', 'edit']
    Returns true if the camera associated with this shot is a camera set.

-----------------------------------------

hsc   : hasStereoCamera [boolean] ['query', 'edit']
    Returns true if the camera associated with this shot is a stereo camera.

-----------------------------------------

ipv   : imagePlaneVisibility [boolean] ['query', 'edit']
    Visibility of the shot imageplane, this value is assigned to the currentCamera's imagePlane.

-----------------------------------------

la    : linkAudio       [string] ['query', 'edit']
    Specify an audio clip to link to this shot. Any currently linked audio will be unlinked.

-----------------------------------------

lck   : lock            [boolean] ['query', 'edit']
    Lock a specific shot. This is different than locking an entire track, which is done via the shotTrack command

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    Mute a specific shot. This is different than muting an entire track, which is done via the shotTrack command. Querying this attribute will return true if the shot is muted due to its own mute, its shot being muted, or its shot being unsoloed. See flag "selfmute" to query only the shot's own state.

-----------------------------------------

p     : paste           [boolean] ['query', 'edit']
    This flag is used to paste a shot or shots from the clipboard to the sequence timeline. Shots are added to the clipboard using the c/copy flag.

-----------------------------------------

pi    : pasteInstance   [boolean] ['query', 'edit']
    This flag is used to paste an instance of a shot or shots from the clipboard to the sequence timeline. Unlike the p/paste flag, which duplicates the camera and image plane from the original source shot, the pi/pasteInstance flag shares the camera and image plane from the source shot. The audio node is duplicated.

-----------------------------------------

pst   : postHoldTime    [time] ['query', 'edit']
    Specify the time length to append to the shot in the sequence timeline. This repeats the last frame of the shot, in sequence time, over the specified duration.

-----------------------------------------

prt   : preHoldTime     [time] ['query', 'edit']
    Specify the time length to prepend to the shot in the sequence timeline. This repeats the first frame of the shot, in sequence time, over the specified duration.

-----------------------------------------

s     : scale           [float] ['query', 'edit']
    Specify an amount to scale the Maya frame range of the shot. This will affect the sequenceEndFrame, leaving the sequenceStartFrame unchanged.

-----------------------------------------

sm    : selfmute        [boolean] ['query', 'edit']
    Query if this individual shot's own mute state is set. This is different from the flag "mute", which will return true if this shot is muted due to the track being muted or another track being soloed. Editing this flag will set this shot's own mute status (identical behavior as the flag "mute").

-----------------------------------------

sqd   : sequenceDuration [time] ['query', 'edit']
    Return the sequence duration of the shot, which will include the holds and scale. This flag can only be queried.

-----------------------------------------

set   : sequenceEndTime [time] ['query', 'edit']
    The shot end in the sequence timeline. Changing the endTime of a shot will scale it in sequence time.

-----------------------------------------

sst   : sequenceStartTime [time] ['query', 'edit']
    The shot start in the sequence timeline. Changing the startTime of a shot will shift it in sequence time.

-----------------------------------------

sn    : shotName        [string] ['query', 'edit']
    Specify a user-defined name for this shot. This allows the assignment of names that are not valid as node names within Maya. Whenever the shotName attribute is defined its value is used in the UI.

-----------------------------------------

sd    : sourceDuration  [time] ['query', 'edit']
    Return the number of source frames in the shot. This flag can only be queried.

-----------------------------------------

st    : startTime       [time] ['query', 'edit']
    The shot start time in the Maya timeline. Changing the startTime will extend the duration of a shot.

-----------------------------------------

trk   : track           [int] ['query', 'edit']
    Specify the track in which this shot resides.

-----------------------------------------

til   : transitionInLength [time] ['query', 'edit']
    Length of the transtion into the shot.

-----------------------------------------

tit   : transitionInType [int] ['query', 'edit']
    Specify the the type of transition for the transition into the shot. 0 = Fade 1 = Dissolve

-----------------------------------------

tol   : transitionOutLength [time] ['query', 'edit']
    Length of the transtion out of the shot.

-----------------------------------------

tot   : transitionOutType [int] ['query', 'edit']
    Specify the the type of transition for the transition out of the shot. 0 = Fade 1 = Dissolve

-----------------------------------------

ula   : unlinkAudio     [boolean]
    COMMENT Unlinks any currently linked audio.

    """

def shotRipple(q=1,e=1,d=1,ed="time",et="time",sd="time",st="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shotRipple.html



-----------------------------------------

shotRipple is undoable, queryable, and editable.

When Ripple Edit Mode is enabled, neighboring shots to the shot that gets
manipulated are moved in sequence time to either make way or close up gaps
corresponding to that node's editing. Given some parameters about the shot
edit that just took place, this command will choose which other shots to move,
and move them the appropriate amounts If no shot name is provided, the command
will attempt to use the first selected shot.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : deleted         [boolean] ['query', 'edit']
    Specify whether this ripple edit is due to a shot deletion

-----------------------------------------

ed    : endDelta        [time] ['query', 'edit']
    Specify the change in the end time in frames

-----------------------------------------

et    : endTime         [time] ['query', 'edit']
    Specify the initial shot end time in the sequence timeline.

-----------------------------------------

sd    : startDelta      [time] ['query', 'edit']
    Specify the change in the start time in frames

-----------------------------------------

st    : startTime       [time]
    Specify the initial shot start time in the sequence timeline.

    """

def simplify(an="string",at="string",cp=1,f="floatrange",ft="float",hi="string",iub=1,index="uint",s=1,t="timerange",tt="time",vt="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/simplify.html



-----------------------------------------

simplify is undoable, NOT queryable, and NOT editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command will simplify (reduce the number of keyframes) an animation
curve.


-----------------------------------------


Return Value:

int  Number of animation curves simplified


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

ft    : floatTolerance  [float] []
    Specify the x-axis tolerance (defaults to 0.05) for float-input animCurves such as those created by "Set Driven Keyframe". This flag is ignored on animCurves driven by time. Higher floatTolerance values will result in sparser keys which may less accurately represent the initial curve.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

tt    : timeTolerance   [time] []
    Specify the x-axis tolerance (defaults to 0.05 seconds) for time-input animCurves. This flag is ignored on animCurves driven by floats. Higher time tolerance values will result in sparser keys which may less accurately represent the initial curve.

-----------------------------------------

vt    : valueTolerance  [float]
    Specify the value tolerance (defaults to 0.01)

    """

def snapKey(an="string",at="string",cp=1,f="floatrange",hi="string",iub=1,index="uint",s=1,t="timerange",tm="float",vm="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/snapKey.html



-----------------------------------------

snapKey is undoable, NOT queryable, and NOT editable.

This command operates on a keyset. A keyset is defined as a group of keys
within a specified time range on one or more animation curves.

The animation curves comprising a keyset depend on the value of the
"-animation" flag:

  * keysOrObjects: 
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or

    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.

  * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything. 

  * objects: Only act on specified objects. If there are no objects specified, don't do anything. 

Note that the "-animation" flag can be used to override the curves uniquely
identified by the multi-use "-attribute" flag, which takes an argument of the
form attributeName, such as "translateX".

Keys on animation curves are identified by either their time values or their
indices. Times and indices can be given individually or as part of a list or
range (see Examples).

This command "snaps" all target key times and/or values so that they have
times and/or values that are multiples of the specified flag arguments. If
neither multiple is specified, default is time snapping with a multiple of
1.0. Note that this command will fail to move keys over other neighboring
keys: a key's index will not change as a result of a snapKey operation.

TbaseKeySetCmd.h


-----------------------------------------


Return Value:

int  Number of animation curves with keys that were not snapped because of
time-snapping conflicts.


-----------------------------------------


Flags:

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

f     : float           [floatrange] []
    value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")  In query mode, this flag needs a value.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

tm    : timeMultiple    [float] []
    If this flag is present, key times will be snapped to a multiple of the specified float value.

-----------------------------------------

vm    : valueMultiple   [float]
    If this flag is present, key values will be snapped to a multiple of the specified float value.

    """

def snapshot(q=1,e=1,ch=1,et="time",i="time",mt=1,n="string",st="time",u="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/snapshot.html



-----------------------------------------

snapshot is undoable, queryable, and editable.

This command can be used to create either a series of surfaces evaluated at
the times specified by the command flags, or a motion trail displaying the
trajectory of the object's pivot point at the times specified.

If the constructionHistory flag is true, the output shapes or motion trail
will re-update when modifications are made to the animation or construction
history of the original shape. When construction history is used, the
forceUpdate flag can be set to false to control when the snapshot recomputes,
which will typically improve performance.


-----------------------------------------


Return Value:

string[]  names of nodes created or edited: transform-name [snapshot-node-
name]    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    update with changes to original geometry

-----------------------------------------

et    : endTime         [time] ['query', 'edit']
    time to stop copying target geometry Default: 10.0

-----------------------------------------

i     : increment       [time] ['query', 'edit']
    time increment between copies Default: 1.0

-----------------------------------------

mt    : motionTrail     [boolean] []
    Rather than create a series of surfaces, create a motion trail displaying the location of the object's pivot point at the specified time steps. Default is false.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    the name of the snapshot node. Query returns string.

-----------------------------------------

st    : startTime       [time] ['query', 'edit']
    time to begin copying target geometry Default: 1.0

-----------------------------------------

u     : update          [string]
    This flag can only be used if the snapshot has constructionHistory. It sets the snapshot node's update value. The update value controls whether the snapshot updates on demand (most efficient), when keyframes change (efficient), or whenever any history changes (least efficient). Valid values are "demand", "animCurve", "always". Default: "always"

    """

def snapshotBeadCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",i=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/snapshotBeadCtx.html



-----------------------------------------

snapshotBeadCtx is undoable, queryable, and editable.

Creates a context for manipulating in and/or out tangent beads on the motion
trail


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

ch    : history         [boolean] []
    If this is a tool command, turn the construction history on for the tool in question.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string] ['query', 'edit']
    Third of three possible icons representing the tool associated with the context.

-----------------------------------------

i     : inTangent       [boolean] ['query', 'edit']
    Indicates that we will be showing beads for the in tangent when entering the context

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

o     : outTangent      [boolean]
    Indicates that we will be showing beads for the out tangent when entering the context

    """

def snapshotModifyKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/snapshotModifyKeyCtx.html



-----------------------------------------

snapshotModifyKeyCtx is undoable, queryable, and editable.

Creates a context for inserting/delete keys on an editable motion trail


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

ch    : history         [boolean] []
    If this is a tool command, turn the construction history on for the tool in question.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string] ['query', 'edit']
    Third of three possible icons representing the tool associated with the context.

-----------------------------------------

n     : name            [string]
    If this is a tool command, name the tool appropriately.

    """

def sound(q=1,e=1,et="time",f="string",l=1,m=1,n="string",o="time",se="time",ss="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sound.html



-----------------------------------------

sound is undoable, queryable, and editable.

Creates an audio node which can be used with UI commands such as soundControl
or timeControl which support sound scrubbing and sound during playback.


-----------------------------------------


Return Value:

string  Name of resulting audio node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

et    : endTime         [time] ['query', 'edit']
    Time at which to end the sound.

-----------------------------------------

f     : file            [string] ['query', 'edit']
    Name of sound file.

-----------------------------------------

l     : length          [boolean] ['query']
    Query the length (in the current time unit) of the sound.

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    Mute the audio clip.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name to give the resulting audio node.

-----------------------------------------

o     : offset          [time] ['query', 'edit']
    Time at which to start the sound.

-----------------------------------------

se    : sourceEnd       [time] ['query', 'edit']
    Time offset from the start of the sound file at which to end the sound.

-----------------------------------------

ss    : sourceStart     [time]
    Time offset from the start of the sound file at which to start the sound.

    """

def timeEditor(q=1,alc="string",id="int",cpt=1,cp="string",dca="string",dco="[string, int]",ip=1,m=1,sc="string",tlc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditor.html



-----------------------------------------

timeEditor is undoable, queryable, and NOT editable.

General Time Editor commands


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

alc   : allClips        [string] []
    Return an exhaustive (recursive) list of all clip IDs from the active composition. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:    * roster    * container    * group

-----------------------------------------

id    : clipId          [int] []
    ID of the clip to be edited.

-----------------------------------------

cpt   : commonParentTrack [boolean] []
    Locate the common parent track node and track index of the given clip IDs. Requires a list of clip IDs to be specified using the clipId flag. The format of the returned string is "track_node:track_index". If the clips specified are on the same track node but in different track indexes, only the track node will be returned.

-----------------------------------------

cp    : composition     [string] []
    A flag to use in conjunction with -dca/drivingClipsForObj to indicate the name of composition to use. By default if this flag is not provided, current active composition will be used.

-----------------------------------------

dca   : drivingClipsForAttr [string] []
    Return a list of clips driving the specified attribute(s). If the composition is not specified, current active composition will be used.

-----------------------------------------

dco   : drivingClipsForObj [[string, int]] []
    Return a list of clips driving the specified object(s) with an integer value indicating the matching mode. If no object is specified explicitly, the selected object(s) will be used. Objects that cannot be driven by clips are ignored. If the composition is not specified, current active composition will be used. Default match mode is 0.    * 0: Include only the clip that has an exact match   * 1: Include any clip that contains all of the specified objects   * 2: Include any clip that contains any of the specified objects   * 3: Include all clips that do not include any of the specified objects

-----------------------------------------

ip    : includeParent   [boolean] []
    A toggle flag to use in conjunction with -dca/drivingClipsForObj. When toggled, parent clip is included in selection (the entire hierarchy will be selected).

-----------------------------------------

m     : mute            [boolean] ['query']
    Mute/unmute Time Editor.

-----------------------------------------

sc    : selectedClips   [string] []
    Return a list of clip IDs of currently selected Time Editor clips. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:    * roster    * container    * group

-----------------------------------------

tlc   : topLevelClips   [string]
    Return a list of all top-level clip IDs from the active composition. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:    * roster    * container    * group

    """

def timeEditorAnimSource(q=1,e=1,asc="string",ap=1,bas="string",ct=1,cp=1,dc=1,ex="string",iu=1,rs="string",ti="string",trg=1,ao="string",akg=1,aso=1,at="string",exc=1,aft=1,fbx="string",ft="string",mf="string",io="string",ipo="string",icn="string",irt=1,pia="string",poc=1,rec=1,rsa=1,sar=1,tl="string",toi="string",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorAnimSource.html



-----------------------------------------

timeEditorAnimSource is undoable, queryable, and editable.

Commands for managing animation sources.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

asc   : addSource       [string] ['edit']
    Add single new target attribute with its animation.

-----------------------------------------

ap    : apply           [boolean] ['edit']
    Connect anim source's animation directly to the target objects. If the Time Editor is not muted, connect to scene storage instead.

-----------------------------------------

bas   : bakeToAnimSource [string] ['edit']
    Create a new anim source with the same animation as this anim source. All non-curve inputs will be baked down, whereas curve sources will be shared.

-----------------------------------------

ct    : calculateTiming [boolean] ['query', 'edit']
    Adjust start/duration when adding/removing sources. If query it returns the [start,duration] pair.

-----------------------------------------

cp    : copyAnimation   [boolean] ['edit']
    Copy animation when adding source.

-----------------------------------------

dc    : drivenClips     [boolean] ['query']
    Return all clips driven by the given anim source.

-----------------------------------------

ex    : export          [string] ['edit']
    Export given anim source and the animation curves to a specified Maya file.

-----------------------------------------

iu    : isUnique        [boolean] ['query']
    Return true if the anim source node is only driving a single clip.

-----------------------------------------

rs    : removeSource    [string] ['edit']
    Remove single attribute.

-----------------------------------------

ti    : targetIndex     [string] ['query']
    Get target index.

-----------------------------------------

trg   : targets         [boolean] ['query']
    Get a list of all targets in this anim source.

-----------------------------------------

ao    : addObjects      [string] ['query', 'edit']
    Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s). Similar to -addSelectedObjects flag but acts on given object(s) instead. This flag will override the flag -addSelectedObjects.

-----------------------------------------

akg   : addRelatedKG    [boolean] ['query', 'edit']
    During population, determine if associated keying groups should be populated or not. Normally used for populating HIK. By default the value is false.

-----------------------------------------

aso   : addSelectedObjects [boolean] ['query', 'edit']
    Populate the currently selected objects and their attributes to anim source or Time Editor. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.

-----------------------------------------

at    : attribute       [string] ['edit']
    Populate a specific attribute on a object.

-----------------------------------------

exc   : exclusive       [boolean] ['edit']
    Populate all types of animation sources which are not listed by "type" Flag.

-----------------------------------------

aft   : importAllFbxTakes [boolean] []
    Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

-----------------------------------------

fbx   : importFbx       [string] []
    Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).

-----------------------------------------

ft    : importFbxTakes  [string] []
    Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

-----------------------------------------

mf    : importMayaFile  [string] []
    Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

-----------------------------------------

io    : importOption    [string] ['edit']
    Option for importing animation source. Specify either 'connect' or 'generate'. connect: Only connect with nodes already existing in the scene. Importing an animation source that does not match with any element of the current scene will not create any clip. (connect is the default mode). generate: Import everything and generate new nodes for items not existing in the scene.

-----------------------------------------

ipo   : importPopulateOption [string] ['edit']
    Option for population when importing.

-----------------------------------------

icn   : importedContainerNames [string] []
    Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.

-----------------------------------------

irt   : includeRoot     [boolean] ['edit']
    Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.

-----------------------------------------

pia   : populateImportedAnimSources [string] []
    Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).

-----------------------------------------

poc   : poseClip        [boolean] []
    Populate as pose clip with current attribute values.

-----------------------------------------

rec   : recursively     [boolean] ['edit']
    Populate selection recursively, adding all the children.

-----------------------------------------

rsa   : removeSceneAnimation [boolean] ['edit']
    If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.

-----------------------------------------

sar   : showAnimSourceRemapping [boolean] []
    Show a remapping dialog when the imported anim source attributes do not match the scene attributes.

-----------------------------------------

tl    : takeList        [string] []
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.

-----------------------------------------

toi   : takesToImport   [string] []
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.

-----------------------------------------

typ   : type            [string]
    Only populate the specified type of animation source.

    """

def timeEditorBakeClips(q=1,e=1,bas="string",btc="string",id="int",cl=1,fs=1,koc=1,pt="string",sb="time",tti="int",ttn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorBakeClips.html



-----------------------------------------

timeEditorBakeClips is undoable, queryable, and editable.

This command is used to bake Time Editor clips and to blend them into a single
clip.


-----------------------------------------


Return Value:

int  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bas   : bakeToAnimSource [string] []
    Bake/merge the selected clips into the animation source.

-----------------------------------------

btc   : bakeToClip      [string] []
    Bake/merge the selected clips into a clip.

-----------------------------------------

id    : clipId          [int] []
    Clip IDs of the clips to bake.

-----------------------------------------

cl    : combineLayers   [boolean] []
    Combine the layers of the input clip.

-----------------------------------------

fs    : forceSampling   [boolean] []
    Force sampling on the whole time range when baking.

-----------------------------------------

koc   : keepOriginalClip [boolean] []
    Keep the source clips after baking.

-----------------------------------------

pt    : path            [string] []
    Full path of clips on which to operate. For example: composition1|track1|group; composition1|track1|group|track2|clip1.

-----------------------------------------

sb    : sampleBy        [time] []
    Sampling interval when baking crossfades and timewarps.

-----------------------------------------

tti   : targetTrackIndex [int] []
    Specify the target track when baking containers. If targetTrackIndex is specified, the track index within the specified node is used. If targetTrackIndex is not specified or is the default value (-1), the track index within the current node is used. If targetTrackIndex is -2, a new track will be created.

-----------------------------------------

ttn   : targetTracksNode [string]
    Target tracks node when baking containers.

    """

def timeEditorClip(q=1,e=1,abs=1,aa="string",eas=1,asr="string",au="string",chl="int",ca=1,cb=1,cdt=1,id="int",idn="int",idp=1,cln=1,clp=1,ccl=1,cfm="int",cfp=1,cvt="time",dgr=1,dat=1,dcs="string",dos=1,dro=1,dsc="string",dcl=1,d="time",ems=1,et="time",exo=1,exs=1,epl="int",eac=1,ef="string",ex=1,exp=1,gh=1,gra="string",grr="string",grp=1,he="time",hs="time",itd="int",ict=1,lug=1,le="time",ls="time",mcd=1,mas=1,mcl="time",m=1,n="string",p="int",pid="int",pgd=1,pcl="time",pt="string",pat=1,rcl="time",rmp="[string, string]",rs="[string, string]",rms=1,rmt=1,ra="string",rmc=1,rcf=1,rwc=1,rt=1,rtr=1,rpl=1,rti="int",rpt="string",sce="time",scp="time",scs="time",k="string",src="int",s="time",tw=1,twc=1,twt="int",trk="string",trn=1,tra=1,tre="time",trs="time",trc=1,uas=1,ugr=1,wc=1,zk=1,ao="string",akg=1,aso=1,at="string",exc=1,aft=1,fbx="string",ft="string",mf="string",io="string",ipo="string",icn="string",irt=1,pia="string",poc=1,rec=1,rsa=1,sar=1,tl="string",toi="string",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClip.html



-----------------------------------------

timeEditorClip is undoable, queryable, and editable.

This command edits/queries Time Editor clips.


-----------------------------------------


Return Value:

string  Return created clip's name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

abs   : absolute        [boolean] ['query']
    This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc. to query (global) absolute time.

-----------------------------------------

aa    : addAttribute    [string] ['edit']
    Add new attribute to the clip.

-----------------------------------------

eas   : allowShrinking  [boolean] ['edit']
    When extending clip, allow shrinking.

-----------------------------------------

asr   : animSource      [string] ['query', 'edit']
    Populate based on animation source.

-----------------------------------------

au    : audio           [string] []
    Create a clip with audio inside.

-----------------------------------------

chl   : children        [int] ['query']
    Get children clip IDs.

-----------------------------------------

ca    : clipAfter       [boolean] ['query']
    Get the clip ID of the next clip.

-----------------------------------------

cb    : clipBefore      [boolean] ['query']
    Get the clip ID of the previous clip.

-----------------------------------------

cdt   : clipDataType    [boolean] ['query']
    Query the type of data being driven by the given clip ID. Return values are:    * 0 : Animation - Clip drives animation curves   * 1 : Audio - Clip drives audio   * 3 : Group - Clip is a group

-----------------------------------------

id    : clipId          [int] ['edit']
    ID of the clip to be edited.

-----------------------------------------

idn   : clipIdFromNodeName [int] ['query']
    Get clip ID from clip node name.

-----------------------------------------

idp   : clipIdFromPath  [boolean] ['query']
    Flag for querying the clip ID given the path. Clip path is a vertical- bar-delimited string to indicate a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented. For example: composition1|track1|clip1 Note: To specify the path, this flag must appear before -query flag.

-----------------------------------------

cln   : clipNode        [boolean] ['query']
    Flag for querying the name of the clip node.

-----------------------------------------

clp   : clipPath        [boolean] ['query']
    Flag for querying the path given the clip ID. Clip path is a vertical bar delimited string to indicate a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented. For example: composition1|track1|clip1. Note: If the clip is not connected to any track, it will return empty string.

-----------------------------------------

ccl   : copyClip        [boolean] ['edit']
    Get the selected clip IDs and store them in a list that could be used for pasting.

-----------------------------------------

cfm   : crossfadeMode   [int] ['query', 'edit']
    Set the crossfading mode between two clips that lie on the same track, and that are specified with the -clipId flags:    * 0 : linear - Two clips are blended with a constant ratio   * 1 : step - Left clip keeps its value until the middle of the crossfading region and then right clip's value is used   * 2 : hold left - Use only left clip's value   * 3 : hold right - Use only right clip's value   * 4 : custom - User defined crossfade curve   * 5 : custom (spline) - User defined crossfade curve with spline preset

-----------------------------------------

cfp   : crossfadePlug   [boolean] ['query']
    Get plug path for a custom crossfade curve between 2 clips.

-----------------------------------------

cvt   : curveTime       [time] ['query']
    Query the curve local time in relation to the given clip.

-----------------------------------------

dgr   : defaultGhostRoot [boolean] ['query', 'edit']
    Edit or query default ghost root variable. Determine whether to use the default ghost root (object driven by clip).

-----------------------------------------

dat   : drivenAttributes [boolean] ['query']
    Return a list of attributes driven by a clip.

-----------------------------------------

dcs   : drivenClipsBySource [string] ['query']
    Returns the clips driven by the given source. Can filter the return result by the specified type, like animCurve, expression, constraint, etc. This flag must come before the -query flag.

-----------------------------------------

dos   : drivenObjects   [boolean] ['query']
    Return an array of strings consisting of the names of all objects driven by the current clip and its children clips.

-----------------------------------------

dro   : drivenRootObjects [boolean] ['query']
    Return an array of strings consisting of the names of all root objects driven by this clip and its children clips.

-----------------------------------------

dsc   : drivingSources  [string] ['query']
    Return all sources driving the given clip. Can filter the return result by the specified type, like animCurve, expression, constraint, etc. If used after the -query flag (without an argument), the command returns all sources driving the given clip. To specify the type, this flag must appear before the -query flag.  In query mode, this flag can accept a value.

-----------------------------------------

dcl   : duplicateClip   [boolean] ['edit']
    Duplicate clip into two clips with the same timing info.

-----------------------------------------

d     : duration        [time] ['query']
    Relative duration of the new clip.

-----------------------------------------

ems   : emptySource     [boolean] []
    Create a clip with an empty source.

-----------------------------------------

et    : endTime         [time] ['query']
    Query the relative end time of the clip.

-----------------------------------------

exo   : existingOnly    [boolean] ['edit']
    This flag can only be used in edit mode, in conjunction with the animSource flag. Retain the animSource flag functionality but only bind attributes that are already part of the clip. It does not attempt to populate unbound source attributes to their default destination.

-----------------------------------------

exs   : exists          [boolean] ['query']
    Return true if the specified clip exists.

-----------------------------------------

epl   : explode         [int] ['edit']
    Reparent all tracks and their clips within a group out to its parent track node and remove the group.

-----------------------------------------

eac   : exportAllClips  [boolean] ['edit']
    When used with the ef/exportFbx flag, export all clips.

-----------------------------------------

ef    : exportFbx       [string] ['edit']
    Export currently selected clips to FBX files.

-----------------------------------------

ex    : extend          [boolean] ['edit']
    Extend the clip to encompass all children.

-----------------------------------------

exp   : extendParent    [boolean] ['edit']
    Extend parent to fit this clip.

-----------------------------------------

gh    : ghost           [boolean] ['query', 'edit']
    Enable/disable ghosting for the specified clip.

-----------------------------------------

gra   : ghostRootAdd    [string] ['edit']
    Add path to specified node as a custom ghost root.

-----------------------------------------

grr   : ghostRootRemove [string] ['edit']
    Remove path to specified node as a custom ghost root.

-----------------------------------------

grp   : group           [boolean] []
    Specify if the new container should be created as a group, containing other specified clips.

-----------------------------------------

he    : holdEnd         [time] ['query', 'edit']
    Hold clip's end to time.

-----------------------------------------

hs    : holdStart       [time] ['query', 'edit']
    Hold clip's start to time.

-----------------------------------------

itd   : importTakeDestination [int] []
    Specify how to organize imported FBX takes: 0 - Import takes into a group (default) 1 - Import takes into multiple compositions 2 - Import takes as a sequence of clips

-----------------------------------------

ict   : isContainer     [boolean] ['query']
    Indicate if given clip ID is a container.

-----------------------------------------

lug   : listUserGhostRoot [boolean] ['query']
    Get user defined ghost root object for indicated clips.

-----------------------------------------

le    : loopEnd         [time] ['query', 'edit']
    Loop clip's end to time.

-----------------------------------------

ls    : loopStart       [time] ['query', 'edit']
    Loop clip's start to time.

-----------------------------------------

mcd   : minClipDuration [boolean] ['query']
    Returns the minimum allowed clip duration.

-----------------------------------------

mas   : modifyAnimSource [boolean] ['edit']
    When populating, automatically modify Anim Source without asking the user.

-----------------------------------------

mcl   : moveClip        [time] ['edit']
    Move clip by adding delta to its start time.

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    Mute/Unmute the clip given a clip ID. In query mode, return the muted state of the clip. Clips muted by soloing are not affected by this flag.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name of the clip. A clip will never have an empty name. If an empty string is provided, it will be replaced with "_".

-----------------------------------------

p     : parent          [int] ['edit']
    Specify group/object parent ID.

-----------------------------------------

pid   : parentClipId    [int] ['query']
    Specify the parent clip ID of a clip to be created.

-----------------------------------------

pgd   : parentGroupId   [boolean] ['query']
    Return the parent group ID of the given clip.

-----------------------------------------

pcl   : pasteClip       [time] ['edit']
    Paste clip to the given time and track. Destination track is required to be specified through the track flag in the format "tracksNode:trackIndex". A trackIndex of -1 indicates that a new track will be created.

-----------------------------------------

pt    : path            [string] ['edit']
    Full path of the clip to be edited. For example: composition1|track1|clip1.  In query mode, this flag can accept a value.

-----------------------------------------

pat   : preserveAnimationTiming [boolean] []
    When used with the population command, it ensures the animation is offset within a clip in such way that it matches its original scene timing, regardless of the new clip's position.

-----------------------------------------

rcl   : razorClip       [time] ['edit']
    Razor clip into two clips at the specified time.

-----------------------------------------

rmp   : remap           [[string, string]] ['edit']
    Change animation source for a given clip item to a new one, specified by the target path. This removes all clips for the roster item and creates new clips from the Anim Source for the new target path.

-----------------------------------------

rs    : remapSource     [[string, string]] ['edit']
    Set animation source to be remapped for a given clip item to new one, specified by the target path.

-----------------------------------------

rms   : remappedSourceAttrs [boolean] ['query']
    Return an array of attribute indices and names of the source attributes of a remapped clip.

-----------------------------------------

rmt   : remappedTargetAttrs [boolean] ['query']
    Return an array of attribute indices and names of the target attributes of a remapped clip.

-----------------------------------------

ra    : removeAttribute [string] ['edit']
    Remove attribute from the clip.

-----------------------------------------

rmc   : removeClip      [boolean] ['edit']
    Remove clip of specified ID.

-----------------------------------------

rcf   : removeCrossfade [boolean] ['edit']
    Remove custom crossfade between two clips specified by -clipId flags.

-----------------------------------------

rwc   : removeWeightCurve [boolean] ['query', 'edit']
    Remove the weight curve connected to the clip.

-----------------------------------------

rt    : resetTiming     [boolean] ['edit']
    Reset start and duration of a clip with the given clip ID to the values stored in its Anim Source.

-----------------------------------------

rtr   : resetTransition [boolean] ['edit']
    Reset transition intervals between specified clips.

-----------------------------------------

rpl   : ripple          [boolean] ['edit']
    Apply rippling to a clip operation.

-----------------------------------------

rti   : rootClipId      [int] ['edit']
    ID of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip. For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.

-----------------------------------------

rpt   : rootPath        [string] ['edit']
    Path of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip. For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.

-----------------------------------------

sce   : scaleEnd        [time] ['edit']
    Scale the end time of the clip to the given time.

-----------------------------------------

scp   : scalePivot      [time] ['edit']
    Scale the time of the clip based on the pivot. This should be used together with -scs/scaleStart or -sce/scaleEnd.

-----------------------------------------

scs   : scaleStart      [time] ['edit']
    Scale the start time of the clip to the given time.

-----------------------------------------

k     : setKeyframe     [string] ['edit']
    Set keyframe on a specific clip for a specified attribute.

-----------------------------------------

src   : speedRamping    [int] ['query', 'edit']
    To control the playback speed of the clip by animation curve:    * 1 : create - Attach a speed curve and a time warp curve to the clip to control the playback speed   * 2 : edit - Open the Graph editor to edit the speed curve   * 3 : enable - Create a time warp curve from current speed curve and attach to clip   * 4 : disable - Remove the time warp curve from clip   * 5 : delete - Delete the attached speed curve and time warp curve   * 6 : reset - Reset the speed curve back to the default   * 7 : convert to speed curve from time warp   * 8 : convert to time warp from speed curve  In query mode, return true if a speed curve is attached to the clip.

-----------------------------------------

s     : startTime       [time] ['query']
    Relative start time of the new clip.

-----------------------------------------

tw    : timeWarp        [boolean] ['query']
    Return true if the clip is being warped by the speed curve. If no speed curve is attached to the clip, it will always return false.

-----------------------------------------

twc   : timeWarpCurve   [boolean] ['query']
    Returns the name of the time warp curve connected to the clip.

-----------------------------------------

twt   : timeWarpType    [int] ['query', 'edit']
    Time warp mode:    * 0: remapping - Connected time warp curve performs frame by frame remapping   * 1: speed curve - Connected time warp curve acts as a speed curve  In query mode, return time warp mode of a clip.

-----------------------------------------

trk   : track           [string] ['query', 'edit']
    The new clip container will be created on the track in the format "trackNode:trackNumber", or on a track path, for example "composition1|track1". In query mode, return a string containing the track number and tracks node of the given clip ID. In create mode, if the track number is '-1' or not given at all, then a new track will be created. For example: "trackNode:-1"; "composition1|".

-----------------------------------------

trn   : tracksNode      [boolean] ['query']
    Get tracks node if specified clip is a group clip.

-----------------------------------------

tra   : transition      [boolean] ['edit']
    Create transition intervals between specified clips.

-----------------------------------------

tre   : trimEnd         [time] ['edit']
    Trim the end time of the clip to the given time.

-----------------------------------------

trs   : trimStart       [time] ['edit']
    Trim the start time of the clip to the given time.

-----------------------------------------

trc   : truncated       [boolean] ['query']
    This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc. to query (global) truncated time.

-----------------------------------------

uas   : uniqueAnimSource [boolean] ['edit']
    If a given clip is sharing its Anim Source node with another clip, make the Anim Source of this clip unique.

-----------------------------------------

ugr   : userGhostRoot   [boolean] ['query', 'edit']
    Edit or query custom ghost root variable. Determine whether to use user defined ghost root.

-----------------------------------------

wc    : weightCurve     [boolean] ['query', 'edit']
    In edit mode, create a weight curve and connect it to the clip. In query mode, return the name of the weight curve connected to the clip.

-----------------------------------------

zk    : zeroKeying      [boolean] ['edit']
    A toggle flag to use in conjunction with k/setKeyframe, set the value of the key frame(s) to be keyed to zero.

-----------------------------------------

ao    : addObjects      [string] ['query', 'edit']
    Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s). Similar to -addSelectedObjects flag but acts on given object(s) instead. This flag will override the flag -addSelectedObjects.

-----------------------------------------

akg   : addRelatedKG    [boolean] ['query', 'edit']
    During population, determine if associated keying groups should be populated or not. Normally used for populating HIK. By default the value is false.

-----------------------------------------

aso   : addSelectedObjects [boolean] ['query', 'edit']
    Populate the currently selected objects and their attributes to anim source or Time Editor. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.

-----------------------------------------

at    : attribute       [string] ['edit']
    Populate a specific attribute on a object.

-----------------------------------------

exc   : exclusive       [boolean] ['edit']
    Populate all types of animation sources which are not listed by "type" Flag.

-----------------------------------------

aft   : importAllFbxTakes [boolean] []
    Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

-----------------------------------------

fbx   : importFbx       [string] []
    Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).

-----------------------------------------

ft    : importFbxTakes  [string] []
    Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

-----------------------------------------

mf    : importMayaFile  [string] []
    Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

-----------------------------------------

io    : importOption    [string] ['edit']
    Option for importing animation source. Specify either 'connect' or 'generate'. connect: Only connect with nodes already existing in the scene. Importing an animation source that does not match with any element of the current scene will not create any clip. (connect is the default mode). generate: Import everything and generate new nodes for items not existing in the scene.

-----------------------------------------

ipo   : importPopulateOption [string] ['edit']
    Option for population when importing.

-----------------------------------------

icn   : importedContainerNames [string] []
    Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.

-----------------------------------------

irt   : includeRoot     [boolean] ['edit']
    Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.

-----------------------------------------

pia   : populateImportedAnimSources [string] []
    Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).

-----------------------------------------

poc   : poseClip        [boolean] []
    Populate as pose clip with current attribute values.

-----------------------------------------

rec   : recursively     [boolean] ['edit']
    Populate selection recursively, adding all the children.

-----------------------------------------

rsa   : removeSceneAnimation [boolean] ['edit']
    If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.

-----------------------------------------

sar   : showAnimSourceRemapping [boolean] []
    Show a remapping dialog when the imported anim source attributes do not match the scene attributes.

-----------------------------------------

tl    : takeList        [string] []
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.

-----------------------------------------

toi   : takesToImport   [string] []
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.

-----------------------------------------

typ   : type            [string]
    Only populate the specified type of animation source.

    """

def timeEditorClipLayer(q=1,e=1,aa="string",al="string",ao="string",all=1,a="string",ak="string",cid="int",idx="int",ks=1,lid="int",ln="string",m="int",mu=1,n=1,pt="string",ra="string",rl=1,ro="string",rs=1,k=1,sl=1,zk=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClipLayer.html



-----------------------------------------

timeEditorClipLayer is undoable, queryable, and editable.

Time Editor clip layers commands


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aa    : addAttribute    [string] ['edit']
    Add given plug to a layer with a supplied layerId.

-----------------------------------------

al    : addLayer        [string] ['edit']
    Add a new layer with a given name.

-----------------------------------------

ao    : addObject       [string] ['edit']
    Add given object with all its attributes in the clip to a layer with a supplied layerId.

-----------------------------------------

all   : allLayers       [boolean] ['query']
    Return all layers given clip ID.

-----------------------------------------

a     : attribute       [string] ['edit']
    The attribute path to key.

-----------------------------------------

ak    : attributeKeyable [string] ['query']
    Return whether specified attribute is keyable.

-----------------------------------------

cid   : clipId          [int] ['edit']
    ID of the clip this layer command operates on.  In query mode, this flag can accept a value.

-----------------------------------------

idx   : index           [int] ['edit']
    Layer index, used when adding new layer at specific location in the stack.

-----------------------------------------

ks    : keySiblings     [boolean] ['edit']
    If set to true, additional attributes might be keyed while keying to achieve desired result.

-----------------------------------------

lid   : layerId         [int] ['edit']
    Layer ID used in conjunction with other edit flags.  In query mode, this flag can accept a value.

-----------------------------------------

ln    : layerName       [string] ['query', 'edit']
    Edit layer name. In query mode, return the layer name given its layer ID and clip ID.

-----------------------------------------

m     : mode            [int] ['edit']
    To control the playback speed of the clip by animation curve:    * 0 : additive   * 1 : additive override   * 2 : override   * 3 : override passthrough

-----------------------------------------

mu    : mute            [boolean] ['edit']
    Mute/unmute a layer given its layer ID and clip ID.

-----------------------------------------

n     : name            [boolean] ['query']
    Query the attribute name of a layer given its layer ID and clip ID.

-----------------------------------------

pt    : path            [string] ['edit']
    Full path of a layer or a clip on which to operate. For example: composition1|track1|clip1|layer1; composition1|track1|group|track1|clip1.  In query mode, this flag can accept a value.

-----------------------------------------

ra    : removeAttribute [string] ['edit']
    Remove given plug from a layer with a supplied layerId.

-----------------------------------------

rl    : removeLayer     [boolean] ['edit']
    Remove layer with an ID.

-----------------------------------------

ro    : removeObject    [string] ['edit']
    Remove given object with all its attributes in the clip to a layer with a supplied layerId.

-----------------------------------------

rs    : resetSolo       [boolean] ['edit']
    Unsolo all soloed layers in a given clip ID.

-----------------------------------------

k     : setKeyframe     [boolean] ['edit']
    Set keyframe on specified attributes on specified layer of a clip. Use -clipId to indicate the specified clip. Use -layerId to indicate the specified layer of the clip. Use -attribute to indicate the specified attributes (if no attribute flag is used, all attribute will be keyed). Use -zeroKeying to indicate that zero offset from original animation should be keyed.

-----------------------------------------

sl    : solo            [boolean] ['edit']
    Solo/unsolo a layer given its layers ID and clip ID.

-----------------------------------------

zk    : zeroKeying      [boolean]
    Indicate if the key to set should be zero offset from original animation.

    """

def timeEditorClipOffset(q=1,e=1,atr=1,id="int",mci="int",mdt="time",mob="name",mor=1,mot=1,mpt="string",mro="int",mst="time",mto="int",oft=1,pt="string",rsm="int",rmp="string",rob="string",upx="float",upy="float",upz="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClipOffset.html



-----------------------------------------

timeEditorClipOffset is undoable, queryable, and editable.

This command is used to compute an offset to apply on a source clip in order
to automatically align it to a destination clip at a specified match element.
For this command to work, offset objects must be specified for the character.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

atr   : applyToAllRoots [boolean] []
    Apply root offsets to all roots in the population. However, if the root objects are specified by rootObj flag, this flag will be ignored.

-----------------------------------------

id    : clipId          [int] ['edit']
    ID of the clip to be edited.

-----------------------------------------

mci   : matchClipId     [int] []
    Specify the ID of a clip to match.

-----------------------------------------

mdt   : matchDstTime    [time] []
    Specify the time on target clip.

-----------------------------------------

mob   : matchObj        [name] []
    Specify the object to match.

-----------------------------------------

mor   : matchOffsetRot  [boolean] ['query']
    Get the rotation of the match offset matrix.

-----------------------------------------

mot   : matchOffsetTrans [boolean] ['query']
    Get the translation of the match offset matrix.

-----------------------------------------

mpt   : matchPath       [string] []
    Full path of the clip to match. For example: composition1|track1|Group|track2|clip1

-----------------------------------------

mro   : matchRotOp      [int] []
    Specify the option for matching rotation.    * 0 : full - All rotation components are matched   * 1 : Y - Y component is matched   * 2 : none - No rotation matching

-----------------------------------------

mst   : matchSrcTime    [time] []
    Specify the time on source clip.

-----------------------------------------

mto   : matchTransOp    [int] []
    Specify the option for matching translation.    * 0 : full - All translation components are matched   * 1 : XZ - X and Z components are matched   * 2 : none - No translation matching

-----------------------------------------

oft   : offsetTransform [boolean] ['query']
    Create/get an offset for the specified clip.

-----------------------------------------

pt    : path            [string] ['edit']
    Full path of a clip to be edited. For example: composition1|track1|group; composition1|track1|group|track2|clip1.  In query mode, this flag can accept a value.

-----------------------------------------

rsm   : resetMatch      [int] []
    Specify clip ID to remove offset.

-----------------------------------------

rmp   : resetMatchPath  [string] []
    Specify clip's full path to remove offset. For example: composition1|track1|Group|track2|clip1

-----------------------------------------

rob   : rootObj         [string] ['query', 'edit']
    Specify the root objects. If specified, this flag will take precedence over applyToAllRoots flag. When used in query mode, returns list of roots defined for the relocator.

-----------------------------------------

upx   : upVectorX       [float] []
    Specify the X coordinate of the up vector.

-----------------------------------------

upy   : upVectorY       [float] []
    Specify the Y coordinate of the up vector.

-----------------------------------------

upz   : upVectorZ       [float]
    Specify the Z coordinate of the up vector.

    """

def timeEditorComposition(q=1,e=1,act=1,acp=1,ct=1,delete=1,df="string",ren="[string, string]",tn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorComposition.html



-----------------------------------------

timeEditorComposition is undoable, queryable, and editable.

Commands related to composition management inside Time Editor.


-----------------------------------------


Return Value:

string  Return values currently not documented.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

act   : active          [boolean] ['query', 'edit']
    Query or edit the active composition.

-----------------------------------------

acp   : allCompositions [boolean] ['query']
    Return all compositions inside Time Editor.

-----------------------------------------

ct    : createTrack     [boolean] []
    Create a default track when creating a new composition.

-----------------------------------------

delete : delete          [boolean] ['query', 'edit']
    Delete the composition.

-----------------------------------------

df    : duplicateFrom   [string] []
    Duplicate the composition.

-----------------------------------------

ren   : rename          [[string, string]] ['edit']
    Rename the composition of the first name to the second name.

-----------------------------------------

tn    : tracksNode      [boolean]
    Query the tracks node of a composition.

    """

def timeEditorPanel(q=1,e=1,ace="int",atr=1,att=1,atv="int",af="string",aft="string",ctl=1,dt="string",dat="string",dak="string",di="string",dk="string",dtn="string",dv="string",dtg="string",ex=1,f="string",fmc="string",gtv="int",hlc="string",kt="int",l="int",lck=1,la="string",mlc="string",m="script",mcw="int",pnl="string",p="string",slc="string",spe=1,st="string",stc=1,stf=1,sto="int",sv="string",sts=1,tv="int",tc=1,up=1,ulk=1,upd=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorPanel.html



-----------------------------------------

timeEditorPanel is undoable, queryable, and editable.

Time Editor - non-linear animation editor


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ace   : activeClipEditMode [int] ['query', 'edit']
    Set the appropriate clip edit mode for the editor.    * 0: Default Mode   * 1: Trim Mode   * 2: Scale Mode   * 3: Loop Mode   * 4: Hold Mode

-----------------------------------------

atr   : activeTabRootClipId [boolean] ['query']
    Get the clip id for which current active tab has been opened. In case of main tab, this will return -1 meaning there is no root clip.

-----------------------------------------

att   : activeTabTime   [boolean] ['query']
    Get current time displayed inside the active tab. This will be global time in case of the main tab and local time for others.

-----------------------------------------

atv   : activeTabView   [int] ['query', 'edit']
    Get/set the index of the tab widget's (active) visible tab. Note: the index is zero-based.

-----------------------------------------

af    : autoFit         [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view.

-----------------------------------------

aft   : autoFitTime     [string] ['query', 'edit']
    on | off | tgl Auto fit-to-view along the time axis, as well.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dat   : displayActiveKeyTangents [string] ['edit']
    on | off | tgl Display active key tangents in the editor.

-----------------------------------------

dak   : displayActiveKeys [string] ['edit']
    on | off | tgl Display active keys in the editor.

-----------------------------------------

di    : displayInfinities [string] ['edit']
    on | off | tgl Display infinities in the editor.

-----------------------------------------

dk    : displayKeys     [string] ['edit']
    on | off | tgl Display keyframes in the editor.

-----------------------------------------

dtn   : displayTangents [string] ['edit']
    on | off | tgl Display tangents in the editor.

-----------------------------------------

dv    : displayValues   [string] ['edit']
    on | off | tgl Display active keys and tangents values in the editor.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

gtv   : groupIdForTabView [int] ['query']
    Get the group clip id for the given tab view index. To specify the tab index, this flag must appear before the -query flag.  In query mode, this flag needs a value.

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

kt    : keyingTarget    [int] ['query', 'edit']
    Set keying target to specified clip ID. If keying into layer, '-layer' flag must be used. In query mode, the clip id is omitted, and the name of the keying target will be returned.

-----------------------------------------

l     : layerId         [int] ['edit']
    Indicate layer ID of keying target.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

la    : lookAt          [string] ['edit']
    all | selected | currentTime FitView helpers.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

m     : menu            [script] []
    Specify a script to be run when the editor is created. The function will be passed one string argument which is the new editor's name.

-----------------------------------------

mcw   : minClipWidth    [int] ['query', 'edit']
    Set the minimum clip width.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

spe   : setToPrevClipEditMode [boolean] ['edit']
    Revert to previous clip edit mode.

-----------------------------------------

st    : snapTime        [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in time.

-----------------------------------------

stc   : snapToClip      [boolean] ['query', 'edit']
    Enable/Disable snap-to-clip option in Time Editor while manipulating and drag-and-drop clips. When snapToClip is on all manipulated timing will land on a clip boundary if it is close to it.

-----------------------------------------

stf   : snapToFrame     [boolean] ['query', 'edit']
    Enable/Disable snap-to-frame option in Time Editor while manipulating and drag-and-drop clips. When snapToFrame is on all manipulated timing will land on an exact frame.

-----------------------------------------

sto   : snapTolerance   [int] ['query', 'edit']
    Set the tolerance value for snapping.

-----------------------------------------

sv    : snapValue       [string] ['query', 'edit']
    none | integer | keyframe Keyframe move snap in values.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

tv    : tabView         [int] ['edit']
    Create a tab view for the given group clip ID.

-----------------------------------------

tc    : timeCursor      [boolean] ['query', 'edit']
    Activate the time cursor in Time Editor for scrubbing.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def timeEditorTracks(q=1,e=1,acw="time",aci="time",at="int",ac=1,atc=1,atr=1,cp=1,pt="string",pi="int",rt="int",rtp="string",rot="[int, int]",rm=1,rs=1,st=1,tgh=1,ti="int",tm=1,tn="string",ts=1,tt="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeEditorTracks.html



-----------------------------------------

timeEditorTracks is undoable, queryable, and editable.

Time Editor tracks commands


-----------------------------------------


Return Value:

Int  In edit mode, return the newly created Track index.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

acw   : activeClipWeight [time] ['query']
    Get the clip weight at the specified time.

-----------------------------------------

aci   : activeClipWeightId [time] ['query']
    Get the clip ID carrying the active clip weight at the specified time.

-----------------------------------------

at    : addTrack        [int] ['edit']
    Add new track at the track index specified. Indices are 0-based. Specify -1 to add the track at the end.

-----------------------------------------

ac    : allClips        [boolean] ['query']
    Return a list of clip IDs under the specified track.

-----------------------------------------

atc   : allTracks       [boolean] ['query']
    Return a list of strings for all the immediate tracks for the given tracks node in the format "tracksNode:trackIndex".

-----------------------------------------

atr   : allTracksRecursive [boolean] ['query']
    Return a list of strings for all the tracks for the given tracks node, or return a list of strings for all tracks of all tracks nodes in the format "tracksNode:trackIndex". If the given root tracks node is from a composition, this command returns the tracks under that composition, including the tracks within groups that is under the same composition.

-----------------------------------------

cp    : composition     [boolean] ['query']
    Return the composition the specified track belongs to.

-----------------------------------------

pt    : path            [string] ['edit']
    Full path of a track node or a track on which to operate. For example: composition1|track1|group; composition1|track1.  In query mode, this flag can accept a value.

-----------------------------------------

pi    : plugIndex       [int] ['query', 'edit']
    Get the plug index of the specified track.

-----------------------------------------

rt    : removeTrack     [int] ['edit']
    Remove track at given index. It is a multi-use flag.

-----------------------------------------

rtp   : removeTrackByPath [string] ['edit']
    Remove track at given path. It is a multi-use flag. For example: composition1|track1|group|track1;

-----------------------------------------

rot   : reorderTrack    [[int, int]] ['edit']
    Move the track relative to other tracks. The first argument is the track index (0-based). The second argument can be a positive or negative number to indicate the steps to move. Positive numbers move forward and negative numbers move backward.

-----------------------------------------

rm    : resetMute       [boolean] []
    Reset all the muted tracks in the active composition.

-----------------------------------------

rs    : resetSolo       [boolean] []
    Reset the soloing of all tracks on the active composition.

-----------------------------------------

st    : selectedTracks  [boolean] ['query']
    Return a list of the indices for all the selected tracks for the given tracks node, or return a list of strings for all selected tracks of all tracks nodes in the format "tracksNode:trackIndex".

-----------------------------------------

tgh   : trackGhost      [boolean] ['query', 'edit']
    Ghost all clips under track.

-----------------------------------------

ti    : trackIndex      [int] ['query', 'edit']
    Specify the track index. This flag is used in conjunction with the other flags.  In query mode, this flag can accept a value.

-----------------------------------------

tm    : trackMuted      [boolean] ['query', 'edit']
    Return whether the track is muted.

-----------------------------------------

tn    : trackName       [string] ['query', 'edit']
    Display name of the track.

-----------------------------------------

ts    : trackSolo       [boolean] ['query', 'edit']
    Return whether the track is soloed.

-----------------------------------------

tt    : trackType       [int]
    Specify the track type. Can only be used together with -at/addTrack. Does not work by itself. In query mode, return the integer corresponding to the track type.    * 0: Animation Track (Default)   * 1: Audio Track

    """

def timeWarp(q=1,e=1,df="int",f="float",g=1,it="[int, string]",mf="[int, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeWarp.html



-----------------------------------------

timeWarp is undoable, queryable, and editable.

This command is used to create a time warp input to a set of animation curves.


-----------------------------------------


Return Value:

string  timeWarp name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

df    : deleteFrame     [int] ['edit']
    The flag value indicates the 0-based index of the warp frame to delete. This flag can only be used in edit mode.

-----------------------------------------

f     : frame           [float] ['query', 'edit']
    In create and edit mode, this flag can be used to specify warp frames added to the warp operation. In query mode, this flag returns a list of the frame values where warping occurs. The moveFrame flag command can be used to query the associated warped values.

-----------------------------------------

g     : g               [boolean] ['query', 'edit']
    In create mode, creates a global time warp node which impacts every animated object in the scene. In query mode, returns the global time warp node. Note: only one global time warp can exist in the scene.

-----------------------------------------

it    : interpType      [[int, string]] ['query', 'edit']
    This flag can be used to set the interpolation type for a given span. Valid interpolation types are linear, easeIn and easeOut. When queried, it returns a string array of the interpolation types for the specified time warp.

-----------------------------------------

mf    : moveFrame       [[int, float]]
    This flag can be used to move a singular warp frame. The first value specified indicates the 0-based index of the warp frame to move. The second value indicates the new warp frame value. This flag can only be used in edit and query mode. When queried, it returns an array of the warped frame values.

    """

def ubercam():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ubercam.html



-----------------------------------------

ubercam is undoable, NOT queryable, and NOT editable.

Use this command to create a "ubercam" with equivalent behavior to all cameras
used by shots in the sequencer.


-----------------------------------------


Return Value:

string  Ubercam name
    """

def bakeDeformer(cs=1,rom="timerange",dm="string",ds="string",hi=1,i="string[]",mi="int",pw="float",sw="int",sm="string",ss="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bakeDeformer.html



-----------------------------------------

bakeDeformer is undoable, NOT queryable, and NOT editable.

Given a rigged character, whose mesh shape is determined by a set of
deformers, bakeDeformer calculates linear blend skin weights most closely
approximating observed deformations. To do this, a test set of examples is
generated by moving the rig through a range of motion. Results mesh and pose
pairs are then used to solve a constrained optimization, solving for skinning
weights. bakeDeformer automatically binds and applies resulting weights to the
destination geometry. If the source and destination mesh/skeleton are
identical, the command will replace the original deformations with a
skinCluster and computed weights. See the below examples for sample usage.


-----------------------------------------


Return Value:

string  BakeDeformer name


-----------------------------------------


Flags:

-----------------------------------------

cs    : colorizeSkeleton [boolean] []
    The new skin cluster created will have its skeleton colorized. Must be used with the -srcSkeletonName and -dstSkeletonName flags.

-----------------------------------------

rom   : customRangeOfMotion [timerange] []
    When this flag is specified with the frames for the range of motion to be used, the tool will step through each frame as a separate pose. Otherwise the tool will use the existing range of motion in the tool that rotates each influence 45 degrees.  Usage examples:    * -rom "10:20" means all frames in the range from 10 to 20, inclusive, in the current time unit.    * Omitting one end of a range means using either end of the animation range (or both), as in the following examples:    * -rom "10:" means all frames from time 10 (in the current time unit) onwards to the maximum time in the animation range (on the timeline).    * -rom ":10" means all frames from the minimum time on the animation range (on the timeline) up to (and including) time 10 (in the current time unit).    * -rom ":" is a short form to specify all frames, from minimum to maximum time on the current animation range.   When using this flag, some of the joints in the specified range of motion may not have changed sufficiently. To improve bakeDeformer results or avoid algorithm errors, the command will return a list of influences that do not move enough in the specified range of motion. To detect these joints, the local transformation of each joint is compared between subsequent frames. We consider that a joint has sufficiently changed if any of the below criteria are met:    * There is a rotation of at least 5 degrees, as determined by the shortest rotation between transforms.   * There is a translation of 1% or greater of the size of the largest bounding box containing all joints for each frame.   * There is a scaling change of at least 1%. This percentage represents the smallest scaling value over the largest scaling value (in absolute value).  If a joint has not met any of the criteria, it will be added to the warning of joints that have not moved enough.  The custom range of motion should be considered experimental.

-----------------------------------------

dm    : dstMeshName     [string] []
    The destination mesh name.

-----------------------------------------

ds    : dstSkeletonName [string] []
    The destination skeleton name.

-----------------------------------------

hi    : hierarchy       [boolean] []
    All children of the passed joints that are used in the influences flag are used.

-----------------------------------------

i     : influences      [string[]] []
    A list of joints that are used as the influences to determine new weights.

-----------------------------------------

mi    : maxInfluences   [int] []
    The maximum number of influences per vertex.

-----------------------------------------

pw    : pruneWeights    [float] []
    On the newly created skin cluster, set any weight below the given the value to zero (post-processing). This will call the skinPercent command as follows: "skinPercent -pruneWeights [value] [skinClusterName] [dstMeshName]" where [value] is the value passed into this flag, [skinClusterName] is the name of the new skinCluster node created after running this tool, and [dstMeshName] is the mesh provided in the -dstMeshName flag.

-----------------------------------------

sw    : smoothWeights   [int] []
    The number of smoothing iterations for smoothing weights (post- processing). This also renormalizes the remaining the weights.

-----------------------------------------

sm    : srcMeshName     [string] []
    The source mesh name.

-----------------------------------------

ss    : srcSkeletonName [string]
    The source skeleton name.

    """

def blendShape(q=1,e=1,af=1,ar=1,at=1,bf=1,cd="[uint, uint, uint]",cid="[uint, uint, uint, uint]",dt=1,en="float",ex="string",ep="string",et="[int, int]",ft="[uint, uint]",foc=1,g="string",gi=1,ignoreSelected=1,ip="string",ib=1,ibi="uint",ibt="string",ihs=1,mgs="int",mgt="uint",md="uint",mt="[uint, uint]",n="string",ng=1,o="string",par=1,pr=1,rm=1,rtd="[uint, uint]",sp=1,sd=1,sa="string",se="string",ss="uint",ts=1,t="[string, uint, string, float]",tc=1,tr="string",w="[uint, float]",wc="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/blendShape.html



-----------------------------------------

blendShape is undoable, queryable, and editable.

This command creates a blendShape deformer, which blends in specified amounts
of each target shape to the initial base shape. Each base shape is deformed by
its own set of target shapes. Every target shape has an index that associates
it with one of the shape weight values.  

In the create mode the first item on the selection list is treated as the base
and the remaining inputs as targets. If the first item on the list has
multiple shapes grouped beneath it, the targets must have an identical shape
hierarchy. Additional base shapes can be added in edit mode using the
deformers -g flag.


-----------------------------------------


Return Value:

string[]  (the blendShape node name)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

at    : automatic       [boolean] ['edit']
    The -automatic flag is used to specify deformer ordering in a way that choses between -frontOfChain and -before automatically. If the geometry being deformed is only affected by invertible deformers, the -frontOfChain mode is used, otherwise the -before mode is used.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

cd    : copyDelta       [[uint, uint, uint]] ['edit']
    Set the base, source, and destination delta index values.

-----------------------------------------

cid   : copyInBetweenDelta [[uint, uint, uint, uint]] ['edit']
    Set the base, target, source, and destination delta index values.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

en    : envelope        [float] ['query', 'edit']
    Set the envelope value for the deformer, controlling how much of the total deformation gets applied. Default is 1.0.

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

ep    : export          [string] ['edit']
    Export the shapes to the named file path.

-----------------------------------------

et    : exportTarget    [[int, int]] ['edit']
    Specify the base and target index pairs for the export.

-----------------------------------------

ft    : flipTarget      [[uint, uint]] ['edit']
    Flip the list of base and target pairs.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ip    : ip              [string] ['edit']
    Import the shapes from the named file path.

-----------------------------------------

ib    : inBetween       [boolean] ['edit']
    Indicate that the specified target should serve as an inbetween. An inbetween target is one that serves as an intermediate target between the base shape and another target.

-----------------------------------------

ibi   : inBetweenIndex  [uint] ['edit']
    Only used with the -rtd/-resetTargetDelta flag to remove delta values for points in the inbetween target geometry defined by this index.

-----------------------------------------

ibt   : inBetweenType   [string] ['edit']
    Specify if the in-between target to be created is relative to the hero target or if it is absolute. If it is relative to hero targets, the in-between target will get any changes made to the hero target. Valid values are "relative" and "absolute". This flag should always be used with the -ib/-inBetween and -t/-target flags.

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

mgs   : mergeSource     [int] ['edit']
    List of source indexes for a merge.

-----------------------------------------

mgt   : mergeTarget     [uint] ['edit']
    Target index of a merge

-----------------------------------------

md    : mirrorDirection [uint] ['edit']
    Mirror direction; 0 = negative, 1 = positive

-----------------------------------------

mt    : mirrorTarget    [[uint, uint]] ['edit']
    Mirror the list of base and target pairs.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

ng    : normalizationGroups [boolean] ['query']
    Returns a list of the used normalization group IDs.

-----------------------------------------

o     : origin          [string] []
    blendShape will be performed with respect to the world by default. Valid values are "world" and "local". The local flag will cause the blend shape to be performed with respect to the shape's local origin.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

rtd   : resetTargetDelta [[uint, uint]] ['edit']
    Remove all delta values for points in the target geometry, including all sequential targets defined by target index.   Parameter list:    1. uint: the base object index   2. uint: the target index

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

sd    : suppressDialog  [boolean] ['edit']
    Suppress dialog box and run the command as defined by the user.

-----------------------------------------

sa    : symmetryAxis    [string] ['query', 'edit']
    Axis for symmetry. Valid values are "X", "Y", and "Z".

-----------------------------------------

se    : symmetryEdge    [string] ['query', 'edit']
    One or two symmetry edge names, separated by a ".". See the blendShape node's symmetryEdge attribute for legal values.

-----------------------------------------

ss    : symmetrySpace   [uint] ['query', 'edit']
    Space for symmetry. 0 = Topological, 1 = Object, 2 = UV

-----------------------------------------

ts    : tangentSpace    [boolean] ['edit']
    Indicate that the delta of the specified target should be relative to the tangent space of the surface.

-----------------------------------------

t     : target          [[string, uint, string, float]] ['query', 'edit']
    Set target object as the index target shape for the base shape base object. The full influence of target shape takes effect when its shape weight is targetValue.   Parameter list:    1. string: the base object   2. int: index   3. string: the target object   4. double: target value

-----------------------------------------

tc    : topologyCheck   [boolean] []
    Set the state of checking for a topology match between the shapes being blended. Default is on.

-----------------------------------------

tr    : transform       [string] ['query', 'edit']
    Set transform for target, then the deltas will become relative to a post transform. Typically the best workflow for this option is to choose a joint that is related to the fix you have introduced. This flag should be used only if the "Deformation order" of blendShape node is "Before".

-----------------------------------------

w     : weight          [[uint, float]] ['query', 'edit']
    Set the weight value (second parameter) at index (first parameter).

-----------------------------------------

wc    : weightCount     [uint]
    Set the number of shape weight values.

    """

def blendShapeEditor(q=1,e=1,ctl=1,dt="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",lck=1,mlc="string",pnl="string",p="string",slc="string",sts=1,tcl=1,tl=1,up=1,ulk=1,upd=1,ut="string",vs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/blendShapeEditor.html



-----------------------------------------

blendShapeEditor is undoable, queryable, and editable.

This command creates an editor that derives from the base editor class that
has controls for blendShape, control nodes.


-----------------------------------------


Return Value:

string  The name of the editor    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

tcl   : targetControlList [boolean] ['query']
    

-----------------------------------------

tl    : targetList      [boolean] ['query']
    

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

vs    : verticalSliders [boolean]
    

    """

def blendShapePanel(q=1,e=1,be=1,ctl=1,cp="string",cs=1,dt="string",dtg="string",es=1,ex=1,init=1,iu=1,l="string",mrl=1,mbv=1,ni=1,p="string",pmp="script",rp="string",to=1,toc="string",tor=1,up=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/blendShapePanel.html



-----------------------------------------

blendShapePanel is undoable, queryable, and editable.

This command creates a panel that derives from the base panel class that
houses a blendShapeEditor.


-----------------------------------------


Return Value:

string  The name of the panel    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

be    : blendShapeEditor [boolean] ['query']
    Query only flag that returns the name of an editor to be associated with the panel.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Returns the top level control for this panel. Usually used for getting a parent to attach popup menus. CAUTION: panels may not have controls at times. This flag can return "" if no control is present.

-----------------------------------------

cp    : copy            [string] ['edit']
    Makes this panel a copy of the specified panel. Both panels must be of the same type.

-----------------------------------------

cs    : createString    [boolean] ['edit']
    Command string used to create a panel

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the Maya panel.

-----------------------------------------

es    : editString      [boolean] ['edit']
    Command string used to edit a panel

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

init  : init            [boolean] ['edit']
    Initializes the panel's default state. This is usually done automatically on file -new and file -open.

-----------------------------------------

iu    : isUnique        [boolean] ['query']
    Returns true if only one instance of this panel type is allowed.

-----------------------------------------

l     : label           [string] ['query', 'edit']
    Specifies the user readable label for the panel.

-----------------------------------------

mrl   : menuBarRepeatLast [boolean] ['query', 'edit']
    Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.

-----------------------------------------

mbv   : menuBarVisible  [boolean] ['query', 'edit']
    Controls whether the menu bar for the panel is displayed.

-----------------------------------------

ni    : needsInit       [boolean] ['query', 'edit']
    (Internal) On Edit will mark the panel as requiring initialization. Query will return whether the panel is marked for initialization. Used during file -new and file -open.

-----------------------------------------

p     : parent          [string] []
    Specifies the parent layout for this panel.

-----------------------------------------

pmp   : popupMenuProcedure [script] ['query', 'edit']
    Specifies the procedure called for building the panel's popup menu(s). The default value is "buildPanelPopupMenu". The procedure should take one string argument which is the panel's name.

-----------------------------------------

rp    : replacePanel    [string] ['edit']
    Will replace the specified panel with this panel. If the target panel is within the same layout it will perform a swap.

-----------------------------------------

to    : tearOff         [boolean] ['query', 'edit']
    Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.

-----------------------------------------

toc   : tearOffCopy     [string] []
    Will create this panel as a torn of copy of the specified source panel.

-----------------------------------------

tor   : tearOffRestore  [boolean] ['edit']
    Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def cluster(q=1,e=1,af=1,ar=1,bf=1,bs=1,dt=1,en="float",ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,n="string",par=1,pr=1,rel=1,rm=1,rg=1,sp=1,wn="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cluster.html



-----------------------------------------

cluster is undoable, queryable, and editable.

The cluster command creates a cluster or edits the membership of an existing
cluster. The command returns the name of the cluster node upon creation of a
new cluster.

After creating a cluster, the cluster's weights can be modified using the
percent command or the set editor window.


-----------------------------------------


Return Value:

string[]  (the cluster node name and the cluster handle name)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

bs    : bindState       [boolean] []
    When turned on, this flag adds in a compensation to ensure the clustered objects preserve their spatial position when clustered. This is required to prevent the geometry from jumping at the time the cluster is created in situations when the cluster transforms at cluster time are not identity.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

en    : envelope        [float] ['query', 'edit']
    Set the envelope value for the deformer. Default is 1.0

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rel   : relative        [boolean] []
    Enable relative mode for the cluster. In relative mode, Only the transformations directly above the cluster are used by the cluster. Default is off.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

rg    : resetGeometry   [boolean] ['edit']
    Reset the geometry matrices for the objects being deformed by the cluster. This flag is used to get rid of undesirable effects that happen if you scale an object that is deformed by a cluster.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

wn    : weightedNode    [[string, string]]
    Transform node in the DAG above the cluster to which all percents are applied. The second DAGobject specifies the descendent of the first DAGobject from where the transformation matrix is evaluated. Default is the cluster handle.

    """

def combinationShape(q=1,e=1,add=1,ald=1,bs="string",cti="int",ctn="string",cm="int",dti="int",dtn="string",ex=1,rmd=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/combinationShape.html



-----------------------------------------

combinationShape is undoable, queryable, and editable.

Command to create or edit drive relationship of blend shape targets


-----------------------------------------


Return Value:

Int  In edit mode, return the newly created combination shape node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addDriver       [boolean] []
    Add drivers to the combination shape

-----------------------------------------

ald   : allDrivers      [boolean] ['query']
    All drivers of the combination shape

-----------------------------------------

bs    : blendShape      [string] []
    Associated blend shape node of the combination shape  In query mode, this flag can accept a value.

-----------------------------------------

cti   : combinationTargetIndex [int] []
    Driven blend shape target index of the combination shape  In query mode, this flag can accept a value.

-----------------------------------------

ctn   : combinationTargetName [string] []
    Driven blend shape target name of the combination shape  In query mode, this flag can accept a value.

-----------------------------------------

cm    : combineMethod   [int] ['query', 'edit']
    Combine method of the combination shape:    * 0 : Multiplication   * 1 : Lowest Weighting   * 2 : Lowest Weighting (Smooth)

-----------------------------------------

dti   : driverTargetIndex [int] []
    Driver blend shape target index of the combination shape

-----------------------------------------

dtn   : driverTargetName [string] []
    Driver blend shape target name of the combination shape

-----------------------------------------

ex    : exist           [boolean] ['query']
    If the combination shape exist

-----------------------------------------

rmd   : removeDriver    [boolean]
    Remove drivers from the combination shape

    """

def copyDeformerWeights(q=1,e=1,dd="string",ds="string",mi=1,mm="string",nm=1,sm=1,sd="string",ss="string",sa="string",uv="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/copyDeformerWeights.html



-----------------------------------------

copyDeformerWeights is undoable, queryable, and editable.

Command to copy or mirror the deformer weights accross one of the three major
axes. The command can be used to mirror weights either from one surface to
another or within the same surface.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dd    : destinationDeformer [string] ['query', 'edit']
    Specify the deformer used by the destination shape

-----------------------------------------

ds    : destinationShape [string] ['query', 'edit']
    Specify the destination deformed shape

-----------------------------------------

mi    : mirrorInverse   [boolean] ['query', 'edit']
    Values are mirrored from the positive side to the negative. If this flag is used then the direction is inverted.

-----------------------------------------

mm    : mirrorMode      [string] ['query', 'edit']
    The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.

-----------------------------------------

nm    : noMirror        [boolean] ['query', 'edit']
    When the no mirror flag is used, the weights are copied instead of mirrored.

-----------------------------------------

sm    : smooth          [boolean] ['query', 'edit']
    When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.

-----------------------------------------

sd    : sourceDeformer  [string] ['query', 'edit']
    Specify the deformer whose weights should be mirrored. When queried, returns the deformers used by the source shapes.

-----------------------------------------

ss    : sourceShape     [string] ['query', 'edit']
    Specify the source deformed shape

-----------------------------------------

sa    : surfaceAssociation [string] ['query', 'edit']
    The surfaceAssociation flag controls how the weights are transferred between the surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.

-----------------------------------------

uv    : uvSpace         [[string, string]]
    The uvSpace flag indicates that the weight transfer should occur in UV space, based on the source and destination UV sets specified.

    """

def deformer(q=1,e=1,af=1,ar=1,bf=1,dt=1,ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,n="string",par=1,pr=1,rm=1,sp=1,typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deformer.html



-----------------------------------------

deformer is undoable, queryable, and editable.

This command creates a deformer of the specified type. The deformer will
deform the selected objects.


-----------------------------------------


Return Value:

string[]  Name of the algorithm node created/edited.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

typ   : type            [string]
    Specify the type of deformer to create. This flag is required in create mode. Typically the type should specify a loaded plugin deformer. This command should typically not be used to create one of the standard deformers such as sculpt, lattice, blendShape, wire and cluster, since they have their own customized commands which perform useful specialized functionality.

    """

def deformerWeights(q=1,e=1,at="string",dv="float",df="string",ex=1,fm="string",ig=1,im=1,m="string",p="string",pt="float",r="string",sh="string",sk="string",vc=1,wp="uint",wt="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deformerWeights.html



-----------------------------------------

deformerWeights is undoable, queryable, and editable.

Command to import and export deformer weights to and from a simple XML file.
The weight data is stored in a per-vertex fashion along with a "point cloud"
corresponding to the vertices from the geometry input to the deformer. For
example a cluster deformer would have the following information:  On import
the weights are then mapped back to a specified deformer based on the
specified mapping method. Note that the geometry used to perform the mapping
association is not the visible shape but rather the incoming geometry to the
deformer. For example, in the case of a skin cluster this would be the bind
pose geometry.


-----------------------------------------


Return Value:

STRING  path to the file imported/exported, if successful    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] ['query', 'edit']
    Specify the long name of deformer attribute that should be imported/exported along with the deformerWeights. i.e. -at "envelope" -at "skinningMethod" etc.. No warning or error is given if a specified attribute does not exist on a particular deformer, making it possible to use this command with multiple deformers without aborting or slowing down the import/export process. Currently supports numeric attributes and matrix attributes

-----------------------------------------

dv    : defaultValue    [float] ['query', 'edit']
    Manually set the default value. Default values are values that are not written to file. For example, for blendShapes the default value is automatically set to 1.0 and these values are not written to disk. For skinClusters the value is 0.0. If all weights should be forced to be written to disk, set a defaultValue = -1.0.

-----------------------------------------

df    : deformer        [string] ['query', 'edit']
    Specify the deformer whose weights should be exported or imported. If a pattern is supplied for the deformer name (i.e: cluster*), only the first deformer that matches the pattern will be imported/exported unless used in conjunction with the -skip option

-----------------------------------------

ex    : export          [boolean] ['query', 'edit']
    Export the given deformer

-----------------------------------------

fm    : format          [string] ['query', 'edit']
    Specify either "XML" or "JSON" as the file extension to save as.

-----------------------------------------

ig    : ignoreName      [boolean] ['query', 'edit']
    Ignore the names of the layers on import, just use the order of the layers instead. This can be used when joint names have been changed. Leaving it on only name that match on import will be write to the deformer.

-----------------------------------------

im    : im              [boolean] ['query', 'edit']
    Import weights to the specified deformer. See the method flag for details on how the weights will be mapped to the destination deformer.

-----------------------------------------

m     : method          [string] ['query', 'edit']
    Specify the method used to map the weight during import. Valid values are: "index", "nearest", "barycentric", "bilinear" and "over". The "index" method uses the vertex index to map the weights onto the object. This is most useful when the destination object shares the same topology as the exported data. The "nearest" method finds the nearest vertex in the imported data set and sets the weight value to that value. This is best used when mapping a higher resolution mesh to a lower resolution. The "barycentric" and "bilinear" methods are only supported with polygon mesh exported with -vc/vertexConnections flag. The "barycentric" method finds the nearest triangle of the input geometry and rescales the weights at the triangle vertices according to the barycentric weights to each vertex of the nearest triangle. The "bilinear" method finds the nearest convex quad of the input geometry and rescales the weights at the quad vertices according to the bilinear weights to each vertex of the nearest convex quad. For non-quad polygon, the "bilinear" method will fall back to "barycentric" method. The "over" method is similar to the "index" method but the weights on the destination mesh are not cleared prior to mapping, so that unmatched indices keep their weights intact.

-----------------------------------------

p     : path            [string] ['query', 'edit']
    The path to the given file. Default to the current project.

-----------------------------------------

pt    : positionTolerance [float] ['query', 'edit']
    The position tolerance is used to determine the radius of search for the nearest method. This flag is only used with import. Defaults to a huge number.

-----------------------------------------

r     : remap           [string] ['query', 'edit']
    Remap maps source regular expression to destination format. It maps any name that matches the regular expression (before the semi-colon) to the expression format (after the semi-colon). For example, -remap "test:(.*);$1" will rename all items in the test namespace to the global namespace. Accepts $1, $2, .., $9 as pattern holders in the expression format. Remap flag must be used together with import or export. When working with import, the name of the object from the xml file matching the regular expression is remapped to object in scene. When working with export, the name of the object from the scene matching the regular expression is remapped to object in xml file.

-----------------------------------------

sh    : shape           [string] ['query', 'edit']
    Specify the source shape. Export will write out all the deformers on the shape node into one file. If a pattern is supplied for the shape name (i.e: pCylinder*), only the first shape that matches the pattern will be imported/exported unless used in conjunction with the -skip option.

-----------------------------------------

sk    : skip            [string] ['query', 'edit']
    Skip any deformer, shape, or layer that whose name matches the given regular expression string

-----------------------------------------

vc    : vertexConnections [boolean] ['query', 'edit']
    Export vertex connection information, which is required for -m/-method "barycentric" and "bilinear". The flag is only used with -ex/-export flag. The vertex connection information is automatically loaded during import if available in xml file.

-----------------------------------------

wp    : weightPrecision [uint] ['query', 'edit']
    Sets the output decimal precision for exported weights. The default value is 3.

-----------------------------------------

wt    : weightTolerance [float] ['query', 'edit']
    The weight tolerance is used to decide if a given weight value is close enough to the default value that it does not need to be included. This flag is only used with export. The default value is .001.

-----------------------------------------

ws    : worldSpace      [boolean]
    For spatially based association methods (nearest), the position should be based on the world space position rather then the local object space.

    """

def deltaMush(q=1,e=1,af=1,ar=1,bf=1,dt=1,en="float",ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,iwc="float",n="string",owc="float",par=1,pbv=1,pr=1,rm=1,si="uint",ss="float",sp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deltaMush.html



-----------------------------------------

deltaMush is undoable, queryable, and editable.

This command is used to create, edit and query deltaMush nodes.


-----------------------------------------


Return Value:

string  Delta mush deformer node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

en    : envelope        [float] ['query', 'edit']
    Envelope of the delta mush node. The envelope determines the percent of deformation. Value is clamped to [0, 1] range. Default is 1.

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

iwc   : inwardConstraint [float] ['query', 'edit']
    Constrains the movement of the vertex to not move inward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

owc   : outwardConstraint [float] ['query', 'edit']
    Constrains the movement of the vertex to not move outward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pbv   : pinBorderVertices [boolean] ['query', 'edit']
    If enabled, vertices on mesh borders will be pinned to their current position during smoothing. Default is true.

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

si    : smoothingIterations [uint] ['query', 'edit']
    Number of smoothing iterations performed by the delta mush node. Default is 10.

-----------------------------------------

ss    : smoothingStep   [float] ['query', 'edit']
    Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A higher value may lead to instabilities but converges faster compared to a lower value. Default is 0.5.

-----------------------------------------

sp    : split           [boolean]
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

    """

def dropoffLocator():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dropoffLocator.html



-----------------------------------------

dropoffLocator is undoable, NOT queryable, and NOT editable.

This command adds one or more dropoff locators to a wire curve, one for each
selected curve point. The dropoff locators can be used to provide localized
tuning of the wire deformation about the curve point.

The arguments are two floats, the envelope and percentage, followed by the
wire node name and then by the curve point(s).


-----------------------------------------


Return Value:

string[]  Locator name(s)
    """

def findDeformers():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/findDeformers.html



-----------------------------------------

findDeformers is undoable, NOT queryable, and NOT editable.

This command finds all deformers for the specified shape(s).

If no shapes are specified on the command then the curently selected shapes
are used.


-----------------------------------------


Return Value:

None
    """

def lattice(q=1,e=1,af=1,ar=1,bf=1,cp=1,dt=1,dv="[uint, uint, uint]",db=1,ex="string",fm=1,foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,lr=1,ldv="[uint, uint, uint]",n="string",oc=1,ofd="float",ol="uint",par=1,pos="[linear, linear, linear]",pr=1,rm=1,rt=1,ro="[angle, angle, angle]",s="[linear, linear, linear]",sp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lattice.html



-----------------------------------------

lattice is undoable, queryable, and editable.

This command creates a lattice deformer that will deform the selected objects.
If the object centered flag is used, the initial lattice will fit around the
selected objects. The lattice will be selected when the command is completed.
The lattice deformer has an associated base lattice. Only objects which are
contained by the base lattice will be deformed by the lattice.


-----------------------------------------


Return Value:

string[]  Ffd node name, lattice name, base lattice name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

cp    : commonParent    [boolean] []
    Group the base lattice and the deformed lattice under a common transform. This means that you can resize the lattice without affecting the deformation by resizing the common transform.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

dv    : divisions       [[uint, uint, uint]] ['query', 'edit']
    Set the number of lattice slices in x, y, z. Default is 2, 5, 2. When queried, this flag returns float float float. When you change the number of divisions, any tweaking or animation of lattice points must be redone.

-----------------------------------------

db    : dualBase        [boolean] []
    Create a special purpose ffd deformer node which accepts 2 base lattices. The default is off which results in the creation of a normal ffd deformer node. Intended for internal usage only.

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

fm    : freezeMapping   [boolean] ['query', 'edit']
    The base position of the geometries points is fixed at the time this flag is set. When mapping is frozen, moving the geometry with respect to the lattice will not cause the deformation to be recomputed.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

lr    : latticeReset    [boolean] ['edit']
    Reset the lattice to match its base position. This will undo any deformations that the lattice is causing. The lattice will only deform points that are enclosed within the lattice's reset (base) position.

-----------------------------------------

ldv   : ldivisions      [[uint, uint, uint]] ['query', 'edit']
    Set the number of local lattice slices in x, y, z.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

oc    : objectCentered  [boolean] []
    Centers the lattice around the selected object(s) or components. Default is off which centers the lattice at the origin.

-----------------------------------------

ofd   : outsideFalloffDistance [float] []
    Set the falloff distance used when the setting for transforming points outside of the base lattice is set to 2. The distance value is a positive number which specifies the size of the falloff distance as a multiple of the base lattice size, thus a value of 1.0 specifies that only points up to the base lattice width/height/depth away are transformed. A value of 0.0 is equivalent to an outsideLattice value of 0 (i.e. no points outside the base lattice are transformed). A huge value is equivalent to transforming an outsideLattice value of 1 (i.e. all points are transformed).

-----------------------------------------

ol    : outsideLattice  [uint] []
    Set the mode describing how points outside the base lattice are transformed. 0 (the default) specifies that no outside points are transformed. 1 specifies that all outside points are transformed, and 2 specifies that only those outside points which fall within the "falloff distance" (see the -ofd/outsideFalloffDistance flag) are transformed. When querying, the current setting for the lattice is returned.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pos   : position        [[linear, linear, linear]] []
    Used to specify the position of the newly created lattice.

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

rt    : removeTweaks    [boolean] ['edit']
    Remove any lattice deformations caused by moving lattice points. Translations/rotations and scales on the lattice itself are not removed.

-----------------------------------------

ro    : rotation        [[angle, angle, angle]] []
    Used to specify the initial rotation of the newly created lattice.

-----------------------------------------

s     : scale           [[linear, linear, linear]] []
    Used to specify the initial scale of the newly created lattice.

-----------------------------------------

sp    : split           [boolean]
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

    """

def nonLinear(q=1,e=1,af=1,ar=1,ap=1,bf=1,cp=1,ds=1,dt=1,ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,n="string",par=1,pr=1,rm=1,sp=1,typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nonLinear.html



-----------------------------------------

nonLinear is undoable, queryable, and editable.

This command creates a functional deformer of the specified type that will
deform the selected objects. The deformer consists of three nodes: The
deformer driver that gets connected to the history of the selected objects,
the deformer handle transform that controls position and orientation of the
axis of the deformation and the deformer handle that maintains the deformation
parameters. The type of the deformer handle shape created depends on the
specified type of the deformer. The deformer handle will be positioned at the
center of the selected objects' bounding box and oriented to match the
orientation of the leading object in the selection list. The deformer handle
transform will be selected when the command is completed.

The nonLinear command has some flags which are specific to the nonLinear type
specified with the -type flag. The flags correspond to the primary keyable
attributes related to the specific type of nonLinear node. For example, if the
type is "bend", then the flags "-curvature", "-lowBound" and "-highBound" may
be used to initialize, edit or query those attribute values on the bend node.
Examples of this are covered in the example section below.


-----------------------------------------


Return Value:

string[]  Deformer driver name, deformer handle transform name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

ap    : autoParent      [boolean] []
    Parents the deformer handle under the selected object's transform. This flag is valid only when a single object is selected.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

cp    : commonParent    [boolean] []
    Creates a new transform and parents the selected object and the deformer handle under it. This flag is valid only when a single object is selected.

-----------------------------------------

ds    : defaultScale    [boolean] []
    Sets the scale of the deformation handle to 1. By default the deformation handle is scaled to the match the largest dimension of the selected objects' bounding box. [deformerFlags] The attributes of the deformer handle shape can be set upon creation, edited and queried as normal flags using either the long or the short attribute name. e.g.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

typ   : type            [string]
    Specifies the type of deformation. The current valid deformation types are: bend, twist, squash, flare, sine and wave

    """

def percent(q=1,ap=1,dax="[linear, linear, linear]",dc="string",dds="linear",dp="[linear, linear, linear]",dt="string",mp=1,v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/percent.html



-----------------------------------------

percent is undoable, queryable, and NOT editable.

This command sets percent values on members of a weighted node such as a
cluster or a jointCluster. With no flags specified the command sets the
percent value for selected components of the specified node to the specified
percent value. A dropoff from the specified percent value to 0 can be
specified from a point, plane or curve using a dropoff distance around that
shape. The percent value can also be added or multiplied with existing percent
values of the node components.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : addPercent      [boolean] []
    Add the percent value specified with the -v flag to the existing percent values

-----------------------------------------

dax   : dropoffAxis     [[linear, linear, linear]] []
    Specifies the axis along which to dropoff the percent value, starting from the dropoffPosition.

-----------------------------------------

dc    : dropoffCurve    [string] []
    Specifies the curve around which to dropoff the percent value.

-----------------------------------------

dds   : dropoffDistance [linear] []
    Specifies the dropoff distance from the point, plane or curve that was specified using the -dp -dax or -dc flags.

-----------------------------------------

dp    : dropoffPosition [[linear, linear, linear]] []
    Specifies the point around which to dropoff the percent value.

-----------------------------------------

dt    : dropoffType     [string] []
    Specifies the type of dropoff. Used in conjunction with the -dp, -dax or -dc flags. Default is linear. Valid values are: linear, sine, exponential, linearSquared, none.

-----------------------------------------

mp    : multiplyPercent [boolean] []
    Multiply the percent value specified with the -v flag with existing percent values

-----------------------------------------

v     : value           [float]
    The percent value to be applied. The default is 1. In query mode, returns an array of doubles corresponding to the weights of the selected object components.

    """

def poseEditor(q=1,e=1,ctl=1,dt="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",lck=1,mlc="string",pnl="string",p="string",slc="string",sts=1,up=1,ulk=1,upd=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/poseEditor.html



-----------------------------------------

poseEditor is undoable, queryable, and editable.

This command creates an editor that derives from the base editor class that
has controls for deformer and control nodes.


-----------------------------------------


Return Value:

string  The name of the editor    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def posePanel(q=1,e=1,ctl=1,cp="string",cs=1,dt="string",dtg="string",es=1,ex=1,init=1,iu=1,l="string",mrl=1,mbv=1,ni=1,p="string",pmp="script",pe=1,rp="string",to=1,toc="string",tor=1,up=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/posePanel.html



-----------------------------------------

posePanel is undoable, queryable, and editable.

This command creates a panel that derives from the base panel class that
houses a poseEditor.


-----------------------------------------


Return Value:

string  The name of the panel    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ctl   : control         [boolean] ['query']
    Returns the top level control for this panel. Usually used for getting a parent to attach popup menus. CAUTION: panels may not have controls at times. This flag can return "" if no control is present.

-----------------------------------------

cp    : copy            [string] ['edit']
    Makes this panel a copy of the specified panel. Both panels must be of the same type.

-----------------------------------------

cs    : createString    [boolean] ['edit']
    Command string used to create a panel

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the Maya panel.

-----------------------------------------

es    : editString      [boolean] ['edit']
    Command string used to edit a panel

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

init  : init            [boolean] ['edit']
    Initializes the panel's default state. This is usually done automatically on file -new and file -open.

-----------------------------------------

iu    : isUnique        [boolean] ['query']
    Returns true if only one instance of this panel type is allowed.

-----------------------------------------

l     : label           [string] ['query', 'edit']
    Specifies the user readable label for the panel.

-----------------------------------------

mrl   : menuBarRepeatLast [boolean] ['query', 'edit']
    Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.

-----------------------------------------

mbv   : menuBarVisible  [boolean] ['query', 'edit']
    Controls whether the menu bar for the panel is displayed.

-----------------------------------------

ni    : needsInit       [boolean] ['query', 'edit']
    (Internal) On Edit will mark the panel as requiring initialization. Query will return whether the panel is marked for initialization. Used during file -new and file -open.

-----------------------------------------

p     : parent          [string] []
    Specifies the parent layout for this panel.

-----------------------------------------

pmp   : popupMenuProcedure [script] ['query', 'edit']
    Specifies the procedure called for building the panel's popup menu(s). The default value is "buildPanelPopupMenu". The procedure should take one string argument which is the panel's name.

-----------------------------------------

pe    : poseEditor      [boolean] ['query']
    Query only flag that returns the name of an editor to be associated with the panel.

-----------------------------------------

rp    : replacePanel    [string] ['edit']
    Will replace the specified panel with this panel. If the target panel is within the same layout it will perform a swap.

-----------------------------------------

to    : tearOff         [boolean] ['query', 'edit']
    Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.

-----------------------------------------

toc   : tearOffCopy     [string] []
    Will create this panel as a torn of copy of the specified source panel.

-----------------------------------------

tor   : tearOffRestore  [boolean] ['edit']
    Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def reorderDeformers(n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/reorderDeformers.html



-----------------------------------------

reorderDeformers is undoable, NOT queryable, and NOT editable.

This command changes the order in which 2 deformation nodes affect the output
geometry. The first string argument is the name of deformer1, the second is
deformer2, followed by the list of objects they deform.

It inserts deformer2 before deformer1. Currently supported deformer nodes
include: sculpt, cluster, jointCluster, lattice, wire, jointLattice,
boneLattice, blendShape.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

n     : name            [string]
    This flag is obsolete and is not used.

    """

def sculpt(q=1,e=1,af=1,ar=1,bf=1,dt=1,dds="linear",drt="string",ex="string",foc=1,g="string",gi=1,gwl=1,ignoreSelected=1,ihs=1,im="string",mxd="linear",m="string",n="string",oc=1,par=1,pr=1,rm=1,st="string",sp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sculpt.html



-----------------------------------------

sculpt is undoable, queryable, and editable.

This command creates/edits/queries a sculpt object deformer. By default for
creation mode an implicit sphere will be used as the sculpting object if no
sculpt tool is specified. The name of the created/edited object is returned.


-----------------------------------------


Return Value:

string[]  Sculpt algorithm node name, sculpt sphere name, and sculpt stretch
origin name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

dds   : dropoffDistance [linear] ['query', 'edit']
    Specifies the distance from the surface of the sculpt object at which the sculpt object produces no deformation effect. Default is 1.0. When queried, this flag returns a float.

-----------------------------------------

drt   : dropoffType     [string] ['query', 'edit']
    Specifies how the deformation effect drops off from maximum effect at the surface of the sculpt object to no effect at dropoff distance limit. Valid values are: linear | none. Default is linear. When queried, this flag returns a string.

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

gwl   : groupWithLocator [boolean] []
    Groups the sculptor and its locator together under a single transform. Default is off.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

im    : insideMode      [string] ['query', 'edit']
    Specifies how the deformation algorithm deals with points that are inside the sculpting primitve. The choices are: ring | even. The default is even. When queried, this flag returns a string. Ring mode will tend to produce a contour like ring of points around the sculpt object as it passes through an object while even mode will try to spread the points out as evenly as possible across the surface of the sculpt object.

-----------------------------------------

mxd   : maxDisplacement [linear] ['query', 'edit']
    Defines the maximum amount the sculpt object may move a point on an object which it is deforming. Default is 1.0. When queried, this flag returns a float.

-----------------------------------------

m     : mode            [string] ['query', 'edit']
    Specifies which deformation algorithm the sculpt object should use. The choices are: flip | project | stretch. The default is stretch. When queried, this flag returns a string.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

oc    : objectCentered  [boolean] []
    Places the sculpt and locator in the center of the bounding box of the selected object(s) or components. Default is off which centers the sculptor and locator at the origin.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

st    : sculptTool      [string] []
    Use the specified NURBS object as the sculpt tool instead of the default implicit sphere.

-----------------------------------------

sp    : split           [boolean]
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

    """

def sculptTarget(e=1,af=1,ar=1,bf=1,dt=1,ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ibw="float",ihs=1,n="string",par=1,pr=1,r=1,rm=1,s="int",sp=1,t="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sculptTarget.html



-----------------------------------------

sculptTarget is undoable, NOT queryable, and editable.

This command is used to specify the blend shape target to be modified by the
sculpting tools and transform manipulators.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

dt    : deformerTools   [boolean] []
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

ex    : exclusive       [string] []
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] []
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ibw   : inbetweenWeight [float] ['edit']
    Specifies the in between target weight of the blend shape node that will be made editable by the sculpting and transform tools.

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

r     : regenerate      [boolean] ['edit']
    When this flag is specified a new shape is created for the specified blend shape target, if the shape does not already exist. The name of the new shape is returned.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

s     : snapshot        [int] ['edit']
    This flag should only be used internally to add in-between target. When this flag is specified a snapshot of the shape will be taken for the specified in-between target when it does not exist yet. This flag specifies the base shape index and must be used with the -target and -inbetweenWeight flags, which specify the in-between target.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

t     : target          [int]
    Specifies the target index of the blend shape node that will be made editable by the sculpting and transform tools.

    """

def shapeEditor(q=1,e=1,cs=1,ctl=1,dt="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",lck=1,ls=1,mlc="string",pnl="string",p="string",slc="string",sts=1,tcl=1,tl=1,up=1,ulk=1,upd=1,ut="string",vs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shapeEditor.html



-----------------------------------------

shapeEditor is undoable, queryable, and editable.

This command creates an editor that derives from the base editor class that
has controls for deformer, control nodes.


-----------------------------------------


Return Value:

string  The name of the editor    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cs    : clearSelection  [boolean] ['edit']
    Clear the shape editor selection.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

ls    : lowestSelection [boolean] ['query']
    Query the lowest selection item.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

tcl   : targetControlList [boolean] ['query']
    Query the target control list.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Query the target list.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

vs    : verticalSliders [boolean]
    Should the sliders be vertical?

    """

def shapePanel(q=1,e=1,ctl=1,cp="string",cs=1,dt="string",dtg="string",es=1,ex=1,init=1,iu=1,l="string",mrl=1,mbv=1,ni=1,p="string",pmp="script",rp="string",se=1,to=1,toc="string",tor=1,up=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shapePanel.html



-----------------------------------------

shapePanel is undoable, queryable, and editable.

This command creates a panel that derives from the base panel class that
houses a shapeEditor.


-----------------------------------------


Return Value:

string  The name of the panel    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ctl   : control         [boolean] ['query']
    Returns the top level control for this panel. Usually used for getting a parent to attach popup menus. CAUTION: panels may not have controls at times. This flag can return "" if no control is present.

-----------------------------------------

cp    : copy            [string] ['edit']
    Makes this panel a copy of the specified panel. Both panels must be of the same type.

-----------------------------------------

cs    : createString    [boolean] ['edit']
    Command string used to create a panel

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the Maya panel.

-----------------------------------------

es    : editString      [boolean] ['edit']
    Command string used to edit a panel

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

init  : init            [boolean] ['edit']
    Initializes the panel's default state. This is usually done automatically on file -new and file -open.

-----------------------------------------

iu    : isUnique        [boolean] ['query']
    Returns true if only one instance of this panel type is allowed.

-----------------------------------------

l     : label           [string] ['query', 'edit']
    Specifies the user readable label for the panel.

-----------------------------------------

mrl   : menuBarRepeatLast [boolean] ['query', 'edit']
    Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.

-----------------------------------------

mbv   : menuBarVisible  [boolean] ['query', 'edit']
    Controls whether the menu bar for the panel is displayed.

-----------------------------------------

ni    : needsInit       [boolean] ['query', 'edit']
    (Internal) On Edit will mark the panel as requiring initialization. Query will return whether the panel is marked for initialization. Used during file -new and file -open.

-----------------------------------------

p     : parent          [string] []
    Specifies the parent layout for this panel.

-----------------------------------------

pmp   : popupMenuProcedure [script] ['query', 'edit']
    Specifies the procedure called for building the panel's popup menu(s). The default value is "buildPanelPopupMenu". The procedure should take one string argument which is the panel's name.

-----------------------------------------

rp    : replacePanel    [string] ['edit']
    Will replace the specified panel with this panel. If the target panel is within the same layout it will perform a swap.

-----------------------------------------

se    : shapeEditor     [boolean] ['query']
    Query only flag that returns the name of an editor to be associated with the panel.

-----------------------------------------

to    : tearOff         [boolean] ['query', 'edit']
    Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.

-----------------------------------------

toc   : tearOffCopy     [string] []
    Will create this panel as a torn of copy of the specified source panel.

-----------------------------------------

tor   : tearOffRestore  [boolean] ['edit']
    Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def softMod(q=1,e=1,af=1,ar=1,bf=1,bs=1,ci="int",cp="float",cv="float",dt=1,en="float",ex="string",fas=1,fbx=1,fby=1,fbz=1,fc="[float, float, float]",fm=1,fom="int",fr="float",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,n="string",par=1,pr=1,rel=1,rm=1,rg=1,sp=1,wn="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/softMod.html



-----------------------------------------

softMod is undoable, queryable, and editable.

The softMod command creates a softMod or edits the membership of an existing
softMod. The command returns the name of the softMod node upon creation of a
new softMod.


-----------------------------------------


Return Value:

string  [] (the softMod node name and the softMod handle name)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

bs    : bindState       [boolean] []
    Specifying this flag adds in a compensation to ensure the softModed objects preserve their spatial position when softModed. This is required to prevent the geometry from jumping at the time the softMod is created in situations when the softMod transforms at softMod time are not identity.

-----------------------------------------

ci    : curveInterpolation [int] []
    Ramp interpolation corresponding to the specified curvePoint position. Integer values of 0-3 are valid, corresponding to "none", "linear", "smooth" and "spline" respectively. This flag may only be used in conjunction with the curvePoint and curveValue flag.

-----------------------------------------

cp    : curvePoint      [float] []
    Position of ramp value on normalized 0-1 scale. This flag may only be used in conjunction with the curveInterpolation and curveValue flags.

-----------------------------------------

cv    : curveValue      [float] []
    Ramp value corresponding to the specified curvePoint position. This flag may only be used in conjunction with the curveInterpolation and curvePoint flags.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

en    : envelope        [float] ['query', 'edit']
    Set the envelope value for the deformer. Default is 1.0

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

fas   : falloffAroundSelection [boolean] []
    Falloff will be calculated around any selected components

-----------------------------------------

fbx   : falloffBasedOnX [boolean] []
    Falloff will be calculated using the X component.

-----------------------------------------

fby   : falloffBasedOnY [boolean] []
    Falloff will be calculated using the Y component.

-----------------------------------------

fbz   : falloffBasedOnZ [boolean] []
    Falloff will be calculated using the Z component.

-----------------------------------------

fc    : falloffCenter   [[float, float, float]] []
    Set the falloff center point of the softMod.

-----------------------------------------

fm    : falloffMasking  [boolean] []
    Deformation will be restricted to selected components

-----------------------------------------

fom   : falloffMode     [int] []
    Set the falloff method used for the softMod.

-----------------------------------------

fr    : falloffRadius   [float] []
    Set the falloff radius of the softMod.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rel   : relative        [boolean] []
    Enable relative mode for the softMod. In relative mode, Only the transformations directly above the softMod are used by the softMod. Default is off.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

rg    : resetGeometry   [boolean] ['edit']
    Reset the geometry matrices for the objects being deformed by the softMod. This flag is used to get rid of undesirable effects that happen if you scale an object that is deformed by a softMod.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

wn    : weightedNode    [[string, string]]
    Transform node in the DAG above the softMod to which all percents are applied. The second node specifies the descendent of the first node from where the transformation matrix is evaluated. Default is the softMod handle.

    """

def substituteGeometry(dnd=1,ngl=1,ogl=1,wdt="float",rog=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/substituteGeometry.html



-----------------------------------------

substituteGeometry is undoable, NOT queryable, and NOT editable.

This command can be used to replace the geometry which is already connected to
deformers with a new geometry. The weights on the old geometry will be
retargeted to the new geometry.


-----------------------------------------


Return Value:

string  Name of shapes that were replaced


-----------------------------------------


Flags:

-----------------------------------------

dnd   : disableNonSkinDeformers [boolean] []
    This flag controls the state of deformers other than skin deformers after the substitution has taken place. If the flag is true then non-skin deformer nodes are left in a disabled state at the completion of the command. Default value is false.

-----------------------------------------

ngl   : newGeometryToLayer [boolean] []
    Create a new layer for the new geometry.

-----------------------------------------

ogl   : oldGeometryToLayer [boolean] []
    Create a new layer and move the old geometry to this layer

-----------------------------------------

wdt   : reWeightDistTolerance [float] []
    Specify the distance tolerance value to be used for retargeting weights. While transferring weights the command tries to find the corresponding vertices by overlapping the geometries with all deformers disabled. Sometimes this results in selection of unrelated vertices. (Example when a hole in the old geometry has been filled with new vertices in the new geometry.) This distance tolerance value is used to detect this kind of faults and either ignore these cases or to vary algorithm to find more corresponding vertices.

-----------------------------------------

rog   : retainOldGeometry [boolean]
    A copy of the old geometry should be retained

    """

def tension(q=1,e=1,af=1,ar=1,bf=1,dt=1,en="float",ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,iwc="float",n="string",owc="float",par=1,pbv=1,pr=1,rm=1,si="uint",ss="float",sp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/tension.html



-----------------------------------------

tension is undoable, queryable, and editable.

This command is used to create, edit and query tension nodes.


-----------------------------------------


Return Value:

string  Tension deformer node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

en    : envelope        [float] ['query', 'edit']
    Envelope of the tension node. The envelope determines the percent of deformation. Value is clamped to [0, 1] range. Default is 1.

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

iwc   : inwardConstraint [float] ['query', 'edit']
    Constrains the movement of the vertex to not move inward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

owc   : outwardConstraint [float] ['query', 'edit']
    Constrains the movement of the vertex to not move outward from the input deforming shape to preserve the contour. Value is in the [0,1] range.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pbv   : pinBorderVertices [boolean] ['query', 'edit']
    If enabled, vertices on mesh borders will be pinned to their current position during smoothing. Default is true.

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

si    : smoothingIterations [uint] ['query', 'edit']
    Number of smoothing iterations performed by the tension node. Default is 10.

-----------------------------------------

ss    : smoothingStep   [float] ['query', 'edit']
    Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A higher value may lead to instabilities but converges faster compared to a lower value. Default is 0.5.

-----------------------------------------

sp    : split           [boolean]
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

    """

def textureDeformer(q=1,e=1,af=1,ar=1,bf=1,dt=1,d="string",en="float",ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,n="string",o="float",par=1,ps="string",pr=1,rm=1,sp=1,s="float",vo="[float, float, float]",vsp="string",vs="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/textureDeformer.html



-----------------------------------------

textureDeformer is undoable, queryable, and editable.

This command creates a texture deformer for the object. The selected objects
are the input geometry objects. The deformer node name will be returned.


-----------------------------------------


Return Value:

string  Texture deformer node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

d     : direction       [string] []
    Set the deformation direction of texture deformer It can only handle three types: "Normal", "Handle" and "Vector". "Normal" each vertices use its own normal vector. "Handle" all vertices use Up vector of the handle. "Vector" each vertices use RGB color vector strings.

-----------------------------------------

en    : envelope        [float] []
    Set the envelope of texture deformer. Envelope determines the percent of deformation. The final result is (color * normal * strength + offset) * envelope

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

o     : offset          [float] []
    Set the offset of texture deformer. Offset plus a translation on the final deformed vertices.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ps    : pointSpace      [string] []
    Set the point space of texture deformer. It can only handle three strings: "World", "Local" and "UV". "World" map world space to color space. "Local" map local space to color space. "UV" map UV space to color space. strings.

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

s     : strength        [float] []
    Set the strength of texture deformer. Strength determines how strong the object is deformed.

-----------------------------------------

vo    : vectorOffset    [[float, float, float]] []
    Set the vector offset of texture deformer. Vector offset indicates the offset of the deformation on the vector mode.

-----------------------------------------

vsp   : vectorSpace     [string] []
    Set the vector space of texture deformer. It can only handle three strings: "Object", "World" and "Tangent". "Object" use color vector in object space "World" use color vector in world space "Tangent" use color vector in tangent space strings.

-----------------------------------------

vs    : vectorStrength  [[float, float, float]]
    Set the vector strength of texture deformer. Vector strength determines how strong the object is deformed on the vector mode.

    """

def wire(q=1,e=1,af=1,ar=1,bf=1,ce="float",dt=1,dds="[uint, linear]",en="float",ex="string",foc=1,g="string",gi=1,gw=1,ho="[uint, string]",ignoreSelected=1,ihs=1,li="float",n="string",par=1,pr=1,rm=1,sp=1,w="string",wc="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/wire.html



-----------------------------------------

wire is undoable, queryable, and editable.

This command creates a wire deformer.  
In the create mode the selection list is treated as the object(s) to be
deformed, Wires are specified with the -w flag. Each wire can optionally have
a holder which helps define the the regon of the object that is affected by
the deformer.


-----------------------------------------


Return Value:

string[]  The wire node name and the wire curve name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ce    : crossingEffect  [float] ['query', 'edit']
    Set the amount of convolution effect. Varies from fully convolved at 0 to a simple additive effect at 1 (which is what you get with the filter off). Default is 0.  This filter should make its way into all blend nodes that deal with combining effects from multiple sources.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

dds   : dropoffDistance [[uint, linear]] ['query', 'edit']
    Set the dropoff distance (second parameter) for the wire at index (first parameter).

-----------------------------------------

en    : envelope        [float] ['query', 'edit']
    Set the envelope value for the deformer. Default is 1.0

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

gw    : groupWithBase   [boolean] []
    Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.

-----------------------------------------

ho    : holder          [[uint, string]] ['query', 'edit']
    Set the specified curve or surface (second parameter as a holder for the wire at index (first parameter).

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

li    : localInfluence  [float] ['query', 'edit']
    Set the local control a wire has with respect to other wires irrespective of whether it is deforming the surface. Varies from no local effect at 0 to full local control at 1. Default is 0.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

w     : wire            [string] ['query', 'edit']
    Specify or query the wire curve name.

-----------------------------------------

wc    : wireCount       [uint]
    Set the number of wires.

    """

def wrinkle(ax="[linear, linear, linear]",brc="uint",bd="uint",ct="[linear, linear, linear]",cr="string",dds="linear",en="linear",rnd="linear",st="string",th="linear",uv="[linear, linear, linear, linear, linear]",wc="uint",wi="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/wrinkle.html



-----------------------------------------

wrinkle is undoable, NOT queryable, and NOT editable.

The wrinkle command is used to create a network of wrinkles on a surface. It
automatically creates a network of wrinkle curves that control a wire
deformer. The wrinkle curves are attached to a cluster deformer.


-----------------------------------------


Return Value:

string[]  List of clusters created followed by list of wire deformers created.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] []
    Specifies the plane of the wrinkle.

-----------------------------------------

brc   : branchCount     [uint] []
    Specifies the number of branches per wrinkle. Default is 2.

-----------------------------------------

bd    : branchDepth     [uint] []
    Specifies the depth of the branching. Default is 0.

-----------------------------------------

ct    : center          [[linear, linear, linear]] []
    Specifies the center of the wrinkle.

-----------------------------------------

cr    : crease          [string] []
    Specifies an existing curve to serve as the wrinkle.

-----------------------------------------

dds   : dropoffDistance [linear] []
    Specifies the dropoff distance around the center.

-----------------------------------------

en    : envelope        [linear] []
    The envelope globally attenuates the amount of deformation. Default is 1.0.

-----------------------------------------

rnd   : randomness      [linear] []
    Amount of randomness. Default is 0.2.

-----------------------------------------

st    : style           [string] []
    Specifies the wrinkle style. Valid values are "radial" or "tangential"

-----------------------------------------

th    : thickness       [linear] []
    Wrinkle thickness. Default is 1.0.

-----------------------------------------

uv    : uvSpace         [[linear, linear, linear, linear, linear]] []
    1/2 length, 1/2 breadth, rotation angle, center u, v definition of a patch in uv space where the wrinkle is to be constructed.

-----------------------------------------

wc    : wrinkleCount    [uint] []
    Specifies the number of wrinkle lines to be generated. Default is 3.

-----------------------------------------

wi    : wrinkleIntensity [linear]
    Increasing the intensity makes it more wrinkly. Default is 0.5.

    """

def bindSkin(q=1,e=1,bcp=1,bp=1,cj=1,d=1,dnd=1,en=1,n="string",p="string",ta=1,tsb=1,ts=1,ub=1,ubk=1,ul=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bindSkin.html



-----------------------------------------

bindSkin is undoable, queryable, and editable.

This command binds the currently selected objects to the currently selected
skeletons. Shapes which can be bound are: meshes, nurbs curves, nurbs
surfaces, lattices, subdivision surfaces, and API shapes. Multiple shapes and
multiple skeletons can be bound at once by selecting them or specifying them
on the command line. Selection order is not important.

The skin is bound using the so-called "rigid" bind, in which the components
are rigidly attached to the closest bone in the skeleton. Flexors can later be
added to the skeleton to smooth out the skinning around joints.

The skin(s) can be bound either to the entire skeleton hierarchy of the
selected joint(s), or to only the selected joints. The entire hierarchy is the
default. The -tsb/-toSelectedBones flag allows binding to only the selected
bones.

This command can also be used to detach the skin from the skeleton. Detaching
the skin is useful in a variety of situations, such as: inserting additional
bones, deleting bones, changing the bind position of the skeleton or skin, or
simply getting rid of the skinning nodes altogether. The options to use when
detaching the skin depend on how much of the skinning info you want to get rid
of. Namely: (1) -delete or -unbind: remove all skinning nodes, (2)
-unbindKeepHistory: remove the skinning sets, but keep the weights, (3)
-disable: disable the skinning but keep the skinning sets and the weights.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bcp   : byClosestPoint  [boolean] []
    bind each point in the object to the segment closest to the point. The byClosestPoint and byPartition flags are mutually exclusive. The byClosestPoint flag is the default.

-----------------------------------------

bp    : byPartition     [boolean] []
    bind each group in the partition to the segment closest to the group's centroid. A partition must be specified with the -p/-partition flag

-----------------------------------------

cj    : colorJoints     [boolean] []
    In bind mode, this flag assigns colors to the joints based on the colors assigned to the joint's skin set. In delete and unlock mode, this flag removes the colors from joints that are no longer bound as skin. In disable and unbindKeepHistory mode, this flag does nothing.

-----------------------------------------

d     : delete          [boolean] []
    Detach the skin on the selected skeletons and remove all bind- related construction history.

-----------------------------------------

dnd   : doNotDescend    [boolean] []
    Do not descend to shapes that are parented below the selected object(s). Bind only the selected objects.

-----------------------------------------

en    : enable          [boolean] []
    Enable or disable a bind that has been disabled on the selected skeletons. To enable the bind on selected bones only, select the bones and use the -tsb flag with the -en flag. This flag is used when you want to temporarily disable the bind without losing the set information or the weight information of the skinning, for example if you want to modify the bindPose.

-----------------------------------------

n     : name            [string] []
    This flag is obsolete.

-----------------------------------------

p     : partition       [string] []
    Specify a partition to bind by. This is only valid when used with the -bp/-byPartition flag.

-----------------------------------------

ta    : toAll           [boolean] []
    objects will be bound to the entire selected skeletons. Even bones with zero influence will be bound, whereas the toSkeleton will only bind non-zero influences.

-----------------------------------------

tsb   : toSelectedBones [boolean] []
    objects will be bound to the selected bones only.

-----------------------------------------

ts    : toSkeleton      [boolean] []
    objects will be bound to the selected skeletons. The toSkeleton, toAll and toSelectedBones flags are mutually exclusive. The toSkeleton flag is the default.

-----------------------------------------

ub    : unbind          [boolean] []
    unbind the selected objects. They will no longer move with the skeleton. Any bindSkin history that is no longer used will be deleted.

-----------------------------------------

ubk   : unbindKeepHistory [boolean] []
    unbind the selected objects. They will no longer move with the skeleton. However, existing weights on the skin will be kept for use the next time the skin is bound. This option is appropriate if you want to modify the skeleton without losing the weighting information on the skin.

-----------------------------------------

ul    : unlock          [boolean]
    unlock the selected objects. Since bindSkin will no longer give normal results if bound objects are moved away from the skeleton, bindSkin locks translate, rotate and scale. This command unlocks the selected objects translate, rotate and scale.

    """

def boneLattice(q=1,e=1,af=1,ar=1,bf=1,bi="float",dt=1,ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,j="string",li="float",lo="float",n="string",par=1,pr=1,rm=1,sp=1,t="string",tr="float",wl="float",wr="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/boneLattice.html



-----------------------------------------

boneLattice is undoable, queryable, and editable.

This command creates/edits/queries a boneLattice deformer. The name of the
created/edited object is returned. Usually you would make use of this
functionality through the higher level flexor command.


-----------------------------------------


Return Value:

string  Name of bone lattice algorithm node created/edited.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

bi    : bicep           [float] ['query', 'edit']
    Affects the bulging of lattice points on the inside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

j     : joint           [string] ['query', 'edit']
    Specifies which joint will be used to drive the bulging behaviors.

-----------------------------------------

li    : lengthIn        [float] ['query', 'edit']
    Affects the location of lattice points along the upper half of the bone. Positive/negative values cause the points to move away/towards the center of the bone. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

lo    : lengthOut       [float] ['query', 'edit']
    Affects the location of lattice points along the lower half of the bone. Positive/negative values cause the points to move away/towards the center of the bone. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

t     : transform       [string] []
    Specifies which dag node is being used to rigidly transform the lattice which this node is going to deform. If this flag is not specified an identity matrix will be assumed.

-----------------------------------------

tr    : tricep          [float] ['query', 'edit']
    Affects the bulging of lattice points on the outside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

wl    : widthLeft       [float] ['query', 'edit']
    Affects the bulging of lattice points on the left side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

wr    : widthRight      [float]
    Affects the bulging of lattice points on the right side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

    """

def copyFlexor():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/copyFlexor.html



-----------------------------------------

copyFlexor is undoable, NOT queryable, and NOT editable.

This command copies an existing bone or joint flexor from one bone (joint) to
another. The attributes of the flexor and their connections as well as any
tweaks in on the latticeFfd are copied from the original to the new flexor. If
the selected bone (joint) appears to be a mirror reflection of the bone
(joint) of the existing flexor then the transform of the ffd lattice group
gets reflected to the new bone (joint). The arguments for the command are the
name of the ffd Lattice and the name of the destination joint. If they are not
specified at the command line, they will be picked up from the current
selection list.


-----------------------------------------


Return Value:

string  The name of the new flexor node
    """

def copySkinWeights(q=1,e=1,ds="string",ia="string",mi=1,mm="string",nbw=1,nm=1,nr=1,spa="uint",sm=1,ss="string",sa="string",uv="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/copySkinWeights.html



-----------------------------------------

copySkinWeights is undoable, queryable, and editable.

Command to copy or mirror the skinCluster weights accross one of the three
major axes. The command can be used to mirror weights either from one surface
to another or within the same surface.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ds    : destinationSkin [string] ['query', 'edit']
    Specify the destination skin shape

-----------------------------------------

ia    : influenceAssociation [string] ['query', 'edit']
    The influenceAssociation flag controls how the influences on the source and target skins are matched up. The flag can be included multiple times to specify multiple association schemes that will be invoked one after the other until all influences have been matched up. Supported values are "closestJoint", "closestBone", "label", "name", "oneToOne". The default is closestJoint.

-----------------------------------------

mi    : mirrorInverse   [boolean] ['query', 'edit']
    Values are mirrored from the positive side to the negative. If this flag is used then the direction is inverted.

-----------------------------------------

mm    : mirrorMode      [string] ['query', 'edit']
    The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.

-----------------------------------------

nbw   : noBlendWeight   [boolean] ['query', 'edit']
    When the no blend flag is used, the blend weights on the skin cluster will not be copied across to the destination.

-----------------------------------------

nm    : noMirror        [boolean] ['query', 'edit']
    When the no mirror flag is used, the weights are copied instead of mirrored.

-----------------------------------------

nr    : normalize       [boolean] ['query', 'edit']
    Normalize the skin weights.

-----------------------------------------

spa   : sampleSpace     [uint] ['query', 'edit']
    Selects which space the attribute transfer is performed in. 0 is world space, 1 is model space. The default is world space.

-----------------------------------------

sm    : smooth          [boolean] ['query', 'edit']
    When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.

-----------------------------------------

ss    : sourceSkin      [string] ['query', 'edit']
    Specify the source skin shape

-----------------------------------------

sa    : surfaceAssociation [string] ['query', 'edit']
    The surfaceAssociation flag controls how the weights are transferred between the surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.

-----------------------------------------

uv    : uvSpace         [[string, string]]
    The uvSpace flag indicates that the weight transfer should occur in UV space, based on the source and destination UV sets specified.

    """

def dagPose(q=1,e=1,a=1,ap=1,bp=1,g=1,m=1,n="string",rm=1,rs=1,r=1,s=1,sl=1,wp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dagPose.html



-----------------------------------------

dagPose is undoable, queryable, and editable.

This command is used to save and restore the matrix information for a dag
hierarchy. Specifically, the data stored will restore the translate, rotate,
scale, scale pivot, rotate pivot, rotation order, and (for joints) joint order
for all the objects on the hierarchy. Data for other attributes is not stored
by this command.

This command can also be used to store a bindPose for an object. When you skin
an object, a dagPose is automatically created for the skin.


-----------------------------------------


Return Value:

string  Name of pose    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : addToPose       [boolean] []
    Allows adding the selected items to the dagPose.

-----------------------------------------

ap    : atPose          [boolean] ['query']
    Query whether the hierarchy is at same position as the pose. Names of hierarchy members that are not at the pose position will be returned. An empty return list indicates that the hierarchy is at the pose.

-----------------------------------------

bp    : bindPose        [boolean] ['query']
    Used to specify the bindPose for the selected hierarchy. Each hierarchy can have only a single bindPose, which is saved automatically at the time of a skin bind. The bindPose is used when adding influence objects, binding new skins, or adding flexors. Take care when modifying the bindPose with the -rs/-reset or -rm/-remove flags, since if the bindPose is ill-defined it can cause problems with subsequent skinning operations.

-----------------------------------------

g     : g               [boolean] []
    This flag can be used in conjunction with the restore flag to signal that the members of the pose should be restored to the global pose. The global pose means not only is each object locally oriented with respect to its parents, it is also in the same global position that it was at when the pose was saved. If a hierarchy's parenting has been changed since the time that the pose was saved, you may have trouble reaching the global pose.

-----------------------------------------

m     : members         [boolean] ['query']
    Query the members of the specified pose. The pose should be specified using the selection list, the -bp/-bindPose or the -n/-name flag.

-----------------------------------------

n     : name            [string] ['query']
    Specify the name of the pose. This can be used during create, restore, reset, remove, and query operations to specify the pose to be created or acted upon.

-----------------------------------------

rm    : remove          [boolean] []
    Remove the selected joints from the specified pose.

-----------------------------------------

rs    : reset           [boolean] []
    Reset the pose on the selected joints. If you are resetting pose data for a bindPose, take care. It is appropriate to use the -rs/-reset flag if a joint has been reparented and/or appears to be exactly at the bindPose. However, a bindPose that is much different from the exact bindPose can cause problems with subsequent skinning operations.

-----------------------------------------

r     : restore         [boolean] []
    Restore the hierarchy to a saved pose. To specify the pose, select the pose node, or use the -bp/-bindPose or -n/-name flag.

-----------------------------------------

s     : save            [boolean] []
    Save a dagPose for the selected dag hierarchy. The name of the new pose will be returned.

-----------------------------------------

sl    : selection       [boolean] ['query']
    Whether or not to store a pose for all items in the hierarchy, or for only the selected items.

-----------------------------------------

wp    : worldParent     [boolean]
    Indicates that the selected pose member should be recalculated as if it is parented to the world. This is typically used when you plan to reparent the object to world as the next operation.

    """

def flexor(q=1,e=1,ab=1,aj=1,dc="string",l=1,n="string",ns=1,ts=1,typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/flexor.html



-----------------------------------------

flexor is undoable, queryable, and editable.

This command creates a flexor. A flexor a deformer plus a set of driving
attributes. For example, a flexor might be a sculpt object that is driven by a
joint's x rotation and a cube's y position.


-----------------------------------------


Return Value:

string[]  (the names of the new flexor nodes)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ab    : atBones         [boolean] []
    Add a flexor at bones. Flexor will be added at each of the selected bones, or at all bones in the selected skeleton if the -ts flag is also specified.

-----------------------------------------

aj    : atJoints        [boolean] []
    Add a flexor at joints. Flexor will be added at each of the selected joints, or at all joints in the selected skeleton if the -ts flag is specified.

-----------------------------------------

dc    : deformerCommand [string] []
    String representing underlying deformer command string.

-----------------------------------------

l     : list            [boolean] ['query']
    List all possible types of flexors. Query mode only.

-----------------------------------------

n     : name            [string] []
    This flag is obsolete.

-----------------------------------------

ns    : noScale         [boolean] []
    Do not auto-scale the flexor to the size of the nearby geometry.

-----------------------------------------

ts    : toSkeleton      [boolean] []
    Specifies that flexors will be added to the entire skeleton rather than just to the selected joints/bones. This flag is used in conjunction with the -ab and -aj flags.

-----------------------------------------

typ   : type            [string]
    Specifies which type of flexor. To see list of valid types, use the "flexor -query -list" command.

    """

def geomBind(q=1,e=1,bm="uint",fo="float",gvp="[uint, boolean]",mi="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/geomBind.html



-----------------------------------------

geomBind is undoable, queryable, and editable.

This command is used to compute weights using geodesic voxel binding
algorithm. It works by setting the right weights values on an already-existing
skinCluster node.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bm    : bindMethod      [uint] []
    Specifies which bind algorithm to use. By default, Geodesic Voxel will be used. Available algorithms are: 3 - Geodesic Voxel

-----------------------------------------

fo    : falloff         [float] ['query', 'edit']
    Falloff controlling the bind stiffness. Valid values range from [0..1].

-----------------------------------------

gvp   : geodesicVoxelParams [[uint, boolean]] ['query', 'edit']
    Specifies the geodesic voxel binding parameters. This flag is composed of three parameters: 0 - Maximum voxel grid resolution which must be a power of two. (ie. 64, 128, 256, etc. ) 1 - Performs a post voxel state validation when enabled. Default values are 256 true.

-----------------------------------------

mi    : maxInfluences   [int]
    Specifies the maximum influences a vertex can have. By default, all influences are used (-1).

    """

def jointLattice(q=1,e=1,af=1,ar=1,bf=1,cr="float",dt=1,ex="string",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,j="string",li="float",lo="float",lb="string",lt="string",n="string",par=1,pr=1,rm=1,ro="float",sp=1,ub="string",ut="string",wl="float",wr="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/jointLattice.html



-----------------------------------------

jointLattice is undoable, queryable, and editable.

This command creates/edits/queries a jointLattice deformer. The name of the
created/edited object is returned. Usually you would make use of this
functionality through the higher level flexor command.


-----------------------------------------


Return Value:

string  Name of joint lattice algorithm node created/edited.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

cr    : creasing        [float] ['query', 'edit']
    Affects the bulging of lattice points on the inside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

j     : joint           [string] []
    Specifies the joint which will be used to drive the bulging behaviours.

-----------------------------------------

li    : lengthIn        [float] ['query', 'edit']
    Affects the location of lattice points on the parent bone. Positive/negative values cause the points to move away/towards the joint. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

lo    : lengthOut       [float] ['query', 'edit']
    Affects the location of lattice points on the child bone. Positive/negative values cause the points to move away/towards the joint. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

lb    : lowerBindSkin   [string] []
    Specifies the node which is performing the bind skin operation on the geometry associated with the lower bone.

-----------------------------------------

lt    : lowerTransform  [string] []
    Specifies which dag node is being used to rigidly transform the lower part of the lattice which this node is going to deform. If this flag is not specified an identity matrix will be assumed.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

ro    : rounding        [float] ['query', 'edit']
    Affects the bulging of lattice points on the outside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ub    : upperBindSkin   [string] []
    Specifies the node which is performing the bind skin operation on the geometry associated with the upper bone.

-----------------------------------------

ut    : upperTransform  [string] []
    Specifies which dag node is being used to rigidly transform the upper part of the lattice which this node is going to deform. If this flag is not specified an identity matrix will be assumed.

-----------------------------------------

wl    : widthLeft       [float] ['query', 'edit']
    Affects the bulging of lattice points on the left side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

-----------------------------------------

wr    : widthRight      [float]
    Affects the bulging of lattice points on the right side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.

    """

def polyUniteSkinned(q=1,e=1,cp=1,ch=1,muv="int",op=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyUniteSkinned.html



-----------------------------------------

polyUniteSkinned is undoable, queryable, and editable.

Command to combine poly mesh objects (as polyUnite) while retaining the smooth
skinning setup on the combined object.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cp    : centerPivot     [boolean] ['query', 'edit']
    Set the resulting object's pivot to the center of the selected objects bounding box.

-----------------------------------------

ch    : constructionHistory [boolean] ['query', 'edit']
    Turn the construction history on or off.

-----------------------------------------

muv   : mergeUVSets     [int] ['query', 'edit']
    Specify how UV sets will be merged on the output mesh. The choices are 0 | 1 | 2. 0 = Do not merge. Each UV set on each mesh will become a new UV set in the output. 1 = Merge by name. UV sets with the same name will be merged. 2 = Merge by UV links. UV sets will be merged so that UV linking on the input meshes continues to work. The default is 1 (merge by name).

-----------------------------------------

op    : objectPivot     [boolean]
    Set the resulting object's pivot to last selected object's pivot.

    """

def skeletonEmbed(q=1,mm=1,sm="uint",sr="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/skeletonEmbed.html



-----------------------------------------

skeletonEmbed is undoable, queryable, and NOT editable.

This command is used to embed a skeleton inside meshes.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

mm    : mergedMesh      [boolean] ['query']
    When specified, the query command merges selected meshes together and returns a Python object representing the merged mesh.

-----------------------------------------

sm    : segmentationMethod [uint] []
    Specifies which segmentation algorithm to use to determine what is inside the mesh and what is outside the mesh. By default, boundary-and-fill- and-grow voxelization will be used.  Available algorithms are:    * 0 : Perfect mesh (no voxelization). This method works for "perfect meshes", i.e. meshes that are closed, watertight, 2-manifold and without self-intersection or interior/hidden geometry. It segments the interior region of the mesh from the exterior using a pseudo-normal test. It does not use voxelization. If mesh conditions are not respected, the segmentation is likely to be wrong. This can make the segmentation process significantly longer and prevent successful skeleton embedding.    * 1 : Watertight mesh (flood fill). This method works for "watertight meshes", i.e. meshes for which faces completely separate the interior region of the mesh from the exterior. The mesh can have degenerated faces, wrong face orientation, self-intersection, etc. The method uses surface voxelization to classify as part of the interior region all voxels intersecting with a mesh face. It then performs flood-filling from the outside, marking all reached voxels as part of the exterior region of the model. Finally, all unreached voxels are marked as part of the interior region. This method works so long as the mesh is watertight, i.e. without holes up to the voxelization resolution. Otherwise, flood-filling reaches the interior region and creates inaccurate segmentation.    * 2 : Imperfect mesh (flood fill + growing). This method works for meshes where holes could make the flood-filling step reach the interior region of the mesh, but that have face orientation consistent enough so filling them is possible. First, it uses surface voxelization to classify as part of the interior region all voxels intersecting with a mesh face. It then alternates flood-filling and growing steps. The flood-filling tries to reach all voxels from the outside so that unreached voxels are marked as part of the interior region. The growing step uses a relatively computation-intensive process to check for interior voxels in all neighbors to those already identified. Any voxel identified as interior is likely to fill holes, allowing subsequent flood-filling steps to identify more interior voxels.    * 3 : Polygon soup (repair). This method has no manifold or face orientation requirements. It reconstructs a mesh that wraps the input mesh with a given offset (3 times the voxel size) and uses this perfect 2-manifold mesh to segment the interior region from the exterior region of the model. Because of the offset, it might lose some of the details and merge parts that are proximal. However, this usually is not an issue with common models where body parts are not too close to one another.    * 99 : Direct skeleton (no embedding). This method does not try to perform embedding. It simply returns the skeleton in its initial pose without any attempt at embedding inside the meshes, other than placing it in the meshes bounding box.

-----------------------------------------

sr    : segmentationResolution [uint]
    Specifies which segmentation resolution to use for the voxel grid. By default, 256x256x256 voxels will be used.

    """

def skinCluster(q=1,e=1,ai="string",ats=1,af=1,ar=1,bsh="string",bf=1,bm="int",dt=1,dr="float",ex="string",fnw=1,foc=1,g="string",gi=1,hmf="float",ibp=1,ih=1,ignoreSelected=1,ihs=1,inf="string",lw=1,mi="int",mjm=1,n="string",nw="int",ns="int",omi=1,par=1,ps="float",pr=1,rbm=1,rm=1,rfs=1,ri="string",rui=1,siv="string",sm="int",sw="float",swi="int",sp=1,tsb=1,tst=1,ub=1,ubk=1,ug=1,vb="float",vt="int",wt="float",wd="int",wi=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/skinCluster.html



-----------------------------------------

skinCluster is undoable, queryable, and editable.

The skinCluster command is used for smooth skinning in maya. It binds the
selected geometry to the selected joints or skeleton by means of a skinCluster
node. Each point of the bound geometry can be affected by any number of
joints. The extent to which each joint affects the motion of each point is
regulated by a corresponding weight factor. Weight factors can be modified
using the skinPercent command. The command returns the name of the new
skinCluster.  

The skinCluster binds only a single geometry at a time. Thus, to bind multiple
geometries, multiple skinCluster commands must be issued.  

Upon creation of a new skinCluster, the command can be used to add and remove
transforms (not necessarily joints) that influence the motion of the bound
skin points.  

The skinCluster command can also be used to adjust parameters such as the
dropoff, nurbs samples, polygon smoothness on a particular influence object.
Note: Any custom weights on a skin point that the influence object affects
will be lost after adjusting these parameters.


-----------------------------------------


Return Value:

string  (the skinCluster node name)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ai    : addInfluence    [string] ['edit']
    The specified transform or joint will be added to the list of transforms that influence the bound geometry. The maximum number of influences will be observed and only the weights of the cv's that the specified transform effects will change. This flag is multi-use.

-----------------------------------------

ats   : addToSelection  [boolean] ['edit']
    When used in conjunction with the selectInfluenceVerts flag, causes the vertices afftected by the influence to be added to the current selection, without first de-selecting other vertices.

-----------------------------------------

af    : after           [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ar    : afterReference  [boolean] ['edit']
    The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.

-----------------------------------------

bsh   : baseShape       [string] ['edit']
    This flag can be used in conjunction with the -addInfluence flag to specify the shape that will be used as the base shape when an influence object with geometry is added to the skinCluster. If the flag is not used then the command will make a copy of the influence object's shape and use that as a base shape.

-----------------------------------------

bf    : before          [boolean] ['edit']
    If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

bm    : bindMethod      [int] ['query']
    This flag sets the binding method. 0 - Closest distance between a joint and a point of the geometry. 1 - Closest distance between a joint, considering the skeleton hierarchy, and a point of the geometry. 2 - Surface heat map diffusion. 3 - Geodesic voxel binding. geomBind command must be called after creating a skinCluster with this method.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

dr    : dropoffRate     [float] ['query', 'edit']
    Sets the rate at which the influence of a transform drops as the distance from that transform increases. The valid range is between 0.1 and 10.0. In Create mode it sets the dropoff rate for all the bound joints. In Edit mode the flag is used together with the inf/influence flag to set the dropoff rate of a particular influence. Note: When the flag is used in Edit mode, any custom weights on the skin points the given transform influences will be lost.

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

fnw   : forceNormalizeWeights [boolean] ['edit']
    If the normalization mode is none or post, it is possible (indeed likely) for the weights in the skin cluster to no longer add up to 1. This flag forces all weights to add back to 1 again.

-----------------------------------------

foc   : frontOfChain    [boolean] ['edit']
    This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

g     : geometry        [string] ['query', 'edit']
    The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...

-----------------------------------------

gi    : geometryIndices [boolean] ['query']
    Complements the -geometry flag in query mode. Returns the multi index of each geometry.

-----------------------------------------

hmf   : heatmapFalloff  [float] []
    This flag sets the heatmap binding falloff. If set to 0.0 (default) the deformation will be smoother due to many small weights spread over the mesh surface per influence. However, if set to 1.0, corresponding to maximum falloff, the number of influences per point will be reduced and points will tend to be greatly influenced by their closest joint decreasing the overall spread of small weights. This flag only works when using heatmap binding.

-----------------------------------------

ibp   : ignoreBindPose  [boolean] ['edit']
    This flag is deprecated and no longer used. It will be ignored if used.

-----------------------------------------

ih    : ignoreHierarchy [boolean] ['query']
    Deprecated. Use bindMethod flag instead. Disregard the place of the joints in the skeleton hierarchy when computing the closest joints that influence a point of the geometry.

-----------------------------------------

ignoreSelected : ignoreSelected  [boolean] []
    Tells the command to not deform objects on the current selection list

-----------------------------------------

ihs   : includeHiddenSelections [boolean] []
    Apply the deformer to any visible and hidden objects in the selection list. Default is false.

-----------------------------------------

inf   : influence       [string] ['query', 'edit']
    This flag specifies the influence object that will be used for the current edit operation. In query mode, returns a string array of the influence objects (joints and transform).  In query mode, this flag can accept a value.

-----------------------------------------

lw    : lockWeights     [boolean] ['query', 'edit']
    Lock the weights of the specified influence object to their current value or to the value specified by the -weight flag.

-----------------------------------------

mi    : maximumInfluences [int] ['query', 'edit']
    Sets the maximum number of transforms that can influence a point (have non-zero weight for the point) when the skinCluster is first created or a new influence is added. Note: When this flag is used in Edit mode any custom weights will be lost and new weights will be reassigned to the whole skin.

-----------------------------------------

mjm   : moveJointsMode  [boolean] ['edit']
    If set to true, puts the skin into a mode where joints can be moved without modifying the skinning. If set to false, takes the skin out of move joints mode.

-----------------------------------------

n     : name            [string] []
    Used to specify the name of the node being created.

-----------------------------------------

nw    : normalizeWeights [int] ['query', 'edit']
    This flag sets the normalization mode. 0 - none, 1 - interactive, 2 - post (default) Interactive normalization makes sure the weights on the influences add up to 1.0, always. Everytime a weight is changed, the weights are automatically normalized. This may make it difficult to perform weighting operations, as the normalization may interfere with the weights the user has set. Post normalization leaves the weights the user has set as is, and only normalizes the weights at the moment it is needed (by dividing by the sum of the weights). This makes it easier for users to weight their skins.

-----------------------------------------

ns    : nurbsSamples    [int] ['edit']
    Sets the number of sample points that will be used along an influence curve or in each direction on an influence NURBS surface to influence the bound skin. The more the sample points the more closely the skin follows the influence NURBS curve/surface.

-----------------------------------------

omi   : obeyMaxInfluences [boolean] ['query', 'edit']
    When true, the skinCluster will continue to enforce the maximum influences each time the user modifies the weight, so that any given point is only weighted by the number of influences in the skinCluster's maximumInfluences attribute.

-----------------------------------------

par   : parallel        [boolean] ['edit']
    Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

ps    : polySmoothness  [float] ['edit']
    This flag controls how accurately the skin control points follow a given polygon influence object. The higher the value of polySmoothnmess the more rounded the deformation resulting from a polygonal influence object will be.

-----------------------------------------

pr    : prune           [boolean] ['edit']
    Removes any points not being deformed by the deformer in its current configuration from the deformer set.

-----------------------------------------

rbm   : recacheBindMatrices [boolean] ['edit']
    Forces the skinCluster node to recache its bind matrices.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Specifies that objects listed after the -g flag should be removed from this deformer.

-----------------------------------------

rfs   : removeFromSelection [boolean] ['edit']
    When used in conjunction with the selectInfluenceVerts flag, causes the vertices afftected by the influence to be removed from the current selection.

-----------------------------------------

ri    : removeInfluence [string] ['edit']
    Remove the specified transform or joint from the list of transforms that influence the bound geometry The weights for the affected points are renormalized. This flag is multi-use.

-----------------------------------------

rui   : removeUnusedInfluence [boolean] []
    If this flag is set to true then transform or joint whose weights are all zero (they have no effect) will not be bound to the geometry. Having this option set will help speed-up the playback of animation.

-----------------------------------------

siv   : selectInfluenceVerts [string] ['edit']
    Given the name of a transform, this will select the verts or control points being influenced by this transform, so users may visualize which vertices are being influenced by the transform.

-----------------------------------------

sm    : skinMethod      [int] ['query', 'edit']
    This flag set the skinning method. 0 - classical linear skinning (default). 1 - dual quaternion (volume preserving), 2 - a weighted blend between the two.

-----------------------------------------

sw    : smoothWeights   [float] ['edit']
    This flag is used to detect sudden jumps in skin weight values, which often indicates bad weighting, and then smooth out those jaggies in skin weights. The argument is the error tolerance ranging from 0 to 1. A value of 1 means that the algorithm will smooth a vertex only if there is a 100% change in weight values from its neighbors. The recommended default to use is 0.5 (50% change in weight value from the neighbors).

-----------------------------------------

swi   : smoothWeightsMaxIterations [int] ['edit']
    This flag is valid only with the smooth weights flag. It is possible that not all the vertices detected as needing smoothing can be smoothed in 1 iteration (because all of their neighbors also have bad weighting and need to be smoothed). With more iterations, more vertices can be smoothed. This flag controls the maximum number of iterations the algorithm will attempt to smooth weights. The default is 2 for this flag.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

tsb   : toSelectedBones [boolean] []
    geometry will be bound to the selected bones only.

-----------------------------------------

tst   : toSkeletonAndTransforms [boolean] []
    geometry will be bound to the skeleton and any transforms in the hierarchy. If any of the transforms are also bindable objects, assume that only the last object passed to the command is the bindable object. The rest are treated as influences.

-----------------------------------------

ub    : unbind          [boolean] ['edit']
    Unbinds the geometry from the skinCluster and deletes the skinCluster node

-----------------------------------------

ubk   : unbindKeepHistory [boolean] ['edit']
    Unbinds the geometry from the skinCluster, but keeps the skinCluster node so that its weights can be used when the skin is rebound. To rebind, use the skinCluster command.

-----------------------------------------

ug    : useGeometry     [boolean] ['edit']
    When adding an influence to a skinCluster, use the geometry parented under the influence transform to determine the weight dropoff of that influence.

-----------------------------------------

vb    : volumeBind      [float] []
    Creates a volume bind node and attaches it to the new skin cluster node. This node holds hull geometry parameters for a volume based weighting system. This system is used in interactive skinning. The value passed will determine the minimum weight value when initializing the volume. The volume in be increase to enclose all the vertices that are above this value.

-----------------------------------------

vt    : volumeType      [int] []
    Defines the initial shape of the binding volume (see volumeBind). 0 - Default (currently set to a capsule) 1 - Capsule, 2 - Cylinder.

-----------------------------------------

wt    : weight          [float] ['edit']
    This flag is only valid in conjunction with the -addInfluence flag. It sets the weight for the influence object that is being added.

-----------------------------------------

wd    : weightDistribution [int] ['query', 'edit']
    This flag sets the weight distribution mode. 0 - distance (default), 1 - neighbors When normalizeWeights is in effect, and a weight has been reduced or removed altogether, the sum is usually brought back up to 1.0 by increasing the contributions of the other non-zero weights. However, if there are no other non-zero weights, the algorithm has to create some weights from thin air and distribute the residual weight between them. This attribute controls how that is done. "Distance" \- the algorithm calculates weights from the world- space distances from the component to the transforms. "Neighbors" \- the algorithm calculates weights from the weights on the neighboring components.

-----------------------------------------

wi    : weightedInfluence [boolean]
    This flag returns a string array of the influence objects (joints and transform) that have non-zero weighting.

    """

def skinPercent(q=1,ib="float",nrm=1,prw="float",r=1,rtd=1,t="string",tmw="string",tv="[string, float]",v=1,zri=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/skinPercent.html



-----------------------------------------

skinPercent is undoable, queryable, and NOT editable.

This command edits and queries the weight values on members of a skinCluster
node, given as the first argument. If no object components are explicitly
mentioned in the command line, the current selection list is used.

Note that setting multiple weights in a single invocation of this command is
far more efficient than calling it once per weighted vertex.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ib    : ignoreBelow     [float] ['query']
    Limits the output of the -value and -transform queries to the entries whose weight values are over the specified limit. This flag has to be used before the -query flag.  In query mode, this flag needs a value.

-----------------------------------------

nrm   : normalize       [boolean] []
    If set, the weights not assigned by the -transformValue flag are normalized so that the sum of the all weights for the selected object component add up to 1. The default is on. NOTE: The skinCluster has a normalizeWeights attribute which when set to OFF overrides this attribute! If the skinCluster.normalizeWeights attribute is OFF, you must set it to Interactive in order to normalize weights using the skinPercent command.

-----------------------------------------

prw   : pruneWeights    [float] []
    Sets to zero any weight smaller than the given value for all the selected components. To use this command to set all the weights to zero, you must turn the -normalize flag "off" or the skinCluster node will normalize the weights to sum to one after pruning them. Weights for influences with a true value on their "Hold Weights" attribute will not be pruned.

-----------------------------------------

r     : relative        [boolean] []
    Used with -transformValue to specify a relative setting of values. If -relative is true, the value passed to -tv is added to the previous value. Otherwise, it replaces the previous value.

-----------------------------------------

rtd   : resetToDefault  [boolean] []
    Sets the weights of the selected components to their default values, overwriting any custom weights.

-----------------------------------------

t     : transform       [string] ['query']
    In Mel, when used after the -query flag (without an argument) the command returns an array of strings corresponding to the names of the transforms influencing the selected object components. If used before the -query flag (with a transform name), the command returns the weight of the selected object component corresponding to the given transform. The command will return an average weight if several components have been selected. In Python, when used with None instead of the name of the transform, the command returns an array of strings corresponding to the names of the transforms influencing the selected object components. If used with a transform name, the command returns the weight of the selected object. The command will return an average weight if several components have been selected.  In query mode, this flag can accept a value.

-----------------------------------------

tmw   : transformMoveWeights [string] []
    This flag is used to transfer weights from a source influence to one or more target influences. It acts on the selected vertices. The flag must be used at least twice to generate a valid command. The first flag usage indicates the source influence from which the weights will be copied. Subsequent flag usages indicate the target influences.

-----------------------------------------

tv    : transformValue  [[string, float]] []
    Accepts a pair consisting of a transform name and a value and assigns that value as the weight of the selected object components corresponding to the given transform.

-----------------------------------------

v     : value           [boolean] ['query']
    Returns an array of doubles corresponding to the joint weights for the selected object component.

-----------------------------------------

zri   : zeroRemainingInfluences [boolean]
    If set, the weights not assigned by the -transformValue flag are set to 0. The default is off.

    """

def substituteGeometry(dnd=1,ngl=1,ogl=1,wdt="float",rog=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/substituteGeometry.html



-----------------------------------------

substituteGeometry is undoable, NOT queryable, and NOT editable.

This command can be used to replace the geometry which is already connected to
deformers with a new geometry. The weights on the old geometry will be
retargeted to the new geometry.


-----------------------------------------


Return Value:

string  Name of shapes that were replaced


-----------------------------------------


Flags:

-----------------------------------------

dnd   : disableNonSkinDeformers [boolean] []
    This flag controls the state of deformers other than skin deformers after the substitution has taken place. If the flag is true then non-skin deformer nodes are left in a disabled state at the completion of the command. Default value is false.

-----------------------------------------

ngl   : newGeometryToLayer [boolean] []
    Create a new layer for the new geometry.

-----------------------------------------

ogl   : oldGeometryToLayer [boolean] []
    Create a new layer and move the old geometry to this layer

-----------------------------------------

wdt   : reWeightDistTolerance [float] []
    Specify the distance tolerance value to be used for retargeting weights. While transferring weights the command tries to find the corresponding vertices by overlapping the geometries with all deformers disabled. Sometimes this results in selection of unrelated vertices. (Example when a hole in the old geometry has been filled with new vertices in the new geometry.) This distance tolerance value is used to detect this kind of faults and either ignore these cases or to vary algorithm to find more corresponding vertices.

-----------------------------------------

rog   : retainOldGeometry [boolean]
    A copy of the old geometry should be retained

    """

def volumeBind(q=1,e=1,inf="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/volumeBind.html



-----------------------------------------

volumeBind is undoable, queryable, and editable.

Command for creating and editing volume binding nodes. The node is use for
storing volume data to define skin weighting data.


-----------------------------------------


Return Value:

string[]  List of queried influences    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

inf   : influence       [string] ['query', 'edit']
    Edit or Query the list of influences connected to the skin cluster.

-----------------------------------------

n     : name            [string]
    Used to specify the name of the node being created.

    """

def aimConstraint(q=1,e=1,aim="[float, float, float]",l="string",mo=1,n="string",o="[float, float, float]",rm=1,sk="string",tl=1,u="[float, float, float]",w="float",wal=1,wuo="name",wut="string",wu="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/aimConstraint.html



-----------------------------------------

aimConstraint is undoable, queryable, and editable.

Constrain an object's orientation to point at a target object or at the
average position of a number of targets.

An aimConstraint takes as input one or more "target" DAG transform nodes at
which to aim the single "constraint object" DAG transform node. The
aimConstraint orients the constrained object such that the aimVector (in the
object's local coordinate system) points to the in weighted average of the
world space position target objects. The upVector (again the the object's
local coordinate system) is aligned in world space with the worldUpVector.


-----------------------------------------


Return Value:

string[]  name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aim   : aimVector       [[float, float, float]] ['query', 'edit']
    Set the aim vector. This is the vector in local coordinates that points at the target. If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

mo    : maintainOffset  [boolean] []
    The offset necessary to preserve the constrained object's initial rotation will be calculated and used as the offset.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

o     : offset          [[float, float, float]] ['query', 'edit']
    Sets or queries the value of the offset. Default is 0,0,0.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

sk    : skip            [string] ['edit']
    Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

u     : upVector        [[float, float, float]] ['query', 'edit']
    Set local up vector. This is the vector in local coordinates that aligns with the world up vector. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean] ['query']
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

-----------------------------------------

wuo   : worldUpObject   [name] ['query', 'edit']
    Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.

-----------------------------------------

wut   : worldUpType     [string] ['query', 'edit']
    Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".

-----------------------------------------

wu    : worldUpVector   [[float, float, float]]
    Set world up vector. This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.

    """

def geometryConstraint(q=1,e=1,l="string",n="string",rm=1,tl=1,w="float",wal=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/geometryConstraint.html



-----------------------------------------

geometryConstraint is undoable, queryable, and editable.

Constrain an object's position based on the shape of the target surface(s) at
the closest point(s) to the object.

A geometryConstraint takes as input one or more surface shapes (the targets)
and a DAG transform node (the object). The geometryConstraint position
constrained object such object lies on the surface of the target with the
greatest weight value. If two targets have the same weight value then the one
with the lowest index is chosen.


-----------------------------------------


Return Value:

string[]  Name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean]
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    """

def normalConstraint(q=1,e=1,aim="[float, float, float]",l="string",n="string",rm=1,tl=1,u="[float, float, float]",w="float",wal=1,wuo="name",wut="string",wu="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/normalConstraint.html



-----------------------------------------

normalConstraint is undoable, queryable, and editable.

Constrain an object's orientation based on the normal of the target surface(s)
at the closest point(s) to the object.

A normalConstraint takes as input one or more surface shapes (the targets) and
a DAG transform node (the object). The normalConstraint orients the
constrained object such that the aimVector (in the object's local coordinate
system) aligns in world space to combined normal vector. The upVector (again
the the object's local coordinate system) is aligned in world space with the
worldUpVector. The combined normal vector is a weighted average of the normal
vector for each target surface at the point closest to the constrained object.


-----------------------------------------


Return Value:

string[]  Name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aim   : aimVector       [[float, float, float]] ['query', 'edit']
    Set the aim vector. This is the vector in local coordinates that points at the target. If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

u     : upVector        [[float, float, float]] ['query', 'edit']
    Set local up vector. This is the vector in local coordinates that aligns with the world up vector. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean] ['query']
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

-----------------------------------------

wuo   : worldUpObject   [name] ['query', 'edit']
    Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.

-----------------------------------------

wut   : worldUpType     [string] ['query', 'edit']
    Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".

-----------------------------------------

wu    : worldUpVector   [[float, float, float]]
    Set world up vector. This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.

    """

def orientConstraint(q=1,e=1,cc="[float, float]",dc=1,l="string",mo=1,n="string",o="[float, float, float]",rm=1,sk="string",tl=1,w="float",wal=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/orientConstraint.html



-----------------------------------------

orientConstraint is undoable, queryable, and editable.

Constrain an object's orientation to match the orientation of the target or
the average of a number of targets.

An orientConstraint takes as input one or more "target" DAG transform nodes to
control the orientation of the single "constraint object" DAG transform The
orientConstraint orients the constrained object to match the weighted average
of the target world space orientations.


-----------------------------------------


Return Value:

string  [] ( name of the created constraint node)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cc    : createCache     [[float, float]] ['edit']
    This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.   The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.

-----------------------------------------

dc    : deleteCache     [boolean] ['edit']
    Delete an existing interpolation cache.

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

mo    : maintainOffset  [boolean] []
    The offset necessary to preserve the constrained object's initial orientation will be calculated and used as the offset.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

o     : offset          [[float, float, float]] ['query', 'edit']
    Sets or queries the value of the offset. Default is 0,0,0.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

sk    : skip            [string] ['edit']
    Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". The default value in create mode is "none". This flag is multi-use.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean]
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    """

def parentConstraint(q=1,e=1,cc="[float, float]",dr=1,dc=1,l="string",mo=1,n="string",rm=1,sr="string",st="string",tl=1,w="float",wal=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/parentConstraint.html



-----------------------------------------

parentConstraint is undoable, queryable, and editable.

Constrain an object's position and rotation so that it behaves as if it were a
child of the target object(s). In the case of multiple targets, the overall
position and rotation of the constrained object is the weighted average of
each target's contribution to the position and rotation of the object.

A parentConstraint takes as input one or more "target" DAG transform nodes at
which to position and rotate the single "constraint object" DAG transform
node. The parentConstraint positions and rotates the constrained object at the
weighted average of the world space position, rotation and scale target
objects.


-----------------------------------------


Return Value:

string[]  Name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cc    : createCache     [[float, float]] ['edit']
    This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.   The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.

-----------------------------------------

dr    : decompRotationToChild [boolean] []
    During constraint creation, if the rotation offset between the constrained object and the target object is maintained, this flag indicates close to which object the offset rotation is decomposed. Setting this flag will make the rotation decomposition close to the constrained object instead of the target object, which is the default setting.

-----------------------------------------

dc    : deleteCache     [boolean] ['edit']
    Delete an existing interpolation cache.

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

mo    : maintainOffset  [boolean] []
    If this flag is specified the position and rotation of the constrained object will be maintained.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

sr    : skipRotate      [string] []
    Causes the axis specified not to be considered when constraining rotation. Valid arguments are "x", "y", "z" and "none".

-----------------------------------------

st    : skipTranslate   [string] []
    Causes the axis specified not to be considered when constraining translation. Valid arguments are "x", "y", "z" and "none".

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean]
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    """

def pointConstraint(q=1,e=1,l="string",mo=1,n="string",o="[float, float, float]",rm=1,sk="string",tl=1,w="float",wal=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pointConstraint.html



-----------------------------------------

pointConstraint is undoable, queryable, and editable.

Constrain an object's position to the position of the target object or to the
average position of a number of targets.

A pointConstraint takes as input one or more "target" DAG transform nodes at
which to position the single "constraint object" DAG transform node. The
pointConstraint positions the constrained object at the weighted average of
the world space position target objects.


-----------------------------------------


Return Value:

string[]  Name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

mo    : maintainOffset  [boolean] []
    The offset necessary to preserve the constrained object's initial position will be calculated and used as the offset.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

o     : offset          [[float, float, float]] ['query', 'edit']
    Sets or queries the value of the offset. Default is 0,0,0.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

sk    : skip            [string] ['edit']
    Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean]
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    """

def pointOnPolyConstraint(q=1,e=1,l="string",mo=1,n="string",o="[float, float, float]",rm=1,sk="string",tl=1,w="float",wal=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pointOnPolyConstraint.html



-----------------------------------------

pointOnPolyConstraint is undoable, queryable, and editable.

Constrain an object's position to the position of the target object or to the
average position of a number of targets.

A pointOnPolyConstraint takes as input one or more "target" DAG transform
nodes at which to position the single "constraint object" DAG transform node.
The pointOnPolyConstraint positions the constrained object at the weighted
average of the world space position target objects.


-----------------------------------------


Return Value:

string[]  Name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

mo    : maintainOffset  [boolean] []
    The offset necessary to preserve the constrained object's initial position will be calculated and used as the offset.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

o     : offset          [[float, float, float]] ['query', 'edit']
    Sets or queries the value of the offset. Default is 0,0,0.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

sk    : skip            [string] ['edit']
    Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean]
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    """

def scaleConstraint(q=1,e=1,l="string",mo=1,n="string",o="[float, float, float]",rm=1,sc=1,sk="string",tl=1,w="float",wal=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scaleConstraint.html



-----------------------------------------

scaleConstraint is undoable, queryable, and editable.

Constrain an object's scale to the scale of the target object or to the
average scale of a number of targets.

A scaleConstraint takes as input one or more "target" DAG transform nodes to
which to scale the single "constraint object" DAG transform node. The
scaleConstraint scales the constrained object at the weighted geometric mean
of the world space target scale factors.


-----------------------------------------


Return Value:

string[]  Name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

mo    : maintainOffset  [boolean] []
    The offset necessary to preserve the constrained object's initial scale will be calculated and used as the offset.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

o     : offset          [[float, float, float]] ['query', 'edit']
    Sets or queries the value of the offset. Default is 1,1,1.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

sc    : scaleCompensate [boolean] ['edit']
    Used only when constraining a joint. It specify if a scaleCompensate will be applied on constrained joint. If true it will connect Tjoint.aCompensateForParentScale to scaleContraint.aConstraintScaleCompensate.

-----------------------------------------

sk    : skip            [string] ['edit']
    Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean]
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    """

def tangentConstraint(q=1,e=1,aim="[float, float, float]",l="string",n="string",rm=1,tl=1,u="[float, float, float]",w="float",wal=1,wuo="name",wut="string",wu="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/tangentConstraint.html



-----------------------------------------

tangentConstraint is undoable, queryable, and editable.

Constrain an object's orientation based on the tangent of the target curve[s]
at the closest point[s] to the object.

A tangentConstraint takes as input one or more NURBS curves (the targets) and
a DAG transform node (the object). The tangentConstraint orients the
constrained object such that the aimVector (in the object's local coordinate
system) aligns in world space to combined tangent vector. The upVector (again
the the object's local coordinate system) is aligned in world space with the
worldUpVector. The combined tangent vector is a weighted average of the
tangent vector for each target curve at the point closest to the constrained
object.


-----------------------------------------


Return Value:

string[]  Name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aim   : aimVector       [[float, float, float]] ['query', 'edit']
    Set the aim vector. This is the vector in local coordinates that points at the target. If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

u     : upVector        [[float, float, float]] ['query', 'edit']
    Set local up vector. This is the vector in local coordinates that aligns with the world up vector. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean] ['query']
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

-----------------------------------------

wuo   : worldUpObject   [name] ['query', 'edit']
    Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.

-----------------------------------------

wut   : worldUpType     [string] ['query', 'edit']
    Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".

-----------------------------------------

wu    : worldUpVector   [[float, float, float]]
    Set world up vector. This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.

    """

def characterize(q=1,e=1,apv=1,aae=1,afp=1,ame=1,ahk="string",mhk="string",aab=1,cpp=1,ef="string",fk="string",nm="string",phf=1,pnp=1,pos="string",sk="string",sp="string",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/characterize.html



-----------------------------------------

characterize is undoable, queryable, and editable.

This command is used to scan a joint hierarchy for predefined joint names or
labels. If the required joints are found, human IK effectors will be created
to control the skeleton using full-body IK. Alternatively, you can manually
create all of the components required for fullbody IK, and use this command to
hook them up. Fullbody IK needs 3 major components: the user input skeleton
(sk), the fk skeleton on which keys are set (fk) and the hik effectors (ik).
Together fk and ik provide parameters to the fullbody IK engine, which solves
for the output and plots it onto sk. This command usage is used internally by
Maya when importing data from fbx files, but is not generally recommended.

Note that a minimum set of required joint names or joint labels must be found
in order for the characterize command to succeed. Please refer to the Maya
documentation for details on properly naming or labeling your skeleton. The
skeleton should also be z-facing, with its y-axis up, its left hand parallel
to positive x-axis and right hand parallel to negative x-axis. END_COMMENT


-----------------------------------------


Return Value:

string  Names of full body IK effectors that were created.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

apv   : activatePivot   [boolean] ['edit']
    Activates a pivot that has been properly placed. After activating this new pivot, you will now be able to rotate and translate about this pivot. A pivot behaves in all ways the same as an effector (it IS an effector, except that it is offset from the normal position of the effector to allow one to rotate about a different point.

-----------------------------------------

aae   : addAuxEffector  [boolean] ['edit']
    Adds an auxilliary (secondary) effector to an existing effector.

-----------------------------------------

afp   : addFloorContactPlane [boolean] ['edit']
    Adds a floor contact plane to one of the hands or feet. With this plane, you will be able to adjust the floor contact height. Select a hand or foot effector and then issue the characterize command with this flag.

-----------------------------------------

ame   : addMissingEffectors [boolean] ['edit']
    This flag tells the characterize command to look for any effectors that can be added to the skeleton. For example, if the user has deleted some effectors or added fingers to an existing skeleton, "characterize -e -addMissingEffectors" can be used to restore them.

-----------------------------------------

ahk   : attributeFromHIKProperty [string] ['query']
    Query for the attribute name associated with a MotionBuilder property.

-----------------------------------------

mhk   : attributeFromHIKPropertyMode [string] ['query']
    Query for the attribute name associated with a MotionBuilder property mode.

-----------------------------------------

aab   : autoActivateBodyPart [boolean] ['query', 'edit']
    Query or change whether auto activation of character nodes representing body parts should be enabled.

-----------------------------------------

cpp   : changePivotPlacement [boolean] ['edit']
    Reverts a pivot back into pivot placement mode. A pivot that is in placement mode will not participate in full body manipulation until it has been activated with the -activatePivot flag.

-----------------------------------------

ef    : effectors       [string] []
    Specify the effectors to be used by human IK by providing 2 pieces of information for each effector: 1) the partial path of the effector and 2) the name of the full body effector this represents. 1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the effectors are automatically created. This flag is for advanced users only.

-----------------------------------------

fk    : fkSkeleton      [string] ['edit']
    Specify the fk skeleton to be used by human IK by providing 2 pieces of information for each joint of the FK skeleton: 1) the partial path of the joint and 2) the name of the full body joint this represents. 1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the fk control skeleton is automatically created. This flag is for advanced users only.

-----------------------------------------

nm    : name            [string] []
    At characterization (FBIK creation) time, use this flag to name your FBIK character. This will affect the name of the hikHandle node and the control rig will be put into a namespace that matches the name of your character. If you do not specify the character name, a default one will be used. At the moment edit and query of the character name is not supported.

-----------------------------------------

phf   : pinHandFeet     [boolean] []
    When the character is first being characterized, pin the hands and feet by default.

-----------------------------------------

pnp   : placeNewPivot   [boolean] ['edit']
    Creates a new pivot and puts it into placement mode. Note that you will not be able to do full body manipulation about this pivot until you have activated it with the -activatePivot flag. A pivot behaves in all ways the same as an effector (it IS an effector, except that it is offset from the normal position of the effector to allow one to rotate about a different point). A new pivot created with this flag allow you to adjust the offset interactively before activating it.

-----------------------------------------

pos   : posture         [string] []
    Specifies the posture of the character. Valid options are "biped" and "quadruped". The default is "biped".

-----------------------------------------

sk    : sourceSkeleton  [string] ['edit']
    This flag can be used to characterize a skeleton that has not been named or labelled according to the FBIK guidelines. It specifies the association between the actual joint names and the expected FBIK joint names. The format of the string is as follows: For each joint that the user wants to involve in the solve: 1) the partial path of the joint and 2) the name of the full body joint this represents. 1) and 2) are to be separated by white space, and multiple entries separated by ",".

-----------------------------------------

sp    : stancePose      [string] ['query']
    Specify the default stance pose to be used by human IK. The stance pose is specified by providing 2 pieces of information for each joint involved in the solve: 1) the partial path to the joint and 2) 9 numbers representing translation rotation and scale. 1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the stance pose is taken from the selected skeleton. This flag is for advanced users only.

-----------------------------------------

typ   : type            [string]
    Specifies the technique used by the characterization to identify the joint type. Valid options are "label" and "name". When "label" is used, the joints must be labelled using the guidelines described in the Maya documentation. When name is used, the joint names must follow the naming conventions described in the Maya documentation. The default is "name". This flag cannot be used in conjunction with the sourceSkeleton flag.

    """

def connectJoint(cm=1,pm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/connectJoint.html



-----------------------------------------

connectJoint is undoable, NOT queryable, and NOT editable.

This command will connect two skeletons based on the two selected joints. The
first selected joint can be made a child of the parent of the second selected
joint or a child of the second selected joint, depending on the flags used.

Note1: The first selected joint must be the root of a skeleton. The second
selected joint must have a parent.

Note2: If a joint name is specified in the command line, it is used as the
child and the first selected joint will be the parent. If no joint name is
given at the command line, two joints must be selected.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cm    : connectMode     [boolean] []
    The first selected joint will be parented under the parent of the second selected joint.

-----------------------------------------

pm    : parentMode      [boolean]
    The first selected joint will be parented under the second selected joint. Both joints will be in the active list(selection list).

    """

def disconnectJoint(ahm=1,dhm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/disconnectJoint.html



-----------------------------------------

disconnectJoint is undoable, NOT queryable, and NOT editable.

This command will break a skeleton at the selected joint and delete any
associated handles.


-----------------------------------------


Return Value:

string  After the joint is disconnected, a new joint will be created. The
return value is the name of the newly created joint and its ancestor.


-----------------------------------------


Flags:

-----------------------------------------

ahm   : attachHandleMode [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

dhm   : deleteHandleMode [boolean]
    Delete the handle on the associated joint.

    """

def effector(q=1,e=1,hi=1,n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/effector.html



-----------------------------------------

effector is undoable, queryable, and editable.

The effector command is used to set the name or hidden flag for the effector.
The standard edit (-e) and query (-q) flags are used for edit and query
functions.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

hi    : hide            [boolean] ['query', 'edit']
    Specifies whether to hide drawing of effector if attached to a handle.

-----------------------------------------

n     : name            [string]
    Specifies the name of the effector.

    """

def ikfkDisplayMethod(q=1,d="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikfkDisplayMethod.html



-----------------------------------------

ikfkDisplayMethod is NOT undoable, queryable, and NOT editable.

The ikfkDisplayMethod command is used to specify how ik/fk blending should be
shown


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : display         [string]
    Specify how ik/fk blending should be shown when the handle is selected. Possible choices are "none" (do not display any blending), "ik" (only show ik),"fk" (only show fk), and "ikfk" (show both ik and fk).

    """

def ikHandle(q=1,e=1,ap=1,ce=1,ccv=1,cra=1,c="name",dh=1,eh=1,ee="string",ex="string",fs=1,fj=1,jl=1,n="string",ns="int",pcv=1,pw="float",p="int",roc=1,rtm=1,srp=1,scv=1,snc=1,shf=1,see=1,sol="string",sj="string",s="string",tws="string",w="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikHandle.html



-----------------------------------------

ikHandle is undoable, queryable, and editable.

The handle command is used to create, edit, and query a handle within Maya.
The standard edit (-e) and query (-q) flags are used for edit and query
functions.

If there are 2 joints selected and neither -startJoint nor -endEffector flags
are not specified, then the handle will be created from the selected joints.

If a single joint is selected and neither -startJoint nor -endEffector flags
are specified, then the handle will be created with the selected joint as the
end-effector and the start joint will be the top of the joint chain containing
the end effector.

The default values of the flags are:

  * -name "ikHandle#"
  * -priority 1
  * -weight 1.0
  * -positionWeight 1.0
  * -solver "ikRPsolver"
  * -forceSolver on
  * -snapHandleFlagToggle on
  * -sticky off
  * -createCurve true
  * -simplifyCurve true
  * -rootOnCurve true
  * -twistType linear
  * -createRootAxis false
  * -parentCurve true
  * -snapCurve false
  * -numSpans 1
  * -rootTwistMode false.

These attributes can be specified in creation mode, edited in edit mode (-e)
or queried in query mode (-q).


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : autoPriority    [boolean] ['edit']
    Specifies that this handle's priority is assigned automatically. The assigned priority will be based on the hierarchy distance from the root of the skeletal chain to the start joint of the handle.

-----------------------------------------

ce    : connectEffector [boolean] ['edit']
    This option is set to true as default, meaning that end-effector translate is connected with the endJoint translate.

-----------------------------------------

ccv   : createCurve     [boolean] []
    Specifies if a curve should automatically be created for the ikSplineHandle.

-----------------------------------------

cra   : createRootAxis  [boolean] []
    Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.

-----------------------------------------

c     : curve           [name] ['query', 'edit']
    Specifies the curve to be used by the ikSplineHandle. Joints will be moved to align with this curve. This flag is mandatory if you use the -freezeJoints option.

-----------------------------------------

dh    : disableHandles  [boolean] ['edit']
    set given handles to full fk (ikBlend attribute = 0.0)

-----------------------------------------

eh    : enableHandles   [boolean] ['edit']
    set given handles to full ik (ikBlend attribute = 1.0)

-----------------------------------------

ee    : endEffector     [string] ['query', 'edit']
    Specifies the end-effector of the handle's joint chain. The end effector may be specified with a joint or an end-effector. If a joint is specified, an end-effector will be created at the same position as the joint and this new end-effector will be used as the end-effector.

-----------------------------------------

ex    : exists          [string] ['edit']
    Indicates if the specified handle exists or not.

-----------------------------------------

fs    : forceSolver     [boolean] ['query', 'edit']
    Forces the solver to be used everytime. It could also be known as animSticky. So, after you set the first key the handle is sticky.

-----------------------------------------

fj    : freezeJoints    [boolean] ['edit']
    Forces the curve, specfied by -curve option, to align itself along the existing joint chain. When false, or unspecified, the joints will be moved to positions along the specified curve.

-----------------------------------------

jl    : jointList       [boolean] ['edit']
    Returns the list of joints that the handle is manipulating.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Specifies the name of the handle.

-----------------------------------------

ns    : numSpans        [int] []
    Specifies the number of spans in the automatically generated curve of the ikSplineHandle.

-----------------------------------------

pcv   : parentCurve     [boolean] []
    Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.

-----------------------------------------

pw    : positionWeight  [float] ['query', 'edit']
    Specifies the position/orientation weight of a handle. This is used to compute the "distance" between the goal position and the end-effector position. A positionWeight of 1.0 computes the distance as the distance between positions only and ignores the orientations. A positionWeight of 0.0 computes the distance as the distance between the orientations only and ignores the positions. A positionWeight of 0.5 attempts to weight the distances equally but cannot actually compute this due to unit differences. Because there is no way to add linear units and angular units.

-----------------------------------------

p     : priority        [int] ['query', 'edit']
    Sets the priority of the handle. Logically, all handles with a lower number priority are solved before any handles with a higher numbered priority. (All handles of priority 1 are solved before any handles of priority 2 and so on.) Handle priorities must be ] 0.

-----------------------------------------

roc   : rootOnCurve     [boolean] ['query', 'edit']
    Specifies if the root is locked onto the curve of the ikSplineHandle.

-----------------------------------------

rtm   : rootTwistMode   [boolean] ['query', 'edit']
    Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types.

-----------------------------------------

srp   : setupForRPsolver [boolean] ['edit']
    If the flag is set and ikSolver is ikRPsolver, call RPRotateSetup for the new ikHandle. It is for ikRPsolver only.

-----------------------------------------

scv   : simplifyCurve   [boolean] []
    Specifies if the ikSplineHandle curve should be simplified.

-----------------------------------------

snc   : snapCurve       [boolean] []
    Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.

-----------------------------------------

shf   : snapHandleFlagToggle [boolean] ['query', 'edit']
    Specifies that the handle position should be snapped to the end-effector position if the end-effector is moved by the user. Setting this flag on allows you to use forward kinematics to pose or adjust your skeleton and then to animate it with inverse kinematics.

-----------------------------------------

see   : snapHandleToEffector [boolean] ['edit']
    All handles are immediately moved so that the handle position and orientation matches the end-effector position and orientation.

-----------------------------------------

sol   : solver          [string] ['query', 'edit']
    Specifies the solver. The complete list of available solvers may not be known until run-time because some of the solvers may be implemented as plug- ins. Currently the only valid solver are ikRPsolver, ikSCsolver and ikSplineSolver.

-----------------------------------------

sj    : startJoint      [string] ['query', 'edit']
    Specifies the start joint of the handle's joint chain.

-----------------------------------------

s     : sticky          [string] ['query', 'edit']
    Specifies that this handle is "sticky". Valid values are "off", "sticky", "superSticky". Sticky handles are solved when the skeleton is being manipulated interactively. If a character has sticky feet, the solver will attempt to keep them in the same position as the user moves the character's root. If they were not sticky, they would move along with the root.

-----------------------------------------

tws   : twistType       [string] ['query', 'edit']
    Specifies the type of interpolation to be used by the ikSplineHandle. The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".

-----------------------------------------

w     : weight          [float]
    Specifies the handles weight in error calculations. The weight only applies when handle goals are in conflict and cannot be solved simultaneously. When this happens, a solution is computed that weights the "distance" from each goal to the solution by the handle's weight and attempts to minimize this value. The weight must be ]= 0.

    """

def ikHandleDisplayScale(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikHandleDisplayScale.html



-----------------------------------------

ikHandleDisplayScale is undoable, queryable, and editable.

This action modifies and queries the current display size of ikHandle. The
default display scale is 1.0.


-----------------------------------------


Return Value:

float  Returns current display size of ikHandle.    
  
In query mode, return type is based on queried flag.
    """

def ikSolver(q=1,e=1,ep="float",mxi="int",n="string",st="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikSolver.html



-----------------------------------------

ikSolver is undoable, queryable, and editable.

The ikSolver command is used to set the attributes for an IK Solver or create
a new one. The standard edit (-e) and query (-q) flags are used for edit and
query functions.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ep    : epsilon         [float] ['query', 'edit']
    max error

-----------------------------------------

mxi   : maxIterations   [int] ['query', 'edit']
    Sets the max iterations for a solution

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name of solver

-----------------------------------------

st    : solverType      [string]
    valid solverType (only ikSystem knows what is valid) for creation of a new solver (required)

    """

def ikSystem(q=1,e=1,ar=1,ap=1,apm=1,aps=1,ls="[int, int]",sn=1,sol=1,st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikSystem.html



-----------------------------------------

ikSystem is undoable, queryable, and editable.

The ikSystem command is used to set the global snapping flag for handles and
set the global solve flag for solvers. The standard edit (-e) and query (-q)
flags are used for edit and query functions.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ar    : allowRotation   [boolean] ['query', 'edit']
    Set true to allow rotation of an ik handle with keys set on translation.

-----------------------------------------

ap    : autoPriority    [boolean] ['edit']
    set autoPriority for all ikHandles

-----------------------------------------

apm   : autoPriorityMC  [boolean] ['edit']
    set autoPriority for all multiChain handles

-----------------------------------------

aps   : autoPrioritySC  [boolean] ['edit']
    set autoPriority for all singleChain handles

-----------------------------------------

ls    : list            [[int, int]] ['query', 'edit']
    returns the solver execution order when in query mode(list of strings) changes execution order when in edit mode (int old position, int new position)

-----------------------------------------

sn    : snap            [boolean] ['query', 'edit']
    Set global snapping

-----------------------------------------

sol   : solve           [boolean] ['query', 'edit']
    Set global solve

-----------------------------------------

st    : solverTypes     [boolean]
    returns a list of valid solverTypes ( query only )

    """

def ikSystemInfo(q=1,gsh=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikSystemInfo.html



-----------------------------------------

ikSystemInfo is undoable, queryable, and NOT editable.

This action modifies and queries the current ikSystem controls.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

gsh   : globalSnapHandle [boolean]
    If this flag is off, all ikHandles will not be snapped.

    """

def insertJoint():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/insertJoint.html



-----------------------------------------

insertJoint is undoable, NOT queryable, and NOT editable.

This command will insert a new joint under the given or selected joint. If the
given joint has child joints, they will be reparented under the new inserted
joint.

The given joint(or selected joint) should not have skin attached. The command
works on the selected joint. No options or flags are necessary.


-----------------------------------------


Return Value:

string  The name of the new inserted joint
    """

def joint(q=1,e=1,a=1,ax="angle",ay="angle",az="angle",apa=1,al=1,ch=1,co=1,dof="string",ex="string",lsx=1,lsy=1,lsz=1,lx="[angle, angle]",ly="[angle, angle]",lz="[angle, angle]",n="string",oj="string",o="[angle, angle, angle]",p="[linear, linear, linear]",rad="float",r=1,roo="string",s="[float, float, float]",sc=1,so="[angle, angle, angle]",sao="string",spa=1,stx="float",sty="float",stz="float",sym=1,sa="string",zso=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/joint.html



-----------------------------------------

joint is undoable, queryable, and editable.

The joint command is used to create, edit, and query, joints within Maya. (The
standard edit(-e) and query(-q) flags are used for edit and query functions).
If the object is not specified, the currently selected object (dag object)
will be used.

Multiple objects are allowed only for the edit mode. The same edit flags will
be applied on all the joints selected, except for -p without -r (set joint
position in the world space). An ik handle in the object list is equivalent to
the list of joints the ik handle commands. When -ch/children is present, all
the child joints of the specified joints, including the joints implied by
possible ik handles, will also be included.

In the creation mode, a new joint will be created as a child of a selected
transform or starts a hierarchy by itself if no transform is selected. An ik
handle will be treated as a transform in the creation mode.

The default values of the arguments are:

-degreeOfFreedom xyz 

-name "Joint#"

-position 0 0 0 

-absolute 

-dof "xyz"

-scale 1.0 1.0 1.0 

-scaleCompensate true 

-orientation 0.0 0.0 0.0 

-scaleOrientation 0.0 0.0 0.0 

-limitX -360 360 

-limitY -360 360 

-limitZ -360 360 

-angleX 0.0 

-angleY 0.0 

-angleZ 0.0 

-stiffnessX 0.0 

-stiffnessY 0.0 

-stiffnessZ 0.0 

-limitSwitchX no 

-limitSwitchY no 

-limitSwitchZ no 

-rotationOrder xyz 

Those arguments can be specified in the creation mode, editied in the edit
mode (-e), or queried in the query mode (-q).


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] ['query', 'edit']
    The joint center position is in absolute world coordinates. (This is the default.)

-----------------------------------------

ax    : angleX          [angle] ['query', 'edit']
    Set the x-axis angle. When queried, this flag returns a float.

-----------------------------------------

ay    : angleY          [angle] ['query', 'edit']
    Set the y-axis angle. When queried, this flag returns a float.

-----------------------------------------

az    : angleZ          [angle] ['query', 'edit']
    Set the z-axis angle. When queried, this flag returns a float.

-----------------------------------------

apa   : assumePreferredAngles [boolean] ['edit']
    Meaningful only in the edit mode. It sets the joint angles to the corresponding preferred angles.

-----------------------------------------

al    : automaticLimits [boolean] []
    Meaningful only in edit mode. It sets the joint to appropriate hinge joint with joint limits. It modifies the joint only if (a) it connects exactly to two joints (one parent, one child), (b) it does not lie on the line drawn between the two connected joints, and the plane it forms with the two connected joints is perpendicular to one of its rotation axes.

-----------------------------------------

ch    : children        [boolean] ['edit']
    It tells the command to apply all the edit options not only to the selected joints, but also to their descendent joints in the DAG.

-----------------------------------------

co    : component       [boolean] ['edit']
    Use with the -position switch to position the joint relative to its parent (like -relative) but to compute new positions for all children joints so their world coordinate positions do not change.

-----------------------------------------

dof   : degreeOfFreedom [string] ['query', 'edit']
    Specifies the degrees of freedom for the IK. Valid strings consist of non-duplicate letters from x, y, and z. The letters in the string indicate what rotations are to be used by IK. The order a letter appear in the string does not matter. Examples are x, yz, xyz. When queried, this flag returns a string. Modifying dof will change the locking state of the corresponding rotation attributes. The rule is: if an rotation is turned into a dof, it will be unlocked if it is currently locked. When it is turned into a non-dof, it will be locked if it is not currently locked.

-----------------------------------------

ex    : exists          [string] ['query']
    Does the named joint exist? When queried, this flag returns a boolean.

-----------------------------------------

lsx   : limitSwitchX    [boolean] ['query', 'edit']
    Use the limit the x-axis rotation? When queried, this flag returns a boolean.

-----------------------------------------

lsy   : limitSwitchY    [boolean] ['query', 'edit']
    Use the limit the y-axis rotation? When queried, this flag returns a boolean.

-----------------------------------------

lsz   : limitSwitchZ    [boolean] ['query', 'edit']
    Use the Limit the z-axis rotation? When queried, this flag returns a boolean.

-----------------------------------------

lx    : limitX          [[angle, angle]] ['query', 'edit']
    Set lower and upper limits on the x-axis of rotation. Also turns on the joint limit. When queried, this flag returns 2 floats.

-----------------------------------------

ly    : limitY          [[angle, angle]] ['query', 'edit']
    Set lower and upper limits on the y-axis of rotation. Also turns on the joint limit. When queried, this flag returns 2 floats.

-----------------------------------------

lz    : limitZ          [[angle, angle]] ['query', 'edit']
    Set lower and upper limits on the z-axis of rotation. Also turns on the joint limit. When queried, this flag returns 2 floats.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Specifies the name of the joint. When queried, this flag returns a string.

-----------------------------------------

oj    : orientJoint     [string] ['edit']
    The argument can be one of the following strings: xyz, yzx, zxy, zyx, yxz, xzy, none.  It modifies the joint orientation and scale orientation so that the axis indicated by the first letter in the argument will be aligned with the vector from this joint to its first child joint. For example, if the argument is "xyz", the x-axis will point towards the child joint.  The alignment of the remaining two joint orient axes are dependent on whether or not the -sao/-secondaryAxisOrient flag is used. If the -sao flag is used, see the documentation for that flag for how the remaining axes are aligned.  In the absence of a user specification for the secondary axis orientation, the rotation axis indicated by the last letter in the argument will be aligned with the vector perpendicular to first axis and the vector from this joint to its parent joint.  The remaining axis is aligned according the right hand rule.  If the argument is "none", the joint orientation will be set to zero and its effect to the hierarchy below will be offset by modifying the scale orientation.  The flag will be ignored if:  A. the joint has non-zero rotations when the argument is not "none".  B. the joint does not have child joint, or the distance to the child joint is zero when the argument is not "none".  C. either flag -o or -so is set.

-----------------------------------------

o     : orientation     [[angle, angle, angle]] ['query', 'edit']
    The joint orientation. When queried, this flag returns 3 floats.

-----------------------------------------

p     : position        [[linear, linear, linear]] ['query', 'edit']
    Specifies the position of the center of the joint. This position may be relative to the joint's parent or in absolute world coordinates (see -r and -a below). When queried, this flag returns 3 floats.

-----------------------------------------

rad   : radius          [float] ['query', 'edit']
    Specifies the joint radius.

-----------------------------------------

r     : relative        [boolean] ['query', 'edit']
    The joint center position is relative to the joint's parent.

-----------------------------------------

roo   : rotationOrder   [string] ['query', 'edit']
    The rotation order of the joint. The argument can be one of the following strings: xyz, yzx, zxy, zyx, yxz, xzy.

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    Scale of the joint. When queried, this flag returns 3 floats.

-----------------------------------------

sc    : scaleCompensate [boolean] ['query', 'edit']
    It sets the scaleCompenstate attribute of the joint to the given argument. When this is true, the scale of the parent joint will be compensated before any rotation of this joint is applied, so that the bone to the joint is scaled but not the bones to its child joints. When queried, this flag returns an boolean.

-----------------------------------------

so    : scaleOrientation [[angle, angle, angle]] ['query', 'edit']
    Set the orientation of the coordinate axes for scaling. When queried, this flag returns 3 floats.

-----------------------------------------

sao   : secondaryAxisOrient [string] ['edit']
    The argument can be one of the following strings: xup, xdown, yup, ydown, zup, zdown, none.  This flag is used in conjunction with the -oj/orientJoint flag. It specifies the scene axis that the second axis should align with. For example, a flag combination of "-oj yzx -sao yup" would result in the y-axis pointing down the bone, the z-axis oriented with the scene's positive y-axis, and the x-axis oriented according to the right hand rule.

-----------------------------------------

spa   : setPreferredAngles [boolean] ['edit']
    Meaningful only in the edit mode. It sets the preferred angles to the current joint angles.

-----------------------------------------

stx   : stiffnessX      [float] ['query', 'edit']
    Set the stiffness (from 0 to 100.0) for x-axis. When queried, this flag returns a float.

-----------------------------------------

sty   : stiffnessY      [float] ['query', 'edit']
    Set the stiffness (from 0 to 100.0) for y-axis. When queried, this flag returns a float.

-----------------------------------------

stz   : stiffnessZ      [float] ['query', 'edit']
    Set the stiffness (from 0 to 100.0) for z-axis. When queried, this flag returns a float.

-----------------------------------------

sym   : symmetry        [boolean] ['edit']
    Create a symmetric joint from the current joint.

-----------------------------------------

sa    : symmetryAxis    [string] ['edit']
    This flag specifies the axis used to mirror symmetric joints. Any combination of x, y, z can be used. This option is only used when the symmetry flag is set to True.

-----------------------------------------

zso   : zeroScaleOrient [boolean]
    It sets the scale orientation to zero and compensate the change by modifing the translation and joint orientation for joint or rotation for general transform of all its child transformations.  The flag will be ignored if the flag -so is set.

    """

def jointCluster(q=1,e=1,ab="float",ac=1,adt="string",av="float",bb="float",bc=1,bdt="string",bv="float",dt=1,j="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/jointCluster.html



-----------------------------------------

jointCluster is undoable, queryable, and editable.

The joint cluster command adds high-level controls to manage the cluster
percentage values on a bound skin around a joint. JointClusters are one way to
create smooth bending behaviour on skin when joints rotate.

    
    
    
    
    
    .                a <---- aboveBound
    .    ____________a_________
    .                a         \
    .     Joint1     a       Joint2
    .   _____________a_______    \
    .                a       \    \     b  <--- belowBound
    .                a        \    \  b
    .                          \    b
    .                           \ b  \
    .                           b\    \
    .                         b   \ Joint3
    
    
    
    

CVs/vertices between Joint1 and aaaaa (aboveBound) receive only
translation/rotation/scale from Joint1. CVs vertices between aaaa and bbbb
transition between translation/rotatation/scale from Joint1 and Joint2. CV2
beyand bbbbb (below bound) receive only translation/ rotation scale from
Joint3.


-----------------------------------------


Return Value:

string  Name of the new jointCluster node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ab    : aboveBound      [float] ['query', 'edit']
    Specifies the where the drop-off begins in the direction of the bone above the joint. A value of 100 indicates the entire length of the bone. The default value is 10.

-----------------------------------------

ac    : aboveCluster    [boolean] ['query']
    Returns the name of the cluster associated with the bone above this joint.

-----------------------------------------

adt   : aboveDropoffType [string] ['query', 'edit']
    Specifies the type of percentage drop-off in the direction of the bone above this joint. Valid values are "linear", "exponential", "sine" and "none". Default is linear.

-----------------------------------------

av    : aboveValue      [float] ['query', 'edit']
    Specifies the drop-off percentage of the joint cluster in the direction of the bone above the cluster. A value of 100 indicates the entire length of the bone. The default value is 50.

-----------------------------------------

bb    : belowBound      [float] ['query', 'edit']
    Specifies where the drop-off ends in the direction of the bone below the joint. A value of 100 indicates the entire length of the bone. The default value is 10.

-----------------------------------------

bc    : belowCluster    [boolean] ['query']
    Returns the name of the cluster associated with this joint.

-----------------------------------------

bdt   : belowDropoffType [string] ['query', 'edit']
    Specifies the type of type of percentage drop-off in the direction of the bone below this joint. Valid values are "linear", "exponential", "sine" and "none". Default is linear.

-----------------------------------------

bv    : belowValue      [float] ['query', 'edit']
    Specifies the drop-off percentage of the joint cluster in the direction of the joint below the cluster. A value of 100 indicates the entire length of the bone. The default value is 50.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Used to query for the helper nodes associated with the jointCluster.

-----------------------------------------

j     : joint           [string] []
    Specifies the joint that the cluster should act about.

-----------------------------------------

n     : name            [string]
    This flag is obsolete.

    """

def jointDisplayScale(q=1,e=1,a=1,ik="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/jointDisplayScale.html



-----------------------------------------

jointDisplayScale is undoable, queryable, and editable.

This action modifies and queries the current display size of skeleton joints.
The joint display size is controlled by a scale factor; a scale factor of 1
sets the display size to its default, which is 1 in diameter. With the plain
format, the float argument is the factor with respect to the default size.
When -a/absolute is used, the float argument refers to the diameter of the
joint display size.


-----------------------------------------


Return Value:

float  Returns current display size of skeleton joints.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] ['query', 'edit']
    Interpret the float argument as the display size as opposed to the scale factor.

-----------------------------------------

ik    : ikfk            [float]
    Set the display size of ik/fk skeleton joints.

    """

def mirrorJoint(mb=1,mxy=1,mxz=1,myz=1,sr="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/mirrorJoint.html



-----------------------------------------

mirrorJoint is undoable, NOT queryable, and NOT editable.

This command will duplicate a branch of the skeleton from the selected joint
symmetrically about a plane in world space. There are three mirroring
modes(xy-, yz-, xz-plane).


-----------------------------------------


Return Value:

string[]  Names of the mirrored joints


-----------------------------------------


Flags:

-----------------------------------------

mb    : mirrorBehavior  [boolean] []
    The mirrorBehavior flag is used to specify that when performing the mirror, the joint orientation axes should be mirrored such that equal rotations on the original and mirrored joints will place the skeleton in a mirrored position (symmetric across the mirroring plane). Thus, animation curves from the original joints can be copied to the mirrored side to produce a similar (but symmetric) behavior. When mirrorBehavior is not specified, the joint orientation on the mirrored side will be identical to the source side.

-----------------------------------------

mxy   : mirrorXY        [boolean] []
    mirror skeleton from the selected joint about xy-plane in world space.

-----------------------------------------

mxz   : mirrorXZ        [boolean] []
    mirror skeleton from the selected joint about xz-plane in world space.

-----------------------------------------

myz   : mirrorYZ        [boolean] []
    mirror skeleton from the selected joint about yz-plane in world space.

-----------------------------------------

sr    : searchReplace   [[string, string]]
    After performing the mirror, rename the new joints by searching the name for the first specified string and replacing it with the second specified string.

    """

def poleVectorConstraint(q=1,e=1,l="string",n="string",rm=1,tl=1,w="float",wal=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/poleVectorConstraint.html



-----------------------------------------

poleVectorConstraint is undoable, queryable, and editable.

Constrains the poleVector of an ikRPsolve handle to point at a target object
or at the average position of a number of targets.

An poleVectorConstraint takes as input one or more "target" DAG transform
nodes at which to aim pole vector for an IK handle using the rotate plane
solver. The pole vector is adjust such that the in weighted average of the
world space position target objects lies is the "rotate plane" of the handle.


-----------------------------------------


Return Value:

string[]  name of the created constraint node    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : layer           [string] ['edit']
    Specify the name of the animation layer where the constraint should be added.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType

-----------------------------------------

rm    : remove          [boolean] ['edit']
    removes the listed target(s) from the constraint.

-----------------------------------------

tl    : targetList      [boolean] ['query']
    Return the list of target objects.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.

-----------------------------------------

wal   : weightAliasList [boolean]
    Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    """

def removeJoint():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/removeJoint.html



-----------------------------------------

removeJoint is undoable, NOT queryable, and NOT editable.

This command will remove the selected joint or the joint given at the command
line from the skeleton.

The given (or selected) joint should not be the root joint of the skeleton,
and not have skin attached. The command works on the given (or selected)
joint. No options or flags are necessary.


-----------------------------------------


Return Value:

None
    """

def reroot():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/reroot.html



-----------------------------------------

reroot is undoable, NOT queryable, and NOT editable.

This command will reroot a skeleton. The selected joint or the given joint at
the command line will be the new root of the skeleton. All ikHandles passing
through the selected joint or above it will be deleted.

The given(or selected) joint should not have skin attached. The command works
on the given or selected joint. No options or flags are necessary.


-----------------------------------------


Return Value:

None
    """

def applyTake(c="string",d="string",f="string",p=1,rc=1,r=1,sc=1,st="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/applyTake.html



-----------------------------------------

applyTake is undoable, NOT queryable, and NOT editable.

This command takes data in a device (refered to as a take) and converts it
into a form that may be played back and reviewed. The take can either be
imported through the readTake action, or recorded by the recordDevice action.
The take is either converted into animation curves or if the -preview flag is
used, into blendDevice nodes.

The command looks for animation curves attached to the target attributes of a
device attachment. If animation curves exist, the take is pasted over the
existing curves. If the curves do not exist, new animation curves are created.

If devices are not specified, all of the devices with take data and that are
enabled for applyTake, will have their data applied.

See also: recordDevice, enableDevice, readTake, writeTake


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

c     : channel         [string] []
    This flag overrides the set channel enable value. If a channel is specified, it will be enabled.   C: The default is all applyTake enabled channels for the device(s).

-----------------------------------------

d     : device          [string] []
    Specifies which device contains the take.   C: The default is all applyTake enabled devices.

-----------------------------------------

f     : filter          [string] []
    This flag specifies the filters to use during the applyTake. If this flag is used multiple times, the ordering of the filters is from left to right.   C: The default is no filters.

-----------------------------------------

p     : preview         [boolean] []
    Applies the take to blendDevice nodes attached to the target attributes connected to the device attachments. Animation curves attached to the attributes will not be altered, but for the time that preview data is defined, the preview data will be the data used during playback.   C: The default is to not preview.

-----------------------------------------

rc    : recurseChannel  [boolean] []
    When this flag is used, the children of the channel(s) specified by -c/channel are also applied. C: The default is all of the enabled channels.

-----------------------------------------

r     : reset           [boolean] []
    Resets the blendDevice nodes affected by -preview. The preview data is removed and if animation curves exist, they are used during playback.

-----------------------------------------

sc    : specifyChannel  [boolean] []
    This flag is used with -c/channel flag. When used, applyTake will only work on the channels listed with the -c/channel flag.   C: The default is all of the enabled channels.

-----------------------------------------

st    : startTime       [time]
    The default start time for a take is determined at record time. The startTime option sets the starting time of the take in the current animation units.   C: The default is the first time stamp of the take. If a time stamp does not exist for the take, 0 is used.

    """

def defineDataServer(d="string",s="string",u=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/defineDataServer.html



-----------------------------------------

defineDataServer is undoable, NOT queryable, and NOT editable.

Connects to the specified data servername, creating a named device which then
can be attached to device handlers.

When the device is defined, it queries queries the server for data axis
information. The "CapChannels" present are represented as axis in form
"channelName"."usage" for scalar channels and "channelName"."component" for
compound channels. See listInputDeviceAxes to list axis names.

Note that undoing

    
    
    defineDataServer -d "myDevice" -s "myServer"
    

does not break the connection with the data server until it cannot be redone.
Executing any other command (sphere for example) will cause this to occur.
Similarly, the command

    
    
    defineDataServer -d "myDevice" -u
    

does not break the connection with the data server until it cannot be undone.
Either flushUndo, or the 'defineDataServer' command falling" off the end of
the undo queue causes this to occur, and the connection. to be broken.

No return value.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

d     : device          [string] []
    specified the device name to be given to the server connection. device name must be unique or the command fails.

-----------------------------------------

s     : server          [string] []
    specifies the name of the server with which the define device connects, and can be specifiied in two ways  name \-- the name of the server socket      Server names of the form name connect to the server socket on the localhost corresponding to name. If name does not begin with "/", then /tmp/name is used. This is the default behavior of most servers. If name begins with "/", name denotes the full path to the socket.  host:service \- a udp service on the specified host.      The service can be any one of a "udp service name," a "port number," or a named service of "tcpmux," and they are found in that order. If host is omitted, the localhost is used.   In any case, if the server cannot be found, the device is not defined (created) and the command fails.

-----------------------------------------

u     : undefine        [boolean]
    undefines (destroys) the dataServer device, closing the connection with the server.

    """

def defineVirtualDevice(q=1,ax="int",c="string",cl=1,cr=1,d="string",p="string",u=1,use="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/defineVirtualDevice.html



-----------------------------------------

defineVirtualDevice is undoable, queryable, and NOT editable.

This command defines a virtual device. Virtual devices act like real devices
and are useful to manipulate/playback data when an command device is not
connected to the computer.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [int] []
    Specifies the axis number of the channel. All children have their axis number determined by their parent's axis number and the width of the parent channel. If this flag is not used, the order of the channel determines the axis number.

-----------------------------------------

c     : channel         [string] []
    After a -create is started, channels may be added to the device definition. The channel string wil be the name of the channel being added to the device. The -channel flag must also be accompanied by the -usage flag and optionally by the -axis flag.

-----------------------------------------

cl    : clear           [boolean] []
    The -clear option will end a device definition and throw away any defined channels.

-----------------------------------------

cr    : create          [boolean] []
    Start defining a virtual device. If a device is currently being defined, the -create flag will produce an error.

-----------------------------------------

d     : device          [string] []
    The -device flag ends the device definition. All of the channels between the -create flag and the -device flag are added to the specified device. If that device already exists, the command will fail and the device should be redefined with another device name. To see the currently defined devices, use the listInputDevices command. The -device flag is also used with -undefine to undefine a virtual device.

-----------------------------------------

p     : parent          [string] []
    Specified the parent channel of the channel being defined. If the channel does not exist, or is an incompatible type, the command will fail.

-----------------------------------------

u     : undefine        [boolean] []
    Undefines the device specified with the -device flag.

-----------------------------------------

use   : usage           [string]
    The -usage option is required for every -channel flag. It describes what usage type the defined channel is. The usage types are:  | unknown| scalar

    """

def deviceManager(q=1,e=1,att=1,acc=1,axi="int",axn=1,axo=1,axs=1,dvi="int",dni="int",nax=1,ndv=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deviceManager.html



-----------------------------------------

deviceManager is undoable, queryable, and editable.

This command queriers the internal device manager for information on attached
devices.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attachment      [boolean] ['query']
    Returns the plugs that a device and axis are attached to. Expects the -deviceIndex and axisIndex to be used in conjunction.

-----------------------------------------

acc   : axisCoordChanges [boolean] ['query']
    Returns whether the axis coordinate changes. Expects the -deviceIndex and -axisIndex flags to be used in conjunction.

-----------------------------------------

axi   : axisIndex       [int] ['query', 'edit']
    Used usually in conjunction with other flags, to indicate the index of the axis.

-----------------------------------------

axn   : axisName        [boolean] ['query']
    Returns the name of the axis. Expects the -deviceIndex and -axisIndex flags to be used in conjunction.

-----------------------------------------

axo   : axisOffset      [boolean] ['query']
    Returns the offset of the axis. Expects the -deviceIndex and -axisIndex flags to be used in conjunction.

-----------------------------------------

axs   : axisScale       [boolean] ['query']
    Returns the scale of the axis. Expects the -deviceIndex and -axisIndex flags to be used in conjunction.

-----------------------------------------

dvi   : deviceIndex     [int] ['query', 'edit']
    Used usually in conjunction with other flags, to indicate the index of the device.

-----------------------------------------

dni   : deviceNameFromIndex [int] ['query']
    Returns the name of the device with the given index.

-----------------------------------------

nax   : numAxis         [boolean] ['query']
    Returns the number of axis this device has. Expects the -deviceIndex flag to be used.

-----------------------------------------

ndv   : numDevices      [boolean]
    Returns the number of devices currently attached.

    """

def enableDevice(q=1,a=1,d="string",en=1,m=1,rec=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/enableDevice.html



-----------------------------------------

enableDevice is undoable, queryable, and NOT editable.

Sets (or queries) the device enable state for actions involving the device.

-monitor
    affects all assignInputDevice and attachDeviceAttr actions for the named device
-record
    controls if the device is recorded (by default) by a recordDevice action
-apply channelName [channelName ... ]
    controls if data from the device channel is applied (by default) by applyTake to the param curves attached to the named channel.

Disabling a channel for applyTake cause applyTake to ignore the enable state
of all "child" channels -- treating them as disabled.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : apply           [boolean] ['query']
    enable/disable "applyTake" for the specified channel(s)

-----------------------------------------

d     : device          [string] ['query']
    specifies the device to change

-----------------------------------------

en    : enable          [boolean] ['query']
    enable (or disable) monitor/record/apply

-----------------------------------------

m     : monitor         [boolean] ['query']
    enables/disables visible update for the device (default)

-----------------------------------------

rec   : record          [boolean]
    enable/disable "recordDevice" device recording

    """

def filter(q=1,e=1,n="string",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filter.html



-----------------------------------------

filter is undoable, queryable, and editable.

Creates or modifies a filter node. Filter nodes are used by applyTake to
modify recorded device data before assigning it to the param curves for the
attached attributes.


-----------------------------------------


Return Value:

string  filter name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name for created filter

-----------------------------------------

t     : type            [string]
    Filter type to create, One of:   | filterEuler | Euler angle "demangler"

    """

def movIn(f="string",st="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/movIn.html



-----------------------------------------

movIn is undoable, NOT queryable, and NOT editable.

Imports a .mov file into animation curves connected to the listed attributes.
The attribute must be writable, since an animation curve will be created and
connected to the attribute. If an animation curve already is connected to the
attribute, the imported data is pasted onto that curve.

The starting time used for the .mov file importation is the current time when
the command is executed.

Valid attribute types are numeric attributes; time attributes; linear
attributes; angular attributes; compound attributes made of the types listed
previously; and multi attributes composed of the types listed previously. If
an unsuppoted attribute type is requested, the command will fail and no data
will be imported. It is important that your user units are set to the same
units used in the .mov file, otherwise linear and angular values will be
incorrect.

To export a .mov file, use the movOut command.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

f     : file            [string] []
    The name of the .mov file. If no extension is used, a .mov will be added.

-----------------------------------------

st    : startTime       [time]
    The default start time for importing the .mov file is the current time. The startTime option sets the starting time for the .mov data in the current time unit.

    """

def movOut(c=1,f="string",pre="uint",t="timerange"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/movOut.html



-----------------------------------------

movOut is undoable, NOT queryable, and NOT editable.

Exports a .mov file from the listed attributes. Valid attribute types are
numeric attributes; time attributes; linear attributes; angular attributes;
compound attributes made of the types listed previously; and multi attributes
composed of the types listed previously.

Length, angle, and time values will be written to the file in the user units.

If an unsupported attribute type is requested, the action will fail. The .mov
file may be read back into Maya using the movIn command.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

c     : comment         [boolean] []
    If true, the attributes written to the .mov file will be listed in a commented section at the top of the .mov file. The default is false.

-----------------------------------------

f     : file            [string] []
    The name of the .mov file. If no extension is used, a .mov will be added.

-----------------------------------------

pre   : precision       [uint] []
    Sets the number of digits to the right of the decimal place in the .mov file.   C: The default is 6.

-----------------------------------------

t     : time            [timerange]
    The time range to save as a .mov file. The default is the current time range.

    """

def readTake(a="string",d="string",f="float",l="string",nt=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/readTake.html



-----------------------------------------

readTake is undoable, NOT queryable, and NOT editable.

This action reads a take (.mov) file to a defined device.  

See also: writeTake, applyTake


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [string] []
    Sets the angular unit used in the take. Valid strings are "deg", "degree", "rad", and "radian".   C: The default is the current user angular unit.

-----------------------------------------

d     : device          [string] []
    Specifies the device into which the take data is read. This is a required argument.

-----------------------------------------

f     : frequency       [float] []
    The timestamp is ignored and the specified frequency is used. If timeStamp data is not in the .mov file, the -noTimestamp flag should also be used. This flag resample, instead the data is assumed to be at the specified frequency.   C: If the take file does not use time stamps, the default frequency is 60Hz.

-----------------------------------------

l     : linear          [string] []
    Sets the linear unit used in the take. Valid strings are "mm", "millimeter", "cm", "centimeter", "m", "meter", "km", "kilometer", "in", "inch", "ft", "foot", "yd", "yard", "mi", and "mile".   C: The default is the current user linear unit.

-----------------------------------------

nt    : noTime          [boolean] []
    Specifies if the take (.mov) file contains time stamps.   C: The default is to assume time stamps are part of the take file.

-----------------------------------------

t     : take            [string]
    Reads the specified take file. It is safest to pass the full path to the flag.

    """

def recordDevice(q=1,c=1,da=1,d="string",dr="int",p=1,st=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/recordDevice.html



-----------------------------------------

recordDevice is undoable, queryable, and NOT editable.

Starts and stops server side device recording. The data is recorded at the
device rate. Once recorded, the data may be brought into Maya with the
applyTake command.  

See also: enableDevice, applyTake, readTake, writeTake


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : cleanup         [boolean] []
    Removes the recorded data from the device.

-----------------------------------------

da    : data            [boolean] ['query']
    Specifies if the device has recorded data. If the device is recording at the time of query, the flag will return false.   Q: When queried, this flag returns an int.

-----------------------------------------

d     : device          [string] []
    Specifies which device(s) to start record recording. The listed device(s) will start recording regardless of their record enable state.   C: The default is to start recording all devices that are record enabled.

-----------------------------------------

dr    : duration        [int] ['query']
    Duration (in seconds) of the recording. When the duration expires, the device will still be in a recording state and must be told to stop recording.   C: The default is 60.   Q: When queried, this flag returns an int.

-----------------------------------------

p     : playback        [boolean] ['query']
    If any attribute is connected to an animation curve, the animation curve will play back while recording the device(s) including any animation curves attached to attributes being recorded.   C: The default is false.   Q: When queried, this flag returns an int.

-----------------------------------------

st    : state           [boolean] ['query']
    Start or stop device recording.   C: The default is true.   Q: When queried, this flag returns an int.

-----------------------------------------

w     : wait            [boolean]
    If -p/playback specified, wait until playback completion before returning control to the user. This flag is ignored if -p is not used.

    """

def writeTake(a="string",d="string",l="string",nt=1,pre="int",t="string",vd="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/writeTake.html



-----------------------------------------

writeTake is undoable, NOT queryable, and NOT editable.

This action writes a take from a device with recorded data to a take (.mov)
file. The writeTake action can also write the virtual definition of a device.

See also: recordDevice, readTake, defineVirtualDevice


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [string] []
    Sets the angular unit used in the take. Valid strings are [deg|degree|rad|radian].   C: The default is the current user angular unit.

-----------------------------------------

d     : device          [string] []
    Specifies the device that contains the take. This is a required argument. If the device does not contain a take, the action will fail.

-----------------------------------------

l     : linear          [string] []
    Sets the linear unit used in the take. Valid strings are [mm|millimeter|cm|centimeter|m|meter|km|kilometer|in|inch|ft|foot|yd|yard|mi|mile]   C: The default is the current user linear unit.

-----------------------------------------

nt    : noTime          [boolean] []
    The take (.mov) file will not contain time stamps.   C: The default is to put time stamps in the take file.

-----------------------------------------

pre   : precision       [int] []
    Sets the number of digits to the right of the decimal place in the take file.   C: The default is 6.

-----------------------------------------

t     : take            [string] []
    Write out the take to a file with the specified name.

-----------------------------------------

vd    : virtualDevice   [string]
    Writes out the virtual device definition to a mel script with the specified file name.

    """

