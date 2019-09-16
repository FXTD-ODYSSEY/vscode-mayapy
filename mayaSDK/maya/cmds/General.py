def about(api=1,a=1,b=1,bd=1,bv=1,cs=1,cm=1,cnt=1,cti=1,cd=1,ct=1,c=1,d=1,env=1,ev=1,f=1,foi=1,hdd=1,iv=1,io=1,ir=1,x64=1,lr=1,li=1,l64=1,lu=1,lrl=1,lt=1,mac=1,ppc=1,x86=1,mjv=1,mnv=1,nt=1,os=1,osv=1,pv=1,pd=1,p=1,qt=1,tab=1,tm=1,uil=1,uis=1,uii=1,ull=1,v=1,w64=1,wm=1,win=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/about.html



-----------------------------------------

about is undoable, NOT queryable, and NOT editable.

This command displays version information about the application if it is
executed without flags. If one of the above flags is specified then the
specified version information is returned.


-----------------------------------------


Return Value:

string  The application's version information.


-----------------------------------------


Flags:

-----------------------------------------

api   : apiVersion      [boolean] []
    Returns the api version.

-----------------------------------------

a     : application     [boolean] []
    Returns the application name string.

-----------------------------------------

b     : batch           [boolean] []
    Returns true if application is in batch mode.

-----------------------------------------

bd    : buildDirectory  [boolean] []
    Returns the build directory string.

-----------------------------------------

bv    : buildVariant    [boolean] []
    Returns the build variant string.

-----------------------------------------

cs    : codeset         [boolean] []
    Returns a string identifying the codeset (codepage) of the locale that Maya is running in. Example return values include "UTF-8", "ISO-8859-1", "1252". Note that the codeset values and naming conventions are highly platform dependent. They may differ in format even if they have the same meaning (e.g. "utf8" vs. "UTF-8").

-----------------------------------------

cm    : compositingManager [boolean] []
    On Linux, returns true if there is a compositing manager running; on all other platforms, it always returns true.

-----------------------------------------

cnt   : connected       [boolean] []
    Return whether the user is connected or not to the Internet.

-----------------------------------------

cti   : ctime           [boolean] []
    Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0

-----------------------------------------

cd    : currentDate     [boolean] []
    Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.

-----------------------------------------

ct    : currentTime     [boolean] []
    Returns the current time in the format hh:mm:ss, e.g. 14:27:53.

-----------------------------------------

c     : cutIdentifier   [boolean] []
    Returns the cut string.

-----------------------------------------

d     : date            [boolean] []
    Returns the build date string.

-----------------------------------------

env   : environmentFile [boolean] []
    Returns the location of the application defaults file.

-----------------------------------------

ev    : evalVersion     [boolean] []
    This flag is now deprecated. Always returns false, as the eval version is no longer supported.

-----------------------------------------

f     : file            [boolean] []
    Returns the file version string.

-----------------------------------------

foi   : fontInfo        [boolean] []
    Returns a string of the specifications of the fonts requested, and the specifications of the fonts that are actually being used.

-----------------------------------------

hdd   : helpDataDirectory [boolean] []
    Returns the help data directory.

-----------------------------------------

iv    : installedVersion [boolean] []
    Returns the product version string.

-----------------------------------------

io    : ioVersion       [boolean] []
    Returns true if this is the Maya IO version of the application.

-----------------------------------------

ir    : irix            [boolean] []
    Returns true if the operating system is Irix. Always false with support for Irix removed.

-----------------------------------------

x64   : is64            [boolean] []
    Returns true if the application is 64 bit.

-----------------------------------------

lr    : languageResources [boolean] []
    Returns a string array of the currently installed language resources. Each string entry consists of three elements delimited with a colon (':'). The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country code). The second token is the language name in English. This third token is the alpha-3 code (ISO 639-2). For example English is represented as "en_US:English:enu".

-----------------------------------------

li    : linux           [boolean] []
    Returns true if the operating system is Linux.

-----------------------------------------

l64   : linux64         [boolean] []
    Returns true if the operating system is Linux 64 bit.

-----------------------------------------

lu    : liveUpdate      [boolean] []
    This flag is deprecated(2019) and may be removed in future releases of Maya. Returns Autodesk formatted product information.

-----------------------------------------

lrl   : localizedResourceLocation [boolean] []
    Returns the path to the top level of the localized resource directory, if we are running in an alternate language. Returns an empty string if we are running in the default language.

-----------------------------------------

lt    : ltVersion       [boolean] []
    Returns true if this is the Maya LT version of the application.

-----------------------------------------

mac   : macOS           [boolean] []
    Returns true if the operating system is Macintosh.

-----------------------------------------

ppc   : macOSppc        [boolean] []
    Returns true if the operating system is a PowerPC Macintosh.

-----------------------------------------

x86   : macOSx86        [boolean] []
    Returns true if the operating system is an Intel Macintosh.

-----------------------------------------

mjv   : majorVersion    [boolean] []
    Returns the major version of Maya.

-----------------------------------------

mnv   : minorVersion    [boolean] []
    Returns the minor version of Maya.

-----------------------------------------

nt    : ntOS            [boolean] []
    Returns true if the operating system is Windows.

-----------------------------------------

os    : operatingSystem [boolean] []
    Returns the operating system type. Valid return types are "nt", "win64", "mac", "linux" and "linux64"

-----------------------------------------

osv   : operatingSystemVersion [boolean] []
    Returns the operating system version. on Linux this returns the equivalent of uname -srvm

-----------------------------------------

pv    : patchVersion    [boolean] []
    Returns the patch version of Maya.

-----------------------------------------

pd    : preferences     [boolean] []
    Returns the location of the preferences directory.

-----------------------------------------

p     : product         [boolean] []
    Returns the license product name.

-----------------------------------------

qt    : qtVersion       [boolean] []
    Returns Qt version string.

-----------------------------------------

tab   : tablet          [boolean] []
    Windows only. Returns true if the PC is a Tablet PC.

-----------------------------------------

tm    : tabletMode      [boolean] []
    Windows 8 (and above) only. If your device is a Tablet PC, then the convertible mode the device is currently running in. Returns either: tablet or laptop (keyboard attached). See the tablet flag.

-----------------------------------------

uil   : uiLanguage      [boolean] []
    Returns the language that Maya's running in. Example return values include "en_US" for English and "ja_JP" for Japanese.

-----------------------------------------

uis   : uiLanguageForStartup [boolean] []
    Returns the language that is used for Maya's next start up. This is read from config file and is rewritten after setting ui language in preference.

-----------------------------------------

uii   : uiLanguageIsLocalized [boolean] []
    Returns true if we are running in an alternate language, not the default (English).

-----------------------------------------

ull   : uiLocaleLanguage [boolean] []
    Returns the language locale of the OS. English is default.

-----------------------------------------

v     : version         [boolean] []
    Returns the version string.

-----------------------------------------

w64   : win64           [boolean] []
    Returns true if the operating system is Windows x64 based.

-----------------------------------------

wm    : windowManager   [boolean] []
    Returns the name of the Window Manager that is assumed to be running.

-----------------------------------------

win   : windows         [boolean]
    Returns true if the operating system is Windows based.

    """

def affectedNet(q=1,e=1,n="string",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/affectedNet.html



-----------------------------------------

affectedNet is undoable, queryable, and editable.

This command gets the list of attributes on a node or node type and creates
nodes of type TdnAffect, one for each attribute, that are connected iff the
source node's attribute affects the destination node's attribute.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name to use for this command

-----------------------------------------

t     : type            [string]
    Get information from the given node type instead of one node

    """

def affects(by=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/affects.html



-----------------------------------------

affects is NOT undoable, NOT queryable, and NOT editable.

This command returns the list of attributes on a node or node type which
affect the named attribute.


-----------------------------------------


Return Value:

string  List of affected/affecting attributes


-----------------------------------------


Flags:

-----------------------------------------

by    : by              [boolean] []
    Show attributes that are affected by the given one rather than the ones that affect it.

-----------------------------------------

t     : type            [string]
    static node type from which to get 'affects' information

    """

def align(atl=1,cs="name",x="string",y="string",z="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/align.html



-----------------------------------------

align is undoable, NOT queryable, and NOT editable.

Align or spread objects along X Y and Z axis.


-----------------------------------------


Return Value:

boolean  true/false


-----------------------------------------


Flags:

-----------------------------------------

atl   : alignToLead     [boolean] []
    When set, the min, center or max values are computed from the lead object. Otherwise, the values are averaged for all objects.   Default is false

-----------------------------------------

cs    : coordinateSystem [name] []
    Defines the X, Y, and Z coordinates. Default is the world coordinates

-----------------------------------------

x     : xAxis           [string] []
    Any of none, min, mid, max, dist, stack.   This defines the kind of alignment to perfom, default is none.

-----------------------------------------

y     : yAxis           [string] []
    Any of none, min, mid, max, dist, stack.   This defines the kind of alignment to perfom, default is none.

-----------------------------------------

z     : zAxis           [string]
    Any of none, min, mid, max, dist, stack.   This defines the kind of alignment to perfom, default is none.

    """

def assembly(q=1,e=1,a="string",al="string",cc="string",cob="script",cr="string",dt="string",dr="string",d="string",input="string",isa="string",ite="string",lbl="string",lrt=1,lrp="script",lr=1,lt=1,n="string",nrl="string",aoc="script",prc="script",rnr="string",rl="string",rnm="string",rns="string",poc="string",pec="string",rt="string",rtl="string",rtp="script",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/assembly.html



-----------------------------------------

assembly is undoable, queryable, and editable.

Command to register assemblies for the scene assembly framework, to create
them, and to edit and query them. Assembly nodes are DAG nodes, and are
therefore shown in the various DAG editors (Outliner, Hypergraph, Node
Editor). At assembly creation time, the node name defaults to the node type
name. The assembly command can create any node that is derived from the
assembly node base class. It also acts as a registry of these types, so that
various scripting callbacks can be defined and registered with the assembly
command. These callbacks are invoked by Maya during operations on assembly
nodes, and can be used to customize behavior.

## Registering a new assembly type

When defining a new type of assembly derived from the assembly node base
class, a number of procedures can be defined through the assembly command to
properly integrate the new assembly node type into Maya. Most of these
procedures are used to integrate the assembly type with the Maya user
interface, and are not required for non-interactive scripting use. For more
information, see the MPxAssembly class description in the Maya API
documentation. Some of the important procedures that can be registered through
the assembly command are the following:

listRepTypesProc

    Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node. 
repTypeLabelProc

    Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
createOptionBoxProc

    Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
repPreCreateUIProc

    Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
postCreateUIProc

    Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : active          [string] ['query', 'edit']
    Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.

-----------------------------------------

al    : activeLabel     [string] ['query', 'edit']
    Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an array of strings when multiple assemblies are specified.

-----------------------------------------

cc    : canCreate       [string] ['query']
    Query the representation types the specific assembly can create.

-----------------------------------------

cob   : createOptionBoxProc [script] ['query', 'edit']
    Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.

-----------------------------------------

cr    : createRepresentation [string] ['edit']
    Create and add a specific type of representation for an assembly. If the representation type needs additional parameters, they must be specified using the "input" flag. For example, the Maya scene assembly reference implementation Cache and Scene representations need an input file.

-----------------------------------------

dt    : defaultType     [string] ['query', 'edit']
    Set or query the default type of assembly. When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify an explicit assembly type.

-----------------------------------------

dr    : deleteRepresentation [string] ['edit']
    Delete a specific representation from an assembly.

-----------------------------------------

d     : deregister      [string] ['edit']
    Deregister a registered assembly type. If the deregistered type is the default type, the default type will be set to the empty string.

-----------------------------------------

input : input           [string] ['edit']
    Specify the additional parameters of representation creation procedure when creating a representation. This flag must be used with createRepresentation flag.

-----------------------------------------

isa   : isAType         [string] ['query']
    Query whether the given object is of an assembly type.

-----------------------------------------

ite   : isTrackingMemberEdits [string] ['query']
    Query whether the given object is tracking member edits.

-----------------------------------------

lbl   : label           [string] ['query', 'edit']
    Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.

-----------------------------------------

lrt   : listRepTypes    [boolean] ['query']
    Query the supported representation types for a given assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.

-----------------------------------------

lrp   : listRepTypesProc [script] ['query', 'edit']
    Set or query the procedure that provides the representation type list which an assembly type supports. This procedure takes no argument, and returns a string array of representation types that represents the full set of representation types this assembly type can create. The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.

-----------------------------------------

lr    : listRepresentations [boolean] ['query']
    Query the created representations list for a specific assembly. The -repType flag can be used to filter the list and return representations for a single representation type. If the -repType flag is not used, all created representations will be returned.

-----------------------------------------

lt    : listTypes       [boolean] ['query']
    Query the supported assembly types.

-----------------------------------------

n     : name            [string] []
    Specify the name of the assembly when creating it.

-----------------------------------------

nrl   : newRepLabel     [string] ['edit']
    Specify the representation label to set on representation label edit.

-----------------------------------------

aoc   : postCreateUIProc [script] ['query', 'edit']
    Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting. It can be used to invoke a dialog, to obtain and set initial parameters on a newly- created assembly. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.

-----------------------------------------

prc   : proc            [script] ['edit']
    Specify the procedure when setting the representation UI post- or pre- creation procedure, for a given assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.

-----------------------------------------

rnr   : renameRepresentation [string] ['edit']
    Renames the representation that is the argument to this flag. The repName flag must be used to provide the new name.

-----------------------------------------

rl    : repLabel        [string] ['query', 'edit']
    Query or edit the label of the representation that is the argument to this flag, for a given assembly. In both query and edit modes, the -repLabel flag specifies the name of the representation. In edit mode, the -newRepLabel flag must be used to specify the new representation label.  In query mode, this flag needs a value.

-----------------------------------------

rnm   : repName         [string] ['edit']
    Specify the representation name to set on representation creation or rename. This flag is optional with the createRepresentation flag: if omitted, the assembly will name the representation. It is mandatory with the renameRepresentation flag.

-----------------------------------------

rns   : repNamespace    [string] ['query']
    Query the representation namespace of this assembly node. The value returned is used by Maya for creating the namespace where nodes created by the activation of a representation will be added. If a name clash occurs when the namespace is added to its parent namespace, Maya will update repNamespace with the new name. Two namespaces are involved when dealing with an assembly node: the namespace of the assembly node itself (which this flag does not affect or query), and the namespace of its representations. The representation namespace is a child of its assembly node's namespace. The assembly node's namespace is set by its containing assembly, if it is nested, or by the top-level file. Either the assembly node's namespace, or the representation namespace, or both, can be the empty string. It should be noted that if the assembly node is nested, the assembly node's namespace will be (by virtue of its nesting) the representation namespace of its containing assembly.

-----------------------------------------

poc   : repPostCreateUIProc [string] ['query', 'edit']
    Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type. This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation. It returns no value. It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting. It can be used to invoke a dialog, to obtain and set initial parameters on a newly-created representation. The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.  In query mode, this flag needs a value.

-----------------------------------------

pec   : repPreCreateUIProc [string] ['query', 'edit']
    Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type. This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting. It can be used to invoke a dialog, to obtain the creation argument for a new representation. The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.  In query mode, this flag needs a value.

-----------------------------------------

rt    : repType         [string] ['query']
    Specify a representation type to use as a filter for the -listRepresentations query. The representation type is the argument to this flag.  In query mode, this flag needs a value.

-----------------------------------------

rtl   : repTypeLabel    [string] ['query']
    Query the label of the specific representation type.  In query mode, this flag needs a value.

-----------------------------------------

rtp   : repTypeLabelProc [script] ['query', 'edit']
    Set or query the procedure that provides the representation type label, for a given assembly type. The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.

-----------------------------------------

typ   : type            [string]
    Set or query properties for the specified registered assembly type.  In query mode, this flag needs a value.

    """

def bakePartialHistory(q=1,e=1,all=1,nps=1,pc=1,pre=1,ppt=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bakePartialHistory.html



-----------------------------------------

bakePartialHistory is undoable, queryable, and editable.

This command is used to bake sections of the construction history of a shape
node when possible. A typical usage would be on a shape that has both
modelling operations and deformers in its history. Using this command with the
-prePostDeformers flag will bake the modeling portions of the graph, so that
only the deformers remain.

Note that not all modeling operations can be baked such that they create
exactly the same effect after baking. For example, imagine the history
contains a skinning operation followed by a smooth. Before baking, the smooth
operation is performed each time the skin deforms, so it will smooth
differently depending on the output of the skin. When the smooth operation is
baked into the skinning, the skin will be reweighted based on the smooth
points to attempt to approximate the original behavior. However, the skin node
does not perform the smooth operation, it merely performs skinning with the
newly calculated weights and the result will not be identical to before the
bake.

In general, modeling operations that occur before deformers can be baked
precisely. Those which occur after can only be approximated. The -pre and
-post flags allow you to control whether only the operations before or after
the deformers are baked.

When the command is used on an object with no deformers, the entire history
will be deleted.


-----------------------------------------


Return Value:

string  name of shapes that were baked    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : allShapes       [boolean] ['query']
    Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and end successfully.

-----------------------------------------

nps   : postSmooth      [boolean] ['query']
    Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values. The default is false.

-----------------------------------------

pc    : preCache        [boolean] ['query']
    Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.

-----------------------------------------

pre   : preDeformers    [boolean] ['query']
    Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.

-----------------------------------------

ppt   : prePostDeformers [boolean]
    Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the default. In query mode, returns a list of the nodes that will be baked.

    """

def baseTemplate(q=1,e=1,ex=1,fn="string",f=1,l=1,mf="string",si=1,u=1,vl="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/baseTemplate.html



-----------------------------------------

baseTemplate is NOT undoable, queryable, and editable.

This is the class for the commands that edit and/or query templates.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] ['query']
    Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.

-----------------------------------------

fn    : fileName        [string] ['query']
    Specifies the filename associated with the template. This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used. It is recommended but not required that the filename and template name correspond.

-----------------------------------------

f     : force           [boolean] []
    This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file. When used in create mode, it will allow an existing template to be recreated (for example when using fromContainer argument to regenerate a template).

-----------------------------------------

l     : load            [boolean] []
    Load an existing template from a file. If a filename is specified for the template, the entire file (and all templates in it) will be loaded. If no file is specified, a default filename will be assumed, based on the template name.

-----------------------------------------

mf    : matchFile       [string] ['query']
    Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.  In query mode, this flag needs a value.

-----------------------------------------

si    : silent          [boolean] ['query', 'edit']
    Silent mode will suppress any error or warning messages that would normally be reported from the command execution. The return values are unaffected.

-----------------------------------------

u     : unload          [boolean] []
    Unload the specified template. This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.

-----------------------------------------

vl    : viewList        [string]
    Used in query mode, returns a list of all views defined on the template.

    """

def baseView(q=1,e=1,ii="string",il=1,vd=1,vb=1,vl=1,vn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/baseView.html



-----------------------------------------

baseView is NOT undoable, queryable, and editable.

A view defines the layout information for the attributes of a particular node
type or container. Views can be selected from a set of built-in views or may
be defined on an associated container template. This command queries the view-
related information for a container node or for a given template. The
information returned from this command will be based on the view-related
settings in force on the container node at the time of the query (i.e. the
container's view mode, template name, view name attributes), when applicable.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ii    : itemInfo        [string] ['query']
    Used in query mode in conjunction with the itemList flag. The command will return a list of information for each item in the view, the information fields returned for each item are determined by this argument value. The information fields will be listed in the string array returned. The order in which the keyword is specified will determine the order in which the data will be returned by the command. One or more of the following keywords, separated by colons ':' are used to specify the argument value.    * itemIndex : sequential item number (0-based)   * itemName : item name (string)   * itemLabel : item display label (string)   * itemDescription : item description field (string)   * itemLevel : item hierarchy level (0-n)   * itemIsGroup : (boolean 0 or 1) indicates whether or not this item is a group   * itemIsAttribute : (boolean 0 or 1) indicates whether or not this item is an attribute   * itemNumChildren: number of immediate children (groups or attributes) of this item   * itemAttrType : item attribute type (string)   * itemCallback : item callback field (string)  In query mode, this flag needs a value.

-----------------------------------------

il    : itemList        [boolean] ['query']
    Used in query mode, the command will return a list of information for each item in the view. The viewName flag is used to select the view to query. The information returned about each item is determined by the itemInfo argument value. For efficiency, it is best to query all necessary item information at one time (to avoid recomputing the view information on each call).

-----------------------------------------

vd    : viewDescription [boolean] ['query']
    Used in query mode, returns the description field associated with the selected view. If no description was defined for this view, the value will be empty.

-----------------------------------------

vb    : viewLabel       [boolean] ['query']
    Used in query mode, returns the display label associated with the view. An appropriate label suitable for the user interface will be returned based on the selected view. Use of the view label is usually more suitable than the view name for display purposes.

-----------------------------------------

vl    : viewList        [boolean] ['query']
    Used in query mode, command will return a list of all views defined for the given target (container or template).

-----------------------------------------

vn    : viewName        [string]
    Used in query mode, specifies the name of the queried view when used in conjunction with a template target. When used in conjunction with a container target, it requires no string argument, and returns the name of the currently active view associated with the container; this value may be empty if the current view is not a valid template view or is generated by one of the built- in views modes. For this reason, the view label is generally more suitable for display purposes.  In query mode, this flag can accept a value.

    """

def color(rgb="[float, float, float]",ud="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/color.html



-----------------------------------------

color is undoable, NOT queryable, and NOT editable.

This command sets the dormant wireframe color of the specified objects to be
their class color or if the -ud/userDefined flag is specified, one of the user
defined colors. The -rgb/rgbColor flags can be specified if the user requires
floating point RGB colors.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

rgb   : rgbColor        [[float, float, float]] []
    Specifies and rgb color to set the selected object to.

-----------------------------------------

ud    : userDefined     [int]
    Specifies the user defined color index to set selected object to. The valid range of numbers is [1-8].

    """

def colorIndex(q=1,hsv=1,rf=1,rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/colorIndex.html



-----------------------------------------

colorIndex is undoable, queryable, and NOT editable.

The index specifies a color index in the color palette. The r, g, and b values
(between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
used) for the color.


-----------------------------------------


Return Value:

int  Returns 1 on success.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

hsv   : hueSaturationValue [boolean] ['query']
    Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.

-----------------------------------------

rf    : resetToFactory  [boolean] []
    Resets all color index palette entries to their factory defaults.

-----------------------------------------

rs    : resetToSaved    [boolean]
    Resets all color palette entries to their saved values.

    """

def colorManagementCatalog(adt="string",eut="string",lse=1,ltc=1,pth="string",qut=1,rmt="string",tcn="string",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/colorManagementCatalog.html



-----------------------------------------

colorManagementCatalog is NOT undoable, NOT queryable, and NOT editable.

This non-undoable action performs additions and removals of custom color
transforms from the Autodesk native color transform catalog. Once a custom
color transform has been added to the catalog, it can be used in the same way
as the builtin Autodesk native color transforms.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

adt   : addTransform    [string] []
    Add transform to collection.

-----------------------------------------

eut   : editUserTransformPath [string] []
    Edit the user transform directory. By changing the directory, all custom transforms currently added could be changed, and new ones could appear.

-----------------------------------------

lse   : listSupportedExtensions [boolean] []
    List the file extensions that are supported by add transform. This list is valid for all transform types, and therefore this flag does not require use of the type flag.

-----------------------------------------

ltc   : listTransformConnections [boolean] []
    List the transforms that can be used as source (for "view" and "output" types) or destination (for "input" and "rendering space" types) to connect a custom transform to the rest of the transform collection.

-----------------------------------------

pth   : path            [string] []
    In addTransform mode, the path to the transform data file.

-----------------------------------------

qut   : queryUserTransformPath [boolean] []
    Query the user transform directory.

-----------------------------------------

rmt   : removeTransform [string] []
    Remove transform from collection.

-----------------------------------------

tcn   : transformConnection [string] []
    In addTransform mode, an existing transform to which the added transform will be connected. For an input transform or rendering space transform, this will be a destination. For a view or output transform, this will be a source.

-----------------------------------------

typ   : type            [string]
    The type of transform added, removed, or whose transform connections are to be listed. Must be one of "view", "rendering space", "input", or "output".

    """

def colorManagementConvert(tds="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/colorManagementConvert.html



-----------------------------------------

colorManagementConvert is NOT undoable, NOT queryable, and NOT editable.

This command can be used to convert rendering (a.k.a. working) space color
values to display space color values. This is useful if you create custom UI
with colors painted to screen, where you need to handle color management
yourself. The current view transform set in the Color Management user
preferences will be used.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

tds   : toDisplaySpace  [[float, float, float]]
    Converts the given RGB value to display space.

    """

def colorManagementFileRules(q=1,e=1,add="string",cs="string",dwn="string",ev="string",ext="string",lsr=1,ld=1,up="string",pat="string",rm="string",rde=1,sav=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/colorManagementFileRules.html



-----------------------------------------

colorManagementFileRules is NOT undoable, queryable, and editable.

This non-undoable action manages the list of rules that Maya uses to assign an
initial input color space to dependency graph nodes that read in color
information from a file. Rules are structured in a chain of responsibility,
from highest priority rule to lowest priority rule, each rule matching a file
path pattern and extension. If a rule matches a given file path, its color
space is returned as the result of rules evaluation, and no further rule is
considered. The lowest priority rule will always return a match. Rules can be
added, removed, and changed in priority in the list. Each rule can have its
file path pattern, extension, and color space changed. The rule list can be
saved to user preferences, and loaded from user preferences.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addRule         [string] ['edit']
    Add a rule with the argument name to the list of rules, as the highest- priority rule. If this flag is used, the pattern, extension, and colorSpace flags must be used as well, to specify the file rule pattern, extension, and color space, respectively.

-----------------------------------------

cs    : colorSpace      [string] ['query', 'edit']
    The input color space for the rule. If the rule matches a file path, this is the color space that is returned. This color space must match an existing color space in the input color space list.

-----------------------------------------

dwn   : down            [string] ['edit']
    Move the rule with the argument name down one position towards lower priority.

-----------------------------------------

ev    : evaluate        [string] ['edit']
    Evaluates the list of rules and returns the input color space name that corresponds to the argument file path.

-----------------------------------------

ext   : extension       [string] ['query', 'edit']
    The file extension for the rule is case insensitive

-----------------------------------------

lsr   : listRules       [boolean] ['edit']
    Returns an array of rule name strings, in order, from lowest-priority (rule 0) to highest-priority (last rule in array).

-----------------------------------------

ld    : load            [boolean] ['edit']
    Read the rules from Maya preferences. Any existing rules are cleared.

-----------------------------------------

up    : moveUp          [string] ['edit']
    Move the rule with the argument name up one position towards higher priority.

-----------------------------------------

pat   : pattern         [string] ['query', 'edit']
    The file path pattern for the rule. This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see http://en.wikipedia.org/wiki/Glob_%28programming%29.

-----------------------------------------

rm    : remove          [string] ['edit']
    Remove the rule with the argument name from the list of rules.

-----------------------------------------

rde   : restoreDefaults [boolean] ['edit']
    Restore the list of rules to the default ones only.

-----------------------------------------

sav   : save            [boolean]
    Save the rules to Maya preferences.

    """

def colorManagementPrefs(q=1,e=1,cfe=1,cme=1,cma=1,cmp=1,cmn=1,cmv="string",cfp="string",din="string",etp="string",epy="string",ie=1,iss=1,lpy="string",ldn="string",lon="string",lrn="string",lvn="string",mcn=1,ore=1,ott="string",ote=1,otn="string",ots=1,otc=1,ovt=1,pfn="string",poe=1,rfr=1,rsn="string",rss=1,rde=1,vtn="string",vts=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/colorManagementPrefs.html



-----------------------------------------

colorManagementPrefs is undoable, queryable, and editable.

This command allows querying and editing the color management global data in a
scene. It also allows for setting the view transform and rendering space which
automatically configures the color processing in the enabled views.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cfe   : cmConfigFileEnabled [boolean] ['query', 'edit']
    Turn on or off applying an OCIO configuration file. If set, the color management configuration set in the preferences is used.

-----------------------------------------

cme   : cmEnabled       [boolean] ['query', 'edit']
    Turn on or off color management in general. If set, the color management configuration set in the preferences is used.

-----------------------------------------

cma   : colorManageAllNodes [boolean] ['query', 'edit']
    Adds color management to all input nodes such as file texture nodes

-----------------------------------------

cmp   : colorManagePots [boolean] ['query', 'edit']
    Turn on or off color management of color pots in the UI. If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.

-----------------------------------------

cmn   : colorManagedNodes [boolean] ['query', 'edit']
    Gets the names of all nodes that apply color management to bring pixels from an input color space to the rendering space. Examples include file texture node.

-----------------------------------------

cmv   : colorManagementSDKVersion [string] ['query', 'edit']
    Obtain the version of the color management SDK used by Maya.

-----------------------------------------

cfp   : configFilePath  [string] ['query', 'edit']
    The configuration file to be used, if color management is enabled.

-----------------------------------------

din   : defaultInputSpaceName [string] ['query', 'edit']
    This flag is obsolete. See the colorManagementFileRules command for more information.

-----------------------------------------

etp   : equalsToPolicyFile [string] ['query', 'edit']
    Query if the current loaded policy settings is the same with the settings described in the policy file which is the argument of the command.  In query mode, this flag needs a value.

-----------------------------------------

epy   : exportPolicy    [string] ['query', 'edit']
    Export the color management parameters to policy file

-----------------------------------------

ie    : inhibitEvents   [boolean] ['query', 'edit']
    Inhibit client-server notifications and event triggers which occur when changing the color management settings.

-----------------------------------------

iss   : inputSpaceNames [boolean] ['query', 'edit']
    Returns the list of available input color spaces. Used to populate the input color spaces UI popup.

-----------------------------------------

lpy   : loadPolicy      [string] ['query', 'edit']
    Load the color management policy file. This file overides the color management settings.

-----------------------------------------

ldn   : loadedDefaultInputSpaceName [string] ['query', 'edit']
    This flag is obsolete.

-----------------------------------------

lon   : loadedOutputTransformName [string] ['query', 'edit']
    Gets the loaded output transform. Used by file open, import, and reference to check for missing color spaces or transforms.

-----------------------------------------

lrn   : loadedRenderingSpaceName [string] ['query', 'edit']
    Gets the loaded rendering space. Used by file open, import, and reference to check for missing color spaces or transforms.

-----------------------------------------

lvn   : loadedViewTransformName [string] ['query', 'edit']
    Gets the loaded view transform. Used by file open, import, and reference to check for missing color spaces or transforms.

-----------------------------------------

mcn   : missingColorSpaceNodes [boolean] ['query', 'edit']
    Gets the names of the nodes that have color spaces not defined in the selected transform collection.

-----------------------------------------

ore   : ocioRulesEnabled [boolean] ['query', 'edit']
    Turn on or off the use of colorspace assignment rules from the OCIO library.

-----------------------------------------

ott   : outputTarget    [string] ['query', 'edit']
    Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast".  In query mode, this flag needs a value.

-----------------------------------------

ote   : outputTransformEnabled [boolean] ['query', 'edit']
    Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.

-----------------------------------------

otn   : outputTransformName [string] ['query', 'edit']
    The output transform to be applied for out of viewport renders. Disables output use view transform mode.

-----------------------------------------

ots   : outputTransformNames [boolean] ['query', 'edit']
    Returns the list of available output transforms.

-----------------------------------------

otc   : outputTransformUseColorConversion [boolean] ['query', 'edit']
    Turn on or off selecting the color space conversion for the output color space of viewport renders. If set, a conversion color space is used; otherwise, a view transform is used.

-----------------------------------------

ovt   : outputUseViewTransform [boolean] ['query', 'edit']
    Turns use view transform mode on. In this mode, the output transform is set to match the view transform. To turn the mode off, set an output transform using the outputTransformName flag.

-----------------------------------------

pfn   : policyFileName  [string] ['query', 'edit']
    Set the policy file name

-----------------------------------------

poe   : popupOnError    [boolean] ['query', 'edit']
    Turn on or off displaying a modal popup on error (as well as the normal script editor reporting of the error), for this invocation of the command. Default is off.

-----------------------------------------

rfr   : refresh         [boolean] ['query', 'edit']
    Refresh the color management.

-----------------------------------------

rsn   : renderingSpaceName [string] ['query', 'edit']
    The color space to be used during rendering. This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.

-----------------------------------------

rss   : renderingSpaceNames [boolean] ['query', 'edit']
    Returns the list of available rendering spaces. Used to populate the color management preference UI popup.

-----------------------------------------

rde   : restoreDefaults [boolean] ['query', 'edit']
    Restore the color management settings to their default value.

-----------------------------------------

vtn   : viewTransformName [string] ['query', 'edit']
    The view transform to be applied by color managed viewers and color managed UI controls.

-----------------------------------------

vts   : viewTransformNames [boolean]
    Returns the list of available view transforms. Used to populate the color management preference UI popup.

    """

def commandLogging(q=1,hs="uint",lc=1,lf="string",rc=1,rl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/commandLogging.html



-----------------------------------------

commandLogging is undoable, queryable, and NOT editable.

This command controls logging of Maya commands, in memory and on disk.

Note that if commands are logged in memory, they will be available to the
crash reporter and appear in crash logs.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

hs    : historySize     [uint] ['query']
    Sets the number of entries in the in-memory command history.

-----------------------------------------

lc    : logCommands     [boolean] ['query']
    Enables or disables the on-disk logging of commands.

-----------------------------------------

lf    : logFile         [string] ['query']
    Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.

-----------------------------------------

rc    : recordCommands  [boolean] ['query']
    Enables or disables the in-memory logging of commands.

-----------------------------------------

rl    : resetLogFile    [boolean]
    Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).

    """

def commandPort(q=1,bs="int",cl=1,eo=1,lp=1,n="string",nr=1,po=1,pre="string",rnc=1,sw=1,stp="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/commandPort.html



-----------------------------------------

commandPort is undoable, queryable, and NOT editable.

Opens or closes the Maya command port. The command port comprises a socket to
which a client program may connect. An example command port client "mcp" is
included in the Motion Capture developers kit.

It supports multi-byte commands and uses utf-8 as its transform format. It
will receive utf8 command string and decode it to Maya native coding. The
result will also be encoded to utf-8 before sending back.

Care should be taken regarding INET domain sockets as no user identification,
or authorization is required to connect to a given socket, and all commands
(including "system(...)") are allowed and executed with the user id and
permissions of the Maya user. The prefix flag can be used to reduce this
security risk, as only the prefix command is executed.

The query flag can be used to determine if a given command port exists. See
examples below.


-----------------------------------------


Return Value:

boolean  \- in query mode    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bs    : bufferSize      [int] []
    Commands and results are each subject to size limits. This option allows the user to specify the size of the buffer used to communicate with Maya. If unspecified the default buffer size is 4096 characters. Commands longer than bufferSize characters will cause the client connection to close. Results longer that bufferSize characters are replaced with an error message.

-----------------------------------------

cl    : close           [boolean] []
    Closes the commandPort, deletes the pipes

-----------------------------------------

eo    : echoOutput      [boolean] []
    Sends a copy of all command output to the command port. Typically only the result is transmitted. This option provides a copy of all output.

-----------------------------------------

lp    : listPorts       [boolean] []
    Returns the available ports

-----------------------------------------

n     : name            [string] []
    Specifies the name of the command port which this command creates. CommandPort names of the form name create a UNIX domain socket on the localhost corresponding to name. If name does not begin with "/", then /tmp/name is used. If name begins with "/", name denotes the full path to the socket. Names of the form :port number create an INET domain on the local host at the given port.

-----------------------------------------

nr    : noreturn        [boolean] []
    Do not write the results from executed commands back to the command port socket. Instead, the results from executed commands are written to the script editor window. As no information passes back to the command port client regarding the execution of the submitted commands, care must be taken not to overflow the command buffer, which would cause the connection to close.

-----------------------------------------

po    : pickleOutput    [boolean] []
    Python output will be pickled.

-----------------------------------------

pre   : prefix          [string] []
    The string argument is the name of a Maya command taking one string argument. This command is called each time data is sent to the command port. The data written to the command port is passed as the argument to the prefix command. The data from the command port is encoded as with enocodeString and enclosed in quotes. If newline characters are embedded in the command port data, the input is split into individual lines. These lines are treated as if they were separate writes to the command port. Only the result to the last prefix command is returned.

-----------------------------------------

rnc   : returnNumCommands [boolean] []
    Ignore the result of the command, but return the number of commands that have been read and executed in this call. This is a simple way to track buffer overflow. This flag is ignored when the noreturn flag is specified.

-----------------------------------------

sw    : securityWarning [boolean] []
    Enables security warning on command port input.

-----------------------------------------

stp   : sourceType      [string]
    The string argument is used to indicate which source type would be passed to the commandPort, like "mel", "python". The default source type is "mel".

    """

def container(q=1,e=1,an="string[]",a="string[]",am="string",ba="[string, string]",cl=1,c=1,fn="string[]",fc="string[]",f=1,iha=1,ihb=1,inc=1,ind="string",isd=1,ish=1,it=1,isc=1,n="string",nl=1,nnp=1,par=1,p=1,pb="[string, string]",pac="[string, string]",pap="[string, string]",pro="[string, boolean]",pa="string",pc=1,pn="string",rc=1,rn="string[]",typ="string",ubp="string",ua="[string, string]",unc="string",unp="string",upc="string",un="string",upp="string",uso=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/container.html



-----------------------------------------

container is undoable, queryable, and editable.

This command can be used to create and query container nodes. It is also used
to perform operations on containers such as:

  * add and remove nodes from the container
  * publish attributes from nodes inside the container
  * replace the connections and values from one container onto another one
  * remove a container without removing its member nodes


-----------------------------------------


Return Value:

string  Name of the node created.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

an    : addNode         [string[]] ['edit']
    Specifies the list of nodes to add to container.

-----------------------------------------

a     : asset           [string[]] ['query']
    When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.

-----------------------------------------

am    : assetMember     [string] ['query']
    Can be used during query in conjunction with the bindAttr flag to query for the only published attributes related to the specified node within the container.  In query mode, this flag needs a value.

-----------------------------------------

ba    : bindAttr        [[string, string]] ['query', 'edit']
    Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName, -publishAsParent, and -publishAsChild flags.

-----------------------------------------

cl    : connectionList  [boolean] ['query']
    Returns a list of the exterior connections to the container node.

-----------------------------------------

c     : current         [boolean] ['query', 'edit']
    In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.

-----------------------------------------

fn    : fileName        [string[]] ['query']
    Used to query for the assets associated with a given file name.  In query mode, this flag needs a value.

-----------------------------------------

fc    : findContainer   [string[]] ['query']
    When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string.  In query mode, this flag needs a value.

-----------------------------------------

f     : force           [boolean] ['edit']
    This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will be removed from all containers, instead of remaining in the parent container if being removed from a nested container.

-----------------------------------------

iha   : includeHierarchyAbove [boolean] ['edit']
    Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.

-----------------------------------------

ihb   : includeHierarchyBelow [boolean] ['edit']
    Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.

-----------------------------------------

inc   : includeNetwork  [boolean] ['edit']
    Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.

-----------------------------------------

ind   : includeNetworkDetails [string] ['edit']
    Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even when constraints are not specified as an input.

-----------------------------------------

isd   : includeShaders  [boolean] ['edit']
    Used to specify that for any shapes included, their shaders will also be included in the container.

-----------------------------------------

ish   : includeShapes   [boolean] ['edit']
    Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all other descendents will automatically be included.

-----------------------------------------

it    : includeTransform [boolean] ['edit']
    Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its parents will automatically be included.

-----------------------------------------

isc   : isContainer     [boolean] ['query']
    Return true if the selected or specified node is a container node. If multiple containers are queried, only the state of the first will be returned.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created container.

-----------------------------------------

nl    : nodeList        [boolean] ['query']
    When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container. This will also display any reordering done with the reorderContainer command.

-----------------------------------------

nnp   : nodeNamePrefix  [boolean] ['edit']
    Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.

-----------------------------------------

par   : parentContainer [boolean] ['query']
    Flag to query the parent container of a specified container.

-----------------------------------------

p     : preview         [boolean] []
    This flag is valid in create mode only. It indicates that you do not want the container to be created, instead you want to preview its contents. When this flag is used, Maya will select the nodes that would be put in the container if you did create the container. For example you can see what would go into the container with -includeNetwork, then modify your selection as desired, and do a create container with the selected objects only.

-----------------------------------------

pb    : publishAndBind  [[string, string]] ['edit']
    Publish the given name and bind the attribute to the given name. First string specifies the node and attribute name in "node.attr" format. Second string specifies the name it should be published with.

-----------------------------------------

pac   : publishAsChild  [[string, string]] ['query', 'edit']
    Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.

-----------------------------------------

pap   : publishAsParent [[string, string]] ['query', 'edit']
    Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.

-----------------------------------------

pro   : publishAsRoot   [[string, boolean]] ['query', 'edit']
    Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been published as root.

-----------------------------------------

pa    : publishAttr     [string] ['query']
    In query mode, can only be used with the -publishName(-pn) flag, and takes an attribute as an argument; returns the published name of the attribute, if any.  In query mode, this flag needs a value.

-----------------------------------------

pc    : publishConnections [boolean] ['edit']
    Publish all connections from nodes inside the container to nodes outside the container.

-----------------------------------------

pn    : publishName     [string] ['query', 'edit']
    Publish a name to the interface of the container, and returns the actual name published to the interface. In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an attribute argument in the "node.attr" format, returns the published name for that attribute, if any.

-----------------------------------------

rc    : removeContainer [boolean] ['edit']
    Disconnects all the nodes from container and deletes container node.

-----------------------------------------

rn    : removeNode      [string[]] ['edit']
    Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.

-----------------------------------------

typ   : type            [string] ['query']
    By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".

-----------------------------------------

ubp   : unbindAndUnpublish [string] ['edit']
    Unbind the given attribute (in "node.attr" format) and unpublish its associated name. Unbinding a compound may trigger unbinds of its compound parents/children. So the advantage of using this one flag is that it will automatically unpublish the names associated with these automatic unbinds.

-----------------------------------------

ua    : unbindAttr      [[string, string]] ['query', 'edit']
    Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.

-----------------------------------------

unc   : unbindChild     [string] ['edit']
    Unbind the node published as child, but do not remove its published name from the interface of the container.

-----------------------------------------

unp   : unbindParent    [string] ['edit']
    Unbind the node published as parent, but do not remove its published name from the interface of the container.

-----------------------------------------

upc   : unpublishChild  [string] ['edit']
    Unpublish node published as child from the interface of the container

-----------------------------------------

un    : unpublishName   [string] ['edit']
    Unpublish an unbound name from the interface of the container.

-----------------------------------------

upp   : unpublishParent [string] ['edit']
    Unpublish node published as parent from the interface of the container

-----------------------------------------

uso   : unsortedOrder   [boolean]
    This flag has no effect on the operation of the container command (OBSOLETE).

    """

def containerBind(q=1,e=1,all=1,bs="string",bsc=1,bsl=1,f=1,p=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/containerBind.html



-----------------------------------------

containerBind is undoable, queryable, and editable.

This is an accessory command to the container command which is used for some
automated binding operations on the container. A container's published
interface can be bound using a bindingSet on the associated container
template.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : allNames        [boolean] []
    Specifies that all published names on the container should be considered during the binding operation. By default only unbound published names will be operated on. Additionally specifying the 'force' option with 'all' will cause all previously bound published names to be reset (or unbound) before the binding operation is performed; in the event that there is no appropriate binding found for the published name, it will be left in the unbound state.

-----------------------------------------

bs    : bindingSet      [string] ['query']
    Specifies the name of the template binding set to use for the bind or query operation. This flag is not available in query mode.  In query mode, this flag needs a value.

-----------------------------------------

bsc   : bindingSetConditions [boolean] ['query']
    Used in query mode, returns a list of binding set condition entries from the specified template binding set. The list returned is composed of of all published name / condition string pairs for each entry in the binding set. This flag returns all entries in the associated binding set and does not take into account the validity of each entry with respect to the container's list of published names, bound or unbound state, etc.

-----------------------------------------

bsl   : bindingSetList  [boolean] ['query', 'edit']
    Used in query mode, returns a list of available binding sets that are defined on the associated container template.

-----------------------------------------

f     : force           [boolean] []
    This flag is used to force certain operations to proceed that would normally not be performed.

-----------------------------------------

p     : preview         [boolean]
    This flag will provide a preview of the results of a binding operation but will not actually perform it. A list of publishedName/boundName pairs are returned for each published name that would be affected by the binding action. If the binding of a published name will not change as a result of the action it will not be listed. Published names that were bound but will become unbound are also listed, in this case the associated boundName will be indicated by an empty string.

    """

def containerProxy(q=1,e=1,ft="string",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/containerProxy.html



-----------------------------------------

containerProxy is undoable, queryable, and editable.

Creates a new container with the same published interface, dynamic attributes
and attribute values as the specified container but with fewer container
members. This proxy container can be used as a reference proxy so that values
can be set on container attributes without loading in the full container. The
proxy container will contain one or more locator nodes. The first locator has
dynamic attributes that serve as stand-ins for the original published
attributes. The remaining locators serve as stand-ins for any dag nodes that
have been published as parent or as child and will be placed at the world
space location of the published parent/child nodes. The expected usage of
container proxies is to serve as a reference proxy for a referenced container.
For automated creation, export and setup of the proxy see the
doExportContainerProxy.mel script which is invoked by the "Export Container
Proxy" menu item.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ft    : fromTemplate    [string] []
    Specifies the name of a template file which will be used to create the new container proxy. Stand-in attributes will be created and published for all the numeric attributes on the proxy.

-----------------------------------------

typ   : type            [string]
    Specifies the type of container node to use for the proxy. This flag is only valid in conjunction with the fromTemplate flag. When creating a proxy for an existing container, the type created will always be identical to that of the source container. The default value for this flag is 'container'.

    """

def containerPublish(q=1,e=1,bn="[string, string]",bts=1,ic=1,ms=1,oc=1,pn="[string, string]",ubn="string",upn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/containerPublish.html



-----------------------------------------

containerPublish is undoable, queryable, and editable.

This is an accessory command to the container command which is used for some
advanced publishing operations on the container. For example, the
"publishConnections" flag on the container will publish all the connections,
but this command can be used to publish just the inputs, outputs, or to
collapse the shared inputs into a single attribute before publishing.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bn    : bindNode        [[string, string]] ['query', 'edit']
    Bind the specified node to the published node name.

-----------------------------------------

bts   : bindTemplateStandins [boolean] ['query', 'edit']
    This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.

-----------------------------------------

ic    : inConnections   [boolean] []
    Specifies that the unpublished connections to nodes in the container from external nodes should be published.

-----------------------------------------

ms    : mergeShared     [boolean] []
    For use with the inConnections flag. Indicates that when an external attribute connects to multiple internal attributes within the container, a single published attribute should be used to correspond to all of the internal attributes.

-----------------------------------------

oc    : outConnections  [boolean] []
    Specifies that the unpublished connections from nodes in the container to external nodes should be published.

-----------------------------------------

pn    : publishNode     [[string, string]] ['query', 'edit']
    Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.

-----------------------------------------

ubn   : unbindNode      [string] ['query', 'edit']
    Unbind the node that is published with the name specified by the flag.

-----------------------------------------

upn   : unpublishNode   [string]
    Unpublish the specified published node name.

    """

def containerTemplate(q=1,e=1,abs="string",an=1,av="string",ak=1,at="string",al="string",bn="string",bsl="string",can=1,d=1,ec=1,fc="string",fs=1,lm="int",mn="string",pan=1,pnl="string",rbs="string",rv="string",rtn=1,s=1,sp="string",tl="string",ubs="string",uh=1,ex=1,fn="string",f=1,l=1,mf="string",si=1,u=1,vl="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/containerTemplate.html



-----------------------------------------

containerTemplate is NOT undoable, queryable, and editable.

A container template is a description of a container's published interface.
This command provides the ability to create and save a template file for a
container or load an existing template file. Once a template exists, the user
can query the template information.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

abs   : addBindingSet   [string] ['edit']
    This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.

-----------------------------------------

an    : addNames        [boolean] ['edit']
    In edit mode, when used with the fromContainer flag, any published name on the container not present as an attribute on the template will be added to the template.

-----------------------------------------

av    : addView         [string] ['edit']
    This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created. The layoutMode flag provides more layout options. The template must be saved before the new view is permanently stored with the template file.

-----------------------------------------

ak    : allKeyable      [boolean] ['edit']
    Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.

-----------------------------------------

at    : attribute       [string] ['edit']
    If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.

-----------------------------------------

al    : attributeList   [string] ['query', 'edit']
    Used in query mode, returns a list of attributes contained in the template definition.

-----------------------------------------

bn    : baseName        [string] ['query']
    Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.

-----------------------------------------

bsl   : bindingSetList  [string] ['query']
    Used in query mode, returns a list of all binding sets defined on the template.

-----------------------------------------

can   : childAnchor     [boolean] ['query']
    This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.

-----------------------------------------

d     : delete          [boolean] []
    Delete the specified template and its file. All objects that are associated with this template or contained in the same template file will be deleted. To simply unload a template without permanently deleting its file, use unload instead.

-----------------------------------------

ec    : expandCompounds [boolean] ['edit']
    This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only used in the situation where both parent and child attributes are published to the container. The default value is false.

-----------------------------------------

fc    : fromContainer   [string] []
    This argument is used in create or edit mode to specify a container node to be used for generating the template contents. In template creation mode, the template definition will be created based on the list of published attributes in the specified container. In edit mode, when used with the addNames flag or with no other flag, any published name on the container not present as an attribute on the template will be added to the template. This flag is also used in conjunction with flags such as addView.

-----------------------------------------

fs    : fromSelection   [boolean] ['edit']
    If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the attributes specified with the attribute flag.

-----------------------------------------

lm    : layoutMode      [int] []
    This argument is used to specify the layout mode when creating a view. Values correspond as follows: 0: layout in flat list (default when not creating view from container) 1: layout grouped by node (default if creating view from container) The fromContainer or fromSelection argument is required to provide the reference container or selection for layout modes that require node information. Note that views can only refer to defined template attributes. This means that when using the fromContainer or from Selection flag to add a view to an existing template, only attributes that are defined on both the template and the container or the current selection will be included in the view (i.e. published attributes on the container that are not defined in the template will be ignored).

-----------------------------------------

mn    : matchName       [string] ['query']
    Used in query mode in conjunction with other flags this flag specifies an optional template name that is to be matched as part of the query operation. The base template name is used for matching, any template with the same basename will be matched even across different packages.  In query mode, this flag needs a value.

-----------------------------------------

pan   : parentAnchor    [boolean] ['query']
    This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.

-----------------------------------------

pnl   : publishedNodeList [string] ['query', 'edit']
    Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.

-----------------------------------------

rbs   : removeBindingSet [string] ['edit']
    This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.

-----------------------------------------

rv    : removeView      [string] ['edit']
    This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.

-----------------------------------------

rtn   : rootTransform   [boolean] ['query']
    This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.

-----------------------------------------

s     : save            [boolean] []
    Save the specified template to a file. If a filename is specified for the template, the entire file (and all templates associated with it) will be saved. If no file name is specified, a default filename will be assumed, based on the template name.

-----------------------------------------

sp    : searchPath      [string] ['query', 'edit']
    The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should conform to a path list format expected on the current platform. This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.

-----------------------------------------

tl    : templateList    [string] ['query']
    Used in query mode, returns a list of all loaded templates. This query can be used with optional matchFile and matchName flags. When used with the matchFile flag, the list of templates will be restricted to those associated with the specified file. When used with the matchName flag, the list of templates will be restricted to those matching the specified template name.

-----------------------------------------

ubs   : updateBindingSet [string] ['edit']
    This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as- is. When used without a reference container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.

-----------------------------------------

uh    : useHierarchy    [boolean] ['edit']
    If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.

-----------------------------------------

ex    : exists          [boolean] ['query']
    Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.

-----------------------------------------

fn    : fileName        [string] ['query']
    Specifies the filename associated with the template. This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used. It is recommended but not required that the filename and template name correspond.

-----------------------------------------

f     : force           [boolean] []
    This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file. When used in create mode, it will allow an existing template to be recreated (for example when using fromContainer argument to regenerate a template).

-----------------------------------------

l     : load            [boolean] []
    Load an existing template from a file. If a filename is specified for the template, the entire file (and all templates in it) will be loaded. If no file is specified, a default filename will be assumed, based on the template name.

-----------------------------------------

mf    : matchFile       [string] ['query']
    Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.  In query mode, this flag needs a value.

-----------------------------------------

si    : silent          [boolean] ['query', 'edit']
    Silent mode will suppress any error or warning messages that would normally be reported from the command execution. The return values are unaffected.

-----------------------------------------

u     : unload          [boolean] []
    Unload the specified template. This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.

-----------------------------------------

vl    : viewList        [string]
    Used in query mode, returns a list of all views defined on the template.

    """

def containerView(q=1,e=1,ii="string",il=1,vd=1,vb=1,vl=1,vn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/containerView.html



-----------------------------------------

containerView is NOT undoable, queryable, and editable.

A container view defines the layout information for the published attributes
of a particular container. Container views can be selected from a set of
built-in views or may be defined on an associated container template. This
command queries the view-related information for a container node. The
information returned from this command will be based on the view-related
settings in force on the container node at the time of the query (i.e. the
container's view mode, template name, view name attributes).


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ii    : itemInfo        [string] ['query']
    Used in query mode in conjunction with the itemList flag. The command will return a list of information for each item in the view, the information fields returned for each item are determined by this argument value. The information fields will be listed in the string array returned. The order in which the keyword is specified will determine the order in which the data will be returned by the command. One or more of the following keywords, separated by colons ':' are used to specify the argument value.    * itemIndex : sequential item number (0-based)   * itemName : item name (string)   * itemLabel : item display label (string)   * itemDescription : item description field (string)   * itemLevel : item hierarchy level (0-n)   * itemIsGroup : (boolean 0 or 1) indicates whether or not this item is a group   * itemIsAttribute : (boolean 0 or 1) indicates whether or not this item is an attribute   * itemNumChildren: number of immediate children (groups or attributes) of this item   * itemAttrType : item attribute type (string)   * itemCallback : item callback field (string)  In query mode, this flag needs a value.

-----------------------------------------

il    : itemList        [boolean] ['query']
    Used in query mode, the command will return a list of information for each item in the view. The viewName flag is used to select the view to query. The information returned about each item is determined by the itemInfo argument value. For efficiency, it is best to query all necessary item information at one time (to avoid recomputing the view information on each call).

-----------------------------------------

vd    : viewDescription [boolean] ['query']
    Used in query mode, returns the description field associated with the selected view. If no description was defined for this view, the value will be empty.

-----------------------------------------

vb    : viewLabel       [boolean] ['query']
    Used in query mode, returns the display label associated with the view. An appropriate label suitable for the user interface will be returned based on the selected view. Use of the view label is usually more suitable than the view name for display purposes.

-----------------------------------------

vl    : viewList        [boolean] ['query']
    Used in query mode, command will return a list of all views defined for the given target (container or template).

-----------------------------------------

vn    : viewName        [string]
    Used in query mode, specifies the name of the queried view when used in conjunction with a template target. When used in conjunction with a container target, it requires no string argument, and returns the name of the currently active view associated with the container; this value may be empty if the current view is not a valid template view or is generated by one of the built- in views modes. For this reason, the view label is generally more suitable for display purposes.  In query mode, this flag can accept a value.

    """

def createDisplayLayer(empty=1,mc=1,n="string",nr=1,num="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/createDisplayLayer.html



-----------------------------------------

createDisplayLayer is undoable, NOT queryable, and NOT editable.

Create a new display layer. The display layer number will be assigned based on
the first unassigned number not less than the base index number found in the
display layer global parameters. Normally all objects and their descendants
will be added to the new display layer but if the '-nr' flag is specified then
only the objects themselves will be added.


-----------------------------------------


Return Value:

string  Name of display layer node that was created


-----------------------------------------


Flags:

-----------------------------------------

e     : empty           [boolean] []
    If set then create an empty display layer. ie. Do not add the selected items to the new display layer.

-----------------------------------------

mc    : makeCurrent     [boolean] []
    If set then make the new display layer the current one.

-----------------------------------------

n     : name            [string] []
    Name of the new display layer being created.

-----------------------------------------

nr    : noRecurse       [boolean] []
    If set then only add selected objects to the display layer. Otherwise all descendants of the selected objects will also be added.

-----------------------------------------

num   : number          [int]
    Number for the new display layer being created.

    """

def delete(all=1,at="string",c=1,cn=1,ch=1,cp=1,expressions=1,hi="string",icn=1,mp=1,s=1,sc=1,tac=1,uac=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/delete.html



-----------------------------------------

delete is undoable, NOT queryable, and NOT editable.

This command is used to delete selected objects, or all objects, or objects
specified along with the command. Flags are available to filter the type of
objects that the command acts on.

At times, more than just specified items will be deleted. For example,
deleting two CVs in the same "row" on a NURBS surface will delete the whole
row.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

all   : all             [boolean] []
    Remove all objects of specified kind, in the scene. This flag is to be used in conjunction with the following flags.

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

c     : channels        [boolean] []
    Remove animation channels in the scene. Either all channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.

-----------------------------------------

cn    : constraints     [boolean] []
    Remove selected constraints and constraints attached to the selected nodes, or remove all constraints in the scene.

-----------------------------------------

ch    : constructionHistory [boolean] []
    Remove the construction history on the objects specified or selected.

-----------------------------------------

cp    : controlPoints   [boolean] []
    This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

e     : expressions     [boolean] []
    Remove expressions in the scene. Either all expressions can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.

-----------------------------------------

hi    : hierarchy       [string] []
    Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

icn   : inputConnectionsAndNodes [boolean] []
    Break input connection to specified attribute and delete all unconnected nodes that are left behind. The graph will be traversed until a node that cannot be deleted is encountered.

-----------------------------------------

mp    : motionPaths     [boolean] []
    Remove motion paths in the scene. Either all motion paths can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

sc    : staticChannels  [boolean] []
    Remove static animation channels in the scene. Either all static channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.

-----------------------------------------

tac   : timeAnimationCurves [boolean] []
    Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to time-input animation curves (for instance, those created by 'setKeyframe' will be deleted. When false, no time-input animation curves will be deleted. Default: true.

-----------------------------------------

uac   : unitlessAnimationCurves [boolean]
    Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to unitless-input animation curves (for instance, those created by 'setDrivenKeyframe' will be deleted. When false, no unitless-input animation curves will be deleted. Default: true.

    """

def distanceDimension(ep="[linear, linear, linear]",sp="[linear, linear, linear]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/distanceDimension.html



-----------------------------------------

distanceDimension is undoable, NOT queryable, and NOT editable.

This command is used to create a distance dimension to display the distance
between two specified points.


-----------------------------------------


Return Value:

string  \- the shape name of the DAG node created.


-----------------------------------------


Flags:

-----------------------------------------

ep    : endPoint        [[linear, linear, linear]] []
    Specifies the point to measure distance to, from the startPoint.

-----------------------------------------

sp    : startPoint      [[linear, linear, linear]]
    Specifies the point to start measuring distance from.

    """

def duplicate(ic=1,ilf=1,n="string",po=1,rc=1,rr=1,st=1,to=1,un=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/duplicate.html



-----------------------------------------

duplicate is undoable, NOT queryable, and NOT editable.

This command duplicates the given objects. If no objects are given, then the
selected list is duplicated.

The smart transform feature allows duplicate to transform newly duplicated
objects based on previous transformations between duplications.

Example: Duplicate an object and move it to a new location. Duplicate it again
with the smart duplicate flag. It should have moved once again the distance
you had previously moved it.

Note: changing the selected list between smart duplications will cause the
transform information to be deleted

The upstream Nodes option forces duplication of all upstream nodes leading
upto the selected objects.. Upstream nodes are defined as all nodes feeding
into selected nodes. During traversal of Dependency graph, if another
dagObject is encountered, then that node and all it's parent transforms are
also duplicated.

The inputConnections option forces the duplication of input connections to the
nodes that are to be duplicated. This is very useful especially in cases where
two nodes that are connected to each other are specified as nodes to be
duplicated. In that situation, the connection between the nodes is also
duplicated.

See also: instance


-----------------------------------------


Return Value:

string[]  : names of the objects created


-----------------------------------------


Flags:

-----------------------------------------

ic    : inputConnections [boolean] []
    Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the nodes at the input side are not duplicated (unlike the -un option).

-----------------------------------------

ilf   : instanceLeaf    [boolean] []
    instead of duplicating leaf DAG nodes, instance them.

-----------------------------------------

n     : name            [string] []
    name to give duplicated object(s)

-----------------------------------------

po    : parentOnly      [boolean] []
    Duplicate only the specified DAG node and not any of its children.

-----------------------------------------

rc    : renameChildren  [boolean] []
    rename the child nodes of the hierarchy, to make them unique.

-----------------------------------------

rr    : returnRootsOnly [boolean] []
    return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted in the result. This flag controls only what is returned in the output string[], and it does NOT change the behaviour of the duplicate command.

-----------------------------------------

st    : smartTransform  [boolean] []
    remembers last transformation and applies it to duplicated object(s)

-----------------------------------------

to    : transformsOnly  [boolean] []
    Duplicate only transform nodes and not any shapes.

-----------------------------------------

un    : upstreamNodes   [boolean]
    the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.

    """

def editDisplayLayerGlobals(q=1,bi="int",cdl="name",mt="int",uc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/editDisplayLayerGlobals.html



-----------------------------------------

editDisplayLayerGlobals is undoable, queryable, and NOT editable.

Edit the parameter values common to all display layers. Some of these
paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
currentDisplayLayer, are stored in the file.


-----------------------------------------


Return Value:

boolean  Command success    
string  Current display layer name, when querying  
int  Merge type, when querying  
int  Base ID, when querying  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bi    : baseId          [int] ['query']
    Set base layer ID. This is the number at which new layers start searching for a unique ID.

-----------------------------------------

cdl   : currentDisplayLayer [name] ['query']
    Set current display layer; ie. the one that all new objects are added to.

-----------------------------------------

mt    : mergeType       [int] ['query']
    Set file import merge type. Valid values are 0, none, 1, by number, and 2, by name.

-----------------------------------------

uc    : useCurrent      [boolean]
    Set whether or not to enable usage of the current display layer as the destination for all new nodes.

    """

def editDisplayLayerMembers(q=1,fn=1,nr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/editDisplayLayerMembers.html



-----------------------------------------

editDisplayLayerMembers is undoable, queryable, and NOT editable.

This command is used to query and edit membership of display layers. No
equivalent 'remove' command is necessary since all objects must be in exactly
one display layer. Removing an object from a layer can be accomplished by
adding it to a different layer.


-----------------------------------------


Return Value:

int  Number of objects added to the layer    
string[]  Query: List of objects in layer  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

fn    : fullNames       [boolean] ['query']
    (Query only.) If set then return the full DAG paths of the objects in the layer. Otherwise return just the name of the object.

-----------------------------------------

nr    : noRecurse       [boolean]
    If set then only add selected objects to the display layer. Otherwise all descendants of the selected objects will also be added.

    """

def exactWorldBoundingBox(ce=1,ii=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/exactWorldBoundingBox.html



-----------------------------------------

exactWorldBoundingBox is undoable, NOT queryable, and NOT editable.

This command figures out an exact-fit bounding box for the specified objects
(or selected objects if none are specified) This bounding box is always in
world space.


-----------------------------------------


Return Value:

float[]  xmin, ymin, zmin, xmax, ymax, zmax.


-----------------------------------------


Flags:

-----------------------------------------

ce    : calculateExactly [boolean] []
    Should the bounding box calculation be exact?

-----------------------------------------

ii    : ignoreInvisible [boolean]
    Should the bounding box calculation include or exclude invisible objects?

    """

def group(a=1,em=1,n="string",p="string",r=1,uag="string",w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/group.html



-----------------------------------------

group is undoable, NOT queryable, and NOT editable.

This command groups the specified objects under a new group and returns the
name of the new group.

If the -em flag is specified, then an empty group (with no objects) is
created.

If the -w flag is specified then the new group is placed under the world,
otherwise if -p is specified it is placed under the specified node. If neither
-w or -p is specified the new group is placed under the lowest common group
they have in common. (or the world if no such group exists)

If an object is grouped with another object that has the same name then one of
the objects will be renamed by this command.


-----------------------------------------


Return Value:

string  \- name of the group node


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]

-----------------------------------------

em    : empty           [boolean] []
    create an empty group (with no objects in it)

-----------------------------------------

n     : name            [string] []
    Assign given name to new group node.

-----------------------------------------

p     : parent          [string] []
    put the new group under the given parent

-----------------------------------------

r     : relative        [boolean] []
    preserve existing local object transformations (relative to the new group node)

-----------------------------------------

uag   : useAsGroup      [string] []
    Use the specified node as the group node. The specified node must be derived from the transform node and must not have any existing parents or children.

-----------------------------------------

w     : world           [boolean]
    put the new group under the world

    """

def instance(lf=1,n="string",st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/instance.html



-----------------------------------------

instance is undoable, NOT queryable, and NOT editable.

Instancing is a way of making the same object appear twice in the scene. This
is accomplished by creation of a new transform node that points to an
exisiting object. Changes to the transform are independent but changes to the
"instanced" object affect all instances since the node is shared.

If no objects are given, then the selected list is instanced. When an object
is instanced a new transform node is created that points to the selected
object.

The smart transform feature allows instance to transform newly instanced
objects based on previous transformations between instances.

Example: Instance an object and move it to a new location. Instance it again
with the smart transform flag. It should have moved once again the distance
you had previously moved it.

Note: changing the selected list between smart instances will cause the
transform information to be deleted.

It returns a list of the new objects created by the instance operation.

See also: duplicate


-----------------------------------------


Return Value:

string  \- the name of the new transform node is returned.


-----------------------------------------


Flags:

-----------------------------------------

lf    : leaf            [boolean] []
    Instances leaf-level objects. Acts like duplicate except leaf-level objects are instanced.

-----------------------------------------

n     : name            [string] []
    Name to give new instance

-----------------------------------------

st    : smartTransform  [boolean]
    Transforms instances item based on movements between transforms

    """

def instanceable(q=1,a=1,r=1,s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/instanceable.html



-----------------------------------------

instanceable is undoable, queryable, and NOT editable.

Flags one or more DAG nodes so that they can (or cannot) be instanced. This
command sets an internal state on the specified DAG nodes which is checked
whenever Maya attempts an instancing operation. If no node names are provided
on the command line then the current selection list is used.

Sets are automatically expanded to their constituent objects. Nodes which are
already instanced (or have children which are already instanced) cannot be
marked as non-instancable.


-----------------------------------------


Return Value:

boolean[]  For query execution.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : allow           [boolean] ['query']
    Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).

-----------------------------------------

r     : recursive       [boolean] []
    Can be specified with the -allow flag in create or edit mode to recursively apply the -allow setting to all non-shape children of the selected node(s). To also affect shapes, also specify the -shape flag along with -recursive.

-----------------------------------------

s     : shape           [boolean]
    Can be specified with the -allow flag in create or edit mode to apply the -allow setting to all shape children of the selected node(s). This flag can be specified in conjunction with the -recursive flag.

    """

def instancer(q=1,e=1,a=1,c="string",cs="float",csu="string",i="int",lod="string",n="string",obj="string",op="string",objectRotation="string",os="string",pds=1,rm=1,ro="string",ru="string",vn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/instancer.html



-----------------------------------------

instancer is undoable, queryable, and editable.

This command is used to create a instancer node and set the proper attributes
in the node.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : addObject       [boolean] ['edit']
    This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.

-----------------------------------------

c     : cycle           [string] ['query', 'edit']
    This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential". The default is "none".

-----------------------------------------

cs    : cycleStep       [float] ['query', 'edit']
    This flag sets or queries the cycle step attribute for the instancer node. This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).

-----------------------------------------

csu   : cycleStepUnits  [string] ['query', 'edit']
    This flag sets or queries the cycle step unit attribute for the instancer node. The options are "frames" or "seconds". The default is "frames".

-----------------------------------------

i     : index           [int] ['query']
    This flag is used to query the name of the ith instanced object.

-----------------------------------------

lod   : levelOfDetail   [string] ['query', 'edit']
    This flag sets or queries the level of detail of the instanced objects. The options are "geometry", "boundingBox", "boundingBoxes". The default is "geometry".

-----------------------------------------

n     : name            [string] ['query']
    This flag sets or queries the name of the instancer node.

-----------------------------------------

obj   : object          [string] ['query', 'edit']
    This flag indicates which objects will be add/removed from the list of instanced objects. The flag is used in conjuction with the -add and -remove flags. If neither of these flags is specified on the command line then -add is assumed.

-----------------------------------------

op    : objectPosition  [string] ['query']
    This flag queries the given objects position. This object can be any instanced object or sub-object.

-----------------------------------------

objectRotation : objectRotation  [string] ['query']
    This flag queries the given objects rotation. This object can be any instanced object or sub-object.

-----------------------------------------

os    : objectScale     [string] ['query']
    This flag queries the given objects scale. This object can be any instanced object or sub-object.

-----------------------------------------

pds   : pointDataSource [boolean] ['query']
    This flag is used to query the source node supply the data for the input points.

-----------------------------------------

rm    : removeObject    [boolean] ['edit']
    This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.

-----------------------------------------

ro    : rotationOrder   [string] ['query', 'edit']
    This flag specifies the rotation order associated with the rotation flag. The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX. By default the attribute is XYZ.

-----------------------------------------

ru    : rotationUnits   [string] ['query', 'edit']
    This flag specifies the rotation units associated with the rotation flag. The options are degrees or radians. By default the attribute is degrees.

-----------------------------------------

vn    : valueName       [string]
    This flag is used to query the value(s) of the array associated with the given name. If the -index flag is used in conjuction with this flag then the ith value will be returned. Otherwise, the entire array will be returned.

    """

def license(b=1,i=1,ib=1,ie=1,it=1,lm=1,pc=1,r=1,sbi=1,spi=1,s=1,u=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/license.html



-----------------------------------------

license is undoable, NOT queryable, and NOT editable.

This command displays version information about the application if it is
executed without flags. If one of the above flags is specified then the
specified version information is returned.


-----------------------------------------


Return Value:

string  The application's license information.


-----------------------------------------


Flags:

-----------------------------------------

b     : borrow          [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

i     : info            [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

ib    : isBorrowed      [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

ie    : isExported      [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

it    : isTrial         [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

lm    : licenseMethod   [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

pc    : productChoice   [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

r     : r               [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

sbi   : showBorrowInfo  [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

spi   : showProductInfoDialog [boolean] []
    Show the Product Information Dialog

-----------------------------------------

s     : status          [boolean] []
    This flag is obsolete and no longer supported.

-----------------------------------------

u     : usage           [boolean]
    This flag is obsolete and no longer supported.

    """

def listNodesWithIncorrectNames():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listNodesWithIncorrectNames.html



-----------------------------------------

listNodesWithIncorrectNames is NOT undoable, NOT queryable, and NOT editable.

List all nodes with incorrect names in the Script Editor.


-----------------------------------------


Return Value:

None
    """

def listSets(allSets=1,ets=1,o="name",t="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listSets.html



-----------------------------------------

listSets is undoable, NOT queryable, and NOT editable.

The listSets command is used to get a list of all the sets an object belongs
to. To get sets of a specific type for an object use the type flag as well.

To get a list of all sets in the scene then don't use an object in the command
line but use one of the flags instead.


-----------------------------------------


Return Value:

string[]  (string array of all sets the object belongs to)


-----------------------------------------


Flags:

-----------------------------------------

allSets : allSets         [boolean] []
    Returns all sets in the scene.

-----------------------------------------

ets   : extendToShape   [boolean] []
    When requesting a transform's sets also walk down to the shape immediately below it for its sets.

-----------------------------------------

o     : object          [name] []
    Returns all sets which this object is a member of.

-----------------------------------------

t     : type            [uint]
    Returns all sets in the scene of the given type:    * 1 - all rendering sets   * 2 - all deformer sets

    """

def lockNode(q=1,ic=1,l=1,ln=1,lu=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lockNode.html



-----------------------------------------

lockNode is undoable, queryable, and NOT editable.

Locks or unlocks one or more dependency nodes. A locked node is restricted in
the following ways:

  * It may not be deleted.
  * It may not be renamed.
  * Its parenting may not be changed.
  * Attributes may not be added to or removed from it.
  * Locked attributes may not be unlocked.
  * Unlocked attributes may not be locked.

Note that an unlocked attribute of a locked node may still have its value set,
or connections to it made or broken. For more information on attribute
locking, see the setAttr command.

If no node names are specified then the current selection list is used.

There are a few special behaviors when locking containers. Containers are
automatically expanded to their constituent objects. When a container is
locked, members of the container may not be unlocked and the container
membership may not be modified. Containers may also be set to lock unpublished
attributes. When in this state, unpublished member attributes may not have
existing connections broken, new connections cannot be made, and values on
unconnected attributes may not be modified. Parenting is allowed to change on
members of locked containers that have been published as parent or child
anchors.


-----------------------------------------


Return Value:

boolean[]  For query execution.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ic    : ignoreComponents [boolean] ['query']
    Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.

-----------------------------------------

l     : lock            [boolean] ['query']
    Specifies the new lock state for the node. The default is true.

-----------------------------------------

ln    : lockName        [boolean] ['query']
    Specifies the new lock state for the node's name.

-----------------------------------------

lu    : lockUnpublished [boolean]
    Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non- containers, lock or unlock unpublished attributes on the specified node.

    """

def ls(an=1,ap=1,assemblies=1,ca=1,ct="string",con=1,dag=1,dn=1,dep=1,et="string",ext="string",fl=1,g=1,gh=1,hd="int",hl=1,io=1,iv=1,lf=1,lt=1,lv=1,ln=1,l=1,mat=1,mod=1,ni=1,nt=1,o=1,os=1,pr=1,pn=1,pl=1,psh=1,ro=1,r=1,rn=1,rf=1,rg=1,rq=1,rr=1,rs=1,sl=1,set=1,s=1,sn=1,sns=1,st=1,tl="int",tm=1,tex=1,tr=1,typ="string",ud=1,ut=1,uid=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ls.html



-----------------------------------------

ls is undoable, NOT queryable, and NOT editable.

The `ls` command returns the names (and optionally the type names) of objects
in the scene.

The most common use of `ls` is to filter or match objects based on their name
(using wildcards) or based on their type. By default `ls` will match any
object in the scene but it can also be used to filter or list the selected
objects when used in conjunction with the -selection flag.

If type names are requested, using the showType flag, they will be interleaved
with object names so the result will be pairs of <object, type> values.

Internal nodes (for example itemFilter nodes) are typically filtered so that
only scene objects are returned. However, using a wildcard will cause all the
nodes matching the wild card to show up, including internal nodes. For
example, `ls *` will list all nodes whether internal or not.

Use the syntax "::" to denote a recursive namespace search when listing nodes.
For example, `ls "::pSphere1"` would match objects named "pSphere1" in any
namespace, at any depth. `ls "ns::*"` would match any node in namespace "ns"
or children namespaces.

When Maya is in relativeNames mode, the `ls` command will return names
relative to the current namespace and `ls *` will list from the the current
namespace. For more details, please refer to the `-relativeNames` flag of the
`namespace` command.

The command may also be passed node UUIDs instead of names/paths, and can
return UUIDs instead of names via the -uuid flag.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

an    : absoluteName    [boolean] []
    This flag can be used in conjunction with the showNamespace flag to specify that the namespace(s) returned by the command be in absolute namespace format. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces. For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace modes.

-----------------------------------------

ap    : allPaths        [boolean] []
    List all paths to nodes in DAG. This flag only works if -dag is also specified or if an object name is supplied.

-----------------------------------------

assemblies : assemblies      [boolean] []
    List top level transform Dag objects

-----------------------------------------

ca    : cameras         [boolean] []
    List camera shapes.

-----------------------------------------

ct    : containerType   [string] []
    List containers with the specified user-defined type.   This flag cannot be used in conjunction with the type or exactType flag.

-----------------------------------------

con   : containers      [boolean] []
    List containers. Includes both standard containers as well as other types of containers such as dagContainers.

-----------------------------------------

dag   : dagObjects      [boolean] []
    List Dag objects of any type. If object name arguments are passed to the command then this flag will list all Dag objects below the specified object(s).

-----------------------------------------

dn    : defaultNodes    [boolean] []
    Returns default nodes. A default node is one that Maya creates automatically and does not get saved out with the scene, although some of its attribute values may.

-----------------------------------------

dep   : dependencyNodes [boolean] []
    List dependency nodes. (including Dag objects)

-----------------------------------------

et    : exactType       [string] []
    List all objects of the specified type, but not objects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.   This flag cannot be used in conjunction with the type or excludeType flag.

-----------------------------------------

ext   : excludeType     [string] []
    List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.   This flag cannot be used in conjunction with the type or exactType flag.

-----------------------------------------

fl    : flatten         [boolean] []
    Flattens the returned list of objects so that each component is identified individually.

-----------------------------------------

g     : geometry        [boolean] []
    List geometric Dag objects.

-----------------------------------------

gh    : ghost           [boolean] []
    List ghosting objects.

-----------------------------------------

hd    : head            [int] []
    This flag specifies the maximum number of elements to be returned from the beginning of the list of items. Note: each type flag will return at most this many items so if multiple type flags are specified then the number of items returned can be greater than this amount.

-----------------------------------------

hl    : hilite          [boolean] []
    List objects that are currently hilited for component selection.

-----------------------------------------

io    : intermediateObjects [boolean] []
    List only intermediate dag nodes.

-----------------------------------------

iv    : invisible       [boolean] []
    List only invisible dag nodes.

-----------------------------------------

lf    : leaf            [boolean] []
    List all leaf nodes in Dag. This flag is a modifier and must be used in conjunction with the -dag flag.

-----------------------------------------

lt    : lights          [boolean] []
    List light shapes.

-----------------------------------------

lv    : live            [boolean] []
    List objects that are currently live.

-----------------------------------------

ln    : lockedNodes     [boolean] []
    Returns locked nodes, which cannot be deleted or renamed. However, their status may change.

-----------------------------------------

l     : long            [boolean] []
    Return full path names for Dag objects. By default the shortest unique name is returned.

-----------------------------------------

mat   : materials       [boolean] []
    List materials or shading groups.

-----------------------------------------

mod   : modified        [boolean] []
    When this flag is set, only nodes modified since the last save will be returned.

-----------------------------------------

ni    : noIntermediate  [boolean] []
    List only non intermediate dag nodes.

-----------------------------------------

nt    : nodeTypes       [boolean] []
    Lists all registered node types.

-----------------------------------------

o     : objectsOnly     [boolean] []
    When this flag is set only object names will be returned and components/attributes will be ignored.

-----------------------------------------

os    : orderedSelection [boolean] []
    List objects and components that are currently selected in their order of selection. This flag depends on the value of the -tso/trackSelectionOrder flag of the selectPref command. If that flag is not enabled than this flag will return the same thing as the -sl/selection flag would.

-----------------------------------------

pr    : partitions      [boolean] []
    List partitions.

-----------------------------------------

pn    : persistentNodes [boolean] []
    Returns persistent nodes, which are nodes that stay in the Maya session after a file > new. These are a special class of default nodes that do not get reset on file > new. Ex: itemFilter and selectionListOperator nodes.

-----------------------------------------

pl    : planes          [boolean] []
    List construction plane shapes.

-----------------------------------------

psh   : preSelectHilite [boolean] []
    List components that are currently hilited for pre-selection.

-----------------------------------------

ro    : readOnly        [boolean] []
    Returns referenced nodes. Referenced nodes are read only. NOTE: Obsolete. Please use "-referencedNodes".

-----------------------------------------

r     : recursive       [boolean] []
    When set to true, this command will look for name matches in all namespaces. When set to false, this command will only look for matches in namespaces that are requested (e.g. by specifying a name containing the ':'... "ns1:pSphere1").

-----------------------------------------

rn    : referencedNodes [boolean] []
    Returns referenced nodes. Referenced nodes are read only.

-----------------------------------------

rf    : references      [boolean] []
    List references associated with files. Excludes special reference nodes such as the sharedReferenceNode and unknown reference nodes.

-----------------------------------------

rg    : renderGlobals   [boolean] []
    List render globals.

-----------------------------------------

rq    : renderQualities [boolean] []
    List named render qualities.

-----------------------------------------

rr    : renderResolutions [boolean] []
    List render resolutions.

-----------------------------------------

rs    : renderSetups    [boolean] []
    Alias for -renderGlobals.

-----------------------------------------

sl    : selection       [boolean] []
    List objects that are currently selected.

-----------------------------------------

set   : sets            [boolean] []
    List sets.

-----------------------------------------

s     : shapes          [boolean] []
    List shape objects.

-----------------------------------------

sn    : shortNames      [boolean] []
    Return short attribute names. By default long attribute names are returned.

-----------------------------------------

sns   : showNamespace   [boolean] []
    Show the namespace of each object after the object name.   This flag cannot be used in conjunction with the showType flag.

-----------------------------------------

st    : showType        [boolean] []
    List the type of each object after its name.

-----------------------------------------

tl    : tail            [int] []
    This flag specifies the maximum number of elements to be returned from the end of the list of items. Note: each type flag will return at most this many items so if multiple type flags are specified then the number of items returned can be greater than this amount

-----------------------------------------

tm    : templated       [boolean] []
    List only templated dag nodes.

-----------------------------------------

tex   : textures        [boolean] []
    List textures.

-----------------------------------------

tr    : transforms      [boolean] []
    List transform objects.

-----------------------------------------

typ   : type            [string] []
    List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a specific object/data type associated with them and will return "untyped" when listed with this flag.   This flag cannot be used in conjunction with the exactType or excludeType flag.

-----------------------------------------

ud    : undeletable     [boolean] []
    Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.

-----------------------------------------

ut    : untemplated     [boolean] []
    List only un-templated dag nodes.

-----------------------------------------

uid   : uuid            [boolean] []
    Return node UUIDs instead of names. Note that there are no "UUID paths" \- combining this flag with e.g. the -long flag will not result in a path formed of node UUIDs.

-----------------------------------------

v     : visible         [boolean]
    List only visible dag nodes.

    """

def makeIdentity(a=1,jo=1,n="uint",pn=1,r=1,s=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/makeIdentity.html



-----------------------------------------

makeIdentity is undoable, NOT queryable, and NOT editable.

The makeIdentity command is a quick way to reset the selected transform and
all of its children down to the shape level by the identity transformation.
You can also specify which of transform, rotate or scale is applied down from
the selected transform. The identity transformation means:

  * translate = 0, 0, 0
  * rotate = 0, 0, 0
  * scale = 1, 1, 1
  * shear = 1, 1, 1

If a transform is a joint, then the "translate" attribute may not be 0, but
will be used to position the joints so that they preserve their world space
positions. The translate flag doesn't apply to joints, since joints must
preserve their world space positions. Only the rotate and scale flags are
meaningful when applied to joints.

If the -a/apply flag is true, then the transforms that are reset are
accumulated and applied to the all shapes below the modified transforms, so
that the shapes will not move. The pivot positions are recalculated so that
they also will not move in world space. If this flag is false, then the
transformations are reset to identity, without any changes to preserve
position.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : apply           [boolean] []
    If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.

-----------------------------------------

jo    : jointOrient     [boolean] []
    If this flag is set, the joint orient on joints will be reset to align with worldspace.

-----------------------------------------

n     : normal          [uint] []
    If this flag is set to 1, the normals on polygonal objects will be frozen. This flag is valid only when the -apply flag is on. If this flag is set to 2, the normals on polygonal objects will be frozen only if its a non- rigid transformation matrix. ie, a transformation that does not contain shear, skew or non-proportional scaling. The default behaviour is not to freeze normals.

-----------------------------------------

pn    : preserveNormals [boolean] []
    If this flag is true, the normals on polygonal objects will be reversed if the objects are negatively scaled (reflection). This flag is valid only when the -apply flag is on.

-----------------------------------------

r     : rotate          [boolean] []
    If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.

-----------------------------------------

s     : scale           [boolean] []
    If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.

-----------------------------------------

t     : translate       [boolean]
    If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied. (Note: the translate flag is not meaningful when applied to joints, since joints are made to preserve their world space position. This flag will have no effect on joints.)

    """

def makeLive(n=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/makeLive.html



-----------------------------------------

makeLive is undoable, NOT queryable, and NOT editable.

This commmand makes an object live. A live object defines the surface on which
to create objects and to move object relative to. Only construction planes,
nurbs surfaces and polygon meshes can be made live.

The makeLive command expects one of these types of objects as an explicit
argument. If no argument is explicitly specified, then there are a number of
default behaviours based on what is currently active. The command will fail if
there is more than one object active or the active object is not one of the
valid types of objects. If there is nothing active, the current live object
will become dormant. Otherwise, the active object will become the live object.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

n     : none            [boolean]
    If the -n/none flag, the live object will become dormant. Use of this flag causes any arguments to be ignored.

    """

def makePaintable(q=1,ac=1,aca=1,aa="string",at="string",ca=1,rm=1,sm="string",ui="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/makePaintable.html



-----------------------------------------

makePaintable is NOT undoable, queryable, and NOT editable.

Make attributes of nodes paintable to Attribute Paint Tool. This command is
used to register new attributes to the Attribute Paint tool as paintable. Once
registered the attributes will be recognized by the Attribute Paint tool and
the user will be able to paint them.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : activate        [boolean] ['query']
    Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.

-----------------------------------------

aca   : activateAll     [boolean] ['query']
    Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.

-----------------------------------------

aa    : altAttribute    [string] ['query']
    Define an alternate attribute which will also receive the same values. There can be multiple such flags.

-----------------------------------------

at    : attrType        [string] ['query']
    Paintable attribute type. Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.

-----------------------------------------

ca    : clearAll        [boolean] ['query']
    Removes all paintable attribute definitions.

-----------------------------------------

rm    : remove          [boolean] ['query']
    Make the attribute not paintable any more.

-----------------------------------------

sm    : shapeMode       [string] ['query']
    This flag controls how Artisan correlates the paintable node to a corresponding shape node. It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present, only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.

-----------------------------------------

ui    : uiName          [string]
    UI name. Default is the attribute name.

    """

def matchTransform(piv=1,pos=1,rot=1,scl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/matchTransform.html



-----------------------------------------

matchTransform is undoable, NOT queryable, and NOT editable.

This command modifies the source object's transform to match the target
object's transform.

If no flags are specified then the command will match position, rotation and
scaling.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

piv   : pivots          [boolean] []
    Match the source object(s) scale/rotate pivot positions to the target transform's pivot.

-----------------------------------------

pos   : position        [boolean] []
    Match the source object(s) position to the target object.

-----------------------------------------

rot   : rotation        [boolean] []
    Match the source object(s) rotation to the target object.

-----------------------------------------

scl   : scale           [boolean]
    Match the source object(s) scale to the target transform.

    """

def move(a=1,co=1,cs=1,xn=1,dph=1,ls=1,x=1,xy=1,xyz=1,xz=1,y=1,yz=1,z=1,os=1,oj="string",p=1,pcp=1,pgp=1,puv=1,rfl=1,rab=1,rao=1,rax=1,ray=1,raz=1,rft="float",r=1,rpr=1,spr=1,sao="string",smn=1,ws=1,wd=1,xc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/move.html



-----------------------------------------

move is undoable, NOT queryable, and NOT editable.

The move command is used to change the positions of geometric objects.

The default behaviour, when no objects or flags are passed, is to do a
absolute move on each currently selected object in the world space. The value
of the coordinates are interpreted as being defined in the current linear unit
unless the unit is explicitly mentioned.

When using -objectSpace there are two ways to use this command. If numbers are
typed without units then the internal values of the object are set to these
values. If, on the other hand a unit is specified then the internal value is
set to the equivalent internal value that represents that world-space
distance.

The -localSpace flag moves the object in its parent space. In this space the
x,y,z values correspond directly to the tx, ty, tz channels on the object.

The -rotatePivotRelative/-scalePivotRelative flags can be used with the
-absolute flag to translate an object so that its pivot point ends up at the
given absolute position. These flags will be ignored if components are
specified.

The -worldSpaceDistance flag is a modifier flag that may be used in
conjunction with the -objectSpace/-localSpace flags. When this flag is
specified the command treats the x,y,z values as world space units so the
object will move the specified world space distance but it will move along the
axis specified by the -objectSpace/-localSpace flag. The default behaviour,
without this flag, is to treat the x,y,z values as units in object space or
local space. In other words, the worldspace distance moved will depend on the
transformations applied to the object unless this flag is specified.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    Perform an absolute operation.

-----------------------------------------

co    : componentOffset [boolean] []
    Move components individually in local space

-----------------------------------------

cs    : componentSpace  [boolean] []
    Move in local component space

-----------------------------------------

xn    : constrainAlongNormal [boolean] []
    When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.

-----------------------------------------

dph   : deletePriorHistory [boolean] []
    If true then delete the history prior to the current operation.

-----------------------------------------

ls    : localSpace      [boolean] []
    Move in local space

-----------------------------------------

x     : moveX           [boolean] []
    Move in X direction

-----------------------------------------

xy    : moveXY          [boolean] []
    Move in XY direction

-----------------------------------------

xyz   : moveXYZ         [boolean] []
    Move in all directions (default)

-----------------------------------------

xz    : moveXZ          [boolean] []
    Move in XZ direction

-----------------------------------------

y     : moveY           [boolean] []
    Move in Y direction

-----------------------------------------

yz    : moveYZ          [boolean] []
    Move in YZ direction

-----------------------------------------

z     : moveZ           [boolean] []
    Move in Z direction

-----------------------------------------

os    : objectSpace     [boolean] []
    Move in object space

-----------------------------------------

oj    : orientJoint     [string] []
    Default is xyz.

-----------------------------------------

p     : parameter       [boolean] []
    Move in parametric space

-----------------------------------------

pcp   : preserveChildPosition [boolean] []
    When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.

-----------------------------------------

pgp   : preserveGeometryPosition [boolean] []
    When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.

-----------------------------------------

puv   : preserveUV      [boolean] []
    When true, UV values on translated components are projected along the translation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.

-----------------------------------------

rfl   : reflection      [boolean] []
    To move the corresponding symmetric components also.

-----------------------------------------

rab   : reflectionAboutBBox [boolean] []
    Sets the position of the reflection axis at the geometry bounding box

-----------------------------------------

rao   : reflectionAboutOrigin [boolean] []
    Sets the position of the reflection axis at the origin

-----------------------------------------

rax   : reflectionAboutX [boolean] []
    Specifies the X=0 as reflection plane

-----------------------------------------

ray   : reflectionAboutY [boolean] []
    Specifies the Y=0 as reflection plane

-----------------------------------------

raz   : reflectionAboutZ [boolean] []
    Specifies the Z=0 as reflection plane

-----------------------------------------

rft   : reflectionTolerance [float] []
    Specifies the tolerance to findout the corresponding reflected components

-----------------------------------------

r     : relative        [boolean] []
    Perform a operation relative to the object's current position

-----------------------------------------

rpr   : rotatePivotRelative [boolean] []
    Move relative to the object's rotate pivot point.

-----------------------------------------

spr   : scalePivotRelative [boolean] []
    Move relative to the object's scale pivot point.

-----------------------------------------

sao   : secondaryAxisOrient [string] []
    Default is xyz.

-----------------------------------------

smn   : symNegative     [boolean] []
    When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.

-----------------------------------------

ws    : worldSpace      [boolean] []
    Move in world space

-----------------------------------------

wd    : worldSpaceDistance [boolean] []
    Move is specified in world space units

-----------------------------------------

xc    : xformConstraint [string]
    Apply a transform constraint to moving components.    * none - no constraint   * surface - constrain components to the surface   * edge - constrain components to surface edges   * live - constraint components to the live surface

    """

def paramDimension():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/paramDimension.html



-----------------------------------------

paramDimension is undoable, NOT queryable, and NOT editable.

This command is used to create a param dimension to display the parameter
value of a curve/surface at a specified point on the curve/surface.


-----------------------------------------


Return Value:

string  Name of the paramDimension shape node created
    """

def paramLocator(q=1,e=1,p=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/paramLocator.html



-----------------------------------------

paramLocator is undoable, queryable, and editable.

The command creates a locator in the underworld of a NURBS curve or NURBS
surface at the specified parameter value. If no object is specified, then a
locator will be created on the first valid selected item (either a curve point
or a surface point).


-----------------------------------------


Return Value:

string  Name for the new locator in the underworld of NURBS shape.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

p     : position        [boolean]
    Whether to set the locator position in normalized space.

    """

def parent(a=1,add=1,nc=1,nis=1,r=1,rm=1,s=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/parent.html



-----------------------------------------

parent is undoable, NOT queryable, and NOT editable.

This command parents (moves) objects under a new group, removes objects from
an existing group, or adds/removes parents.

If the -w flag is specified all the selected or specified objects are parented
to the world (unparented first).

If the -rm flag is specified then all the selected or specified instances are
removed.

If there are more than two objects specified all the objects are parented to
the last object specified.

If the -add flag is specified, the objects are not reparented but also become
children of the last object specified.

If there is only a single object specified then the selected objects are
parented to that object.

If an object is parented under a different group and there is an object in
that group with the same name then this command will rename the parented
object.


-----------------------------------------


Return Value:

string[]  Names of the objects parented (possibly renamed)


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]

-----------------------------------------

add   : addObject       [boolean] []
    preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.

-----------------------------------------

nc    : noConnections   [boolean] []
    The parent command will normally generate new instanced set connections when adding instances. (ie. make a connection to the shading engine for new instances) This flag suppresses this behaviour and is primarily used by the file format.

-----------------------------------------

nis   : noInvScale      [boolean] []
    The parent command will normally connect inverseScale to its parent scale on joints. This is used to compensate scale on joint. The connection of inverseScale will occur if both child and parent are joints and no connection is present on child's inverseScale. In case of a reparenting, the old inverseScale will only get broken if the old parent is a joint. Otherwise connection will remain intact. This flag suppresses this behaviour.

-----------------------------------------

r     : relative        [boolean] []
    preserve existing local object transformations (relative to the parent node)

-----------------------------------------

rm    : removeObject    [boolean] []
    Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the scene. Use -world to remove the world as a parent of the given object.

-----------------------------------------

s     : shape           [boolean] []
    The parent command usually only operates on transforms. Using this flags allows a shape that is specified to be directly parented under the given transform. This is used to instance a shape node. (ie. "parent -add -shape" is equivalent to the "instance" command). This flag is primarily used by the file format.

-----------------------------------------

w     : world           [boolean]
    unparent given object(s) (parent to world)

    """

def partition(q=1,e=1,add="name",n="string",rm="name",re=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/partition.html



-----------------------------------------

partition is undoable, queryable, and editable.

This command is used to create, query or add/remove sets to a partition. If a
partition name needs to be specified, it is the first argument, other
arguments represent the set names.

Without any flags, the command will create a partition with a default name.
Any sets which are arguments to the command will be added to the partition.

A set can be added to a partition only if none of its members are in any of
the other sets in the partition. If the -re/render flag is specified when the
partition is created, only 'renderable' sets can be added to the partition.

Sets can be added and removed from a partition by using the -addSet or
-removeSet flags.

Note: If a set is already selected, and the partition command is executed, the
set will be added to the created partition.


-----------------------------------------


Return Value:

string  Name of the partition that was created or edited    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addSet          [name] []
    Adds the list of sets to the named partition.

-----------------------------------------

n     : name            [string] []
    Assigns the given name to new partition. Valid only for create mode.

-----------------------------------------

rm    : removeSet       [name] []
    Removes the list of sets from the named partition.

-----------------------------------------

re    : render          [boolean]
    New partition can contain render sets. For use in creation mode only. Default is false. Can also be used with query flag - returns boolean.

    """

def performanceOptions(q=1,cr="float",ds="string",dtb="string",dt="string",lr="float",pbf="string",pbs="string",pc="string",pdm="string",pf="string",pl="string",pp="string",ps="string",pw="string",sht=1,ucr="string",ulr="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/performanceOptions.html



-----------------------------------------

performanceOptions is undoable, queryable, and NOT editable.

Sets the global performance options for the application. The options allow the
disabling of features such as stitch surfaces or deformers to cut down on
computation time in the scene.

Performance options that are in effect may be on all the time, or they can be
turned on only for interaction. In the latter case, the options will only take
effect during UI interaction or playback.

Note that none of these performance options will affect rendering.


-----------------------------------------


Return Value:

string  One of "on", "off", or "interactive" giving the state of the option    
float  Global resolution value  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cr    : clusterResolution [float] ['query']
    Sets the global cluster resolution. This value may range between 0.0 (exact calculation) and 10.0 (rough approximation)

-----------------------------------------

ds    : disableStitch   [string] ['query']
    Sets the state of stitch surface disablement. Setting this to "on" suppresses the generation of stitch surfaces. Valid values are "on", "off", "interactive".

-----------------------------------------

dtb   : disableTrimBoundaryDisplay [string] ['query']
    Sets the state of trim boundary drawing disablement. Setting this to "on" suppresses the drawing of surface trim boundaries. Valid values are "on", "off", "interactive".

-----------------------------------------

dt    : disableTrimDisplay [string] ['query']
    Sets the state of trim drawing disablement. Setting this to "on" suppresses the drawing of surface trims. Valid values are "on", "off", "interactive".

-----------------------------------------

lr    : latticeResolution [float] ['query']
    Sets the global lattice resolution. This value may range between 0.0 (exact calculation) and 1.0 (rough approximation)

-----------------------------------------

pbf   : passThroughBindSkinAndFlexors [string] ['query']
    Sets the state of bind skin and all flexors pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

pbs   : passThroughBlendShape [string] ['query']
    Sets the state of blend shape deformer pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

pc    : passThroughCluster [string] ['query']
    Sets the state of cluster deformer pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

pdm   : passThroughDeltaMush [string] ['query']
    Sets the state of delta mush deformer pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

pf    : passThroughFlexors [string] ['query']
    Sets the state of flexor pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

pl    : passThroughLattice [string] ['query']
    Sets the state of lattice deformer pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

pp    : passThroughPaintEffects [string] ['query']
    Sets the state of paint effects pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

ps    : passThroughSculpt [string] ['query']
    Sets the state of sculpt deformer pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

pw    : passThroughWire [string] ['query']
    Sets the state of wire deformer pass through. Valid values are "on", "off", "interactive".

-----------------------------------------

sht   : skipHierarchyTraversal [boolean] ['query']
    When enabled, hierarchy traversal of invisible objects in the scene will be disabled in order to increase performance however this has a side effect of performing redundant viewport refreshes on certain actions such as manipulations, start/end of playback, idle refresh calls, etc.

-----------------------------------------

ucr   : useClusterResolution [string] ['query']
    Sets the state of cluster deformer global resolution. This allows clusters to be calculated at a lower resolution. Valid values are "on", "off", "interactive".

-----------------------------------------

ulr   : useLatticeResolution [string]
    Sets the state of lattice deformer global resolution. This allows lattices to be calculated at a lower resolution. Valid values are "on", "off", "interactive".

    """

def pixelMove():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pixelMove.html



-----------------------------------------

pixelMove is undoable, NOT queryable, and NOT editable.

The pixelMove command moves objects by what appears as pixel units based on
the current view. It takes two integer arguments which specify the direction
in screen space an object should appear to move. The vector between the center
pixel of the view and the specified offset is mapped to some world space
vector which defines the relative amount to move the selected objects. The
mapping is dependent upon the view.


-----------------------------------------


Return Value:

None
    """

def quit(a=1,ec="uint",f=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/quit.html



-----------------------------------------

quit is undoable, NOT queryable, and NOT editable.

This command is used to exit the application.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : abort           [boolean] []
    Will quit without saving like -force, but will also prevent preferences/hotkeys/colors from being saved. Use at your own risk.

-----------------------------------------

ec    : exitCode        [uint] []
    Specifies the exit code to be returned once the application exits. The default exit code is 0.

-----------------------------------------

f     : force           [boolean]
    If specified, this flag will force a quit without saving or prompting for saving changes. Use at your own risk.

    """

def rename(ignoreShape=1,uid=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rename.html



-----------------------------------------

rename is undoable, NOT queryable, and NOT editable.

Renames the given object to have the new name. If only one argument is
supplied the command will rename the (first) selected object. If the new name
conflicts with an existing name, the object will be given a unique name based
on the supplied name. It is not legal to rename an object to the empty string.

When a transform is renamed then any shape nodes beneath the transform that
have the same prefix as the old transform name are renamed. For example,
"rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to
"ball|ballShape".

If the new name ends in a single '#' then the rename command will replace the
trailing '#' with a number that ensures the new name is unique.

## Notes

If the name has an absolute namespace part, it will be considered. Namespaces
that do not exist will be created automatically as needed. If the name has a
relative namespace part, it will be ignored. In that case, the object will be
put under the current namespace. (see example below).


-----------------------------------------


Return Value:

string  The new name. When undone returns original name.


-----------------------------------------


Flags:

-----------------------------------------

ignoreShape : ignoreShape     [boolean] []
    Indicates that renaming of shape nodes below transform nodes should be prevented.

-----------------------------------------

uid   : uuid            [boolean]
    Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)

    """

def reorder(b=1,f=1,r="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/reorder.html



-----------------------------------------

reorder is undoable, NOT queryable, and NOT editable.

This command reorders (moves) objects relative to their siblings.

For relative moves, both positive and negative numbers may be specified.
Positive numbers move the object forward and negative numbers move the object
backward amoung its siblings. When an object is at the end (beginning) of the
list of siblings, a relative move of 1 (-1) will put the object at the
beginning (end) of the list of siblings. That is, relative moves will wrap if
necessary.

If a shape is specified and it is the only child then its parent will be
reordered.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

b     : back            [boolean] []
    Move object(s) to back of sibling list.

-----------------------------------------

f     : front           [boolean] []
    Move object(s) to front of sibling list.

-----------------------------------------

r     : relative        [int]
    Move object(s) relative to other siblings.

    """

def reorderContainer(q=1,e=1,b=1,f=1,r="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/reorderContainer.html



-----------------------------------------

reorderContainer is undoable, queryable, and editable.

This command reorders (moves) objects relative to their siblings in a
container.

For relative moves, both positive and negative numbers may be specified.
Positive numbers move the object forward and negative numbers move the object
backward amoung its siblings. When an object is at the end (beginning) of the
list of siblings, a relative move of 1 (-1) will put the object at the
beginning (end) of the list of siblings. That is, relative moves will wrap if
necessary.

Only nodes within one container can be moved at a time. Note: The container
command's -nodeList flag will return a sorted list of contained nodes. To see
the effects of reordering, use the -unsortedOrder flag in conjunction with the
-nodeList flag.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : back            [boolean] ['query', 'edit']
    Move object(s) to back of container contents list

-----------------------------------------

f     : front           [boolean] ['query', 'edit']
    Move object(s) to front of container contents list

-----------------------------------------

r     : relative        [int]
    Move object(s) relative to other container contents

    """

def rotate(a=1,cp=1,cs=1,xn=1,dph=1,eu=1,fo=1,ocp=1,os=1,oa="[angle, angle, angle]",p="[linear, linear, linear]",pcp=1,pgp=1,puv=1,rfl=1,rab=1,rao=1,rax=1,ray=1,raz=1,rft="float",r=1,x=1,xy=1,xyz=1,xz=1,y=1,yz=1,z=1,smn=1,t=1,ws=1,xc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rotate.html



-----------------------------------------

rotate is undoable, NOT queryable, and NOT editable.

The rotate command is used to change the rotation of geometric objects. The
rotation values are specified as Euler angles (rx, ry, rz). The values are
interpreted based on the current working unit for Angular measurements. Most
often this is degrees.

The default behaviour, when no objects or flags are passed, is to do a
absolute rotate on each currently selected object in the world space.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    Perform an absolute operation.

-----------------------------------------

cp    : centerPivot     [boolean] []
    Let the pivot be the center of the bounding box of all objects

-----------------------------------------

cs    : componentSpace  [boolean] []
    Rotate in local component space

-----------------------------------------

xn    : constrainAlongNormal [boolean] []
    When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.

-----------------------------------------

dph   : deletePriorHistory [boolean] []
    If true then delete the history prior to the current operation.

-----------------------------------------

eu    : euler           [boolean] []
    Modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.

-----------------------------------------

fo    : forceOrderXYZ   [boolean] []
    When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.

-----------------------------------------

ocp   : objectCenterPivot [boolean] []
    Let the pivot be the center of the bounding box of each object

-----------------------------------------

os    : objectSpace     [boolean] []
    Perform rotation about object-space axis.

-----------------------------------------

oa    : orientAxes      [[angle, angle, angle]] []
    Euler axis for orientation.

-----------------------------------------

p     : pivot           [[linear, linear, linear]] []
    Define the pivot point for the transformation

-----------------------------------------

pcp   : preserveChildPosition [boolean] []
    When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.

-----------------------------------------

pgp   : preserveGeometryPosition [boolean] []
    When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.

-----------------------------------------

puv   : preserveUV      [boolean] []
    When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.

-----------------------------------------

rfl   : reflection      [boolean] []
    To move the corresponding symmetric components also.

-----------------------------------------

rab   : reflectionAboutBBox [boolean] []
    Sets the position of the reflection axis at the geometry bounding box

-----------------------------------------

rao   : reflectionAboutOrigin [boolean] []
    Sets the position of the reflection axis at the origin

-----------------------------------------

rax   : reflectionAboutX [boolean] []
    Specifies the X=0 as reflection plane

-----------------------------------------

ray   : reflectionAboutY [boolean] []
    Specifies the Y=0 as reflection plane

-----------------------------------------

raz   : reflectionAboutZ [boolean] []
    Specifies the Z=0 as reflection plane

-----------------------------------------

rft   : reflectionTolerance [float] []
    Specifies the tolerance to findout the corresponding reflected components

-----------------------------------------

r     : relative        [boolean] []
    Perform a operation relative to the object's current position

-----------------------------------------

x     : rotateX         [boolean] []
    Rotate in X direction

-----------------------------------------

xy    : rotateXY        [boolean] []
    Rotate in X and Y direction

-----------------------------------------

xyz   : rotateXYZ       [boolean] []
    Rotate in all directions (default)

-----------------------------------------

xz    : rotateXZ        [boolean] []
    Rotate in X and Z direction

-----------------------------------------

y     : rotateY         [boolean] []
    Rotate in Y direction

-----------------------------------------

yz    : rotateYZ        [boolean] []
    Rotate in Y and Z direction

-----------------------------------------

z     : rotateZ         [boolean] []
    Rotate in Z direction

-----------------------------------------

smn   : symNegative     [boolean] []
    When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.

-----------------------------------------

t     : translate       [boolean] []
    When true, the command will modify the node's translate attribute instead of its rotateTranslate attribute, when rotating around a pivot other than the object's own rotate pivot.

-----------------------------------------

ws    : worldSpace      [boolean] []
    Perform rotation about global world-space axis.

-----------------------------------------

xc    : xformConstraint [string]
    Apply a transform constraint to moving components.    * none - no constraint   * surface - constrain components to the surface   * edge - constrain components to surface edges   * live - constraint components to the live surface

    """

def scale(a=1,cp=1,cs=1,xn=1,dph=1,dso=1,ls=1,ocp=1,os=1,oa="[angle, angle, angle]",p="[linear, linear, linear]",pcp=1,pgp=1,puv=1,rfl=1,rab=1,rao=1,rax=1,ray=1,raz=1,rft="float",r=1,x=1,xy=1,xyz=1,xz=1,y=1,yz=1,z=1,smn=1,ws=1,xc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scale.html



-----------------------------------------

scale is undoable, NOT queryable, and NOT editable.

The scale command is used to change the sizes of geometric objects.

The default behaviour, when no objects or flags are passed, is to do a
relative scale on each currently selected object object using each object's
existing scale pivot point.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    Perform an absolute operation.

-----------------------------------------

cp    : centerPivot     [boolean] []
    Let the pivot be the center of the bounding box of all objects

-----------------------------------------

cs    : componentSpace  [boolean] []
    Move in local component space

-----------------------------------------

xn    : constrainAlongNormal [boolean] []
    When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.

-----------------------------------------

dph   : deletePriorHistory [boolean] []
    If true then delete the history prior to the current operation.

-----------------------------------------

dso   : distanceOnly    [boolean] []
    Scale only the distance between the objects.

-----------------------------------------

ls    : localSpace      [boolean] []
    Use local space for scaling

-----------------------------------------

ocp   : objectCenterPivot [boolean] []
    Let the pivot be the center of the bounding box of each object

-----------------------------------------

os    : objectSpace     [boolean] []
    Use object space for scaling

-----------------------------------------

oa    : orientAxes      [[angle, angle, angle]] []
    Use the angles for the orient axes.

-----------------------------------------

p     : pivot           [[linear, linear, linear]] []
    Define the pivot point for the transformation

-----------------------------------------

pcp   : preserveChildPosition [boolean] []
    When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.

-----------------------------------------

pgp   : preserveGeometryPosition [boolean] []
    When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.

-----------------------------------------

puv   : preserveUV      [boolean] []
    When true, UV values on scaled components are projected along the axis of scaling in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.

-----------------------------------------

rfl   : reflection      [boolean] []
    To move the corresponding symmetric components also.

-----------------------------------------

rab   : reflectionAboutBBox [boolean] []
    Sets the position of the reflection axis at the geometry bounding box

-----------------------------------------

rao   : reflectionAboutOrigin [boolean] []
    Sets the position of the reflection axis at the origin

-----------------------------------------

rax   : reflectionAboutX [boolean] []
    Specifies the X=0 as reflection plane

-----------------------------------------

ray   : reflectionAboutY [boolean] []
    Specifies the Y=0 as reflection plane

-----------------------------------------

raz   : reflectionAboutZ [boolean] []
    Specifies the Z=0 as reflection plane

-----------------------------------------

rft   : reflectionTolerance [float] []
    Specifies the tolerance to findout the corresponding reflected components

-----------------------------------------

r     : relative        [boolean] []
    Perform a operation relative to the object's current position

-----------------------------------------

x     : scaleX          [boolean] []
    Scale in X direction

-----------------------------------------

xy    : scaleXY         [boolean] []
    Scale in X and Y direction

-----------------------------------------

xyz   : scaleXYZ        [boolean] []
    Scale in all directions (default)

-----------------------------------------

xz    : scaleXZ         [boolean] []
    Scale in X and Z direction

-----------------------------------------

y     : scaleY          [boolean] []
    Scale in Y direction

-----------------------------------------

yz    : scaleYZ         [boolean] []
    Scale in Y and Z direction

-----------------------------------------

z     : scaleZ          [boolean] []
    Scale in Z direction

-----------------------------------------

smn   : symNegative     [boolean] []
    When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.

-----------------------------------------

ws    : worldSpace      [boolean] []
    Use world space for scaling

-----------------------------------------

xc    : xformConstraint [string]
    Apply a transform constraint to moving components.    * none - no constraint   * surface - constrain components to the surface   * edge - constrain components to surface edges   * live - constraint components to the live surface

    """

def scaleComponents(p="[linear, linear, linear]",ro="[angle, angle, angle]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scaleComponents.html



-----------------------------------------

scaleComponents is undoable, NOT queryable, and NOT editable.

This is a limited version of the scale command. First, it only works on
selected components. You provide a pivot in world space, and you can provide a
rotation. This rotation affects the scaling, so that rather than scaling in X,
Y, Z, this is scaling in X, Y, and Z after they have been rotated by the given
rotation.

This allows selected components to be scaled in any arbitrary space, not just
object or world space as the regular scale allows.

Scale values are always relative, not absolute.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

p     : pivot           [[linear, linear, linear]] []
    The pivot position in world space (default is origin)

-----------------------------------------

ro    : rotation        [[angle, angle, angle]]
    The rotational offset for the scaling (default is none)

    """

def sceneLint(q=1,i="string",v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sceneLint.html



-----------------------------------------

sceneLint is NOT undoable, queryable, and NOT editable.

{ "sceneLint" : { "ISSUE_CODE" : { "description" :
"DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
can be applied { "objects" : [
LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }

The sceneLint command is used to analyze the currently loaded scene to find
potential areas for improvement in performance, memory use, or reduction of
clutter.

In the query mode it will report back the list of available checks it can do.
Each check will have an associated short-form which can be passed to the
command to run specific checks.

In create mode the returned string is a JSON format list of issues and
mitigations that suggest a way to solve the problem it describes.

Mitigation can be automatically performed by extracting the mitigation code
and arguments then running the Python code exec(code, {}, {'OBJECTS' :
objects})


-----------------------------------------


Return Value:

string  JSON formatted results showing the issues that could potentially cause
problems in the scene.    
string[]  When querying issueType shows the description, and benefit values
for the named scene issue.  
string[]  When querying returns the list of all issueTypes by name.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

i     : issueType       [string] ['query']
    Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.  In query mode, this flag can accept a value.

-----------------------------------------

v     : verbose         [boolean]
    If set then include both name and description when querying the list of available issue types.

    """

def sets(q=1,e=1,add="name",af=1,cl="name",co="int",cp="name",eg=1,ep=1,em=1,fc=1,fl="name",fe="name",include="name",int="name",ii="name",im="name",l=1,n="string",nss=1,nw=1,no=1,rm="name",r=1,s=1,sp="name",sub="name",t="string",un="name",v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sets.html



-----------------------------------------

sets is undoable, queryable, and editable.

This command is used to create a set, query some state of a set, or perform
operations to update the membership of a set. A set is a logical grouping of
an arbitrary collection of objects, attributes, or components of objects. Sets
are dependency nodes. Connections from objects to a set define membership in
the set.

Sets are used throughout Maya in a multitude of ways. They are used to define
an association of material properties to objects, to define an association of
lights to objects, to define a bookmark or named collection of objects, to
define a character, and to define the components to be deformed by some
deformation operation.

Sets can be connected to any number of partitions. A partition is a node which
enforces mutual exclusivity amoung the sets in the partition. That is, if an
object is in a set which is in a partition, that object cannot be a member of
any other set that is in the partition.

Without any flags, the sets command will create a set with a default name of
"set#" (where # is an integer). If no items are specified on the command line,
the currently selected items are added to the set. The -em/empty flag can be
used to create an empty set and not have the selected items added to the set.

Sets can be created to have certain restrictions on membership. There can be
"renderable" sets which only allow renderable objects (such as nurbs geometry
or polymesh faces) to be members of the set. There can also be vertex (or
control point), edit point, edge, or face sets which only allow those types of
components to be members of a set. Note that for these sets, if an object with
a valid type of component is to be added to a set, the components of the
object are added to the set instead.

Sets can have an associated color which is only of use when creating vertex
sets. The color can be one of the eight user defined colors defined in the
color preferences. This color can be used, for example to distinguish which
vertices are being deformed by a particular deformation.

Objects, components, or attributes can be added to a set using one of three
flags. The -add/addElement flag will add the objects to a set as long as this
won't break any mutual exclusivity constraints. If there are any items which
can't be added, the command will fail. The -in/include flag will only add
those items which can be added and warn of those which can't. The
-fe/forceElement flag will add all the items to the set but will also remove
any of those items that are in any other set which is in the same partition as
the set.

There are several operations on sets that can be performed with the sets
command. Membership can be queried. Tests for whether an item is in a set or
whether two sets share the same item can be performed. Also, the union,
intersection and difference of sets can be performed which returns a list of
members of the sets which are a result of the operation.


-----------------------------------------


Return Value:

string  For creation operations (name of the set that was created or edited)    
string[]  For query operation (names of items in the set)  
boolean  For isIntersecting and isMember operations  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addElement      [name] ['edit']
    Adds the list of items to the given set. If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.

-----------------------------------------

af    : afterFilters    [boolean] ['edit']
    Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.

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

r     : renderable      [boolean] ['query']
    This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use in creation or query mode only. The default value is false which means a normal set is created.

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

def shapeCompare():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shapeCompare.html



-----------------------------------------

shapeCompare is undoable, NOT queryable, and NOT editable.

Compares two shapes. If no shapes are specified in the command line, then the
shapes from the active list are used.


-----------------------------------------


Return Value:

int  0 if successful, 1 if both shapes are not determined to be equal based on
requested flags.
    """

def snapMode(q=1,c=1,dsi="linear",em="uint",emt="float",gr=1,lfc=1,lp=1,mc=1,pc=1,ps=1,p=1,t="uint",ut=1,uvt="uint",vp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/snapMode.html



-----------------------------------------

snapMode is undoable, queryable, and NOT editable.

The snapMode command is used to control snapping. It toggles the snapping
modes in effect and sets information used for snapping.


-----------------------------------------


Return Value:

boolean  if command is a query    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : curve           [boolean] ['query']
    Set curve snap mode

-----------------------------------------

dsi   : distanceIncrement [linear] ['query']
    Set the distance for the snapping to objects such as a lines or planes.

-----------------------------------------

em    : edgeMagnet      [uint] ['query']
    Number of extra magnets to snap onto, regularly spaced along the edge.

-----------------------------------------

emt   : edgeMagnetTolerance [float] ['query']
    Precision for edge magnet snapping.

-----------------------------------------

gr    : grid            [boolean] ['query']
    Set grid snap mode

-----------------------------------------

lfc   : liveFaceCenter  [boolean] ['query']
    While moving on live polygon objects, snap to its face centers.

-----------------------------------------

lp    : livePoint       [boolean] ['query']
    While moving on live polygon objects, snap to its vertices.

-----------------------------------------

mc    : meshCenter      [boolean] ['query']
    While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.

-----------------------------------------

pc    : pixelCenter     [boolean] ['query']
    Snap UV to the center of the pixel instead of the corner.

-----------------------------------------

ps    : pixelSnap       [boolean] ['query']
    Snap UVs to the nearest pixel center or corner.

-----------------------------------------

p     : point           [boolean] ['query']
    Set point snap mode

-----------------------------------------

t     : tolerance       [uint] ['query']
    Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).

-----------------------------------------

ut    : useTolerance    [boolean] ['query']
    If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.

-----------------------------------------

uvt   : uvTolerance     [uint] ['query']
    uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).

-----------------------------------------

vp    : viewPlane       [boolean]
    Set view-plane snap mode

    """

def snapTogetherCtx(q=1,e=1,cs=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",so=1,spf=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/snapTogetherCtx.html



-----------------------------------------

snapTogetherCtx is undoable, queryable, and editable.

The snapTogetherCtx command creates a tool for snapping surfaces together.


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cs    : clearSelection  [boolean] ['query', 'edit']
    Sets whether the tool should clear the selection on entry to the tool. Default true.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

so    : setOrientation  [boolean] ['query', 'edit']
    Sets whether the tool should orient as well as moving an item. Default true.

-----------------------------------------

spf   : snapPolygonFace [boolean]
    Sets whether the tool should snap the cursor to polygon face centers. Default false.

    """

def spaceLocator(q=1,e=1,a=1,n="string",p="[linear, linear, linear]",r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/spaceLocator.html



-----------------------------------------

spaceLocator is undoable, queryable, and editable.

The command creates a locator at the specified position in space. By default
it is created at (0,0,0).


-----------------------------------------


Return Value:

string[]  The name for the new locator in space.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] ['edit']
    If set, the locator's position is in world space.

-----------------------------------------

n     : name            [string] ['edit']
    Name for the locator.

-----------------------------------------

p     : position        [[linear, linear, linear]] ['query', 'edit']
    Location in 3-dimensional space where locator is to be created.

-----------------------------------------

r     : relative        [boolean]
    If set, the locator's position is relative to its local space. The locator is created in relative mode by default.

    """

def suitePrefs(ats="string",ias=1,ics=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/suitePrefs.html



-----------------------------------------

suitePrefs is undoable, NOT queryable, and NOT editable.

This command sets the mouse and keyboard interaction mode for Maya and other
Suites applications (if Maya is part of a Suites install).


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

ats   : applyToSuite    [string] []
    Apply the mouse and keyboard interaction settings for the given application to all applications in the Suite (if Maya is part of a Suites install). Valid values are "Maya", "3dsMax", or "undefined", which signifies that each app is to use their own settings.

-----------------------------------------

ias   : installedAsSuite [boolean] []
    Returns true if Maya is part of a Suites install, false otherwise.

-----------------------------------------

ics   : isCompleteSuite [boolean]
    Returns true if the Suites install contains all Entertainment Creation Suite products, false otherwise.

    """

def threadCount(q=1,n="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/threadCount.html



-----------------------------------------

threadCount is undoable, queryable, and NOT editable.

This command sets the number of threads to be used by Maya in regions of code
that are multithreaded. By default the number of threads is equal to the
number of logical CPUs, not the number of physical CPUs. Logical CPUs are
different from physical CPUs in the following ways:

A physical CPU with hyperthreading counts as two logical CPUs  
A dual-core CPU counts as two logical CPUs

With some workloads, using one thread per logical CPU may not perform well.
This is sometimes the case with hyperthreading. It is worth experimenting with
different numbers of threads to see which gives the best performance. Note
that having more threads can mean Maya uses more memory.

Setting a value of zero means the number of threads used will equal the number
of logical processors in the system.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

n     : numberOfThreads [int]
    Sets the number of threads to use

    """

def toggleAxis(q=1,o=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/toggleAxis.html



-----------------------------------------

toggleAxis is undoable, queryable, and NOT editable.

Toggles the state of the display axis.

Note: the display of the axis in the bottom left corner has been rendered
obsolete by the headsUpDisplay command.


-----------------------------------------


Return Value:

boolean  if in the query mode, otherwise none.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

o     : origin          [boolean] ['query']
    Turns display of the axis at the origin of the ground plane on or off.

-----------------------------------------

v     : view            [boolean]
    Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)

    """

def transformCompare(r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/transformCompare.html



-----------------------------------------

transformCompare is undoable, NOT queryable, and NOT editable.

Compares two transforms passed as arguments. If they are the same, returns 0.
If they are different, returns 1. If no transforms are specified in the
command line, then the transforms from the active list are used.


-----------------------------------------


Return Value:

int  0 if successful, 1 if transform1 and transform2 are not determined to be
equal.


-----------------------------------------


Flags:

-----------------------------------------

r     : root            [boolean]
    Compare the root only, rather than the entire hierarchy below the roots.

    """

def transformLimits(q=1,e=1,erx="[boolean, boolean]",ery="[boolean, boolean]",erz="[boolean, boolean]",esx="[boolean, boolean]",esy="[boolean, boolean]",esz="[boolean, boolean]",etx="[boolean, boolean]",ety="[boolean, boolean]",etz="[boolean, boolean]",rm=1,rx="[angle, angle]",ry="[angle, angle]",rz="[angle, angle]",sx="[float, float]",sy="[float, float]",sz="[float, float]",tx="[linear, linear]",ty="[linear, linear]",tz="[linear, linear]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/transformLimits.html



-----------------------------------------

transformLimits is undoable, queryable, and editable.

The transformLimits command allows us to set, edit, or query the limits of the
transformation that can be applied to objects.

We can also turn any limits off which may have been previously set. When an
object is first created, all the transformation limits are off by default.

Transformation limits allow us to control how much an object can be
transformed. This is most useful for joints, although it can be used any place
we would like to limit the movement of an object.

Default values are:  
( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

erx   : enableRotationX [[boolean, boolean]] ['query']
    enable/disable the lower and upper x-rotation limits   When queried, it returns boolean boolean

-----------------------------------------

ery   : enableRotationY [[boolean, boolean]] ['query']
    enable/disable the lower and upper y-rotation limits   When queried, it returns boolean boolean

-----------------------------------------

erz   : enableRotationZ [[boolean, boolean]] ['query']
    enable/disable the lower and upper z-rotation limits   When queried, it returns boolean boolean

-----------------------------------------

esx   : enableScaleX    [[boolean, boolean]] ['query']
    enable/disable the lower and upper x-scale limits   When queried, it returns boolean boolean

-----------------------------------------

esy   : enableScaleY    [[boolean, boolean]] ['query']
    enable/disable the lower and upper y-scale limits   When queried, it returns boolean boolean

-----------------------------------------

esz   : enableScaleZ    [[boolean, boolean]] ['query']
    enable/disable the lower and upper z-scale limits   When queried, it returns boolean boolean

-----------------------------------------

etx   : enableTranslationX [[boolean, boolean]] ['query']
    enable/disable the ower and upper x-translation limits   When queried, it returns boolean boolean

-----------------------------------------

ety   : enableTranslationY [[boolean, boolean]] ['query']
    enable/disable the lower and upper y-translation limits   When queried, it returns boolean boolean

-----------------------------------------

etz   : enableTranslationZ [[boolean, boolean]] ['query']
    enable/disable the lower and upper z-translation limits   When queried, it returns boolean boolean

-----------------------------------------

rm    : remove          [boolean] []
    turn all the limits off and reset them to their default values

-----------------------------------------

rx    : rotationX       [[angle, angle]] ['query']
    set the lower and upper x-rotation limits   When queried, it returns angle angle

-----------------------------------------

ry    : rotationY       [[angle, angle]] ['query']
    set the lower and upper y-rotation limits   When queried, it returns angle angle

-----------------------------------------

rz    : rotationZ       [[angle, angle]] ['query']
    set the lower and upper z-rotation limits   When queried, it returns angle angle

-----------------------------------------

sx    : scaleX          [[float, float]] ['query']
    set the lower and upper x-scale limits   When queried, it returns float float

-----------------------------------------

sy    : scaleY          [[float, float]] ['query']
    set the lower and upper y-scale limits   When queried, it returns float float

-----------------------------------------

sz    : scaleZ          [[float, float]] ['query']
    set the lower and upper z-scale limits   When queried, it returns float float

-----------------------------------------

tx    : translationX    [[linear, linear]] ['query']
    set the lower and upper x-translation limits   When queried, it returns linear linear

-----------------------------------------

ty    : translationY    [[linear, linear]] ['query']
    set the lower and upper y-translation limits   When queried, it returns linear linear

-----------------------------------------

tz    : translationZ    [[linear, linear]]
    set the lower and upper z-translation limits   When queried, it returns linear linear

    """

def ungroup(a=1,p="string",r=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ungroup.html



-----------------------------------------

ungroup is undoable, NOT queryable, and NOT editable.

This command ungroups the specified objects.

The objects will be placed at the same level in the hierarchy the group node
occupied unless the -w flag is specified, in which case they will be placed
under the world.

If an object is ungrouped and there is an object in the new group with the
same name then this command will rename the ungrouped object.

See also: group, parent, instance, duplicate


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]

-----------------------------------------

p     : parent          [string] []
    put the ungrouped objects under the given parent

-----------------------------------------

r     : relative        [boolean] []
    preserve existing local object transformations (don't modify local transformation)

-----------------------------------------

w     : world           [boolean]
    put the ungrouped objects under the world

    """

def upAxis(q=1,ax="string",rv=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/upAxis.html



-----------------------------------------

upAxis is undoable, queryable, and NOT editable.

The upAxis command changes the world up direction. Current implementation
provides only two choices of axis (the Y-axis or the Z-axis) as the world up
direction.

By default, the ground plane in Maya is on the XY plane. Hence, the default
up-direction is the direction of the positive Z-axis.

The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag
is specified, the camera of currently active view is revolved about the X-axis
such that the position of the groundplane in the view will remain the same as
before the the up direction is changed.

The screen update is applied to all cameras of all views.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [string] ['query']
    This flag specifies the axis as the world up direction. The valid axis are either "y" or "z".   When queried, it returns a string.

-----------------------------------------

rv    : rotateView      [boolean]
    This flag specifies to rotate the view as well.

    """

def webView(url="string",wh="int",ww="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/webView.html



-----------------------------------------

webView is undoable, NOT queryable, and NOT editable.

This command allows the user to bring up a web page view


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

url   : urlAddress      [string] []
    Bring up webView on given URL

-----------------------------------------

wh    : windowHeight    [int] []
    Set the window height

-----------------------------------------

ww    : windowWidth     [int]
    Set the window width

    """

def xform(q=1,a=1,bb=1,bbi=1,cp=1,cpc=1,dph=1,eu=1,m="[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]",os=1,piv="[linear, linear, linear]",p=1,puv=1,rfl=1,rab=1,rao=1,rax=1,ray=1,raz=1,rft="float",r=1,ra="[angle, angle, angle]",roo="string",rp="[linear, linear, linear]",rt="[linear, linear, linear]",ro="[angle, angle, angle]",s="[float, float, float]",sp="[linear, linear, linear]",st="[linear, linear, linear]",sh="[float, float, float]",t="[linear, linear, linear]",ws=1,wd=1,ztp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/xform.html



-----------------------------------------

xform is undoable, queryable, and NOT editable.

This command can be used query/set any element in a transformation node. It
can also be used to query some values that cannot be set directly such as the
transformation matrix or the bounding box. It can also set both pivot points
to convenient values.

All values are specified in transformation coordinates. (attribute-space)

In addition, the attributes are applied/returned in the order in which they
appear in the flags section. (which corresponds to the order they appear in
the transformation matrix as given below)

See also: move, rotate, scale

## Notes

The transformation matrix for a node is built by post-multiplying the
following matrices in the given order (Note: rotations are applied according
to the rotation order parameter and the 6 different rotation possibilities are
not shown below)

    
    
    -1                       -1
    [M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    
    
    
    where:
    
    
    
    [sp] = |  1      0        0       0 | = scale pivot matrix
    |  0      1        0       0 |
    |  0      0        1       0 |
    | -spx   -spy     -spz     1 |
    
    
    
    
    
    
    [s]  = |  sx     0        0       0 | = scale matrix
    |  0      sy       0       0 |
    |  0      0        sz      0 |
    |  0      0        0       1 |
    
    
    
    
    
    
    [sh] = |  1      0        0       0 | = shear matrix
    |  xy     1        0       0 |
    |  xz     yz       1       0 |
    |  0      0        0       1 |
    
    
    
    -1
    [sp] = |  1       0       0       0 | = scale pivot inverse matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  spx     spy     spz     1 |
    
    
    
    
    
    
    [st] = |  1       0       0       0 | = scale translate matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  stx     sty     stz     1 |
    
    
    
    
    
    
    [rp] = |  1       0       0       0 | = rotate pivot matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    | -rpx    -rpy    -rpz     1 |
    
    
    
    
    
    
    [ar] = |  *       *       *       0 | = axis rotation matrix
    |  *       *       *       0 |   (composite rotation,
    |  *       *       *       0 |    see [rx], [ry], [rz]
    |  0       0       0       1 |    below for details)
    
    
    
    
    
    
    [rx] = |  1       0       0       0 | = rotate X matrix
    |  0       cos(x)  sin(x)  0 |
    |  0      -sin(x)  cos(x)  0 |
    |  0       0       0       1 |
    
    
    
    
    
    
    [ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    |  0       1       0       0 |
    |  sin(y)  0       cos(y)  0 |
    |  0       0       0       1 |
    
    
    
    
    
    
    [rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    | -sin(z)  cos(z)  0       0 |
    |  0       0       1       0 |
    |  0       0       0       1 |
    
    
    
    -1
    [rp] = |  1       0       0       0 | = rotate pivot matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  rpx     rpy     rpz     1 |
    
    
    
    
    
    
    [rt] = |  1       0       0       0 | = rotate translate matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  rtx     rty     rtz     1 |
    
    
    
    
    
    
    [t]  = |  1       0       0       0 | = translation matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  tx      ty      tz      1 |


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    perform absolute transformation (default)

-----------------------------------------

bb    : boundingBox     [boolean] ['query']
    Returns the bounding box of an object. The values returned are in the following order: xmin ymin zmin xmax ymax zmax.

-----------------------------------------

bbi   : boundingBoxInvisible [boolean] ['query']
    Returns the bounding box of an object. This includes the bounding boxes of all invisible children which are not included using the boundingBox flag. The values returned are in following order: xmin ymin zmin xmax ymax zmax.

-----------------------------------------

cp    : centerPivots    [boolean] []
    Set pivot points to the center of the object's bounding box. (see -p flag)

-----------------------------------------

cpc   : centerPivotsOnComponents [boolean] []
    Set pivot points to the center of the component's bounding box. (see -p flag)

-----------------------------------------

dph   : deletePriorHistory [boolean] []
    If true then delete the construction history before the operation is performed.

-----------------------------------------

eu    : euler           [boolean] []
    modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.

-----------------------------------------

m     : matrix          [[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]] ['query']
    Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.

-----------------------------------------

os    : objectSpace     [boolean] ['query']
    treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)

-----------------------------------------

piv   : pivots          [[linear, linear, linear]] ['query']
    convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)

-----------------------------------------

p     : preserve        [boolean] []
    preserve overall transformation. used to prevent object from "jumping" when changing pivots or rotation order. the default value is true. (used with -sp, -rp, -roo, -cp, -ra)

-----------------------------------------

puv   : preserveUV      [boolean] []
    When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.

-----------------------------------------

rfl   : reflection      [boolean] []
    To move the corresponding symmetric components also.

-----------------------------------------

rab   : reflectionAboutBBox [boolean] []
    Sets the position of the reflection axis at the geometry bounding box

-----------------------------------------

rao   : reflectionAboutOrigin [boolean] []
    Sets the position of the reflection axis at the origin

-----------------------------------------

rax   : reflectionAboutX [boolean] []
    Specifies the X=0 as reflection plane

-----------------------------------------

ray   : reflectionAboutY [boolean] []
    Specifies the Y=0 as reflection plane

-----------------------------------------

raz   : reflectionAboutZ [boolean] []
    Specifies the Z=0 as reflection plane

-----------------------------------------

rft   : reflectionTolerance [float] []
    Specifies the tolerance to findout the corresponding reflected components

-----------------------------------------

r     : relative        [boolean] []
    perform relative transformation

-----------------------------------------

ra    : rotateAxis      [[angle, angle, angle]] ['query']
    rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)

-----------------------------------------

roo   : rotateOrder     [string] ['query']
    rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>

-----------------------------------------

rp    : rotatePivot     [[linear, linear, linear]] ['query']
    rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)

-----------------------------------------

rt    : rotateTranslation [[linear, linear, linear]] ['query']
    rotation translation

-----------------------------------------

ro    : rotation        [[angle, angle, angle]] ['query']
    rotation transformation

-----------------------------------------

s     : scale           [[float, float, float]] ['query']
    scale transformation

-----------------------------------------

sp    : scalePivot      [[linear, linear, linear]] ['query']
    scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)

-----------------------------------------

st    : scaleTranslation [[linear, linear, linear]] ['query']
    scale translation

-----------------------------------------

sh    : shear           [[float, float, float]] ['query']
    shear transformation. The values represent the shear <xy,xz,yz>

-----------------------------------------

t     : translation     [[linear, linear, linear]] ['query']
    translation

-----------------------------------------

ws    : worldSpace      [boolean] ['query']
    (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.

-----------------------------------------

wd    : worldSpaceDistance [boolean] ['query']
    Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for world space.

-----------------------------------------

ztp   : zeroTransformPivots [boolean]
    reset pivot points and pivot translations without changing the overall matrix by applying these values into the translation channel.

    """

def xformConstraint(q=1,e=1,n="int",l=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/xformConstraint.html



-----------------------------------------

xformConstraint is undoable, queryable, and editable.

This command allows you to change the transform constraint used by the
transform tools during component transforms.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

n     : alongNormal     [int] ['query', 'edit']
    When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.

-----------------------------------------

l     : live            [boolean] ['query']
    Query-only flag that can be used to check whether the current live surface will be used as a transform constraint.

-----------------------------------------

t     : type            [string]
    Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.    * none - no constraint   * surface - constrain components to their surface   * edge - constrain components to surface edges

    """

def addAttr(q=1,e=1,at="string",bt="string",ci=1,ct="string",dt="string",dv="float",dcb="uint",en="string",ex=1,fp=1,hxv=1,hnv=1,hsx=1,hsn=1,h=1,im=1,internalSet=1,k=1,ln="string",max="float",min="float",m=1,nn="string",nc="uint",p="string",pxy="string",r=1,sn="string",smx="float",smn="float",s=1,uac=1,uaf=1,uap=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/addAttr.html



-----------------------------------------

addAttr is undoable, queryable, and editable.

This command is used to add a dynamic attribute to a node or nodes. Either the
longName or the shortName or both must be specified. If neither a dataType nor
an attributeType is specified, a double attribute will be added. The dataType
flag can be specified more than once indicating that any of the supplied types
will be accepted (logical-or).

To add a non-double attribute the following criteria can be used to determine
whether the dataType or the attributeType flag is appropriate. Some types,
such as double3 can use either. In these cases the -dt flag should be used
when you only wish to access the data as an atomic entity (eg. you never want
to access the three individual values that make up a double3). In general it
is best to use the -at in these cases for maximum flexibility. In most cases
the -dt version will not display in the attribute editor as it is an atomic
type and you are not allowed to change individual parts of it.

All attributes flagged as "(compound)" below or the compound attribute itself
are not actually added to the node until all of the children are defined
(using the "-p" flag to set their parent to the compound being created). See
the EXAMPLES section for more details.

Type of attribute |  Flag and argument to use  
---|---  
boolean |  -at bool  
32 bit integer |  -at long  
16 bit integer |  -at short  
8 bit integer |  -at byte  
char |  -at char  
enum |  -at enum (specify the enum names using the enumName flag)  
float |  -at "float" (use quotes since float is a mel keyword)  
double |  -at double  
angle value |  -at doubleAngle  
linear value |  -at doubleLinear  
string |  -dt "string" (use quotes since string is a mel keyword)  
array of strings |  -dt stringArray  
compound |  -at compound  
message (no data) |  -at message  
time |  -at time  
4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)  
4x4 float matrix |  -at fltMatrix  
reflectance |  -dt reflectanceRGB  
reflectance (compound) |  -at reflectance  
spectrum |  -dt spectrumRGB  
spectrum (compound) |  -at spectrum  
2 floats |  -dt float2  
2 floats (compound) |  -at float2  
3 floats |  -dt float3  
3 floats (compound) |  -at float3  
2 doubles |  -dt double2  
2 doubles (compound) |  -at double2  
3 doubles |  -dt double3  
3 doubles (compound) |  -at double3  
2 32-bit integers |  -dt long2  
2 32-bit integers (compound) |  -at long2  
3 32-bit integers |  -dt long3  
3 32-bit integers (compound) |  -at long3  
2 16-bit integers |  -dt short2  
2 16-bit integers (compound) |  -at short2  
3 16-bit integers |  -dt short3  
3 16-bit integers (compound) |  -at short3  
array of doubles |  -dt doubleArray  
array of floats |  -dt floatArray  
array of 32-bit ints |  -dt Int32Array  
array of vectors |  -dt vectorArray  
nurbs curve |  -dt nurbsCurve  
nurbs surface |  -dt nurbsSurface  
polygonal mesh |  -dt mesh  
lattice |  -dt lattice  
array of double 4D points |  -dt pointArray


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attributeType   [string] ['query']
    Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.

-----------------------------------------

bt    : binaryTag       [string] ['query']
    This flag is obsolete and does not do anything any more

-----------------------------------------

ci    : cachedInternally [boolean] ['query']
    Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.

-----------------------------------------

ct    : category        [string] ['query', 'edit']
    An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.

-----------------------------------------

dt    : dataType        [string] ['query']
    Specifies the data type. See "setAttr" for more information on data type names.

-----------------------------------------

dv    : defaultValue    [float] ['query', 'edit']
    Specifies the default value for the attribute (can only be used for numeric attributes).

-----------------------------------------

dcb   : disconnectBehaviour [uint] ['query']
    defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete

-----------------------------------------

en    : enumName        [string] ['query', 'edit']
    Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5. (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu. Extra menu items can appear that represent the numbers inbetween non-sequential option values. To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box. For example: "solo=1:triplet=2:quintet=3".)

-----------------------------------------

ex    : exists          [boolean] ['query']
    Returns true if the attribute queried is a user-added, dynamic attribute; false if not.

-----------------------------------------

fp    : fromPlugin      [boolean] ['query']
    Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.

-----------------------------------------

hxv   : hasMaxValue     [boolean] ['query', 'edit']
    Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).

-----------------------------------------

hnv   : hasMinValue     [boolean] ['query', 'edit']
    Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).

-----------------------------------------

hsx   : hasSoftMaxValue [boolean] ['query']
    Flag indicating whether a numeric attribute has a soft maximum.

-----------------------------------------

hsn   : hasSoftMinValue [boolean] ['query']
    Flag indicating whether a numeric attribute has a soft minimum.

-----------------------------------------

h     : hidden          [boolean] ['query']
    Will this attribute be hidden from the UI?

-----------------------------------------

im    : indexMatters    [boolean] ['query']
    Sets whether an index must be used when connecting to this multi- attribute. Setting indexMatters to false forces the attribute to non-readable.

-----------------------------------------

internalSet : internalSet     [boolean] ['query']
    Whether or not the internal cached value is set when this attribute value is changed. This is an internal flag used for updating UI elements.

-----------------------------------------

k     : keyable         [boolean] ['query']
    Is the attribute keyable by default?

-----------------------------------------

ln    : longName        [string] ['query']
    Sets the long name of the attribute.

-----------------------------------------

max   : maxValue        [float] ['query', 'edit']
    Specifies the maximum value for the attribute (can only be used for numeric attributes).

-----------------------------------------

min   : minValue        [float] ['query', 'edit']
    Specifies the minimum value for the attribute (can only be used for numeric attributes).

-----------------------------------------

m     : multi           [boolean] ['query']
    Makes the new attribute a multi-attribute.

-----------------------------------------

nn    : niceName        [string] ['query', 'edit']
    Sets the nice name of the attribute for display in the UI. Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog. (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)

-----------------------------------------

nc    : numberOfChildren [uint] ['query']
    How many children will the new attribute have?

-----------------------------------------

p     : parent          [string] ['query']
    Attribute that is to be the new attribute's parent.

-----------------------------------------

pxy   : proxy           [string] ['query']
    Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.

-----------------------------------------

r     : readable        [boolean] ['query']
    Can outgoing connections be made from this attribute?

-----------------------------------------

sn    : shortName       [string] ['query']
    Sets the short name of the attribute.

-----------------------------------------

smx   : softMaxValue    [float] ['query', 'edit']
    Soft maximum, valid for numeric attributes only. Specifies the upper default limit used in sliders for this attribute.

-----------------------------------------

smn   : softMinValue    [float] ['query', 'edit']
    Soft minimum, valid for numeric attributes only. Specifies the upper default limit used in sliders for this attribute.

-----------------------------------------

s     : storable        [boolean] ['query']
    Can the attribute be stored out to a file?

-----------------------------------------

uac   : usedAsColor     [boolean] ['query']
    Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag. The attribute type "-at" should be "double3" or "float3" as appropriate. It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative. The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.

-----------------------------------------

uaf   : usedAsFilename  [boolean] ['query']
    Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".

-----------------------------------------

uap   : usedAsProxy     [boolean] ['query']
    Set if the specified attribute should be treated as a proxy to another attributes.

-----------------------------------------

w     : writable        [boolean]
    Can incoming connections be made to this attribute?

    """

def addExtension(q=1,e=1,nt="string",at="string",bt="string",ci=1,ct="string",dt="string",dv="float",dcb="uint",en="string",ex=1,fp=1,hxv=1,hnv=1,hsx=1,hsn=1,h=1,im=1,internalSet=1,k=1,ln="string",max="float",min="float",m=1,nn="string",nc="uint",p="string",pxy="string",r=1,sn="string",smx="float",smn="float",s=1,uac=1,uaf=1,uap=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/addExtension.html



-----------------------------------------

addExtension is NOT undoable, queryable, and editable.

This command is used to add an extension attribute to a node type. Either the
longName or the shortName or both must be specified. If neither a dataType nor
an attributeType is specified, a double attribute will be added. The dataType
flag can be specified more than once indicating that any of the supplied types
will be accepted (logical-or).

To add a non-double attribute the following criteria can be used to determine
whether the dataType or the attributeType flag is appropriate. Some types,
such as double3 can use either. In these cases the -dt flag should be used
when you only wish to access the data as an atomic entity (eg. you never want
to access the three individual values that make up a double3). In general it
is best to use the -at in these cases for maximum flexibility. In most cases
the -dt version will not display in the attribute editor as it is an atomic
type and you are not allowed to change individual parts of it.

All attributes flagged as "(compound)" below or the compound attribute itself
are not actually added to the node until all of the children are defined
(using the "-p" flag to set their parent to the compound being created). See
the EXAMPLES section for more details.

Type of attribute |  Flag and argument to use  
---|---  
boolean |  -at bool  
32 bit integer |  -at long  
16 bit integer |  -at short  
8 bit integer |  -at byte  
char |  -at char  
enum |  -at enum (specify the enum names using the enumName flag)  
float |  -at "float" (use quotes since float is a mel keyword)  
double |  -at double  
angle value |  -at doubleAngle  
linear value |  -at doubleLinear  
string |  -dt "string" (use quotes since string is a mel keyword)  
array of strings |  -dt stringArray  
compound |  -at compound  
message (no data) |  -at message  
time |  -at time  
4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)  
4x4 float matrix |  -at fltMatrix  
reflectance |  -dt reflectanceRGB  
reflectance (compound) |  -at reflectance  
spectrum |  -dt spectrumRGB  
spectrum (compound) |  -at spectrum  
2 floats |  -dt float2  
2 floats (compound) |  -at float2  
3 floats |  -dt float3  
3 floats (compound) |  -at float3  
2 doubles |  -dt double2  
2 doubles (compound) |  -at double2  
3 doubles |  -dt double3  
3 doubles (compound) |  -at double3  
2 32-bit integers |  -dt long2  
2 32-bit integers (compound) |  -at long2  
3 32-bit integers |  -dt long3  
3 32-bit integers (compound) |  -at long3  
2 16-bit integers |  -dt short2  
2 16-bit integers (compound) |  -at short2  
3 16-bit integers |  -dt short3  
3 16-bit integers (compound) |  -at short3  
array of doubles |  -dt doubleArray  
array of floats |  -dt floatArray  
array of 32-bit ints |  -dt Int32Array  
array of vectors |  -dt vectorArray  
nurbs curve |  -dt nurbsCurve  
nurbs surface |  -dt nurbsSurface  
polygonal mesh |  -dt mesh  
lattice |  -dt lattice  
array of double 4D points |  -dt pointArray


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

nt    : nodeType        [string] ['query', 'edit']
    Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.

-----------------------------------------

at    : attributeType   [string] ['query']
    Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.

-----------------------------------------

bt    : binaryTag       [string] ['query']
    This flag is obsolete and does not do anything any more

-----------------------------------------

ci    : cachedInternally [boolean] ['query']
    Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.

-----------------------------------------

ct    : category        [string] ['query', 'edit']
    An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.

-----------------------------------------

dt    : dataType        [string] ['query']
    Specifies the data type. See "setAttr" for more information on data type names.

-----------------------------------------

dv    : defaultValue    [float] ['query', 'edit']
    Specifies the default value for the attribute (can only be used for numeric attributes).

-----------------------------------------

dcb   : disconnectBehaviour [uint] ['query']
    defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete

-----------------------------------------

en    : enumName        [string] ['query', 'edit']
    Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5. (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu. Extra menu items can appear that represent the numbers inbetween non-sequential option values. To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box. For example: "solo=1:triplet=2:quintet=3".)

-----------------------------------------

ex    : exists          [boolean] ['query']
    Returns true if the attribute queried is a user-added, dynamic attribute; false if not.

-----------------------------------------

fp    : fromPlugin      [boolean] ['query']
    Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.

-----------------------------------------

hxv   : hasMaxValue     [boolean] ['query', 'edit']
    Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).

-----------------------------------------

hnv   : hasMinValue     [boolean] ['query', 'edit']
    Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).

-----------------------------------------

hsx   : hasSoftMaxValue [boolean] ['query']
    Flag indicating whether a numeric attribute has a soft maximum.

-----------------------------------------

hsn   : hasSoftMinValue [boolean] ['query']
    Flag indicating whether a numeric attribute has a soft minimum.

-----------------------------------------

h     : hidden          [boolean] ['query']
    Will this attribute be hidden from the UI?

-----------------------------------------

im    : indexMatters    [boolean] ['query']
    Sets whether an index must be used when connecting to this multi- attribute. Setting indexMatters to false forces the attribute to non-readable.

-----------------------------------------

internalSet : internalSet     [boolean] ['query']
    Whether or not the internal cached value is set when this attribute value is changed. This is an internal flag used for updating UI elements.

-----------------------------------------

k     : keyable         [boolean] ['query']
    Is the attribute keyable by default?

-----------------------------------------

ln    : longName        [string] ['query']
    Sets the long name of the attribute.

-----------------------------------------

max   : maxValue        [float] ['query', 'edit']
    Specifies the maximum value for the attribute (can only be used for numeric attributes).

-----------------------------------------

min   : minValue        [float] ['query', 'edit']
    Specifies the minimum value for the attribute (can only be used for numeric attributes).

-----------------------------------------

m     : multi           [boolean] ['query']
    Makes the new attribute a multi-attribute.

-----------------------------------------

nn    : niceName        [string] ['query', 'edit']
    Sets the nice name of the attribute for display in the UI. Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog. (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)

-----------------------------------------

nc    : numberOfChildren [uint] ['query']
    How many children will the new attribute have?

-----------------------------------------

p     : parent          [string] ['query']
    Attribute that is to be the new attribute's parent.

-----------------------------------------

pxy   : proxy           [string] ['query']
    Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.

-----------------------------------------

r     : readable        [boolean] ['query']
    Can outgoing connections be made from this attribute?

-----------------------------------------

sn    : shortName       [string] ['query']
    Sets the short name of the attribute.

-----------------------------------------

smx   : softMaxValue    [float] ['query', 'edit']
    Soft maximum, valid for numeric attributes only. Specifies the upper default limit used in sliders for this attribute.

-----------------------------------------

smn   : softMinValue    [float] ['query', 'edit']
    Soft minimum, valid for numeric attributes only. Specifies the upper default limit used in sliders for this attribute.

-----------------------------------------

s     : storable        [boolean] ['query']
    Can the attribute be stored out to a file?

-----------------------------------------

uac   : usedAsColor     [boolean] ['query']
    Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag. The attribute type "-at" should be "double3" or "float3" as appropriate. It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative. The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.

-----------------------------------------

uaf   : usedAsFilename  [boolean] ['query']
    Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".

-----------------------------------------

uap   : usedAsProxy     [boolean] ['query']
    Set if the specified attribute should be treated as a proxy to another attributes.

-----------------------------------------

w     : writable        [boolean]
    Can incoming connections be made to this attribute?

    """

def aliasAttr(q=1,e=1,rm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/aliasAttr.html



-----------------------------------------

aliasAttr is undoable, queryable, and editable.

Allows aliases (alternate names) to be defined for any attribute of a
specified node. When an attribute is aliased, the alias will be used by the
system to display information about the attribute. The user may, however,
freely use either the alias or the original name of the attribute. Only a
single alias can be specified for an attribute so setting an alias on an
already-aliased attribute destroys the old alias.


-----------------------------------------


Return Value:

string[]  in query mode.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

rm    : remove          [boolean]
    Specifies that aliases listed should be removed (otherwise new aliases are added).

    """

def applyAttrPattern(nt="string",pn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/applyAttrPattern.html



-----------------------------------------

applyAttrPattern is undoable, NOT queryable, and NOT editable.

Take the attribute structure described by a pre-defined pattern and apply it
either to a node (as dynamic attributes) or a node type (as extension
attributes). The same pattern can be applied more than once to different nodes
or node types as the operation duplicates the attribute structure described by
the pattern. See the 'createAttrPatterns' command for a description of how to
create a pattern.


-----------------------------------------


Return Value:

int  Number of nodes or node types to which the attribute were added


-----------------------------------------


Flags:

-----------------------------------------

nt    : nodeType        [string] []
    Name of the node type to which the attribute pattern is to be applied. This flag will cause a new extension attribute tree to be created, making the new attributes available on all nodes of the given type. If it is not specified then either a node name must be specified or a node must be selected for application of dynamic attributes.

-----------------------------------------

pn    : patternName     [string]
    The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.

    """

def attributeInfo(all=1,b=1,enumerated=1,h=1,inherited=1,i=1,l=1,logicalAnd=1,m=1,s=1,ui=1,w=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/attributeInfo.html



-----------------------------------------

attributeInfo is NOT undoable, NOT queryable, and NOT editable.

This command lists all of the attributes that are marked with certain flags.
Combinations of flags may be specified and all will be considered. (The method
of combination depends on the state of the "logicalAnd/and" flag.) When the
"allAttributes/all" flag is specified, attributes of all types will be listed.


-----------------------------------------


Return Value:

string[]  List of attributes matching criteria


-----------------------------------------


Flags:

-----------------------------------------

all   : allAttributes   [boolean] []
    Show all attributes associated with the node regardless of type. Use of this flag overrides any other attribute type flags and logical operation that may be specified on the command.

-----------------------------------------

b     : bool            [boolean] []
    Show the attributes that are of type boolean. Use the 'on' state to get only boolean attributes; the 'off' state to ignore boolean attributes.

-----------------------------------------

e     : enumerated      [boolean] []
    Show the attributes that are of type enumerated. Use the 'on' state to get only enumerated attributes; the 'off' state to ignore enumerated attributes.

-----------------------------------------

h     : hidden          [boolean] []
    Show the attributes that are marked as hidden. Use the 'on' state to get hidden attributes; the 'off' state to get non-hidden attributes.

-----------------------------------------

inherited : inherited       [boolean] []
    Filter the attributes based on whether they belong to the node type directly or have been inherited from a root type (e.g. meshShape/direct or dagObject/inherited). Use the 'on' state to get only inherited attributes, the 'off' state to get only directly owned attributes, and leave the flag unspecified to get both.

-----------------------------------------

i     : internal        [boolean] []
    Show the attributes that are marked as internal to the node. Use the 'on' state to get internal attributes; the 'off' state to get non-internal attributes.

-----------------------------------------

l     : leaf            [boolean] []
    Show the attributes that are complex leaves (ie. that have parent attributes and have no children themselves). Use the 'on' state to get leaf attributes; the 'off' state to get non-leaf attributes.

-----------------------------------------

logicalAnd : logicalAnd      [boolean] []
    The default is to take the logical 'or' of the above conditions. Specifying this flag switches to the logical 'and' instead.

-----------------------------------------

m     : multi           [boolean] []
    Show the attributes that are multis. Use the 'on' state to get multi attributes; the 'off' state to get non-multi attributes.

-----------------------------------------

s     : short           [boolean] []
    Show the short attribute names instead of the long names.

-----------------------------------------

ui    : userInterface   [boolean] []
    Show the UI-friendly attribute names instead of the Maya ASCII names. Takes precedence over the -s/-short flag if both are specified.

-----------------------------------------

w     : writable        [boolean] []
    Show the attributes that are writable (ie. can have input connections). Use the 'on' state to get writable attributes; the 'off' state to get non- writable attributes.

-----------------------------------------

t     : type            [string]
    static node type from which to get 'affects' information

    """

def attributeName(lf=1,l=1,n=1,s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/attributeName.html



-----------------------------------------

attributeName is NOT undoable, NOT queryable, and NOT editable.

This command takes one "node.attribute"-style specifier on the command line
and returns either the attribute's long, short, or nice name. (The "nice"
name, or UI name, is the name used to display the attribute in Maya's
interface, and may be localized when running Maya in a language other than
English.) If more than one "node.attribute" specifier is given on the command
line, only the first valid specifier is processed.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

lf    : leaf            [boolean] []
    When false, shows parent multi attributes (like "controlPoints[2].xValue"). When true, shows only the leaf-level attribute name (like "xValue"). Default is true. Note that for incomplete attribute strings, like a missing multi-parent index ("controlPoints.xValue") or an incorrectly named compound (cntrlPnts[2].xValue), this flag defaults to true and provides a result as long as the named leaf-level attribute is defined for the node.

-----------------------------------------

l     : long            [boolean] []
    Returns names in "long name" format like "translateX"

-----------------------------------------

n     : nice            [boolean] []
    Returns names in "nice name" format like "Translate X"

-----------------------------------------

s     : short           [boolean]
    Returns names in "short name" format like "tx"

    """

def attributeQuery(aa=1,aws=1,at=1,ci=1,ct=1,ch=1,c=1,enum=1,ex=1,h=1,idt=1,im=1,i=1,ig=1,internalSet=1,k=1,lc=1,ld=1,le=1,lp=1,ls=1,ln=1,mxe=1,max=1,msg=1,mne=1,min=1,m=1,nn=1,n="name",nc=1,r=1,re=1,rd=1,rs=1,sn=1,smx=1,sxe=1,smn=1,sme=1,s=1,se=1,st=1,typ="string",tex="string",uac=1,uaf=1,umb=1,ws=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/attributeQuery.html



-----------------------------------------

attributeQuery is NOT undoable, NOT queryable, and NOT editable.

attributeQuery returns information about the configuration of an attribute. It
handles both boolean flags, returning true or false, as well as other return
values. Specifying more than one boolean flag will return the logical "and" of
all the specified boolean flags. You may not specify any two flags when both
do not provide a boolean return type. (eg. "-internal -hidden" is okay but
"-range -hidden" or "-range -softRange" is not.)


-----------------------------------------


Return Value:

float[]  when querying ranges or default values    
boolean  when querying attribute flags


-----------------------------------------


Flags:

-----------------------------------------

aa    : affectsAppearance [boolean] []
    Return true if the attribute affects the appearance of the node

-----------------------------------------

aws   : affectsWorldspace [boolean] []
    Return the status of the attribute flag marking attributes affecting worldspace

-----------------------------------------

at    : attributeType   [boolean] []
    Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).

-----------------------------------------

ci    : cachedInternally [boolean] []
    Return whether the attribute is cached within the node as well as in the datablock

-----------------------------------------

ct    : categories      [boolean] []
    Return the categories to which the attribute belongs or an empty list if it does not belong to any.

-----------------------------------------

ch    : channelBox      [boolean] []
    Return whether the attribute should show up in the channelBox or not

-----------------------------------------

c     : connectable     [boolean] []
    Return the connectable status of the attribute

-----------------------------------------

e     : enum            [boolean] []
    Return true if the attribute is a enum attribute

-----------------------------------------

ex    : exists          [boolean] []
    Return true if the attribute exists

-----------------------------------------

h     : hidden          [boolean] []
    Return the hidden status of the attribute

-----------------------------------------

idt   : indeterminant   [boolean] []
    Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time

-----------------------------------------

im    : indexMatters    [boolean] []
    Return the indexMatters status of the attribute

-----------------------------------------

i     : internal        [boolean] []
    Return true if the attribute is either internalSet or internalGet

-----------------------------------------

ig    : internalGet     [boolean] []
    Return true if the attribute come from getCachedValue

-----------------------------------------

internalSet : internalSet     [boolean] []
    Return true if the attribute must be set through setCachedValue

-----------------------------------------

k     : keyable         [boolean] []
    Return the keyable status of the attribute

-----------------------------------------

lc    : listChildren    [boolean] []
    Return the list of children attributes of the given attribute.

-----------------------------------------

ld    : listDefault     [boolean] []
    Return the default values of numeric and compound numeric attributes.

-----------------------------------------

le    : listEnum        [boolean] []
    Return the list of enum strings for the given attribute.

-----------------------------------------

lp    : listParent      [boolean] []
    Return the parent of the given attribute.

-----------------------------------------

ls    : listSiblings    [boolean] []
    Return the list of sibling attributes of the given attribute.

-----------------------------------------

ln    : longName        [boolean] []
    Return the long name of the attribute.

-----------------------------------------

mxe   : maxExists       [boolean] []
    Return true if the attribute has a hard maximum. A min does not have to be present.

-----------------------------------------

max   : maximum         [boolean] []
    Return the hard maximum of the attribute's value

-----------------------------------------

msg   : message         [boolean] []
    Return true if the attribute is a message attribute

-----------------------------------------

mne   : minExists       [boolean] []
    Return true if the attribute has a hard minimum. A max does not have to be present.

-----------------------------------------

min   : minimum         [boolean] []
    Return the hard minimum of the attribute's value

-----------------------------------------

m     : multi           [boolean] []
    Return true if the attribute is a multi-attribute

-----------------------------------------

nn    : niceName        [boolean] []
    Return the nice name (or "UI name") of the attribute.

-----------------------------------------

n     : node            [name] []
    Use all attributes from node named NAME

-----------------------------------------

nc    : numberOfChildren [boolean] []
    Return the number of children the attribute has

-----------------------------------------

r     : range           [boolean] []
    Return the hard range of the attribute's value

-----------------------------------------

re    : rangeExists     [boolean] []
    Return true if the attribute has a hard range. Both min and max must be present.

-----------------------------------------

rd    : readable        [boolean] []
    Return the readable status of the attribute

-----------------------------------------

rs    : renderSource    [boolean] []
    Return whether this attribute is marked as a render source or not

-----------------------------------------

sn    : shortName       [boolean] []
    Return the short name of the attribute.

-----------------------------------------

smx   : softMax         [boolean] []
    Return the soft max (slider range) of the attribute's value

-----------------------------------------

sxe   : softMaxExists   [boolean] []
    Return true if the attribute has a soft maximum. A min does not have to be present.

-----------------------------------------

smn   : softMin         [boolean] []
    Return the soft min (slider range) of the attribute's value

-----------------------------------------

sme   : softMinExists   [boolean] []
    Return true if the attribute has a soft minimum. A max does not have to be present.

-----------------------------------------

s     : softRange       [boolean] []
    Return the soft range (slider range) of the attribute's value

-----------------------------------------

se    : softRangeExists [boolean] []
    Return true if the attribute has a soft range. Both min and max must be present.

-----------------------------------------

st    : storable        [boolean] []
    Return true if the attribute is storable

-----------------------------------------

typ   : type            [string] []
    Use static attributes from nodes of type TYPE. Includes attributes inherited from parent class nodes.

-----------------------------------------

tex   : typeExact       [string] []
    Use static attributes only from nodes of type TYPE. Does not included inherited attributes.

-----------------------------------------

uac   : usedAsColor     [boolean] []
    Return true if the attribute should bring up a color picker

-----------------------------------------

uaf   : usedAsFilename  [boolean] []
    Return true if the attribute should bring up a file browser

-----------------------------------------

umb   : usesMultiBuilder [boolean] []
    Return true if the attribute is a multi-attribute and it uses the multi- builder to handle its data

-----------------------------------------

ws    : worldspace      [boolean] []
    Return the status of the attribute flag marking worldspace attribute

-----------------------------------------

w     : writable        [boolean]
    Return the writable status of the attribute

    """

def connectAttr(f=1,l=1,na=1,rd="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/connectAttr.html



-----------------------------------------

connectAttr is undoable, NOT queryable, and NOT editable.

Connect the attributes of two dependency nodes and return the names of the two
connected attributes. The connected attributes must be be of compatible types.
First argument is the source attribute, second one is the destination.

Refer to dependency node documentation.


-----------------------------------------


Return Value:

string  A phrase containing the names of the connected attributes.


-----------------------------------------


Flags:

-----------------------------------------

f     : force           [boolean] []
    Forces the connection. If the destination is already connected, the old connection is broken and the new one made.

-----------------------------------------

l     : lock            [boolean] []
    If the argument is true, the destination attribute is locked after making the connection. If the argument is false, the connection is unlocked before making the connection.

-----------------------------------------

na    : nextAvailable   [boolean] []
    If the destination multi-attribute has set the indexMatters to be false with this flag specified, a connection is made to the next available index. No index need be specified.

-----------------------------------------

rd    : referenceDest   [string]
    This flag is used for file io only. The flag indicates that the connection replaces a connection made in a referenced file, and the flag argument indicates the original destination from the referenced file. This flag is used so that if the reference file is modified, maya can still attempt to make the appropriate connections in the main scene to the referenced object.

    """

def connectionInfo(dfs=1,ged=1,ges=1,gla=1,id=1,ied=1,ies=1,il=1,isSource=1,sfd=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/connectionInfo.html



-----------------------------------------

connectionInfo is undoable, NOT queryable, and NOT editable.

The connectionInfo command is used to get information about connection sources
and destinations. Unlike the isConnected command, this command needs only one
end of the connection.


-----------------------------------------


Return Value:

boolean  When asking for a property, depending on the flags used.    
string  When asking for a plug name.  
string[]  When asking for a list of plugs.


-----------------------------------------


Flags:

-----------------------------------------

dfs   : destinationFromSource [boolean] []
    If the specified plug (or its ancestor) is a source, this flag returns the list of destinations connected from the source. (array of strings, empty array if none)

-----------------------------------------

ged   : getExactDestination [boolean] []
    If the plug or its ancestor is connection destination, this returns the name of the plug that is the exact destination. (empty string if there is no such connection).

-----------------------------------------

ges   : getExactSource  [boolean] []
    If the plug or its ancestor is a connection source, this returns the name of the plug that is the exact source. (empty string if there is no such connection).

-----------------------------------------

gla   : getLockedAncestor [boolean] []
    If the specified plug is locked, its name is returned. If an ancestor of the plug is locked, its name is returned. If more than one ancestor is locked, only the name of the closest one is returned. If neither this plug nor any ancestors are locked, an empty string is returned.

-----------------------------------------

id    : isDestination   [boolean] []
    Returns true if the plug (or its ancestor) is the destination of a connection, false otherwise.

-----------------------------------------

ied   : isExactDestination [boolean] []
    Returns true if the plug is the exact destination of a connection, false otherwise.

-----------------------------------------

ies   : isExactSource   [boolean] []
    Returns true if the plug is the exact source of a connection, false otherwise.

-----------------------------------------

il    : isLocked        [boolean] []
    Returns true if this plug (or its ancestor) is locked

-----------------------------------------

isSource : isSource        [boolean] []
    Returns true if the plug (or its ancestor) is the source of a connection, false otherwise.

-----------------------------------------

sfd   : sourceFromDestination [boolean]
    If the specified plug (or its ancestor) is a destination, this flag returns the source of the connection. (string, empty if none)

    """

def copyAttr(q=1,e=1,at="string",cpc=1,ic=1,ksc=1,oc=1,rtc=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/copyAttr.html



-----------------------------------------

copyAttr is undoable, queryable, and editable.

Given two nodes, transfer the connections and/or the values from the first
node to the second for all attributes whose names and data types match. When
values are transferred, they are transferred directly. They are not mapped or
modified in any way. The transferAttributes command can be used to transfer
and remap some mesh attributes. The attributes flag can be used to specify a
list of attributes to be processed. If the attributes flag is unused, all
attributes will be processed. For dynamic attributes, the values and/or
connections will only be transferred if the attributes names on both nodes
match. This command does not support geometry shape nodes such as meshes,
subds and nurbs. This command does not support transfer of multi-attribute
values such as weight arrays.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.

-----------------------------------------

cpc   : containerParentChild [boolean] []
    For use when copying from one container to another only. This option indicates that the published parent and/or child relationships on the original container should be transferred to the target container if the published names match.

-----------------------------------------

ic    : inConnections   [boolean] []
    Indicates that incoming connections should be transferred.

-----------------------------------------

ksc   : keepSourceConnections [boolean] []
    For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out connections on the source node will be broken and made to the target node.

-----------------------------------------

oc    : outConnections  [boolean] []
    Indicates that outgoing connections should be transferred.

-----------------------------------------

rtc   : renameTargetContainer [boolean] []
    For use when copying from one container to another only. This option will rename the target container to the name of the original container, and rename the original container to its old name + "Orig". You would want to use this option if your original container was referenced and edited, and you want those edits from the main scene to now apply to the new container.

-----------------------------------------

v     : values          [boolean]
    Indicates that values should be transferred.

    """

def createAttrPatterns(pd="string",pf="string",pt="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/createAttrPatterns.html



-----------------------------------------

createAttrPatterns is undoable, NOT queryable, and NOT editable.

Create a new instance of an attribute pattern given a pattern type (e.g. XML)
and a string or data file containing the description of the attribute tree in
the pattern's format.


-----------------------------------------


Return Value:

string  Name of created pattern


-----------------------------------------


Flags:

-----------------------------------------

pd    : patternDefinition [string] []
    Hardcoded string containing the pattern definition, for simpler formats that don't really need a separate file for definition.

-----------------------------------------

pf    : patternFile     [string] []
    File where the pattern information can be found

-----------------------------------------

pt    : patternType     [string]
    Name of the pattern definition type to use in creating this instance of the pattern.

    """

def createNode(n="string",p="string",s=1,ss=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/createNode.html



-----------------------------------------

createNode is undoable, NOT queryable, and NOT editable.

This command creates a new node in the dependency graph of the specified type.


-----------------------------------------


Return Value:

string  The name of the new node.


-----------------------------------------


Flags:

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.

-----------------------------------------

p     : parent          [string] []
    Specifies the parent in the DAG under which the new node belongs.

-----------------------------------------

s     : shared          [boolean] []
    This node is shared across multiple files, so only create it if it does not already exist.

-----------------------------------------

ss    : skipSelect      [boolean]
    This node is not to be selected after creation, the original selection will be preserved.

    """

def cycleCheck(q=1,all=1,c=1,dag=1,evaluation=1,fco=1,fpn=1,lpn=1,l=1,ls="string",p=1,s=1,tl="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cycleCheck.html



-----------------------------------------

cycleCheck is undoable, queryable, and NOT editable.

This command searches for plug cycles in the dependency graph. If a plug or
node is selected then it searches for cycles that that plug or node is
involved with. Plugs or nodes can also be passed as arguments. If the -all
flag is used then the entire graph is searched.

Normally the return value is a boolean indicating whether or not the given
items were involved in a cycle. If the -list flag is used then the return
value is the list of all plugs in cycles (involving the selected plug or node
if any).

Note that it is possible for evaluation cycles to occur even where no DG
connections exist. Here are some examples:

1) Nodes with evaluation-time dependent connections: An example is expression
nodes, because we cannot tell what an expression node is actually referring to
until it is evaluated, and such evaluation-time dependent nodes may behave
differently based on the context (e.g. time) they are evaluated at. If you
suspect a cycle due to such a connection, the best way to detect the cycle is
through manual inspection.

2) Cycles due to DAG hierarchy: noting that DAG nodes are implicitely
connected through parenting, if a child DAG node connects an output into the
input of a parent node, a cycle will exist if the plugs involved also affect
each other. In order to enable detection of cycles involving the DAG, add the
-dag flag to the command line.

Note also that this command may incorrectly report a cycle on an instanced
skeleton where some of the instances use IK. You will have to examine the
reported cycle yourself to determine if it is truly a cycle or not. The
evaluation time cycle checking will not report false cycles.


-----------------------------------------


Return Value:

boolean  in the general case.    
string[]  When the list flag is used.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : all             [boolean] []
    search the entire graph for cycles instead of the selection list. (Note: if nothing is selected, -all is assumed).

-----------------------------------------

c     : children        [boolean] []
    Do not consider cycles on the children, only the specified plugs

-----------------------------------------

dag   : dag             [boolean] []
    Also look for cycles due to relationships in the DAG. For each DAG node, the parenting connection on its children is also considered when searching for cycles.

-----------------------------------------

e     : evaluation      [boolean] ['query']
    Turn on and off cycle detection during graph evaluation

-----------------------------------------

fco   : firstCycleOnly  [boolean] []
    When -list is used to return a plug list, the list may contain multiple cycles or partial cycles. When -firstCycleOnly is specified only the first such cycle (which will be a full cycle) is returned.

-----------------------------------------

fpn   : firstPlugPerNode [boolean] []
    When -list is used to return a plug list, the list will typically contain multiple plugs per node (e.g. ... A.output B.input B.output C.input ...), reflecting internal "affects" relationships rather than external DG connections. When -firstPlugPerNode is specified, only the first plug in the list for each node is returned (B.input in the example).

-----------------------------------------

lpn   : lastPlugPerNode [boolean] []
    When -list is used to return a plug list, the list will typically contain multiple plugs per node (e.g. ... A.output B.input B.output C.input ...), reflecting internal "affects" relationships rather than external DG connections. When -lastPlugPerNode is specified, only the last plug in the list for each node is returned (B.output in the example).

-----------------------------------------

l     : list            [boolean] []
    Return all plugs involved in one or more cycles. If not specified, returns a boolean indicating whether a cycle exists.

-----------------------------------------

ls    : listSeparator   [string] []
    When -list is used to return a plug list, the list may contain multiple cycles or partial cycles. Use -listSeparator to specify a string that will be inserted into the returned string array to separate the cycles.

-----------------------------------------

p     : parents         [boolean] []
    Do not consider cycles on the parents, only the specified plugs

-----------------------------------------

s     : secondary       [boolean] []
    Look for cycles on related plugs as well as the specified plugs Default is "on" for the "-all" case and "off" for others

-----------------------------------------

tl    : timeLimit       [time]
    Limit the search to the given amount of time

    """

def deleteAttr(q=1,e=1,at="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deleteAttr.html



-----------------------------------------

deleteAttr is undoable, queryable, and editable.

This command is used to delete a dynamic attribute from a node or nodes. The
attribute can be specified by using either the long or short name. Only one
dynamic attribute can be deleted at a time. Static attributes cannot be
deleted. Children of a compound attribute cannot be deleted. You must delete
the complete compound attribute. This command has no edit capabilities. The
only query ability is to list all the dynamic attributes of a node.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    Specify either the long or short name of the attribute.

-----------------------------------------

n     : name            [string]
    The name of the node.

    """

def deleteAttrPattern(all=1,pn="string",pt="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deleteAttrPattern.html



-----------------------------------------

deleteAttrPattern is undoable, NOT queryable, and NOT editable.

After a while the list of attribute patterns could become cluttered. This
command provides a way to remove patterns from memory so that only the ones of
interest will show.


-----------------------------------------


Return Value:

string  Name(s) of deleted pattern(s)


-----------------------------------------


Flags:

-----------------------------------------

all   : allPatterns     [boolean] []
    If specified it means delete all known attribute patterns.

-----------------------------------------

pn    : patternName     [string] []
    The name of the pattern to be deleted.

-----------------------------------------

pt    : patternType     [string]
    Delete all patterns of the given type.

    """

def deleteExtension(at="string",fd=1,nt="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deleteExtension.html



-----------------------------------------

deleteExtension is NOT undoable, NOT queryable, and NOT editable.

This command is used to delete an extension attribute from a node type. The
attribute can be specified by using either the long or short name. Only one
extension attribute can be deleted at a time. Children of a compound attribute
cannot be deleted, you must delete the complete compound attribute. This
command has no undo, edit, or query capabilities.


-----------------------------------------


Return Value:

int  Number of nodes with altered data after the delete


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    Specify either the long or short name of the attribute.

-----------------------------------------

fd    : forceDelete     [boolean] []
    If this flag is set and turned ON then data values for the extension attributes are all deleted without confirmation. If it's set and turned OFF then any extension attributes that have non-default values set on any node will remain in place. If this flag is not set at all then the user will be asked if they wish to preserve non-default values on this attribute.

-----------------------------------------

nt    : nodeType        [string]
    The name of the node type.

    """

def disconnectAttr(na=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/disconnectAttr.html



-----------------------------------------

disconnectAttr is undoable, NOT queryable, and NOT editable.

Disconnects two connected attributes. First argument is the source attribute,
second is the destination.


-----------------------------------------


Return Value:

string  A phrase containing the names of the disconnected attributes.


-----------------------------------------


Flags:

-----------------------------------------

na    : nextAvailable   [boolean]
    If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection. No index needs to be specified.

    """

def getAttr(asString=1,ca=1,cb=1,x=1,k=1,l=1,mi=1,se=1,sl=1,s=1,t="time",typ=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getAttr.html



-----------------------------------------

getAttr is undoable, NOT queryable, and NOT editable.

This command returns the value of the named object's attribute. UI units are
used where applicable. Currently, the types of attributes that can be
displayed are:

  * numeric attributes
  * string attributes
  * matrix attributes
  * numeric compound attributes (whose children are all numeric)
  * vector array attributes
  * double array attributes
  * int32 array attributes
  * point array attributes
  * data component list attributes

Other data types cannot be retrieved. No result is returned if the attribute
contains no data.


-----------------------------------------


Return Value:

Any  Value or state of the attribute. The number and type of values returned
is dependent on the attribute type.


-----------------------------------------


Flags:

-----------------------------------------

asString : asString        [boolean] []
    This flag is only valid for enum attributes. It allows you to get the attribute values as strings instead of integer values. Note that the returned string value is dependent on the UI language Maya is running in (about -uiLanguage).

-----------------------------------------

ca    : caching         [boolean] []
    Returns whether the attribute is set to be cached internally

-----------------------------------------

cb    : channelBox      [boolean] []
    Returns whether the attribute is set to show in the channelBox. Keyable attributes also show in the channel box.

-----------------------------------------

x     : expandEnvironmentVariables [boolean] []
    Expand any environment variable and (tilde characters on UNIX) found in string attributes which are returned.

-----------------------------------------

k     : keyable         [boolean] []
    Returns the keyable state of the attribute.

-----------------------------------------

l     : lock            [boolean] []
    Returns the lock state of the attribute.

-----------------------------------------

mi    : multiIndices    [boolean] []
    If the attribute is a multi, this will return a list containing all of the valid indices for the attribute.

-----------------------------------------

se    : settable        [boolean] []
    Returns 1 if this attribute is currently settable by setAttr, 0 otherwise. An attribute is settable if it's not locked and either not connected, or has only keyframed animation.

-----------------------------------------

sl    : silent          [boolean] []
    When evaluating an attribute that is not a numeric or string value, suppress the error message saying that the data cannot be displayed. The attribute will be evaluated even though its data cannot be displayed. This flag does not suppress all error messages, only those that are benign.

-----------------------------------------

s     : size            [boolean] []
    Returns the size of a multi-attribute array. Returns 1 if non-multi.

-----------------------------------------

t     : time            [time] []
    Evaluate the attribute at the given time instead of the current time.

-----------------------------------------

typ   : type            [boolean]
    Returns the type of data currently in the attribute.  Attributes of simple types such as strings and numerics always contain data, but attributes of complex types (arrays, meshes, etc) may contain no data if none has ever been assigned to them. When this happens the command will return with no result: not an empty string, but no result at all. Attempting to directly compare this non-result to another value or use it in an expression will result in an error, but you can assign it to a variable in which case the variable will be set to the default value for its type (e.g. an empty string for a string variable, zero for an integer variable, an empty array for an array variable). So to be safe when using this flag, always assign its result to a string variable, never try to use it directly.

    """

def getClassification(sat="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getClassification.html



-----------------------------------------

getClassification is undoable, NOT queryable, and NOT editable.

Returns the classification string for a given node type.

Classification strings look like file pathnames ("shader/reflective" or
"texture/2D", for example). Multiple classifications can be combined into a
single compound classification string by joining the individual
classifications with ':'. For example, the classification string
"shader/reflective:texture/2D" means that the node is both a reflective shader
and a 2D texture.

The classification string is used to determine how rendering nodes are
categorized in various UI, such as the Create Render Node and HyperShade
windows:

Category| Classification String  
---|---  
2D Textures| "texture/2d"  
3D Textures| "texture/3d"  
Env Textures| "texture/environment"  
Surface Materials| "shader/surface"  
Volumetric Materials| "shader/volume"  
Displacement Materials| "shader/displacement"  
Lights| "light"  
General Utilities| "utility/general"  
Color Utilities| "utility/color  
Particle Utilities| "utility/particle"  
Image Planes| "imageplane"  
Glow| "postprocess/opticalFX"  
  
The classification string is also used to determine how Viewport 2.0 will
interpret the node.

Category| Classification String  
---|---  
Geometry| "drawdb/geometry"  
Transform| "drawdb/geometry/transform"  
Sub-Scene Object| "drawdb/subscene"  
Shader| "drawdb/shader"  
Surface Shader| "drawdb/shader/surface"


-----------------------------------------


Return Value:

string[]  Returns the classification strings for the given node type, or an
empty array if the node type is not classified.


-----------------------------------------


Flags:

-----------------------------------------

sat   : satisfies       [string]
    Returns true if the given node type's classification satisfies the classification string which is passed with the flag.  A non-compound classification string A is said to satisfy a non-compound classification string B if A is a subclassification of B (for example, "shaders/reflective" satisfies "shaders").  A compound classification string A satisfies a compound classification string B iff:    1. every component of A satisfies at least one component of B and    2. every component of B is satisfied by at least one component of A  Hence, "shader/reflective/phong:texture" satisfies "shader:texture", but "shader/reflective/phong" does not satisfy "shader:texture".

    """

def inheritTransform(q=1,off=1,on=1,p=1,tgl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/inheritTransform.html



-----------------------------------------

inheritTransform is undoable, queryable, and NOT editable.

This command toggles the inherit state of an object. If this flag is off the
object will not inherit transformations from its parent. In other words
transformations applied to the parent node will not affect the object and it
will act as though it is under the world.

If the -p flag is specified then the object's transformation will be modified
to compensate when changing the inherit flag so the object will not change its
world-space location.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

off   : off             [boolean] ['query']
    turn off inherit state for the given object(s)

-----------------------------------------

on    : on              [boolean] ['query']
    turn on inherit state for the given object(s)

-----------------------------------------

p     : preserve        [boolean] ['query']
    preserve the objects world-space position by modifying the object(s) transformation matrix.

-----------------------------------------

tgl   : toggle          [boolean]
    toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)

    """

def isConnected(iuc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/isConnected.html



-----------------------------------------

isConnected is undoable, NOT queryable, and NOT editable.

The isConnected command is used to check if two plugs are connected in the
dependency graph. The return value is false if they are not and true if they
are.

  
The first string specifies the source plug to check for connection.  
The second one specifies the destination plug to check for connection.


-----------------------------------------


Return Value:

boolean  Are the two plugs connected?


-----------------------------------------


Flags:

-----------------------------------------

iuc   : ignoreUnitConversion [boolean]
    In looking for connections, skip past unit conversion nodes.

    """

def isDirty(c=1,d=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/isDirty.html



-----------------------------------------

isDirty is undoable, NOT queryable, and NOT editable.

The isDirty command is used to check if a plug is dirty. The return value is 0
if it is not and 1 if it is. If more than one plug is specified then the
result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs
are dirty).


-----------------------------------------


Return Value:

boolean  Is the plug dirty? If more than one plug is given then it returns the
logical "and" of all dirty states.


-----------------------------------------


Flags:

-----------------------------------------

c     : connection      [boolean] []
    Check the connection of the plug (default).

-----------------------------------------

d     : datablock       [boolean]
    Check the datablock entry for the plug.

    """

def listAttr(a=1,ca=1,ct="string",cfo=1,cb=1,c=1,ex=1,fp=1,hd=1,hnd=1,iu=1,k=1,lf=1,l=1,m=1,o=1,ra=1,r=1,ro=1,s=1,sa=1,se=1,sn=1,st="string",u=1,uf=1,ud=1,v=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listAttr.html



-----------------------------------------

listAttr is undoable, NOT queryable, and NOT editable.

This command lists the attributes of a node. If no flags are specified all
attributes are listed.


-----------------------------------------


Return Value:

string[]  : List of attributes matching criteria


-----------------------------------------


Flags:

-----------------------------------------

a     : array           [boolean] []
    only list array (not multi) attributes

-----------------------------------------

ca    : caching         [boolean] []
    only show attributes that are cached internally

-----------------------------------------

ct    : category        [string] []
    only show attributes belonging to the given category. Category string can be a regular expression.

-----------------------------------------

cfo   : changedSinceFileOpen [boolean] []
    Only list the attributes that have been changed since the file they came from was opened. Typically useful only for objects/attributes coming from referenced files.

-----------------------------------------

cb    : channelBox      [boolean] []
    only show non-keyable attributes that appear in the channelbox

-----------------------------------------

c     : connectable     [boolean] []
    only show connectable attributes

-----------------------------------------

ex    : extension       [boolean] []
    list user-defined attributes for all nodes of this type (extension attributes)

-----------------------------------------

fp    : fromPlugin      [boolean] []
    only show attributes that were created by a plugin

-----------------------------------------

hd    : hasData         [boolean] []
    list only attributes that have data (all attributes except for message attributes)

-----------------------------------------

hnd   : hasNullData     [boolean] []
    list only attributes that have null data. This will list all attributes that have data (see hasData flag) but the data value is uninitialized. A common example where an attribute may have null data is when a string attribute is created but not yet assigned an initial value. Similarly array attribute data is often null until it is initialized.

-----------------------------------------

iu    : inUse           [boolean] []
    only show attributes that are currently marked as in use. This flag indicates that an attribute affects the scene data in some way. For example it has a non-default value or it is connected to another attribute. This is the general concept though the precise implementation is subject to change.

-----------------------------------------

k     : keyable         [boolean] []
    only show attributes that can be keyframed

-----------------------------------------

lf    : leaf            [boolean] []
    Only list the leaf-level name of the attribute. controlPoints[44].xValue would be listed as "xValue".

-----------------------------------------

l     : locked          [boolean] []
    list only attributes which are locked

-----------------------------------------

m     : multi           [boolean] []
    list each currently existing element of a multi-attribute

-----------------------------------------

o     : output          [boolean] []
    List only the attributes which are numeric or which are compounds of numeric attributes.

-----------------------------------------

ra    : ramp            [boolean] []
    list only attributes which are ramps

-----------------------------------------

r     : read            [boolean] []
    list only attributes which are readable

-----------------------------------------

ro    : readOnly        [boolean] []
    List only the attributes which are readable and not writable.

-----------------------------------------

s     : scalar          [boolean] []
    only list scalar numerical attributes

-----------------------------------------

sa    : scalarAndArray  [boolean] []
    only list scalar and array attributes

-----------------------------------------

se    : settable        [boolean] []
    list attribute which are settable

-----------------------------------------

sn    : shortNames      [boolean] []
    list short attribute names (default is to list long names)

-----------------------------------------

st    : string          [string] []
    List only the attributes that match the other criteria AND match the string(s) passed from this flag. String can be a regular expression.

-----------------------------------------

u     : unlocked        [boolean] []
    list only attributes which are unlocked

-----------------------------------------

uf    : usedAsFilename  [boolean] []
    list only attributes which are designated to be treated as filenames

-----------------------------------------

ud    : userDefined     [boolean] []
    list user-defined (dynamic) attributes

-----------------------------------------

v     : visible         [boolean] []
    only show visible or non-hidden attributes

-----------------------------------------

w     : write           [boolean]
    list only attributes which are writable

    """

def listAttrPatterns(pt=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listAttrPatterns.html



-----------------------------------------

listAttrPatterns is NOT undoable, NOT queryable, and NOT editable.

Attribute patterns are plain text descriptions of an entire Maya attribute
forest. ("forest" because there could be an arbitrary number of root level
attributes, it's not restricted to having a single common parent though in
general that practice is a good idea.) This command lists the various pattern
types available, usually created via plugin, as well as any specific patterns
that have already been instantiated. A pattern type is a thing that knows how
to take some textual description of an attribute tree, e.g. XML or plaintext,
and convert it into an attribute pattern that can be applied to any node or
node type in Maya.


-----------------------------------------


Return Value:

string[]  List of patterns or pattern instances available


-----------------------------------------


Flags:

-----------------------------------------

pt    : patternType     [boolean] []
    If turned on then show the list of pattern types rather than actual instantiated patterns.

-----------------------------------------

v     : verbose         [boolean]
    If turned on then show detailed information about the patterns or pattern types. The same list of instance or pattern names is returned as for the non-verbose case.

    """

def listConnections(c=1,d=1,et=1,p=1,sh=1,scn=1,s=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listConnections.html



-----------------------------------------

listConnections is NOT undoable, NOT queryable, and NOT editable.

This command returns a list of all attributes/objects of a specified type that
are connected to the given object(s). If no objects are specified then the
command lists the connections on selected nodes.


-----------------------------------------


Return Value:

string[]  List of connection plugs/nodes


-----------------------------------------


Flags:

-----------------------------------------

c     : connections     [boolean] []
    If true, return both attributes involved in the connection. The one on the specified object is given first. Default false.

-----------------------------------------

d     : destination     [boolean] []
    Give the attributes/objects that are on the "destination" side of connection to the given object. Default true.

-----------------------------------------

et    : exactType       [boolean] []
    When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.

-----------------------------------------

p     : plugs           [boolean] []
    If true, return the connected attribute names; if false, return the connected object names only. Default false;

-----------------------------------------

sh    : shapes          [boolean] []
    Actually return the shape name instead of the transform when the shape is "selected". Default false.

-----------------------------------------

scn   : skipConversionNodes [boolean] []
    If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side. Default false.

-----------------------------------------

s     : source          [boolean] []
    Give the attributes/objects that are on the "source" side of connection to the given object. Default true.

-----------------------------------------

t     : type            [string]
    If specified, only take objects of a specified type.

    """

def listHistory(q=1,ac=1,af=1,ag=1,bf=1,f=1,fl=1,fw=1,gl=1,ha=1,il="int",lf=1,lv="uint",pdo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listHistory.html



-----------------------------------------

listHistory is undoable, queryable, and NOT editable.

This command traverses backwards or forwards in the graph from the specified
node and returns all of the nodes whose construction history it passes
through. The construction history consists of connections to specific
attributes of a node defined as the creators and results of the node's main
data, eg. the curve for a Nurbs Curve node.

For information on history connections through specific plugs use the
"listConnections" command first to find where the history begins then use this
command on the resulting node.


-----------------------------------------


Return Value:

string[]  List of history nodes    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : allConnections  [boolean] []
    If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).

-----------------------------------------

af    : allFuture       [boolean] []
    If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data, and that plug is connected, only list the future history downstream from that connection.

-----------------------------------------

ag    : allGraphs       [boolean] []
    This flag is obsolete and has no effect.

-----------------------------------------

bf    : breadthFirst    [boolean] []
    The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow a complete path away from the node, then return to any other paths from the node. Default is depth first.

-----------------------------------------

f     : future          [boolean] []
    List the future instead of the history.

-----------------------------------------

fl    : futureLocalAttr [boolean] ['query']
    This flag allows querying of the local-space future-related attribute(s) on shape nodes.

-----------------------------------------

fw    : futureWorldAttr [boolean] ['query']
    This flag allows querying of the world-space future-related attribute(s) on shape nodes.

-----------------------------------------

gl    : groupLevels     [boolean] []
    The node names are grouped depending on the level. > 1 is the lead, the rest are grouped with it.

-----------------------------------------

ha    : historyAttr     [boolean] ['query']
    This flag allows querying of the attribute where history connects on shape nodes.

-----------------------------------------

il    : interestLevel   [int] []
    If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed. The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers. 1 for the TDs, 2 for the users.

-----------------------------------------

lf    : leaf            [boolean] []
    If transform is selected, show history for its leaf shape. Default is true.

-----------------------------------------

lv    : levels          [uint] []
    Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.

-----------------------------------------

pdo   : pruneDagObjects [boolean]
    If this flag is set, prune at dag objects.

    """

def listNodeTypes(ex="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listNodeTypes.html



-----------------------------------------

listNodeTypes is undoable, NOT queryable, and NOT editable.

Lists dependency node types satisfying a specified classification string.

See the 'getClassification' command for a list of the standard classification
strings.


-----------------------------------------


Return Value:

string[]  The type names of all node types in the system that satisfy the
given classification string.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exclude         [string]
    Nodes that satisfies this exclude classification will be filtered out.

    """

def listRelatives(ad=1,ap=1,c=1,f=1,ni=1,p=1,pa=1,s=1,typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listRelatives.html



-----------------------------------------

listRelatives is undoable, NOT queryable, and NOT editable.

This command lists parents and children of DAG objects. The flags -c/children,
-ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually
exclusive. Only one can be used in a command.

When listing parents of objects directly under the world, the command will
return an empty parent list. Listing parents of objects directly under a shape
(underworld objects) will return their containing shape node in the list of
parents. Listing parents of components of objects will return the object.

When listing children, shape nodes will return their underworld objects in the
list of children. Listing children of components of objects returns nothing.

The -ni/noIntermediate flag works with the -s/shapes flag. It causes any
intermediate shapes among the descendents to be ignored.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

ad    : allDescendents  [boolean] []
    Returns all the children, grand-children etc. of this dag node. If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before children.

-----------------------------------------

ap    : allParents      [boolean] []
    Returns all the parents of this dag node. Normally, this command only returns the parent corresponding to the first instance of the object

-----------------------------------------

c     : children        [boolean] []
    List all the children of this dag node (default).

-----------------------------------------

f     : fullPath        [boolean] []
    Return full pathnames instead of object names.

-----------------------------------------

ni    : noIntermediate  [boolean] []
    No intermediate objects

-----------------------------------------

p     : parent          [boolean] []
    Returns the parent of this dag node

-----------------------------------------

pa    : path            [boolean] []
    Return a proper object name that can be passed to other commands.

-----------------------------------------

s     : shapes          [boolean] []
    List all the children of this dag node that are shapes (ie, not transforms)

-----------------------------------------

typ   : type            [string]
    List all relatives of the specified type.

    """

def nodeCast(cda=1,dsa=1,dsj=1,dua=1,f=1,sn=1,sv=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nodeCast.html



-----------------------------------------

nodeCast is undoable, NOT queryable, and NOT editable.

Given two nodes, a source node of type A and a target node of type B, where
type A is either type B or a sub-type of B, this command will replace the
target node with the source node. That is, all node connections, DAG hierarchy
and attribute values on the target node will be removed from the target node
and placed on the source node. This operation will fail if either object is
referenced, locked or if the nodes do not share a common sub-type. This
operation is atomic. If the given parameters fail, then the source and target
nodes will remain in their initial state prior to execution of the command.
IMPORTANT: the command will currently ignore instance connections and instance
objects. It will also ignore reference nodes.


-----------------------------------------


Return Value:

int  0 for success, 1 for failure.


-----------------------------------------


Flags:

-----------------------------------------

cda   : copyDynamicAttrs [boolean] []
    If the target node contains any dynamic attributes that are not defined on the source node, then create identical dynamic attricutes on the source node and copy the values and connections from the target node into them.

-----------------------------------------

dsa   : disableAPICallbacks [boolean] []
    add comment

-----------------------------------------

dsj   : disableScriptJobCallbacks [boolean] []
    add comment

-----------------------------------------

dua   : disconnectUnmatchedAttrs [boolean] []
    If the node that is being swapped out has any connections that do not exist on the target node, then indicate if the connection should be disconnected. By default these connections are not removed because they cannot be restored if the target node is swapped back with the source node.

-----------------------------------------

f     : force           [boolean] []
    Forces the command to do the node cast operation even if the nodes do not share a common base object. When this flag is specified the command will try to do the best possible attribute matching when swapping the command. It is not recommended to use the '-swapValues/sv' flag with this flag.

-----------------------------------------

sn    : swapNames       [boolean] []
    Swap the names of the nodes. By default names are not swapped.

-----------------------------------------

sv    : swapValues      [boolean]
    Indicates if the commands should exchange attributes on the common attributes between the two nodes. For example, if the nodes are the same base type as a transform node, then rotate, scale, translate values would be copied over.

    """

def nodeType(api=1,d=1,i=1,itn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nodeType.html



-----------------------------------------

nodeType is undoable, NOT queryable, and NOT editable.

This command returns a string which identifies the given node's type.

When no flags are used, the unique type name is returned. This can be useful
for seeing if two nodes are of the same type.

When the api flag is used, the MFn::Type of the node is returned. This can be
useful for seeing if a plug-in node belongs to a given class. The api flag
cannot be used in conjunction with any other flags.

When the derived flag is used, the command returns a string array containing
the names of all the currently known node types which derive from the node
type of the given object.

When the inherited flag is used, the command returns a string array containing
the names of all the base node types inherited by the the given node.

If the isTypeName flag is present then the argument provided to the command is
taken to be the name of a node type rather than the name of a specific node.
This makes it possible to query the hierarchy of node types without needing to
have instances of each node type.


-----------------------------------------


Return Value:

string  Single command result    
string[]  Multiple command result


-----------------------------------------


Flags:

-----------------------------------------

api   : apiType         [boolean] []
    Return the MFn::Type value (as a string) corresponding to the given node. This is particularly useful when the given node is defined by a plug-in, since in this case, the MFn::Type value corresponds to the underlying proxy class.  This flag cannot be used in combination with any of the other flags.

-----------------------------------------

d     : derived         [boolean] []
    Return a string array containing the names of all the currently known node types which derive from the type of the specified node.

-----------------------------------------

i     : inherited       [boolean] []
    Return a string array containing the names of all the base node types inherited by the specified node.

-----------------------------------------

itn   : isTypeName      [boolean]
    If this flag is present, then the argument provided to the command is the name of a node type rather than the name of a specific node.

    """

def objectCenter(gl=1,l=1,x=1,y=1,z=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/objectCenter.html



-----------------------------------------

objectCenter is undoable, NOT queryable, and NOT editable.

This command returns the coordinates of the center of the bounding box of the
specified object. If one coordinate only is specified, it will be returned as
a float. If no coordinates are specified, an array of floats is returned,
containing x, y, and z. If you specify multiple coordinates, only one will be
returned.


-----------------------------------------


Return Value:

float[]  When the asking for the center (default).    
float  When asking for one coordinate only.


-----------------------------------------


Flags:

-----------------------------------------

gl    : gl              [boolean] []
    Return positional values in global coordinates (default).

-----------------------------------------

l     : local           [boolean] []
    Return positional values in local coordinates.

-----------------------------------------

x     : x               [boolean] []
    Return X value only

-----------------------------------------

y     : y               [boolean] []
    Return Y value only

-----------------------------------------

z     : z               [boolean]
    Return Z value only

    """

def objectType(isa="string",i="string",tgt="string",tpt="int",tt=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/objectType.html



-----------------------------------------

objectType is undoable, NOT queryable, and NOT editable.

This command returns the type of elements. Warning: This command is incomplete
and may not be supported by all object types.


-----------------------------------------


Return Value:

string  The type of the specified object    
boolean  For "isType": was the object of the specified type?


-----------------------------------------


Flags:

-----------------------------------------

isa   : isAType         [string] []
    Returns true if the object is the specified type or derives from an object that is of the specified type. This flag will only work with dependency nodes.

-----------------------------------------

i     : isType          [string] []
    Returns true if the object is exactly of the specified type. False otherwise.

-----------------------------------------

tgt   : tagFromType     [string] []
    Returns the type tag given a type name.

-----------------------------------------

tpt   : typeFromTag     [int] []
    Returns the type name given an integer type tag.

-----------------------------------------

tt    : typeTag         [boolean]
    Returns an integer tag that is unique for that object type. Not all object types will have tags. This is the unique 4-byte value that is used to identify nodes of a given type in the binary file format.

    """

def objExists():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/objExists.html



-----------------------------------------

objExists is undoable, NOT queryable, and NOT editable.

This command simply returns true or false depending on whether an object with
the given name exists.


-----------------------------------------


Return Value:

boolean  Command result
    """

def relationship(q=1,e=1,b=1,rd="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/relationship.html



-----------------------------------------

relationship is undoable, queryable, and editable.

This is primarily for use with file IO. Rather than write out the specific
attributes/connections required to maintain a relationship, a description of
the related nodes/plugs is written instead. The relationship must have an
owner node, and have a specific type. During file read, maya will make the
connections and/or set the data necessary to represent the realtionship in the
dependency graph.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : b               [boolean] ['query', 'edit']
    Break the specified relationship instead of creating it

-----------------------------------------

rd    : relationshipData [string]
    Provide relationship data to be used when creating the relationship.

    """

def removeMultiInstance(all=1,b=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/removeMultiInstance.html



-----------------------------------------

removeMultiInstance is undoable, NOT queryable, and NOT editable.

Removes a particular instance of a multiElement. This is only useful for input
attributes since outputs will get regenerated the next time the node gets
executed. This command will remove the instance and optionally break all
incoming and outgoing connections to that instance. If the connections are not
broken (with the -b true) flag, then the command will fail if connections
exist.


-----------------------------------------


Return Value:

boolean  (true if the instance was removed, false if something went wrong,
like the attribute is connected but -b true was not specified)


-----------------------------------------


Flags:

-----------------------------------------

all   : allChildren     [boolean] []
    If the argument is true, remove all children of the multi parent.

-----------------------------------------

b     : b               [boolean]
    If the argument is true, all connections to the attribute will be broken before the element is removed. If false, then the command will fail if the element is connected.

    """

def renameAttr():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renameAttr.html



-----------------------------------------

renameAttr is undoable, NOT queryable, and NOT editable.

Renames the given user-defined attribute to the name given in the string
argument. If the new name conflicts with an existing name then this command
will fail. Note that it is not legal to rename an attribute to the empty
string.


-----------------------------------------


Return Value:

string  The new name. When undone returns the original name.
    """

def setAttr(q=1,e=1,av=1,ca=1,ch="uint",cb=1,c=1,k=1,l=1,s="uint",typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setAttr.html



-----------------------------------------

setAttr is undoable, queryable, and editable.

Sets the value of a dependency node attribute. No value for the the attribute
is needed when the -l/-k/-s flags are used. The -type flag is only required
when setting a non-numeric attribute.

The following chart outlines the syntax of setAttr for non-numeric data types:

  * {TYPE} below means any number of values of type TYPE, separated by a space
  * [TYPE] means that the value of type TYPE is optional
  * A|B means that either of A or B may appear

In order to run its examples, first execute these commands to create the
sample attribute types:  

    
    
    sphere -n node;
    addAttr -ln short2Attr -at short2;
    addAttr -ln short2a -p short2Attr -at short;
    addAttr -ln short2b -p short2Attr -at short;
    addAttr -ln short3Attr -at short3;
    addAttr -ln short3a -p short3Attr -at short;
    addAttr -ln short3b -p short3Attr -at short;
    addAttr -ln short3c -p short3Attr -at short;
    addAttr -ln long2Attr -at long2;
    addAttr -ln long2a -p long2Attr -at long;
    addAttr -ln long2b -p long2Attr -at long;
    addAttr -ln long3Attr -at long3;
    addAttr -ln long3a -p long3Attr -at long;
    addAttr -ln long3b -p long3Attr -at long;
    addAttr -ln long3c -p long3Attr -at long;
    addAttr -ln float2Attr -at float2;
    addAttr -ln float2a -p float2Attr -at "float";
    addAttr -ln float2b -p float2Attr -at "float";
    addAttr -ln float3Attr -at float3;
    addAttr -ln float3a -p float3Attr -at "float";
    addAttr -ln float3b -p float3Attr -at "float";
    addAttr -ln float3c -p float3Attr -at "float";
    addAttr -ln double2Attr -at double2;
    addAttr -ln double2a -p double2Attr -at double;
    addAttr -ln double2b -p double2Attr -at double;
    addAttr -ln double3Attr -at double3;
    addAttr -ln double3a -p double3Attr -at double;
    addAttr -ln double3b -p double3Attr -at double;
    addAttr -ln double3c -p double3Attr -at double;
    addAttr -ln int32ArrayAttr -dt Int32Array;
    addAttr -ln doubleArrayAttr -dt doubleArray;
    addAttr -ln pointArrayAttr -dt pointArray;
    addAttr -ln vectorArrayAttr -dt vectorArray;
    addAttr -ln stringArrayAttr -dt stringArray;
    addAttr -ln stringAttr -dt "string";
    addAttr -ln matrixAttr -dt "matrix";
    addAttr -ln sphereAttr -dt sphere;
    addAttr -ln coneAttr -dt cone;
    addAttr -ln meshAttr -dt mesh;
    addAttr -ln latticeAttr -dt lattice;
    addAttr -ln spectrumRGBAttr -dt spectrumRGB;
    addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
    addAttr -ln componentListAttr -dt componentList;
    addAttr -ln attrAliasAttr -dt attributeAlias;
    addAttr -ln curveAttr -dt nurbsCurve;
    addAttr -ln surfaceAttr -dt nurbsSurface;
    addAttr -ln trimFaceAttr -dt nurbsTrimface;
    addAttr -ln polyFaceAttr -dt polyFaces;
    

-type short2 |  | Array of two short integers  
---  
Value Syntax | short short  
Value Meaning | value1 value2  
Mel Example | setAttr node.short2Attr -type short2 1 2;  
Python Example | cmds.setAttr('node.short2Attr',1,2,type='short2')  
  
-type short3 |  | Array of three short integers  
---  
Value Syntax | short short short  
Value Meaning | value1 value2 value3  
Mel Example | setAttr node.short3Attr -type short3 1 2 3;  
Python Example | cmds.setAttr('node.short3Attr',1,2,3,type='short3')  
  
-type long2 |  | Array of two long integers  
---  
Value Syntax | long long  
Value Meaning | value1 value2  
Mel Example | setAttr node.long2Attr -type long2 1000000 2000000;  
Python Example | cmds.setAttr('node.long2Attr',1000000,2000000,type='long2')  
  
-type long3 |  | Array of three long integers  
---  
Value Syntax | long long long  
Value Meaning | value1 value2 value3  
Mel Example | setAttr node.long3Attr -type long3 1000000 2000000 3000000;  
Python Example |
cmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')  
  
-type Int32Array |  | Variable length array of long integers  
---  
Value Syntax | int {int}  
Value Meaning | numberOfArrayValues {arrayValue}  
Mel Example | setAttr node.int32ArrayAttr -type Int32Array 2 12 75;  
Python Example |
cmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')  
  
-type float2 |  | Array of two floats  
---  
Value Syntax | float float  
Value Meaning | value1 value2  
Mel Example | setAttr node.float2Attr -type float2 1.1 2.2;  
Python Example | cmds.setAttr('node.float2Attr',1.1,2.2,type='float2')  
  
-type float3 |  | Array of three floats  
---  
Value Syntax | float float float  
Value Meaning | value1 value2 value3  
Mel Example | setAttr node.float3Attr -type float3 1.1 2.2 3.3;  
Python Example | cmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')  
  
-type double2 |  | Array of two doubles  
---  
Value Syntax | double double  
Value Meaning | value1 value2  
Mel Example | setAttr node.double2Attr -type double2 1.1 2.2;  
Python Example | cmds.setAttr('node.double2Attr',1.1,2.2,type='double2')  
  
-type double3 |  | Array of three doubles  
---  
Value Syntax | double double double  
Value Meaning | value1 value2 value3  
Mel Example | setAttr node.double3Attr -type double3 1.1 2.2 3.3;  
Python Example | cmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')  
  
-type doubleArray |  | Variable length array of doubles  
---  
Value Syntax | int {double}  
Value Meaning | numberOfArrayValues {arrayValue}  
Mel Example | setAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;  
Python Example | cmds.setAttr( "node.doubleArrayAttr", (2, 3.14159, 2.782,),
type="doubleArray")  
  
-type matrix |  | 4x4 matrix of doubles  
---  
Value Syntax | double double double double  
double double double double  
double double double double  
double double double double  
Value Meaning | row1col1 row1col2 row1col3 row1col4  
row2col1 row2col2 row2col3 row2col4  
row3col1 row3col2 row3col3 row3col4  
row4col1 row4col2 row4col3 row4col4  
Alternate Syntax | string double double double  
double double double  
integer  
double double double  
double double double  
double double double  
double double double  
double double double  
double double double  
double double double double  
double double double double  
double double double  
boolean  
Alternate Meaning | "xform" scaleX scaleY scaleZ  
rotateX rotateY rotateZ  
rotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)  
translateX translateY translateZ  
shearXY shearXZ shearYZ  
scalePivotX scalePivotY scalePivotZ  
scaleTranslationX scaleTranslationY scaleTranslationZ  
rotatePivotX rotatePivotY rotatePivotZ  
rotateTranslationX rotateTranslationY rotateTranslationZ  
rotateOrientW rotateOrientX rotateOrientY rotateOrientZ  
jointOrientW jointOrientX jointOrientY jointOrientZ  
inverseParentScaleX inverseParentScaleY inverseParentScaleZ  
compensateForParentScale  
Mel Example | setAttr node.matrixAttr -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2
3 4 1;  
setAttr node.matrixAttr -type "matrix" "xform" 1 1 1 0 0 0 0 2 3 4 0 0 0  
0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 false;  
Python Example |
cmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')  
cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),  
(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,type="matrix")  
  
-type pointArray |  | Variable length array of points  
---  
Value Syntax | int {double double double double}  
Value Meaning | numberOfArrayValues {xValue yValue zValue wValue}  
Mel Example | setAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2 1;  
Python Example |
cmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')  
  
-type vectorArray |  | Variable length array of vectors  
---  
Value Syntax | int {double double double}  
Value Meaning | numberOfArrayValues {xValue yValue zValue}  
Mel Example | setAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;  
Python Example |
cmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')  
  
-type "string" |  | Character string  
---  
Value Syntax | string  
Value Meaning | characterStringValue  
Mel Example | setAttr node.stringAttr -type "string" "blarg";  
Python Example | cmds.setAttr('node.stringAttr',"blarg",type="string")  
  
-type stringArray |  | Variable length array of strings  
---  
Value Syntax | int {string}  
Value Meaning | numberOfArrayValues {arrayValue}  
Mel Example | setAttr node.stringArrayAttr -type stringArray 3 "a" "b" "c";  
Python Example |
cmds.setAttr('node.stringArrayAttr',3,"a","b","c",type='stringArray')  
  
-type sphere |  | Sphere data  
---  
Value Syntax | double  
Value Meaning | sphereRadius  
Example | setAttr node.sphereAttr -type sphere 5.0;  
  
-type cone |  | Cone data  
---  
Value Syntax | double double  
Value Meaning | coneAngle coneCap  
Mel Example | setAttr node.coneAttr -type cone 45.0 5.0;  
Python Example | cmds.setAttr('node.coneAttr',45.0,5.0,type='cone')  
  
-type reflectanceRGB |  | Reflectance data  
---  
Value Syntax | double double double  
Value Meaning | redReflect greenReflect blueReflect  
Mel Example | setAttr node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5
0.1;  
Python Example |
cmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')  
  
-type spectrumRGB |  | Spectrum data  
---  
Value Syntax | double double double  
Value Meaning | redSpectrum greenSpectrum blueSpectrum  
Mel Example | setAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;  
Python Example |
cmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')  
  
-type componentList |  | Variable length array of components  
---  
Value Syntax | int {string}  
Value Meaning | numberOfComponents {componentName}  
Mel Example | setAttr node.componentListAttr -type componentList 3 cv[1]
cv[12] cv[3];  
Python Example |
cmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')  
  
-type attributeAlias |  | String alias data  
---  
Value Syntax | string string  
Value Meaning | newAlias currentName  
Mel Example | setAttr node.attrAliasAttr -type attributeAlias  
{"GoUp", "translateY", "GoLeft", "translateX"};  
Python Example | cmds.setAttr('node.attrAliasAttr',("GoUp", "translateY",  
"GoLeft", "translateX"),type='attributeAlias')  
  
-type nurbsCurve |  | NURBS curve data  
---  
Value Syntax | int int int bool int int {double}  
int {double double double}  
Value Meaning | degree spans form isRational dimension knotCount {knotValue}  
cvCount {xCVValue yCVValue [zCVValue] [wCVValue]}  
Mel Example | // degree is the degree of the curve(range 1-7)  
// spans is the number of spans  
// form is open (0), closed (1), periodic (2)  
// dimension is 2 or 3, depending on the dimension of the curve  
// isRational is true if the curve CVs contain a rational component  
// knotCount is the size of the knot list  
// knotValue is a single entry in the knot list  
// cvCount is the number of CVs in the curve  
// xCVValue,yCVValue,[zCVValue] [wCVValue] is a single CV.  
// zCVValue is only present when dimension is 3.  
// wCVValue is only present when isRational is true.  
//  
setAttr node.curveAttr -type nurbsCurve 3 1 0 no 3  
6 0 0 0 1 1 1  
4 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;  
  
-type nurbsSurface |  | NURBS surface data  
---  
Value Syntax | int int int int bool  
int {double}  
int {double}  
[string] int {double double double}  
Value Meaning | uDegree vDegree uForm vForm isRational  
uKnotCount {uKnotValue}  
vKnotCount {vKnotValue} ["TRIM"|"NOTRIM"] cvCount {xCVValue yCVValue zCVValue
[wCVValue]}  
Example | // uDegree is degree of the surface in U direction (range 1-7)  
// vDegree is degree of the surface in V direction (range 1-7)  
// uForm is open (0), closed (1), periodic (2) in U direction  
// vForm is open (0), closed (1), periodic (2) in V direction  
// isRational is true if the surface CVs contain a rational component  
// uKnotCount is the size of the U knot list  
// uKnotValue is a single entry in the U knot list  
// vKnotCount is the size of the V knot list  
// vKnotValue is a single entry in the V knot list  
// If "TRIM" is specified then additional trim information is expected  
// If "NOTRIM" is specified then the surface is not trimmed  
// cvCount is the number of CVs in the surface  
// xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.  
// zCVValue is only present when dimension is 3.  
// wCVValue is only present when isRational is true  
//  
setAttr node.surfaceAttr -type nurbsSurface 3 3 0 0 no  
6 0 0 0 1 1 1  
6 0 0 0 1 1 1  
16 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0  
-1 3 0 -1 1 0 -1 -1 0 -1 -3 0  
1 3 0 1 1 0 1 -1 0 1 -3 0  
3 3 0 3 1 0 3 -1 0 3 -3 0;  
  
-type nurbsTrimface |  | NURBS trim face data  
---  
Value Syntax | bool int {int {int {double bool bool} int {bool double}}}  
Value Meaning | flipNormal boundaryCount {boundaryType tedgeCountOnBoundary  
{splineCountOnEdge {edgeTolerance isEdgeReversed geometricContinuity}  
{splineCountOnPedge {isMonotone pedgeTolerance}}}  
Example | // flipNormal if true turns the surface inside out  
// boundaryCount: number of boundaries  
// boundaryType:  
// tedgeCountOnBoundary : number of edges in a boundary  
// splineCountOnEdge : number of splines in an edge in  
// edgeTolerance : tolerance used to build the 3d edge  
// isEdgeReversed : if true, the edge is backwards  
// geometricContinuity : if true, the edge is tangent continuous  
// splineCountOnPedge : number of splines in a 2d edge  
// isMonotone : if true, curvature is monotone  
// pedgeTolerance : tolerance for the 2d edge  
//  
  
  
-type polyFaces |  | Polygon face data  
---  
Value Syntax | {"f" int {int}}  
{"h" int {int}}  
{"mf" int {int}}  
{"mh" int {int}}  
{"mu" int int {int}}  
{"mc" int int {int}}  
Value Meaning | {"f" faceEdgeCount {edgeIdValue}}  
{"h" holeEdgeCount {edgeIdValue}}  
{"mf" faceUVCount {uvIdValue}}  
{"mh" holeUVCount {uvIdValue}}  
{"mu" uvSet faceUVCount {uvIdValue}}  
{"mc" colorIndex multiColorCount {colorIdValue}}  
  
Example | // This data type (polyFace) is meant to be used in file I/O  
// after setAttrs have been written out for vertex position  
// arrays, edge connectivity arrays (with corresponding start  
// and end vertex descriptions), texture coordinate arrays and  
// color arrays. The reason is that this data type references  
// all of its data through ids created by the former types.  
//  
// "f" specifies the ids of the edges making up a face -  
// negative value if the edge is reversed in the face  
// "h" specifies the ids of the edges making up a hole -  
// negative value if the edge is reversed in the face  
// "mf" specifies the ids of texture coordinates (uvs) for a face.  
// This data type is obsolete as of version 3.0. It is replaced by "mu".  
// "mh" specifies the ids of texture coordinates (uvs) for a hole  
// This data type is obsolete as of version 3.0. It is replaced by "mu".  
// "mu" The first argument refers to the uv set. This is a zero-based  
// integer number. The second argument refers to the number of vertices (n)  
// on the face which have valid uv values. The last n values are the uv  
// ids of the texture coordinates (uvs) for the face. These indices  
// are what used to be represented by the "mf" and "mh" specification.  
// There may be more than one "mu" specification, one for each unique uv set.  
// "mc" specifies the color index values for a face. The first argument  
// is color index. The second argument is the number of color ids to follow.  
// Rest of the arguments are color ids for the face.  
//  
setAttr node.polyFaceAttr -type polyFaces "f" 3 1 2 3 "mc" 0 4 0 1 2 3;  
  
-type mesh |  | Polygonal mesh  
---  
Value Syntax | {string [int {double double double}]}  
{string [int {double double double}]}  
[{string [int {double double}]}]  
{string [int {double double string}]}  
Value Meaning | "v" [vertexCount {vertexX vertexY vertexZ}]  
"vn" [normalCount {normalX normalY normalZ}]  
["vt" [uvCount {uValue vValue}]]  
"e" [edgeCount {startVertex endVertex "smooth"|"hard"}]  
  
Example | // "v" specifies the vertices of the polygonal mesh  
// "vn" specifies the normal of each vertex  
// "vt" is optional and specifies a U,V texture coordinate for each vertex  
// "e" specifies the edge connectivity information between vertices  
//  
setAttr node.meshAttr -type mesh "v" 3 0 0 0 0 1 0 0 0 1  
"vn" 3 1 0 0 1 0 0 1 0 0  
"vt" 3 0 0 0 1 1 0  
"e" 3 0 1 "hard" 1 2 "hard" 2 0 "hard";  
  
-type lattice |  | Lattice data  
---  
Value Syntax | int int int int {double double double}  
Value Meaning | sDivisionCount tDivisionCount uDivisionCount  
pointCount {pointX pointY pointZ}  
Example | // sDivisionCount is the horizontal lattice division count  
// tDivisionCount is the vertical lattice division count  
// uDivisionCount is the depth lattice division count  
// pointCount is the total number of lattice points  
// pointX,pointY,pointZ is one lattice point. The list is  
// specified varying first in S, then in T, last in U so the  
// first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)  
//  
setAttr node.latticeAttr -type lattice 2 5 2 20  
-2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -2  
2 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2  
-2 -2 2 2 -2 2 -2 -1 2 2 -1 2 -2 0 2  
2 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

av    : alteredValue    [boolean] []
    The value is only the current value, which may change in the next evalution (if the attribute has an incoming connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data overwritten during the first evaluation after a file is opened.

-----------------------------------------

ca    : caching         [boolean] []
    Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes that are not defined by default to be cached can be made caching. As well, multi attribute elements cannot be made caching. Caching also affects child attributes for compound attributes.

-----------------------------------------

ch    : capacityHint    [uint] []
    Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and the interpretation of the flag value varies per attribute. This flag is currently used by (node.attribute):    * mesh.face - hints the total number of elements in the face edge lists

-----------------------------------------

cb    : channelBox      [boolean] []
    Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox regardless of the channelBox settting.

-----------------------------------------

c     : clamp           [boolean] []
    For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of failing

-----------------------------------------

k     : keyable         [boolean] []
    Sets the attribute's keyable state on or off.

-----------------------------------------

l     : lock            [boolean] []
    Sets the attribute's lock state on or off.

-----------------------------------------

s     : size            [uint] []
    Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as possible.

-----------------------------------------

typ   : type            [string]
    Identifies the type of data. If the -type flag is not present, a numeric type is assumed.

    """

def currentUnit(q=1,a="string",f=1,l="string",t="string",ua=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/currentUnit.html



-----------------------------------------

currentUnit is undoable, queryable, and NOT editable.

This command allows you to change the units in which you will work in Maya.
There are three types of units: linear, angular and time.

The current unit affects how all commands in Maya interpret their numeric
values. For example, if the current linear unit is cm, then the command:

    
    
    move 5 -2 3;
    sphere -radius 4;
    

will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a
sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames
per second), then the command:

    
    
    currentTime 6;
    

will be interpreted as setting the current time to frame 6 in the Film unit,
which is 6/24 or 0.25 seconds.

You can always override the unit of a particular numeric value to a command be
specifying it one the command. For example, using the above examples:

    
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    

would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z,
create a sphere of radius 4 inches, and change the current time to 6 frames in
the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film)
unit.


-----------------------------------------


Return Value:

string  The new current unit that has been set    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [string] ['query']
    Set the current angular unit. Valid strings are:   [deg | degree | rad | radian]   When queried, returns a string which is the current angular unit

-----------------------------------------

f     : fullName        [boolean] ['query']
    A query only flag. When specified in conjunction with any of the -linear/-angle/-time flags, will return the long form of the unit. For example, mm and millimeter are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.

-----------------------------------------

l     : linear          [string] ['query']
    Set the current linear unit. Valid strings are:   [mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]   When queried, returns a string which is the current linear unit

-----------------------------------------

t     : time            [string] ['query']
    Set the current time unit. Valid strings are:   [hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]   When queried, returns a string which is the current time unit  Note that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:    * game: 15 fps   * film: 24 fps   * pal: 25 fps   * ntsc: 30 fps   * show: 48 fps   * palf: 50 fps   * ntscf: 60 fps

-----------------------------------------

ua    : updateAnimation [boolean]
    An edit only flag. When specified in conjunction with the -time flag indicates that times for keys are not updated. By default when the current time unit is changed, the times for keys are modified so that playback timing is preserved. For example a key set a frame 12film is changed to frame 15ntsc when the current time unit is changed to ntsc, since they both represent a key at a time of 0.5 seconds. Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.

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

def displayAffected(q=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displayAffected.html



-----------------------------------------

displayAffected is undoable, queryable, and NOT editable.

Turns on/off the special coloring of objects that are affected by the objects
that are currently in the selection list.

If one of the curves in a loft were selected and this feature were turned on,
then the lofted surface would be highlighted because it is affected by the
loft curve.


-----------------------------------------


Return Value:

int  Affected display count    
  
In query mode, return type is based on queried flag.
    """

def displayColor(q=1,a=1,c=1,d=1,l=1,qi="int",rf=1,rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displayColor.html



-----------------------------------------

displayColor is undoable, queryable, and NOT editable.

This command changes or queries the display color for anything in the
application that allows the user to set its color. The color is defined by a
color index into either the dormant or active color palette. These colors are
part of the UI and not part of the saved data for a model. This command is not
undoable.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : active          [boolean] []
    Specifies the color index applies to active color palette. name Specifies the name of color to change. index The color index for the color.

-----------------------------------------

c     : create          [boolean] []
    Creates a new display color which can be queried or set. If is used only when saving color preferences.

-----------------------------------------

d     : dormant         [boolean] []
    Specifies the color index applies to dormant color palette. If neither of the dormant or active flags is specified, dormant is the default.

-----------------------------------------

l     : list            [boolean] []
    Writes out a list of all color names and their value.

-----------------------------------------

qi    : queryIndex      [int] []
    Allows you to obtain a list of color names with the given color indices.

-----------------------------------------

rf    : resetToFactory  [boolean] []
    Resets all display colors to their factory defaults.

-----------------------------------------

rs    : resetToSaved    [boolean]
    Resets all display colors to their saved values.

    """

def displayCull(q=1,bfc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displayCull.html



-----------------------------------------

displayCull is undoable, queryable, and NOT editable.

This command is responsible for setting the display culling property of back
faces of surfaces.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bfc   : backFaceCulling [boolean]
    Enable/disable culling of back faces.

    """

def displayLevelOfDetail(q=1,lod=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displayLevelOfDetail.html



-----------------------------------------

displayLevelOfDetail is undoable, queryable, and NOT editable.

This command is responsible for setting the display level-of-detail for edit
refreshes. If enabled, objects will draw with lower detail based on their
distance from the camera. When disabled objects will display at full
resolution at all times. This is not an undoable command


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

lod   : levelOfDetail   [boolean]
    Enable/disable level of detail.

    """

def displayPref(q=1,aop=1,da=1,dgr=1,gf="[int, int, int]",mld="string",mhr=1,mtr="int",pet=1,roe=1,st=1,tdp=1,wsa="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displayPref.html



-----------------------------------------

displayPref is undoable, queryable, and NOT editable.

This command sets/queries the state of global display parameters.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aop   : activeObjectPivots [boolean] ['query']
    Sets the display state for drawing pivots for active objects.

-----------------------------------------

da    : displayAffected [boolean] ['query']
    Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be highlighted because it is affected by the loft curve.

-----------------------------------------

dgr   : displayGradient [boolean] ['query']
    Set whether to display the background using a colored gradient as opposed to a constant background color.

-----------------------------------------

gf    : ghostFrames     [[int, int, int]] ['query']
    Sets the ghosting frame preferences: steps before, steps after and step size.

-----------------------------------------

mld   : materialLoadingMode [string] ['query']
    Sets the material loading mode when loading the scene. Possible values for the string argument are "immediate", "deferred" and "parallel".

-----------------------------------------

mhr   : maxHardwareTextureResolution [boolean] ['query']
    Query the maximum allowable hardware texture resolution available on the current video card. This maximum can vary between different video cards and different operating systems.

-----------------------------------------

mtr   : maxTextureResolution [int] ['query']
    Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.

-----------------------------------------

pet   : purgeExistingTextures [boolean] []
    Purge any existing hardware textures. This will force a re-evaluation of hardware textures used for display, and thus may take some time to evaluate.

-----------------------------------------

roe   : regionOfEffect  [boolean] ['query']
    Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.

-----------------------------------------

st    : shadeTemplates  [boolean] ['query']
    Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.

-----------------------------------------

tdp   : textureDrawPixel [boolean] ['query']
    Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.

-----------------------------------------

wsa   : wireframeOnShadedActive [string]
    Sets the display state for drawing the wireframe on active shaded objects. Possible values for the string argument are "full", "reduced" and "none".

    """

def displayRGBColor(q=1,c=1,hsv=1,l=1,rf=1,rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displayRGBColor.html



-----------------------------------------

displayRGBColor is undoable, queryable, and NOT editable.

This command changes or queries the display color for anything in the
application that allows the user to set its color. These colors are part of
the UI and not part of the saved data for a model. This command is not
undoable.


-----------------------------------------


Return Value:

string  when the list flag is used, none otherwise    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : create          [boolean] []
    Creates a new RGB display color which can be queried or set. If is used only when saving color preferences. name Specifies the name of color to change.

-----------------------------------------

hsv   : hueSaturationValue [boolean] ['query']
    Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats. r g b The RGB values for the color. (Between 0-1)

-----------------------------------------

l     : list            [boolean] []
    Writes out a list of all RGB color names and their value.

-----------------------------------------

rf    : resetToFactory  [boolean] []
    Resets all the RGB display colors to their factory defaults.

-----------------------------------------

rs    : resetToSaved    [boolean]
    Resets all the RGB display colors to their saved values.

    """

def displaySmoothness(q=1,all=1,bn=1,dc=1,du="int",dv="int",f=1,hl=1,ps="int",pw="int",po="int",rt=1,su="int",sv="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displaySmoothness.html



-----------------------------------------

displaySmoothness is undoable, queryable, and NOT editable.

This command is responsible for setting the display smoothness of NURBS curves
and surfaces to either predefined or custom values. It also sets display modes
for smoothness such as hulls and the hull simplification factors. At present,
this command is NOT un-doable.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : all             [boolean] ['query']
    Change smoothness for all curves and surfaces

-----------------------------------------

bn    : boundary        [boolean] ['query']
    Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet

-----------------------------------------

dc    : defaultCreation [boolean] ['query']
    The default values at creation (applies only -du, -dv, -pw, -ps)

-----------------------------------------

du    : divisionsU      [int] ['query']
    Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].

-----------------------------------------

dv    : divisionsV      [int] ['query']
    Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].

-----------------------------------------

f     : full            [boolean] ['query']
    Display surface at full resolution - the default.

-----------------------------------------

hl    : hull            [boolean] ['query']
    Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.

-----------------------------------------

ps    : pointsShaded    [int] ['query']
    Number of points per surface span in shaded mode. The valid range of values is [1,64].

-----------------------------------------

pw    : pointsWire      [int] ['query']
    Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.

-----------------------------------------

po    : polygonObject   [int] ['query']
    Display the polygon objects with the given resolution

-----------------------------------------

rt    : renderTessellation [boolean] ['query']
    Display using render tesselation parameters when in shaded mode.

-----------------------------------------

su    : simplifyU       [int] ['query']
    Number of spans to skip in the U direction when in hull display mode.

-----------------------------------------

sv    : simplifyV       [int]
    Number of spans to skip in the V direction when in hull display mode.

    """

def displaySurface(q=1,flp=1,two=1,x=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displaySurface.html



-----------------------------------------

displaySurface is undoable, queryable, and NOT editable.

This command toggles display options on the specified or active surfaces.
Typically this command applies to NURBS or poly mesh surfaces and ignores
other type of objects.


-----------------------------------------


Return Value:

boolean  when in the query mode.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

flp   : flipNormals     [boolean] ['query']
    flip normal direction on the surface

-----------------------------------------

two   : twoSidedLighting [boolean] ['query']
    toggle if the surface should be considered two-sided. If it's single- sided, drawing and rendering may use single sided lighting and back face cull to improve performance.

-----------------------------------------

x     : xRay            [boolean]
    toggle X ray mode (make surface transparent)

    """

def hide(all=1,clh=1,cs=1,ic=1,rh=1,tv=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hide.html



-----------------------------------------

hide is undoable, NOT queryable, and NOT editable.

The hide command is used to make objects invisible. If no flags are used, the
objects specified, or the active objects if none are specified, will be made
invisible.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

all   : allObjects      [boolean] []
    Make everything invisible (top level objects).

-----------------------------------------

clh   : clearLastHidden [boolean] []
    Clear the last hidden list.

-----------------------------------------

cs    : clearSelection  [boolean] []
    Clear selection after the operation.

-----------------------------------------

ic    : invertComponents [boolean] []
    Hide components that are not specified.

-----------------------------------------

rh    : returnHidden    [boolean] []
    Hide objects, but also return list of hidden objects.

-----------------------------------------

tv    : testVisibility  [boolean]
    Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).

    """

def showHidden(a=1,all=1,b=1,lh=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/showHidden.html



-----------------------------------------

showHidden is undoable, NOT queryable, and NOT editable.

The showHidden command is used to make invisible objects visible. If no flags
are specified, only the objects given to the command will be made visible. If
a parent of an object is invisible, the object will still be invisible.
Invisibility is inherited. To ensure the object becomes visible, use the
-a/above flag. This forces all invisible ancestors of the object(s) to be
visible. If the -b/below flag is used, any invisible objects below the object
will be made visible. To make all objects visible, use the -all/allObjects
flag.

See also: hide


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : above           [boolean] []
    Make objects and all their invisible ancestors visible.

-----------------------------------------

all   : allObjects      [boolean] []
    Make all invisible objects visible.

-----------------------------------------

b     : below           [boolean] []
    Make objects and all their invisible descendants visible.

-----------------------------------------

lh    : lastHidden      [boolean]
    Show everything that was hidden with the last hide command.

    """

def timeCode(q=1,e=1,msf="float",psf="float",psh="float",psm="float",pss="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timeCode.html



-----------------------------------------

timeCode is undoable, queryable, and editable.

Use this command to query and set the time code information in the file


-----------------------------------------


Return Value:

time  values    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

msf   : mayaStartFrame  [float] ['query', 'edit']
    Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.

-----------------------------------------

psf   : productionStartFrame [float] ['query', 'edit']
    Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.

-----------------------------------------

psh   : productionStartHour [float] ['query', 'edit']
    Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.

-----------------------------------------

psm   : productionStartMinute [float] ['query', 'edit']
    Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.

-----------------------------------------

pss   : productionStartSecond [float]
    Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.

    """

def toggle(q=1,a=1,b=1,bn=1,box=1,cv=1,dnw=1,ep=1,et=1,f=1,g=1,gl=1,hpn=1,hl=1,lp=1,ls=1,la=1,nc=1,np=1,ns=1,nr=1,o=1,pt=1,pd=1,pf=1,rp=1,sp=1,sh=1,st=1,sf=1,te=1,uv=1,vt=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/toggle.html



-----------------------------------------

toggle is undoable, queryable, and NOT editable.

The toggle command is used to toggle the display of various object features
for objects which have these components. For example, CV and edit point
display may be toggled for those listed NURB curves or surfaces.

Note: This command is not undoable.


-----------------------------------------


Return Value:

boolean  when in the query mode. none otherwise.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : above           [boolean] []
    Toggle state for all objects above listed objects.

-----------------------------------------

b     : below           [boolean] []
    Toggle state for all objects below listed objects.

-----------------------------------------

bn    : boundary        [boolean] ['query']
    Toggle boundary display of listed mesh objects.

-----------------------------------------

box   : boundingBox     [boolean] ['query']
    Toggle or query the bounding box display of listed objects.

-----------------------------------------

cv    : controlVertex   [boolean] ['query']
    Toggle CV display of listed curves and surfaces.

-----------------------------------------

dnw   : doNotWrite      [boolean] ['query']
    Toggle the "this should be written to the file" state.

-----------------------------------------

ep    : editPoint       [boolean] ['query']
    Toggle edit point display of listed curves and surfaces.

-----------------------------------------

et    : extent          [boolean] ['query']
    Toggle display of extents of listed mesh objects.

-----------------------------------------

f     : facet           [boolean] ['query']
    For use with normal flag. Set the normal display style to facet display.

-----------------------------------------

g     : geometry        [boolean] ['query']
    Toggle geometry display of listed objects.

-----------------------------------------

gl    : gl              [boolean] []
    Toggle state for all objects

-----------------------------------------

hpn   : highPrecisionNurbs [boolean] ['query']
    Toggle high precision display for Nurbs

-----------------------------------------

hl    : hull            [boolean] ['query']
    Toggle hull display of listed curves and surfaces.

-----------------------------------------

lp    : latticePoint    [boolean] ['query']
    Toggle point display of listed lattices

-----------------------------------------

ls    : latticeShape    [boolean] ['query']
    Toggle display of listed lattices

-----------------------------------------

la    : localAxis       [boolean] ['query']
    Toggle local axis display of listed objects.

-----------------------------------------

nc    : newCurve        [boolean] ['query']
    Set component display state of new curve objects

-----------------------------------------

np    : newPolymesh     [boolean] ['query']
    Set component display state of new polymesh objects

-----------------------------------------

ns    : newSurface      [boolean] ['query']
    Set component display state of new surface objects

-----------------------------------------

nr    : normal          [boolean] ['query']
    Toggle display of normals of listed surface and mesh objects.

-----------------------------------------

o     : origin          [boolean] ['query']
    Toggle origin display of listed surfaces.

-----------------------------------------

pt    : point           [boolean] ['query']
    For use with normal flag. Set the normal display style to vertex display.

-----------------------------------------

pd    : pointDisplay    [boolean] ['query']
    Toggle point display of listed surfaces.

-----------------------------------------

pf    : pointFacet      [boolean] ['query']
    For use with normal flag. Set the normal display style to vertex and face display.

-----------------------------------------

rp    : rotatePivot     [boolean] ['query']
    Toggle rotate pivot display of listed objects.

-----------------------------------------

sp    : scalePivot      [boolean] ['query']
    Toggle scale pivot display of listed objects.

-----------------------------------------

sh    : selectHandle    [boolean] ['query']
    Toggle select handle display of listed objects.

-----------------------------------------

st    : state           [boolean] []
    Explicitly set the state to true or false instead of toggling the state. Can not be queried.

-----------------------------------------

sf    : surfaceFace     [boolean] ['query']
    Toggle surface face handle display of listed surfaces.

-----------------------------------------

te    : template        [boolean] ['query']
    Toggle template state of listed objects

-----------------------------------------

uv    : uvCoords        [boolean] ['query']
    Toggle display uv coords of listed mesh objects.

-----------------------------------------

vt    : vertex          [boolean]
    Toggle vertex display of listed mesh objects.

    """

def toggleDisplacement():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/toggleDisplacement.html



-----------------------------------------

toggleDisplacement is undoable, NOT queryable, and NOT editable.

This command toggles the displacement preview of the polygon. This command is
NOT un-doable.


-----------------------------------------


Return Value:

None
    """

def expandedSelection(d="uint",et="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/expandedSelection.html



-----------------------------------------

expandedSelection is NOT undoable, NOT queryable, and NOT editable.

Examines the current selection list and returns that list, expanded to meet
certain criteria. See the command flags for the exact criteria that will be
used.


-----------------------------------------


Return Value:

string  List of objects in the requested selection list expansion    
string[]  List of nodes visited in the DG expansion  
string[]  (Python only) List of single nodes and tuples visited in the EG or
SG expansion, where tuples represent the DG nodes in a cluster


-----------------------------------------


Flags:

-----------------------------------------

d     : depth           [uint] []
    Number of steps away from current selection to expand to. A value of 0 will not expand the selection at all.

-----------------------------------------

et    : expansionType   [string]
    The type of graph along which to expand the selection. Legal values are:    * DG : Use the normal DG connections   * EG : Use the evaluation graph connections   * SG : Use the scheduling graph connections within the evaluation graph  If the actual selected node is not included in the graph being expanded on, e.g. there is no evaluation node when using the EG type, then the selected node will not appear in the output. If this flag is not specified then the type defaults to DG.

    """

def hilite(r=1,tgl=1,u=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hilite.html



-----------------------------------------

hilite is undoable, NOT queryable, and NOT editable.

Hilites/Unhilites the specified object(s). Hiliting an object makes it
possible to select the components of the object. If no objects are specified
then the selection list is used.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

r     : replace         [boolean] []
    Hilite the specified objects. Any objects previously hilited will no longer be hilited.

-----------------------------------------

tgl   : toggle          [boolean] []
    Toggle the hilite state of the specified objects.

-----------------------------------------

u     : unHilite        [boolean]
    Remove the specified objects from the hilite list.

    """

def isolateSelect(q=1,ado="name",addSelected=1,aso=1,ls=1,rdo="name",rs=1,s=1,u=1,vo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/isolateSelect.html



-----------------------------------------

isolateSelect is undoable, queryable, and NOT editable.

This command turns on/off isolate select mode in a specified modeling view,
specified as the argument. Isolate select mode is a display mode where the
currently selected objects are added to a list and only those objects are
displayed in the view. It allows for selective viewing of specific objects and
object components.


-----------------------------------------


Return Value:

boolean  When used with query    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ado   : addDagObject    [name] []
    Add the specified object to the set of objects to be displayed in the view.

-----------------------------------------

addSelected : addSelected     [boolean] []
    Add the currently active objects to the set of objects to be displayed in the view.

-----------------------------------------

aso   : addSelectedObjects [boolean] []
    Add selected objects to the set of objects to be displayed in the view. This flag differs from addSelected in that it will ignore selected components and add the entire object.

-----------------------------------------

ls    : loadSelected    [boolean] []
    Replace the objects being displayed with the currently active objects.

-----------------------------------------

rdo   : removeDagObject [name] []
    Remove the specified object from the set of objects to be displayed in the view.

-----------------------------------------

rs    : removeSelected  [boolean] []
    Remove the currently active objects to the set of objects to be displayed in the view.

-----------------------------------------

s     : state           [boolean] ['query']
    Turns isolate select mode on/off.

-----------------------------------------

u     : update          [boolean] []
    Update the view's list of objects due to a change to the set of objects to be displayed.

-----------------------------------------

vo    : viewObjects     [boolean]
    Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.

    """

def pickWalk(d="string",r=1,typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pickWalk.html



-----------------------------------------

pickWalk is undoable, NOT queryable, and NOT editable.

The pickWalk command allows you to quickly change the selection list relative
to the nodes that are currently selected. It is called pickWalk, because it
walks from one selection list to another by unselecting what's currently
selected, and selecting nodes that are in the specified direction from the
currently selected list. If you specify objects on the command line, the
pickWalk command will walk from those objects instead of the selected list.

If the -type flag is instances, then the left and right direction will walk to
the previous or next instance of the same selected dag node.


-----------------------------------------


Return Value:

string[]  A list of the newly selected items


-----------------------------------------


Flags:

-----------------------------------------

d     : direction       [string] []
    The direction to walk from the node. The choices are up | down | left | right | in | out. up walks to the parent node, down to the child node, and left and right to the sibling nodes. If a CV on a surface is selected, the left and right directions walk in the U parameter direction of the surface, and the up and down directions walk in the V parameter direction. In and out are only used if the type flag is 'latticepoints'. Default is right.

-----------------------------------------

r     : recurse         [boolean] []
    If specified then recurse down when walking

-----------------------------------------

typ   : type            [string]
    The choices are nodes | instances | edgeloop | edgering | faceloop | keys | latticepoints | motiontrailpoints. If type is nodes, then the left and right direction walk to the next dag siblings. If type is instances, the left and right direction walk to the previous or next instance of the same dag node. If type is edgeloop, then the edge loop starting at the first selected edge will be selected. If type is edgering, then the edge ring starting at the first selected edge will be selected. If type is faceloop, and there are two connected quad faces selected which define a face loop, then that face loop will be selected. edgeloop, edgering and faceloop all remember which was the first edge or faces selected for as long as consecutive selections are made by this command. They use this information to determine what the "next" loop or ring selection should be. Users can make selections forwards and backwards by using the direction flag with "left" or "right". If type is motiontrailpoints, then the left and right direction walk to the previous or next motion trail points respectively. Default is nodes.

    """

def select(add=1,af=1,all=1,ado=1,adn=1,cl=1,cc=1,d=1,hi=1,ne=1,r=1,sym=1,sys="int",tgl=1,vis=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/select.html



-----------------------------------------

select is undoable, NOT queryable, and NOT editable.

This command is used to put objects onto or off of the active list. If none of
the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to
replace the objects on the active list with the given list of objects.

When selecting a set as in "select set1", the behaviour is for all the members
of the set to become selected instead of the set itself. If you want to select
a set, the "-ne/noExpand" flag must be used.

With the advent of namespaces, selection by name may be confusing. To clarify,
without a qualified namespace, name lookup is limited to objects in the root
namespace ":". There are really two parts of a name: the namespace and the
name itself which is unique within the namespace. If you want to select
objects in a specific namespace, you need to include the namespace separator
":".

For example, 'select -r "foo*"' is trying to look for an object with the "foo"
prefix in the root namespace. It is not trying to look for all objects in the
namespace with the "foo" prefix. If you want to select all objects in a
namespace (foo), use 'select "foo:*"'.

Note: When the application starts up, there are several dependency nodes
created by the system which must exist. These objects are not deletable but
are selectable. All objects (dag and dependency nodes) in the scene can be
obtained using the "ls" command without any arguments. When using the "-all",
"adn/allDependencyNodes" or "-ado/allDagObjects" flags, only the deletable
objects are selected. The non deletable object can still be selected by
explicitly specifying their name as in "select time1;".


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

add   : add             [boolean] []
    Indicates that the specified items should be added to the active list without removing existing items from the active list.

-----------------------------------------

af    : addFirst        [boolean] []
    Indicates that the specified items should be added to the front of the active list without removing existing items from the active list.

-----------------------------------------

all   : all             [boolean] []
    Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.

-----------------------------------------

ado   : allDagObjects   [boolean] []
    Indicates that all deletable root level dag objects should be selected.

-----------------------------------------

adn   : allDependencyNodes [boolean] []
    Indicates that all deletable dependency nodes including all deletable dag objects should be selected.

-----------------------------------------

cl    : clear           [boolean] []
    Clears the active list. This is more efficient than "select -d;". Also "select -d;" will not remove sets from the active list unless the "-ne" flag is also specified.

-----------------------------------------

cc    : containerCentric [boolean] []
    Specifies that the same selection rules as apply to selection in the main viewport will also be applied to the select command. In particular, if the specified objects are members of a black-boxed container and are not published as nodes, Maya will not select them. Instead, their first parent valid for selection will be selected.

-----------------------------------------

d     : deselect        [boolean] []
    Indicates that the specified items should be removed from the active list if they are on the active list.

-----------------------------------------

hi    : hierarchy       [boolean] []
    Indicates that all children, grandchildren, ... of the specified dag objects should also be selected.

-----------------------------------------

ne    : noExpand        [boolean] []
    Indicates that any set which is among the specified items should not be expanded to its list of members. This allows sets to be selected as opposed to the members of sets which is the default behaviour.

-----------------------------------------

r     : replace         [boolean] []
    Indicates that the specified items should replace the existing items on the active list.

-----------------------------------------

sym   : symmetry        [boolean] []
    Specifies that components should be selected symmetrically using the current symmetricModelling command settings. If symmetric modeling is not enabled then this flag has no effect.

-----------------------------------------

sys   : symmetrySide    [int] []
    Indicates that components involved in the current symmetry object should be selected, according to the supplied parameter. Valid values for the parameter are:   -1 : Select components in the unsymmetrical region.    0 : Select components on the symmetry seam.   1 : Select components on side 1.   2 : Select components on side 2. If symmetric modeling is not enabled then this flag has no effect. Note: currently only works for topological symmetry.

-----------------------------------------

tgl   : toggle          [boolean] []
    Indicates that those items on the given list which are on the active list should be removed from the active list and those items on the given list which are not on the active list should be added to the active list.

-----------------------------------------

vis   : visible         [boolean]
    Indicates that of the specified items only those that are visible should be affected.

    """

def selectKey(add=1,an="string",at="string",cl=1,cp=1,f="floatrange",hi="string",it=1,iub=1,index="uint",k=1,ot=1,rm=1,r=1,s=1,t="timerange",tgl=1,uk="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectKey.html



-----------------------------------------

selectKey is undoable, NOT queryable, and NOT editable.

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

This command places keyframes and/or keyframe tangents on the active list.


-----------------------------------------


Return Value:

int  The number of curves on which keys were selected (or deselcted).


-----------------------------------------


Flags:

-----------------------------------------

add   : addTo           [boolean] []
    Add to the current selection of keyframes/tangents

-----------------------------------------

an    : animation       [string] []
    Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." (See Description for details.)

-----------------------------------------

at    : attribute       [string] []
    List of attributes to select  In query mode, this flag needs a value.

-----------------------------------------

cl    : clear           [boolean] []
    Remove all keyframes and tangents from the active list.

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

it    : inTangent       [boolean] []
    Select in-tangents of keyframes in the specified time range

-----------------------------------------

iub   : includeUpperBound [boolean] []
    When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.)

-----------------------------------------

index : index           [uint] []
    index of a key on an animCurve  In query mode, this flag needs a value.

-----------------------------------------

k     : keyframe        [boolean] []
    select only keyframes (cannot be combined with -in/-out)

-----------------------------------------

ot    : outTangent      [boolean] []
    Select out-tangents of keyframes in the specified time range

-----------------------------------------

rm    : remove          [boolean] []
    Remove from the current selection of keyframes/tangents

-----------------------------------------

r     : replace         [boolean] []
    Replace the current selection of keyframes/tangents

-----------------------------------------

s     : shape           [boolean] []
    Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)  In query mode, this flag needs a value.

-----------------------------------------

t     : time            [timerange] []
    time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.  In query mode, this flag needs a value.

-----------------------------------------

tgl   : toggle          [boolean] []
    Toggle the picked state of the specified keyset

-----------------------------------------

uk    : unsnappedKeys   [float]
    Select only keys that have times that are not a multiple of the specified numeric value.

    """

def selectMode(q=1,co=1,h=1,l=1,o=1,p=1,r=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectMode.html



-----------------------------------------

selectMode is undoable, queryable, and NOT editable.

The selectMode command is used to change the selection mode. Object,
component, root, leaf and template modes are mutually exclusive.


-----------------------------------------


Return Value:

boolean  if a query operation    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

co    : component       [boolean] ['query']
    Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are selectable.

-----------------------------------------

h     : hierarchical    [boolean] ['query']
    Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template. Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root, leaf, or template was last on.

-----------------------------------------

l     : leaf            [boolean] ['query']
    Set leaf selection mode on. This mode allows the leaf level objects to be selected. It is similar to object selection mode but ignores the object selection mask.

-----------------------------------------

o     : object          [boolean] ['query']
    Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable. The masks are controlled by the "selectType" command. Object selection mode selects the leaf level objects.

-----------------------------------------

p     : preset          [boolean] ['query']
    Allow selection of anything with the mask set, independent of it being an object or a component.

-----------------------------------------

r     : root            [boolean] ['query']
    Set root selection mode on. This mode allows the root of a hierarchy to be selected by selecting any of its descendents. It ignores the object selection mask.

-----------------------------------------

t     : template        [boolean]
    Set template selection mode on. This mode allows selection of templated objects. It selects the templated object closest to the root of the hierarchy.

    """

def selectPref(q=1,aa=1,ahs=1,asc=1,aud=1,cbs="uint",cld=1,ccs=1,dcp=1,epl=1,isp=1,mcb="uint",ps=1,psd=1,pms=1,psb=1,psc=1,pds="uint",psh=1,phs="float",pdt="uint",stc=1,sch="int",sbs=1,sld=1,tso=1,ud=1,xns=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectPref.html



-----------------------------------------

selectPref is undoable, queryable, and NOT editable.

This command controls state variables used to selection UI behavior.


-----------------------------------------


Return Value:

boolean  in the query mode.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aa    : affectsActive   [boolean] ['query']
    Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.

-----------------------------------------

ahs   : allowHiliteSelection [boolean] ['query']
    When in component selection mode, allow selection of objects for editing. If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.

-----------------------------------------

asc   : autoSelectContainer [boolean] ['query']
    When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.

-----------------------------------------

aud   : autoUseDepth    [boolean] ['query']
    When enabled, useDepth and paintSelectWithDepth will be automatically enabled in shaded display mode and disabled in wireframe display mode.

-----------------------------------------

cbs   : clickBoxSize    [uint] ['query']
    When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position. The size must be positive.

-----------------------------------------

cld   : clickDrag       [boolean] ['query']
    Set click/drag selection interaction on/off

-----------------------------------------

ccs   : containerCentricSelection [boolean] ['query']
    When enabled, selecting any DAG node in a container in the viewport will select the container's root transform if there is one. If there is no root transform then the highest DAG node in the container will be selected. There is no effect when selecting nodes which are not in a container.

-----------------------------------------

dcp   : disableComponentPopups [boolean] ['query']
    A separate preference to allow users to disable popup menus when selecting components. This pref is only meaningful if the popupMenuSelection pref is enabled.

-----------------------------------------

epl   : expandPopupList [boolean] ['query']
    When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.

-----------------------------------------

isp   : ignoreSelectionPriority [boolean] ['query']
    If this is set, selection priority will be ignored when performing selection.

-----------------------------------------

mcb   : manipClickBoxSize [uint] ['query']
    When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position. The size must be positive.

-----------------------------------------

ps    : paintSelect     [boolean] ['query']
    When enabled, the select tool will use drag selection instead of marquee selection.

-----------------------------------------

psd   : paintSelectWithDepth [boolean] ['query']
    When enabled, paint selection will not select components that are behind the surface in the current camera view.

-----------------------------------------

pms   : popupMenuSelection [boolean] ['query']
    If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.

-----------------------------------------

psb   : preSelectBackfacing [boolean] ['query']
    When enabled preselection will highlight backfacing components whose normals face away from the camera.

-----------------------------------------

psc   : preSelectClosest [boolean] ['query']
    When enabled and the cursor is over a surface, preselection highlighting will try to preselect the closest component to the cursor regardless of distance.

-----------------------------------------

pds   : preSelectDeadSpace [uint] ['query']
    This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface.

-----------------------------------------

psh   : preSelectHilite [boolean] ['query']
    When enabled, the closest component under the cursor will be highlighted to indicate that clicking will select that component.

-----------------------------------------

phs   : preSelectHiliteSize [float] ['query']
    This value defines the size of the region around the cursor used for preselection highlighting. Within this region the closest component to the cursor will be highlighted.

-----------------------------------------

pdt   : preSelectTweakDeadSpace [uint] ['query']
    This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface in tweak mode.

-----------------------------------------

stc   : selectTypeChangeAffectsActive [boolean] ['query']
    If true then the active list will be updated according to the new selection preferences.

-----------------------------------------

sch   : selectionChildHighlightMode [int] ['query']
    Controls the highlighting of the children of a selected object. Valid modes are: 0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting. Default mode is (0): Always highlight children. For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.

-----------------------------------------

sbs   : singleBoxSelection [boolean] ['query']
    Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true. Otherwise, all those objects inside the box will be selected.

-----------------------------------------

sld   : straightLineDistance [boolean] ['query']
    If true then use straight line distances for selection proximity.

-----------------------------------------

tso   : trackSelectionOrder [boolean] ['query']
    When enabled, the order of selected objects and components will be tracked. The 'ls' command will be able to return the active list in the order of selection which will allow scripts to be written that depend on the order.

-----------------------------------------

ud    : useDepth        [boolean] ['query']
    When enabled, marquee selection will not select components that are behind the surface in the current camera view.

-----------------------------------------

xns   : xformNoSelect   [boolean]
    Disable selection in xform tools

    """

def selectPriority(q=1,alc="uint",alo="uint",abd="uint",ac="uint",ait="uint",ak="uint",aot="uint",bn="[string, boolean]",ca="uint",cl="uint",clm="uint",cv="uint",c="uint",ck="uint",cos="uint",cpp="uint",dim="uint",dc="uint",eg="uint",ep="uint",em="uint",fc="uint",fi="uint",fl="uint",fo="uint",hs="uint",ha="uint",hl="uint",iee="uint",ikh="uint",ip="uint",ig="uint",iso="uint",j="uint",jp="uint",la="uint",lp="uint",lt="uint",ra="uint",lc="uint",luv="uint",xyz="uint",msh="uint",mtp="uint",mtt="uint",ncl="uint",npr="uint",nps="uint",nr="uint",nl="uint",nc="uint",ns="uint",ol="uint",pr="uint",ps="uint",pl="uint",p="uint",pe="uint",pf="uint",pfe="uint",puv="uint",pv="uint",pvf="uint",qbn="string",rb="uint",rc="uint",rp="uint",sp="uint",sc="uint",sh="uint",spr="uint",spc="uint",str="uint",sd="uint",sme="uint",smf="uint",smp="uint",smu="uint",se="uint",sf="uint",sk="uint",spp="uint",sr="uint",tx="uint",v="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectPriority.html



-----------------------------------------

selectPriority is undoable, queryable, and NOT editable.

The selectPriority command is used to change the selection priority of
particular types of objects that can be selected when using the select tool.
It accepts no other arguments besides the flags. These flags are the same as
used by the 'selectType' command.


-----------------------------------------


Return Value:

int  if a query operation    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

alc   : allComponents   [uint] ['query']
    Set all component selection priority

-----------------------------------------

alo   : allObjects      [uint] ['query']
    Set all object selection priority

-----------------------------------------

abd   : animBreakdown   [uint] ['query']
    Set animation breakdown selection priority

-----------------------------------------

ac    : animCurve       [uint] ['query']
    Set animation curve selection priority

-----------------------------------------

ait   : animInTangent   [uint] ['query']
    Set animation in-tangent selection priority

-----------------------------------------

ak    : animKeyframe    [uint] ['query']
    Set animation keyframe selection priority

-----------------------------------------

aot   : animOutTangent  [uint] ['query']
    Set animation out-tangent selection priority

-----------------------------------------

bn    : byName          [[string, boolean]] []
    Set selection priority for the specified user-defined selection type

-----------------------------------------

ca    : camera          [uint] ['query']
    Set camera selection priority

-----------------------------------------

cl    : cluster         [uint] ['query']
    Set cluster selection priority

-----------------------------------------

clm   : collisionModel  [uint] ['query']
    Set collision model selection priority

-----------------------------------------

cv    : controlVertex   [uint] ['query']
    Set control vertex selection priority

-----------------------------------------

c     : curve           [uint] ['query']
    Set curve selection priority

-----------------------------------------

ck    : curveKnot       [uint] ['query']
    Set curve knot selection priority

-----------------------------------------

cos   : curveOnSurface  [uint] ['query']
    Set curve-on-surface selection priority

-----------------------------------------

cpp   : curveParameterPoint [uint] ['query']
    Set curve parameter point selection priority

-----------------------------------------

dim   : dimension       [uint] ['query']
    Set dimension shape selection priority

-----------------------------------------

dc    : dynamicConstraint [uint] ['query']
    Set dynamicConstraint selection priority

-----------------------------------------

eg    : edge            [uint] ['query']
    Set mesh edge selection priority

-----------------------------------------

ep    : editPoint       [uint] ['query']
    Set edit-point selection priority

-----------------------------------------

em    : emitter         [uint] ['query']
    Set emitter selection priority

-----------------------------------------

fc    : facet           [uint] ['query']
    Set mesh face selection priority

-----------------------------------------

fi    : field           [uint] ['query']
    Set field selection priority

-----------------------------------------

fl    : fluid           [uint] ['query']
    Set fluid selection priority

-----------------------------------------

fo    : follicle        [uint] ['query']
    Set follicle selection priority

-----------------------------------------

hs    : hairSystem      [uint] ['query']
    Set hairSystem selection priority

-----------------------------------------

ha    : handle          [uint] ['query']
    Set object handle selection priority

-----------------------------------------

hl    : hull            [uint] ['query']
    Set hull selection priority

-----------------------------------------

iee   : ikEndEffector   [uint] ['query']
    Set ik end effector selection priority

-----------------------------------------

ikh   : ikHandle        [uint] ['query']
    Set ik handle selection priority

-----------------------------------------

ip    : imagePlane      [uint] ['query']
    Set image plane selection mask priority

-----------------------------------------

ig    : implicitGeometry [uint] ['query']
    Set implicit geometry selection priority

-----------------------------------------

iso   : isoparm         [uint] ['query']
    Set surface iso-parm selection priority

-----------------------------------------

j     : joint           [uint] ['query']
    Set ik handle selection priority

-----------------------------------------

jp    : jointPivot      [uint] ['query']
    Set joint pivot selection priority

-----------------------------------------

la    : lattice         [uint] ['query']
    Set lattice selection priority

-----------------------------------------

lp    : latticePoint    [uint] ['query']
    Set lattice point selection priority

-----------------------------------------

lt    : light           [uint] ['query']
    Set light selection priority

-----------------------------------------

ra    : localRotationAxis [uint] ['query']
    Set local rotation axis selection priority

-----------------------------------------

lc    : locator         [uint] ['query']
    Set locator (all types) selection priority

-----------------------------------------

luv   : locatorUV       [uint] ['query']
    Set uv locator selection priority

-----------------------------------------

xyz   : locatorXYZ      [uint] ['query']
    Set xyz locator selection priority

-----------------------------------------

msh   : meshUVShell     [uint] ['query']
    Set uv shell component mask on/off.

-----------------------------------------

mtp   : motionTrailPoint [uint] ['query']
    Set motion point selection priority

-----------------------------------------

mtt   : motionTrailTangent [uint] ['query']
    Set motion point tangent priority

-----------------------------------------

ncl   : nCloth          [uint] ['query']
    Set nCloth selection priority

-----------------------------------------

npr   : nParticle       [uint] ['query']
    Set nParticle point selection priority

-----------------------------------------

nps   : nParticleShape  [uint] ['query']
    Set nParticle shape selection priority

-----------------------------------------

nr    : nRigid          [uint] ['query']
    Set nRigid selection priority

-----------------------------------------

nl    : nonlinear       [uint] ['query']
    Set nonlinear selection priority

-----------------------------------------

nc    : nurbsCurve      [uint] ['query']
    Set nurbs-curve selection priority

-----------------------------------------

ns    : nurbsSurface    [uint] ['query']
    Set nurbs-surface selection priority

-----------------------------------------

ol    : orientationLocator [uint] ['query']
    Set orientation locator selection priority

-----------------------------------------

pr    : particle        [uint] ['query']
    Set particle point selection priority

-----------------------------------------

ps    : particleShape   [uint] ['query']
    Set particle shape selection priority

-----------------------------------------

pl    : plane           [uint] ['query']
    Set sketch plane selection priority

-----------------------------------------

p     : polymesh        [uint] ['query']
    Set poly-mesh selection priority

-----------------------------------------

pe    : polymeshEdge    [uint] ['query']
    Set poly-mesh edge selection priority

-----------------------------------------

pf    : polymeshFace    [uint] ['query']
    Set poly-mesh face selection priority

-----------------------------------------

pfe   : polymeshFreeEdge [uint] ['query']
    Set poly-mesh free-edge selection priority

-----------------------------------------

puv   : polymeshUV      [uint] ['query']
    Set poly-mesh UV point selection priority

-----------------------------------------

pv    : polymeshVertex  [uint] ['query']
    Set poly-mesh vertex selection priority

-----------------------------------------

pvf   : polymeshVtxFace [uint] ['query']
    Set poly-mesh vtxFace selection priority

-----------------------------------------

qbn   : queryByName     [string] ['query']
    Query selection priority for the specified user-defined selection type  In query mode, this flag needs a value.

-----------------------------------------

rb    : rigidBody       [uint] ['query']
    Set rigid body selection priority

-----------------------------------------

rc    : rigidConstraint [uint] ['query']
    Set rigid constraint selection priority

-----------------------------------------

rp    : rotatePivot     [uint] ['query']
    Set rotate pivot selection priority

-----------------------------------------

sp    : scalePivot      [uint] ['query']
    Set scale pivot selection priority

-----------------------------------------

sc    : sculpt          [uint] ['query']
    Set sculpt selection priority

-----------------------------------------

sh    : selectHandle    [uint] ['query']
    Set select handle selection priority

-----------------------------------------

spr   : spring          [uint] ['query']
    Set spring shape selection priority

-----------------------------------------

spc   : springComponent [uint] ['query']
    Set individual spring selection priority

-----------------------------------------

str   : stroke          [uint] ['query']
    Set stroke selection priority

-----------------------------------------

sd    : subdiv          [uint] ['query']
    Set subdivision surface selection priority

-----------------------------------------

sme   : subdivMeshEdge  [uint] ['query']
    Set subdivision surface mesh edge selection priority

-----------------------------------------

smf   : subdivMeshFace  [uint] ['query']
    Set subdivision surface mesh face selection priority

-----------------------------------------

smp   : subdivMeshPoint [uint] ['query']
    Set subdivision surface mesh point selection priority

-----------------------------------------

smu   : subdivMeshUV    [uint] ['query']
    Set subdivision surface mesh UV map selection priority

-----------------------------------------

se    : surfaceEdge     [uint] ['query']
    Set surface edge selection priority

-----------------------------------------

sf    : surfaceFace     [uint] ['query']
    Set surface face selection priority

-----------------------------------------

sk    : surfaceKnot     [uint] ['query']
    Set surface knot selection priority

-----------------------------------------

spp   : surfaceParameterPoint [uint] ['query']
    Set surface parameter point selection priority

-----------------------------------------

sr    : surfaceRange    [uint] ['query']
    Set surface range selection priority

-----------------------------------------

tx    : texture         [uint] ['query']
    Set texture selection priority

-----------------------------------------

v     : vertex          [uint]
    Set mesh vertex selection priority

    """

def selectType(q=1,alc=1,alo=1,abd=1,ac=1,ait=1,ak=1,aot=1,bn="[string, boolean]",ca=1,cl=1,clm=1,cv=1,c=1,ck=1,cos=1,cpp=1,dim=1,dc=1,eg=1,ep=1,em=1,fc=1,fi=1,fl=1,fo=1,hs=1,ha=1,hl=1,iee=1,ikh=1,ip=1,ig=1,iso=1,j=1,jp=1,la=1,lp=1,lt=1,ra=1,lc=1,luv=1,xyz=1,msh=1,mtp=1,mtt=1,ncl=1,npr=1,nps=1,nr=1,nl=1,nc=1,ns=1,ocm=1,ol=1,pr=1,ps=1,pl=1,p=1,pe=1,pf=1,pfe=1,puv=1,pv=1,pvf=1,qbn="string",rb=1,rc=1,rp=1,sp=1,sc=1,sh=1,spr=1,spc=1,str=1,sd=1,sme=1,smf=1,smp=1,smu=1,se=1,sf=1,sk=1,spp=1,sr=1,suv=1,tx=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectType.html



-----------------------------------------

selectType is undoable, queryable, and NOT editable.

The selectType command is used to change the set of allowable types of objects
that can be selected when using the select tool. It accepts no other arguments
besides the flags.

There are basically two different types of items that are selectable when
interactively selecting objects in the 3D views. They are classified as
objects (entire objects) or components (parts of objects). The object and
component command flags control which class of objects are selectable.

It is possible to select components while in the object selection mode. To set
the components which are selectable in object selection mode you must use the
-ocm flag when specifying the component flags.


-----------------------------------------


Return Value:

boolean  if a query operation    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

alc   : allComponents   [boolean] ['query']
    Set all component selection masks on/off

-----------------------------------------

alo   : allObjects      [boolean] ['query']
    Set all object selection masks on/off

-----------------------------------------

abd   : animBreakdown   [boolean] ['query']
    Set animation breakdown selection mask on/off.

-----------------------------------------

ac    : animCurve       [boolean] ['query']
    Set animation curve selection mask on/off.

-----------------------------------------

ait   : animInTangent   [boolean] ['query']
    Set animation in-tangent selection mask on/off.

-----------------------------------------

ak    : animKeyframe    [boolean] ['query']
    Set animation keyframe selection mask on/off.

-----------------------------------------

aot   : animOutTangent  [boolean] ['query']
    Set animation out-tangent selection mask on/off.

-----------------------------------------

bn    : byName          [[string, boolean]] []
    Set the specified user-defined selection mask on/off. (object flag)

-----------------------------------------

ca    : camera          [boolean] ['query']
    Set camera selection mask on/off. (object flag)

-----------------------------------------

cl    : cluster         [boolean] ['query']
    Set cluster selection mask on/off. (object flag)

-----------------------------------------

clm   : collisionModel  [boolean] ['query']
    Set collision model selection mask on/off. (object flag)

-----------------------------------------

cv    : controlVertex   [boolean] ['query']
    Set control vertex selection mask on/off. (component flag)

-----------------------------------------

c     : curve           [boolean] ['query']
    Set curve selection mask on/off. (object flag)

-----------------------------------------

ck    : curveKnot       [boolean] ['query']
    Set curve knot selection mask on/off. (component flag)

-----------------------------------------

cos   : curveOnSurface  [boolean] ['query']
    Set curve-on-surface selection mask on/off. (object flag)

-----------------------------------------

cpp   : curveParameterPoint [boolean] ['query']
    Set curve parameter point selection mask on/off. (component flag)

-----------------------------------------

dim   : dimension       [boolean] ['query']
    Set dimension shape selection mask on/off. (object flag)

-----------------------------------------

dc    : dynamicConstraint [boolean] ['query']
    Set dynamicConstraint selection mask on/off. (object flag)

-----------------------------------------

eg    : edge            [boolean] ['query']
    Set mesh edge selection mask on/off. (component flag)

-----------------------------------------

ep    : editPoint       [boolean] ['query']
    Set edit-point selection mask on/off. (component flag)

-----------------------------------------

em    : emitter         [boolean] ['query']
    Set emitter selection mask on/off. (object flag)

-----------------------------------------

fc    : facet           [boolean] ['query']
    Set mesh face selection mask on/off. (component flag)

-----------------------------------------

fi    : field           [boolean] ['query']
    Set field selection mask on/off. (object flag)

-----------------------------------------

fl    : fluid           [boolean] ['query']
    Set fluid selection mask on/off. (object flag)

-----------------------------------------

fo    : follicle        [boolean] ['query']
    Set follicle selection mask on/off. (object flag)

-----------------------------------------

hs    : hairSystem      [boolean] ['query']
    Set hairSystem selection mask on/off. (object flag)

-----------------------------------------

ha    : handle          [boolean] ['query']
    Set object handle selection mask on/off. (object flag)

-----------------------------------------

hl    : hull            [boolean] ['query']
    Set hull selection mask on/off. (component flag)

-----------------------------------------

iee   : ikEndEffector   [boolean] ['query']
    Set ik end effector selection mask on/off. (object flag)

-----------------------------------------

ikh   : ikHandle        [boolean] ['query']
    Set ik handle selection mask on/off. (object flag)

-----------------------------------------

ip    : imagePlane      [boolean] ['query']
    Set image plane selection mask on/off. (component flag)

-----------------------------------------

ig    : implicitGeometry [boolean] ['query']
    Set implicit geometry selection mask on/off. (object flag)

-----------------------------------------

iso   : isoparm         [boolean] ['query']
    Set surface iso-parm selection mask on/off. (component flag)

-----------------------------------------

j     : joint           [boolean] ['query']
    Set ik handle selection mask on/off. (object flag)

-----------------------------------------

jp    : jointPivot      [boolean] ['query']
    Set joint pivot selection mask on/off. (component flag)

-----------------------------------------

la    : lattice         [boolean] ['query']
    Set lattice selection mask on/off. (object flag)

-----------------------------------------

lp    : latticePoint    [boolean] ['query']
    Set lattice point selection mask on/off. (component flag)

-----------------------------------------

lt    : light           [boolean] ['query']
    Set light selection mask on/off. (object flag)

-----------------------------------------

ra    : localRotationAxis [boolean] ['query']
    Set local rotation axis selection mask on/off. (component flag)

-----------------------------------------

lc    : locator         [boolean] ['query']
    Set locator (all types) selection mask on/off. (object flag)

-----------------------------------------

luv   : locatorUV       [boolean] ['query']
    Set uv locator selection mask on/off. (object flag)

-----------------------------------------

xyz   : locatorXYZ      [boolean] ['query']
    Set xyz locator selection mask on/off. (object flag)

-----------------------------------------

msh   : meshUVShell     [boolean] ['query']
    Set uv shell component mask on/off.

-----------------------------------------

mtp   : motionTrailPoint [boolean] ['query']
    Set motion point selection mask on/off.

-----------------------------------------

mtt   : motionTrailTangent [boolean] ['query']
    Set motion point tangent mask on/off.

-----------------------------------------

ncl   : nCloth          [boolean] ['query']
    Set nCloth selection mask on/off. (object flag)

-----------------------------------------

npr   : nParticle       [boolean] ['query']
    Set nParticle point selection mask on/off. (component flag)

-----------------------------------------

nps   : nParticleShape  [boolean] ['query']
    Set nParticle shape selection mask on/off. (object flag)

-----------------------------------------

nr    : nRigid          [boolean] ['query']
    Set nRigid selection mask on/off. (object flag)

-----------------------------------------

nl    : nonlinear       [boolean] ['query']
    Set nonlinear selection mask on/off. (object flag)

-----------------------------------------

nc    : nurbsCurve      [boolean] ['query']
    Set nurbs-curve selection mask on/off. (object flag)

-----------------------------------------

ns    : nurbsSurface    [boolean] ['query']
    Set nurbs-surface selection mask on/off. (object flag)

-----------------------------------------

ocm   : objectComponent [boolean] ['query']
    Component flags apply to object mode.

-----------------------------------------

ol    : orientationLocator [boolean] ['query']
    Set orientation locator selection mask on/off. (object flag)

-----------------------------------------

pr    : particle        [boolean] ['query']
    Set particle point selection mask on/off. (component flag)

-----------------------------------------

ps    : particleShape   [boolean] ['query']
    Set particle shape selection mask on/off. (object flag)

-----------------------------------------

pl    : plane           [boolean] ['query']
    Set sketch plane selection mask on/off. (object flag)

-----------------------------------------

p     : polymesh        [boolean] ['query']
    Set poly-mesh selection mask on/off. (object flag)

-----------------------------------------

pe    : polymeshEdge    [boolean] ['query']
    Set poly-mesh edge selection mask on/off. (component flag)

-----------------------------------------

pf    : polymeshFace    [boolean] ['query']
    Set poly-mesh face selection mask on/off. (component flag)

-----------------------------------------

pfe   : polymeshFreeEdge [boolean] ['query']
    Set poly-mesh free-edge selection mask on/off. (component flag)

-----------------------------------------

puv   : polymeshUV      [boolean] ['query']
    Set poly-mesh UV point selection mask on/off. (component flag)

-----------------------------------------

pv    : polymeshVertex  [boolean] ['query']
    Set poly-mesh vertex selection mask on/off. (component flag)

-----------------------------------------

pvf   : polymeshVtxFace [boolean] ['query']
    Set poly-mesh vertexFace selection mask on/off. (component flag)

-----------------------------------------

qbn   : queryByName     [string] ['query']
    Query the specified user-defined selection mask. (object flag)  In query mode, this flag needs a value.

-----------------------------------------

rb    : rigidBody       [boolean] ['query']
    Set rigid body selection mask on/off. (object flag)

-----------------------------------------

rc    : rigidConstraint [boolean] ['query']
    Set rigid constraint selection mask on/off. (object flag)

-----------------------------------------

rp    : rotatePivot     [boolean] ['query']
    Set rotate pivot selection mask on/off. (component flag)

-----------------------------------------

sp    : scalePivot      [boolean] ['query']
    Set scale pivot selection mask on/off. (component flag)

-----------------------------------------

sc    : sculpt          [boolean] ['query']
    Set sculpt selection mask on/off. (object flag)

-----------------------------------------

sh    : selectHandle    [boolean] ['query']
    Set select handle selection mask on/off. (component flag)

-----------------------------------------

spr   : spring          [boolean] ['query']
    Set spring shape selection mask on/off. (object flag)

-----------------------------------------

spc   : springComponent [boolean] ['query']
    Set individual spring selection mask on/off. (component flag)

-----------------------------------------

str   : stroke          [boolean] ['query']
    Set the Paint Effects stroke selection mask on/off. (object flag)

-----------------------------------------

sd    : subdiv          [boolean] ['query']
    Set subdivision surfaces selection mask on/off. (object flag)

-----------------------------------------

sme   : subdivMeshEdge  [boolean] ['query']
    Set subdivision surfaces mesh edge selection mask on/off. (component flag)

-----------------------------------------

smf   : subdivMeshFace  [boolean] ['query']
    Set subdivision surfaces mesh face selection mask on/off. (component flag)

-----------------------------------------

smp   : subdivMeshPoint [boolean] ['query']
    Set subdivision surfaces mesh point selection mask on/off. (component flag)

-----------------------------------------

smu   : subdivMeshUV    [boolean] ['query']
    Set subdivision surfaces mesh UV map selection mask on/off. (component flag)

-----------------------------------------

se    : surfaceEdge     [boolean] ['query']
    Set surface edge selection mask on/off. (component flag)

-----------------------------------------

sf    : surfaceFace     [boolean] ['query']
    Set surface face selection mask on/off. (component flag)

-----------------------------------------

sk    : surfaceKnot     [boolean] ['query']
    Set surface knot selection mask on/off. (component flag)

-----------------------------------------

spp   : surfaceParameterPoint [boolean] ['query']
    Set surface parameter point selection mask on/off. (component flag)

-----------------------------------------

sr    : surfaceRange    [boolean] ['query']
    Set surface range selection mask on/off. (component flag)

-----------------------------------------

suv   : surfaceUV       [boolean] ['query']
    Set surface uv selection mask on/off. (component flag)

-----------------------------------------

tx    : texture         [boolean] ['query']
    Set texture selection mask on/off. (object flag)

-----------------------------------------

v     : vertex          [boolean]
    Set mesh vertex selection mask on/off. (component flag)

    """

def softSelect(q=1,e=1,cu="int",efc="int",scc="string",ssc="string",ssd="float",sse="int",ssf="int",ssr=1,sud="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/softSelect.html



-----------------------------------------

softSelect is undoable, queryable, and editable.

This command allows you to change the soft modelling options.

Soft modelling is an option that allows for reflection of basic manipulator
actions such as move, rotate, and scale.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cu    : compressUndo    [int] ['query', 'edit']
    Controls how soft selection settings behave in undo:    * 0 means all changes undo individually   * 1 means all consecutive changes undo as a group   * 2 means only interactive changes undo as a group  When queried, returns an int indicating the current undo behaviour.

-----------------------------------------

efc   : enableFalseColor [int] ['query', 'edit']
    Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.

-----------------------------------------

scc   : softSelectColorCurve [string] ['query', 'edit']
    Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.

-----------------------------------------

ssc   : softSelectCurve [string] ['query', 'edit']
    Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3 successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff curve.

-----------------------------------------

ssd   : softSelectDistance [float] ['query', 'edit']
    Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.

-----------------------------------------

sse   : softSelectEnabled [int] ['query', 'edit']
    Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.

-----------------------------------------

ssf   : softSelectFalloff [int] ['query', 'edit']
    Sets the falloff mode:    * 0 for volume based falloff   * 1 for surface based falloff   * 2 for global falloff  When queried, returns an int indicating the falloff mode.

-----------------------------------------

ssr   : softSelectReset [boolean] ['edit']
    Resets soft selection to its default settings.

-----------------------------------------

sud   : softSelectUVDistance [float]
    Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.

    """

def symmetricModelling(q=1,e=1,a="string",ap=1,ax="string",ps="int",r=1,sf="string",st="float",s="int",t="float",ts=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/symmetricModelling.html



-----------------------------------------

symmetricModelling is undoable, queryable, and editable.

This command allows you to change the symmetric modelling options.

Symmetric modelling is an option that allows for reflection of basic
manipulator actions such as move, rotate, and scale.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : about           [string] ['query', 'edit']
    Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.

-----------------------------------------

ap    : allowPartial    [boolean] ['query', 'edit']
    Specifies whether partial symmetry should be allowed when enabling topological symmetry.

-----------------------------------------

ax    : axis            [string] ['query', 'edit']
    Set the current axis to be reflected over. When queried, returns a string which is the current axis.

-----------------------------------------

ps    : preserveSeam    [int] ['query', 'edit']
    Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.

-----------------------------------------

r     : reset           [boolean] ['edit']
    Reset the redo information before starting.

-----------------------------------------

sf    : seamFalloffCurve [string] ['query', 'edit']
    Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.

-----------------------------------------

st    : seamTolerance   [float] ['query', 'edit']
    Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.

-----------------------------------------

s     : symmetry        [int] ['query', 'edit']
    Set the symmetry option on or off. When queried, returns an int for the option.

-----------------------------------------

t     : tolerance       [float] ['query', 'edit']
    Set the tolerance of reflection. When queried, returns a float of the tolerance.

-----------------------------------------

ts    : topoSymmetry    [boolean]
    Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.

    """

def alignCtx(q=1,e=1,a=1,afo=1,d=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",sat=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/alignCtx.html



-----------------------------------------

alignCtx is undoable, queryable, and editable.

The alignCtx command creates a tool for aligning and distributing objects.


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : align           [boolean] ['query', 'edit']
    Align objects

-----------------------------------------

afo   : anchorFirstObject [boolean] ['query', 'edit']
    Anchor first or last selected object. Default false. Only applicable when aligning objects.

-----------------------------------------

d     : distribute      [boolean] ['query', 'edit']
    Distribute objects

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

sat   : showAlignTouch  [boolean]
    Show or hide align touching handles. Default true. Only applicable when aligning objects.

    """

def arcLenDimContext(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/arcLenDimContext.html



-----------------------------------------

arcLenDimContext is undoable, queryable, and editable.

Command used to register the arcLenDimCtx tool.


-----------------------------------------


Return Value:

string  : name of the context created    
  
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

def art3dPaintCtx(q=1,e=1,aco=1,asc="string",abm="string",ast=1,atn="string",bsc="string",bra=1,bd="float",brf=1,brt="string",clr=1,cat="string",dsl="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",efc=1,eff="string",far="float",ftx="int",fty="int",fop="float",fal=1,fsl=1,ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,kar=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",n="string",op="float",o=1,owp=1,pm="string",pot="string",pta="string",ptn="string",psc="float",pwd="float",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,pm1="int",pm2="int",pm3="int",px1="float",px2="float",px3="float",ps1="float",ps2="float",ps3="float",psf="string",prm=1,r="float",rec=1,rn=1,rno=1,ra="string",rtf=1,rr="float",rft=1,rgb="[float, float, float]",fc="[float, float, float]",sts=1,sos=1,stx=1,scR="float",scs=1,hnm="string",spa=1,shn="string",sa=1,sod=1,stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,tfn=1,uet=1,up=1,wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/art3dPaintCtx.html



-----------------------------------------

art3dPaintCtx is undoable, queryable, and editable.

This is a tool context command for 3d Paint tool.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

abm   : alphablendmode  [string] ['query', 'edit']
    Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is "Default".

-----------------------------------------

ast   : assigntxt       [boolean] ['edit']
    Sends a request to the tool to allocate and assign file textures to the specified attibute on the selected shaders.

-----------------------------------------

atn   : attrnames       [string] ['query', 'edit']
    Name of attributes

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

bd    : brushdepth      [float] ['query', 'edit']
    Depth of the brush

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

brt   : brushtype       [string] ['query', 'edit']
    Name of the brush type

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

cat   : commonattr      [string] ['query']
    Returns a string with the names of all common to all the shaders paintable attributes and supported by the Paint Texture Tool.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

-----------------------------------------

efc   : extendFillColor [boolean] ['query', 'edit']
    States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.

-----------------------------------------

eff   : fileformat      [string] ['query', 'edit']
    Name of the file format

-----------------------------------------

far   : filetxtaspectratio [float] ['query', 'edit']
    Specifies the aspect ration of the texture width and height. Default is 1.

-----------------------------------------

ftx   : filetxtsizex    [int] ['query', 'edit']
    Specifies the width of the texture. Default is 256.

-----------------------------------------

fty   : filetxtsizey    [int] ['query', 'edit']
    Specifies the height of the texture. Default is 256.

-----------------------------------------

fop   : floodOpacity    [float] ['query', 'edit']
    Value of the flood opacity

-----------------------------------------

fal   : floodall        [boolean] ['query', 'edit']
    Turn on to flood everything

-----------------------------------------

fsl   : floodselect     [boolean] ['query', 'edit']
    Should the selected area be flooded?

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

kar   : keepaspectratio [boolean] ['query', 'edit']
    States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pta   : painttxtattr    [string] ['query', 'edit']
    Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor", "Reflectivity", "ReflectedColor", and user- defined float, float3, double, and double3 attributes. Default is "Color".

-----------------------------------------

ptn   : painttxtattrname [string] ['query', 'edit']
    Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.

-----------------------------------------

psc   : pfxScale        [float] ['query', 'edit']
    Specifies the scale for Paint Effect brushes.

-----------------------------------------

pwd   : pfxWidth        [float] ['query', 'edit']
    Specifies the width for Paint Effect brushes.

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

pm1   : pressureMapping1 [int] ['query', 'edit']
    First pressure mapping value

-----------------------------------------

pm2   : pressureMapping2 [int] ['query', 'edit']
    Second pressure mapping value

-----------------------------------------

pm3   : pressureMapping3 [int] ['query', 'edit']
    Third pressure mapping value

-----------------------------------------

px1   : pressureMax1    [float] ['query', 'edit']
    First pressure maximum value

-----------------------------------------

px2   : pressureMax2    [float] ['query', 'edit']
    Second pressure maximum value

-----------------------------------------

px3   : pressureMax3    [float] ['query', 'edit']
    Third pressure maximum value

-----------------------------------------

ps1   : pressureMin1    [float] ['query', 'edit']
    First pressure minimum value

-----------------------------------------

ps2   : pressureMin2    [float] ['query', 'edit']
    Second pressure minimum value

-----------------------------------------

ps3   : pressureMin3    [float] ['query', 'edit']
    Third pressure minimum value

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

rtf   : reloadtexfile   [boolean] ['edit']
    Sends a request to the tool to reload the texture from the disc.

-----------------------------------------

rr    : resizeratio     [float] ['query', 'edit']
    Specifies the scale by which to resize the current textures.

-----------------------------------------

rft   : resizetxt       [boolean] ['edit']
    Sends a request to the tool to resize all the currently in use textures.

-----------------------------------------

rgb   : rgbcolor        [[float, float, float]] ['query', 'edit']
    Colour value

-----------------------------------------

fc    : rgbflood        [[float, float, float]] ['query', 'edit']
    Color of the flood

-----------------------------------------

sts   : saveTextureOnStroke [boolean] ['query', 'edit']
    States if the original texture will be automatically saved on each stroke. Default is false.

-----------------------------------------

sos   : saveonstroke    [boolean] ['query', 'edit']
    States if the temporary texture will be automatically saved on each stroke. Default is false.

-----------------------------------------

stx   : savetexture     [boolean] ['edit']
    Sends a request to the tool to save the texture to the disc.

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

hnm   : shadernames     [string] ['query']
    Returns a string with the names of all shaders assigned to selected surfaces.

-----------------------------------------

spa   : shapeattr       [boolean] ['query', 'edit']
    States if the attribute to paint is an attribute of the shape and not the shader. Default is false.

-----------------------------------------

shn   : shapenames      [string] ['query']
    Returns a string with the names of all surfaces which are being painted on.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

sod   : soloAsDiffuse   [boolean] ['query', 'edit']
    States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tfn   : textureFilenames [boolean] ['query']
    Returns a string array with the names of all the painted file textures.

-----------------------------------------

uet   : updateEraseTex  [boolean] ['query', 'edit']
    Should the erase texture update?

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def artAttrCtx(q=1,e=1,aco=1,alp="string",asc="string",alc="string",acl="float",acu="float",asl="string",bsc="string",bra=1,brf=1,cl="string",cll="float",clu="float",clr=1,cl1="float",cl4="[float, float, float, float]",cl3="[float, float, float]",cr="string",cf=1,cfo=1,crl="float",cru="float",dti="int",dl=1,dsl="string",dsk="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",fon=1,ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,iu=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",mxv="float",miv="float",n="string",oaa="string",op="float",o=1,owp=1,pna="string",pas="string",pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,psf="string",prm=1,r="float",rxc="[float, float, float]",rmc="[float, float, float]",rec=1,rn=1,rno=1,ra="string",scR="float",scs=1,sao="string",sa=1,stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,tfp="string",top="string",ucr=1,umc=1,up=1,val="float",wst="string",wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artAttrCtx.html



-----------------------------------------

artAttrCtx is undoable, queryable, and editable.

This is a context command to set the flags on the artAttrContext, which is the
base context for attribute painting operations. All commands require the name
of the context as the last argument as this provides the name of the context
to create, edit or query.

This is a context command to set the flags on the Attribute Paint Tool
context.


-----------------------------------------


Return Value:

string  The name of the context created.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

alp   : activeListChangedProc [string] ['query', 'edit']
    Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

alc   : alphaclamp      [string] ['query', 'edit']
    Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

acl   : alphaclamplower [float] ['query', 'edit']
    Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

acu   : alphaclampupper [float] ['query', 'edit']
    Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

asl   : attrSelected    [string] ['query']
    Returns a name of the currently selected attribute. Q: When queried, it returns a string.

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

cl    : clamp           [string] ['query', 'edit']
    Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

cll   : clamplower      [float] ['query', 'edit']
    Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

clu   : clampupper      [float] ['query', 'edit']
    Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

cl1   : colorAlphaValue [float] ['query', 'edit']
    The Alpha value of the color.

-----------------------------------------

cl4   : colorRGBAValue  [[float, float, float, float]] ['query', 'edit']
    The RGBA value of the color.

-----------------------------------------

cl3   : colorRGBValue   [[float, float, float]] ['query', 'edit']
    The RGB value of the color.

-----------------------------------------

cr    : colorRamp       [string] ['query', 'edit']
    Allows a user defined color ramp to be used to map values to colors.

-----------------------------------------

cf    : colorfeedback   [boolean] ['query', 'edit']
    Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

cfo   : colorfeedbackOverride [boolean] ['query', 'edit']
    Sets on/off the color feedback override. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

crl   : colorrangelower [float] ['query', 'edit']
    Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

cru   : colorrangeupper [float] ['query', 'edit']
    Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

dti   : dataTypeIndex   [int] ['query', 'edit']
    When the selected paintable attribute is a vectorArray, it specifies which field to paint on.

-----------------------------------------

dl    : disablelighting [boolean] ['query', 'edit']
    If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dsk   : duringStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

-----------------------------------------

fon   : filterNodes     [boolean] ['edit']
    Sets the node filter.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

iu    : interactiveUpdate [boolean] ['query', 'edit']
    Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

mxv   : maxvalue        [float] ['query', 'edit']
    Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

miv   : minvalue        [float] ['query', 'edit']
    Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

oaa   : objattrArray    [string] ['query']
    An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pna   : paintNodeArray  [string] ['query']
    An array of paintable nodes. Q: When queried, it returns a string.

-----------------------------------------

pas   : paintattrselected [string] ['edit']
    An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rxc   : rampMaxColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is greater than or equal to the maximum value.

-----------------------------------------

rmc   : rampMinColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is less than or equal to the minimum value.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

sao   : selectedattroper [string] ['query', 'edit']
    Sets the edit weight operation. Four edit weights operations are provided : "absolute" \- the value of the weight is replaced by the current one, "additive" \- the value of the weight is added to the current one, "scale" \- the value of the weight is multiplied by the current one, "smooth" \- the value of the weight is divided by the current one. C: Default is "absolute". Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tfp   : toolOffProc     [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

top   : toolOnProc      [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

ucr   : useColorRamp    [boolean] ['query', 'edit']
    Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.

-----------------------------------------

umc   : useMaxMinColor  [boolean] ['query', 'edit']
    Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

val   : value           [float] ['query', 'edit']
    Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

wst   : whichTool       [string] ['query', 'edit']
    The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def artAttrPaintVertexCtx(q=1,e=1,aco=1,alp="string",asc="string",alc="string",acl="float",acu="float",asl="string",bsc="string",bra=1,brf=1,cl="string",cll="float",clu="float",clr=1,cl1="float",cl4="[float, float, float, float]",cl3="[float, float, float]",cr="string",cf=1,cfo=1,crl="float",cru="float",dti="int",dl=1,dsl="string",dsk="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",fon=1,ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,iu=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",mxv="float",miv="float",n="string",oaa="string",op="float",o=1,owp=1,pc="int",pna="string",pnc="int",pc4=1,pvf=1,pas="string",pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,psf="string",prm=1,r="float",rxc="[float, float, float]",rmc="[float, float, float]",rec=1,rn=1,rno=1,ra="string",scR="float",scs=1,sao="string",sa=1,stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,tfp="string",top="string",ucr=1,umc=1,up=1,val="float",vcr=1,vcl="float",vcu="float",wst="string",wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artAttrPaintVertexCtx.html



-----------------------------------------

artAttrPaintVertexCtx is undoable, queryable, and editable.

This is a context command to set the flags on the artAttrContext, which is the
base context for attribute painting operations. All commands require the name
of the context as the last argument as this provides the name of the context
to create, edit or query.

This is a context command to set the flags on the Paint color on vertex Tool
context.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

alp   : activeListChangedProc [string] ['query', 'edit']
    Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

alc   : alphaclamp      [string] ['query', 'edit']
    Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

acl   : alphaclamplower [float] ['query', 'edit']
    Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

acu   : alphaclampupper [float] ['query', 'edit']
    Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

asl   : attrSelected    [string] ['query']
    Returns a name of the currently selected attribute. Q: When queried, it returns a string.

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

cl    : clamp           [string] ['query', 'edit']
    Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

cll   : clamplower      [float] ['query', 'edit']
    Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

clu   : clampupper      [float] ['query', 'edit']
    Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

cl1   : colorAlphaValue [float] ['query', 'edit']
    The Alpha value of the color.

-----------------------------------------

cl4   : colorRGBAValue  [[float, float, float, float]] ['query', 'edit']
    The RGBA value of the color.

-----------------------------------------

cl3   : colorRGBValue   [[float, float, float]] ['query', 'edit']
    The RGB value of the color.

-----------------------------------------

cr    : colorRamp       [string] ['query', 'edit']
    Allows a user defined color ramp to be used to map values to colors.

-----------------------------------------

cf    : colorfeedback   [boolean] ['query', 'edit']
    Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

cfo   : colorfeedbackOverride [boolean] ['query', 'edit']
    Sets on/off the color feedback override. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

crl   : colorrangelower [float] ['query', 'edit']
    Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

cru   : colorrangeupper [float] ['query', 'edit']
    Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

dti   : dataTypeIndex   [int] ['query', 'edit']
    When the selected paintable attribute is a vectorArray, it specifies which field to paint on.

-----------------------------------------

dl    : disablelighting [boolean] ['query', 'edit']
    If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dsk   : duringStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

-----------------------------------------

fon   : filterNodes     [boolean] ['edit']
    Sets the node filter.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

iu    : interactiveUpdate [boolean] ['query', 'edit']
    Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

mxv   : maxvalue        [float] ['query', 'edit']
    Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

miv   : minvalue        [float] ['query', 'edit']
    Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

oaa   : objattrArray    [string] ['query']
    An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pc    : paintComponent  [int] ['query', 'edit']
    Specifies whether face or vertex or vertex face is being painted. 1 - Vertex 2 - VertexFace 3 - Face C: Default is Vertex. Q: When queried, it returns a int.

-----------------------------------------

pna   : paintNodeArray  [string] ['query']
    An array of paintable nodes. Q: When queried, it returns a string.

-----------------------------------------

pnc   : paintNumChannels [int] ['query', 'edit']
    Number of channels to paint - 1 (alpha), 3 (RGB), or 4 (RGBA)

-----------------------------------------

pc4   : paintRGBA       [boolean] ['query', 'edit']
    Specifies whether RGB or RGBA channels are being painted. TRUE: RGBA channels. FALSE: RGB channels. Alpha channel remains unaffected. C: Default is FALSE (Painting RGB channels). Q: When queried, it returns a int.

-----------------------------------------

pvf   : paintVertexFace [boolean] ['query', 'edit']
    Specifies whether vertex face is being painted. TRUE: Vertex face being painted. (Allows each face connected to the vertex to be painted) FALSE: Vertex being painted.(affects all connected faces) C: Default is FALSE. Q: When queried, it returns a int.

-----------------------------------------

pas   : paintattrselected [string] ['edit']
    An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rxc   : rampMaxColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is greater than or equal to the maximum value.

-----------------------------------------

rmc   : rampMinColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is less than or equal to the minimum value.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

sao   : selectedattroper [string] ['query', 'edit']
    Sets the edit weight operation. Four edit weights operations are provided : "absolute" \- the value of the weight is replaced by the current one, "additive" \- the value of the weight is added to the current one, "scale" \- the value of the weight is multiplied by the current one, "smooth" \- the value of the weight is divided by the current one. C: Default is "absolute". Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tfp   : toolOffProc     [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

top   : toolOnProc      [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

ucr   : useColorRamp    [boolean] ['query', 'edit']
    Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.

-----------------------------------------

umc   : useMaxMinColor  [boolean] ['query', 'edit']
    Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

val   : value           [float] ['query', 'edit']
    Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

vcr   : vertexColorRange [boolean] ['query', 'edit']
    Specifies whether the vertex color range should be applied to the currently selected object. C: Default is false Q: When queried, it returns a boolean.

-----------------------------------------

vcl   : vertexColorRangeLower [float] ['query', 'edit']
    Specifies the min value of the vertex color range. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

vcu   : vertexColorRangeUpper [float] ['query', 'edit']
    Specifies the max value of the vertex color range. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

wst   : whichTool       [string] ['query', 'edit']
    The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def artAttrSkinPaintCtx(q=1,e=1,aco=1,alp="string",asc="string",alc="string",acl="float",acu="float",asl="string",bsc="string",bra=1,brf=1,cl="string",cll="float",clu="float",clr=1,cl1="float",cl4="[float, float, float, float]",cl3="[float, float, float]",cr="string",cf=1,cfo=1,crl="float",cru="float",dti="int",dl=1,dsl="string",dsk="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",fon=1,ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,inf="string",iu=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",mxv="float",miv="float",n="string",oaa="string",op="float",o=1,owp=1,pna="string",psm="int",pas="string",pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,psf="string",prm=1,r="float",rxc="[float, float, float]",rmc="[float, float, float]",rec=1,rn=1,rno=1,ra="string",scR="float",scs=1,sao="string",sa=1,spm="int",stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,tfp="string",top="string",ucr=1,umc=1,up=1,val="float",wst="string",wlR="float",xry=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artAttrSkinPaintCtx.html



-----------------------------------------

artAttrSkinPaintCtx is undoable, queryable, and editable.

This is a context command to set the flags on the artAttrContext, which is the
base context for attribute painting operations. All commands require the name
of the context as the last argument as this provides the name of the context
to create, edit or query.

This is a context command to set the flags on the Paint skin weights tool
context.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

alp   : activeListChangedProc [string] ['query', 'edit']
    Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

alc   : alphaclamp      [string] ['query', 'edit']
    Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

acl   : alphaclamplower [float] ['query', 'edit']
    Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

acu   : alphaclampupper [float] ['query', 'edit']
    Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

asl   : attrSelected    [string] ['query']
    Returns a name of the currently selected attribute. Q: When queried, it returns a string.

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

cl    : clamp           [string] ['query', 'edit']
    Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

cll   : clamplower      [float] ['query', 'edit']
    Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

clu   : clampupper      [float] ['query', 'edit']
    Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

cl1   : colorAlphaValue [float] ['query', 'edit']
    The Alpha value of the color.

-----------------------------------------

cl4   : colorRGBAValue  [[float, float, float, float]] ['query', 'edit']
    The RGBA value of the color.

-----------------------------------------

cl3   : colorRGBValue   [[float, float, float]] ['query', 'edit']
    The RGB value of the color.

-----------------------------------------

cr    : colorRamp       [string] ['query', 'edit']
    Allows a user defined color ramp to be used to map values to colors.

-----------------------------------------

cf    : colorfeedback   [boolean] ['query', 'edit']
    Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

cfo   : colorfeedbackOverride [boolean] ['query', 'edit']
    Sets on/off the color feedback override. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

crl   : colorrangelower [float] ['query', 'edit']
    Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

cru   : colorrangeupper [float] ['query', 'edit']
    Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

dti   : dataTypeIndex   [int] ['query', 'edit']
    When the selected paintable attribute is a vectorArray, it specifies which field to paint on.

-----------------------------------------

dl    : disablelighting [boolean] ['query', 'edit']
    If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dsk   : duringStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

-----------------------------------------

fon   : filterNodes     [boolean] ['edit']
    Sets the node filter.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

inf   : influence       [string] ['query', 'edit']
    Specifies which joint has been selected by the user for painting. Q: When queried, it returns a string.

-----------------------------------------

iu    : interactiveUpdate [boolean] ['query', 'edit']
    Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

mxv   : maxvalue        [float] ['query', 'edit']
    Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

miv   : minvalue        [float] ['query', 'edit']
    Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

oaa   : objattrArray    [string] ['query']
    An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pna   : paintNodeArray  [string] ['query']
    An array of paintable nodes. Q: When queried, it returns a string.

-----------------------------------------

psm   : paintSelectMode [int] ['query', 'edit']
    Specifies whether the paint select tool: adds to selection (1) removes from selection (2), toggles selection (3) Q: When queried, it returns an int as defined above.

-----------------------------------------

pas   : paintattrselected [string] ['edit']
    An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rxc   : rampMaxColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is greater than or equal to the maximum value.

-----------------------------------------

rmc   : rampMinColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is less than or equal to the minimum value.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

sao   : selectedattroper [string] ['query', 'edit']
    Sets the edit weight operation. Four edit weights operations are provided : "absolute" \- the value of the weight is replaced by the current one, "additive" \- the value of the weight is added to the current one, "scale" \- the value of the weight is multiplied by the current one, "smooth" \- the value of the weight is divided by the current one. C: Default is "absolute". Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

spm   : skinPaintMode   [int] ['query', 'edit']
    Specifies whether the skin paint tool is in paint skin weights mode (1) Marquee select mode (0), or paint select mode (2) Q: When queried, it returns an int as defined above.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tfp   : toolOffProc     [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

top   : toolOnProc      [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

ucr   : useColorRamp    [boolean] ['query', 'edit']
    Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.

-----------------------------------------

umc   : useMaxMinColor  [boolean] ['query', 'edit']
    Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

val   : value           [float] ['query', 'edit']
    Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

wst   : whichTool       [string] ['query', 'edit']
    The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.

-----------------------------------------

wlR   : worldRadius     [float] ['query', 'edit']
    Radius in worldspace

-----------------------------------------

xry   : xrayJoints      [boolean]
    Specifies whether joints should be displayed in xray mode while painting Q: When queried, it returns a boolean.

    """

def artAttrTool(q=1,add="string",ex="string",rm="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artAttrTool.html



-----------------------------------------

artAttrTool is NOT undoable, queryable, and NOT editable.

The artAttrTool command manages the list of tool types which are used for
attribute painting. This command supports querying the list contents as well
as adding new tools to the list. Note that there is a set of built-in tools.
The list of built-ins can be queried by starting Maya and doing an
"artAttrTool -q".

The tools which are managed by this command are all intended for attribute
painting via Artisan: when you create a new context via artAttrCtx you specify
the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
simply use one of the built-in tools. However, if you need to have custom
Properties and Values sheets asscociated with your tool, you will need to
define a custom tool via artAttrTool -add "toolName". For an example of a
custom attribute painting tool, see the devkit example customtoolPaint.mel.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

      : add             [string] []
    Adds the named tool to the internal list of tools.

-----------------------------------------

ex    : exists          [string] ['query']
    Checks if the named tool exists, returning true if found, and false otherwise.

-----------------------------------------

rm    : remove          [string]
    Removes the named tool from the internal list of tools.

    """

def artFluidAttrCtx(q=1,e=1,aco=1,alp="string",asc="string",alc="string",acl="float",acu="float",asl="string",autoSave="string",bsc="string",bra=1,brf=1,cl="string",cll="float",clu="float",clr=1,cl1="float",cl4="[float, float, float, float]",cl3="[float, float, float]",cr="string",cf=1,cfo=1,crl="float",cru="float",cpf="string",dti="int",dsc=1,dl=1,dar=1,dv=1,das=1,dsl="string",dsk="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",fon=1,ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,iu=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",mxv="float",miv="float",n="string",oaa="string",op="float",o=1,owp=1,pna="string",pas="string",pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,psf="string",prm=1,p="string",r="float",rxc="[float, float, float]",rmc="[float, float, float]",rec=1,rn=1,rno=1,ra="string",rgb="[float, float, float]",scR="float",scs=1,sao="string",sa=1,stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,tfp="string",top="string",ucr=1,umc=1,usd=1,up=1,val="float",v="[float, float, float]",wst="string",wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artFluidAttrCtx.html



-----------------------------------------

artFluidAttrCtx is undoable, queryable, and editable.

This is a context command to set the flags on the artAttrContext, which is the
base context for attribute painting operations. All commands require the name
of the context as the last argument as this provides the name of the context
to create, edit or query.

This command is used to paint properties (such as density) of selected fluid
volumes.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

alp   : activeListChangedProc [string] ['query', 'edit']
    Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

alc   : alphaclamp      [string] ['query', 'edit']
    Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

acl   : alphaclamplower [float] ['query', 'edit']
    Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

acu   : alphaclampupper [float] ['query', 'edit']
    Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

asl   : attrSelected    [string] ['query']
    Returns a name of the currently selected attribute. Q: When queried, it returns a string.

-----------------------------------------

autoSave : autoSave        [string] ['query', 'edit']
    A MEL command to save the fluid state. Called before an event which could overwrite unsaved values of painted fluid properties. Such events include: changing current time, changing the current paintable property, and exiting the paint tool. (To turn auto-save off, pass in an empty-valued string argument: e.g., "".)

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

cl    : clamp           [string] ['query', 'edit']
    Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

cll   : clamplower      [float] ['query', 'edit']
    Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

clu   : clampupper      [float] ['query', 'edit']
    Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

cl1   : colorAlphaValue [float] ['query', 'edit']
    The Alpha value of the color.

-----------------------------------------

cl4   : colorRGBAValue  [[float, float, float, float]] ['query', 'edit']
    The RGBA value of the color.

-----------------------------------------

cl3   : colorRGBValue   [[float, float, float]] ['query', 'edit']
    The RGB value of the color.

-----------------------------------------

cr    : colorRamp       [string] ['query', 'edit']
    Allows a user defined color ramp to be used to map values to colors.

-----------------------------------------

cf    : colorfeedback   [boolean] ['query', 'edit']
    Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

cfo   : colorfeedbackOverride [boolean] ['query', 'edit']
    Sets on/off the color feedback override. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

crl   : colorrangelower [float] ['query', 'edit']
    Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

cru   : colorrangeupper [float] ['query', 'edit']
    Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

cpf   : currentPaintableFluid [string] ['query']
    Query the name of the fluid on which this context is currently painting. Returns string.

-----------------------------------------

dti   : dataTypeIndex   [int] ['query', 'edit']
    When the selected paintable attribute is a vectorArray, it specifies which field to paint on.

-----------------------------------------

dsc   : delaySelectionChanged [boolean] ['query', 'edit']
    Internal use only. Under normal conditions, the tool responds to changes to the selection list so it can update its list of paintable geometry. When -dsl true is used, the tool will not update its paintable list until a corresponding -dsl false is called.

-----------------------------------------

dl    : disablelighting [boolean] ['query', 'edit']
    If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

dar   : displayAsRender [boolean] ['query', 'edit']
    When true, sets the "Shaded Display" attribute of the fluid to "AsRender": all fluid properties displayed as hardware rendered. When false, displays only the currently selected paintable attribute of the fluid.

-----------------------------------------

dv    : displayVelocity [boolean] ['query', 'edit']
    Turns on/off velocity display, independently of the above "dar/displayAsRender" setting. Use this flag to enable velocity display while only displaying density, for example.

-----------------------------------------

das   : doAutoSave      [boolean] ['edit']
    Execute the -autoSave command if there are unsaved painted fluid properties.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dsk   : duringStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

-----------------------------------------

fon   : filterNodes     [boolean] ['edit']
    Sets the node filter.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

iu    : interactiveUpdate [boolean] ['query', 'edit']
    Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

mxv   : maxvalue        [float] ['query', 'edit']
    Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

miv   : minvalue        [float] ['query', 'edit']
    Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

oaa   : objattrArray    [string] ['query']
    An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pna   : paintNodeArray  [string] ['query']
    An array of paintable nodes. Q: When queried, it returns a string.

-----------------------------------------

pas   : paintattrselected [string] ['edit']
    An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

p     : property        [string] ['query', 'edit']
    Specifies a property to paint on the fluid. Valid values are "color", "density", "densityAndColor," "densityAndFuel," "temperature," "fuel", "velocity".

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rxc   : rampMaxColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is greater than or equal to the maximum value.

-----------------------------------------

rmc   : rampMinColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is less than or equal to the minimum value.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

rgb   : rgbValue        [[float, float, float]] ['query', 'edit']
    Specifies the values of the red, green, and blue components of the color to use when painting the property "color."

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

sao   : selectedattroper [string] ['query', 'edit']
    Sets the edit weight operation. Four edit weights operations are provided : "absolute" \- the value of the weight is replaced by the current one, "additive" \- the value of the weight is added to the current one, "scale" \- the value of the weight is multiplied by the current one, "smooth" \- the value of the weight is divided by the current one. C: Default is "absolute". Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tfp   : toolOffProc     [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

top   : toolOnProc      [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

ucr   : useColorRamp    [boolean] ['query', 'edit']
    Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.

-----------------------------------------

umc   : useMaxMinColor  [boolean] ['query', 'edit']
    Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.

-----------------------------------------

usd   : useStrokeDirection [boolean] ['query', 'edit']
    Applicable only during "velocity" painting. Specifies whether the value of the painted velocity should come from the direction of the brush stroke, overriding the value specified by the -v/-velocity flag.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

val   : value           [float] ['query', 'edit']
    Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

v     : velocity        [[float, float, float]] ['query', 'edit']
    Specifies the values of the x, y, and z components of the velocity to use when painting the property "velocity".

-----------------------------------------

wst   : whichTool       [string] ['query', 'edit']
    The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def artPuttyCtx(q=1,e=1,aco=1,alp="string",asc="string",alc="string",acl="float",acu="float",asl="string",asm=1,bsc="string",bs="float",bra=1,brf=1,cl="string",cll="float",clu="float",clr=1,clc="float",cl1="float",cl4="[float, float, float, float]",cl3="[float, float, float]",cr="string",cf=1,cfo=1,crl="float",cru="float",dti="int",dl=1,dde=1,din=1,dsl="string",dsk="string",dcm=1,eut=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",fon=1,ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,iu=1,irv=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",md="float",mxv="float",miv="float",mth="string",mtm="string",mtt="string",n="string",oaa="string",op="float",o=1,owp=1,pna="string",pas="string",pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcv=1,pcs=1,psf="string",prm=1,r="float",rxc="[float, float, float]",rmc="[float, float, float]",rec=1,rn=1,rno=1,ra="string",rs=1,rv="string",rvu="float",rvv="float",scR="float",scs=1,sao="string",sa=1,si="int",stD="float",stP="string",stS="float",stc=1,sef=1,stt="string",ssm="string",scv=1,tab=1,to=1,tfp="string",top="string",ues=1,urs=1,ucr=1,umc=1,up=1,val="float",wst="string",wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artPuttyCtx.html



-----------------------------------------

artPuttyCtx is undoable, queryable, and editable.

This is a context command to set the flags on the artAttrContext, which is the
base context for attribute painting operations. All commands require the name
of the context as the last argument as this provides the name of the context
to create, edit or query.

This command is used to modify NURBS surfaces using a brush based interface
(Maya Artisan). This is accomplished by moving the control vertices (CVs)
under the brush in the specified direction.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

alp   : activeListChangedProc [string] ['query', 'edit']
    Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

alc   : alphaclamp      [string] ['query', 'edit']
    Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

acl   : alphaclamplower [float] ['query', 'edit']
    Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

acu   : alphaclampupper [float] ['query', 'edit']
    Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

asl   : attrSelected    [string] ['query']
    Returns a name of the currently selected attribute. Q: When queried, it returns a string.

-----------------------------------------

asm   : autosmooth      [boolean] ['query', 'edit']
    Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bs    : brushStrength   [float] ['query', 'edit']
    Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the motion of the brush. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

cl    : clamp           [string] ['query', 'edit']
    Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

cll   : clamplower      [float] ['query', 'edit']
    Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

clu   : clampupper      [float] ['query', 'edit']
    Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

clc   : collapsecvtol   [float] ['query', 'edit']
    Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm. Q: When queried, it returns a float.

-----------------------------------------

cl1   : colorAlphaValue [float] ['query', 'edit']
    The Alpha value of the color.

-----------------------------------------

cl4   : colorRGBAValue  [[float, float, float, float]] ['query', 'edit']
    The RGBA value of the color.

-----------------------------------------

cl3   : colorRGBValue   [[float, float, float]] ['query', 'edit']
    The RGB value of the color.

-----------------------------------------

cr    : colorRamp       [string] ['query', 'edit']
    Allows a user defined color ramp to be used to map values to colors.

-----------------------------------------

cf    : colorfeedback   [boolean] ['query', 'edit']
    Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

cfo   : colorfeedbackOverride [boolean] ['query', 'edit']
    Sets on/off the color feedback override. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

crl   : colorrangelower [float] ['query', 'edit']
    Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

cru   : colorrangeupper [float] ['query', 'edit']
    Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

dti   : dataTypeIndex   [int] ['query', 'edit']
    When the selected paintable attribute is a vectorArray, it specifies which field to paint on.

-----------------------------------------

dl    : disablelighting [boolean] ['query', 'edit']
    If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

dde   : dispdecr        [boolean] ['edit']
    Decreases a maximum displacement by 10%.

-----------------------------------------

din   : dispincr        [boolean] ['edit']
    Increases a maximum displacement by 10%.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dsk   : duringStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

eut   : erasesrfupd     [boolean] ['query', 'edit']
    Toggles the update for the erase surface

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

-----------------------------------------

fon   : filterNodes     [boolean] ['edit']
    Sets the node filter.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

iu    : interactiveUpdate [boolean] ['query', 'edit']
    Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

irv   : invertrefvector [boolean] ['query', 'edit']
    Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

md    : maxdisp         [float] ['query', 'edit']
    Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

mxv   : maxvalue        [float] ['query', 'edit']
    Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

miv   : minvalue        [float] ['query', 'edit']
    Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

mth   : mouldtypehead   [string] ['query', 'edit']
    Type of type mould to use

-----------------------------------------

mtm   : mouldtypemouse  [string] ['query', 'edit']
    Specifies the putty operations/mode ("push" \- pushes CVs along the given direction (see refvector flag), "pull" \- pulls CVs along the specified direction, "smooth" \- smooths the sculpt, "erase" \- erases the paint). C: Default is "push". Q: When queried, it returns a string.

-----------------------------------------

mtt   : mouldtypetail   [string] ['query', 'edit']
    Type of eraser mould to use

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

oaa   : objattrArray    [string] ['query']
    An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pna   : paintNodeArray  [string] ['query']
    An array of paintable nodes. Q: When queried, it returns a string.

-----------------------------------------

pas   : paintattrselected [string] ['edit']
    An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcv   : polecv          [boolean] ['query', 'edit']
    Pull all the pole CVs to the same position.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rxc   : rampMaxColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is greater than or equal to the maximum value.

-----------------------------------------

rmc   : rampMinColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is less than or equal to the minimum value.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

rs    : refsurface      [boolean] ['query', 'edit']
    Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button (see updaterefsrf). C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

rv    : refvector       [string] ['query', 'edit']
    Specifies the direction of the push/pull operation ("normal" \- sculpt along normals, "firstnormal" \- sculpt along the first normal of the stroke, "view" \- sculpt along the view direction, "xaxis", "yaxis", "zaxis" \- sculpt along a given axis directions, "uisoparm", "visoparm" \- sculpt along U or V isoparametric lines), "uvvector" \- sculpt along an arbitrary vector in UV space. C: Default is "normal". Q: When queried, it returns a string.

-----------------------------------------

rvu   : refvectoru      [float] ['query', 'edit']
    Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".

-----------------------------------------

rvv   : refvectorv      [float] ['query', 'edit']
    Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

sao   : selectedattroper [string] ['query', 'edit']
    Sets the edit weight operation. Four edit weights operations are provided : "absolute" \- the value of the weight is replaced by the current one, "additive" \- the value of the weight is added to the current one, "scale" \- the value of the weight is multiplied by the current one, "smooth" \- the value of the weight is divided by the current one. C: Default is "absolute". Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

si    : smoothiters     [int] ['query', 'edit']
    Sets the quality of the smoothing operation (number of iterations). C: Default is 3. Q: When queried, it returns an int.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

stc   : stitchcorner    [boolean] ['query', 'edit']
    Sets on/off the stitching corner mode C: Default is "off". Q: When queried, it returns a boolean.

-----------------------------------------

sef   : stitchedgeflood [boolean] ['edit']
    Triggers postprocessing stitching edge procedure.

-----------------------------------------

stt   : stitchtype      [string] ['query', 'edit']
    Sets on/off the stitching mode ( "off" \- stitching is turned off, "position" \- position stitching is done without taking care about the tangent continuity C0, "tan" \- C1 continuity is preserved). C: Default is "position". Q: When queried, it returns a string.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tfp   : toolOffProc     [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

top   : toolOnProc      [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

ues   : updateerasesrf  [boolean] ['edit']
    Updates the erase surface.

-----------------------------------------

urs   : updaterefsrf    [boolean] ['edit']
    Updates the reference surface.

-----------------------------------------

ucr   : useColorRamp    [boolean] ['query', 'edit']
    Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.

-----------------------------------------

umc   : useMaxMinColor  [boolean] ['query', 'edit']
    Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

val   : value           [float] ['query', 'edit']
    Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

wst   : whichTool       [string] ['query', 'edit']
    The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def artSelectCtx(q=1,e=1,aco=1,ads=1,asc="string",bsc="string",bra=1,brf=1,clr=1,dsl="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,ift="float",lrc="string",lsn="string",lr="float",mst="uint",mp="string",n="string",op="float",o=1,owp=1,pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,psf="string",prm=1,r="float",rec=1,rn=1,rno=1,ra="string",scR="float",sal=1,scs=1,sop="string",sa=1,stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,tal=1,ual=1,up=1,wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artSelectCtx.html



-----------------------------------------

artSelectCtx is undoable, queryable, and editable.

This command is used to select/deselect/toggle components on selected surfaces
using a brush interface (Maya Artisan). Since, it selects components of the
surface, it only works in the component mode.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

ads   : addselection    [boolean] ['query', 'edit']
    If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

ift   : importthreshold [float] ['query', 'edit']
    Specifies the threshold for the import of the attribute maps. C: Default is 0.5. Q: When queried, it returns a float.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

sal   : selectall       [boolean] ['edit']
    Selects all vertices/egdes/faces/uvs.

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

sop   : selectop        [string] ['query', 'edit']
    Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tal   : toggleall       [boolean] ['edit']
    Toggle all vertices/egdes/faces/uvs.

-----------------------------------------

ual   : unselectall     [boolean] ['edit']
    Unselects all vertices/egdes/faces/uvs.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def artSetPaintCtx(q=1,e=1,aco=1,asc="string",bsc="string",bra=1,brf=1,clr=1,dsl="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",n="string",osn="string",op="float",o=1,owp=1,pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,psf="string",prm=1,r="float",rec=1,rn=1,rno=1,ra="string",scR="float",scs=1,scf=1,dcv=1,sot="string",stm="string",sa=1,stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,up=1,wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artSetPaintCtx.html



-----------------------------------------

artSetPaintCtx is undoable, queryable, and editable.

This tool allows the user to modify the set membership (add, transfer, remove
cvs) on nurbs surfaces using Maya Artisan's interface.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

osn   : objectsetnames  [string] ['query', 'edit']
    Default name of object sets

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

scf   : setcolorfeedback [boolean] ['query', 'edit']
    Specifies if the color feedback is on or off. C: Default is ON. Q: When queried, it returns a boolean.

-----------------------------------------

dcv   : setdisplaycvs   [boolean] ['query', 'edit']
    Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.

-----------------------------------------

sot   : setopertype     [string] ['query', 'edit']
    Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.

-----------------------------------------

stm   : settomodify     [string] ['query', 'edit']
    Specifies the name of the set to modify. Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def artUserPaintCtx(q=1,e=1,aco=1,alp="string",asc="string",alc="string",acl="float",acu="float",asl="string",bsc="string",bra=1,brf=1,cc="string",cl="string",cll="float",clu="float",clr=1,cl1="float",cl4="[float, float, float, float]",cl3="[float, float, float]",cr="string",cf=1,cfo=1,crl="float",cru="float",dti="int",dl=1,dsl="string",dsk="string",dcm=1,ex=1,eef=1,ear="float",efm="string",esf="string",fsx="int",fsy="int",eft="string",fon=1,fc="string",fp=1,gac="string",gsc="string",gvc="string",ch=1,i1="string",i2="string",i3="string",ifl="string",ifm="string",irm=1,ic="string",iu=1,lrc="string",lsn="string",lr="float",mst="uint",mp="string",mxv="float",miv="float",n="string",oaa="string",op="float",o=1,owp=1,pna="string",pas="string",pm="string",pot="string",pcm=1,pv=1,plc="[float, float]",plp="float",pcs=1,psf="string",prm=1,r="float",rxc="[float, float, float]",rmc="[float, float, float]",rec=1,rn=1,rno=1,ra="string",scR="float",scs=1,sao="string",sac="string",svc="string",sa=1,stD="float",stP="string",stS="float",ssm="string",scv=1,tab=1,to=1,tcc="string",tfp="string",top="string",tsc="string",ucr=1,umc=1,up=1,val="float",wst="string",wlR="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/artUserPaintCtx.html



-----------------------------------------

artUserPaintCtx is undoable, queryable, and editable.

This is a context command to set the flags on the artAttrContext, which is the
base context for attribute painting operations. All commands require the name
of the context as the last argument as this provides the name of the context
to create, edit or query.

This command executes a scriptable paint (Maya Artisan). It allows the user to
apply Mel commands/scripts to modify cvs' attributes for all cvs under the
paint brush.


-----------------------------------------


Return Value:

string  The name of the context created.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aco   : accopacity      [boolean] ['query', 'edit']
    Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.

-----------------------------------------

alp   : activeListChangedProc [string] ['query', 'edit']
    Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

asc   : afterStrokeCmd  [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

alc   : alphaclamp      [string] ['query', 'edit']
    Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

acl   : alphaclamplower [float] ['query', 'edit']
    Specifies the lower bound for the alpha values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

acu   : alphaclampupper [float] ['query', 'edit']
    Specifies the upper bound for the alpha values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

asl   : attrSelected    [string] ['query']
    Returns a name of the currently selected attribute. Q: When queried, it returns a string.

-----------------------------------------

bsc   : beforeStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

bra   : brushalignment  [boolean] ['query', 'edit']
    Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.

-----------------------------------------

brf   : brushfeedback   [boolean] ['query', 'edit']
    Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

cc    : chunkCommand    [string] ['query', 'edit']
    Specifies th name of the Mel script/procedure that is called once for every selected surface when a chunk is received on that surface. Q: When queried, it returns a string.

-----------------------------------------

cl    : clamp           [string] ['query', 'edit']
    Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" \- no clamping is performed, "lower" \- clamps only to the lower bound, "upper" \- clamps only to the upper bounds, "both" \- clamps to the lower and upper bounds. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

cll   : clamplower      [float] ['query', 'edit']
    Specifies the lower bound for the values. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

clu   : clampupper      [float] ['query', 'edit']
    Specifies the upper bound for the values. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Floods all cvs/vertices to the current value.

-----------------------------------------

cl1   : colorAlphaValue [float] ['query', 'edit']
    The Alpha value of the color.

-----------------------------------------

cl4   : colorRGBAValue  [[float, float, float, float]] ['query', 'edit']
    The RGBA value of the color.

-----------------------------------------

cl3   : colorRGBValue   [[float, float, float]] ['query', 'edit']
    The RGB value of the color.

-----------------------------------------

cr    : colorRamp       [string] ['query', 'edit']
    Allows a user defined color ramp to be used to map values to colors.

-----------------------------------------

cf    : colorfeedback   [boolean] ['query', 'edit']
    Sets on/off the color feedback display. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

cfo   : colorfeedbackOverride [boolean] ['query', 'edit']
    Sets on/off the color feedback override. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

crl   : colorrangelower [float] ['query', 'edit']
    Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

cru   : colorrangeupper [float] ['query', 'edit']
    Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

dti   : dataTypeIndex   [int] ['query', 'edit']
    When the selected paintable attribute is a vectorArray, it specifies which field to paint on.

-----------------------------------------

dl    : disablelighting [boolean] ['query', 'edit']
    If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

dsl   : dragSlider      [string] ['edit']
    Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".

-----------------------------------------

dsk   : duringStrokeCmd [string] ['query', 'edit']
    The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command

-----------------------------------------

dcm   : dynclonemode    [boolean] ['query', 'edit']
    Enable or disable dynamic clone mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eef   : expandfilename  [boolean] ['edit']
    If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.

-----------------------------------------

ear   : exportaspectratio [float] ['query', 'edit']
    Value of aspect ratio for export

-----------------------------------------

efm   : exportfilemode  [string] ['query', 'edit']
    Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.

-----------------------------------------

esf   : exportfilesave  [string] ['edit']
    Exports the attribute map and saves to a specified file.

-----------------------------------------

fsx   : exportfilesizex [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

fsy   : exportfilesizey [int] ['query', 'edit']
    Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.

-----------------------------------------

eft   : exportfiletype  [string] ['query', 'edit']
    Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.

-----------------------------------------

fon   : filterNodes     [boolean] ['edit']
    Sets the node filter.

-----------------------------------------

fc    : finalizeCmd     [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called at the end of each stroke. Q: When queried, it returns a string.

-----------------------------------------

fp    : fullpaths       [boolean] ['query', 'edit']
    Specifies whether full path names should be used when surface names are passed to scripts. If false, just the surface name is passed. C: Default is false Q: When queried, it returns a boolean.

-----------------------------------------

gac   : getArrayAttrCommand [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called once for every surface that is selected for painting. This procedure returns a string, which is interpreted as a list of names referring to double array attributes on some dependency node. Q: When queried, it returns a string.

-----------------------------------------

gsc   : getSurfaceCommand [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called once for every dependency node on the selection list, whenever Artisan processes the selection list. It returns the name of the surface to paint on. Q: When queried, it returns a string.

-----------------------------------------

gvc   : getValueCommand [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called every time a value on the surface is needed by the scriptable paint tool. Q: When queried, it returns a string.

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

ifl   : importfileload  [string] ['edit']
    Load the attribute map a specified file.

-----------------------------------------

ifm   : importfilemode  [string] ['query', 'edit']
    Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.

-----------------------------------------

irm   : importreassign  [boolean] ['query', 'edit']
    Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

ic    : initializeCmd   [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called in the beginning of each stroke. Q: When queried, it returns a string.

-----------------------------------------

iu    : interactiveUpdate [boolean] ['query', 'edit']
    Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

lrc   : lastRecorderCmd [string] ['query', 'edit']
    Value of last recorded command.

-----------------------------------------

lsn   : lastStampName   [string] ['query', 'edit']
    Value of the last stamp name.

-----------------------------------------

lr    : lowerradius     [float] ['query', 'edit']
    Sets the lower size of the brush (only apply on tablet).

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

mp    : mappressure     [string] ['query', 'edit']
    Sets the tablet pressure mapping when the table is used. There are four options: "none" \- the pressure has no effect, "opacity" \- the pressure is mapped to the opacity, "radius" \- the is mapped to modify the radius of the brush, "both" \- the pressure modifies both the opacity and the radius. C: Default is "none". Q: When queried, it returns a string.

-----------------------------------------

mxv   : maxvalue        [float] ['query', 'edit']
    Specifies the maximum value for each attribute. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

miv   : minvalue        [float] ['query', 'edit']
    Specifies the minimum value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

oaa   : objattrArray    [string] ['query']
    An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.

-----------------------------------------

op    : opacity         [float] ['query', 'edit']
    Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.

-----------------------------------------

o     : outline         [boolean] ['query', 'edit']
    Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

owp   : outwhilepaint   [boolean] ['query', 'edit']
    Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.

-----------------------------------------

pna   : paintNodeArray  [string] ['query']
    An array of paintable nodes. Q: When queried, it returns a string.

-----------------------------------------

pas   : paintattrselected [string] ['edit']
    An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.

-----------------------------------------

pm    : paintmode       [string] ['query', 'edit']
    Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.

-----------------------------------------

pot   : paintoperationtype [string] ['query', 'edit']
    Specifies the operation type used by the Paint Tool. Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".

-----------------------------------------

pcm   : pickColor       [boolean] ['query', 'edit']
    Set pick color mode on or off

-----------------------------------------

pv    : pickValue       [boolean] ['query', 'edit']
    Toggle for picking

-----------------------------------------

plc   : playbackCursor  [[float, float]] ['query', 'edit']
    Values for the playback cursor.

-----------------------------------------

plp   : playbackPressure [float] ['query', 'edit']
    Valus for the playback pressure.

-----------------------------------------

pcs   : preserveclonesource [boolean] ['query', 'edit']
    Whether or not to preserve a clone source.

-----------------------------------------

psf   : profileShapeFile [string] ['query', 'edit']
    Passes a name of the image file for the stamp shape profile.

-----------------------------------------

prm   : projective      [boolean] ['query', 'edit']
    Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.

-----------------------------------------

rxc   : rampMaxColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is greater than or equal to the maximum value.

-----------------------------------------

rmc   : rampMinColor    [[float, float, float]] ['query', 'edit']
    Defines a special color to be used when the value is less than or equal to the minimum value.

-----------------------------------------

rec   : record          [boolean] ['query', 'edit']
    Toggle on for recording.

-----------------------------------------

rn    : reflection      [boolean] ['query', 'edit']
    Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.

-----------------------------------------

rno   : reflectionaboutorigin [boolean] ['query', 'edit']
    Toggle on to reflect about the origin

-----------------------------------------

ra    : reflectionaxis  [string] ['query', 'edit']
    Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.

-----------------------------------------

scR   : screenRadius    [float] ['query', 'edit']
    Brush radius on the screen

-----------------------------------------

scs   : selectclonesource [boolean] ['query', 'edit']
    Toggle on to select the clone source

-----------------------------------------

sao   : selectedattroper [string] ['query', 'edit']
    Sets the edit weight operation. Four edit weights operations are provided : "absolute" \- the value of the weight is replaced by the current one, "additive" \- the value of the weight is added to the current one, "scale" \- the value of the weight is multiplied by the current one, "smooth" \- the value of the weight is divided by the current one. C: Default is "absolute". Q: When queried, it returns a string.

-----------------------------------------

sac   : setArrayValueCommand [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called for each paint stamp. A stamp may affect one or more values on the surface. This call rolls up all the calls that would be made to setValueCommand for the stamp into one call with array arguments. Q: When queried, it returns a string.

-----------------------------------------

svc   : setValueCommand [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called every time a value on the surface is changed. Q: When queried, it returns a string.

-----------------------------------------

sa    : showactive      [boolean] ['query', 'edit']
    Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.

-----------------------------------------

stD   : stampDepth      [float] ['query', 'edit']
    Depth of the stamps

-----------------------------------------

stP   : stampProfile    [string] ['query', 'edit']
    Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.

-----------------------------------------

stS   : stampSpacing    [float] ['query', 'edit']
    Specifies the stamp spacing. Default is 1.0.

-----------------------------------------

ssm   : strokesmooth    [string] ['query', 'edit']
    Stroke smoothing type name

-----------------------------------------

scv   : surfaceConformedBrushVertices [boolean] ['query', 'edit']
    Enables/disables the the display of the effective brush area as affected vertices.

-----------------------------------------

tab   : tablet          [boolean] ['query']
    Returns true if the tablet device is present, false if it is absent

-----------------------------------------

to    : tangentOutline  [boolean] ['query', 'edit']
    Enables/disables the display of the brush circle tangent to the surface.

-----------------------------------------

tcc   : toolCleanupCmd  [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called when this tool is exited. Q: When queried, it returns a string.

-----------------------------------------

tfp   : toolOffProc     [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

top   : toolOnProc      [string] ['query', 'edit']
    Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.

-----------------------------------------

tsc   : toolSetupCmd    [string] ['query', 'edit']
    Specifies the name of the Mel script/procedure that is called once for every selected surface when an initial click is received on that surface. Q: When queried, it returns a string.

-----------------------------------------

ucr   : useColorRamp    [boolean] ['query', 'edit']
    Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.

-----------------------------------------

umc   : useMaxMinColor  [boolean] ['query', 'edit']
    Specifies whether the out of range colors should be used. See rampMinColor and rampMaxColor flags for further details.

-----------------------------------------

up    : usepressure     [boolean] ['query', 'edit']
    Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.

-----------------------------------------

val   : value           [float] ['query', 'edit']
    Specifies the value for each attribute. C: Default is 0.0. Q: When queried, it returns a float.

-----------------------------------------

wst   : whichTool       [string] ['query', 'edit']
    The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.

-----------------------------------------

wlR   : worldRadius     [float]
    Radius in worldspace

    """

def boxDollyCtx(q=1,e=1,ac=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",tn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/boxDollyCtx.html



-----------------------------------------

boxDollyCtx is undoable, queryable, and editable.

This command can be used to create, edit, or query a dolly context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

tn    : toolName        [string]
    Name of the specific tool to which this command refers.

    """

def boxZoomCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",zs="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/boxZoomCtx.html



-----------------------------------------

boxZoomCtx is undoable, queryable, and editable.

This command can be used to create, edit, or query a box zoom context. If this
context is used on a perspective camera, the field of view and view direction
are changed. If the camera is orthographic, the orthographic width and eye
point are changed. The left and middle mouse interactively zoom the view. The
control key can be used to enable box zoom. A box starting from left to right
will zoom in, and a box starting from right to left will zoom out.


-----------------------------------------


Return Value:

string  The name of the context    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

zs    : zoomScale       [float]
    Scale the zoom.

    """

def clipEditorCurrentTimeCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/clipEditorCurrentTimeCtx.html



-----------------------------------------

clipEditorCurrentTimeCtx is undoable, queryable, and editable.

This command creates a context which may be used to change current time within
the track area of a clip editor.


-----------------------------------------


Return Value:

string  Context name    
  
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

def contextInfo(q=1,e=1,c=1,esc=1,ex=1,i1=1,i2=1,i3=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/contextInfo.html



-----------------------------------------

contextInfo is undoable, queryable, and editable.

This command allows you to get information on named contexts.


-----------------------------------------


Return Value:

string  Info requested    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : c               [boolean] []
    Return the class type of the named context.

-----------------------------------------

esc   : escapeContext   [boolean] []
    Return the command string that will allow you to exit the current tool.

-----------------------------------------

ex    : exists          [boolean] []
    Return true if the context exists, false if it does not exists (or is internal and therefore untouchable)

-----------------------------------------

i1    : image1          [boolean] []
    Returns the name of an xpm associated with the named context.

-----------------------------------------

i2    : image2          [boolean] []
    Returns the name of an xpm associated with the named context.

-----------------------------------------

i3    : image3          [boolean] []
    Returns the name of an xpm associated with the named context.

-----------------------------------------

t     : title           [boolean]
    Return the title string of the named context.

    """

def ctxAbort():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ctxAbort.html



-----------------------------------------

ctxAbort is undoable, NOT queryable, and NOT editable.

This command tells the current context to reset itself, losing what has been
done so far. If a escape context has been set it then makes that context
current.


-----------------------------------------


Return Value:

None
    """

def ctxCompletion():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ctxCompletion.html



-----------------------------------------

ctxCompletion is undoable, NOT queryable, and NOT editable.

This command tells the current context to finish what it is doing and create
any objects that is is working on.


-----------------------------------------


Return Value:

None
    """

def ctxEditMode(btd=1,btu=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ctxEditMode.html



-----------------------------------------

ctxEditMode is undoable, NOT queryable, and NOT editable.

This command tells the current context to switch edit modes.  
It acts as a toggle.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

btd   : buttonDown      [boolean] []
    Edit mode is being invoked from a hotkey press event.

-----------------------------------------

btu   : buttonUp        [boolean]
    Edit mode is being invoked from a hotkey release event.

    """

def ctxTraverse(d=1,l=1,r=1,up=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ctxTraverse.html



-----------------------------------------

ctxTraverse is undoable, NOT queryable, and NOT editable.

This command tells the current context to do a traversal.

  
Some contexts will ignore this command. Individual contexts determine what
up/down left/right mean.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

d     : down            [boolean] []
    Move "down" as defined by the current context.

-----------------------------------------

l     : left            [boolean] []
    Move "left" as defined by the current context.

-----------------------------------------

r     : right           [boolean] []
    Move "right" as defined by the current context.

-----------------------------------------

up    : up              [boolean]
    Move "up" as defined by the current context.

    """

def currentCtx():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/currentCtx.html



-----------------------------------------

currentCtx is undoable, NOT queryable, and NOT editable.

This command returns the currently selected tool context.


-----------------------------------------


Return Value:

string  : The name of the currently selected tool context.
    """

def currentTimeCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/currentTimeCtx.html



-----------------------------------------

currentTimeCtx is undoable, queryable, and editable.

This command creates a context which may be used to change current time within
the graph editor


-----------------------------------------


Return Value:

string  Context name    
  
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

def curveAddPtCtx(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveAddPtCtx.html



-----------------------------------------

curveAddPtCtx is undoable, queryable, and editable.

The curveAddPtCtx command creates a new curve add points context, which adds
either control vertices (CVs) or edit points to an existing curve.


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

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def curveCVCtx(q=1,e=1,bez=1,d="uint",ex=1,ch=1,i1="string",i2="string",i3="string",me=1,n="string",ps=1,rl=1,rf=1,sm=1,un=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveCVCtx.html



-----------------------------------------

curveCVCtx is undoable, queryable, and editable.

The curveCVCtx command creates a new context for creating curves by placing
control vertices (CVs).


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bez   : bezier          [boolean] ['query', 'edit']
    

-----------------------------------------

d     : degree          [uint] ['query', 'edit']
    Curve degree

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

me    : multEndKnots    [boolean] ['query', 'edit']
    Specify if multiple end knots are to be created.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ps    : preserveShape   [boolean] ['query', 'edit']
    Set this flag to make the operation preserve the shape

-----------------------------------------

rl    : rational        [boolean] ['query', 'edit']
    Should the curve be rational?

-----------------------------------------

rf    : refit           [boolean] ['query', 'edit']
    Set this flag to refit the curve

-----------------------------------------

sm    : symmetry        [boolean] ['query', 'edit']
    Specify if symmetry is to be used

-----------------------------------------

un    : uniform         [boolean]
    Should the curve use uniform parameterization?

    """

def curveEditorCtx(q=1,e=1,dir="int",ex=1,ch=1,i1="string",i2="string",i3="string",n="string",rts="float",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveEditorCtx.html



-----------------------------------------

curveEditorCtx is undoable, queryable, and editable.

The curveEditorCtx command creates a new NURBS editor context, which is used
to edit a NURBS curve or surface.


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dir   : direction       [int] ['query']
    Query the current direction of the tangent control. Always zero for the curve case. In the surface case, its 0 for the normal direction, 1 for U direction and 2 for V direction.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

rts   : relativeTangentSize [float] ['query', 'edit']
    Relative size of the tangent manipulator handle. Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.

-----------------------------------------

t     : title           [string]
    The title for the tool.

    """

def curveEPCtx(q=1,e=1,bez=1,d="uint",ex=1,ch=1,i1="string",i2="string",i3="string",n="string",ps=1,pf="float",rf=1,un=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveEPCtx.html



-----------------------------------------

curveEPCtx is undoable, queryable, and editable.

The curveEPCtx command creates a new context for creating curves by placing
edit points.


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bez   : bezier          [boolean] ['query', 'edit']
    Use bezier curves

-----------------------------------------

d     : degree          [uint] ['query', 'edit']
    Curve degree

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ps    : preserveShape   [boolean] ['query', 'edit']
    Set this flag to make the operation preserve the shape

-----------------------------------------

pf    : preserveShapeFraction [float] ['query', 'edit']
    Fraction value used when preserving the shape

-----------------------------------------

rf    : refit           [boolean] ['query', 'edit']
    Set this flag to refit the curve

-----------------------------------------

un    : uniform         [boolean]
    Should the curve use uniform parameterization?

    """

def curveMoveEPCtx(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveMoveEPCtx.html



-----------------------------------------

curveMoveEPCtx is undoable, queryable, and editable.

The curveMoveEPCtx command creates a new context for moving curve edit points
using a manipulator. Edit points can only be moved one at a time.


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

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def curveSketchCtx(q=1,e=1,d="uint",ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveSketchCtx.html



-----------------------------------------

curveSketchCtx is undoable, queryable, and editable.

The curveSketchCtx command creates a new curve sketch context, also known as
the "pencil context".


-----------------------------------------


Return Value:

string  (name of the new curve sketch context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : degree          [uint] ['query', 'edit']
    Valid values are 1 or 3

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

def directKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",o="string",so=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/directKeyCtx.html



-----------------------------------------

directKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to directly manipulate
keyframes within the graph editor


-----------------------------------------


Return Value:

string  Context name    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

o     : option          [string] ['query', 'edit']
    Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.

-----------------------------------------

so    : selectedOnly    [boolean]
    Controls whether only selected curves/keys can be moved, or all.

    """

def distanceDimContext(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/distanceDimContext.html



-----------------------------------------

distanceDimContext is undoable, queryable, and editable.

Command used to register the distanceDimCtx tool.


-----------------------------------------


Return Value:

string  \- name of the context created    
  
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

def dollyCtx(q=1,e=1,ac=1,bdt="string",cd=1,dtc=1,ex=1,ch=1,i1="string",i2="string",i3="string",ld=1,n="string",oz=1,s="float",tn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dollyCtx.html



-----------------------------------------

dollyCtx is undoable, queryable, and editable.

This command can be used to create, edit, or query a dolly context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

-----------------------------------------

bdt   : boxDollyType    [string] ['query', 'edit']
    Set the behavior of where the camera's center of interest is set to after the box dolly. In surface mode, the center of interest will be snapped to the surface point at the center of the marquee. In bbox mode, the closest bounding box to the camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.

-----------------------------------------

cd    : centerOfInterestDolly [boolean] ['query', 'edit']
    Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using the left mouse button for selection. The default select mask will be used.

-----------------------------------------

dtc   : dollyTowardsCenter [boolean] ['query', 'edit']
    Dolly towards center (if true), else dolly towards point where user clicks in the view.

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

ld    : localDolly      [boolean] ['query', 'edit']
    Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

oz    : orthoZoom       [boolean] ['query', 'edit']
    Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.

-----------------------------------------

s     : scale           [float] ['query', 'edit']
    The sensitivity for dollying the camera.

-----------------------------------------

tn    : toolName        [string]
    Name of the specific tool to which this command refers.

    """

def dragAttrContext(q=1,e=1,ct="name",ex=1,ch=1,i1="string",i2="string",i3="string",n="string",r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dragAttrContext.html



-----------------------------------------

dragAttrContext is undoable, queryable, and editable.

The dragAttrContext allows a user to manipulate the attributes of an object by
using a virtual slider within the viewport. The virtual slider is used by
dragging in a viewport with the middle mouse button. The speed at which the
attributes are changed can be controlled by holding down the Ctrl key to slow
it down and the Shift key to speed it up.


-----------------------------------------


Return Value:

string  The name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ct    : connectTo       [name] ['query', 'edit']
    Specifies an attribute to which to connect the context. This is a multi- use flag, but all attributes used must be from one object.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

r     : reset           [boolean]
    Resets the list of attributes to which the context is connected.

    """

def draggerContext(q=1,e=1,ap="[float, float, float]",bu="int",cs="int",cur="string",dc="script",dp="[float, float, float]",ds="string",ex=1,fnz="script",hs="string",ch=1,hc="script",i1="string",i2="string",i3="string",inz="script",mo="string",n="string",pl="[float, float, float]",ppc="script",pc="script",pr="string",rc="script",snp=1,sp="string",sc="int",um="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/draggerContext.html



-----------------------------------------

draggerContext is undoable, queryable, and editable.

The draggerContext allows the user to program the behavior of the mouse or an
equivalent dragging device in MEL.


-----------------------------------------


Return Value:

string  The name of the context.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : anchorPoint     [[float, float, float]] ['query']
    Anchor point (double array) where dragger was initially pressed.

-----------------------------------------

bu    : button          [int] ['query']
    Returns the current mouse button (1,2,3).

-----------------------------------------

cs    : currentStep     [int] ['query']
    Current step (press-drag-release sequence) for dragger context. When queried before first press event happened, returns 0.

-----------------------------------------

cur   : cursor          [string] ['query', 'edit']
    Cursor displayed while context is active. Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".

-----------------------------------------

dc    : dragCommand     [script] ['query', 'edit']
    Command called when mouse dragger is dragged.

-----------------------------------------

dp    : dragPoint       [[float, float, float]] ['query']
    Drag point (double array) current position of dragger during drag.

-----------------------------------------

ds    : drawString      [string] ['edit']
    A string to be drawn at the current position of the pointer.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

fnz   : finalize        [script] ['query', 'edit']
    Command called when the tool is exited.

-----------------------------------------

hs    : helpString      [string] ['query']
    Help string for context

-----------------------------------------

ch    : history         [boolean] []
    If this is a tool command, turn the construction history on for the tool in question.

-----------------------------------------

hc    : holdCommand     [script] ['query', 'edit']
    Command called when mouse dragger is held.

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

inz   : initialize      [script] ['query', 'edit']
    Command called when the tool is entered.

-----------------------------------------

mo    : modifier        [string] ['query']
    Returns the current modifier type: ctrl, alt or none.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

pl    : plane           [[float, float, float]] ['edit']
    Provide normal of projection plane (see -projection flag for details).

-----------------------------------------

ppc   : prePressCommand [script] ['query', 'edit']
    Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.

-----------------------------------------

pc    : pressCommand    [script] ['query', 'edit']
    Command called when mouse dragger is pressed.

-----------------------------------------

pr    : projection      [string] ['query', 'edit']
    Sets current projection of drag point. Valid types are:  | viewPlane | project to view plane

-----------------------------------------

rc    : releaseCommand  [script] ['query', 'edit']
    Command called when mouse dragger is released.

-----------------------------------------

snp   : snapping        [boolean] ['query', 'edit']
    Enable/disable snapping for dragger context.

-----------------------------------------

sp    : space           [string] ['query', 'edit']
    Sets current space that coordinates are reported in. Types are:  | world | world space (global)

-----------------------------------------

sc    : stepsCount      [int] ['query', 'edit']
    Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.

-----------------------------------------

um    : undoMode        [string]
    Undo queue mode for the context actions. Acceptable values are:    * "all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk.   * "step" \- all the actions that happen between each press and release are combined into one undo chunk.   * "sequence" \- all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger context.

    """

def dynParticleCtx(q=1,e=1,c="float",cp=1,ex=1,gr=1,grs="float",ch=1,i1="string",i2="string",i3="string",jr="float",llx="float",lly="float",llz="float",n="string",nc=1,nj="int",pn="string",sk=1,ski="int",tp=1,urx="float",ury="float",urz="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynParticleCtx.html



-----------------------------------------

dynParticleCtx is undoable, queryable, and editable.

The particle context command creates a particle context. The particle context
provides an interactive means to create particle objects. The particle context
command also provides an interactive means to set the option values, through
the Tool Property Sheet, for the "particle" command that the context will
issue.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : conserve        [float] ['query', 'edit']
    Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default) corresponds to the true physical law of conservation of momentum.

-----------------------------------------

cp    : cursorPlacement [boolean] ['query', 'edit']
    Use the cursor to place the lower left and upper right of the grid.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

gr    : grid            [boolean] ['query', 'edit']
    Create a particle grid.

-----------------------------------------

grs   : gridSpacing     [float] ['query', 'edit']
    Spacing between particles in the grid.

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

jr    : jitterRadius    [float] ['query', 'edit']
    Max radius from the center to place the particle instances.

-----------------------------------------

llx   : lowerLeftX      [float] ['query', 'edit']
    Lower left X position of the particle grid.

-----------------------------------------

lly   : lowerLeftY      [float] ['query', 'edit']
    Lower left Y position of the particle grid.

-----------------------------------------

llz   : lowerLeftZ      [float] ['query', 'edit']
    Lower left Z position of the particle grid.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

nc    : nucleus         [boolean] ['query', 'edit']
    If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.

-----------------------------------------

nj    : numJitters      [int] ['query', 'edit']
    Number of jitters (instances) per particle.

-----------------------------------------

pn    : particleName    [string] ['query', 'edit']
    Particle name.

-----------------------------------------

sk    : sketch          [boolean] ['query', 'edit']
    Create particles in sketch mode.

-----------------------------------------

ski   : sketchInterval  [int] ['query', 'edit']
    Interval between particles, when in sketch mode.

-----------------------------------------

tp    : textPlacement   [boolean] ['query', 'edit']
    Use the textfields to specify the lower left and upper right of/ the grid.

-----------------------------------------

urx   : upperRightX     [float] ['query', 'edit']
    Upper right X position of the particle grid.

-----------------------------------------

ury   : upperRightY     [float] ['query', 'edit']
    Upper right Y position of the particle grid.

-----------------------------------------

urz   : upperZ          [float]
    Upper right Z position of the particle grid.

    """

def filterButterworthCtx(q=1,e=1,a=1,cof="float",endTime="time",ex=1,ch=1,i1="string",i2="string",i3="string",kof=1,n="string",sr="float",sk=1,s="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filterButterworthCtx.html



-----------------------------------------

filterButterworthCtx is undoable, queryable, and editable.

Creates/edits a Butterworth filter context. This context can be used to
interactively preview/edit the Butterworth filter on a set of animation
curves.


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : apply           [boolean] ['edit']
    When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.

-----------------------------------------

cof   : cutoffFrequency [float] ['query', 'edit']
    Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.

-----------------------------------------

e     : endTime         [time] ['query', 'edit']
    Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.

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

kof   : keepKeysOnFrame [boolean] ['query', 'edit']
    When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

sr    : samplingRate    [float] ['query', 'edit']
    Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.

-----------------------------------------

sk    : selectedKeys    [boolean] ['query', 'edit']
    If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.

-----------------------------------------

s     : startTime       [time]
    Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.

    """

def filterKeyReducerCtx(q=1,e=1,a=1,endTime="time",ex=1,ch=1,i1="string",i2="string",i3="string",ks=1,n="string",pre="float",pm="int",pkt="string",sk=1,s="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filterKeyReducerCtx.html



-----------------------------------------

filterKeyReducerCtx is undoable, queryable, and editable.

Creates/edits a KeyReducer filter context. This context can be used to
interactively preview/edit the KeyReducer filter on a set of animation curves.


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : apply           [boolean] ['edit']
    When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.

-----------------------------------------

e     : endTime         [time] ['query', 'edit']
    Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.

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

ks    : keySync         [boolean] ['query', 'edit']
    When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

pre   : precision       [float] ['query', 'edit']
    Defines the precision parameter. For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.

-----------------------------------------

pm    : precisionMode   [int] ['query', 'edit']
    Specifies the precision mode for the Key Reducer filter. Avaiable modes are: 0: Absolute value. 1: Percentage Default is 1 (percentage mode).

-----------------------------------------

pkt   : preserveKeyTangent [string] ['query', 'edit']
    When specified, keys whose in or out tangent type match the specified type are preserved. Supported tangent types: fixed linear flat smooth step clamped plateau stepnext auto

-----------------------------------------

sk    : selectedKeys    [boolean] ['query', 'edit']
    If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.

-----------------------------------------

s     : startTime       [time]
    Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.

    """

def graphDollyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/graphDollyCtx.html



-----------------------------------------

graphDollyCtx is undoable, queryable, and editable.

This command can be used to create a dolly context for the graph editor.


-----------------------------------------


Return Value:

string  Context name    
  
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

def graphSelectContext(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/graphSelectContext.html



-----------------------------------------

graphSelectContext is undoable, queryable, and editable.

This command can be used to create a selection context for the hypergraph
editor.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def graphTrackCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/graphTrackCtx.html



-----------------------------------------

graphTrackCtx is undoable, queryable, and editable.

This command can be used to create a track context for the graph editor.


-----------------------------------------


Return Value:

string  Context name    
  
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

def greasePencilCtx(q=1,e=1,acf=1,cd=1,cef="int",ex=1,eac="[string, string]",fts="int",gpt="int",i1="string",i2="string",i3="string",iac="string",mst="uint",rf="int",rb=1,rgb="[float, float, float]",snn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/greasePencilCtx.html



-----------------------------------------

greasePencilCtx is undoable, queryable, and editable.

This is a tool context command for the grease pencil tool.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

acf   : autoCreateFrames [boolean] ['query', 'edit']
    Should frames be automatically created when drawing?

-----------------------------------------

cd    : canDraw         [boolean] ['query']
    Check to see if drawing is allowed

-----------------------------------------

cef   : createOrEditFrame [int] ['query']
    Frame number for create or edit

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

eac   : exportArchive   [[string, string]] ['edit']
    Modify names of export archive

-----------------------------------------

fts   : fileTextureSize [int] ['query', 'edit']
    Both width and height dimensions of the file texture (they are square).

-----------------------------------------

gpt   : greasePencilType [int] ['query', 'edit']
    Grease pencil type. 1 = Pencil, 2 = Marker, 3 = Soft Pencil, 4 = Eraser

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

iac   : importArchive   [string] ['edit']
    Modify name of import archive

-----------------------------------------

mst   : makeStroke      [uint] ['query', 'edit']
    Stroke point values.

-----------------------------------------

rf    : removeFrame     [int] ['edit']
    Remove the given frame

-----------------------------------------

rb    : resetBrushes    [boolean] ['query', 'edit']
    Should the brushes reset?

-----------------------------------------

rgb   : rgbcolor        [[float, float, float]] ['query', 'edit']
    Color of the grease pencil

-----------------------------------------

snn   : sequenceNodeName [string]
    Query the name of the sequence node

    """

def ikHandleCtx(q=1,e=1,apH=1,ccv=1,cra=1,ex=1,fsH=1,ch=1,i1="string",i2="string",i3="string",n="string",ns="int",pcv=1,pwH="float",pH="int",roc=1,rtm=1,scv=1,snc=1,snH=1,stH="string",sH="string",tws="string",wH="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikHandleCtx.html



-----------------------------------------

ikHandleCtx is undoable, queryable, and editable.

The ikHandle context command (ikHandleCtx) updates parameters of ikHandle
tool. The options for the tool will be set to the flags that the user
specifies.


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

apH   : autoPriorityH   [boolean] ['query', 'edit']
    Specifies that this handle's priority is assigned automatically.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

ccv   : createCurve     [boolean] ['query', 'edit']
    Specifies if a curve should be automatically created for the ikSplineHandle. The flag is ignored in the ikHandleCtx.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

cra   : createRootAxis  [boolean] ['edit']
    Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path. This flag is ignored in the ikHandleCtx.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

fsH   : forceSolverH    [boolean] ['query', 'edit']
    Specifies if the ikSolver is enabled for the ikHandle.   C: The default is on.   Q: When queried, this flag returns an int.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ns    : numSpans        [int] ['edit']
    Specifies the number of spans in the automatically generated curve of the ikSplineHandle. This flag is ignored in the ikHandleCtx.   C: The default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

pcv   : parentCurve     [boolean] ['edit']
    Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle. The flag is ignored in the ikHandleCtx.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

pwH   : poWeightH       [float] ['query', 'edit']
    Specifies the position/orientation weight of the ikHandle.   C: The default is 1.   Q: When queried, this flag returns a float.

-----------------------------------------

pH    : priorityH       [int] ['query', 'edit']
    Specifies the priority of the ikHandle.   C: The default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

roc   : rootOnCurve     [boolean] ['edit']
    Specifies if the root is locked onto the curve of the ikSplineHandle. This flag is ignored in the ikHandleCtx.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

rtm   : rootTwistMode   [boolean] ['edit']
    Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. This flag is ignored in the ikHandleCtx.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

scv   : simplifyCurve   [boolean] ['edit']
    Specifies if the ikSplineHandle curve should be simplified. This flag is ignored in the ikHandleCtx.   C: The default is on.   Q: When queried, this returns an int.

-----------------------------------------

snc   : snapCurve       [boolean] ['edit']
    Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle. This flag is ignored in the ikHandleCtx.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

snH   : snapHandleH     [boolean] ['query', 'edit']
    Specifies if the ikHandle snapping is on.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

stH   : solverTypeH     [string] ['query', 'edit']
    Lists what ikSolver is being used. The ikSplineSolver may not be selected. To use an ikSplineSolver use the ikSplineHandleCtx command.   C: The default solver is the default set by the user preferences.   Q: When queried, this flag returns a string.

-----------------------------------------

sH    : stickyH         [string] ['query', 'edit']
    Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off".   C: The default is "off".   Q: When queried, this flag returns a string.

-----------------------------------------

tws   : twistType       [string] ['edit']
    Specifies the type of interpolation to be used by the ikSplineHandle. This flag is ignored in the ikHandleCtx. The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".   C: The default is "linear".   Q: When queried, this flag returns a string.

-----------------------------------------

wH    : weightH         [float]
    Specifies the weight of the ikHandle.   C: The default is 1.   Q: When queried, this flag returns a float.

    """

def ikSplineHandleCtx(q=1,e=1,apH=1,ccv=1,cra=1,ex=1,fsH=1,ch=1,i1="string",i2="string",i3="string",n="string",ns="int",pcv=1,pwH="float",pH="int",roc=1,rtm=1,scv=1,snc=1,snH=1,stH="string",sH="string",tws="string",wH="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ikSplineHandleCtx.html



-----------------------------------------

ikSplineHandleCtx is undoable, queryable, and editable.

The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
ikSplineHandle tool. The options for the tool will be set to the flags the
user specifies.


-----------------------------------------


Return Value:

string  The name of the context.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

apH   : autoPriorityH   [boolean] ['query', 'edit']
    Specifies that this handle's priority is assigned automatically.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

ccv   : createCurve     [boolean] ['query', 'edit']
    Specifies if a curve should be automatically created for the ikSplineHandle.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

cra   : createRootAxis  [boolean] ['edit']
    Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

fsH   : forceSolverH    [boolean] ['query', 'edit']
    Specifies if the ikSolver is enabled for the ikHandle.   C: The default is on.   Q: When queried, this flag returns an int.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ns    : numSpans        [int] ['edit']
    Specifies the number of spans in the automatically generated curve of the ikSplineHandle.   C: The default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

pcv   : parentCurve     [boolean] ['edit']
    Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

pwH   : poWeightH       [float] ['query', 'edit']
    Specifies the position/orientation weight of the ikHandle.   C: The default is 1.   Q: When queried, this flag returns a float.

-----------------------------------------

pH    : priorityH       [int] ['query', 'edit']
    Specifies the priority of the ikHandle.   C: The default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

roc   : rootOnCurve     [boolean] ['edit']
    Specifies if the root is locked onto the curve of the ikSplineHandle.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

rtm   : rootTwistMode   [boolean] ['edit']
    Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

scv   : simplifyCurve   [boolean] ['edit']
    Specifies if the ikSplineHandle curve should be simplified.   C: The default is on.   Q: When queried, this returns an int.

-----------------------------------------

snc   : snapCurve       [boolean] ['edit']
    Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

snH   : snapHandleH     [boolean] ['query', 'edit']
    Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

stH   : solverTypeH     [string] ['query', 'edit']
    Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.   C: The default solver is the ikSplineSolver.   Q: When queried, this flag returns a string.

-----------------------------------------

sH    : stickyH         [string] ['query', 'edit']
    Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.   C: The default is "off".   Q: When queried, this flag returns a string.

-----------------------------------------

tws   : twistType       [string] ['edit']
    Specifies the type of interpolation to be used by the ikSplineHandle.   The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".   C: The default is "linear".   Q: When queried, this flag returns a string.

-----------------------------------------

wH    : weightH         [float]
    Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.   C: The default is 1.   Q: When queried, this flag returns a float.

    """

def insertJointCtx(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/insertJointCtx.html



-----------------------------------------

insertJointCtx is undoable, queryable, and editable.

The command will create an insert joint context. The insert joint tool inserts
joints into an existing chain of joints.


-----------------------------------------


Return Value:

string  The name of the context.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def insertKeyCtx(q=1,e=1,bd=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/insertKeyCtx.html



-----------------------------------------

insertKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to insert keys within the
graph editor


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bd    : breakdown       [boolean] ['query', 'edit']
    Specifies whether or not to create breakdown keys

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

def jointCtx(q=1,e=1,ajo="string",apH=1,ikh=1,dJ="string",ex=1,fsH=1,i1="string",i2="string",i3="string",jal=1,joJ="[angle, angle, angle]",lbl="float",lbr="float",pwH="float",pH="int",scJ=1,sJ="[float, float, float]",soJ="[angle, angle, angle]",sao="string",sbl="float",sbr="float",snH=1,stH="string",sH="string",sym=1,sa="string",vbs=1,wH="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/jointCtx.html



-----------------------------------------

jointCtx is undoable, queryable, and editable.

The joint context command (jointCtx) updates the parameters of the joint tool.
The options for the tool will be set by the flags the user specifies.


-----------------------------------------


Return Value:

string  The name of the context.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ajo   : autoJointOrient [string] ['query', 'edit']
    Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.   C: The default is "xyz".   Q: When queried, this flag returns a string.

-----------------------------------------

apH   : autoPriorityH   [boolean] ['query', 'edit']
    Specifies if the ikHandle's priority is assigned automatically.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

ikh   : createIKHandle  [boolean] ['query', 'edit']
    Enables the joint tool to create an ikHandle when the tool is completed.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

dJ    : degreeOfFreedomJ [string] ['query', 'edit']
    Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".   C: The default is "xyz".   Q: When queried, this flag returns a string.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

fsH   : forceSolverH    [boolean] ['query', 'edit']
    Specifies if the ikSolver for the ikHandle is enabled.   C: The default is on.   Q: When queried, this flag returns an int.

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

jal   : jointAutoLimits [boolean] ['query', 'edit']
    Automatically computes the joint limits based on the kind of joint created.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

joJ   : jointOrientationJ [[angle, angle, angle]] ['query', 'edit']
    Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.   C: The default is 0 0 0.   Q: When queried, this flag returns an array of three floats.

-----------------------------------------

lbl   : largeBoneLength [float] ['query', 'edit']
    Specifies the length above which bones should be assigned the largeBoneRadius.

-----------------------------------------

lbr   : largeBoneRadius [float] ['query', 'edit']
    Specifies the radius for bones whose length is above the largeBoneLength

-----------------------------------------

pwH   : poWeightH       [float] ['query', 'edit']
    Specifies the position/orientation weight of the ikHandle.   C: The default is 1.   Q: When queried, this flag returns a float.

-----------------------------------------

pH    : priorityH       [int] ['query', 'edit']
    Specifies the priority of the ikHandle.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

scJ   : scaleCompensateJ [boolean] ['query', 'edit']
    Specifies if scale compensate is enabled.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

sJ    : scaleJ          [[float, float, float]] ['query', 'edit']
    Sets the scale for the joints created by the tool.   C: The default is 1 1 1.   Q: When queried, this flag returns an array of three floats.

-----------------------------------------

soJ   : scaleOrientationJ [[angle, angle, angle]] ['query', 'edit']
    Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.   C: The default is 0 0 0.   Q: When queried, this flag returns an array of three floats.

-----------------------------------------

sao   : secondaryAxisOrient [string] ['query', 'edit']
    Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".

-----------------------------------------

sbl   : smallBoneLength [float] ['query', 'edit']
    Specifies the length below which bones should be assigned the smallBoneRadius.

-----------------------------------------

sbr   : smallBoneRadius [float] ['query', 'edit']
    Specifies the radius for bones whose length is below the smallBoneLength.

-----------------------------------------

snH   : snapHandleH     [boolean] ['query', 'edit']
    Sepcifies if snapping is enabled for the ikHandle.   C: The default is on.   Q: When queried, this flag returns an int.

-----------------------------------------

stH   : solverTypeH     [string] ['query', 'edit']
    Sets the name of the solver to use with the ikHandle.   C: The default is the solver set to the default in the user preferences.   Q: When queried, this flag returns a string.

-----------------------------------------

sH    : stickyH         [string] ['query', 'edit']
    Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.   C: The default is "off".   Q: When queried, this flag returns a string.

-----------------------------------------

sym   : symmetry        [boolean] ['query', 'edit']
    Automaticaly create a symmetry joint based if symmetry is on.   C: The default is off.   Q: When queried, this flag returns an int.

-----------------------------------------

sa    : symmetryAxis    [string] ['query', 'edit']
    Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.   C: The default is x.   Q: When queried, this flag returns a string.

-----------------------------------------

vbs   : variableBoneSize [boolean] ['query', 'edit']
    Specifies whether or not variable bone length and radius settings should be used.

-----------------------------------------

wH    : weightH         [float]
    Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.   C: The default is 1.   Q: When queried, this flag returns a float.

    """

def keyframeRegionCurrentTimeCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionCurrentTimeCtx.html



-----------------------------------------

keyframeRegionCurrentTimeCtx is undoable, queryable, and editable.

This command creates a context which may be used to change current time within
the keyframe region of the dope sheet editor.


-----------------------------------------


Return Value:

string  Context name    
  
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

def keyframeRegionDirectKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",o="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionDirectKeyCtx.html



-----------------------------------------

keyframeRegionDirectKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to directly manipulate
keyframes within the dope sheet editor


-----------------------------------------


Return Value:

string  Context name    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

o     : option          [string]
    Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.

    """

def keyframeRegionDollyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionDollyCtx.html



-----------------------------------------

keyframeRegionDollyCtx is undoable, queryable, and editable.

This command can be used to create a dolly context for the dope sheet editor.


-----------------------------------------


Return Value:

string  Context name    
  
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

def keyframeRegionInsertKeyCtx(q=1,e=1,bd=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionInsertKeyCtx.html



-----------------------------------------

keyframeRegionInsertKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to insert keys within the
keyframe region of the dope sheet editor


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bd    : breakdown       [boolean] ['query', 'edit']
    Specifies whether or not to create breakdown keys

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

def keyframeRegionMoveKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",o="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionMoveKeyCtx.html



-----------------------------------------

keyframeRegionMoveKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to move keyframes within the
keyframe region of the dope sheet editor


-----------------------------------------


Return Value:

string  Context name    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

o     : option          [string]
    Valid values are "move," "insert," "over," and "segmentOver". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.

    """

def keyframeRegionScaleKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",ssk=1,typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionScaleKeyCtx.html



-----------------------------------------

keyframeRegionScaleKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to scale keyframes within the
keyframe region of the dope sheet editor


-----------------------------------------


Return Value:

string  Context name    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ssk   : scaleSpecifiedKeys [boolean] ['query', 'edit']
    Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.

-----------------------------------------

typ   : type            [string]
    rect | manip Specifies the type of scale manipulator to use

    """

def keyframeRegionSelectKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionSelectKeyCtx.html



-----------------------------------------

keyframeRegionSelectKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to select keyframes within
the keyframe region of the dope sheet editor


-----------------------------------------


Return Value:

string  Context name    
  
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

def keyframeRegionSetKeyCtx(q=1,e=1,bd=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionSetKeyCtx.html



-----------------------------------------

keyframeRegionSetKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to set keys within the
keyframe region of the dope sheet editor


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bd    : breakdown       [boolean] ['query', 'edit']
    Specifies whether or not to create breakdown keys

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

def keyframeRegionTrackCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionTrackCtx.html



-----------------------------------------

keyframeRegionTrackCtx is undoable, queryable, and editable.

This command can be used to create a track context for the dope sheet editor.


-----------------------------------------


Return Value:

string  Context name    
  
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

def lassoContext(q=1,e=1,dc=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lassoContext.html



-----------------------------------------

lassoContext is undoable, queryable, and editable.

Creates a context to perform selection via a "lasso". Use for irregular
selection regions, where the "marquee-style" select of the "selectContext" is
inappropriate.


-----------------------------------------


Return Value:

string  Name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dc    : drawClosed      [boolean] ['query', 'edit']
    Turns the closed display of the lasso on/off.

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

def latticeDeformKeyCtx(q=1,e=1,ev="float",ex=1,ch=1,i1="string",i2="string",i3="string",lc="uint",lr="uint",n="string",slp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/latticeDeformKeyCtx.html



-----------------------------------------

latticeDeformKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to deform key frames with
lattice manipulator. This context only works in the graph editor.


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ev    : envelope        [float] ['query', 'edit']
    Specifies the influence of the lattice.

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

lc    : latticeColumns  [uint] ['query', 'edit']
    Specifies the number column points the lattice contains.

-----------------------------------------

lr    : latticeRows     [uint] ['query', 'edit']
    Specifies the number of rows the lattice contains.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

slp   : scaleLatticePts [boolean]
    Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'

    """

def manipMoveContext(q=1,e=1,ah="int",ahn="int",aa="[float, float, float]",xn=1,cah="int",epm=1,epp=1,ex=1,i1="string",i2="string",i3="string",iu=1,lm="int",vis=1,m="int",oa="[float, float, float]",oj="string",oje=1,oo="string",ot="[float, float, float]",pin=1,poh=1,p=1,psc="script",pod="[script, string]",prc="script",prd="[script, string]",pcp=1,puv=1,rfl=1,rab="int",rfa="int",rft="float",sao="string",s=1,scr=1,slf=1,slp=1,spo=1,spp=1,sr=1,sv="float",tr="[float, float, float]",twk=1,xc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipMoveContext.html



-----------------------------------------

manipMoveContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a move manip context. Note
that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
all move manip context. Changing one context independently is not allowed.
Changing a context's behaviour using the above flags, will change all existing
move manip context.


-----------------------------------------


Return Value:

string  The name of the new context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ah    : activeHandle    [int] ['query', 'edit']
    Sets the default active handle for the manip. That is, the handle which should be initially active when the tool is activated. Values can be:    * 0 - X axis handle is active   * 1 - Y axis handle is active   * 2 - Z axis handle is active   * 3 - Center handle (all 3 axes) is active (default)

-----------------------------------------

ahn   : activeHandleNormal [int] ['query', 'edit']
    * 0 - U axis handle is active   * 1 - V axis handle is active   * 2 - N axis handle is active ( default )   * 3 - Center handle (all 3 axes) is active  applicable only when the manip mode is 3.

-----------------------------------------

aa    : alignAlong      [[float, float, float]] ['edit']
    Aligns active handle along vector.

-----------------------------------------

xn    : constrainAlongNormal [boolean] ['query', 'edit']
    When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.

-----------------------------------------

cah   : currentActiveHandle [int] ['query', 'edit']
    Sets the active handle for the manip. Values can be:    * 0 - X axis handle is active   * 1 - Y axis handle is active   * 2 - Z axis handle is active   * 3 - Center handle (all 3 axes) is active   * 4 - XY plane handle is active   * 5 - YZ plane handle is active   * 6 - XZ plane handle is active

-----------------------------------------

epm   : editPivotMode   [boolean] ['query']
    Returns true manipulator is in edit pivot mode

-----------------------------------------

epp   : editPivotPosition [boolean] ['query']
    Returns the current position of the edit pivot manipulator.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

iu    : interactiveUpdate [boolean] ['query', 'edit']
    Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.

-----------------------------------------

lm    : lastMode        [int] ['query']
    Returns the previous translation mode.

-----------------------------------------

vis   : manipVisible    [boolean] ['query']
    Returns true if the main translate manipulator is visible.

-----------------------------------------

m     : mode            [int] ['query', 'edit']
    Translate mode:    * 0 - Object Space   * 1 - Local Space   * 2 - World Space (default)   * 3 - Move Along Vertex Normal   * 4 - Move Along Rotation Axis   * 5 - Move Along Live Object Axis   * 6 - Custom Axis Orientation   * 10 - Component Space

-----------------------------------------

oa    : orientAxes      [[float, float, float]] ['query', 'edit']
    Orients manipulator rotating around axes by specified angles

-----------------------------------------

oj    : orientJoint     [string] ['query', 'edit']
    Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.

-----------------------------------------

oje   : orientJointEnabled [boolean] ['query', 'edit']
    Specifies if joints should be reoriented when moved.

-----------------------------------------

oo    : orientObject    [string] ['edit']
    Orients manipulator to the passed in object/component

-----------------------------------------

ot    : orientTowards   [[float, float, float]] ['edit']
    Orients active handle towards world point

-----------------------------------------

pin   : pinPivot        [boolean] ['query', 'edit']
    Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.

-----------------------------------------

poh   : pivotOriHandle  [boolean] ['query', 'edit']
    When true, the pivot manipulator will show the orientation handle during editing. Default is true.

-----------------------------------------

p     : position        [boolean] ['query']
    Returns the current position of the manipulator

-----------------------------------------

psc   : postCommand     [script] ['edit']
    Specifies a command to be executed when the tool is exited.

-----------------------------------------

pod   : postDragCommand [[script, string]] ['edit']
    Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.

-----------------------------------------

prc   : preCommand      [script] ['edit']
    Specifies a command to be executed when the tool is entered.

-----------------------------------------

prd   : preDragCommand  [[script, string]] ['edit']
    Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.

-----------------------------------------

pcp   : preserveChildPosition [boolean] ['query', 'edit']
    When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.

-----------------------------------------

puv   : preserveUV      [boolean] ['query', 'edit']
    When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.

-----------------------------------------

rfl   : reflection      [boolean] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rab   : reflectionAbout [int] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rfa   : reflectionAxis  [int] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rft   : reflectionTolerance [float] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

sao   : secondaryAxisOrient [string] ['query', 'edit']
    Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.

-----------------------------------------

s     : snap            [boolean] ['query', 'edit']
    Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag. The interval between the points can be controlled using the 'snapValue' flag.

-----------------------------------------

scr   : snapComponentsRelative [boolean] ['query', 'edit']
    Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'), and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.

-----------------------------------------

slf   : snapLiveFaceCenter [boolean] ['query', 'edit']
    Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.

-----------------------------------------

slp   : snapLivePoint   [boolean] ['query', 'edit']
    Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.

-----------------------------------------

spo   : snapPivotOri    [boolean] ['query', 'edit']
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

-----------------------------------------

spp   : snapPivotPos    [boolean] ['query', 'edit']
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

-----------------------------------------

sr    : snapRelative    [boolean] ['query', 'edit']
    Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE: If in local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.

-----------------------------------------

sv    : snapValue       [float] ['query', 'edit']
    Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'

-----------------------------------------

tr    : translate       [[float, float, float]] ['query', 'edit']
    Returns the translation of the manipulator for its current orientation/mode.

-----------------------------------------

twk   : tweakMode       [boolean] ['query', 'edit']
    When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.

-----------------------------------------

xc    : xformConstraint [string]
    * none - no transform constraint   * edge - edge transform constraint   * surface - surface transform constraint

    """

def manipMoveLimitsCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipMoveLimitsCtx.html



-----------------------------------------

manipMoveLimitsCtx is undoable, queryable, and editable.

Create a context for the translate limits manipulator.


-----------------------------------------


Return Value:

string  Name of newly created context    
  
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

def manipRotateContext(q=1,e=1,ah="int",aa="[float, float, float]",ctb=1,xn=1,cah="int",epm=1,epp=1,ex=1,i1="string",i2="string",i3="string",lm="int",vis=1,m="int",mt=1,oa="[float, float, float]",oo="string",ot="[float, float, float]",pin=1,poh=1,p=1,psc="script",pod="[script, string]",prc="script",prd="[script, string]",pcp=1,puv=1,rfl=1,rab="int",rfa="int",rft="float",ro="[float, float, float]",s=1,spo=1,spp=1,sr=1,sv="float",twk=1,ucp=1,ump=1,uop=1,xc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipRotateContext.html



-----------------------------------------

manipRotateContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a rotate manip context.


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ah    : activeHandle    [int] ['query', 'edit']
    Sets the default active handle for the manip. That is, the handle which should be initially active when the tool is activated. Values can be:    * 0 - X axis handle is active   * 1 - Y axis handle is active   * 2 - Z axis handle is active   * 3 - View rotation handle (outer ring) is active (default)

-----------------------------------------

aa    : alignAlong      [[float, float, float]] ['edit']
    Aligns active handle along vector.

-----------------------------------------

ctb   : centerTrackball [boolean] ['query', 'edit']
    Specify if the center is to be handled like a trackball

-----------------------------------------

xn    : constrainAlongNormal [boolean] ['query', 'edit']
    When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.

-----------------------------------------

cah   : currentActiveHandle [int] ['query', 'edit']
    Sets the active handle for the manip. Values can be:    * 0 - X axis handle is active   * 1 - Y axis handle is active   * 2 - Z axis handle is active   * 3 - View rotation handle (outer ring) is active   * 4 - Arc Ball is active

-----------------------------------------

epm   : editPivotMode   [boolean] ['query']
    Returns true manipulator is in edit pivot mode

-----------------------------------------

epp   : editPivotPosition [boolean] ['query']
    Returns the current position of the edit pivot manipulator.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

lm    : lastMode        [int] ['query']
    Returns the previous rotation mode.

-----------------------------------------

vis   : manipVisible    [boolean] ['query']
    Returns true if the rotate manipulator is visible.

-----------------------------------------

m     : mode            [int] ['query', 'edit']
    Rotate mode:    * 0 - Object Space (default)   * 1 - World Space   * 2 - Gimbal Mode   * 3 - Custom Axis Orientation   * 10 - Component Space

-----------------------------------------

mt    : modifyTranslation [boolean] ['query', 'edit']
    When false, and an object is rotated about a point other than its rotate pivot, its rotateTranslate attribute is modified to put the object at the correct position. When true, its translate attribute is used instead. Default is false.

-----------------------------------------

oa    : orientAxes      [[float, float, float]] ['query', 'edit']
    Orients manipulator rotating around axes by specified angles

-----------------------------------------

oo    : orientObject    [string] ['edit']
    Orients manipulator to the passed in object/component

-----------------------------------------

ot    : orientTowards   [[float, float, float]] ['edit']
    Orients active handle towards world point

-----------------------------------------

pin   : pinPivot        [boolean] ['query', 'edit']
    Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.

-----------------------------------------

poh   : pivotOriHandle  [boolean] ['query', 'edit']
    When true, the pivot manipulator will show the orientation handle during editing. Default is true.

-----------------------------------------

p     : position        [boolean] ['query']
    Returns the current position of the manipulator.

-----------------------------------------

psc   : postCommand     [script] ['edit']
    Specifies a command to be executed when the tool is exited.

-----------------------------------------

pod   : postDragCommand [[script, string]] ['edit']
    Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.

-----------------------------------------

prc   : preCommand      [script] ['edit']
    Specifies a command to be executed when the tool is entered.

-----------------------------------------

prd   : preDragCommand  [[script, string]] ['edit']
    Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.

-----------------------------------------

pcp   : preserveChildPosition [boolean] ['query', 'edit']
    When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.

-----------------------------------------

puv   : preserveUV      [boolean] ['query', 'edit']
    When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.

-----------------------------------------

rfl   : reflection      [boolean] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rab   : reflectionAbout [int] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rfa   : reflectionAxis  [int] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rft   : reflectionTolerance [float] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

ro    : rotate          [[float, float, float]] ['query', 'edit']
    Returns the rotation of the manipulator for its current orientation/mode.

-----------------------------------------

s     : snap            [boolean] ['query', 'edit']
    Specify that the manipulation is to use absolute snap

-----------------------------------------

spo   : snapPivotOri    [boolean] ['query', 'edit']
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

-----------------------------------------

spp   : snapPivotPos    [boolean] ['query', 'edit']
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

-----------------------------------------

sr    : snapRelative    [boolean] ['query', 'edit']
    Specify that the manipulation is to use relative snap

-----------------------------------------

sv    : snapValue       [float] ['query', 'edit']
    Specify the snapping value

-----------------------------------------

twk   : tweakMode       [boolean] ['query', 'edit']
    When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.

-----------------------------------------

ucp   : useCenterPivot  [boolean] ['query', 'edit']
    When true, use the center of the selection's bounding box as the center of the rotation (for all objects).

-----------------------------------------

ump   : useManipPivot   [boolean] ['query', 'edit']
    When true, use the manipulator's center as the center of the rotation (for all objects).

-----------------------------------------

uop   : useObjectPivot  [boolean] ['query', 'edit']
    When true, use each object's pivot as the center of its rotation.

-----------------------------------------

xc    : xformConstraint [string]
    * none - no transform constraint   * edge - edge transform constraint   * surface - surface transform constraint

    """

def manipRotateLimitsCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipRotateLimitsCtx.html



-----------------------------------------

manipRotateLimitsCtx is undoable, queryable, and editable.

Create a context for the rotate limits manipulator.


-----------------------------------------


Return Value:

string  Name of newly created context    
  
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

def manipScaleContext(q=1,e=1,ah="int",aa="[float, float, float]",xn=1,cah="int",epm=1,epp=1,ex=1,i1="string",i2="string",i3="string",lm="int",vis=1,m="int",oa="[float, float, float]",oo="string",ot="[float, float, float]",pin=1,poh=1,p=1,psc="script",pod="[script, string]",prc="script",prd="[script, string]",pcp=1,puv=1,pns=1,rfl=1,rab="int",rfa="int",rft="float",sc="[float, float, float]",s=1,spo=1,spp=1,sr=1,sv="float",twk=1,ump=1,uop=1,xc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipScaleContext.html



-----------------------------------------

manipScaleContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a scale manip context.


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ah    : activeHandle    [int] ['query', 'edit']
    Sets the default active handle for the manip. That is, the handle which should be initially active when the tool is activated. Values can be:    * 0 - X axis handle is active   * 1 - Y axis handle is active   * 2 - Z axis handle is active   * 3 - Center handle (all axes) is active (default)

-----------------------------------------

aa    : alignAlong      [[float, float, float]] ['edit']
    Aligns active handle along vector.

-----------------------------------------

xn    : constrainAlongNormal [boolean] ['query', 'edit']
    When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.

-----------------------------------------

cah   : currentActiveHandle [int] ['query', 'edit']
    Sets the active handle for the manip. Values can be:    * 0 - X axis handle is active   * 1 - Y axis handle is active   * 2 - Z axis handle is active   * 3 - Center handle (all axes) is active   * 4 - XY plane handle is active   * 5 - YZ plane handle is active   * 6 - XZ plane handle is active

-----------------------------------------

epm   : editPivotMode   [boolean] ['query']
    Returns true manipulator is in edit pivot mode

-----------------------------------------

epp   : editPivotPosition [boolean] ['query']
    Returns the current position of the edit pivot manipulator.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

lm    : lastMode        [int] ['query']
    Returns the previous scaling mode.

-----------------------------------------

vis   : manipVisible    [boolean] ['query']
    Returns true if the scale manipulator is visible.

-----------------------------------------

m     : mode            [int] ['query', 'edit']
    Scale mode:    * 0 - Object Space   * 1 - Local Space   * 2 - World Space (default)   * 3 - Scale Along Vertex Normal   * 4 - Scale Along Rotation Axis   * 5 - Scale Along Live Object Axis   * 6 - Custom Axis Orientation   * 10 - Component Space

-----------------------------------------

oa    : orientAxes      [[float, float, float]] ['query', 'edit']
    Orients manipulator rotating around axes by specified angles

-----------------------------------------

oo    : orientObject    [string] ['edit']
    Orients manipulator to the passed in object/component

-----------------------------------------

ot    : orientTowards   [[float, float, float]] ['edit']
    Orients active handle towards world point

-----------------------------------------

pin   : pinPivot        [boolean] ['query', 'edit']
    Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.

-----------------------------------------

poh   : pivotOriHandle  [boolean] ['query', 'edit']
    When true, the pivot manipulator will show the orientation handle during editing. Default is true.

-----------------------------------------

p     : position        [boolean] ['query']
    Returns the current position of the manipulator.

-----------------------------------------

psc   : postCommand     [script] ['edit']
    Specifies a command to be executed when the tool is exited.

-----------------------------------------

pod   : postDragCommand [[script, string]] ['edit']
    Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.

-----------------------------------------

prc   : preCommand      [script] ['edit']
    Specifies a command to be executed when the tool is entered.

-----------------------------------------

prd   : preDragCommand  [[script, string]] ['edit']
    Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.

-----------------------------------------

pcp   : preserveChildPosition [boolean] ['query', 'edit']
    When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.

-----------------------------------------

puv   : preserveUV      [boolean] ['query', 'edit']
    When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.

-----------------------------------------

pns   : preventNegativeScale [boolean] ['query']
    When this is true, negative scale is not allowed.

-----------------------------------------

rfl   : reflection      [boolean] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rab   : reflectionAbout [int] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rfa   : reflectionAxis  [int] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

rft   : reflectionTolerance [float] []
    This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.

-----------------------------------------

sc    : scale           [[float, float, float]] ['query', 'edit']
    Returns the scale of the manipulator for its current orientation/mode.

-----------------------------------------

s     : snap            [boolean] ['query', 'edit']
    Specify that the manipulation is to use absolute snap

-----------------------------------------

spo   : snapPivotOri    [boolean] ['query', 'edit']
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

-----------------------------------------

spp   : snapPivotPos    [boolean] ['query', 'edit']
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

-----------------------------------------

sr    : snapRelative    [boolean] ['query', 'edit']
    Specify that the manipulation is to use relative snap

-----------------------------------------

sv    : snapValue       [float] ['query', 'edit']
    Specify the snapping value

-----------------------------------------

twk   : tweakMode       [boolean] ['query', 'edit']
    When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.

-----------------------------------------

ump   : useManipPivot   [boolean] ['query', 'edit']
    Specify whether to pivot on the manip

-----------------------------------------

uop   : useObjectPivot  [boolean] ['query', 'edit']
    Specify whether to pivot on the object

-----------------------------------------

xc    : xformConstraint [string]
    * none - no transform constraint   * edge - edge transform constraint   * surface - surface transform constraint

    """

def manipScaleLimitsCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipScaleLimitsCtx.html



-----------------------------------------

manipScaleLimitsCtx is undoable, queryable, and editable.

Create a context for the scale limits manipulator.


-----------------------------------------


Return Value:

string  Name of newly created context.    
  
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

def modelCurrentTimeCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",per="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/modelCurrentTimeCtx.html



-----------------------------------------

modelCurrentTimeCtx is undoable, queryable, and editable.

This command creates a context which may be used to change current time within
the model views.


-----------------------------------------


Return Value:

string  Context name    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

per   : percent         [float]
    Percent of the screen space that represents the full time slider range (default is 50%)

    """

def moveKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",mf="string",n="string",o="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/moveKeyCtx.html



-----------------------------------------

moveKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to move keyframes within the
graph editor


-----------------------------------------


Return Value:

string  Context name    
  
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

mf    : moveFunction    [string] ['query', 'edit']
    linear | power | constant. Specifies how the keys are dragged. The default move type is constant where all keys move the same amount as controlled by user movement. Power provides a fall-off function where the center of the drag moves the most and the keys around the drag move less.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

o     : option          [string]
    Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.

    """

def orbitCtx(q=1,e=1,ac=1,ex=1,ch=1,i1="string",i2="string",i3="string",lo=1,n="string",os="float",tn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/orbitCtx.html



-----------------------------------------

orbitCtx is undoable, queryable, and editable.

Create, edit, or query an orbit context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

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

lo    : localOrbit      [boolean] ['query', 'edit']
    Orbit around the camera's center of interest.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

os    : orbitScale      [float] ['query', 'edit']
    In degrees of rotation per 100 pixels of cursor drag.

-----------------------------------------

tn    : toolName        [string]
    Name of the specific tool to which this command refers.

    """

def panZoomCtx(q=1,e=1,ac=1,btd=1,btu=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",pm=1,tn="string",zm=1,zs="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/panZoomCtx.html



-----------------------------------------

panZoomCtx is undoable, queryable, and editable.

This command can be used to create camera 2D pan/zoom context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

-----------------------------------------

btd   : buttonDown      [boolean] []
    Perform the button down operation

-----------------------------------------

btu   : buttonUp        [boolean] []
    Perform the button up operation

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

pm    : panMode         [boolean] []
    Specify to create a camera 2D pan context, which is the default.

-----------------------------------------

tn    : toolName        [string] ['query']
    Name of the specific tool to which this command refers.

-----------------------------------------

zm    : zoomMode        [boolean] []
    Specify to create a camera 2D zoom context.

-----------------------------------------

zs    : zoomScale       [float]
    Scale the zoom. The smaller the scale the slower the drag.

    """

def paramDimContext(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/paramDimContext.html



-----------------------------------------

paramDimContext is undoable, queryable, and editable.

Command used to register the paramDimCtx tool.


-----------------------------------------


Return Value:

string  \- name of the context created    
  
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

def polyAppendFacetCtx(q=1,e=1,ap=1,ex=1,i1="string",i2="string",i3="string",isr=1,mp="int",pc=1,r="float",s="int",tx="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyAppendFacetCtx.html



-----------------------------------------

polyAppendFacetCtx is undoable, queryable, and editable.

Create a new context to append facets on polygonal objects


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : append          [boolean] ['query', 'edit']
    Allows to switch to polyCreateFacetCtx tool

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

isr   : isRotateAvailable [boolean] ['query']
    Tells if the control associated to rotate flag is available. If several edges are already selected and they are not aligned (thus there is no "rotation axis") the rotation is no longer available.

-----------------------------------------

mp    : maximumNumberOfPoints [int] ['query', 'edit']
    Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.

-----------------------------------------

pc    : planarConstraint [boolean] ['query', 'edit']
    Allows/avoid new facet to be non-planar.   If on, all new points will be projected onto current facet plane. Selected edges will be checked as well.

-----------------------------------------

r     : rotate          [float] ['query', 'edit']
    Rotate current facet around the first edge selected.

-----------------------------------------

s     : subdivision     [int] ['query', 'edit']
    Number of sub-edges created for each new edge. Default is 1.

-----------------------------------------

tx    : texture         [int]
    Number of textures. Default is 1.

    """

def polyCreaseCtx(q=1,e=1,cs="string",ex=1,es=1,i1="string",i2="string",i3="string",r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCreaseCtx.html



-----------------------------------------

polyCreaseCtx is undoable, queryable, and editable.

Create a new context to crease components on polygonal objects


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cs    : createSet       [string] ['edit']
    Creates a set for the selected components.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

es    : extendSelection [boolean] ['query', 'edit']
    Enable/disable extending selection to all connected creased components.

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

r     : relative        [boolean]
    Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.

    """

def polyCreateFacetCtx(q=1,e=1,ap=1,ex=1,i1="string",i2="string",i3="string",mp="int",pc=1,s="int",tx="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCreateFacetCtx.html



-----------------------------------------

polyCreateFacetCtx is undoable, queryable, and editable.

Create a new context to create polygonal objects


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : append          [boolean] ['query', 'edit']
    Allows to switch to polyAppendFacetCtx tool

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

mp    : maximumNumberOfPoints [int] ['query', 'edit']
    Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.

-----------------------------------------

pc    : planarConstraint [boolean] ['query', 'edit']
    allows/avoid new facet to be non-planar.   If on, all new points will be projected onto current facet plane.

-----------------------------------------

s     : subdivision     [int] ['query', 'edit']
    Number of subdivisions for each edge.   Default: 1

-----------------------------------------

tx    : texture         [int]
    What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized textures   Default: 0

    """

def polyCutCtx(q=1,e=1,df=1,ex=1,ef=1,eo="[linear, linear, linear]",i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCutCtx.html



-----------------------------------------

polyCutCtx is undoable, queryable, and editable.

Create a new context to cut facets on polygonal objects


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

df    : deleteFaces     [boolean] ['query', 'edit']
    whether to delete the one-half of the cut-faces of the poly. If true, they are deleted.   Default: false

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

ef    : extractFaces    [boolean] ['query', 'edit']
    whether to extract the cut-faces of the poly into a separate shell. If true, they are extracted.   Default: false

-----------------------------------------

eo    : extractOffset   [[linear, linear, linear]] ['query', 'edit']
    The displacement offset of the cut faces.   Default: 0.5, 0.5, 0.5

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def polyCutUVCtx(q=1,e=1,ls="int",mbc="[float, float, float]",scm=1,stb=1,ssc=1,ss=1,ssd="float",sym="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCutUVCtx.html



-----------------------------------------

polyCutUVCtx is undoable, queryable, and editable.

Create a new context to cut UVs on polygonal objects


-----------------------------------------


Return Value:

boolean  Whether steady stroke is on or not, when querying the steadyStroke
flag.    
float  The distance for a steady stroke, when querying the
steadyStrokeDistance flag.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ls    : loopSpeed       [int] ['query', 'edit']
    Edit the speed of loop cutting.

-----------------------------------------

mbc   : mapBordersColor [[float, float, float]] ['query', 'edit']
    Color of UV map border edges in 3d view.

-----------------------------------------

scm   : showCheckerMap  [boolean] ['query', 'edit']
    Display checker map.

-----------------------------------------

stb   : showTextureBorders [boolean] ['query', 'edit']
    Display texture border edges.

-----------------------------------------

ssc   : showUVShellColoring [boolean] ['query', 'edit']
    Turn on UV shell coloring or not.

-----------------------------------------

ss    : steadyStroke    [boolean] ['query', 'edit']
    Turn on steady stroke or not.

-----------------------------------------

ssd   : steadyStrokeDistance [float] ['query', 'edit']
    The distance for steady stroke.

-----------------------------------------

sym   : symmetry        [int]
    Symmetric modeling.

    """

def polyMergeEdgeCtx(q=1,e=1,anq=1,ex=1,i1="string",i2="string",i3="string",im=1,n="string",pv=1,rs=1,tnq=1,cch=1,ch=1,fe="int",mm="int",mt=1,nds="int",se="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMergeEdgeCtx.html



-----------------------------------------

polyMergeEdgeCtx is undoable, queryable, and editable.

Sews two border edges together.  
The new edge is located either on the first, last, or between both selected
edges, depending on the mode.

Both edges must belong to the same object, and orientations must match (i.e.
normals on corresponding faces must point in the same direction).  
Edge flags are mandatory.

Create a new context to merge edges on polygonal objects


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

anq   : activeNodes     [boolean] ['query']
    Return the active nodes in the tool

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

im    : immediate       [boolean] ['edit']
    Acts on the object not the tool defaults

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

pv    : previous        [boolean] ['edit']
    Reset to previously stored values

-----------------------------------------

rs    : reset           [boolean] ['edit']
    Reset to default values

-----------------------------------------

tnq   : toolNode        [boolean] ['query']
    Return the node used for tool defaults

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

fe    : firstEdge       [int] ['query', 'edit']
    First edge to merge. Invalid default value to force the value to be set.   Default: -1

-----------------------------------------

mm    : mergeMode       [int] ['query', 'edit']
    Merge mode : 0=first, 1=halfway between both edges, 2=second.   Default: 1

-----------------------------------------

mt    : mergeTexture    [boolean] ['query', 'edit']
    Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

se    : secondEdge      [int]
    Second edge to merge. Invalid default value to force the value to be set.   Default: -1

    """

def polyMergeFacetCtx(q=1,e=1,anq=1,ex=1,i1="string",i2="string",i3="string",im=1,n="string",pv=1,rs=1,tnq=1,cch=1,ch=1,ff="int",mm="int",nds="int",sf="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMergeFacetCtx.html



-----------------------------------------

polyMergeFacetCtx is undoable, queryable, and editable.

The second face becomes a hole in the first face.  
The new holed face is located either on the first, last, or between both
selected faces, depending on the mode.

Both faces must belong to the same object.  
Facet flags are mandatory.

Create a new context to merge facets on polygonal objects


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

anq   : activeNodes     [boolean] ['query']
    Return the active nodes in the tool

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

im    : immediate       [boolean] ['edit']
    Acts on the object not the tool defaults

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

pv    : previous        [boolean] ['edit']
    Reset to previously stored values

-----------------------------------------

rs    : reset           [boolean] ['edit']
    Reset to default values

-----------------------------------------

tnq   : toolNode        [boolean] ['query']
    Return the node used for tool defaults

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ff    : firstFacet      [int] ['query', 'edit']
    The number of the first (outer) face to merge.

-----------------------------------------

mm    : mergeMode       [int] ['query', 'edit']
    This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves.   C: Default is None (6).

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

sf    : secondFacet     [int]
    The number of the second (hole) face to merge.

    """

def polySelectCtx(q=1,e=1,ex=1,i1="string",i2="string",i3="string",m="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySelectCtx.html



-----------------------------------------

polySelectCtx is undoable, queryable, and editable.

Create a new context to select polygon components


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

m     : mode            [int]
    Edge loop or Edge ring or Border edge mode

    """

def polySelectEditCtx(q=1,e=1,aef="float",div="int",ex=1,fq=1,i1="string",i2="string",i3="string",ief=1,sma="angle",stp="int",uem=1,abo=1,ac=1,de=1,evo="float",m="int",svo="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySelectEditCtx.html



-----------------------------------------

polySelectEditCtx is undoable, queryable, and editable.

Create a new context to select and edit polygonal objects


-----------------------------------------


Return Value:

string  The context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aef   : adjustEdgeFlow  [float] ['query', 'edit']
    The weight value of the edge vertices to be positioned.   Default: 1.0f

-----------------------------------------

div   : divisions       [int] ['query', 'edit']
    Number of divisions.   Default: 2

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

fq    : fixQuads        [boolean] ['query', 'edit']
    Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.   Default: false

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

ief   : insertWithEdgeFlow [boolean] ['query', 'edit']
    True to enable edge flow. Otherwise, the edge flow is disabled.   Default: false

-----------------------------------------

sma   : smoothingAngle  [angle] ['query', 'edit']
    Angle below which new edges will be smoothed   Default: kPi

-----------------------------------------

stp   : splitType       [int] ['query', 'edit']
    Format: 0 - Absolute, 1 - Relative, 2 - Multi   Default: TdnpolySplitRing::Relative

-----------------------------------------

uem   : useEqualMultiplier [boolean] ['query', 'edit']
    Changes how the profile curve effects the offset when doing a multisplit. If true then the verts will be offset the same distance based on the shortest edge being split. If false then each inserted edge loop will be offset a distance relative to the length of the edge that is being split.   Default: true

-----------------------------------------

abo   : absoluteOffset  [boolean] ['query', 'edit']
    This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.

-----------------------------------------

ac    : autoComplete    [boolean] []
    If true then use auto completion on selections

-----------------------------------------

de    : deleteEdge      [boolean] ['query', 'edit']
    When true, the end edges are deleted so the end triangles are converted to quads.

-----------------------------------------

evo   : endVertexOffset [float] ['query', 'edit']
    Weight value controlling the offset of the end vertex of the edgeloop.

-----------------------------------------

m     : mode            [int] ['query', 'edit']
    which mode to work on. Available modes are 1-loop and 2-ring

-----------------------------------------

svo   : startVertexOffset [float]
    Weight value controlling the offset of the start vertex of the edgeloop.

    """

def polyShortestPathCtx(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyShortestPathCtx.html



-----------------------------------------

polyShortestPathCtx is undoable, queryable, and editable.

Creates a new context to select shortest edge path between two vertices or UVs
in the 3d viewport.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def polySplitCtx(q=1,e=1,es=1,ex=1,i1="string",i2="string",i3="string",ms="int",ps="float",sma="angle",ste=1,s="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySplitCtx.html



-----------------------------------------

polySplitCtx is undoable, queryable, and editable.

Create a new context to split facets on polygonal objects


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

es    : enablesnap      [boolean] ['query', 'edit']
    Enable/disable custom magnet snapping to start/middle/end of edge

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

ms    : magnetsnap      [int] ['query', 'edit']
    number of extra magnets to snap onto, regularly spaced along the edge

-----------------------------------------

ps    : precsnap        [float] ['query', 'edit']
    precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.

-----------------------------------------

sma   : smoothingangle  [angle] ['query', 'edit']
    the threshold that controls whether newly created edges are hard or soft

-----------------------------------------

ste   : snaptoedge      [boolean] ['query', 'edit']
    Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to snap to certain points along the edge.

-----------------------------------------

s     : subdivision     [int]
    number of sub-edges to add between 2 consecutive edge points. Default is 1.

    """

def polySplitCtx2(q=1,e=1,ex=1,i1="string",i2="string",i3="string",aef="float",cte=1,em="int",ief=1,st="float",sec="[float, float, float]",sfc="[float, float, float]",smc="[float, float, float]",svc="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySplitCtx2.html



-----------------------------------------

polySplitCtx2 is undoable, queryable, and editable.

Create a new context to split facets on polygonal objects


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

aef   : adjustEdgeFlow  [float] ['query', 'edit']
    The weight value of the edge vertices to be positioned.

-----------------------------------------

cte   : constrainToEdges [boolean] ['query', 'edit']
    Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to snap to certain points along the edge.

-----------------------------------------

em    : edgeMagnets     [int] ['query', 'edit']
    number of extra magnets to snap onto, regularly spaced along the edge

-----------------------------------------

ief   : insertWithEdgeFlow [boolean] ['query', 'edit']
    True to enable edge flow. Otherwise, the edge flow is disabled.

-----------------------------------------

st    : snapTolerance   [float] ['query', 'edit']
    precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.

-----------------------------------------

sec   : snappedToEdgeColor [[float, float, float]] ['query', 'edit']
    Color for edge snapping.

-----------------------------------------

sfc   : snappedToFaceColor [[float, float, float]] ['query', 'edit']
    Color for face snapping.

-----------------------------------------

smc   : snappedToMagnetColor [[float, float, float]] ['query', 'edit']
    Color for magnet snapping.

-----------------------------------------

svc   : snappedToVertexColor [[float, float, float]]
    Color for vertex snapping.

    """

def projectionContext(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/projectionContext.html



-----------------------------------------

projectionContext is undoable, queryable, and editable.

Set the context for projection manips


-----------------------------------------


Return Value:

string  Context name.    
  
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

def propModCtx(q=1,e=1,ac="string",acf="[float, float]",acp="string",d="[float, float, float]",ex=1,i1="string",i2="string",i3="string",l="float",lp="[float, float]",nc="string",pc="float",pcp="[float, float]",pd="float",pdp="float",s="string",sp="string",t="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/propModCtx.html



-----------------------------------------

propModCtx is undoable, queryable, and editable.

Controls the proportional move context.


-----------------------------------------


Return Value:

string  Name of the new context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : animCurve       [string] ['query', 'edit']
    Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds". The profile of the curve will be used as the profile for propmod function.

-----------------------------------------

acf   : animCurveFalloff [[float, float]] ['query', 'edit']
    The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction while the curve itself provides the magnitudes.

-----------------------------------------

acp   : animCurveParam  [string] ['query', 'edit']
    Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.

-----------------------------------------

d     : direction       [[float, float, float]] ['query', 'edit']
    Direction along which to compute the distance for the distance based drop-off functions. The default is (1 1 1)

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

l     : linear          [float] ['query', 'edit']
    If using linear drop-off function, this is its slope. The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.

-----------------------------------------

lp    : linearParam     [[float, float]] ['query', 'edit']
    If using parametric linear drop-off function, these specify its limits along the U and V directions.

-----------------------------------------

nc    : nurbsCurve      [string] ['query', 'edit']
    Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.

-----------------------------------------

pc    : powerCutoff     [float] ['query', 'edit']
    If using the power drop-off function, this is its distance cutoff value. The default is 10.0.

-----------------------------------------

pcp   : powerCutoffParam [[float, float]] ['query', 'edit']
    If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V. The default cutoff is 10.0.

-----------------------------------------

pd    : powerDegree     [float] ['query', 'edit']
    If using the power drop-off function, this is its degree. The default is 3.

-----------------------------------------

pdp   : powerDegreeParam [float] ['query', 'edit']
    If using the power drop-off function, this is its degree. The default is 3.

-----------------------------------------

s     : script          [string] ['query', 'edit']
    The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated. The script should return a drop- off coefficient which could be negative or zero.

-----------------------------------------

sp    : scriptParam     [string] ['query', 'edit']
    The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated. The script should return a drop-off coefficient which could be negative or zero.

-----------------------------------------

t     : type            [int] ['query', 'edit']
    Choose the type for the drop-off function. Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.

-----------------------------------------

ws    : worldspace      [boolean]
    Set the space in which the tool works. True for world space, false for parametric space.

    """

def regionSelectKeyCtx(q=1,e=1,bot="float",ex=1,ch=1,i1="string",i2="string",i3="string",lft="float",n="string",rgt="float",top="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/regionSelectKeyCtx.html



-----------------------------------------

regionSelectKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to scale keyframes within the
graph editor using the region select tool.


-----------------------------------------


Return Value:

float  Manip values, when queried    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bot   : bottomManip     [float] ['query']
    Get a point located inside the bottom manipulator of the region box, in screen space.

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

lft   : leftManip       [float] ['query']
    Get a point located inside the left manipulator of the region box, in screen space.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

rgt   : rightManip      [float] ['query']
    Get a point located inside the right manipulator of the region box, in screen space.

-----------------------------------------

top   : topManip        [float]
    Get a point located inside the top manipulator of the region box, in screen space.

    """

def renderWindowSelectContext(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderWindowSelectContext.html



-----------------------------------------

renderWindowSelectContext is undoable, queryable, and editable.

Set the selection context for the render view panel.


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def resetTool():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/resetTool.html



-----------------------------------------

resetTool is undoable, NOT queryable, and NOT editable.

This command resets a tool back to its "factory settings"


-----------------------------------------


Return Value:

None
    """

def retimeKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",mbf="int",n="string",sof=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/retimeKeyCtx.html



-----------------------------------------

retimeKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to scale keyframes within the
graph editor using the retime tool.


-----------------------------------------


Return Value:

boolean  Query value from the snapOnFame setting.    
  
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

mbf   : moveByFrame     [int] ['edit']
    Move the selected retime bar by the specified number of frames

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

sof   : snapOnFrame     [boolean]
    When set, the retime markers will snap on frames as they are moved.

    """

def rollCtx(q=1,e=1,ac=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",rs="float",tn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rollCtx.html



-----------------------------------------

rollCtx is undoable, queryable, and editable.

Create, edit, or query a roll context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

rs    : rollScale       [float] ['query', 'edit']
    In degrees of rotation per 100 pixels of cursor drag.

-----------------------------------------

tn    : toolName        [string]
    Name of the specific tool to which this command refers.

    """

def saveToolSettings():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/saveToolSettings.html



-----------------------------------------

saveToolSettings is undoable, NOT queryable, and NOT editable.

This command causes all the tools not on the shelf to save their settings as
optionVars. This is called automatically by the system when Maya exits.


-----------------------------------------


Return Value:

None
    """

def scaleKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",ssk=1,typ="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scaleKeyCtx.html



-----------------------------------------

scaleKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to scale keyframes within the
graph editor


-----------------------------------------


Return Value:

string  Scale type, if the type flag was queried    
boolean  Whether specified keys should be scaled, if the scaleSpecifiedKeys
flag was queried  
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ssk   : scaleSpecifiedKeys [boolean] ['query', 'edit']
    Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.

-----------------------------------------

typ   : type            [string]
    rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)

    """

def scriptCtx(q=1,e=1,alc=1,alo=1,abd=1,ac=1,ait=1,ak=1,aot=1,bcn="string",ca=1,cl=1,clm=1,cv=1,cls=1,c=1,ck=1,cos=1,cpp=1,dim=1,dc=1,eg=1,ep=1,em=1,ers=1,esc=1,ex=1,euc=1,esl=1,fc=1,fi=1,fcs="script",fl=1,fo=1,fas=1,hs=1,ha=1,ch=1,hl=1,iii=1,iee=1,ikh=1,i1="string",i2="string",i3="string",ip=1,ig=1,iso=1,j=1,jp=1,lac=1,la=1,lp=1,lt=1,ra=1,lc=1,luv=1,xyz=1,ncl=1,npr=1,nps=1,nr=1,n="string",nl=1,nc=1,ns=1,ocm=1,ol=1,pr=1,ps=1,pl=1,p=1,pe=1,pf=1,pfe=1,puv=1,pv=1,pvf=1,rb=1,rc=1,rp=1,sp=1,sc=1,sh=1,sae=1,sac=1,sat=1,dsp="string",snh="string",snp="string",ssc="int",ssh="string",ssp="string",sm=1,spr=1,spc=1,str=1,sd=1,sme=1,smf=1,smp=1,smu=1,se=1,sf=1,sk=1,spp=1,sr=1,suv=1,tx=1,t="string",tct="string",tf="script",ts="script",tss="int",v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scriptCtx.html



-----------------------------------------

scriptCtx is undoable, queryable, and editable.

This command allows a user to create their own tools based on the selection
tool. A number of selection lists can be collected, the behaviour of the
selection and the selection masks are fully customizable, etc.

The command is processed prior to being executed. The keyword "$Selection#"
where # is a number 1 or greater specifies a selection set. The context can
specify several selection sets which are substituted in place of the
$Selection# keyword in the form of a Mel string array. Items that are specific
per set need to be specified in each set, if they are going to be specified
for any of the sets. See examples below.

In addition, in order to specify the type of selection you need to be making,
any of the selection type flags from "selectType" command can be used here.


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

alc   : allComponents   [boolean] ['query']
    Set all component selection masks on/off

-----------------------------------------

alo   : allObjects      [boolean] ['query']
    Set all object selection masks on/off

-----------------------------------------

abd   : animBreakdown   [boolean] ['query']
    Set animation breakdown selection mask on/off.

-----------------------------------------

ac    : animCurve       [boolean] ['query']
    Set animation curve selection mask on/off.

-----------------------------------------

ait   : animInTangent   [boolean] ['query']
    Set animation in-tangent selection mask on/off.

-----------------------------------------

ak    : animKeyframe    [boolean] ['query']
    Set animation keyframe selection mask on/off.

-----------------------------------------

aot   : animOutTangent  [boolean] ['query']
    Set animation out-tangent selection mask on/off.

-----------------------------------------

bcn   : baseClassName   [string] ['query', 'edit']
    This string will be used to produce MEL function names for the property sheets for the tool. For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets. The default is "scriptTool".

-----------------------------------------

ca    : camera          [boolean] ['query']
    Set camera selection mask on/off. (object flag)

-----------------------------------------

cl    : cluster         [boolean] ['query']
    Set cluster selection mask on/off. (object flag)

-----------------------------------------

clm   : collisionModel  [boolean] ['query']
    Set collision model selection mask on/off. (object flag)

-----------------------------------------

cv    : controlVertex   [boolean] ['query']
    Set control vertex selection mask on/off. (component flag)

-----------------------------------------

cls   : cumulativeLists [boolean] ['query', 'edit']
    If set, the selection lists will be cumulative. For example, the second list will contain all the items from the first list, the third all the items from the second list etc. Make sure your script specified above takes that into account. Relevant if there is more than one selection set.

-----------------------------------------

c     : curve           [boolean] ['query']
    Set curve selection mask on/off. (object flag)

-----------------------------------------

ck    : curveKnot       [boolean] ['query']
    Set curve knot selection mask on/off. (component flag)

-----------------------------------------

cos   : curveOnSurface  [boolean] ['query']
    Set curve-on-surface selection mask on/off. (object flag)

-----------------------------------------

cpp   : curveParameterPoint [boolean] ['query']
    Set curve parameter point selection mask on/off. (component flag)

-----------------------------------------

dim   : dimension       [boolean] ['query']
    Set dimension shape selection mask on/off. (object flag)

-----------------------------------------

dc    : dynamicConstraint [boolean] ['query']
    Set dynamicConstraint selection mask on/off. (object flag)

-----------------------------------------

eg    : edge            [boolean] ['query']
    Set mesh edge selection mask on/off. (component flag)

-----------------------------------------

ep    : editPoint       [boolean] ['query']
    Set edit-point selection mask on/off. (component flag)

-----------------------------------------

em    : emitter         [boolean] ['query']
    Set emitter selection mask on/off. (object flag)

-----------------------------------------

ers   : enableRootSelection [boolean] ['query', 'edit']
    If set, the items to be selected are at their root transform level. Default is false.

-----------------------------------------

esc   : escToQuit       [boolean] ['query', 'edit']
    If set to true, exit the tool when press "Esc". Default is false.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

euc   : exitUponCompletion [boolean] ['query', 'edit']
    If set, completing the last selection set will exit the tool. Default is true.

-----------------------------------------

esl   : expandSelectionList [boolean] ['query', 'edit']
    If set, the selection lists will expand to have a single component in each item. You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.  To ensure that components on the same object are returned in the order in which they are selected, use the `selectPref -trackSelectionOrder on` command in your `-toolStart` script to enable ordered selection, then restore it to its original value in your `-toolFinish` script.

-----------------------------------------

fc    : facet           [boolean] ['query']
    Set mesh face selection mask on/off. (component flag)

-----------------------------------------

fi    : field           [boolean] ['query']
    Set field selection mask on/off. (object flag)

-----------------------------------------

fcs   : finalCommandScript [script] ['query', 'edit']
    Supply the script that will be run when the user presses the enter key and the context is completed. Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...

-----------------------------------------

fl    : fluid           [boolean] ['query']
    Set fluid selection mask on/off. (object flag)

-----------------------------------------

fo    : follicle        [boolean] ['query']
    Set follicle selection mask on/off. (object flag)

-----------------------------------------

fas   : forceAddSelect  [boolean] ['query', 'edit']
    If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed. Default is false.  ### Flags for each selection set. These flags are multi-use.

-----------------------------------------

hs    : hairSystem      [boolean] ['query']
    Set hairSystem selection mask on/off. (object flag)

-----------------------------------------

ha    : handle          [boolean] ['query']
    Set object handle selection mask on/off. (object flag)

-----------------------------------------

ch    : history         [boolean] []
    If this is a tool command, turn the construction history on for the tool in question.

-----------------------------------------

hl    : hull            [boolean] ['query']
    Set hull selection mask on/off. (component flag)

-----------------------------------------

iii   : ignoreInvalidItems [boolean] ['query', 'edit']
    If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it". You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets. If this flag is set, those items will be detected and ignored. You will never know it happened. Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need. If this flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.

-----------------------------------------

iee   : ikEndEffector   [boolean] ['query']
    Set ik end effector selection mask on/off. (object flag)

-----------------------------------------

ikh   : ikHandle        [boolean] ['query']
    Set ik handle selection mask on/off. (object flag)

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

ip    : imagePlane      [boolean] ['query']
    Set image plane selection mask on/off. (component flag)

-----------------------------------------

ig    : implicitGeometry [boolean] ['query']
    Set implicit geometry selection mask on/off. (object flag)

-----------------------------------------

iso   : isoparm         [boolean] ['query']
    Set surface iso-parm selection mask on/off. (component flag)

-----------------------------------------

j     : joint           [boolean] ['query']
    Set ik handle selection mask on/off. (object flag)

-----------------------------------------

jp    : jointPivot      [boolean] ['query']
    Set joint pivot selection mask on/off. (component flag)

-----------------------------------------

lac   : lastAutoComplete [boolean] ['query', 'edit']
    True if auto complete is set for the last selection set, false otherwise. Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.

-----------------------------------------

la    : lattice         [boolean] ['query']
    Set lattice selection mask on/off. (object flag)

-----------------------------------------

lp    : latticePoint    [boolean] ['query']
    Set lattice point selection mask on/off. (component flag)

-----------------------------------------

lt    : light           [boolean] ['query']
    Set light selection mask on/off. (object flag)

-----------------------------------------

ra    : localRotationAxis [boolean] ['query']
    Set local rotation axis selection mask on/off. (component flag)

-----------------------------------------

lc    : locator         [boolean] ['query']
    Set locator (all types) selection mask on/off. (object flag)

-----------------------------------------

luv   : locatorUV       [boolean] ['query']
    Set uv locator selection mask on/off. (object flag)

-----------------------------------------

xyz   : locatorXYZ      [boolean] ['query']
    Set xyz locator selection mask on/off. (object flag)

-----------------------------------------

ncl   : nCloth          [boolean] ['query']
    Set nCloth selection mask on/off. (object flag)

-----------------------------------------

npr   : nParticle       [boolean] ['query']
    Set nParticle point selection mask on/off. (component flag)

-----------------------------------------

nps   : nParticleShape  [boolean] ['query']
    Set nParticle shape selection mask on/off. (object flag)

-----------------------------------------

nr    : nRigid          [boolean] ['query']
    Set nRigid selection mask on/off. (object flag)

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

nl    : nonlinear       [boolean] ['query']
    Set nonlinear selection mask on/off. (object flag)

-----------------------------------------

nc    : nurbsCurve      [boolean] ['query']
    Set nurbs-curve selection mask on/off. (object flag)

-----------------------------------------

ns    : nurbsSurface    [boolean] ['query']
    Set nurbs-surface selection mask on/off. (object flag)

-----------------------------------------

ocm   : objectComponent [boolean] ['query']
    Component flags apply to object mode.

-----------------------------------------

ol    : orientationLocator [boolean] ['query']
    Set orientation locator selection mask on/off. (object flag)

-----------------------------------------

pr    : particle        [boolean] ['query']
    Set particle point selection mask on/off. (component flag)

-----------------------------------------

ps    : particleShape   [boolean] ['query']
    Set particle shape selection mask on/off. (object flag)

-----------------------------------------

pl    : plane           [boolean] ['query']
    Set sketch plane selection mask on/off. (object flag)

-----------------------------------------

p     : polymesh        [boolean] ['query']
    Set poly-mesh selection mask on/off. (object flag)

-----------------------------------------

pe    : polymeshEdge    [boolean] ['query']
    Set poly-mesh edge selection mask on/off. (component flag)

-----------------------------------------

pf    : polymeshFace    [boolean] ['query']
    Set poly-mesh face selection mask on/off. (component flag)

-----------------------------------------

pfe   : polymeshFreeEdge [boolean] ['query']
    Set poly-mesh free-edge selection mask on/off. (component flag)

-----------------------------------------

puv   : polymeshUV      [boolean] ['query']
    Set poly-mesh UV point selection mask on/off. (component flag)

-----------------------------------------

pv    : polymeshVertex  [boolean] ['query']
    Set poly-mesh vertex selection mask on/off. (component flag)

-----------------------------------------

pvf   : polymeshVtxFace [boolean] ['query']
    Set poly-mesh vertexFace selection mask on/off. (component flag)

-----------------------------------------

rb    : rigidBody       [boolean] ['query']
    Set rigid body selection mask on/off. (object flag)

-----------------------------------------

rc    : rigidConstraint [boolean] ['query']
    Set rigid constraint selection mask on/off. (object flag)

-----------------------------------------

rp    : rotatePivot     [boolean] ['query']
    Set rotate pivot selection mask on/off. (component flag)

-----------------------------------------

sp    : scalePivot      [boolean] ['query']
    Set scale pivot selection mask on/off. (component flag)

-----------------------------------------

sc    : sculpt          [boolean] ['query']
    Set sculpt selection mask on/off. (object flag)

-----------------------------------------

sh    : selectHandle    [boolean] ['query']
    Set select handle selection mask on/off. (component flag)

-----------------------------------------

sae   : setAllowExcessCount [boolean] ['edit']
    If set, the number if items is to be interpreted as the minimum.

-----------------------------------------

sac   : setAutoComplete [boolean] ['edit']
    If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.

-----------------------------------------

sat   : setAutoToggleSelection [boolean] ['edit']
    If set to true, it is as if "shift" key is pressed when there are no modifiers pressed. That means that you get the "toggle select" behaviour by default. This only applies to the 3D view, and the selection done in the hypergraph, outliner or elsewhere is still a subject to the usual rules.

-----------------------------------------

dsp   : setDoneSelectionPrompt [string] ['edit']
    If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set. If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.

-----------------------------------------

snh   : setNoSelectionHeadsUp [string] ['edit']
    Supply a string that will be shown as a heads up prompt when there is nothing selected. This must be set separately for each selection set.

-----------------------------------------

snp   : setNoSelectionPrompt [string] ['edit']
    Supply a string that will be shown as help when there is nothing selected. This must be set separately for each selection set.

-----------------------------------------

ssc   : setSelectionCount [int] ['edit']
    The number of items in this selection set. 0 means as many as you need until completion.

-----------------------------------------

ssh   : setSelectionHeadsUp [string] ['edit']
    Supply a string that will be shown as a heads up prompt when there is something selected. This must be set separately for each selection set.

-----------------------------------------

ssp   : setSelectionPrompt [string] ['edit']
    Supply a string that will be shown as help when there is something selected. This must be set separately for each selection set.

-----------------------------------------

sm    : showManipulators [boolean] ['query', 'edit']
    If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.

-----------------------------------------

spr   : spring          [boolean] ['query']
    Set spring shape selection mask on/off. (object flag)

-----------------------------------------

spc   : springComponent [boolean] ['query']
    Set individual spring selection mask on/off. (component flag)

-----------------------------------------

str   : stroke          [boolean] ['query']
    Set the Paint Effects stroke selection mask on/off. (object flag)

-----------------------------------------

sd    : subdiv          [boolean] ['query']
    Set subdivision surfaces selection mask on/off. (object flag)

-----------------------------------------

sme   : subdivMeshEdge  [boolean] ['query']
    Set subdivision surfaces mesh edge selection mask on/off. (component flag)

-----------------------------------------

smf   : subdivMeshFace  [boolean] ['query']
    Set subdivision surfaces mesh face selection mask on/off. (component flag)

-----------------------------------------

smp   : subdivMeshPoint [boolean] ['query']
    Set subdivision surfaces mesh point selection mask on/off. (component flag)

-----------------------------------------

smu   : subdivMeshUV    [boolean] ['query']
    Set subdivision surfaces mesh UV map selection mask on/off. (component flag)

-----------------------------------------

se    : surfaceEdge     [boolean] ['query']
    Set surface edge selection mask on/off. (component flag)

-----------------------------------------

sf    : surfaceFace     [boolean] ['query']
    Set surface face selection mask on/off. (component flag)

-----------------------------------------

sk    : surfaceKnot     [boolean] ['query']
    Set surface knot selection mask on/off. (component flag)

-----------------------------------------

spp   : surfaceParameterPoint [boolean] ['query']
    Set surface parameter point selection mask on/off. (component flag)

-----------------------------------------

sr    : surfaceRange    [boolean] ['query']
    Set surface range selection mask on/off. (component flag)

-----------------------------------------

suv   : surfaceUV       [boolean] ['query']
    Set surface uv selection mask on/off. (component flag)

-----------------------------------------

tx    : texture         [boolean] ['query']
    Set texture selection mask on/off. (object flag)

-----------------------------------------

t     : title           [string] ['query', 'edit']
    Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.

-----------------------------------------

tct   : toolCursorType  [string] ['query', 'edit']
    Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn", "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".

-----------------------------------------

tf    : toolFinish      [script] ['query', 'edit']
    Supply the script that will be run when the user exits the script.

-----------------------------------------

ts    : toolStart       [script] ['query', 'edit']
    Supply the script that will be run when the user first enters the script

-----------------------------------------

tss   : totalSelectionSets [int] ['query', 'edit']
    Total number of selection sets.

-----------------------------------------

v     : vertex          [boolean]
    Set mesh vertex selection mask on/off. (component flag)

    """

def sculptMeshCacheChangeCloneSource(q=1,e=1,bs="string",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sculptMeshCacheChangeCloneSource.html



-----------------------------------------

sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.

This command changes the source blend shape and target for the clone target
tool. Used internally for undo/redo, and should not be called directly.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bs    : blendShape      [string] ['query', 'edit']
    Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.

-----------------------------------------

t     : target          [string]
    Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.

    """

def sculptMeshCacheCtx(q=1,e=1,asz=1,ast=1,aal=1,bd="int",bsz="float",bst="float",bur="float",chs=1,cm="int",css="string",cas="string",cts=1,d="int",df=1,dm=1,dw=1,ft="int",fl="float",ff="float",frm=1,fsl=1,gfp=1,gs=1,gtw=1,inv=1,lm="string",lsb=1,mt="[uint, uint, uint, float, float]",msz="float",mst="float",mr="int",m="string",ots=1,rcs=1,sfc="string",sz="float",s="float",stp="string",sfx=1,sfy=1,sos=1,sp="int",srd=1,sre="int",srx=1,sry=1,spx="float",spy="float",srr="float",src="float",srs="float",sr="float",ssd="float",st="float",upl=1,ugs=1,ssp=1,usd=1,usi=1,uss=1,wst=1,wa="float",wc="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sculptMeshCacheCtx.html



-----------------------------------------

sculptMeshCacheCtx is undoable, queryable, and editable.

This is a tool context command for mesh cache sculpting tool.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

asz   : adjustSize      [boolean] ['edit']
    If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.

-----------------------------------------

ast   : adjustStrength  [boolean] ['edit']
    If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.

-----------------------------------------

aal   : affectAllLayers [boolean] ['query', 'edit']
    If true, the brush affects all layers at once.

-----------------------------------------

bd    : brushDirection  [int] ['query', 'edit']
    Specifies the direction of the named brush.

-----------------------------------------

bsz   : brushSize       [float] ['query', 'edit']
    Specifies the world-space size of the named brush.

-----------------------------------------

bst   : brushStrength   [float] ['query', 'edit']
    Specifies the world-space strength of the named brush.

-----------------------------------------

bur   : buildUpRate     [float] ['query', 'edit']
    Specifies the brush strength increasing along the stroke.

-----------------------------------------

chs   : cloneHideSource [boolean] ['query', 'edit']
    True if the cloned source should be hidden.

-----------------------------------------

cm    : cloneMethod     [int] ['query', 'edit']
    Controls how the source delta vectors should change the target. 0=copy 1=add

-----------------------------------------

css   : cloneShapeSource [string] ['query', 'edit']
    Name of the shape source to clone.

-----------------------------------------

cas   : cloneTargetSource [string] ['query', 'edit']
    Name of the target source of the clone.

-----------------------------------------

cts   : constrainToSurface [boolean] ['query', 'edit']
    If true, the modification keeps the surface curvature.

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    Specifies the direction in which the vertices are moved.

-----------------------------------------

df    : displayFrozen   [boolean] ['query', 'edit']
    If false, turns off the display of frozen area on the object.

-----------------------------------------

dm    : displayMask     [boolean] ['query', 'edit']
    If false, turns off the display of masked area on the object.

-----------------------------------------

dw    : displayWireframe [boolean] ['query', 'edit']
    If false, turns off the wireframe display of the object.

-----------------------------------------

ft    : falloffType     [int] ['query', 'edit']
    Specifies how the brush determines which vertices to affect.

-----------------------------------------

fl    : flood           [float] ['edit']
    Sets the brush effect for each vertex to the given value.

-----------------------------------------

ff    : floodFreeze     [float] ['edit']
    Sets the freeze value for each vertex to the given value.

-----------------------------------------

frm   : frame           [boolean] ['edit']
    Frames on the sculpted area.

-----------------------------------------

fsl   : freezeSelection [boolean] ['edit']
    Freezes selected components.

-----------------------------------------

gfp   : grabFollowPath  [boolean] ['query', 'edit']
    If true, the grab brush effect follows mouse movement.

-----------------------------------------

gs    : grabSilhouette  [boolean] ['query', 'edit']
    If true, the grab brush uses paint-through mode.

-----------------------------------------

gtw   : grabTwist       [boolean] ['query', 'edit']
    If true, the grab brush twists the vertices.

-----------------------------------------

inv   : inverted        [boolean] ['query', 'edit']
    If true, inverts the effect of the brush.

-----------------------------------------

lm    : lastMode        [string] ['query', 'edit']
    Specifies the type of the last active sculpting brush.

-----------------------------------------

lsb   : lockShellBorder [boolean] ['query', 'edit']
    Lock the shell borders so that they won't be moved by a UV texture brush.

-----------------------------------------

mt    : makeStroke      [[uint, uint, uint, float, float]] ['edit']
    Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke. The first argument is the mesh index. The second argument is the side index. use 0 for the original side, and 1 for the mirrored side The third argument is the face index within the specified mesh. The fourth and fifth arguments are the face coordinates within the specified face.

-----------------------------------------

msz   : minSize         [float] ['query', 'edit']
    Specifies the minimum size percentage of the current brush.

-----------------------------------------

mst   : minStrength     [float] ['query', 'edit']
    Specifies the minimum strength percentage of the current brush.

-----------------------------------------

mr    : mirror          [int] ['query', 'edit']
    Specifies the mirror mode of the brush.

-----------------------------------------

m     : mode            [string] ['query', 'edit']
    Specifies the type of sculpting effect the brush will perform.

-----------------------------------------

ots   : orientToSurface [boolean] ['query', 'edit']
    If true, aligns the brush display to the surface of the mesh.

-----------------------------------------

rcs   : recordStroke    [boolean] ['query', 'edit']
    Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.

-----------------------------------------

sfc   : sculptFalloffCurve [string] ['query', 'edit']
    Specifies the falloff curve of sculpting effect the brush will perform.

-----------------------------------------

sz    : size            [float] ['query', 'edit']
    Specifies the world-space size of the current brush.

-----------------------------------------

s     : stampDistance   [float] ['query', 'edit']
    Specifies the stamping distance of the brush.

-----------------------------------------

stp   : stampFile       [string] ['query', 'edit']
    Specifies an image file to use as stamp.

-----------------------------------------

sfx   : stampFlipX      [boolean] ['query', 'edit']
    Specifies if the brush stamp is flipped on the X axis.

-----------------------------------------

sfy   : stampFlipY      [boolean] ['query', 'edit']
    Specifies if the brush stamp is flipped on the Y axis.

-----------------------------------------

sos   : stampOrientToStroke [boolean] ['query', 'edit']
    Specifies if the brush stamp is aligned to the stroke direction.

-----------------------------------------

sp    : stampPlacement  [int] ['query', 'edit']
    Specifies the placement mode of the stamp image.

-----------------------------------------

srd   : stampRandomization [boolean] ['query', 'edit']
    Specifies if the brush stamp is randomized.

-----------------------------------------

sre   : stampRandomizationSeed [int] ['edit']
    Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.

-----------------------------------------

srx   : stampRandomizeFlipX [boolean] ['query', 'edit']
    Specifies if the brush stamp flipping is randomized on the X axis.

-----------------------------------------

sry   : stampRandomizeFlipY [boolean] ['query', 'edit']
    Specifies if the brush stamp flipping is randomized on the Y axis.

-----------------------------------------

spx   : stampRandomizePosX [float] ['query', 'edit']
    Specifies the stamp X position value is randomized.

-----------------------------------------

spy   : stampRandomizePosY [float] ['query', 'edit']
    Specifies the stamp Y position value is randomized.

-----------------------------------------

srr   : stampRandomizeRotation [float] ['query', 'edit']
    Specifies the stamp rotation value is randomized.

-----------------------------------------

src   : stampRandomizeScale [float] ['query', 'edit']
    Specifies the stamp scale value is randomized.

-----------------------------------------

srs   : stampRandomizeStrength [float] ['query', 'edit']
    Specifies the stamp strength value is randomized.

-----------------------------------------

sr    : stampRotation   [float] ['query', 'edit']
    Specifies the rotation value of the stamp image.

-----------------------------------------

ssd   : steadyStrokeDistance [float] ['query', 'edit']
    Specifies the distance for the steady stroke.

-----------------------------------------

st    : strength        [float] ['query', 'edit']
    Specifies the world-space strength of the current brush.

-----------------------------------------

upl   : updatePlane     [boolean] ['query', 'edit']
    Recalculates the underlying tool plane for each stamp in a stroke.

-----------------------------------------

ugs   : useGlobalSize   [boolean] ['query', 'edit']
    If true, all the brushes have a shared size property; otherwise size is local.

-----------------------------------------

ssp   : useScreenSpace  [boolean] ['query', 'edit']
    If true, the brush size is in screen space pixels.

-----------------------------------------

usd   : useStampDistance [boolean] ['query', 'edit']
    Force the stamps to be spread out along the stroke, rather than building up continually.

-----------------------------------------

usi   : useStampImage   [boolean] ['query', 'edit']
    Specifies if the brush uses a stamp image.

-----------------------------------------

uss   : useSteadyStroke [boolean] ['query', 'edit']
    Turns using steady stroke on/off.

-----------------------------------------

wst   : wholeStroke     [boolean] ['query', 'edit']
    Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.

-----------------------------------------

wa    : wireframeAlpha  [float] ['query', 'edit']
    Sets the alpha value of the wireframe for the object that is being sculpted.

-----------------------------------------

wc    : wireframeColor  [[float, float, float]]
    Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.

    """

def selectContext(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectContext.html



-----------------------------------------

selectContext is undoable, queryable, and editable.

Creates a context to perform selection.


-----------------------------------------


Return Value:

string  Name of the context created    
  
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

def selectKeyCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectKeyCtx.html



-----------------------------------------

selectKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to select keyframes within
the graph editor


-----------------------------------------


Return Value:

None

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

def selectKeyframeRegionCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectKeyframeRegionCtx.html



-----------------------------------------

selectKeyframeRegionCtx is undoable, queryable, and editable.

This command creates a context which may be used to select keyframes within
the keyframe region of the dope sheet editor


-----------------------------------------


Return Value:

None

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

def setEditCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setEditCtx.html



-----------------------------------------

setEditCtx is undoable, queryable, and editable.

This command creates a tool that can be used to modify set membership.


-----------------------------------------


Return Value:

string  The name of the context    
  
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

def setKeyCtx(q=1,e=1,bd=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setKeyCtx.html



-----------------------------------------

setKeyCtx is undoable, queryable, and editable.

This command creates a context which may be used to set keys within the graph
editor


-----------------------------------------


Return Value:

boolean  Value of the breakdown flag, when queried    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bd    : breakdown       [boolean] ['query', 'edit']
    Specifies whether or not to create breakdown keys

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

def setToolTo():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setToolTo.html



-----------------------------------------

setToolTo is undoable, NOT queryable, and NOT editable.

This command switches control to the named context.


-----------------------------------------


Return Value:

None
    """

def shadingGeometryRelCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",ofc="string",onc="string",s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shadingGeometryRelCtx.html



-----------------------------------------

shadingGeometryRelCtx is undoable, queryable, and editable.

This command creates a context that can be used for associating geometry to
shading groups. You can put the context into shading-centric mode by using the
-shadingCentric flag and specifying true. This means that the shading group is
selected first then geometry associated with the shading group are
highlighted. Subsequent selections result in assignments.

Specifying -shadingCentric false means that the geometry is to be selected
first. The shading group associated with the geometry will then be selected
and subsequent selections will result in assignments being made.


-----------------------------------------


Return Value:

string  Name of the context created.    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ofc   : offCommand      [string] ['query', 'edit']
    command to be issued when context is turned on

-----------------------------------------

onc   : onCommand       [string] ['query', 'edit']
    command to be issued when context is turned on

-----------------------------------------

s     : shadingCentric  [boolean]
    shading-centric mode.

    """

def shadingLightRelCtx(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",ofc="string",onc="string",s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shadingLightRelCtx.html



-----------------------------------------

shadingLightRelCtx is undoable, queryable, and editable.

This command creates a context that can be used for associating lights to
shading groups. You can put the context into shading-centric mode by using the
-shadingCentric flag and specifying true. This means that the shading group is
selected first then lights associated with the shading group are highlighted.
Subsequent selections result in assignments.

Specifying -shadingCentric false means that the light is to be selected first.
The shading groups associated with the light will then be selected and
subsequent selections will result in assignments being made.


-----------------------------------------


Return Value:

string  Name of the context created.    
  
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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ofc   : offCommand      [string] ['query', 'edit']
    command to be issued when context is turned on

-----------------------------------------

onc   : onCommand       [string] ['query', 'edit']
    command to be issued when context is turned on

-----------------------------------------

s     : shadingCentric  [boolean]
    shading-centric mode.

    """

def showManipCtx(q=1,e=1,cnn=1,ex=1,ch=1,i1="string",i2="string",i3="string",incSnap="[uint, boolean]",isr="[uint, boolean]",isu=1,isv="[uint, float]",ls=1,n="string",tis=1,tf="script",ts="script"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/showManipCtx.html



-----------------------------------------

showManipCtx is undoable, queryable, and editable.

This command can be used to create a show manip context. The show manip
context will display manips for all selected objects that have valid manips
defined for them.


-----------------------------------------


Return Value:

string  The name of the newly created context.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cnn   : currentNodeName [boolean] ['query']
    Returns the name of the first node that the context is attached to.

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

incSnap : incSnap         [[uint, boolean]] ['query', 'edit']
    If true, the manipulator owned by the context will use incremental snapping for specified mode.

-----------------------------------------

isr   : incSnapRelative [[uint, boolean]] ['query', 'edit']
    If true, the manipulator owned by the context will use relative incremental snapping for specified mode.

-----------------------------------------

isu   : incSnapUI       [boolean] ['query']
    Returns an array of elements indicating what kind of incremental snap UI is required by the manipulator owned by the context. If no UI is required, the result array will contain a single element of with the value 0. The other values and their meanings are:    * 1 - UI for linear incremental translate   * 2 - UI for incremental rotate   * 3 - UI for inclremental scale

-----------------------------------------

isv   : incSnapValue    [[uint, float]] ['query', 'edit']
    Supply the step value which the manipulator owned by the context will use for specified mode.

-----------------------------------------

ls    : lockSelection   [boolean] ['query', 'edit']
    If true, this context will never change the current selection. By default this is set to false.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

tis   : toggleIncSnap   [boolean] ['edit']
    Toggles (enables/disables) snapping for all modes.

-----------------------------------------

tf    : toolFinish      [script] ['query', 'edit']
    Supply the script that will be run when the user exits the script.

-----------------------------------------

ts    : toolStart       [script]
    Supply the script that will be run when the user first enters the script

    """

def skinBindCtx(q=1,e=1,a="string",ax="string",cr="string",ci="string",di="int",dn=1,ex=1,fc="string",ch=1,i1="string",i2="string",i3="string",n="string",s=1,t="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/skinBindCtx.html



-----------------------------------------

skinBindCtx is undoable, queryable, and editable.

This command creates a tool that can be used to edit volumes from an
interactive bind.


-----------------------------------------


Return Value:

string  The name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : about           [string] ['query', 'edit']
    The space in which the axis should be mirrored. Valid values are: "world" and "object".

-----------------------------------------

ax    : axis            [string] ['query', 'edit']
    The mirror axis. Valid values are: "x","y", and "z".

-----------------------------------------

cr    : colorRamp       [string] ['query', 'edit']
    Set the values on the color ramp used to display the weight values.

-----------------------------------------

ci    : currentInfluence [string] ['query', 'edit']
    Set the index of the current influence or volume to be adjusted by the manipulator.

-----------------------------------------

di    : displayInactiveMode [int] ['query', 'edit']
    Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes

-----------------------------------------

dn    : displayNormalized [boolean] ['query', 'edit']
    Display raw select weights (false) or finalized normalized weights (true).

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

fc    : falloffCurve    [string] ['query', 'edit']
    Set the values on the falloff curve control.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

s     : symmetry        [boolean] ['query', 'edit']
    Controls whether or not the tool operates in symmetric (mirrored) mode.

-----------------------------------------

t     : tolerance       [float]
    The tolerance setting for determining whether another influence is symmetric to the the current influence.

    """

def softModCtx(q=1,e=1,ds="string",ex=1,fc=1,i1="string",i2="string",i3="string",rst=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/softModCtx.html



-----------------------------------------

softModCtx is undoable, queryable, and editable.

Controls the softMod context.


-----------------------------------------


Return Value:

string  \- name of the new context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ds    : dragSlider      [string] ['edit']
    Specify the slider mode for hotkey radius resizing.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

fc    : falseColor      [boolean] ['edit']
    Enable or disable false color display on the soft mod manipulator.

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

rst   : reset           [boolean]
    Reset the tool options to their default values.

    """

def srtContext(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/srtContext.html



-----------------------------------------

srtContext is undoable, queryable, and editable.

This command can be used to create a combined transform
(translate/scale/rotate) context.


-----------------------------------------


Return Value:

string  \- name of the newly created context    
  
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

def targetWeldCtx(q=1,e=1,ex=1,i1="string",i2="string",i3="string",mtc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/targetWeldCtx.html



-----------------------------------------

targetWeldCtx is undoable, queryable, and editable.

Create a new context to weld vertices together on a poly object.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

mtc   : mergeToCenter   [boolean]
    If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge. If set to false the source vertex will be moved to the target vertex before doing the merge.

    """

def texCutContext(q=1,e=1,asz=1,dsb=1,ess="float",ex=1,ch=1,i1="string",i2="string",i3="string",m="string",mvr="float",n="string",sz="float",ss=1,ssd="float",tts=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texCutContext.html



-----------------------------------------

texCutContext is undoable, queryable, and editable.

This command creates a context for cut uv tool. This context only works in the
UV editor.


-----------------------------------------


Return Value:

float  Size of the brush rung, when querying brushSize    
float  The value of the edge selection sensitivity, when querying the
edgeSelectSensitive flag.  
boolean  Whether steady stroke is on or not, when querying the steadyStroke
flag.  
float  The distance for a steady stroke, when querying the
steadyStrokeDistance flag.  
float  The cut open ratio relative to edge length, when querying the moveRatio
flag.  
string  The type of effect the brush will perform, when querying the mode
flag.  
boolean  Whether shell borders are displayed, when querying the
displayShellBorders flag.  
boolean  Current touch-to-sew mode, when querying the touchToSew flag.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

asz   : adjustSize      [boolean] ['edit']
    If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous mode.

-----------------------------------------

dsb   : displayShellBorders [boolean] ['query', 'edit']
    Toggle the display of shell borders.

-----------------------------------------

ess   : edgeSelectSensitive [float] ['query', 'edit']
    Set the value of the edge selection sensitivity.

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

m     : mode            [string] ['query', 'edit']
    Specifies the type of effect the brush will perform, Cut or Sew.

-----------------------------------------

mvr   : moveRatio       [float] ['query', 'edit']
    The cut open ratio relative to edge length.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

sz    : size            [float] ['query', 'edit']
    Brush size value of the brush ring.

-----------------------------------------

ss    : steadyStroke    [boolean] ['query', 'edit']
    Turn on steady stroke or not.

-----------------------------------------

ssd   : steadyStrokeDistance [float] ['query', 'edit']
    The distance for steady stroke.

-----------------------------------------

tts   : touchToSew      [boolean]
    Toggle the touch to sew mode.

    """

def texLatticeDeformContext(q=1,e=1,ev="float",ex=1,ch=1,i1="string",i2="string",i3="string",lc="uint",lr="uint",n="string",smm=1,spm=1,ubr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texLatticeDeformContext.html



-----------------------------------------

texLatticeDeformContext is undoable, queryable, and editable.

This command creates a context which may be used to deform UV maps with
lattice manipulator. This context only works in the texture UV editor.


-----------------------------------------


Return Value:

int  Number of column divisions, when querying the latticeColumns flag.    
int  Number of row divisions, when querying the latticeRows flag.  
float  Value of the deform envelope, when querying the envelope flag.  
boolean  Whether snapping to pixels is on, when querying the snapPixelMode
flag.  
boolean  Whether the bounding rectangle is to be used for deforemation, when
querying the useBoundingRect flag.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ev    : envelope        [float] ['query', 'edit']
    Specifies the influence of the lattice.

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

lc    : latticeColumns  [uint] ['query', 'edit']
    Specifies the number column points the lattice contains. The maximum size lattice is restricted to 8 columns.

-----------------------------------------

lr    : latticeRows     [uint] ['query', 'edit']
    Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

smm   : showMoveManipulator [boolean] ['query', 'edit']
    Specifies whether show move manipulator in UV Editor

-----------------------------------------

spm   : snapPixelMode   [boolean] ['query', 'edit']
    Specifies the influenced uv points should be snapped to a pixel center or corner.

-----------------------------------------

ubr   : useBoundingRect [boolean]
    When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice. When this is disabled the extents of the marquee selections are used as the extents for the lattice.

    """

def texManipContext(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texManipContext.html



-----------------------------------------

texManipContext is undoable, queryable, and editable.

Command used to register the texSelectCtx tool. Command used to register the
texManipCtx tool.


-----------------------------------------


Return Value:

string  : name of the context created    
string  : name of the context created  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def texMoveContext(q=1,e=1,epm=1,ex=1,i1="string",i2="string",i3="string",p=1,s=1,scr=1,spm="int",sv="float",twk=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texMoveContext.html



-----------------------------------------

texMoveContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a texture editor move manip
context. Note that the above flags control the global behaviour of all texture
editor move manip contexts. Changing one context independently is not allowed.
Changing a context's behaviour using the above flags, will change all existing
texture editor move manip contexts.


-----------------------------------------


Return Value:

string  (the name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

epm   : editPivotMode   [boolean] ['query']
    Returns true when the manipulator is in edit pivot mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

p     : position        [boolean] ['query']
    Returns the current position of the manipulator

-----------------------------------------

s     : snap            [boolean] ['query', 'edit']
    Sets or queries whether snapping is to be used.

-----------------------------------------

scr   : snapComponentsRelative [boolean] ['query', 'edit']
    Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point

-----------------------------------------

spm   : snapPixelMode   [int] ['query', 'edit']
    Sets the snapping mode to be the pixel center or upper left corner.

-----------------------------------------

sv    : snapValue       [float] ['query', 'edit']
    Sets or queries the size of the snapping increment.

-----------------------------------------

twk   : tweakMode       [boolean]
    When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.

    """

def texMoveUVShellContext(q=1,e=1,ex=1,i1="string",i2="string",i3="string",it="int",m=1,p=1,sb="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texMoveUVShellContext.html



-----------------------------------------

texMoveUVShellContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a texture editor move manip
context. Note that the above flags control the global behaviour of all texture
editor move manip contexts. Changing one context independently is not allowed.
Changing a context's behaviour using the above flags, will change all existing
texture editor move manip contexts.


-----------------------------------------


Return Value:

string  (the name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

it    : iterations      [int] ['query', 'edit']
    Sets or queries the number of iterations to perform.

-----------------------------------------

m     : mask            [boolean] ['query', 'edit']
    Sets or queries masking on the shell.

-----------------------------------------

p     : position        [boolean] ['query']
    Returns the current position of the manipulator

-----------------------------------------

sb    : shellBorder     [float]
    Sets or queries the size of the shell border.

    """

def texRotateContext(q=1,e=1,epm=1,ex=1,i1="string",i2="string",i3="string",p=1,s=1,sr=1,sv="float",twk=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texRotateContext.html



-----------------------------------------

texRotateContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a rotate context for the UV
Editor. Note that the above flag controls the global behaviour of all texture
editor rotate contexts. Changing one context independently is not allowed.
Changing a context's behaviour using the above flag, will change all existing
texture editor rotate contexts.


-----------------------------------------


Return Value:

string  : name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

epm   : editPivotMode   [boolean] ['query']
    Returns true when the manipulator is in edit pivot mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

p     : position        [boolean] ['query']
    Returns the current position of the manipulator.

-----------------------------------------

s     : snap            [boolean] ['query', 'edit']
    Sets or queries whether snapping is to be used.

-----------------------------------------

sr    : snapRelative    [boolean] ['query', 'edit']
    Sets or queries whether snapping is relative.

-----------------------------------------

sv    : snapValue       [float] ['query', 'edit']
    Sets or queries the size of the snapping increment.

-----------------------------------------

twk   : tweakMode       [boolean]
    When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.

    """

def texScaleContext(q=1,e=1,epm=1,ex=1,i1="string",i2="string",i3="string",p=1,pns=1,s=1,sr=1,sv="float",twk=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texScaleContext.html



-----------------------------------------

texScaleContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a scale context for the UV
Editor. Note that the above flag controls the global behaviour of all texture
editor scale contexts. Changing one context independently is not allowed.
Changing a context's behaviour using the above flag, will change all existing
texture editor scale contexts.


-----------------------------------------


Return Value:

string  : name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

epm   : editPivotMode   [boolean] ['query']
    Returns true when manipulator is in edit pivot mode.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

p     : position        [boolean] ['query']
    Returns the current position of the manipulator.

-----------------------------------------

pns   : preventNegativeScale [boolean] ['query', 'edit']
    Prevent negative scale for components.

-----------------------------------------

s     : snap            [boolean] ['query', 'edit']
    Sets or queries whether snapping is to be used.

-----------------------------------------

sr    : snapRelative    [boolean] ['query', 'edit']
    Sets or queries whether snapping is relative.

-----------------------------------------

sv    : snapValue       [float] ['query', 'edit']
    Sets or queries the size of the snapping increment.

-----------------------------------------

twk   : tweakMode       [boolean]
    When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.

    """

def texSculptCacheContext(q=1,e=1,asz=1,ast=1,d="int",ft="int",fp="float",gtw=1,inv=1,m="string",sfc="string",sbr=1,sz="float",st="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texSculptCacheContext.html



-----------------------------------------

texSculptCacheContext is undoable, queryable, and editable.

This is a tool context command for uv cache sculpting tool.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

asz   : adjustSize      [boolean] ['edit']
    If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.

-----------------------------------------

ast   : adjustStrength  [boolean] ['edit']
    If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    Specifies how the brush determines where the uvs go.

-----------------------------------------

ft    : falloffType     [int] ['query', 'edit']
    Specifies how the brush determines which uvs to affect.

-----------------------------------------

fp    : floodPin        [float] ['edit']
    Sets the pin value for each UV to the given value

-----------------------------------------

gtw   : grabTwist       [boolean] ['query', 'edit']
    If true, the grab brush twists the UVs

-----------------------------------------

inv   : inverted        [boolean] ['query', 'edit']
    If true, inverts the effect of the brush.

-----------------------------------------

m     : mode            [string] ['query', 'edit']
    Specifies the type of sculpting effect the brush will perform.

-----------------------------------------

sfc   : sculptFalloffCurve [string] ['query', 'edit']
    Specifies the falloff curve that affects the brush.

-----------------------------------------

sbr   : showBrushRingDuringStroke [boolean] ['query', 'edit']
    Specifies whether or not to show the brush ring during stroke.

-----------------------------------------

sz    : size            [float] ['query', 'edit']
    Specifies the world-space size of the current brush.

-----------------------------------------

st    : strength        [float]
    Specifies the world-space strength of the current brush.

    """

def texSelectContext(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texSelectContext.html



-----------------------------------------

texSelectContext is undoable, queryable, and editable.

Command used to register the texSelectCtx tool.


-----------------------------------------


Return Value:

string  : name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def texSelectShortestPathCtx(q=1,e=1,ex=1,i1="string",i2="string",i3="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texSelectShortestPathCtx.html



-----------------------------------------

texSelectShortestPathCtx is undoable, queryable, and editable.

Creates a new context to select shortest edge path between two vertices or UVs
in the texture editor window.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons representing the tool associated with the context.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons representing the tool associated with the context.

-----------------------------------------

i3    : image3          [string]
    Third of three possible icons representing the tool associated with the context.

    """

def texSmudgeUVContext(q=1,e=1,ds="string",et="string",ex=1,ft="string",ch=1,i1="string",i2="string",i3="string",n="string",prs="float",r="float",sim=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texSmudgeUVContext.html



-----------------------------------------

texSmudgeUVContext is undoable, queryable, and editable.

This command creates a context for smudge UV tool. This context only works in
the texture UV editor.


-----------------------------------------


Return Value:

string  Name of the effect type created.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ds    : dragSlider      [string] ['query', 'edit']
    radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.

-----------------------------------------

et    : effectType      [string] ['query', 'edit']
    fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

ft    : functionType    [string] ['query', 'edit']
    exponential | linear | constant. Specifies how UVs fall off from the center of influence.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

prs   : pressure        [float] ['query', 'edit']
    Pressure value when effect type is set to smudge.

-----------------------------------------

r     : radius          [float] ['query', 'edit']
    Radius of the smudge tool. All UVs within this radius are affected by the tool

-----------------------------------------

sim   : smudgeIsMiddle  [boolean]
    By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.

    """

def texturePlacementContext(q=1,e=1,ex=1,ch=1,i1="string",i2="string",i3="string",lm=1,n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texturePlacementContext.html



-----------------------------------------

texturePlacementContext is undoable, queryable, and editable.

Create a command for creating new texture placement contexts. By default label
mapping is on when the context is created.


-----------------------------------------


Return Value:

string  The name of the context created    
  
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

lm    : labelMapping    [boolean] ['query', 'edit']
    Set the context to label mapping.

-----------------------------------------

n     : name            [string]
    If this is a tool command, name the tool appropriately.

    """

def texTweakUVContext(q=1,e=1,ex=1,i1="string",i2="string",i3="string",p=1,t="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texTweakUVContext.html



-----------------------------------------

texTweakUVContext is undoable, queryable, and editable.

This command can be used to create, edit, or query a texture editor move manip
context. Note that the above flags control the global behaviour of all texture
editor move manip contexts. Changing one context independently is not allowed.
Changing a context's behaviour using the above flags, will change all existing
texture editor move manip contexts.


-----------------------------------------


Return Value:

string  (the name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

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

p     : position        [boolean] ['query']
    Returns the current position of the manipulator

-----------------------------------------

t     : tolerance       [float]
    Controls the initial selection snapping tolerance.

    """

def texWinToolCtx(q=1,e=1,ac=1,bz=1,do=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",tn="string",tr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/texWinToolCtx.html



-----------------------------------------

texWinToolCtx is undoable, queryable, and editable.

This class creates a context for the View Tools "track", "dolly", and "box
zoom" in the texture window.


-----------------------------------------


Return Value:

string  Context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

-----------------------------------------

bz    : boxzoom         [boolean] ['query', 'edit']
    Perform Box Zoom

-----------------------------------------

do    : dolly           [boolean] ['query', 'edit']
    Dollies the view

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

tn    : toolName        [string] ['query']
    Name of the specific tool to which this command refers.

-----------------------------------------

tr    : track           [boolean]
    Tracks the view

    """

def threePointArcCtx(q=1,e=1,d="uint",ex=1,ch=1,i1="string",i2="string",i3="string",n="string",s="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/threePointArcCtx.html



-----------------------------------------

threePointArcCtx is undoable, queryable, and editable.

The threePointArcCtx command creates a new context for creating 3 point arcs


-----------------------------------------


Return Value:

string  (name of the new context)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : degree          [uint] ['query', 'edit']
    VAlid values are 1 or 3. Default degree 3.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

s     : spans           [uint]
    Default is 8.

    """

def toolDropped():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/toolDropped.html



-----------------------------------------

toolDropped is undoable, NOT queryable, and NOT editable.

This command builds and executes the commands necessary to recreate the
specified tool button. It is invoked when a tool is dropped on the shelf.


-----------------------------------------


Return Value:

None
    """

def toolHasOptions():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/toolHasOptions.html



-----------------------------------------

toolHasOptions is undoable, NOT queryable, and NOT editable.

This command queries a tool to see if it has options. If it does, it returns
true. Otherwise it returns false.


-----------------------------------------


Return Value:

boolean  True if the queried tool has options, otherwise false.
    """

def toolPropertyWindow(q=1,e=1,fld="string",hb="string",icn="string",imw=1,loc="string",nm=1,rb="string",rs=1,sel="string",shw="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/toolPropertyWindow.html



-----------------------------------------

toolPropertyWindow is undoable, queryable, and editable.

End users should only call this command as 1. a query (in the custom tool
property sheet code) or 2. with no arguments to create the default tool
property sheet. The more complex uses of it are internal.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

fld   : field           [string] ['query', 'edit']
    Sets/returns the name of the text field used to store the tool name in the property sheet.

-----------------------------------------

hb    : helpButton      [string] ['query', 'edit']
    Sets/returns the name of the button used to show help on the tool in the property sheet.

-----------------------------------------

icn   : icon            [string] ['query', 'edit']
    Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).

-----------------------------------------

imw   : inMainWindow    [boolean] []
    Specify true if you want the tool settings to appear in the main window rather than a separate window.

-----------------------------------------

loc   : location        [string] ['query', 'edit']
    Sets/returns the location of the current tool property sheet, or an empty string if there is none.

-----------------------------------------

nm    : noviceMode      [boolean] ['query', 'edit']
    Sets/returns the 'novice mode' flag.(unused at the moment)

-----------------------------------------

rb    : resetButton     [string] ['query', 'edit']
    Sets/returns the name of the button used to restore the tool settings in the property sheet.

-----------------------------------------

rs    : restore         [boolean] []
    Reopens the tool settings window. This flag can be used with the flag inMainWindow for the fall back location if the tool settings can't be restored.

-----------------------------------------

sel   : selectCommand   [string] ['query', 'edit']
    Sets/returns the property sheet's select command.

-----------------------------------------

shw   : showCommand     [string]
    Sets/returns the property sheet's display command.

    """

def trackCtx(q=1,e=1,ac=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",tn="string",tg=1,ts="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/trackCtx.html



-----------------------------------------

trackCtx is undoable, queryable, and editable.

This command can be used to create a track context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

tn    : toolName        [string] ['query']
    Name of the specific tool to which this command refers.

-----------------------------------------

tg    : trackGeometry   [boolean] ['query', 'edit']
    Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.

-----------------------------------------

ts    : trackScale      [float]
    Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.

    """

def tumbleCtx(q=1,e=1,ac=1,aoc=1,asp=1,ex=1,ch=1,i1="string",i2="string",i3="string",lt="int",n="string",ot=1,ol=1,os="angle",tn="string",ts="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/tumbleCtx.html



-----------------------------------------

tumbleCtx is undoable, queryable, and editable.

This command can be used to create, edit, or query a tumble context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

-----------------------------------------

aoc   : autoOrthoConstrain [boolean] ['query', 'edit']
    Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.

-----------------------------------------

asp   : autoSetPivot    [boolean] ['query', 'edit']
    Automatically set the camera pivot to the selection or tool effect region

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

lt    : localTumble     [int] ['query', 'edit']
    Describes what point the camera will tumble around:    * 0 for the camera's tumble pivot   * 1 for the camera's center of interest   * 2 for the camera's local axis, offset by its tumble pivot

-----------------------------------------

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

ot    : objectTumble    [boolean] ['query', 'edit']
    Make the camera tumble around the selected object, if true.

-----------------------------------------

ol    : orthoLock       [boolean] ['query', 'edit']
    Orthographic cameras cannot be tumbled while orthoLock is on.

-----------------------------------------

os    : orthoStep       [angle] ['query', 'edit']
    Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.

-----------------------------------------

tn    : toolName        [string] ['query']
    Name of the specific tool to which this command refers.

-----------------------------------------

ts    : tumbleScale     [float]
    Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.

    """

def twoPointArcCtx(q=1,e=1,d="uint",ex=1,ch=1,i1="string",i2="string",i3="string",n="string",s="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/twoPointArcCtx.html



-----------------------------------------

twoPointArcCtx is undoable, queryable, and editable.

The twoPointArcCtx command creates a new context for creating two point
circular arcs


-----------------------------------------


Return Value:

string  Name of the new context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : degree          [uint] ['query', 'edit']
    Valid values are 1 or 3. Default degree 3.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

s     : spans           [uint]
    Default is 4.

    """

def view2dToolCtx(q=1,e=1,ac=1,bz=1,do=1,ex=1,ch=1,i1="string",i2="string",i3="string",n="string",tn="string",tr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/view2dToolCtx.html



-----------------------------------------

view2dToolCtx is undoable, queryable, and editable.

This class creates a context for the View Tools "track", "dolly", and "box
zoom" in the Hypergraph.


-----------------------------------------


Return Value:

string  The context name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

-----------------------------------------

bz    : boxzoom         [boolean] ['query']
    Perform Box Zoom

-----------------------------------------

do    : dolly           [boolean] ['query']
    Dollies the view

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

tn    : toolName        [string] ['query']
    Name of the specific tool to which this command refers.

-----------------------------------------

tr    : track           [boolean]
    Tracks the view

    """

def walkCtx(q=1,e=1,ac=1,wcc="float",ex=1,ch=1,i1="string",i2="string",i3="string",n="string",tn="string",wh="float",wsv="float",ws="float",wth=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/walkCtx.html



-----------------------------------------

walkCtx is undoable, queryable, and editable.

This command can be used to create, edit, or query a walk context.


-----------------------------------------


Return Value:

string  The name of the context    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : alternateContext [boolean] ['query']
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

-----------------------------------------

wcc   : crouchCount     [float] ['query', 'edit']
    The camera crouch count.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

tn    : toolName        [string] ['query']
    Name of the specific tool to which this command refers.

-----------------------------------------

wh    : walkHeight      [float] ['query', 'edit']
    The camera initial height.

-----------------------------------------

wsv   : walkSensitivity [float] ['query', 'edit']
    The camera rotate sensitivity.

-----------------------------------------

ws    : walkSpeed       [float] ['query', 'edit']
    The camera move speed.

-----------------------------------------

wth   : walkToolHud     [boolean]
    Control whether show walk tool HUD.

    """

def wireContext(q=1,e=1,ce="linear",do="string",dds="linear",en="linear",exc=1,ep="string",ex=1,gw=1,ch=1,ho=1,i1="string",i2="string",i3="string",li="linear",n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/wireContext.html



-----------------------------------------

wireContext is undoable, queryable, and editable.

This command creates a tool that can be used to create a wire deformer.


-----------------------------------------


Return Value:

string  The name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ce    : crossingEffect  [linear] ['query', 'edit']
    Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.

-----------------------------------------

do    : deformationOrder [string] ['query', 'edit']
    Set the appropriate flag that determines the position in in the deformation hierarchy.

-----------------------------------------

dds   : dropoffDistance [linear] ['query', 'edit']
    Set the dropoff Distance for the wires.

-----------------------------------------

en    : envelope        [linear] ['query', 'edit']
    Set the envelope value for the deformer. Default is 1.0

-----------------------------------------

exc   : exclusive       [boolean] ['query', 'edit']
    Set exclusive mode on or off.

-----------------------------------------

ep    : exclusivePartition [string] ['query', 'edit']
    Set the name of an exclusive partition.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

gw    : groupWithBase   [boolean] ['query', 'edit']
    Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.

-----------------------------------------

ch    : history         [boolean] []
    If this is a tool command, turn the construction history on for the tool in question.

-----------------------------------------

ho    : holder          [boolean] ['edit']
    Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.

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

li    : localInfluence  [linear] ['query', 'edit']
    Set the amount of local influence a wire has with respect to other wires. Default is 0.

-----------------------------------------

n     : name            [string]
    If this is a tool command, name the tool appropriately.

    """

def wrinkleContext(q=1,e=1,brc="uint",bd="uint",ex=1,ch=1,i1="string",i2="string",i3="string",n="string",rnd="linear",st="string",th="linear",wc="uint",wi="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/wrinkleContext.html



-----------------------------------------

wrinkleContext is undoable, queryable, and editable.

This command creates a context that creates wrinkles.


-----------------------------------------


Return Value:

string  The name of the context created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

brc   : branchCount     [uint] ['query', 'edit']
    Set the number of branches spawned from a crease for radial wrinkles. Default is 2.

-----------------------------------------

bd    : branchDepth     [uint] ['query', 'edit']
    Set the depth of branching for radial wrinkles. Defaults to 0.

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

n     : name            [string] []
    If this is a tool command, name the tool appropriately.

-----------------------------------------

rnd   : randomness      [linear] ['query', 'edit']
    Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.

-----------------------------------------

st    : style           [string] ['query', 'edit']
    Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".

-----------------------------------------

th    : thickness       [linear] ['query', 'edit']
    Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.

-----------------------------------------

wc    : wrinkleCount    [uint] ['query', 'edit']
    Set the number of wrinkle creases. Default is 3.

-----------------------------------------

wi    : wrinkleIntensity [linear]
    Set the depth intensity of the wrinkle furrows. Defaults to 0.5.

    """

