def attrCompatibility(a=1,clr=1,dmp=1,enable=1,nr="string",pn="string",rm=1,r="string",typ="string",v="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/attrCompatibility.html



-----------------------------------------

attrCompatibility is undoable, NOT queryable, and NOT editable.

This command is used by Maya to handle compatibility issues between file
format versions by providing a mechanism to describe differences between two
versions. Plug-in writers can make use of this command to handle attribute
compatibility changes to files.

The first optional command argument argument is a node type name and the
second optional command argument is the short name of an attribute.

Warning: Only use this command to describe changes in names or attributes of
nodes that you have written as plugins. Do not use this command to change
information about builtin dependency graph nodes. Removing attributes on a
plug-in node is a special case. Use a separate attrCompatibility call with
pluginNode flag and name so that these attributes can be tracked even though
the plug-in may not be loaded.

Only one flag may be used per invocation of the command. If multiple flags are
provided one will arbitrarily be chosen as the action to perform and the
others will be silently ignored.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : addAttr         [boolean] []
    Add the given attribute to the named node.

-----------------------------------------

clr   : clear           [boolean] []
    Clear out the compatibility table. This is only used internally for debugging purposes.

-----------------------------------------

dmp   : dumpTable       [boolean] []
    Dump the current contents of the compatibility table. This is only used internally for debugging purposes.

-----------------------------------------

e     : enable          [boolean] []
    Enable or disable the compatibility table. This is only used internally for debugging purposes.

-----------------------------------------

nr    : nodeRename      [string] []
    Replace all uses of the node type 'nodeName' with given string.

-----------------------------------------

pn    : pluginNode      [string] []
    Registers the string argument as a plug-in node type. This is necessary for subsequent attrCompatibility calls that reference node attributes of unloaded plug-ins. Specifically, this works in the case when attributes are being removed.

-----------------------------------------

rm    : removeAttr      [boolean] []
    Remove the given attribute from the named node.

-----------------------------------------

r     : renameAttr      [string] []
    Change the short name of the attribute specified in the command's arguments to the new short name provided as a parameter to this flag. Once the mapping between short names has been established, Maya will handle the long names automatically.

-----------------------------------------

typ   : type            [string] []
    Change the type of the given attribute to the given type.

-----------------------------------------

v     : version         [string]
    Set the version target for subsequent commands to the given string.

    """

def autoSave(q=1,dst="int",df=1,en=1,fol="string",int="float",lim=1,max="int",p=1,prm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/autoSave.html



-----------------------------------------

autoSave is undoable, queryable, and NOT editable.

Provides an interface to the auto-save mechanism.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dst   : destination     [int] ['query']
    Sets the option for where auto-save files go. 0 - auto-saves go into the workspace autosave folder 1 - auto-saves go into the named folder (set with the -folder flag) 2 - auto-saves go into a folder set by an environment variable (MAYA_AUTOSAVE_FOLDER)

-----------------------------------------

df    : destinationFolder [boolean] ['query']
    Queries the actual destination folder for auto-saves, based on the current setting of the -destination flag, workspace rules and environment variables. Resolves environment variables etc. and makes any relative path absolute (resolved relative to the workspace root). The returned string will end with a trailing separator ('/').

-----------------------------------------

en    : enable          [boolean] ['query']
    Enables or disables auto-saves.

-----------------------------------------

fol   : folder          [string] ['query']
    Sets the folder for auto-saves used if the destination option is 1.

-----------------------------------------

int   : interval        [float] ['query']
    Sets the interval between auto-saves (in seconds). The default interval is 600 seconds (10 minutes).

-----------------------------------------

lim   : limitBackups    [boolean] ['query']
    Sets whether the number of auto-save files is limited.

-----------------------------------------

max   : maxBackups      [int] ['query']
    Sets the maximum number of auto-save files, if limiting is in effect.

-----------------------------------------

p     : perform         [boolean] []
    Invokes the auto-save process.

-----------------------------------------

prm   : prompt          [boolean]
    Sets whether the auto-save prompts the user before auto-saving.

    """

def cmdFileOutput(q=1,c="uint",ca=1,o="string",s="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cmdFileOutput.html



-----------------------------------------

cmdFileOutput is undoable, queryable, and NOT editable.

This command will open a text file to receive all of the commands and results
that normally get printed to the Script Editor window or console. The file
will stay open until an explicit -close with the correct file descriptor or a
-closeAll, so care should be taken not to leave a file open.

To enable logging to commence as soon as Maya starts up, the environment
variable MAYA_CMD_FILE_OUTPUT may be specified prior to launching Maya.
Setting MAYA_CMD_FILE_OUTPUT to a filename will create and output to that
given file. To access the descriptor after Maya has started, use the -query
and -open flags together.


-----------------------------------------


Return Value:

int  : On open, returns a value (descriptor) that can be used to query the
status or close the file. Otherwise, a status code indicating status of file    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : close           [uint] []
    Closes the file corresponding to the given descriptor. If -3 is returned, the file did not exist. -1 is returned on error, 0 is returned on successful close.

-----------------------------------------

ca    : closeAll        [boolean] []
    Closes all open files.

-----------------------------------------

o     : open            [string] ['query']
    Opens the given file for writing (will overwrite if it exists and is writable). If successful, a value is returned to enable status queries and file close. -1 is returned if the file cannot be opened for writing. The -open flag can also be specified in -query mode. In query mode, if the named file is currently opened, the descriptor for the specified file is returned, otherwise -1 is returned. This is an easy way to check if a given file is currently open.  In query mode, this flag needs a value.

-----------------------------------------

s     : status          [uint]
    Queries the status of the given descriptor. -3 is returned if no such file exists, -2 indicates the file is not open, -1 indicates an error condition, 0 indicates file is ready for writing.

    """

def dirmap(q=1,cd="string",en=1,gam=1,gmd="string",m="[string, string]",um="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dirmap.html



-----------------------------------------

dirmap is undoable, queryable, and NOT editable.

Use this command to map a directory to another directory. The first argument
is the directory to map, and the second is the destination directory to map
to.

Directories must both be absolute paths, and should be separated with forward
slashes ('/'). The mapping is case-sensitive on all platforms. This command
can be useful when moving projects to another machine where some textures may
not be contained in the Maya project, or when a texture archive moves to a new
location. This command is not necessary when moving a (self-contained) project
from one machine to another - instead copy the entire project over and set the
Maya project to the new location.

For one-time directory moves, if the command is enabled and the mapping
configured correctly, when a scene is opened and saved the mapped locations
will be reflected in the filenames saved with the file. To set up a permanent
mapping the command should be enabled and the mappings set up in a script
which is executed every time you launch Maya (userSetup.mel is sourced on
startup). The directory mappings and enabled state are not preserved between
Maya sessions. This command requires one "main" flag that specifies the action
to take. Flags are:

-[m|um|gmd|gam|cd|en]


-----------------------------------------


Return Value:

string  when convertDirectory is used    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cd    : convertDirectory [string] []
    Convert a file or directory. Returns the name of the mapped file or directory, if the command is enabled. If the given string contains one of the mapped directories, the return value will have that substring replaced with the mapped one. Otherwise the given argument string will be returned. If the command is disabled the given argument is always returned. Checks are not made for whether the file or directory exists. If the given string is a directory it should have a trailing '/'.

-----------------------------------------

en    : enable          [boolean] ['query']
    Enable directory mapping. Directory mapping is off when you start Maya. If enabled, when opening Maya scenes, file texture paths (and other file paths) will be converted when the scene is opened. The -cd flag only returns mapped directories when -enable is true. Query returns whether mapping has been enabled.

-----------------------------------------

gam   : getAllMappings  [boolean] []
    Get all current mappings. Returns string array of current mappings in format: [redirect1, replacement1, ... redirectN, replacementN]

-----------------------------------------

gmd   : getMappedDirectory [string] []
    Get the mapped redirected directory. The given argument must exactly match the first string used with the -mapDirectory flag.

-----------------------------------------

m     : mapDirectory    [[string, string]] []
    Map a directory - the first argument is mapped to the second. Neither directory needs to exist on the local machine at the time of invocation.

-----------------------------------------

um    : unmapDirectory  [string]
    Unmap a directory. The given argument must exactly match the argument used with the -mapDirectory flag.

    """

def exportEdits(q=1,ehr=1,en="string",exs=1,f=1,ian=1,ic=1,idf=1,inw=1,includeNode="string",isa=1,sdk=1,ish=1,sel=1,typ="string",ec="string",orn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/exportEdits.html



-----------------------------------------

exportEdits is NOT undoable, queryable, and NOT editable.

Use this command to export edits made in the scene to a file. The exported
file can be subsequently imported to another scene. Edits may include: nodes,
connections and reference edits such as value changes. The nodes that are
included in the exported file will be based on the options used. At least one
option flag that describes the set of target nodes to include in the exported
file must be specified (e.g. 'selected', 'onReferenceNode'). Use the inclusion
flags ('includeAnimation', 'includeShaders', 'includeNetwork') to specify
which additional related nodes will be added to the export list. In export
mode, when the command completes successfully, the name of the exported file
will be returned. In query mode, this command will return information about
the contents of the exported file. The query mode will return the list of
nodes that will be considered for inclusion in the exported file based on the
specified flags.


-----------------------------------------


Return Value:

string[]  For query execution.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ehr   : excludeHierarchy [boolean] ['query']
    By default, all DAG parents and DAG history are written to the export file. To prevent any DAG relations not otherwise connected to the target nodes to be included, specify the -excludeHierarchy flag.

-----------------------------------------

en    : excludeNode     [string] ['query']
    Prevent the node from being included in the list of nodes being exported. This flag is useful to exclude specific scene nodes that might otherwise be exported. In the case where more than one Maya node has the same name, the DAG path can be specified to uniquely identify the node.

-----------------------------------------

exs   : exportSelected  [boolean] ['query']
    The selected nodes and their connections to each other will be exported. Additionally, any dangling connections to non-exported nodes will be exported. Default nodes are ignored and never exported. Note that when using the exportSelected flag, only selected nodes are exported, and -include/-exclude flags such as -includeHierarchy are ignored.

-----------------------------------------

f     : force           [boolean] ['query']
    Force the export action to take place. This flag is required to overwrite an existing file.

-----------------------------------------

ian   : includeAnimation [boolean] ['query']
    Additionally include animation nodes and animation helper nodes associated with the target nodes being exported.

-----------------------------------------

ic    : includeConstraints [boolean] ['query']
    Additionally include constraint-related nodes associated with the target nodes being exported.

-----------------------------------------

idf   : includeDeformers [boolean] ['query']
    Additionally include deformer networks associated with the target nodes being exported.

-----------------------------------------

inw   : includeNetwork  [boolean] ['query']
    Additionally include the network of nodes connected to the target nodes being exported.

-----------------------------------------

includeNode : includeNode     [string] ['query']
    Additionally include the named node in the list of nodes being exported. In the case where more than one Maya node has the same name, the DAG path can be specified to uniquely identify the node.

-----------------------------------------

isa   : includeSetAttrs [boolean] ['query']
    When using the -selected/-sel flag, if any of the selected nodes are referenced, also include/exclude any setAttr edits on those nodes. If used with the -onReferenceNode/-orn flag, include/exclude any setAttr edits on the reference.

-----------------------------------------

sdk   : includeSetDrivenKeys [boolean] ['query']
    Additionally include setDrivenKey-related nodes associated with the target nodes being exported.

-----------------------------------------

ish   : includeShaders  [boolean] ['query']
    Additionally include shaders associated with the target nodes being exported.

-----------------------------------------

sel   : selected        [boolean] ['query']
    Export will operate on the list of nodes currently selected. This flag differs from the exportSelected flag in that the selected nodes are not exported, only the edits on them, and any nodes found via the include flags that are used (such as includeAnimation, includeNetwork and so on).

-----------------------------------------

typ   : type            [string] ['query']
    Set the type of the exported file. Valid values are "editMA" or "editMB". Note that this command respects the global "defaultExtensions" setting for file naming that is controlled with the file command defaultExtensions option. See the file command for more information.

-----------------------------------------

ec    : editCommand     [string] ['query']
    This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be included. This flag requires a string parameter. Valid values are: "addAttr", "connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr", "lock" and "unlock". In some contexts, this flag may be specified more than once to specify multiple edit types to consider.

-----------------------------------------

orn   : onReferenceNode [string]
    This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports multiple uses when specified with the "exportEdits" command.

    """

def file(q=1,e=1,an=1,a=1,ap=1,add=1,amf=1,at="string",bls=1,chn=1,cr="string",c="[string, string]",cmp=1,con=1,ch=1,cnl=1,de=1,dns=1,dr=1,ec="string",err=1,esn=1,ex=1,exn=1,ea=1,ean=1,ear=1,er=1,exs=1,es=1,eas=1,esa=1,esr=1,ess=1,esc="[script, string]",eur=1,exp=1,fmd=1,fr="string",f=1,gl=1,gn="string",gr=1,iv=1,i=1,ifr=1,ir=1,itr="string",lfo=1,ltf=1,l=1,lad=1,lar=1,lnr=1,lr="string",lrd="string",lrp="string",ls="string",loc=1,lcu=1,lf=1,lck=1,mns="[string, string]",mnp=1,mnr=1,mnc=1,mf=1,ms=1,ns="string",new=1,o=1,op="string",pns=1,pos="string",prs="string",pn=1,pr=1,pv=1,pmt=1,pm="string",pt="string",r=1,rdi="uint",rfn="string",rns="string",rdn=1,rr=1,rn="string",ra=1,rts=1,rpr="string",rpl=1,rep="[string, string]",rer=1,rnn=1,s=1,sdc="string",sr=1,sru=1,stx="string",sn=1,seg="string",sa=1,sh=1,shd="string",srf=1,shn=1,str=1,sns="[string, string]",typ="string",uc=1,ur="string",un=1,uns=1,wcn=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/file.html



-----------------------------------------

file is undoable, queryable, and editable.

#### Opening, importing, exporting, referencing, saving, or renaming a file

This command needs a single main flag that specifies the action to take. Some
of the main flags also take optional secondary flags to modify that action.

The main flags are: cr | ea | ean | ear | eas | er | esa | es  
---|---|---|---|---|---|---|---  
esn | ex | fr | i | ir | l | lr | lrp  
loc | ltf | mf | new | o | op | ot | pmt  
r | rdi | rn | rr | rts | s | sa | sdx  
st | stx | typ | uc | ur | w  
  
o/open can be modified by the following secondary flags: f | lad | lad | lnr |
rnn  
---|---|---|---|---  
  
es/exportSelected can be modified by the following secondary flags: ch | chn |
con | exp | sh  
---|---|---|---|---  
  
r/reference can be modified by the following secondary flags: dns | dr | gr |
gl | gn | mnc | ns | rfn | rpr | sns | srf | shd | rnn  
---|---|---|---|---|---|---|---|---|---|---|---|---  
  
i/import can be modified by the following secondary flags: dns | dr | gr | gn
| mnc | pr | ra | rdn | rnn | rpr | sns  
---|---|---|---|---|---|---|---|---|---|---  
  
n/new and s/save can be modified by the following secondary flags: f  
---  
  
er/exportAsReference can be modified by the following secondary flags: ns |
rpr  
---|---  
  
ea/exportAll and es/exportSelected can be modified by the following secondary
flags: f | pr  
---|---  
  
ean/exportAnim, eas/exportSelectedAnim can be modified by the following
secondary flags: f  
---  
  
ear/exportAnimFromReference, esa/exportSelectedAnimFromReference can be
modified by the following secondary flags: f | rfn  
---|---  
  
#### Querying information about a file

This command needs a single main query flag that specifies the query to take
and then optional secondary flags to modify that query.

The main query flags are: amf | ch | chn | con | dr | err | ex | exn  
---|---|---|---|---|---|---|---  
exp | l | loc | ltf | mf | ns | op | ot  
pmt | pns | r | rfn | rpl | rpr | rts | sdc  
sh | sn | stx | typ | uc | w  
  
dr/deferReference can be modified by the following secondary flags: rfn  
---  
  
exn/expandName, l/list, r/reference, sn/sceneName can be modified by the
following secondary flags: un | shn | wcn  
---|---|---  
  
#### Querying file names

When querying a file name there are a number of ways to format the result:

##### Resolved vs. unresolved name:

When a file is loaded into Maya (e.g., by opening or referencing it), the file
path provided may not be complete. It could, for example, be a relative path
(ex: "scenes/myScene.ma"), it could contain environment variables (ex:
"$PRODUCTION_DIR/myScene.ma"), and it could even be a path which simply
doesn't exist on the local disk. In each of these cases Maya goes through a
number of steps to resolve the path and find the file on disk. By default the
'file' command will return the resolved file name (i.e., the location from
which Maya is actually reading the file), but if the un/unresolved flag is
used, the unresolved file (e.g., the one that was originally specified) will
be returned. When providing a file path with an environment variable; for
example, when using the -rename flag, the environment variable should be set
to a relative path ( such as "/scenes/scenesSetA"; ). Providing a path using
an environment variable that is set to an absolute path ( for example,
"C:/scenes/" ) is not supported.

##### Full vs. short name:

By default the 'file' command will return the full path to a file, but if the
shn/shortName flag is used just the file name will be returned.

##### With vs. without copy number:

When the same file is loaded into Maya more than once (for example by
referencing the same file twice), Maya distinguishes between the various
copies by appending a copy number to the end of the file name. The first time
the file is loaded, no copy number is appended. The second time the file is
loaded a "{1}" is appended, the third time a "{2}" is used, and so on. By
default the 'file' command will return the file name with the copy number
appended, but if the wcn/withoutCopyNumber flag is used the file name will be
returned without the copy number.

#### Additional Details

  * The file command usually expects a file name as its argument, if none is specified then the root scene is used.
  * See the individual flag descriptions for details and limitations.


-----------------------------------------


Return Value:

string  The name of the specified file for most actions. When the
returnNewNodes flag is used, an array of strings will be returned indicating
the names of the nodes that were read.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

an    : absoluteName    [boolean] ['query']
    This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces. For example ":ns:ball" is an absolute namespace name while "ns:ball" is not.

-----------------------------------------

a     : activate        [boolean] []
    This flag is obsolete.

-----------------------------------------

ap    : activeProxy     [boolean] []
    This flag is intended for internal use by Maya during file referencing. It specifes which file is the active proxy when the file is loaded when used with the reference flag. It is also used to specify which file is the active proxy in the file referencing preload information when used with the referenceDepthInfo flag.

-----------------------------------------

add   : add             [boolean] []
    When used with selectAll it indicates that the specified items should be added to the active list without removing existing items from the active list.

-----------------------------------------

amf   : anyModified     [boolean] ['query']
    This flag is obsolete. Please use file -q -modified instead.

-----------------------------------------

at    : applyTo         [string] []
    When importing or referencing an offline edit file, apply it to to the given reference (i.e., determine what <main> gets mapped to). Specify the reference node name as argument. To apply the edits to nodes in the main scene (i.e., the root namespace), pass in ":". To collapse <main> (i.e., map it to "None"), pass in "". May only be used with the file -i/import or -r/reference flags.

-----------------------------------------

bls   : buildLoadSettings [boolean] []
    When used with the "o/open" flag it indicates that the specified file should be read for reference hierarchy information only. This information will be stored in temporary load settings under the name "implicitLoadSettings". When this flag is used the specified scene file will not be loaded: no objects/nodes will be created or modified. Note: most users will not need to use this flag or the "implicitLoadSettings" it builds. They can access the same functionality by setting the "Selective Load" option in the File > Open Option Box.

-----------------------------------------

chn   : channels        [boolean] ['query']
    For use with exportSelected to specify whether attached channels should be included in the export.

-----------------------------------------

cr    : cleanReference  [string] []
    Remove edits from the passed in reference node. The reference must be in an unloaded state. To remove a particular type of edit, use the editCommand flag. If no flag is specified, all edits will be removed.

-----------------------------------------

c     : command         [[string, string]] ['query']
    Specifies the callback to execute before any file operation. This is an internal flag used only in the file format.

-----------------------------------------

cmp   : compress        [boolean] []
    When used with save, it will compress (gzip) the file on output.

-----------------------------------------

con   : constraints     [boolean] ['query']
    For use with exportSelected to specify whether attached constraints should be included in the export.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    For use with exportSelected to specify whether attached construction history should be included in the export.

-----------------------------------------

cnl   : copyNumberList  [boolean] ['query']
    When queried, this flag returns a string array containing a number that uniquely identifies each instance the file is used.

-----------------------------------------

de    : defaultExtensions [boolean] ['query']
    Use the default extensions to rename the files. This defaults to true, but is a persistent setting within a given session of Maya, meaning that if you set it to true or false, that value will continue to be used in subsequent file commands until a new value is set.

-----------------------------------------

dns   : defaultNamespace [boolean] []
    Use the default name space for import and referencing. This is an advanced option. If set, then on import or reference, Maya will attempt to place all nodes from the imported or referenced file directly into the root (default) name space, without invoking any name clash resolution algorithms. If the names of any of the new objects already exist in the root namespace, then errors will result. The user of this flag is responsible for creating a name clash resolution mechanism outside of Maya to avoid such errors. Note: This flag is intended only for use with custom file translators written through the API. Use at your own risk.

-----------------------------------------

dr    : deferReference  [boolean] ['query']
    When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is deferred.   C: The default is false.   Q: When queried, this flag returns true if the reference is deferred, or false if the reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.

-----------------------------------------

ec    : editCommand     [string] []
    For use with cleanReference. Remove only this type of edit. Supported edits are: setAttr addAttr deleteAttr connectAttr disconnectAttr and parent

-----------------------------------------

err   : errorStatus     [boolean] ['query']
    Query the error status of the last file read. Returns true if and error occurred during the last file read.

-----------------------------------------

esn   : executeScriptNodes [boolean] []
    If true, allow the appropriate script nodes to execute. If false, do not allow any script node scripts to run.   For more information, see the documentation for script nodes.   Default: true.

-----------------------------------------

ex    : exists          [boolean] ['query']
    Query if the file exists. Returns true if the file exists.

-----------------------------------------

exn   : expandName      [boolean] ['query']
    This is a query only flag that can be used to query for the file path name of the file.

-----------------------------------------

ea    : exportAll       [boolean] []
    Export everything into a single file. Returns the name of the exported file.

-----------------------------------------

ean   : exportAnim      [boolean] []
    Export all animation nodes and animation helper nodes from all objects in the scene. The resulting animation export file will contain connections to objects that are not included in the animation file. As a result, importing/referencing this file back in will require objects of the same name to be present, else errors will occur. The -sns/swapNamespace flag is available for swapping the namespaces of given objects to another namespace. This use of namespaces can be used to re-purpose the animation file to multiple targets using a consistent naming scheme. The exportAnim flag will not export animation layers. For generalized file export of animLayers and other types of nodes, refer to the exportEdits command. Or use the Export Layers functionality.

-----------------------------------------

ear   : exportAnimFromReference [boolean] []
    Export the main scene animation nodes and animation helper nodes from all referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the specified reference file. See -ean/exportAnim flag description for details on usage of animation files.

-----------------------------------------

er    : exportAsReference [boolean] []
    Export the selected objects into a reference file with the given name. The file is saved on disk during the process. Returns the name of the reference created.

-----------------------------------------

exs   : exportAsSegment [boolean] []
    This flag is obsolete.

-----------------------------------------

es    : exportSelected  [boolean] []
    Export the selected items into the specified file. Returns the name of the exported file.

-----------------------------------------

eas   : exportSelectedAnim [boolean] []
    Export all animation nodes and animation helper nodes from the selected objects in the scene. See -ean/exportAnim flag description for details on usage of animation files.

-----------------------------------------

esa   : exportSelectedAnimFromReference [boolean] []
    Export the main scene animation nodes and animation helper nodes from the selected referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the selected nodes of a specified reference file. See -ean/exportAnim flag description for details on usage of animation files.

-----------------------------------------

esr   : exportSelectedNoReference [boolean] []
    This flag is obsolete.

-----------------------------------------

ess   : exportSelectedStrict [boolean] []
    Export the selected items into the specified file. This flag differs from exportSelected in that it will only export the nodes that are explicitly on the selection list. Related nodes (both history and DAG related) are not automatically exported unless those nodes are also on the selection list. Node relationships are only preserved if both nodes in the relationship (parent/child, source/destination) are exported. It is important to note that there is potential for scene data loss in the exported scene since not all related nodes are not exported by default. The user is responsible for selecting all relevant nodes before exporting. Returns the name of the exported file.

-----------------------------------------

esc   : exportSnapshotCallback [[script, string]] []
    When specified alongside -ea/exportAll, es/exportSelected and -ess/exportSelectedStrict, this flag enables Maya to temporarily duplicate the export targets into a specified namespace and invoke a callback to interact with the duplicate export targets before writing the duplicate export targets to disk. Once written to disk, the duplicate export targets, new nodes created by the callback and temporary namespace are removed from the scene. Implicitly created nodes (eg. persp, top, etc.) are not duplicated. For the duration of the callback: 1\. The specified namespace will be made current. 2\. All nodes added by the callback are tracked as a temporary export target. 3\. Although the intent of the callback is to only operate on the duplicate export targets, there is nothing limiting the callback from modifying the main scene. Thus, the callback should be written with care. This flag accepts two arguments: a. [string] Callback to invoke prior to write to disk. b. [string] Temporary namespace to store duplicate export targets. This flag can only be used in conjunction with -ea/exportAll, -es/exportSelected and -ess/exportSelectedStrict. Note that the -pv/preview flag still only previews the contents of the export targets _prior_ to the snapshot duplication. It does not preview the final output after the callback. Referenced nodes are duplicated in the same manner as duplicating those nodes manually in the scene. Similarly, scene assembly nodes will duplicate as they would if manually duplicated, however scene assembly nodes have special duplication behavior, so the callback should be aware of these differences when anticipating the duplicate export targets.

-----------------------------------------

eur   : exportUnloadedReferences [boolean] []
    Only effective when preserveReferences is used. When used with the exportAll flag, tells the exporter to include all unloaded references in the export. When used with the exportSelected flag, tells the exporter to include all unloaded proxy references that are related to any node in the selection.

-----------------------------------------

exp   : expressions     [boolean] ['query']
    For use with exportSelected to specify whether attached expressions should be included in the export.

-----------------------------------------

fmd   : fileMetaData    [boolean] ['query']
    This is a query only flag to get the file metadata for audio files. It returns the referenceTime. This field is only extracted from BWAVE files, for other files it returns 0

-----------------------------------------

fr    : flushReference  [string] []
    This flag will unload the reference file associated with the passed reference node, retaining all associated reference nodes and scene files. ** This option only works when using namespaces **. More Details: This flag is primarily intended to be used as part of a custom asset management system. It can be used to defer loading of a reference which contains child references without losing information about those child references. Prior to reloading a flushed reference which contains child references, the 'createNode reference' lines should be manually removed from the children's Maya ASCII files. If this is not done, extra reference nodes will be created.

-----------------------------------------

f     : force           [boolean] []
    Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without prompting a dialog that warns user about the lost of edits.

-----------------------------------------

gl    : groupLocator    [boolean] []
    Used only with the -r and the -gr flag. Used to group the output of groupReference under a locator

-----------------------------------------

gn    : groupName       [string] []
    Used only with the -gr flag. Optionally used to set the name of the transform node that the imported/referenced items will be grouped under.

-----------------------------------------

gr    : groupReference  [boolean] []
    Used only with the -r or the -i flag. Used to group all the imported/referenced items under a single transform.

-----------------------------------------

iv    : ignoreVersion   [boolean] []
    Used to open files with version greater or less than those officially supported. Data loss, data corruption or failure to open altogether are all possibilities, but as much as can be successfully read, will be. May only be used with the -o flag.

-----------------------------------------

i     : i               [boolean] []
    Import the specified file. Returns the name of the imported file.

-----------------------------------------

ifr   : importFrameRate [boolean] []
    Used only with the -i flag. Used to import the frame rate and set it as Maya's frame rate.

-----------------------------------------

ir    : importReference [boolean] []
    Remove the encapsulation of the reference around the data within the specified file. This makes the contents of the specified file part of the current scene and all references to the original file are lost. Returns the name of the reference that was imported.

-----------------------------------------

itr   : importTimeRange [string] []
    Used only with the -i flag. Used to import the time range and apply it to Maya's playback range in one of three different ways as specified by the string. The valid strings are "keep", which keeps Maya's playback range untouched, "override", which overrides Maya's playback range with the imported range, and "combine", which extends Maya's playback range to encompass the imported range.

-----------------------------------------

lfo   : lastFileOption  [boolean] ['query']
    On query, returns the last option string used by the file command.

-----------------------------------------

ltf   : lastTempFile    [boolean] ['query']
    When queried, this flag returns the temp file name used during file save. The temp file will be left in the same directory as the intended file name if the save fails.

-----------------------------------------

l     : list            [boolean] ['query']
    List all files. Returns a string array of the names of all segment/reference files. Duplicates will be removed. So if a file is referenced more than once, and the -withoutCopyNumber flag is set, it will only be listed once. in the scene.

-----------------------------------------

lad   : loadAllDeferred [boolean] []
    This flag is obsolete, and has been replaced by the loadReferenceDepth flag. When used with the -open flag, determines if the -deferReference flag is respected when reading in the file. If true is passed, all of the references are loaded. If false is passed, the -deferReference flag is respected.

-----------------------------------------

lar   : loadAllReferences [boolean] []
    This flag is obsolete and has been replaced with the loadReferenceDepth flag. When used with the -open flag, this will cause all references to be loaded.

-----------------------------------------

lnr   : loadNoReferences [boolean] []
    This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top- most reference only.

-----------------------------------------

lr    : loadReference   [string] ['query']
    This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file.   If a file is not given, the command will load (or reload) the last used reference file.

-----------------------------------------

lrd   : loadReferenceDepth [string] []
    Used to specify which references should be loaded. Valid types are "all", "none" and "topOnly", which will load all references, no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or -lr/loadReference flags. When "none" is used with -lr/loadReference, only path validation is performed. This can be used to replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth type, "asPrefs". This will force any nested references to be loaded according to the state (if any) stored in the current scene file, rather than according to the state saved in the reference file itself.

-----------------------------------------

lrp   : loadReferencePreview [string] []
    This flag will perform a special preview-only load of a reference file. A preview-only reference file is not completely loaded, but instead is partially loaded so that certain information, such as nested references it contains, can be determined. Nested references that are previewed remain in a special preview-only state.

-----------------------------------------

ls    : loadSettings    [string] []
    When used with the "o/open" flag this flag specifies which reference load settings should be used. Reference load settings specify which references should be brought in loaded and which unloaded. Those reference files that are brought in unloaded will usually not need to be read and interpreted by Maya. This can potentially reduce the time it takes Maya to load the whole scene. If no "ls/loadSettings" flag is specified, or the empty string ("") is used as the flag argument, the default load settings are used. The default load settings represent the state of all references when the file was last saved. The load settings "implicitLoadSettings" refer to the temporary load settings generated by the "bls/buildLoadSettings" flag and edited with the "loadSettings" command. Currently on the default and implicit load settings are supported.

-----------------------------------------

loc   : location        [boolean] ['query']
    Query the location of the given file name.

-----------------------------------------

lcu   : lockContainerUnpublished [boolean] []
    Set the unpublised lock state for all containers in this file. This will not lock the attributes in the main scene directly, but any file that references this scene will have all its containers come in as unpublished locked.

-----------------------------------------

lf    : lockFile        [boolean] []
    Lock or unlock the main scene. Any file referencing this scene will automatically lock all attributes and nodes. Also prevents reference edits from being saved to it from a parent file.

-----------------------------------------

lck   : lockReference   [boolean] []
    Locks attributes and nodes from the referenced file.

-----------------------------------------

mns   : mapPlaceHolderNamespace [[string, string]] ['query', 'edit']
    Map a placeHolderNamespace to the given reference. Must be used with the file -i/import, -r/reference flags in create mode. The first string is the place holder namespace, including the angle brackets (ex: "<foo>"). The second string is the reference node whose namespace it should be mapped to (ex: "refRN"). If the namespace should be mapped to the root namespace, use ":". To collapse the namespace (i.e., map it to "None"), use "". When queried, namespaces that are mapped to "None" will return "(None)" for clarity.

-----------------------------------------

mnp   : mergeNamespaceWithParent [boolean] []
    Used with the removeReference flag. When removing a file reference and its namespace, move the rest of the namespace content to parent namespace. Cannot be used if the reference resides in the root namespace.

-----------------------------------------

mnr   : mergeNamespaceWithRoot [boolean] []
    Used with the removeReference flag. When removing a file reference and its namespace, move the rest of the namespace content to root namespace. Cannot be used if the reference resides in the root namespace.

-----------------------------------------

mnc   : mergeNamespacesOnClash [boolean] []
    Used with the import, reference or edit flags, this option will prevent new namespaces from being created when namespaces of the same name already exist within Maya. The default value is false. For example, if an object "pSphere1", which is being imported, refers to the namespace "ref" and there is already a namespace called "ref" defined in Maya. If mergeNamespacesOnClash is true, the existing "ref" namespace will be reused and pSphere1 will be moved into the existing namespace; and if the namespace has another object which is also named "pSphere1", then the imported one will be renamed with an incremental number("pSphere2"). On the other hand, if mergeNamespacesOnClash is false, a new namespace will be created with an incremental number (in first case is "ref1") and pSphere1 will be moved into the "ref1" namespace. This flag also support nested namespace, for example, if an object "pSphere1" which is imported and refers to namespace "ref:foo" and mergeNamespacesOnClash is true this time, then the existing "ref:foo" will be reused and the object will be moved into "ref:foo". Also if mergeNamespacesOnClash is false, then a new namespace "ref:foo1" will be created and "pSphere1" will be moved into that new namespace.

-----------------------------------------

mf    : modified        [boolean] ['query']
    Set the modified state of the entire scene. If the scene is modified it will need to be saved before a new file is opened or created. Normally there is no need to edit this flag as the state of the file is updated automatically whenever an object is created or modified. If editing of the state is desired, it is done without use of the edit flag as covered in the example section below. In query mode, if the scene has been modified 1 is returned. Otherwise 0 is returned.

-----------------------------------------

ms    : moveSelected    [boolean] ['edit']
    This flag is obsolete.

-----------------------------------------

ns    : namespace       [string] ['edit']
    The namespace name to use that will group all objects during importing and referencing. Change the namespace used to group all the objects from the specified referenced file. The reference must have been created with the "Using Namespaces" option, and must be loaded. Non-referenced nodes contained in the existing namespace will also be moved to the new namespace. The new namespace will be created by this command and can not already exist. The old namespace will be removed.

-----------------------------------------

new   : newFile         [boolean] []
    Initialize the scene. Returns untitled scene with default location.

-----------------------------------------

o     : open            [boolean] []
    Open the specified file. Returns the name of the opened file.

-----------------------------------------

op    : options         [string] ['query']
    Set/query the currently set file options. file options are used while saving a maya file. Two file option flags supported in current file command are v and p.    * v(verbose) indicates whether long or short attribute names and command flags names are used when saving the file. Used by both maya ascii and maya binary file formats.   It only can be 0 or 1.   Setting v=1 indicates that long attribute names and command flag names will be used. By default, or by setting v=0, short attribute names will be used.    * p(precision) defines the maya file IO's precision when saving the file. Only used by maya ascii file format.   It is an integer value. The default value is 17.    The option format is "flag1=XXX;flag2=XXX".Maya uses the last v and p as the final result.   Note:   1\. Use a semicolon(";") to separate several flags. 2\. No blank space(" ") in option string.

-----------------------------------------

pns   : parentNamespace [boolean] ['query']
    Returns the name(s) of a referenced file's parent namespaces.

-----------------------------------------

pos   : postSaveScript  [string] []
    When used with the save flag, the specified script will be executed after the file is saved.

-----------------------------------------

prs   : preSaveScript   [string] []
    When used with the save flag, the specified script will be executed before the file is saved.

-----------------------------------------

pn    : preserveName    [boolean] []
    When used with compress, it will retain the regular extension rather than appending .gz.

-----------------------------------------

pr    : preserveReferences [boolean] []
    Modifies the various import/export flags such that references are imported/exported as actual references rather than copies of those references.

-----------------------------------------

pv    : preview         [boolean] []
    Used in conjunction with any of the -exportXXX flags, causes Maya to return a list of the nodes that would be exported, without actually writing the exported file to disk.

-----------------------------------------

pmt   : prompt          [boolean] ['query']
    This flag controls the display of file prompting dialogs. Some examples of file prompting dialogs include error messages that require user confirmation and missing file reference dialogs. Once this flag is used, every instance of the file command will use the last set value of this flag. Some interactive file operations may post dialogs even when the flag is set to false, but every scripted file command will not display any dialogs when this flag is set to false. The default value is true.

-----------------------------------------

pm    : proxyManager    [string] []
    When a one or more proxy references are added to an existing file reference, the proxy manage node is used to define the proxies associated with that reference. This flag is used in conjunction with the activeProxy and proxyTag flag to specify the proxyManager of interest. This flag is also used to specify the proxyManager for a proxy reference in the file referencing preload information, when used in conjunction with the referenceDepthInfo flag.

-----------------------------------------

pt    : proxyTag        [string] []
    This flag is intended for internal use only during file load or preload. Proxy tags are names you assign to proxy references to more easily manage the proxy references from the reference editor. Proxy tags are unique within a given proxy set. This flag must be used in conjunction with the proxyManager flag.

-----------------------------------------

r     : reference       [boolean] ['query']
    Create a reference to the specified file. Returns the name of the file referenced.   Query all file references from the specified file.

-----------------------------------------

rdi   : referenceDepthInfo [uint] []
    This flag is used to store reference loading preferences associated with a Maya ascii file (.ma). This flag is only useful during file I/O so users should not have any need to use this flag.

-----------------------------------------

rfn   : referenceNode   [string] ['query']
    This flag is only used during queries. In MEL, if it appears before -query then it must be followed by the name of one of the scene's reference nodes. That will determine the reference to be queried by whatever flags appear after -query. If the named reference node does not exist within the scene the command will fail with an error.  In Python the equivalent behavior is obtained by passing the name of the reference node as the flag's value.  In MEL, if this flag appears after -query then it takes no argument and will cause the command to return the name of the reference node associated with the file given as the command's argument. If the file is not a reference or for some reason does not have a reference node (e.g., the user deleted it) then an empty string will be returned. If the file is not part of the current scene then the command will fail with an error.  In Python the equivalent behavior is obtained by passing True as the flag's value.  In query mode, this flag can accept a value.

-----------------------------------------

rns   : relativeNamespace [string] []
    This flag can be used with the exportSelected, exportSelectedStrict and exportAll operations to specify that the nodes in the exported file are to be written out relative to a specified namespace. This provides the ability to remove undesired levels of namespacing from the node names as they are exported. The relativeNamespace value specifies the namespace to use as the relative root for the exported nodes, and must be specified as an absolute namespace. Nodes in the exported file not residing within the specified relative namespace will be written out using absolute namespace names. Note: this flag cannot be used in conjunction with the preserveReferences flag.

-----------------------------------------

rdn   : removeDuplicateNetworks [boolean] []
    When set, Maya will remove imported networks if the same network is also detected in the current scene. You can explicitly specify that certain types of networks be exempted from removal by this flag. For example, if you set to the optionVar removeDuplicateShadingNetworksOnImport to 0 (or disable the option Remove Duplicate Shading Networks from the File > Import options), then shading networks will be exempted from removal by this flag.This flag can only be used in conjunction with the -i/import flag.

-----------------------------------------

rr    : removeReference [boolean] []
    Remove the given file reference from its parent. This will also Remove everything this file references. Returns the name of the file removed. If the reference is alone in its namespace, remove the namespace. If there are objects remaining in the namespace after the file reference is removed, by default, keep the remaining objects in the namespace. To merge the objects remaining in the namespace to the parent or root namespace, use flags mergeNamespaceWithParent or mergeNamespaceWithRoot. The empty file reference namespace is then removed. To forcibly delete all objects, use flag force. The empty file reference namespace is then removed.

-----------------------------------------

rn    : rename          [string] []
    Rename the scene. Used mostly during save to set the saveAs name. Returns the new name of the scene.

-----------------------------------------

ra    : renameAll       [boolean] []
    If true, rename all newly-created nodes, not just those whose names clash with existing nodes. Only available with -i/import.

-----------------------------------------

rts   : renameToSave    [boolean] ['query']
    If true, the scene will need to be renamed before it can be saved. When queried this flag returns true if the scene must be renamed before it can be saved.   The default is false.

-----------------------------------------

rpr   : renamingPrefix  [string] ['query']
    The string to use as a prefix for all objects from this file. This flag has been replaced by -ns/namespace.

-----------------------------------------

rpl   : renamingPrefixList [boolean] ['query']
    This flag returns a list of all of the renaming prefixes used by the file.

-----------------------------------------

rep   : replaceName     [[string, string]] ['query', 'edit']
    Define a search and replace string. Will apply search and replace to leaf node names. The search string can include namespaces and wild-cards, but will only apply to leaf nodes in a dag hierarchy. Intended for use with offline edits files. May only be used with file -i/import or -r/reference. If a nested reference also defines a substitution, it will become the active substitution table while loading the nested reference. Note: if used with the -e/edit flag, the replacement will only be applied the next time the reference is loaded Examples: -replace "*pCube1" "prop" will change "foo:pCube1" to "foo:prop" and "|A:pCube1|B:pCube1" to "|A:pCube1|prop".

-----------------------------------------

rer   : resetError      [boolean] []
    Turn off any pre-existing global file errors.

-----------------------------------------

rnn   : returnNewNodes  [boolean] []
    Used to control the return value in open, import, loadReference, and reference operations. It will force the file command to return a list of new nodes added to the current scene.

-----------------------------------------

s     : save            [boolean] []
    Save the specified file. Returns the name of the saved file.

-----------------------------------------

sdc   : saveDiskCache   [string] ['query']
    This flag sets the saveAs option for Jiggle disk caches. The valid inputs are "always" \- always copy a file texture to a new location, "never" \- do not copy at all.   C: The default is "always".   Q: When queried it returns a string ("always", "never").

-----------------------------------------

sr    : saveReference   [boolean] []
    Save reference node edits and connections to reference file. This includes newly added history and animation, provided that these do not apply to any objects outside the reference being saved.

-----------------------------------------

sru   : saveReferencesUnloaded [boolean] []
    This flag can only be used in conjunction with the save flag. It specifies that the saved file will be saved with all references unloaded.

-----------------------------------------

stx   : saveTextures    [string] ['query']
    This flag sets the saveAs option for 3d Paint file textures. The valid inputs are "always" \- always copy a file texture to a new location, "unlessRef" \- copy only if this is not a referenced file texture, "never" \- do not copy at all.   C: The default is "unlessRef".   Q: When queried it returns a string ("always", unlessRef", "never").

-----------------------------------------

sn    : sceneName       [boolean] ['query']
    return the name of the current scene.

-----------------------------------------

seg   : segment         [string] []
    This flag is obsolete.

-----------------------------------------

sa    : selectAll       [boolean] []
    Select all the components of this file as well as its child files. Note that the file specified must be one that is already opened in this Maya session. The default behavior is to replace the existing selection. Use with the "add" flag to keep the active selection list.

-----------------------------------------

sh    : shader          [boolean] ['query']
    For use with exportSelected to specify whether attached shaders should be included in the export.

-----------------------------------------

shd   : sharedNodes     [string] []
    This flag modifies the '-r/reference' flag to indicate that certain types of nodes within that reference should be treated as shared nodes. All shared nodes will be placed in the default namespace. New copies of those nodes will not be created if a copy already exists in the default namespace, instead the shared node will be merged with the existing node. The specifics of what happens when two nodes are merged depends on the node type. In general attribute values will not be merged, meaning the values set on any existing shared nodes will be retained, and the values of the nodes being merged in will be ignored. The valid options are "displayLayers", "shadingNetworks", "renderLayersByName", and "renderLayersById". This flag is multi-use; it may be specified multiple times to for example, share both display layers and shading networks. Two shading networks will only be merged if they are identical: the network of nodes feeding into the shading group must be arranged identically with equivalent nodes have the same name and node type. Additionally if a network is animated or contains a DAG object or expression it will not be mergeable. This flag cannot be used in conjunction with -srf/sharedReferenceFile.

-----------------------------------------

srf   : sharedReferenceFile [boolean] []
    Can only be used in conjunction with the -r/reference flag and the -ns/namespace flag (there is no prefix support). This flag modifies the '-r/reference' flag to indicate that all nodes within that reference should be treated as shared nodes. New copies of those nodes will not be created if a copy already exists. Instead, the shared node will be merged with the existing node. The specifics of what happens when two nodes are merged depends on the node type. This flag cannot be used in conjunction with -shd/sharedNodes.

-----------------------------------------

shn   : shortName       [boolean] ['query']
    When used with a main query flag it indicates that the file name returned will be the short name (i.e., just a file name without any directory paths). If this flag is not present, the full name and directory path will be returned.

-----------------------------------------

str   : strict          [boolean] []
    Set strict file path resolution. If true, all paths will be matched exactly, both relative and absolute. Relative paths will be considered relative to the project root directory. May only be used with the -o/open, -i/import, -ir/importReference or -r/reference flags.

-----------------------------------------

sns   : swapNamespace   [[string, string]] []
    Can only be used in conjunction with the -r/reference or -i/import flags. This flag will replace any occurrences of a given namespace to an alternate specified namespace. This namespace "swap" will occur as the file is referenced in. It takes in two string arguments. The first argument specifies the namespace to replace. The second argument specifies the replacement namespace. Use of this flag, implicitly enables the use of namespaces and cannot be used with deferReference.

-----------------------------------------

typ   : type            [string] ['query']
    Set the type of this file. By default this can be any one of: "mayaAscii", "mayaBinary", "mel", "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Adobe(R) Illustrator(R)", "image" plug-ins may define their own types as well.   Return a string array of file types that match this file.

-----------------------------------------

uc    : uiConfiguration [boolean] ['query']
    Save the ui configuration with the scene in a uiConfiguration script node. (eg. panes, etc.) The current default is on and is set in initialStartup.mel.

-----------------------------------------

ur    : unloadReference [string] []
    This flag will unload the reference file associated with the passed reference node.

-----------------------------------------

un    : unresolvedName  [boolean] ['query']
    When used with a main query flag it indicates that the file name returned will be unresolved (i.e., it will be the path originally specified when the file was loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will be returned.

-----------------------------------------

uns   : usingNamespaces [boolean] ['query']
    Returns boolean. Queries whether the specified reference file uses namespaces or renaming prefixes.

-----------------------------------------

wcn   : withoutCopyNumber [boolean] ['query']
    When used with a main query flag it indicates that the file name returned will not have a copy number appended to the end. If this flag is not present, the file name returned may have a copy number appended to the end.

-----------------------------------------

w     : writable        [boolean]
    Query whether the given file is writable in the current scene. For main scene files this indicates writable to the file system by the current user. Files referenced by the main scene file are always not writable (referenced files are by nature read only). Files not present in the current scene always return false.

    """

def fileBrowserDialog(an="string",ds="int",fc="script",ft="string",fl="string",includeName="string",m="int",om="string",tm="string",wt="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fileBrowserDialog.html



-----------------------------------------

fileBrowserDialog is undoable, NOT queryable, and NOT editable.

The fileBrowserDialog and fileDialog commands have now been deprecated. Both
commands are still callable, but it is recommended that the fileDialog2
command be used instead. To maintain some backwards compatibility, both
fileBrowserDialog and fileDialog will convert the flags/values passed to them
into the appropriate flags/values that the fileDialog2 command uses and will
call that command internally. It is not guaranteed that this compatibility
will be able to be maintained in future versions so any new scripts that are
written should use fileDialog2.

See below for an example of how to change a script to use fileDialog2.


-----------------------------------------


Return Value:

string  Dialog name


-----------------------------------------


Flags:

-----------------------------------------

an    : actionName      [string] []
    Script to be called when the file is validated.

-----------------------------------------

ds    : dialogStyle     [int] []
    * 0 for old style dialog   * 1 for Windows 2000 style Explorer style   * 2 for Explorer style with "Shortcut" tip at bottom

-----------------------------------------

fc    : fileCommand     [script] []
    The script to run on command action

-----------------------------------------

ft    : fileType        [string] []
    Set the type of file to filter. By default this can be any one of: "mayaAscii", "mayaBinary", "mel", "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Illustrator", "image".   plug-ins may define their own types as well.

-----------------------------------------

fl    : filterList      [string] []
    Specify file filters. Used with dialog style 1 and 2. Each string should be a description followed by a comma followed by a semi-colon separated list of file extensions with wildcard.

-----------------------------------------

includeName : includeName     [string] []
    Include the given string after the actionName in parentheses. If the name is too long, it will be shortened to fit on the dialog (for example, /usr/alias/commands/scripts/fileBrowser.mel might be shortened to /usr/...pts/fileBrowser.mel)

-----------------------------------------

m     : mode            [int] []
    Defines the mode in which to run the file brower:    * 0 for read   * 1 for write   * 2 for write without paths (segmented files)   * 4 for directories have meaning when used with the action  +100 for returning short names

-----------------------------------------

om    : operationMode   [string] []
    Enables the option dialog. Valid strings are:    * "Import"   * "Reference"   * "SaveAs"   * "ExportAll"   * "ExportActive"

-----------------------------------------

tm    : tipMessage      [string] []
    Message to be displayed at the bottom of the style 2 dialog box.

-----------------------------------------

wt    : windowTitle     [string]
    Set the window title of a style 1 or 2 dialog box

    """

def fileDialog(app=1,dfn="string",dm="string",m="int",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fileDialog.html



-----------------------------------------

fileDialog is undoable, NOT queryable, and NOT editable.

The fileBrowserDialog and fileDialog commands have now been deprecated. Both
commands are still callable, but it is recommended that the fileDialog2
command be used instead. To maintain some backwards compatibility, both
fileBrowserDialog and fileDialog will convert the flags/values passed to them
into the appropriate flags/values that the fileDialog2 command uses and will
call that command internally. It is not guaranteed that this compatibility
will be able to be maintained in future versions so any new scripts that are
written should use fileDialog2.

See below for an example of how to change a script to use fileDialog2.


-----------------------------------------


Return Value:

string  Name of dialog


-----------------------------------------


Flags:

-----------------------------------------

app   : application     [boolean] []
    This is a "Mac" only flag. This brings up the dialog which selects only the application bundle.

-----------------------------------------

dfn   : defaultFileName [string] []
    Set default file name. This flag is available under "write" mode

-----------------------------------------

dm    : directoryMask   [string] []
    This can be used to specify what directory and file names will be displayed in the dialog. If not specified, the current directory will be used, with all files displayed. The string may contain a path name, and must contain a wild-carded file specifier. (eg "*.cc" or "/usr/u/*") If just a path is specified, then the last directory in the path is taken to be a file specifier, and this will not produce the desired results.

-----------------------------------------

m     : mode            [int] []
    Defines the mode in which to run the file dialog:    * 0 for read   * 1 for write  Write mode can not be used in conjunction with the -application flag.

-----------------------------------------

t     : title           [string]
    Set title text. The default value under "write" mode is "Save As". The default value under "read" mode is "Open".

    """

def fileDialog2(bbo="int",cc="string",cap="string",ds="int",ff="string",fm="int",ftc="script",hne=1,okc="string",oca="script",ocm="script",oc2="script",ocr="script",oin="script",rf=1,sff="string",sc="script",spe=1,dir="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fileDialog2.html



-----------------------------------------

fileDialog2 is undoable, NOT queryable, and NOT editable.

This command provides a dialog that allows users to select files or
directories.


-----------------------------------------


Return Value:

string  array


-----------------------------------------


Flags:

-----------------------------------------

bbo   : buttonBoxOrientation [int] []
    * 1 Vertical button box layout. Cancel button is below the accept button.    * 2 Horizontal button box layout. Cancel button is to the right of the accept button.

-----------------------------------------

cc    : cancelCaption   [string] []
    If the dialogStyle flag is set to 2 then this provides a caption for the Cancel button within the dialog.

-----------------------------------------

cap   : caption         [string] []
    Provide a title for the dialog.

-----------------------------------------

ds    : dialogStyle     [int] []
    * 1 On Windows or Mac OS X will use a native style file dialog.   * 2 Use a custom file dialog with a style that is consistent across platforms.

-----------------------------------------

ff    : fileFilter      [string] []
    Provide a list of file type filters to the dialog. Multiple filters should be separated by double semi-colons. See the examples section.

-----------------------------------------

fm    : fileMode        [int] []
    Indicate what the dialog is to return.    * 0 Any file, whether it exists or not.   * 1 A single existing file.   * 2 The name of a directory. Both directories and files are displayed in the dialog.   * 3 The name of a directory. Only directories are displayed in the dialog.   * 4 Then names of one or more existing files.

-----------------------------------------

ftc   : fileTypeChanged [script] []
    MEL only. The string is interpreted as a MEL callback, to be called when the user-selected file type changes. The callback is of the form:  global proc MyCustomFileTypeChanged(string $parent, string $newType)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag. The newType argument is the new file type.

-----------------------------------------

hne   : hideNameEdit    [boolean] []
    Hide name editing input field.

-----------------------------------------

okc   : okCaption       [string] []
    If the dialogStyle flag is set to 2 then this provides a caption for the OK, or Accept, button within the dialog.

-----------------------------------------

oca   : optionsUICancel [script] []
    MEL only. The string is interpreted as a MEL callback, to be called when the dialog is cancelled (with Cancel button or close button to close window). The callback is of the form:  global proc MyCustomOptionsUICancel()

-----------------------------------------

ocm   : optionsUICommit [script] []
    MEL only. The string is interpreted as a MEL callback, to be called when the dialog is successfully dismissed. It will not be called if the user cancels the dialog, or closes the window using window title bar controls or other window system means. The callback is of the form:  global proc MyCustomOptionsUICommit(string $parent)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.

-----------------------------------------

oc2   : optionsUICommit2 [script] []
    MEL only. As optionsUICommit, the given string is interpreted as a MEL callback, to be called when the dialog is successfully dismissed. The difference is that this callback takes one additional argument which is the file name selected by the user before the dialog validation. It will not be called if the user cancels the dialog, or closes the window using window title bar controls or other window system means. The callback is of the form:  global proc MyCustomOptionsUICommit(string $parent, string $selectedFile)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.

-----------------------------------------

ocr   : optionsUICreate [script] []
    MEL only. The string is interpreted as a MEL callback, to be called on creation of the file dialog. The callback is of the form:  global proc MyCustomOptionsUISetup(string $parent)  The parent argument is the parent layout into which controls can be added. This parent is the right-hand pane of the file dialog.

-----------------------------------------

oin   : optionsUIInit   [script] []
    MEL only. The string is interpreted as a MEL callback, to be called just after file dialog creation, to initialize controls. The callback is of the form:  global proc MyCustomOptionsUIInitValues(string $parent, string $filterType)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag. The filterType argument is the initial file filter.

-----------------------------------------

rf    : returnFilter    [boolean] []
    If true, the selected filter will be returned as the last item in the string array along with the selected files.

-----------------------------------------

sff   : selectFileFilter [string] []
    Specify the initial file filter to select. Specify just the begining text and not the full wildcard spec.

-----------------------------------------

sc    : selectionChanged [script] []
    MEL only. The string is interpreted as a MEL callback, to be called when the user changes the file selection in the file dialog. The callback is of the form:  global proc MyCustomSelectionChanged(string $parent, string $selection)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag. The selection argument is the full path to the newly-selected file.

-----------------------------------------

spe   : setProjectBtnEnabled [boolean] []
    Define whether the project button should be enabled

-----------------------------------------

dir   : startingDirectory [string]
    Provide the starting directory for the dialog.

    """

def fileInfo(q=1,rfn="string",rm="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fileInfo.html



-----------------------------------------

fileInfo is NOT undoable, queryable, and NOT editable.

fileInfo provides a mechanism for keeping information related to a Maya scene
file. Each invocation of the command consists of a keyword/value pair, where
both the keyword and the associated value are strings. The command may be
invoked multiple times with different keywords. Maya emits this command
several times into each file it creates, primarily to provide details such as
which productization or packaging of the program was used (e.g "Complete",
"Unlimited"), the specific version and build identification that was run, and
the operating system on which it was run. Maya may make use of this
information when present in files it reads. All keyword/value pairs defined by
use of the fileInfo command are preserved when Maya saves the scene, whether
to an ASCII or binary file.


-----------------------------------------


Return Value:

string[]  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

rfn   : referenceNode   [string] ['query']
    Specify the name of a referenceNode to indicate the scene file to query. This flag is only valid during query.  In query mode, this flag needs a value.

-----------------------------------------

rm    : remove          [string]
    If the remove flag is specified, the string following it is a keyword to remove from the list of fileInfo to be saved with the scene file.

    """

def filePathEditor(q=1,ao=1,at="string",bt="string",cr="[string, string]",dt="string",f=1,ld="string",lf="string",lrt=1,p=1,rc=1,rf=1,rt="string",rel=1,r="string",ra=1,rfd="string",rs="[string, string]",s=1,tmp=1,tl="string",u=1,wa=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filePathEditor.html



-----------------------------------------

filePathEditor is undoable, queryable, and NOT editable.

Maya can reference and use external files, such as textures or other Maya
scenes. This command is used to get the information about those file paths and
modify them in bulk. By default, only the most frequently used types of files
are presented to the user:

  * Texture
  * Scene reference
  * Audio
  * Image plane

For the command to manage more file types, those must be explicitly requested
by the caller using the "registerType" flag. This flag tells the command about
attributes or nodes that are to reveal their paths when the command is used.

Currently, the attributes specified through this flag must have the
"usedAsFileName" property. Supported nodes are "reference" and plug-in nodes.
For example: "brush.flowerImage" or "reference" can be used as value for this
flag.

Conversely, the "deregisterType" flag can be used to tell the command to stop
handling certain attributes or nodes.

Once the set of attributes and nodes to be searched for external files is
selected, the command can be used to obtain a list of plugs that contain file
names. Additional information can be obtained, such as each file's name,
directory, and report whether the file exists. Additional information about
the associated node or plug can also be obtained, such as its name, type and
label.

Finally, the command can be used to perform various manipulations such as
editing the paths, remapping the files or verifying the presence of
identically-named files in target directories. See the "repath",
"copyAndRepath" and "replaceField" flags for more information.

The results of these manipulations can be previewed before they are applied
using the "preview" flag.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ao    : attributeOnly   [boolean] ['query']
    Used with "listFiles" to return the node and attribute name that are using the files.

-----------------------------------------

at    : attributeType   [string] ['query']
    Query the attribute type for the specified plug.

-----------------------------------------

bt    : byType          [string] ['query']
    Used with "listFiles" to query files that are used by the specified node type or attribute type.  In query mode, this flag needs a value.

-----------------------------------------

cr    : copyAndRepath   [[string, string]] []
    Copy a source file to the destination path and repath the plug data to the new file. The source file must have the same name as the one in the plug. The command will look for the file at the specified location first. If not found, the command will try to use the original file in the plug. If the file is still not found, nothing is done.

-----------------------------------------

dt    : deregisterType  [string] []
    Deregister a file type from the list of registered types so the command stops handling it. Unless the "temporary" flag is used, the type will be removed from the preferences will not reappear on application restart. When the "temporary" flag is specified, the deregistration is only effective for the current session. The deregistration will be rejected if the type has already been unregistered. However, it is valid to deregister permanently (without the "temporary" flag) a type after it has been temporarily deregistered.

-----------------------------------------

f     : force           [boolean] []
    Used with flag "repath" to repath all files to the new location, including the resolved files. Otherwise, "repath" will only deal with the missing files. Used with flag "copyAndRepath" to overwrite any colliding file at the destination. Otherwise, "copyAndRepath" will use the existing file at the destination instead of overwriting it. The default value is off.

-----------------------------------------

ld    : listDirectories [string] ['query']
    List all sub directories of the specified directory. Only directories containing at least one file whose type is registered (see "registerType") will be listed. If no directory is provided, all directories applicable to the scene will be returned.  In query mode, this flag needs a value.

-----------------------------------------

lf    : listFiles       [string] ['query']
    List files in the specified directory. No recursion in subdirectories will be performed.  In query mode, this flag needs a value.

-----------------------------------------

lrt   : listRegisteredTypes [boolean] ['query']
    Query the list of registered attribute types. The registered types include the auto-loaded types from the preference file and the types explicitly registered by the user, both with and without the "temporary" flag.

-----------------------------------------

p     : preview         [boolean] []
    Used with "repath", "replaceString" or "copyAndRepath" to preview the result of the operation instead of excuting it. When it is used with "repath" or "replaceString", the command returns the new file path and a status flag indicating whether the new file exists (1) or not (0). The path name and the file status are listed in pairs. When it is used with "copyAndRepath", the command returns the files that need copying.

-----------------------------------------

rc    : recursive       [boolean] []
    Used with flag "repath" to search the files in the target directory and its subdirectories recursively. If the flag is on, the command will repath the plug to a file that has the same name in the target directory or sub directories. If the flag is off, the command will apply the directory change without verifying that the resulting file exists.

-----------------------------------------

rf    : refresh         [boolean] []
    Clear and re-collect the file information in the scene. The command does not automatically track file path modifications in the scene. So it is the users responsibility to cause refreshes in order to get up-to-date information.

-----------------------------------------

rt    : registerType    [string] []
    Register a new file type that the command will handle and recognize from now on. Unless the "temporary" flag is used, the registered type is saved in the preferences and reappears on application restart. The new type will be rejected if it collides with an existing type or label. One exception to this is when registering a type without the "temporary" flag after the type has been registered with it. This is considered as modifying the persistent/temporary property of the existing type, rather than registering a new type.

-----------------------------------------

rel   : relativeNames   [boolean] ['query']
    Used with "listDirectories" or "listFiles" to return the relative path of each directory or file. Paths are relative to the current project folder. If a file or the directory is not under the current project folder, the returned path will still be a full path.

-----------------------------------------

r     : repath          [string] []
    Replace the directory part of a file path with a specified location. The file name will be preserved.

-----------------------------------------

ra    : replaceAll      [boolean] []
    Used with flag "replaceString", specifies how many times the matched string will be replaced. When the flag is false, only the first matched string will be replaced. Otherwise, all matched strings will be replaced. The default value is false.

-----------------------------------------

rfd   : replaceField    [string] []
    Used with the "replaceString" flag to control the scope of the replacement. Possible values are: "pathOnly" \- only replace strings in the directory part. "nameOnly" \- only replace strings in the file name, without the directory. "fullPath" \- replace strings anywhere in the full name. The default argument is "fullPath".

-----------------------------------------

rs    : replaceString   [[string, string]] []
    Replace the target string with the new string in the file paths. The flag needs two arguments: the first one is the target string and the second one is the new string. See the "replaceField" and "replaceAll" flags to control how the replacement is performed.

-----------------------------------------

s     : status          [boolean] ['query']
    Used with "listFiles", this will cause the returned list of files to include one status flag per file: 0 if it cannot be resolved and 1 if it can. Used with "listDirectories", this will cause the returned list of directories to include one status flag per directory: 0 if it cannot be resolved, 1 if it can and 2 if the resolution is partial. The status will be interleaved with the file/directory names, with the name appearing first. See the example for "listFiles". See the "withAttribute" flag for another way of getting per-file information. When multiple per-entry items appear in the list (e.g.: plug name), the status is always last.

-----------------------------------------

tmp   : temporary       [boolean] []
    Make the effect of the "register"/"deregister" flag only applicable in the current session. Normally, a type registration/deregistration is permanent and is made persistent via a preference file. When the "temporary" flag is specified, the changes will not be saved to the preference file. When the application restarts, any type that has been previously temporarily registered will not appear and any type that was temporarily deregistered will re-appear.

-----------------------------------------

tl    : typeLabel       [string] ['query']
    Used with "registerType" to set the label name for the new file type. Used with "query" to return the type label for the specified attribute type. For default types, the type label is the localized string. For other types, the type label is supplied by user.  In query mode, this flag needs a value.

-----------------------------------------

u     : unresolved      [boolean] ['query']
    Used with "listFiles" to query the unresolved files that are being used in the scene.

-----------------------------------------

wa    : withAttribute   [boolean]
    Used with "listFiles" to return the name of the plug using a given file. For example, if "file.jpg" is used by the plug "node1.fileTextureName", then the returned string will become the pair "file.jpg node1.fileTextureName". See the "status" flag for another way to get per-file information.

    """

def filterStudioImport(sp=1,ic=1,il=1,td="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filterStudioImport.html



-----------------------------------------

filterStudioImport is NOT undoable, NOT queryable, and NOT editable.

Directly sets the filter options on the studioImport plugin from anywhere in
MEL without having to use the UI. This is used by ViCE.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

sp    : convertShellToPoly [boolean] []
    If true, shells in the input will be converted to triangular meshes. If false, any/all shells encountered will be groups of surfaces.

-----------------------------------------

ic    : includeCameras  [boolean] []
    If true, cameras in the input to "studioImport" will be translated. If false, any/all cameras encountered by "studioImport" will be ignored.

-----------------------------------------

il    : includeLights   [boolean] []
    If true, lights in the input to "studioImport" will be translated. If false, any/all lights encountered by "studioImport" will be ignored.

-----------------------------------------

td    : transferDirectoryName [string]
    If set (non-empty), use as directory for storing imbedded binary files, else use the directory given by "theTempDirectory->fullName()".

    """

def getFileList(fs="string",fld="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getFileList.html



-----------------------------------------

getFileList is undoable, NOT queryable, and NOT editable.

Returns a list of files matching an optional wildcard pattern. Note that this
command works directly on raw system files and does not go through standard
Maya file path resolution.


-----------------------------------------


Return Value:

string[]  an array of file names


-----------------------------------------


Flags:

-----------------------------------------

fs    : filespec        [string] []
    wildcard specifier for search.

-----------------------------------------

fld   : folder          [string]
    return a directory listing

    """

def imfPlugins(q=1,ext="string",key="string",mfs="string",pn="string",rs="string",ws="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/imfPlugins.html



-----------------------------------------

imfPlugins is NOT undoable, queryable, and NOT editable.

This command queries all the available imf plugins for its name, keyword or
image file extension. Only one of the attributes (name, keyword or extension)
can be queried at a time. If no flags are specified, this command returns a
list of all available plugin names.


-----------------------------------------


Return Value:

string[]  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ext   : extension       [string] ['query']
    image file extension

-----------------------------------------

key   : keyword         [string] ['query']
    imf keyword

-----------------------------------------

mfs   : multiFrameSupport [string] ['query']
    multi frame IO is supported

-----------------------------------------

pn    : pluginName      [string] ['query']
    imf plugin name

-----------------------------------------

rs    : readSupport     [string] ['query']
    read operation is supported

-----------------------------------------

ws    : writeSupport    [string]
    write operation is supported

    """

def internalVar(uad=1,ubd=1,uhk=1,umm=1,upd=1,ups=1,usd=1,ush=1,utd=1,uwd=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/internalVar.html



-----------------------------------------

internalVar is undoable, NOT queryable, and NOT editable.

This command returns the values of internal variables. No modification of
these variables is supported.


-----------------------------------------


Return Value:

string  The value of the variable specified by the flag use.


-----------------------------------------


Flags:

-----------------------------------------

uad   : userAppDir      [boolean] []
    Return the user application directory.

-----------------------------------------

ubd   : userBitmapsDir  [boolean] []
    Return the user bitmaps prefs directory.

-----------------------------------------

uhk   : userHotkeyDir   [boolean] []
    Return the user hotkey directory.

-----------------------------------------

umm   : userMarkingMenuDir [boolean] []
    Return the user marking menu directory.

-----------------------------------------

upd   : userPrefDir     [boolean] []
    Return the user preference directory.

-----------------------------------------

ups   : userPresetsDir  [boolean] []
    Return the user presets directory.

-----------------------------------------

usd   : userScriptDir   [boolean] []
    Return the user script directory.

-----------------------------------------

ush   : userShelfDir    [boolean] []
    Return the user shelves directory.

-----------------------------------------

utd   : userTmpDir      [boolean] []
    Return a temp directory. Will check for TMPDIR environment variable, otherwise will return the current directory.

-----------------------------------------

uwd   : userWorkspaceDir [boolean]
    Return the user workspace directory (also known as the projects directory).

    """

def launch(dir="string",mov="string",pdf="string",web="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/launch.html



-----------------------------------------

launch is undoable, NOT queryable, and NOT editable.

Launch the appropriate application to open the document, web page or directory
specified.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

dir   : directory       [string] []
    A directory.

-----------------------------------------

mov   : movie           [string] []
    A movie file. The only acceptable movie file formats are MPEG, Quicktime, and Windows Media file. The file's name must end with .mpg, .mpeg, .mp4, .wmv, .mov, or .qt.

-----------------------------------------

pdf   : pdfFile         [string] []
    A PDF (Portable Document Format) document. The file's name must end with .pdf.

-----------------------------------------

web   : webPage         [string]
    A web page.

    """

def launchImageEditor(eif="string",vif="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/launchImageEditor.html



-----------------------------------------

launchImageEditor is undoable, NOT queryable, and NOT editable.

Launch the appropriate application to edit/view the image files specified.
This command works only on the Macintosh and Windows platforms.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

eif   : editImageFile   [string] []
    If the file is a PSD, then the specified verison of Photoshop is launched, and the file is opened in it. If file is any other image type, then the preferred image editor is launched, and the file is opened in it.

-----------------------------------------

vif   : viewImageFile   [string]
    Opens up an Image editor to view images.

    """

def melInfo():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/melInfo.html



-----------------------------------------

melInfo is NOT undoable, NOT queryable, and NOT editable.

This command returns the names of all global MEL procedures that are currently
defined as a string array. The user can query the definition of each MEL
procedure using the "whatIs" command.


-----------------------------------------


Return Value:

string[]  procedure names
    """

def namespace(q=1,an=1,add="string",ch="string",dnc=1,ex="string",f=1,ir="string",mno="string",mnp=1,mnr=1,mv="[string, string]",p="string",r=1,rel=1,rm="string",ren="[string, string]",set="string",vn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/namespace.html



-----------------------------------------

namespace is undoable, queryable, and NOT editable.

This command allows a namespace to be created, set or removed.

A namespace is a simple grouping of objects under a given name. Namespaces are
primarily used to resolve name-clash issues in Maya, where a new object has
the same name as an existing object (from importing a file, for example).
Using namespaces, you can have two objects with the same name, as long as they
are contained in differenct namespaces.

Namespaces are reminiscent of hierarchical structures like file systems where
namespaces are analogous to directories and objects are analogous to files.
The colon (':') character is the separator used to separate the names of
namespaces and nodes instead of the slash ('/') or backslash ('\') character.
Namespaces can contain other namespaces as well as objects. Like objects, the
names of namespaces must be unique within another namespace. Objects and
namespaces can be in only one namespace. Namespace names and object names
don't clash so a namespace and an object contained in another namespace can
have the same name.

There is an unnamed root namespace specified with a leading colon (':'). Any
object not in a named namespace is in the root namespace. Normally, the
leading colon is omitted from the name of an object as it's presence is
implied. The presence of a leading colon is important when moving objects
between namespaces using the 'rename' command. For the 'rename' command, the
new name is relative to the current namespace unless the new name is fully
qualified with a leading colon.

Namespaces are created using the 'add/addNamespace' flag. By default they are
created under the current namespace. Changing the current namespace is done
with the 'set/setNamespace' flag. To reset the current namespace to the root
namespace, use 'namespace -set ":";'. Whenever an object is created, it is
added by default to the current namespace.

When creating a new namespace using a qualified name, any intervening
namespaces which do not yet exist will be automatically created. For example,
if the name of the new namespace is specified as "A:B" and the current
namespace already has a child namespace named "A" then a new child namespace
named "B" will be created under "A". But if the current namespace does not yet
have a child named "A" then it will be created automatically. This applies
regardless of the number of levels in the provided name (e.g. "A:B:C:D").

The 'p/parent' flag can be used to explicitly specify the parent namespace
under which the new one should be created, rather than just defaulting to the
current namespace.

If the name given for the new namespace is absolute (i.e. it begins with a
colon, as in ":A:B") then both the current namespace and the 'parent' flag
will be ignored and the new namespace will be created under the root
namespace.

The relativeNamespace flag can be used to change the way node names are
displayed in the UI and returned by the 'ls' command. Here are some specific
details on how the return from the 'ls' command works in relativeNamespace
mode:

List all mesh objects in the scene:  
ls -type "mesh";  
The above command lists all mesh objects in the root and any child namespaces.
In relative name lookup mode, all names will be displayed relative to the
current namespace. When not in relative name lookup mode (the default
behaviour in Maya), results are printed relative to the root namespace.  
  
Using a "*" wildcard:  
namespace -set myNS;  
ls -type "mesh "*";  
  
  
In relative name lookup mode, the "*" will match to the current namespace and
thus the ls command will list only those meshes defined within the current
namespace (i.e. myNs). If relative name lookup is off (the default behaviour
in Maya), names are root-relative and thus "*" matches the root namespace,
with the net result being that only thoses meshes defined in the root
namespace will be listed.  
  
You can force the root namespace to be listed when in relative name lookup
mode by specifying ":*" as your search pattern (i.e. ls -type mesh ":*" which
lists those meshes defined in the root namespace only). Note that you can also
use ":*" when relative name lookup mode is off to match the root if you want a
consistent way to list the root.  
  
Listing child namespace contents:  
ls -type mesh "*:*";  
  
  
For an example to list all meshes in immediate child namespaces, use "*:*". In
relative name lookup mode "*:*" lists those meshes in immediate child
namespaces of the current namespaces. When not in relative name lookup mode,
"*:*" lists meshes in namespaces one level below the root.  
  
Recursive listing of namespace contents:  
Example: ls -type mesh -recurse on "*"  
  
  
The 'recurse' flag is provided on the "ls" command to recursively traverse any
child namespaces. In relative name lookup mode, the above example command will
list all meshes in the current and any child namespaces of current. When not
in relative name lookup mode, the above example command works from the root
downwards and is thus equivalent to "ls -type mesh".


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

an    : absoluteName    [boolean] ['query']
    This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces. For example ":ns:ball" is an absolute namespace name while "ns:ball" is not.

-----------------------------------------

add   : addNamespace    [string] []
    Create a new namespace with the given name. Both qualified names ("A:B") and unqualified names ("A") are acceptable. If any of the higher-level namespaces in a qualified name do not yet exist, they will be created. If the supplied name contains invalid characters it will first be modified as per the validateName flag.

-----------------------------------------

ch    : collapseAncestors [string] []
    Delete all empty ancestors of the given namespace. An empty namespace is a a namespace that does not contain any objects or other nested namespaces

-----------------------------------------

dnc   : deleteNamespaceContent [boolean] []
    Used with the 'rm/removeNamespace' flag to indicate that when removing a namespace the contents of the namespace will also be removed.

-----------------------------------------

ex    : exists          [string] ['query']
    Returns true if the specified namespace exists, false if not.

-----------------------------------------

f     : force           [boolean] []
    Used with 'mv/moveNamespace' to force the move operation to ignore name clashes.

-----------------------------------------

ir    : isRootNamespace [string] ['query']
    Returns true if the specified namespace is root, false if not.

-----------------------------------------

mno   : mergeNamespaceWithOther [string] []
    Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the specified namespace.

-----------------------------------------

mnp   : mergeNamespaceWithParent [boolean] []
    Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the parent namespace.

-----------------------------------------

mnr   : mergeNamespaceWithRoot [boolean] []
    Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the root namespace.

-----------------------------------------

mv    : moveNamespace   [[string, string]] []
    Move the contents of the first namespace into the second namespace. Child namespaces will also be moved.      Attempting to move a namespace containing referenced nodes will result in an error; use the 'file' command ('file -edit -namespace') to change a reference namespace.      If there are objects in the source namespace with the same name as objects in the destination namespace, an error will be issued. Use the 'force' flag to override this error - name clashes will be resolved by renaming the objects to ensure uniqueness.

-----------------------------------------

p     : parent          [string] []
    Used with the 'addNamespace' or 'rename' flags to specifiy the parent of the new namespace. The full namespace parent path is required. When using 'addNamespace' with an absolute name, the 'parent' will be ignored and the command will display a warning

-----------------------------------------

r     : recurse         [boolean] ['query']
    Can be used with the 'exists' flag to recursively look for the specified namespace

-----------------------------------------

rel   : relativeNames   [boolean] ['query']
    Turns on relative name lookup, which causes name lookups within Maya to be relative to the current namespace. By default this is off, meaning that name lookups are always relative to the root namespace. Be careful turning this feature on since commands such as setAttr will behave differently. It is wise to only turn this feature on while executing custom procedures that you have written to be namespace independent and turning relativeNames off when returning control from your custom procedures. Note that Maya will turn on relative naming during file I/O. Although it is not recommended to leave relativeNames turned on, if you try to toggle the value during file I/O you may notice that the value stays "on" because Maya has already temporarily enabled it internally.      When relativeNames are enabled, the returns provided by the 'ls' command will be relative to the current namespace. See the main description of this command for more details.

-----------------------------------------

rm    : removeNamespace [string] []
    Deletes the given namespace. The namespace must be empty for it to be deleted.

-----------------------------------------

ren   : rename          [[string, string]] []
    Rename the first namespace to second namespace name. Child namespaces will also be renamed. Both names are relative to the current namespace. Use the 'parent' flag to specify a parent namespace for the renamed namespace. An error is issued if the second namespace name already exists. If the supplied name contains invalid characters it will first be modified as per the validateName flag.

-----------------------------------------

set   : setNamespace    [string] []
    Sets the current namespace.

-----------------------------------------

vn    : validateName    [string]
    Convert the specified name to a valid name to make it contain no illegal characters. The leading illegal characters will be removed and other illegal characters will be converted to '_'. Specially, the leading numeric characters and trailing space characters will be also removed. Full name path can be validated as well. However, if the namespace of the path does not exist, command will only return the base name. For example, ":nonExistentNS:name" will be converted to "name". If the entire name consists solely of illegal characters, e.g. "123" which contains only leading digits, then the returned string will be empty.

    """

def namespaceInfo(an=1,bn=1,cur=1,dp=1,fn=1,int=1,ir=1,ls=1,lod=1,lon=1,p=1,r=1,sn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/namespaceInfo.html



-----------------------------------------

namespaceInfo is undoable, NOT queryable, and NOT editable.

This command displays information about a namespace. The target namespace can
optionally be specified on the command line. If no namespace is specified, the
command will display information about the current namespace.

A namespace is a simple grouping of objects under a given name. Each item in a
namespace can then be identified by its own name, along with what namespace it
belongs to. Namespaces can contain other namespaces like sets, with the
restriction that all namespaces are disjoint.

Namespaces are primarily used to resolve name-clash issues in Maya, where a
new object has the same name as an existing object (from importing a file, for
example). Using namespaces, you can have two objects with the same name, as
long as they are contained in different namespaces.

Note that namespaces are a simple grouping of names, so they do not effect
selection, the DAG, the Dependency Graph, or any other aspect of Maya. All
namespace names are colon-separated.

The namespace format flags are: baseName(shortName), fullName and
absoluteName. The flags are used in conjunction with the main query flags to
specify the desired namespace format of the returned result. They can also be
used to return the different formats of a specified namespace. By default,
when no format is specified, the result will be returned as a full name.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

an    : absoluteName    [boolean] []
    This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces. For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace modes. See also other format modifiers 'baseName', 'fullName', etc

-----------------------------------------

bn    : baseName        [boolean] []
    This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The base name of the namespace contains only the leaf level name and does not contain its parent namespace(s). For example the base name of an object named "ns:ball" is "ball". This mode will always return the base name in the same manner, and is not affected by the current namespace or relative namespace mode. See also other format modifiers 'absoluteName', 'fullName', etc The flag 'shortName' is a synonym for 'baseName'.

-----------------------------------------

cur   : currentNamespace [boolean] []
    Display the name of the current namespace.

-----------------------------------------

dp    : dagPath         [boolean] []
    This flag modifies the 'listNamespace' and 'listOnlyDependencyNodes' flags to indicate that the names of any dag objects returned will include as much of the dag path as is necessary to make the names unique. If this flag is not present, the names returned will not include any dag paths.

-----------------------------------------

fn    : fullName        [boolean] []
    This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The full name of the namespace contains both the namespace path and the base name, but without the leading colon representing the root namespace. For example "ns:ball" is a full name, whereas ":ns:ball" is an absolute name. This mode is affected by the current namespace and relative namespace modes. See also other format modifiers 'baseName', 'absoluteName', etc.

-----------------------------------------

int   : internal        [boolean] []
    This flag is used together with the 'listOnlyDependencyNodes' flag. When this flag is set, the returned list will include internal nodes (for example itemFilters) that are not listed by default.

-----------------------------------------

ir    : isRootNamespace [boolean] []
    Returns true if the namespace is root(":"), false if not.

-----------------------------------------

ls    : listNamespace   [boolean] []
    List the contents of the namespace.

-----------------------------------------

lod   : listOnlyDependencyNodes [boolean] []
    List all dependency nodes in the namespace.

-----------------------------------------

lon   : listOnlyNamespaces [boolean] []
    List all namespaces in the namespace.

-----------------------------------------

p     : parent          [boolean] []
    Display the parent of the namespace. By default, the list returned will not include internal nodes (such as itemFilters). To include the internal nodes, use the 'internal' flag.

-----------------------------------------

r     : recurse         [boolean] []
    Can be specified with 'listNamespace', 'listOnlyNamespaces' or 'listOnlyDependencyNode' to cause the listing to recursively include any child namespaces of the namespaces;

-----------------------------------------

sn    : shortName       [boolean]
    This flag is deprecated and may be removed in future releases of Maya. It is a synonym for the baseName flag. Please use the baseName flag instead.

    """

def preloadRefEd(q=1,e=1,ctl=1,dt="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",lck=1,mlc="string",pnl="string",p="string",sc="script",sf=1,slc="string",sts=1,up=1,ulk=1,upd=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/preloadRefEd.html



-----------------------------------------

preloadRefEd is undoable, queryable, and editable.

This creates an editor for managing which references will be read in (loaded)
and which deferred (unloaded) upon opening a file.


-----------------------------------------


Return Value:

string  Name of editor    
  
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

sc    : selectCommand   [script] ['query', 'edit']
    A script to be executed when an item is selected.

-----------------------------------------

sf    : selectFileNode  [boolean] ['query']
    Query the currently selected load setting. Returns the id of the currently selected load setting. This id can be used as an argument to the selLoadSettings command.

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

def referenceEdit(afe=1,cet="[string, string]",fld=1,r=1,scs=1,ec="string",orn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/referenceEdit.html



-----------------------------------------

referenceEdit is NOT undoable, NOT queryable, and NOT editable.

Use this command to remove and change the modifications which have been
applied to references. A valid commandTarget is either a reference node, a
reference file, a node in a reference, or a plug from a reference. Only
modifications that have been made from the currently open scene can be changed
or removed. The 'referenceQuery -topReference' command can be used to
determine what modifications have been made to a given commandTarget.
Additionally only unapplied edits will be affected. Edits are unapplied when
the node(s) which they affect are unloaded, or when they could not be
successfully applied. By default this command only works on failed edits (this
can be adjusted using the "-failedEdits" and "-successfulEdits" flags).
Specifying a reference node as the command target is equivalent to specifying
every node in the target reference file as a target. In this situation the
results may differ depending on whether the target reference is loaded or
unloaded. When it is unloaded, edits that affect both a node in the target
reference and a node in one of its descendant references may be missed (e.g.
those edits may not be removed). This is because when a reference is unloaded
Maya no longer retains detailed information about which nodes belong to it.
However, edits that only affect nodes in the target reference or in one of its
ancestral references should be removed as expected. When the flags
-removeEdits and -editCommand are used together, by default all connectAttr
edits are removed from the specified source object. To remove only edits that
connect to a specific target object, the target object can be passed as an
additional argument to the command. This narrows the match criteria, so that
only edits that connect the source object to the provided target in this
additional argument are removed. See the example below. NOTE: When specifying
a plug it is important to use the appropriate long attribute name.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

afe   : applyFailedEdits [boolean] []
    Attempts to apply any unapplied edits. This flag is useful if previously failing edits have been fixed using the -changeEditTarget flag. This flag can only be used on loaded references. If the command target is a referenced node, the associated reference is used instead.

-----------------------------------------

cet   : changeEditTarget [[string, string]] []
    Used to change a target of the specified edits. This flag takes two parameters: the old target of the edits, and the new target to change it to. The target can either be a node name ("node"), a node and attribute name ("node.attr"), or just an attribute name (".attr"). If an edit currently affects the old target, it will be changed to affect the new target. Flag 'referenceQuery' should be used to determine the format of the edit targets. As an example most edits store the long name of the attribute (e.g. "translateX"), so when specifying the old target, a long name must also be used. If the short name is specified (e.g. "tx"), chances are the edit won't be retargeted.

-----------------------------------------

fld   : failedEdits     [boolean] []
    This is a secondary flag used to indicate whether or not failed edits should be acted on (e.g. queried, removed, etc...). A failed edit is an edit which could not be successfully applied the last time its reference was loaded. An edit can fail for a variety of reasons (e.g. the referenced node to which it applies was removed from the referenced file). By default failed edits will be acted on.

-----------------------------------------

r     : removeEdits     [boolean] []
    Remove edits which affect the specified unloaded commandTarget.

-----------------------------------------

scs   : successfulEdits [boolean] []
    This is a secondary flag used to indicate whether or not successful edits should be acted on (e.g. queried, removed, etc...). A successful edit is any edit which was successfully applied the last time its reference was loaded. This flag will have no affect if the commandTarget is loaded. By default successful edits will not be acted on.

-----------------------------------------

ec    : editCommand     [string] ['query']
    This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be included. This flag requires a string parameter. Valid values are: "addAttr", "connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr", "lock" and "unlock". In some contexts, this flag may be specified more than once to specify multiple edit types to consider.

-----------------------------------------

orn   : onReferenceNode [string]
    This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports multiple uses when specified with the "exportEdits" command.

    """

def referenceQuery(ch=1,iee=1,il=1,le=1,dp=1,ea=1,en=1,es=1,fld=1,f=1,inr=1,ipo=1,ns=1,n=1,p=1,pns=1,rfn=1,shn=1,sdp=1,sns=1,scs=1,tr=1,un=1,wcn=1,ec="string",orn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/referenceQuery.html



-----------------------------------------

referenceQuery is NOT undoable, NOT queryable, and NOT editable.

Use this command to find out information about references and referenced
nodes. A valid target is either a reference node, a reference file, or a
referenced node. Some flags don't require a target, see flag descriptions for
more information on what effect this has. When a scene contains multiple
levels of file references, those edits which affect a nested reference may be
stored on several different reference nodes. For example: A.ma has a reference
to B.ma which has a reference to C.ma which contains a poly sphere (pSphere1).
If you were to open B.ma and translate the sphere, an edit would be stored on
CRN which refers to a node named "C:pSphere1". If you were then to open A.ma
and parent the sphere, an edit would be stored on BRN which refers to a node
named "B:C:pSphere1". It is important to note that when querying edits which
affect a nested reference, the edits will be returned in the same format that
they were applied. In the above example, opening A.ma and querying all edits
which affect C.ma, would return two edits a parent edit affecting
"B:C:pSphere1", and a setAttr edit affecting "C:pSphere1". Since there is
currently no node named C:pSphere1 (only B:C:pSphere1) care will have to be
taken when interpreting the returned information. The same care should be
taken when referenced DAG nodes have been parented or instanced. Continuing
with the previous example, let's say that you were to open A.ma and, instead
of simply parenting pSphere1, you were to instance it. While A.ma is open,
"B:C:pSphere1" may now be an amibiguous name, replaced by "|B:C:pSphere1" and
"group1|B:C:pSphere1". However querying the edits which affect C.ma would
still return a setAttr edit affecting "C:pSphere1" since it was applied prior
to B:C:pSphere1 being instanced. Some tips: 1\. Use the '-topReference' flag
to query only those edits which were applied from the currently open file. 2\.
Use the '-onReferenceNode' flag to limit the results to those edits where are
stored on a given reference node. You can then use various string manipulation
techniques to extrapolate the current name of any affected nodes.


-----------------------------------------


Return Value:

string[]  For query execution.


-----------------------------------------


Flags:

-----------------------------------------

ch    : child           [boolean] []
    This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to indicate the the children of the target reference will be returned. Returns a string array.

-----------------------------------------

iee   : isExportEdits   [boolean] []
    Returns a boolean indicating whether the specified reference node or file name is an edits file (created with the Export Edits feature)

-----------------------------------------

il    : isLoaded        [boolean] []
    Returns a boolean indicating whether the specified reference node or file name refers to a loaded or unloaded reference.

-----------------------------------------

le    : liveEdits       [boolean] []
    Specifies that the edits should be returned based on the live edits database. Only valid when used in conjunction with the editStrings flag.

-----------------------------------------

dp    : dagPath         [boolean] []
    This flag modifies the '-n/-nodes' flag to indicate that the names of any dag objects returned will include as much of the dag path as is necessary to make the names unique. If this flag is not present, the names returned will not include any dag paths.

-----------------------------------------

ea    : editAttrs       [boolean] []
    Returns string array. A main flag used to query the edits that have been applied to the target. Only the names of the attributes involved in the reference edit will be returned. If an edit involves multiple attributes (e.g. "connectAttr" edits) the nodes will be returned as separate, consecutive entries in the string array. A valid target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to the target. This flag can be used in combination with the '-ea/-editAttrs' flag to indicate that the names of both the involved nodes and attributes will be returned in the format 'node.attribute'.

-----------------------------------------

en    : editNodes       [boolean] []
    Returns string array. A main flag used to query the edits that have been applied to the target. Only the names of the nodes involved in the reference edit will be returned. If an edit involves multiple nodes (e.g. "connectAttr" edits) the nodes will be returned as separate, consecutive entries in the string array. A valid target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to the target. This flag can be used in combination with the '-ea/-editAttrs' flag to indicate that the names of both the involved nodes and attributes will be returned in the format 'node.attribute'.

-----------------------------------------

es    : editStrings     [boolean] []
    Returns string array. A main flag used to query the edits that have been applied to the target. The edit will be returned as a valid MEL command. A valid target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to the target. This flag cannot be used with either the '-en/-editNodes' or '-ea/-editAttrs' flags.

-----------------------------------------

fld   : failedEdits     [boolean] []
    This is a secondary flag used to indicate whether or not failed edits should be acted on (e.g. queried, removed, etc...). A failed edit is an edit which could not be successfully applied the last time its reference was loaded. An edit can fail for a variety of reasons (e.g. the referenced node to which it applies was removed from the referenced file). By default failed edits will not be acted on.

-----------------------------------------

f     : filename        [boolean] []
    Returns string. A main flag used to query the filename associated with the target reference.

-----------------------------------------

inr   : isNodeReferenced [boolean] []
    Returns boolean. A main flag used to determine whether or not the target node comes from a referenced file. true if the target node comes from a referenced file, false if not.

-----------------------------------------

ipo   : isPreviewOnly   [boolean] []
    Returns boolean. This flag is used to determine whether or not the target reference node is only a preview reference node.

-----------------------------------------

ns    : namespace       [boolean] []
    Returns string. This flag returns the full namespace path of the target reference, starting from the root namespace ":". It can be combined with the shortName flag to return just the base name of the namespace.

-----------------------------------------

n     : nodes           [boolean] []
    Returns string array. A main flag used to query the contents of the target reference.

-----------------------------------------

p     : parent          [boolean] []
    This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to indicate the the parent of the target reference will be returned.

-----------------------------------------

pns   : parentNamespace [boolean] []
    A main flag used to query and return the parent namespace of the target reference.

-----------------------------------------

rfn   : referenceNode   [boolean] []
    Returns string. A main flag used to query the reference node associated with the target reference.

-----------------------------------------

shn   : shortName       [boolean] []
    This flag modifies the '-f/-filename' and '-ns/-namespace' flags. Used with the '-f/-filename' flag indicates that the file name returned will be the short name (i.e. just a file name without any directory paths). If this flag is not present, the full name and directory path will be returned. Used with the '-ns/-namespace' flag indicates that the namespace returned will be the base name of the namespace. (i.e. the base name of the full namespace path ":AAA:BBB:CCC" is "CCC" )

-----------------------------------------

sdp   : showDagPath     [boolean] []
    Shows/hides the full dag path for edits. If false only displays the node-name of reference edits. Must be used with the -editNodes, -editStrings or -editAttrs flag.

-----------------------------------------

sns   : showNamespace   [boolean] []
    Shows/hides the namespaces on nodes in the reference edits. Must be used with the -editNodes, -editStrings or -editAttrs flag

-----------------------------------------

scs   : successfulEdits [boolean] []
    This is a secondary flag used to indicate whether or not successful edits should be acted on (e.g. queried, removed, etc...). A successful edit is any edit which was successfully applied the last time its reference was loaded. By default successful edits will be acted on.

-----------------------------------------

tr    : topReference    [boolean] []
    This flag modifies the '-rfn/-referenceNode' flag to indicate the top level ancestral reference of the target reference will be returned.

-----------------------------------------

un    : unresolvedName  [boolean] []
    This flag modifies the '-f/-filename' flag to indicate that the file name returned will be unresolved (i.e. it will be the path originally specified when the file was loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will be returned.

-----------------------------------------

wcn   : withoutCopyNumber [boolean] []
    This flag modifies the '-f/-filename' flag to indicate that the file name returned will not have a copy number (e.g. '{1}') appended to the end. If this flag is not present, the file name returned may have a copy number appended to the end.

-----------------------------------------

ec    : editCommand     [string] ['query']
    This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be included. This flag requires a string parameter. Valid values are: "addAttr", "connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr", "lock" and "unlock". In some contexts, this flag may be specified more than once to specify multiple edit types to consider.

-----------------------------------------

orn   : onReferenceNode [string]
    This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports multiple uses when specified with the "exportEdits" command.

    """

def reloadImage():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/reloadImage.html



-----------------------------------------

reloadImage is undoable, NOT queryable, and NOT editable.

This command reloads an xpm image from disk. This can be used when the file
has changed on disk and needs to be reloaded.

The first string argument is the file name of the .xpm file. The second string
argument is the name of a control using the specified pixmap.


-----------------------------------------


Return Value:

boolean  True if image is successfully loaded, false otherwise.
    """

def requires(dt="string",nt="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/requires.html



-----------------------------------------

requires is undoable, NOT queryable, and NOT editable.

This command is used during file I/O to specify the requirements needed to
load the given file. It defines what file format version was used to write the
file, or what plug-ins are required to load the scene.

The first string names a product (either "maya", or a plug-in name)

The second string gives the version. This command is only useful during file
I/O, so users should not have any need to use this command themselves.

The flags "-nodeType" and "-dataType" specify the node types and data types
defined by the plug-in. When Maya open a scene file, it runs "requires"
command in the file and load required plug-ins. But some plug-ins may be not
loaded because they are missing. The flags "-nodeType" and "-dataType" are
used by the missing plug-ins. If one plug-in is missing, nodes and data
created by this plug-in are created as unknown nodes and unknown data. Maya
records their original types for these unknown nodes and data. When these
nodes and data are saved back to file, it will be possible to determine the
associated missing plug-ins. And when export selected nodes, Maya can write
out the exact required plug-ins. The flags "-nodeType" and "-dataType" is
optional. In this command, if these flags are not given for one plug-in and
the plug-in is missing, the "requires" command of this plug-in will always be
saved back.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

dt    : dataType        [string] []
    Specify a data type defined by this plug-in. The data type is specified by MFnPlugin::registerData() when register the plug-in.

-----------------------------------------

nt    : nodeType        [string]
    Specify a node type defined by this plug-in. The node type is specified by MFnPlugin::registerNode() when register the plug-in.

    """

def saveImage(q=1,e=1,ann="string",bgc="[float, float, float]",cv=1,dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",i="string",io=1,m=1,nbg=1,npm=1,ot="string",p="string",pma=1,po=1,sf="string",sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/saveImage.html



-----------------------------------------

saveImage is undoable, queryable, and editable.

This command creates a static image for non-xpm files. Any image file format
supported by the file texture node is supported by this command.

This command creates a static image control for non-xpm files used to display
a thumbnail image of the scene file.


-----------------------------------------


Return Value:

string  The name of the image created.    
string  The name of the saveImage control created.  
  
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

cv    : currentView     [boolean] ['edit']
    Generate the image from the current view.

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

i     : image           [string] ['query', 'edit']
    Sets the image given the file name.

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

ot    : objectThumbnail [string] ['edit']
    Use an image of the named object, if possible.

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

sf    : sceneFile       [string] ['edit']
    The name of the file that the icon is to be associated with.

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

def sceneEditor(q=1,e=1,ctl=1,dt="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",lck=1,mlc="string",op=1,pnl="string",p="string",rr=1,sc="script",si="int",sr="string",slc="string",shn=1,sts=1,up=1,ulk=1,un=1,upd=1,ut="string",wcn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sceneEditor.html



-----------------------------------------

sceneEditor is undoable, queryable, and editable.

This creates an editor for managing the files in a scene.


-----------------------------------------


Return Value:

string  Name of editor.    
  
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

op    : onlyParents     [boolean] ['query']
    When used with the 'selectItem' or 'selectReference' queries it indicates that, if both a parent and a child file or reference are selected, only the parent will be returned.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

rr    : refreshReferences [boolean] ['edit']
    Force refresh of references

-----------------------------------------

sc    : selectCommand   [script] ['query', 'edit']
    A script to be executed when an item is selected.

-----------------------------------------

si    : selectItem      [int] ['query', 'edit']
    Query or change the currently selected item. When queried, the currently selected file name will be return.

-----------------------------------------

sr    : selectReference [string] ['query']
    Query the currently selected reference. Returns the name of the currently selected reference node.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

shn   : shortName       [boolean] ['query']
    When used with the 'selectItem' query it indicates that the file name returned will be the short name (i.e. just a file name without any directory paths). If this flag is not present, the full name and directory path will be returned.

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

un    : unresolvedName  [boolean] ['query']
    When used with the 'selectItem' query it indicates that the file name returned will be unresolved (i.e. it will be the path originally specified when the file was loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will be returned.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

wcn   : withoutCopyNumber [boolean]
    When used with the 'selectItem' query it indicates that the file name returned will not have a copy number appended to the end. If this flag is not present, the file name returned may have a copy number appended to the end.

    """

def sceneUIReplacement(cl=1,dr=1,gf="[string, string]",gp="[string, string]",gsp="[string, string]",u="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sceneUIReplacement.html



-----------------------------------------

sceneUIReplacement is undoable, NOT queryable, and NOT editable.

This command returns existing scene based UI that can be utilized by the scene
that is being loaded. It can also delete any such UI that is not used by the
loading scene.


-----------------------------------------


Return Value:

string  When used with getNextScriptedPanel, getNextPanel, or getNextFilter


-----------------------------------------


Flags:

-----------------------------------------

cl    : clear           [boolean] []
    Frees any resources allocated by the command.

-----------------------------------------

dr    : deleteRemaining [boolean] []
    Delete any UI that is scene dependent and has not been referenced by this command since the last update.

-----------------------------------------

gf    : getNextFilter   [[string, string]] []
    Returns the next filter of the specified type with the specified name.

-----------------------------------------

gp    : getNextPanel    [[string, string]] []
    Returns the next panel of the specified type, preferably with the specified label.

-----------------------------------------

gsp   : getNextScriptedPanel [[string, string]] []
    Returns the next scripted panel of the specified scripted panel type, preferably with the specified label.

-----------------------------------------

u     : update          [string]
    Updates the state of the command to reflect the current state of the application. The string argument is the name of the main window pane layout holding the panels.

    """

def scriptNode(q=1,e=1,afterScript="string",bs="string",ea=1,eb=1,ire=1,n="string",st="int",stp="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scriptNode.html



-----------------------------------------

scriptNode is undoable, queryable, and editable.

scriptNodes contain scripts that are executed when a file is loaded or when
the script node is deleted. If a script modifies a referenced node, the
changes will be tracked as reference edits unless the scriptNode was created
with the ignoreReferenceEdits flag. The scriptNode command is used to create,
edit, query, and test scriptNodes.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

afterScript : afterScript     [string] ['query', 'edit']
    The script executed when the script node is deleted.   C: The default is an empty string.   Q: When queried, this flag returns a string.

-----------------------------------------

bs    : beforeScript    [string] ['query', 'edit']
    The script executed during file load.   C: The default is an empty string.   Q: When queried, this flag returns a string.

-----------------------------------------

ea    : executeAfter    [boolean] []
    Execute the script stored in the .after attribute of the scriptNode. This script is normally executed when the script node is deleted.

-----------------------------------------

eb    : executeBefore   [boolean] []
    Execute the script stored in the .before attribute of the scriptNode. This script is normally executed when the file is loaded.

-----------------------------------------

ire   : ignoreReferenceEdits [boolean] []
    Sets whether changes made to referenced nodes during the execution of the script should be recorded as reference edits. This flag must be set when the scriptNode is created. If this flag is not set, changes to referenced nodes will be recorded as edits by default.

-----------------------------------------

n     : name            [string] []
    When creating a new scriptNode, this flag specifies the name of the node. If a non-unique name is used, the name will be modified to ensure uniqueness.

-----------------------------------------

st    : scriptType      [int] ['query', 'edit']
    Specifies when the script is executed. The following values may be used: | 0 | Execute on demand.

-----------------------------------------

stp   : sourceType      [string]
    Sets the language type for both the attached scripts. Valid values are "mel" (enabled by default), and "python".

    """

def selLoadSettings(q=1,e=1,ap="string",dr=1,fn="string",ns="uint",pm="string",psf="string",pst="string",pt="string",rfn="string",shn=1,un=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selLoadSettings.html



-----------------------------------------

selLoadSettings is NOT undoable, queryable, and editable.

This command is used to edit and query information about the implicit load
settings. Currently this is primarily intended for internal use within the
Preload Reference Editor. selLoadSettings acts on load setting IDs. When
implict load settings are built for a target scene, there will be one load
setting for each reference in the target scene. Each load setting has a
numerical ID which is its index in a pre-order traversal of the target
reference hierarchy (with the root scenefile being assigned an ID of 0).
Although the IDs are numerical they must be passed to the command as string
array. Example: Given the scene:

    
    
            a
           / \
          b   c
             / \
            d   e
    

where: a references b and c c references d and e the IDs will be as follows: a
= 0 b = 1 c = 2 d = 3 e = 4 selLoadSettings can be used to change the load
state of a reference: whether it will be loaded or unloaded (deferred) when
the target scene is opened. Note: selLoadSettings can accept multiple command
parameters, but the order must be selected carefully such that no reference is
set to the loaded state while its parent is in the unlaoded state. Given the
scene:

    
    
    a
    |
    b [-]
    |
    c [-]
    

where: a references b b references c a = 0 b = 1 c = 2 and b and c are
currently in the unloaded state. The following command will succeed and change
both b and c to the loaded state: selLoadSettings -e -deferReference 0 "1"
"2"; whereas the following command will fail and leave both b and c in the
unloaded state: selLoadSettings -e -deferReference 0 "2" "1"; Bear in mind
that the following command will also change both b and c to the loaded state:
selLoadSettings -e -deferReference 0 "1"; This is because setting a reference
to the loaded state automatically sets all child references to the loaded
state as well. And vice versa, setting a reference the the unloaded state
automatically sets all child reference to the unloaded state.


-----------------------------------------


Return Value:

string  For query execution.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : activeProxy     [string] ['query', 'edit']
    Change or query the active proxy of a proxy set. In query mode, returns the proxyTag of the active proxy; in edit mode, finds the proxy in the proxySet with the given tag and makes it the active proxy.

-----------------------------------------

dr    : deferReference  [boolean] ['query', 'edit']
    Change or query the load state of a reference.

-----------------------------------------

fn    : fileName        [string] ['query']
    Return the file name reference file(s) associated with the indicated load setting(s).

-----------------------------------------

ns    : numSettings     [uint] ['query']
    Return the number of settings in the group of implicit load settings. This is equivalent to number of references in the scene plus 1.

-----------------------------------------

pm    : proxyManager    [string] ['query']
    Return the name(s) of the proxy manager(s) associated with the indicated load setting(s).

-----------------------------------------

psf   : proxySetFiles   [string] ['query']
    Return the name(s) of the proxy(ies) available in the proxy set associated with the indicated load setting(s).

-----------------------------------------

pst   : proxySetTags    [string] ['query']
    Return the name(s) of the proxy tag(s) available in the proxy set associated with the indicated load setting(s).

-----------------------------------------

pt    : proxyTag        [string] ['query']
    Return the name(s) of the proxy tag(s) associated with the indicated load setting(s).

-----------------------------------------

rfn   : referenceNode   [string] ['query']
    Return the name(s) of the reference node(s) associated with the indicated load setting(s).

-----------------------------------------

shn   : shortName       [boolean] ['query']
    Formats the return value of the 'fileName' query flag to only return the short name(s) of the reference file(s).

-----------------------------------------

un    : unresolvedName  [boolean]
    Formats the return value of the 'fileName' query flag to return the unresolved name(s) of the reference file(s). The unresolved file name is the file name used when the reference was created, whether or not that file actually exists on disk. When Maya encounters a file name which does not exist on disk it attempts to resolve the name by looking for the file in a number of other locations. By default the 'fileName' flag will return this resolved value.

    """

def sysFile(cp="string",delete=1,md=1,mov="string",red=1,ren="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sysFile.html



-----------------------------------------

sysFile is undoable, NOT queryable, and NOT editable.

This command provides a system independent way to create a directory or to
rename or delete a file.


-----------------------------------------


Return Value:

boolean  True if successful, false otherwise.


-----------------------------------------


Flags:

-----------------------------------------

cp    : copy            [string] []
    Copy the file to the name given by the newFileName paramter.

-----------------------------------------

delete : delete          [boolean] []
    Deletes the file.

-----------------------------------------

md    : makeDir         [boolean] []
    Create the directory path given in the parameter. This will create the entire path if more than one directory needs to be created.

-----------------------------------------

mov   : move            [string] []
    Behaves identically to the -rename flag and remains for compatibility with old scripts

-----------------------------------------

red   : removeEmptyDir  [boolean] []
    Delete the directory path given in the parameter if the directory is empty. The command will not delete a directory which is not empty.

-----------------------------------------

ren   : rename          [string]
    Rename the file to the name given by the newFileName parameter.

    """

def translator(q=1,dfr=1,do="string",ext=1,cmp="string",f=1,l=1,ld=1,ot=1,os=1,rs=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/translator.html



-----------------------------------------

translator is undoable, queryable, and NOT editable.

Set or query parameters associated with the file translators specified in as
the argument.


-----------------------------------------


Return Value:

boolean  or string array depending upon which flags are specified.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dfr   : defaultFileRule [boolean] ['query']
    Returns the default file rule value, can return "" as well

-----------------------------------------

do    : defaultOptions  [string] ['query']
    Return/set a string of default options used by this translator.

-----------------------------------------

ext   : extension       [boolean] ['query']
    Returns the default file extension for this translator.

-----------------------------------------

cmp   : fileCompression [string] ['query']
    Specifies the compression action to take when a file is saved. Possible values are "compressed", "uncompressed" "asCompressed".

-----------------------------------------

f     : filter          [boolean] ['query']
    Returns the filter string used for this translator.

-----------------------------------------

l     : list            [boolean] ['query']
    Return a string array of all the translators that are loaded.

-----------------------------------------

ld    : loaded          [boolean] ['query']
    Returns true if the given translator is currently loaded.

-----------------------------------------

ot    : objectType      [boolean] ['query']
    This flag is obsolete. This will now return the same results as defaultFileRule going forward.

-----------------------------------------

os    : optionsScript   [boolean] ['query']
    Query the name of the options script to use to post the user options UI. When this script is invoked it will expect the name of the parent layout in which the options will be displayed as well as the name of the callback to be invoked once the apply button has been depressed in the options area.

-----------------------------------------

rs    : readSupport     [boolean] ['query']
    Returns true if this translator supports read operations.

-----------------------------------------

ws    : writeSupport    [boolean]
    Returns true if this translator supports write operations.

    """

def unknownNode(q=1,p=1,rcn=1,rct=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/unknownNode.html



-----------------------------------------

unknownNode is undoable, queryable, and NOT editable.

Allows querying of the data stored for unknown nodes (nodes that are defined
by a plug-in that Maya could not load when loading a scene file).


-----------------------------------------


Return Value:

string[]  in query mode    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

p     : plugin          [boolean] ['query']
    In query mode return the name of the plug-in from which the unknown node originated. If no plug-in then the empty string is returned.

-----------------------------------------

rcn   : realClassName   [boolean] ['query']
    Return the real class name of the node.

-----------------------------------------

rct   : realClassTag    [boolean]
    Return the real class IFF tag of the node.

    """

def unknownPlugin(q=1,dt=1,l=1,nt=1,r=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/unknownPlugin.html



-----------------------------------------

unknownPlugin is undoable, queryable, and NOT editable.

Allows querying of the unknown plug-ins used by the scene, and provides a
means to remove them.


-----------------------------------------


Return Value:

string[]  in query mode    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dt    : dataTypes       [boolean] ['query']
    Returns the data types associated with the given unknown plug-in. This will always be empty for pre-Maya 2014 files.

-----------------------------------------

l     : list            [boolean] ['query']
    Lists the unknown plug-ins in the scene.

-----------------------------------------

nt    : nodeTypes       [boolean] ['query']
    Returns the node types associated with the given unknown plug-in. This will always be empty for pre-Maya 2014 files.

-----------------------------------------

r     : remove          [boolean] []
    Removes the given unknown plug-in from the scene. For Maya 2014 files and onwards, this will fail if node or data types defined by the plug-in are still in use.

-----------------------------------------

v     : version         [boolean]
    Returns the version string of the given unknown plug-in.

    """

def workspace(q=1,act=1,bw="string",cr="string",dir="string",en="string",fr="[string, string]",fre="string",frl=1,f=1,fn=1,l=1,lfw=1,lw=1,n=1,ot="[string, string]",ote="string",otl=1,o=1,pp="string",rfr="string",rve="string",rt="[string, string]",rte="string",rtl=1,rd=1,s=1,sn=1,u=1,ua=1,v="[string, string]",ve="string",vl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/workspace.html



-----------------------------------------

workspace is undoable, queryable, and NOT editable.

Create, open, or edit a workspace associated with a given workspace file.

The string argument represents the workspace. If no workspace is specified
then the current workspace is assumed.

A workspace provides the underlying definition of a Maya Project. Each project
has an associated workspace file, named workspace.mel, which is stored in the
project root directory. The workspace file defines a set of rules that map
file types to their storage, either relative to the project root or as an
absolute location. These rules are used when resolving file paths at runtime.

The workspace command operates directly on the low-level definition of the
workspace to read, change and store the definition to the underlying file. Use
of this command is not generally required, for most purposes it is recommended
that project definition changes be done via the Project Window in the User
Interface. Multiple actions go under the assumption that given paths exist.


-----------------------------------------


Return Value:

string  Project short name when querying the 'shortName' flag.    
string  Project full name when querying the 'fullName' flag.  
string  Current workspace name when querying the 'openWorkspace' flag and
there is a current one.  
string  Working space directory when querying the 'directory' flag.  
string  File rule on the current workspace when querying one of the
'renderTypeEntry', 'fileRuleEntry', or 'objectTypeEntry' flags.  
string  File rule on the current workspace when querying the 'variableEntry'
flag.  
string  Resolved full name of the given file name, or the current root
directory if no name given when querying the 'expandName' flag.  
string  Path to the current project workspace when querying the 'projectPath'
flag.  
string  Current workspace's base workspace name when querying the
'baseWorkspace' flag.  
string  Current workspace's root directory when querying the 'rootDirectory'
flag.  
string[]  List of file rules when querying the 'fileRule' flag.  
string[]  List of variables when querying the 'variableList' flag.  
string[]  List of all workspaces when querying the 'listWorkspaces' flag.  
string[]  List of full names of all workspaces when querying the
'listFullWorkspaces' flag.  
string[]  List of path names for all workspace in the directory named when
querying the 'list' flag or the current workspace if no directory is named.  
string[]  List of alternating (file rule, rule location) strings corresponding
to the current workspace's file rules.  
string[]  List of alternating (variable, value) strings corresponding to the
current workspace's variables.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

act   : active          [boolean] ['query']
    This flag is a synonym for -o/openWorkspace.

-----------------------------------------

bw    : baseWorkspace   [string] ['query']
    A workspace may be based on another workspace. This means that all the file rules and variables in the base workspace apply to this workspace unless they are explicitly overridden. By default, a new workspace has the workspace "default" as it's base workspace. Note that "duplicated" file rules containing relative paths are not verified nor created when creating a new workspace or when changing the base workspace.

-----------------------------------------

cr    : create          [string] []
    Create a new directory. If the directory name is not a full path name, it will be created as a subdirectory of the "current" directory set with the -dir flag. Note that this flag does not create a workspace.

-----------------------------------------

dir   : directory       [string] ['query']
    This option will set the current workspace directory to the path specified. When queried it will return the current workspace directory. This directory is used as an initial directory for the fileBrowser and is part of the search path used for locating files. It should not be confused with the current working directory as used by the pwd and chdir commands. When the file browser is used, it will set this value to the last location navigated to.

-----------------------------------------

en    : expandName      [string] ['query']
    Query for the full path location of a filename using the current workspace definition. The path may be a project relative file name, a full path name or a variable name. The return value is always a full path name. If the path is an empty string, the return value will be the project root directory. Variable expansion is supported, and will consider both variables defined in the workspace as well as environment variables. There are three formats supported for expanding variable names: %variableName%, $variableName, ${variableName}. Maya will first attempt to find matching variables defined in the current workspace, then search for a matching environment variable. The tilde character ('~') is also supported. If a tilde is located at the beginning of a variable, Maya will only consider and expand environment variables, and will leave the tilde in the expanded result. On linux and mac platforms, a tilde can be used to expand a user's home directory, using the form ~username, ~, or ~/. When specified as ~username, it will be replaced with the corresponding user's home directory. When specified as ~ or ~/, it will be replaced with the value of the HOME environment variable.

-----------------------------------------

fr    : fileRule        [[string, string]] ['query']
    Set the default location for a file. The first parameter is the fileRule name(scenes, images, etc) and the second is the location. When queried, it returns a list of strings. The elements of the returned list alternate between fileRule names and the corresponding location. There is typically one file rule for each available translator. Environment variables are supported. You can set multiple path for the file rule by separating them with semicolons (;) on Windows and colons(:) on MacOSX and Linux. Note that whitespace at the beginning and end of each item in the separated sequence is significant and will be included as part of the path name (which is not usually desired unless the pathname does actually start or end with spaces). A valid filerule name cannot contain multiple byte characters. Note that creating a filerule does not create any directories. It is the user's responsibility to ensure that all paths are valid.

-----------------------------------------

fre   : fileRuleEntry   [string] ['query']
    Return the location for the given fileRule.

-----------------------------------------

frl   : fileRuleList    [boolean] ['query']
    Returns a list of the currently defined file rules.

-----------------------------------------

f     : filter          [boolean] []
    This flag is obsolete.

-----------------------------------------

fn    : fullName        [boolean] ['query']
    Return the full name of the workspace.

-----------------------------------------

l     : list            [boolean] ['query']
    This option will list the current workspace directory. If a path is specified for the "workspaceFile" then the contents of that directory will be listed. Otherwise, the contents of the directory set with the -dir flag will be listed.

-----------------------------------------

lfw   : listFullWorkspaces [boolean] ['query']
    Returns a list of the full path names of all the currently defined workspaces.

-----------------------------------------

lw    : listWorkspaces  [boolean] ['query']
    Returns a list of all the currently defined workspace names.

-----------------------------------------

n     : newWorkspace    [boolean] []
    This specifies that a new workspace is being created with a given path (full path or relative to "current" directory). If a workspace with this path already exists, the command will fail. Note that the application is creating a virtual workspace without creating any new directories. If given a relative path, it will map the new workspace to the "current" directory set with the -dir flag concatenated with the given path. If the path does not exist, it will default the workspace root directory -rd to the system's root path (e.g. C:\ or '/'). It is the user's responsibility to ensure that all paths exist.

-----------------------------------------

ot    : objectType      [[string, string]] ['query']
    This flag is obsolete. All default locations will be added to the fileRules going forward.

-----------------------------------------

ote   : objectTypeEntry [string] ['query']
    This flag is obsolete. This will now return the same as fileRuleEntry.

-----------------------------------------

otl   : objectTypeList  [boolean] ['query']
    This flag is obsolete. This will now return the same results as fileRuleList going forward.

-----------------------------------------

o     : openWorkspace   [boolean] ['query']
    Open the workspace. The workspace becomes the current workspace.

-----------------------------------------

pp    : projectPath     [string] ['query']
    Convert filePath passed as argument to a filename that is relative to the project root directory (if possible) and return it. If the filePath is not under the project root directory, a full path name will be returned.

-----------------------------------------

rfr   : removeFileRuleEntry [string] []
    Remove the given file rule from the specified workspace. If the workspace name is not specified, the given file rule will be removed from the current workspace.

-----------------------------------------

rve   : removeVariableEntry [string] []
    Remove the given variable from the specified workspace. If the workspace name is not specified, the given variable will be removed from the current workspace.

-----------------------------------------

rt    : renderType      [[string, string]] ['query']
    This flag is obsolete. All default render types will be added to fileRules going forward.

-----------------------------------------

rte   : renderTypeEntry [string] ['query']
    This flag is obsolete, use fileRuleEntry going forward

-----------------------------------------

rtl   : renderTypeList  [boolean] ['query']
    This flag is obsolete, use fileRuleList going forward.

-----------------------------------------

rd    : rootDirectory   [boolean] ['query']
    Returns the root directory of the workspace.

-----------------------------------------

s     : saveWorkspace   [boolean] []
    Save the workspace. Workspaces are normally saved when Maya exits but this flag will make sure that the data is flushed to disk.

-----------------------------------------

sn    : shortName       [boolean] ['query']
    Query the short name of the workspace.

-----------------------------------------

u     : update          [boolean] []
    This flag reads all the workspace definitions from the project directory. It is used by Maya at startup time to find the available workspaces.

-----------------------------------------

ua    : updateAll       [boolean] []
    This flag is a synonym for -u/update.

-----------------------------------------

v     : variable        [[string, string]] ['query']
    Set or query the value of a project variable. Project variables are used when expanding names. See the -en/expandName flag below.

-----------------------------------------

ve    : variableEntry   [string] ['query']
    Given a variable name, will return its value.

-----------------------------------------

vl    : variableList    [boolean]
    Return a list of all variables in the workspace.

    """

def assignInputDevice(q=1,c="string",ct=1,d="string",im=1,m=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/assignInputDevice.html



-----------------------------------------

assignInputDevice is undoable, queryable, and NOT editable.

This command associates a command string (i.e. a mel script) with the input
device. When the device moves or a button on the device is pressed, the
command string is executed as if you typed it into the window. If the command
string contains the names of buttons or axes of the device, the current value
of these buttons/axes are substituted in. Buttons are reported as booleans and
axes as doubles.

This command is most useful for associating buttons on a device with commands.
For using a device to capture continous movements it is much more efficient to
attach the device directly into the dependency graph.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : clutch          [string] []
    specify a clutch button. This button must be down for the command string to be executed. If no clutch is specified the command string is executed everytime the device state changes

-----------------------------------------

ct    : continuous      [boolean] []
    if this flag is set the command string is continously (once for everytime the device changes state). By default if a clutch button is specified the command string is only executed once when the button is pressed.

-----------------------------------------

d     : device          [string] []
    specify which device to assign the command string.

-----------------------------------------

im    : immediate       [boolean] []
    Immediately executes the command, without using the queue.

-----------------------------------------

m     : multiple        [boolean]
    if this flag is set the other command strings associated with this device are not deleted. By default, when a new command string is attached to the device, all other command strings are deleted.

    """

def attachDeviceAttr(q=1,at="string",ax="string",cam=1,cr=1,ct=1,c="string",d="string",sl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/attachDeviceAttr.html



-----------------------------------------

attachDeviceAttr is undoable, queryable, and NOT editable.

This command associates a device/axis pair with a node/attribute pair. When
the device axis moves, the value of the attribute is set to the value of the
axis. This value can be scaled and offset using the setAttrScale command.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    specify the attribute to attach to

-----------------------------------------

ax    : axis            [string] []
    specify the axis to attach from.

-----------------------------------------

cam   : camera          [boolean] []
    This flag attaches the device/axis to the current camera. The mapping between device axes and camera controls is uses a heuristic based on the device descripton. The interaction is a copy of the mouse camera navigation controls.

-----------------------------------------

cr    : cameraRotate    [boolean] []
    This flag attaches the device/axis to the current cameras rotation controls.

-----------------------------------------

ct    : cameraTranslate [boolean] []
    This flag attaches the device/axis to the current cameras translate controls.

-----------------------------------------

c     : clutch          [string] []
    specify a clutch button. This button must be down for the command string to be executed. If no clutch is specified the command string is executed everytime the device state changes

-----------------------------------------

d     : device          [string] []
    specify which device to assign the command string.

-----------------------------------------

sl    : selection       [boolean]
    This flag attaches to the nodes in the selection list. This is different from the default arguments of the command since changing the selection will change the attachments.

    """

def detachDeviceAttr(q=1,all=1,at="string",ax="string",d="string",sl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/detachDeviceAttr.html



-----------------------------------------

detachDeviceAttr is undoable, queryable, and NOT editable.

This command detaches connections between device axes and node attributes. The
command line arguments are the same as for the corresponding attachDeviceAttr
except for the clutch argument which can not be used in this command.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : all             [boolean] []
    Delete all attachments on every device.

-----------------------------------------

at    : attribute       [string] []
    The attribute to detach. This flag must be used with the -d/device flag.

-----------------------------------------

ax    : axis            [string] []
    The axis to detach. This flag must be used with the -d/device flag.

-----------------------------------------

d     : device          [string] []
    Delete the attachment for this device. If the -ax/axis flag is not used, all of the attachments connected to this device are detached.

-----------------------------------------

sl    : selection       [boolean]
    Detaches selection attachments.

    """

def deviceEditor(q=1,e=1,ctl=1,dt="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",lck=1,mlc="string",pnl="string",p="string",slc="string",sts=1,tp="string",up=1,ulk=1,upd=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deviceEditor.html



-----------------------------------------

deviceEditor is undoable, queryable, and editable.

This creates an editor for creating/modifying attachments to input devices.


-----------------------------------------


Return Value:

string  name of the editor    
  
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

tp    : takePath        [string] ['query', 'edit']
    The path used for writing/reading take data through the editor.

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

def devicePanel(q=1,e=1,ctl=1,cp="string",cs=1,dt="string",dtg="string",es=1,ex=1,init=1,iu=1,l="string",mrl=1,mbv=1,ni=1,p="string",pmp="script",rp="string",to=1,toc="string",tor=1,up=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/devicePanel.html



-----------------------------------------

devicePanel is undoable, queryable, and editable.

This command is now obsolete. It is included only for the purpose of file
compatibility. It creates a blank panel.


-----------------------------------------


Return Value:

string  name of panel    
  
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

def getInputDeviceRange(max=1,min=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getInputDeviceRange.html



-----------------------------------------

getInputDeviceRange is undoable, NOT queryable, and NOT editable.

This command lists the minimum and maximum values the device axis can return.
This value is the raw device values before any mapping is applied. If you
don't specify an axis the values for all axes of the device are returned.


-----------------------------------------


Return Value:

float[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

max   : maxValue        [boolean] []
    list only the maximum value of the axis

-----------------------------------------

min   : minValue        [boolean]
    list only the minimum value of the axis

    """

def getModifiers():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getModifiers.html



-----------------------------------------

getModifiers is undoable, NOT queryable, and NOT editable.

This command returns the current state of the modifier keys. The state of each
modifier can be obtained by testing for the modifier's corresponding bit value
in the return value. Shift is bit 1, Ctrl is bit 3, Alt is bit 4, and bit 5 is
the 'Windows' key on Windows keyboards and the Command key on Mac keyboards.
See the provided example for more details on testing for each modifier's bit
value.


-----------------------------------------


Return Value:

int  indicating which modifier keys are pressed.
    """

def listDeviceAttachments(at="string",ax="string",c="string",d="string",f="string",sl=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listDeviceAttachments.html



-----------------------------------------

listDeviceAttachments is undoable, NOT queryable, and NOT editable.

This command lists the current set of device attachments. The listing is in
the form of the commands required to recreate them. This includes both
attachments and device mappings.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    specify the attribute attachments to list

-----------------------------------------

ax    : axis            [string] []
    specify the axis attachments to list

-----------------------------------------

c     : clutch          [string] []
    List only attachment clutched with this button

-----------------------------------------

d     : device          [string] []
    specify which device attachments to list

-----------------------------------------

f     : file            [string] []
    Specify the name of the file to write out device attachments.

-----------------------------------------

sl    : selection       [boolean] []
    This flag list only attachments on selection

-----------------------------------------

w     : write           [boolean]
    Write out device attachments to a file specified by the -f flag, is set. If -f is not set, it'll write out to a file named for the device.

    """

def listInputDeviceAxes():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listInputDeviceAxes.html



-----------------------------------------

listInputDeviceAxes is undoable, NOT queryable, and NOT editable.

This command lists all of the axes of the specified input device.


-----------------------------------------


Return Value:

string[]  Command result
    """

def listInputDeviceButtons():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listInputDeviceButtons.html



-----------------------------------------

listInputDeviceButtons is undoable, NOT queryable, and NOT editable.

This command lists all of the buttons of the specified input device specified
as an argument.


-----------------------------------------


Return Value:

string[]  Command result
    """

def listInputDevices(f=1,p=1,s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listInputDevices.html



-----------------------------------------

listInputDevices is undoable, NOT queryable, and NOT editable.

This command lists all input devices that maya knows about.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

f     : free            [boolean] []
    List the free devices

-----------------------------------------

p     : primary         [boolean] []
    List the primary devices

-----------------------------------------

s     : secondary       [boolean]
    List the secondary devices

    """

def mouse(esw=1,mbt="int",mbs=1,sws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/mouse.html



-----------------------------------------

mouse is undoable, NOT queryable, and NOT editable.

This command allows to configure mouse.


-----------------------------------------


Return Value:

int  When -scrollWheelStatus flag is used, will return 1 if scroll wheel
support enabled, otherwise 0.  
When -mouseButtonTrackingStatus flag is used, will return the number of mouse
buttons being tracked.


-----------------------------------------


Flags:

-----------------------------------------

esw   : enableScrollWheel [boolean] []
    Enable or disable scroll wheel support.

-----------------------------------------

mbt   : mouseButtonTracking [int] []
    Set the number (1, 2 or 3) of mouse buttons to track.   Note: this is only supported on Macintosh

-----------------------------------------

mbs   : mouseButtonTrackingStatus [boolean] []
    returns the current number of mouse buttons being tracked.

-----------------------------------------

sws   : scrollWheelStatus [boolean]
    returns the current status of scroll wheel support.

    """

def recordAttr(q=1,at="string",d=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/recordAttr.html



-----------------------------------------

recordAttr is undoable, queryable, and NOT editable.

This command sets up an attribute to be recorded. When the record command is
executed, any changes to this attribute are recorded. When recording stops
these changes are turned into keyframes.

If no attributes are specified all attributes of the node are recorded.

When the query flag is used, a list of the attributes being recorded will be
returned.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    specify the attribute to record

-----------------------------------------

d     : delete          [boolean]
    Do not record the specified attributes

    """

def setAttrMapping(q=1,a=1,at="string",ax="string",c="string",d="string",o="float",r=1,s="float",sl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setAttrMapping.html



-----------------------------------------

setAttrMapping is undoable, queryable, and NOT editable.

This command applies an offset and scale to a specified device attachment.
This command is different than the setInputDeviceMapping command, which
applies a mapping to a device axis.

The value from the device is multiplied by the scale and the offset is added
to this product. With an absolute mapping, the attached attribute gets the
resulting value. If the mapping is relative, the resulting value is added to
the previous calculated value. The calculated value will also take into
account the setInputDeviceMapping, if it was defined.

As an example, if the space ball is setup with absolute attachment mappings,
pressing in one direction will cause the attached attribute to get a constant
value. If a relative mapping is used, and the spaceball is pressed in one
direction, the attached attribute will get a constantly increasing (or
constantly decreasing) value.

Note that the definition of relative is different than the definition used by
the setInputDeviceMapping command. In general, both a relative attachment
mapping (this command) and a relative device mapping (setInputDeviceMapping)
should not be used together one the same axis.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    Make the mapping absolute.

-----------------------------------------

at    : attribute       [string] []
    The attribute used in the attachment.

-----------------------------------------

ax    : axis            [string] []
    The axis on the device used in the attachment.

-----------------------------------------

c     : clutch          [string] []
    The clutch button used in the attachment.

-----------------------------------------

d     : device          [string] []
    The device used in the attachment.

-----------------------------------------

o     : offset          [float] []
    Specify the offset value.

-----------------------------------------

r     : relative        [boolean] []
    Make the mapping relative.

-----------------------------------------

s     : scale           [float] []
    Specify the scale value.

-----------------------------------------

sl    : selection       [boolean]
    This flag specifies the mapping should be on the selected objects

    """

def setInputDeviceMapping(a=1,ax="string",d="string",o="float",r=1,s="float",v=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setInputDeviceMapping.html



-----------------------------------------

setInputDeviceMapping is undoable, NOT queryable, and NOT editable.

The command sets a scale and offset for all attachments made to a specified
device axis. Any attachment made to a mapped device axis will have the scale
and offset applied to its values.

The value from the device is multiplied by the scale and the offset is added
to this product. With an absolute mapping, the attached attribute gets the
resulting value. If the mapping is relative, the final value is the offset
added to the scaled difference between the current device value and the
previous device value.

This mapping will be applied to the device data before any mappings defined by
the setAttrMapping command. A typical use would be to scale a device's input
so that it is within a usable range. For example, the device mapping can be
used to calibrate a spaceball to work in a specific section of a scene.

As an example, if the space ball is setup with absolute device mappings,
constantly pressing in one direction will cause the attached attribute to get
a constant value. If a relative mapping is used, and the spaceball is pressed
in one direction, the attached attribute will jump a constantly increasing (or
constantly decreasing) value and will find a rest value equal to the offset.

There are important differences between how the relative flag is handled by
this command and the setAttrMapping command. (See the setAttrMapping
documentation for specifics on how it calculates relative values). In general,
both a relative device mapping (this command) and a relative attachment
mapping (setAttrMapping) should not be used together on the same axis.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    report absolute axis values

-----------------------------------------

ax    : axis            [string] []
    specify the axis to map

-----------------------------------------

d     : device          [string] []
    specify which device to map

-----------------------------------------

o     : offset          [float] []
    specify the axis offset value

-----------------------------------------

r     : relative        [boolean] []
    report the change in axis value since the last sample

-----------------------------------------

s     : scale           [float] []
    specify the axis scale value

-----------------------------------------

v     : view            [boolean] []
    translate the device coordinates into the coordinates of the active camera

-----------------------------------------

w     : world           [boolean]
    translate the device coordinates into world space coordinates

    """

def unassignInputDevice(q=1,c="string",d="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/unassignInputDevice.html



-----------------------------------------

unassignInputDevice is undoable, queryable, and NOT editable.

This command deletes all command strings associated with this device.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : clutch          [string] []
    Only delete command attachments with this clutch.

-----------------------------------------

d     : device          [string]
    Specifies the device to work on.

    """

def getModulePath(mn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getModulePath.html



-----------------------------------------

getModulePath is NOT undoable, NOT queryable, and NOT editable.

Returns the module path for a given module name.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

mn    : moduleName      [string]
    The name of the module whose path you want to retrieve.

    """

def loadModule(a=1,ld="string",sc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/loadModule.html



-----------------------------------------

loadModule is NOT undoable, NOT queryable, and NOT editable.

Maya plug-ins may be installed individually within one of Maya's standard
plug-in directories, or they may be packaged up with other resources in a
"module". Each module resides in its own directory and provides a module
definition file to make Maya aware of the plug-ins it provides. When Maya
starts up it loads all of the module files it finds, making the module's plug-
ins, scripts and other resources available for use. Note that the plug-ins
themselves are not loaded at this time, Maya is simply made aware of them so
that they can be loaded if needed. The loadModule command provides the ability
to list and load any new modules which have been added since Maya started up,
thereby avoiding the need to restart Maya before being able to use them.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

a     : allModules      [boolean] []
    Load all new modules not yet loaded in Maya. New modules are the one returned by the -scan option.

-----------------------------------------

ld    : load            [string] []
    Load the module specified by the module definition file.

-----------------------------------------

sc    : scan            [boolean]
    Rescan module presence. Returns the list of module definition files found and not yet loaded into Maya. Does not load any of these newly found modules, nor change the Maya state.

    """

def loadPlugin(ac="script",a=1,n="string",qt=1,rc="script"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/loadPlugin.html



-----------------------------------------

loadPlugin is undoable, NOT queryable, and NOT editable.

Load plug-ins into Maya. The parameter(s) to this command are either the names
or pathnames of plug-in files. The convention for naming plug-ins is to use a
.so extension on Linux, a .mll extension on Windows and .bundle extension on
Mac OS X. If no extension is provided then the default extension for the
platform will be used. To load a Python plugin you must explicitly supply the
'.py' extension.

If the plugin was specified with a pathname then that is where the plugin will
be searched for. If no pathname was provided then the current working
directory (i.e. the one returned by Maya's 'pwd' command) will be searched,
followed by the directories in the MAYA_PLUG_IN_PATH environment variable.

When the plug-in is loaded, the name used in Maya's internal plug-in registry
for the plug-in information will be the file name with the extension removed.
For example, if you load the plug-in "newNode.mll" the name used in the Maya's
registry will be "newNode". This value as well as that value with either a
".so", ".mll" or ".bundle" extension can be used as valid arguments to either
the unloadPlugin or pluginInfo commands.


-----------------------------------------


Return Value:

string[]  the internal names of the successfully loaded plug-ins


-----------------------------------------


Flags:

-----------------------------------------

ac    : addCallback     [script] []
    Add a MEL or Python callback script to be called after a plug-in is loaded. For MEL, the procedure should have the following signature: global proc procedureName(string $pluginName). For Python, you may specify either a script as a string, or a Python callable object such as a function. If you specify a string, then put the formatting specifier "%s" where you want the name of the plug-in to be inserted. If you specify a callable such as a function, then the name of the plug-in will be passed as an argument.

-----------------------------------------

a     : allPlugins      [boolean] []
    Cause all plug-ins in the search path specified in MAYA_PLUG_IN_PATH to be loaded.

-----------------------------------------

n     : name            [string] []
    Set a user defined name for the plug-ins that are loaded. If the name is already taken, then a number will be added to the end of the name to make it unique.

-----------------------------------------

qt    : quiet           [boolean] []
    Don't print a warning if you attempt to load a plug-in that is already loaded.

-----------------------------------------

rc    : removeCallback  [script]
    Removes a procedure which was previously added with -addCallback.

    """

def moduleInfo(d=1,lm=1,mn="string",p=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/moduleInfo.html



-----------------------------------------

moduleInfo is NOT undoable, NOT queryable, and NOT editable.

Returns information on modules found by Maya.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

d     : definition      [boolean] []
    Returns module definition file name for the module specified by the -moduleName parameter.

-----------------------------------------

lm    : listModules     [boolean] []
    Returns an array containing the names of all currently loaded modules.

-----------------------------------------

mn    : moduleName      [string] []
    The name of the module whose information you want to retrieve. Has to be used with either -definition / -path / -version flags.

-----------------------------------------

p     : path            [boolean] []
    Returns the module path for the module specified by the -moduleName parameter.

-----------------------------------------

v     : version         [boolean]
    Returns the module version for the module specified by the -moduleName parameter.

    """

def openMayaPref(q=1,e=1,el=1,lz=1,ow=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/openMayaPref.html



-----------------------------------------

openMayaPref is undoable, queryable, and editable.

Set or query API preferences.


-----------------------------------------


Return Value:

int  indicates success or failure    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

el    : errlog          [boolean] ['query', 'edit']
    toggles whether or not an error log of failed API method calls will be created. When set to true, a file called "OpenMayaErrorLog" will be created in Maya's current working directory. Each time an API method fails, a detailed description of the error will be written to the file along with a mini-stack trace that indicates the routine that called the failing method. Defaults to false(off).

-----------------------------------------

lz    : lazyLoad        [boolean] ['query', 'edit']
    toggles whether or not plugins will be loaded with the RTLD_NOW flag or the RTLD_LAZY flag of dlopen(3C). If set to true, RTLD_LAZY will be used. In this mode references to functions that cannot be resolved at load time will not be considered an error. However, if one of these symbols is actually dereferenced by the plug-in at run time, Maya will crash. Defaults to false(off).

-----------------------------------------

ow    : oldPluginWarning [boolean]
    toggles whether or not loadPlugin will generate a warning when plug-ins are loaded that were compiled against an older, and possibly incompatible Maya release. Defaults to true(on).

    """

def pluginDisplayFilter(q=1,cls="string",dr=1,ex=1,l="string",lf=1,r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pluginDisplayFilter.html



-----------------------------------------

pluginDisplayFilter is NOT undoable, queryable, and NOT editable.

Register, deregister or query a plugin display filter. Plug-ins can use this
command to register their own display filters which will appear in the 'Show'
menus on Maya's model panels.


-----------------------------------------


Return Value:

string  string[]    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cls   : classification  [string] ['query']
    The classification used to filter objects in Viewport 2.0. This classification is the same as MFnPlugin::registerNode(). If the node was registered with multiple classifications, use the one beginning with "drawdb". The default value of this flag is an empty string (""). It will not filter any objects in Viewport 2.0.

-----------------------------------------

dr    : deregister      [boolean] []
    Deregister a plugin display filter.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true if the specified filter exists, false otherwise. Other flags are ignored.

-----------------------------------------

l     : label           [string] ['query']
    The string to be displayed for this filter in the UI. E.g. in the 'Show' menu of a model panel. The default value of this flag is the same as the plugin display filter name.

-----------------------------------------

lf    : listFilters     [boolean] ['query']
    Returns an array of all plugin display filters.

-----------------------------------------

r     : register        [boolean]
    Register a plugin display filter. The -register is implied if both -register and -deregister flags are missing in create mode. You are responsible for deregistering any filters which you register. Filters are reference counted, meaning that if you register the same filter twice then you will have to deregister it twice as well.

    """

def pluginInfo(q=1,e=1,af=1,aci="string",av=1,a=1,cf=1,cc="script",c="string",cnc=1,ctc=1,d="[string, string]",dn=1,dnt="string",dni="string",dv=1,ddb=1,ik=1,ls=1,lsp=1,lpp=1,l=1,mec=1,n="string",p="string",pu=1,rtr=1,r=1,rm=1,rdr=1,spp=1,sd=1,set=1,t="string",tr=1,uo=1,u=1,vd="string",v=1,wr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pluginInfo.html



-----------------------------------------

pluginInfo is undoable, queryable, and editable.

This command provides access to the plug-in registry of the application. It is
used mainly to query the characteristics of registered plug-ins. Plugins
automatically become registered the first time that they are loaded.

The argument is either the internal name of the plug-in or the path to access
it.


-----------------------------------------


Return Value:

Any  Dependent upon the action requested.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : activeFile      [boolean] ['query']
    Restricts the command to the active file only, not the entire scene. This only affects the dependNode/dn and pluginsInUse/pu flags. For use during export selected.

-----------------------------------------

aci   : animCurveInterp [string] ['query']
    Returns a string array containing the names of all of the animation curve interpolators registered by this plug-in.

-----------------------------------------

av    : apiVersion      [boolean] ['query']
    Returns a string containing the version of the API that this plug-in was compiled with. See the comments in MTypes.h for the details on how to interpret this value.

-----------------------------------------

a     : autoload        [boolean] ['query', 'edit']
    Sets whether or not this plug-in should be loaded every time the application starts up. Returns a boolean in query mode.

-----------------------------------------

cf    : cacheFormat     [boolean] ['query']
    Returns a string array containing the names of all of the registered geometry cache formats

-----------------------------------------

cc    : changedCommand  [script] []
    Adds a callback that will get executed every time the plug-in registry changes. Any other previously registered callbacks will also get called.

-----------------------------------------

c     : command         [string] ['query']
    Returns a string array containing the names of all of the normal commands registered by this plug-in. Constraint, control, context and model editor commands are not included.

-----------------------------------------

cnc   : constraintCommand [boolean] ['query']
    Returns a string array containing the names of all of the constraint commands registered by this plug-in.

-----------------------------------------

ctc   : controlCommand  [boolean] ['query']
    Returns a string array containing the names of all of the control commands registered by this plug-in.

-----------------------------------------

d     : data            [[string, string]] ['query']
    Returns a string array containing the names of all of the data types registered by this plug-in.

-----------------------------------------

dn    : dependNode      [boolean] ['query']
    Returns a string array containing the names of all of the custom nodes types registered by this plug-in.

-----------------------------------------

dnt   : dependNodeByType [string] ['query']
    Returns a string array of all registered node types within a specified class of nodes. Each custom node type registered by a plug-in belongs to a more general class of node types as specified by its MPxNode::Type. The flag's argument is an MPxNode::Type as a string. For example, if you want to list all registered Locator nodes, you should specify kLocatorNode as a argument to this flag.

-----------------------------------------

dni   : dependNodeId    [string] ['query']
    Returns an integer array containing the ids of all of the custom node types registered by this plug-in.

-----------------------------------------

dv    : device          [boolean] ['query']
    Returns a string array containing the names of all of the devices registered by this plug-in.

-----------------------------------------

ddb   : dragAndDropBehavior [boolean] ['query']
    Returns a string array containing the names of all of the drag and drop behaviors registered by this plug-in.

-----------------------------------------

ik    : iksolver        [boolean] ['query']
    Returns a string array containing the names of all of the ik solvers registered by this plug-in.

-----------------------------------------

ls    : listPlugins     [boolean] ['query']
    Returns a string array containing all the plug-ins that are currently loaded.

-----------------------------------------

lsp   : listPluginsPath [boolean] ['query']
    Returns a string array containing the full paths of all the plug-ins that are currently loaded.

-----------------------------------------

lpp   : loadPluginPrefs [boolean] []
    Loads the plug-in preferences (ie. autoload) from pluginPrefs.mel into Maya.

-----------------------------------------

l     : loaded          [boolean] ['query']
    Returns a boolean specifying whether or not the plug-in is loaded.

-----------------------------------------

mec   : modelEditorCommand [boolean] ['query']
    Returns a string array containing the names of all of the model editor commands registered by this plug-in.

-----------------------------------------

n     : name            [string] ['query']
    Returns a string containing the internal name by which the plug-in is registered.

-----------------------------------------

p     : path            [string] ['query']
    Returns a string containing the absolute path name to the plug-in.

-----------------------------------------

pu    : pluginsInUse    [boolean] ['query']
    Returns a string array containing all the plug-ins that are currently being used in the scene.

-----------------------------------------

rtr   : referenceTranslators [boolean] ['query']
    If this flag is used in conjunction with the pluginsInUse/pu flag then it will modify the output. When true it will only show plug-ins currently in use containing translators that are used to load referenced files. When false it will only show plug-ins not containing such translators.

-----------------------------------------

r     : registered      [boolean] ['query']
    Returns a boolean specifying whether or not plug-in is currently registered with the system.

-----------------------------------------

rm    : remove          [boolean] ['edit']
    Removes the given plug-in's record from the registry. There is no return value.

-----------------------------------------

rdr   : renderer        [boolean] ['query']
    Returns a string array containing the names of all of the renderers registered by this plug-in.

-----------------------------------------

spp   : savePluginPrefs [boolean] []
    Saves the plug-in preferences (ie. autoload) out to pluginPrefs.mel

-----------------------------------------

sd    : serviceDescriptions [boolean] ['query']
    If there are services in use, then this flag will return a string array containing short descriptions saying what those services are.

-----------------------------------------

set   : settings        [boolean] ['query']
    Returns an array of values with the loaded, autoload, registered flags

-----------------------------------------

t     : tool            [string] ['query']
    Returns a string array containing the names of all of the tool contexts registered by this plug-in.

-----------------------------------------

tr    : translator      [boolean] ['query']
    Returns a string array containing the names of all of the file translators registered by this plug-in.

-----------------------------------------

uo    : unloadOk        [boolean] ['query']
    Returns a boolean that specifies whether or not the plug-in can be safely unloaded. It will return false if the plug-in is currently in use. For example, if the plug-in adds a new dependency node type, and an instance of that node type is present in the scene, then this query will return false.

-----------------------------------------

u     : userNamed       [boolean] ['query']
    Returns a boolean specifying whether or not the plug-in has been assigned a name by the user.

-----------------------------------------

vd    : vendor          [string] ['query']
    Returns a string containing the vendor of the plug-in.

-----------------------------------------

v     : version         [boolean] ['query']
    Returns a string containing the version the plug-in.

-----------------------------------------

wr    : writeRequires   [boolean]
    Sets whether or not this plug-in should write "requires" command into the saved file. "requires" command could autoload the plug-in when you open or import that saved file. This way, Maya will load the plug-in when a file is being loaded for some specified reason, such as to create a customized UI or to load some plug-in data that is not saved in any node or attributes. For example, "stereoCamera" is using this flag for its customized UI.

    """

def unloadPlugin(ac="script",f=1,rc="script"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/unloadPlugin.html



-----------------------------------------

unloadPlugin is undoable, NOT queryable, and NOT editable.

Unload plug-ins from Maya. After the successful execution of this command,
plug-in services will no longer be available.


-----------------------------------------


Return Value:

string[]  the internal names of the successfully unloaded plug-ins


-----------------------------------------


Flags:

-----------------------------------------

ac    : addCallback     [script] []
    Add a procedure to be called just before a plugin is unloaded. The procedure should have one string argument, which will be the plugin's name.

-----------------------------------------

f     : force           [boolean] []
    Unload the plugin even if it is providing services. This is not recommended. If you unload a plug-in that implements a node or data type in the scene, those instances will be converted to unknown nodes or data and the scene will no longer behave properly. Maya may become unstable or even crash. If you use this flag you are advised to save your scene in MayaAscii format and restart Maya as soon as possible.

-----------------------------------------

rc    : removeCallback  [script]
    Remove a procedure which was previously added with -addCallback.

    """

def displayString(q=1,d=1,ex=1,k=1,r=1,v="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displayString.html



-----------------------------------------

displayString is NOT undoable, queryable, and NOT editable.

Assign a string value to a string identifier. Allows you define a string in
one location and then refer to it by its identifier in many other locations.
Formatted strings are also supported (NOTE however, this functionality is now
provided in a more general fashion by the format command, use of format is
recommended). You may embed up to 3 special character sequences ^1s, ^2s, and
^3s to perform automatic string replacement. The embedded characters will be
replaced with the extra command arguments. See example section for more
detail. Note the extra command arguments do not need to be display string
identifiers.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : delete          [boolean] []
    This flag is used to remove an identifer string. The command will fail if the identifier does not exist.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true or false depending upon whether the specified identifier exists.

-----------------------------------------

k     : keys            [boolean] ['query']
    List all displayString keys that match the identifier string. The identifier string may be a whole or partial key string. The command will return a list of all identifier keys that contain this identifier string as a substring.

-----------------------------------------

r     : replace         [boolean] ['query']
    Since a displayString command will fail if it tries to assign a new value to an existing identifer, this flag is required to allow updates to the value of an already-existing identifier. If the identifier does not already exist, a new identifier is added as if the -replace flag were not present.

-----------------------------------------

v     : value           [string]
    The display string\'s value. If you do not specify this flag when creating a display string then the value will be the same as the identifier.

    """

def format(s="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/format.html



-----------------------------------------

format is NOT undoable, NOT queryable, and NOT editable.

This command takes a format string, where the format string contains format
specifiers. The format specifiers have a number associated with them relating
to which parameter they represent to allow for alternate ordering of the
passed-in values for other languages by merely changing the format string


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

s     : stringArg       [string]
    Specify the arguments for the format string.

    """

def aaf2fcp(df=1,dst="string",gfn="int",pr="int",src="string",t="int",wc="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/aaf2fcp.html



-----------------------------------------

aaf2fcp is NOT undoable, NOT queryable, and NOT editable.

This command is used to convert an aff file to a Final Cut Pro (fcp) xml file
The conversion process can take several seconds to complete and the command is
meant to be run asynchronously


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

df    : deleteFile      [boolean] []
    Delete temporary file. Can only be used with the terminate option

-----------------------------------------

dst   : dstPath         [string] []
    Specifiy a destination path

-----------------------------------------

gfn   : getFileName     [int] []
    Query output file name

-----------------------------------------

pr    : progress        [int] []
    Request progress report

-----------------------------------------

src   : srcFile         [string] []
    Specifiy a source file

-----------------------------------------

t     : terminate       [int] []
    Complete the task

-----------------------------------------

wc    : waitCompletion  [int]
    Wait for the conversion process to complete

    """

def allNodeTypes(ia=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/allNodeTypes.html



-----------------------------------------

allNodeTypes is NOT undoable, NOT queryable, and NOT editable.

This command returns a list containing the type names of every kind of
creatable node registered with the system. Note that some node types are
abstract and cannot be created. These will not show up on this list. (e.g.
transform and polyShape both inherit from dagObject, but dagObject cannot be
created directly so it will not appear on this list.)


-----------------------------------------


Return Value:

string[]  List of node types


-----------------------------------------


Flags:

-----------------------------------------

ia    : includeAbstract [boolean]
    Show every node type, even the abstract ones which cannot be created via the 'createNode' command. These will have the suffix "(abstract)" appended to them in the list.

    """

def audioTrack(q=1,e=1,it="uint",l=1,m=1,nt="uint",ret=1,rt="uint",so=1,st="[uint, uint]",t="string",tr="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/audioTrack.html



-----------------------------------------

audioTrack is undoable, queryable, and editable.

This command is used for inserting and removing tracks related to the audio
clips displayed in the sequencer. It can also be used to modify the track
state, for example, to lock or mute a track.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

it    : insertTrack     [uint] []
    This flag is used to insert a new empty track at the track index specified. Indices are 1-based.

-----------------------------------------

l     : lock            [boolean] ['query', 'edit']
    This flag specifies whether all audio clips on the same track as the specified audio node are to be locked at their current location and track.

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    This flag specifies whether all audio clips on the same track as the specified audio node are to be muted or not.

-----------------------------------------

nt    : numTracks       [uint] ['query']
    To query the number of audio tracks

-----------------------------------------

ret   : removeEmptyTracks [boolean] []
    This flag is used to remove all tracks that have no clips.

-----------------------------------------

rt    : removeTrack     [uint] []
    This flag is used to remove the track with the specified index. The track must have no clips on it before it can be removed.

-----------------------------------------

so    : solo            [boolean] ['query', 'edit']
    This flag specifies whether all audio clips on the same track as the specified audio node are to be soloed or not.

-----------------------------------------

st    : swapTracks      [[uint, uint]] []
    This flag is used to swap the contents of two specified tracks. Indices are 1-based.

-----------------------------------------

t     : title           [string] ['query', 'edit']
    This flag specifies the title for the track.

-----------------------------------------

tr    : track           [uint]
    Specify the track on which to operate by using the track's trackNumber.  In query mode, this flag needs a value.

    """

def cacheFile(q=1,e=1,apf=1,af=1,cfn="string",cf="string",ci="string",cat="string",cnd="string",chi=1,cnm="string",pc2=1,ccn=1,cch="string",dsz=1,dcf=1,dfn=1,dir="string",dtf=1,et="time",f="string",fm="string",gm=1,ia="string",it="string",iet="time",ist="time",nb=1,oa="string",ot="string",pcf="string",pc=1,pts="string",pan="string",p=1,r=1,rcf=1,rws=1,rf="int",spm="int",smr="time",sch=1,st="time",sc=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cacheFile.html



-----------------------------------------

cacheFile is undoable, queryable, and editable.

Creates one or more cache files on disk to store attribute data for a span of
frames. The caches can be created for points/normals on a geometry (using the
pts/points or pan/pointsAndNormals flag), for vectorArray output data (using
the oa/outAttr flag), or for additional node specific data (using the
cnd/cacheableNode flag for those nodes that support it).

When the ia/inAttr flag is used, connects a cacheFile node that associates the
data file on disk with the attribute.

Frames can be replaced/appended to an existing cache with the
rcf/replaceCachedFrame and apf/appendFrame flag. Replaced frames are never
deleted. They are stored in the same directory as the original cache files
with the name provided by the f/fileName flag. If no file name is provided,
the cacheFile name is prefixed with "backup" followed by a unique number.

Single file caches are backed up in their entirety. To revert to an older
version, simply attach to this cache. One file per frame caches only backup
the description file and the frames that were replaced. To recover these types
of caches, the user must rename these files to the original name.


-----------------------------------------


Return Value:

string  name of created cache description file(s)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

apf   : appendFrame     [boolean] []
    Appends data to the cache for the times specified by the startTime and endTime flags. If no time is provided, appends the current time. Must be used in conjunction with the pts/points or cnd/cacheableNode flag. Any overwritten frames will not be deleted, but renamed as specified by the f/fileName flag.

-----------------------------------------

af    : attachFile      [boolean] []
    Used to indicate that rather than creating a cache file, that an existing cache file on disk should be attached to an attribute in the scene. The inAttr flag is used to specify the attribute.

-----------------------------------------

cfn   : cacheFileNode   [string] []
    Specifies the name of the cache file node(s) we are appending/replacing to if more than one cache is attached to the specified geometries.  In query mode, this flag needs a value.

-----------------------------------------

cf    : cacheFormat     [string] ['query']
    Cache file format, default is Maya's .mcx format, but others available via plugin

-----------------------------------------

ci    : cacheInfo       [string] ['query']
    In create mode, used to specify a mel script returning a string array. When creating the cache, this mel script will be executed and the returned strings will be written to the .xml description file of the cache. In query mode, returns descriptive info stored in the cacheFile such as the user name, Maya scene name and maya version number.

-----------------------------------------

cat   : cacheableAttrs  [string] ['query']
    Returns the list of cacheable attributes defined on the accompanying cache node. This argument requires the use of the cacheableNode flag.

-----------------------------------------

cnd   : cacheableNode   [string] []
    Specifies the name of a cacheable node whose contents will be cached. A cacheable node is a node that is specially designed to work with the caching mechanism. An example of a cacheable node is a nCloth node.  In query mode, this flag needs a value.

-----------------------------------------

chi   : channelIndex    [boolean] ['query']
    A query-only flag which returns the channel index for the selected geometry for the cacheFile node specified using the cacheFileNode flag.

-----------------------------------------

cnm   : channelName     [string] ['query']
    When attachFile is used, used to indicate the channel in the file that should be attached to inAttr. If not specified, the first channel in the file is used. In query mode, allows user to query the channels associated with a description file.

-----------------------------------------

pc2   : convertPc2      [boolean] []
    Convert a PC2 file to the Maya cache format (true), or convert Maya cache to pc2 format (false)

-----------------------------------------

ccn   : createCacheNode [boolean] []
    Used to indicate that rather than creating a cache file, that a cacheFile node should be created related to an existing cache file on disk.

-----------------------------------------

cch   : creationChannelName [string] []
    When creating a new cache, this multi-use flag specifies the channels to be cached. The names come from the cacheable channel names defined by the object being cached. If this flag is not used when creating a cache, then all cacheable channels are cached.

-----------------------------------------

dsz   : dataSize        [boolean] ['query']
    This is a query-only flag that returns the size of the data being cached per frame. This flag is to be used in conjunction with the cacheableNode, points, pointsAndNormals and outAttr flags.

-----------------------------------------

dcf   : deleteCachedFrame [boolean] []
    Deletes cached data for the times specified by the startTime/endTime flags. If no time is provided, deletes the current frame. Must be used in conjunction with the pts/points or cnd/cacheableNode flag. Deleted frames will not be removed from disk, but renamed as specified by the f/fileName flag.

-----------------------------------------

dfn   : descriptionFileName [boolean] ['query']
    This is a query-only flag that returns the name of the description file for an existing cacheFile node. Or if no cacheFile node is specified, it returns the description file name that would be created based on the other flags specified.

-----------------------------------------

dir   : directory       [string] ['query']
    Specifies the directory where the cache files will be located. If the directory flag is not specified, the cache files will be placed in the project data directory.

-----------------------------------------

dtf   : doubleToFloat   [boolean] []
    During cache creation, double data is stored in the file as floats. This helps cut down file size.

-----------------------------------------

et    : endTime         [time] []
    Specifies the end frame of the cache range.

-----------------------------------------

f     : fileName        [string] ['query']
    Specifies the base file name for the cache files. If more than one object is being cached and the format is OneFilePerFrame, each cache file will be prefixed with this base file name. In query mode, returns the files associated with the specified cacheFile node. When used with rpf/replaceCachedFrame or apf/appendFrame specifies the name of the backup files. If not specified, replaced frames will be stored with a default name.  In query mode, this flag can accept a value.

-----------------------------------------

fm    : format          [string] []
    Specifies the distribution format of the cache. Valid values are "OneFile" and "OneFilePerFrame"

-----------------------------------------

gm    : geometry        [boolean] ['query']
    A query flag which returns the geometry controlled by the specified cache node

-----------------------------------------

ia    : inAttr          [string] []
    Specifies the name of the attribute that the cache file will drive. This file is optional when creating cache files. If this flag is not used during create mode, the cache files will be created on disk, but will not be driving anything in the scene. This flag is required when the attachFile flag is used.

-----------------------------------------

it    : inTangent       [string] []
    Specifies the in-tangent type when interpolating frames before the replaced frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags. Valid values are "linear", "smooth" and "step".

-----------------------------------------

iet   : interpEndTime   [time] []
    Specifies the frame until which there will be linear interpolation, beginning at endTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flag. Interpolation is achieved by removing frames between endTime and interpEndTime from the cache. Removed frames will be renamed as specified by the f/fileName flag.

-----------------------------------------

ist   : interpStartTime [time] []
    Specifies the frame from which to begin linear interpolation, ending at startTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flags. Interpolation is achieved by removing frames between interpStartTime and startTime from the cache. These removed frames will will be renamed as specified by the f/fileName flag.

-----------------------------------------

nb    : noBackup        [boolean] []
    Specifies that backup files should not be created for any files that may be over-written during append, replace or delete cache frames. Can only be used with the apf/appendFrame, rpf/replaceCachedFrame or dcf/deleteCachedFrame flags.

-----------------------------------------

oa    : outAttr         [string] []
    Specifies the name of the attribute that will be cached to disk.  In query mode, this flag needs a value.

-----------------------------------------

ot    : outTangent      [string] []
    Specifies the out-tangent type when interpolating frames after the replaced frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags. Valid values are "linear", "smooth" and "step".

-----------------------------------------

pcf   : pc2File         [string] []
    Specifies the full path to the pc2 file. Must be used in conjunction with the pc2 flag.

-----------------------------------------

pc    : pointCount      [boolean] ['query']
    A query flag which returns the number of points stored in the cache file. The channelName flag should be used to specify the channel to be queried.

-----------------------------------------

pts   : points          [string] []
    Specifies the name of a geometry whose points will be cached.  In query mode, this flag needs a value.

-----------------------------------------

pan   : pointsAndNormals [string] []
    Specifies the name of a geometry whose points and normals will be cached. The normals is per-vertex per-polygon. The normals cache cannot be imported back to geometry. This flag can only be used to export cache file. It cannot be used with the apf/appendFrame, dcf/deleteCachedFrame and rpf/replaceCachedFrame flags.  In query mode, this flag needs a value.

-----------------------------------------

p     : prefix          [boolean] []
    Indicates that the specified fileName should be used as a prefix for the cacheName.

-----------------------------------------

r     : refresh         [boolean] []
    When used during cache creation, forces a screen refresh during caching. This causes the cache creation to be slower but allows you to see how the simulation is progressing during the cache.

-----------------------------------------

rcf   : replaceCachedFrame [boolean] []
    Replaces cached data for the times specified by the startTime/endTime flags. If no time is provided, replaces cache file for the current time. Must be used in conjunction with the pts/points or cnd/cacheableNode flag. Replaced frames will not be deleted, but renamed as specified by the f/fileName flag.

-----------------------------------------

rws   : replaceWithoutSimulating [boolean] ['edit']
    When replacing cached frames, this flag specifies whether the replacement should come from the cached node without simulating or from advancing time and letting the simulation run. This flag is valid only when neither the startTime nor endTime flags are used or when both the startTime and endTime flags specify the same time value.

-----------------------------------------

rf    : runupFrames     [int] ['query', 'edit']
    Specifies the number of frames of runup to simulate ahead of the starting frame. The value must be greater than or equal to 0. The default is 2.

-----------------------------------------

spm   : sampleMultiplier [int] ['query', 'edit']
    Specifies the sample rate when caches are being created as a multiple of simulation Rate. If the value is 1, then a sample will be cached everytime the time is advanced. If the value is 2, then every other sample will be cached, and so on. The default is 1.

-----------------------------------------

smr   : simulationRate  [time] ['query', 'edit']
    Specifies the simulation rate when caches are being created. During cache creation, the time will be advanced by the simulation rate, until the end time of the cache is reached or surpassed. The value is given in frames. The default value is 1 frame.

-----------------------------------------

sch   : singleCache     [boolean] []
    When used in conjunction with the points, pointsAndNormal or cacheableNode flag, specifies whether multiple geometries should be put into a single cache or to create one cache per geometry (default).

-----------------------------------------

st    : startTime       [time] []
    Specifies the start frame of the cache range.

-----------------------------------------

sc    : staticCache     [boolean] ['query']
    If false, during cache creation, do not save a cache for the object if it appears to have no animation or deformation. If true, save a cache even if the object appears to have no animation or deformation. Default is true. In query mode, when supplied a shape, the flag returns true if the shape appears to have no animation or deformation.

-----------------------------------------

ws    : worldSpace      [boolean]
    If the points flag is used, turning on this flag will result in the world space positions of the points being written. The expected use of this flag is for cache export.

    """

def cacheFileCombine(q=1,e=1,ci=1,cnm="string",cc="string",kw=1,ln=1,na=1,obj="string",oi="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cacheFileCombine.html



-----------------------------------------

cacheFileCombine is undoable, queryable, and editable.

Creates a cacheBlend node that can be used to combine, layer or blend multiple
cacheFiles for a given object.


-----------------------------------------


Return Value:

string  Name of created cache layer node(s)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ci    : cacheIndex      [boolean] ['query']
    A query only flag that returns the index related to the cache specified with the connectCache flag.

-----------------------------------------

cnm   : channelName     [string] ['edit']
    Used in conjunction with the connectCache flag to indicate the channel(s) that should be connected. If not specified, the first channel in the file is used.

-----------------------------------------

cc    : connectCache    [string] ['query', 'edit']
    An edit flag that specifies a cacheFile node that should be connected to the next available index on the specified cacheBlend node. As a query flag, it returns a string array containing the cacheFiles that feed into the specified cacheBlend node.  In query mode, this flag can accept a value.

-----------------------------------------

kw    : keepWeights     [boolean] ['edit']
    This is a flag for use in combination with the connectCache flag only. By default, the connectCache flag will set all weights other than the newly added cacheWeight to 0 so that the new cache gets complete control. This flag disables that behavior so that all existing blend weights are retained.

-----------------------------------------

ln    : layerNode       [boolean] ['query']
    A query flag that returns a string array of the existing cacheBlends on the selected object(s). Returns an empty string array if no cacheBlends are found.

-----------------------------------------

na    : nextAvailable   [boolean] ['query']
    A query flag that returns the next available index on the selected cacheBlend node.

-----------------------------------------

obj   : object          [string] ['query']
    This flag is used in combination with the objectIndex flag. It is used to specify the object whose index you wish to query.  In query mode, this flag needs a value.

-----------------------------------------

oi    : objectIndex     [int]
    In edit mode, used in conjunction with the connectCache flag to indicate the objectIndex to be connected. In query mode, returns the index related to the object specified with the object flag.

    """

def cacheFileMerge(q=1,e=1,et="time",g=1,st="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cacheFileMerge.html



-----------------------------------------

cacheFileMerge is undoable, queryable, and editable.

If selected/specified caches can be successfully merged, will return the
start/end frames of the new cache followed by the start/end frames of any gaps
in the merged cache for which no data should be written to file. In query
mode, will return the names of geometry associated with the specified cache
file nodes.


-----------------------------------------


Return Value:

float[]  The start and end times of merged cache followed by start/end of any
gaps    
string[]  Names of geometry associated with specified cache in query mode.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

et    : endTime         [time] []
    Specifies the end frame of the merge range. If not specified, will figure out range from times of caches being merged.

-----------------------------------------

g     : geometry        [boolean] ['query']
    Query-only flag used to find the geometry nodes associated with the specified cache files.

-----------------------------------------

st    : startTime       [time]
    Specifies the start frame of the merge range. If not specified, will figure out range from the times of the caches being merged.

    """

def cacheFileTrack(q=1,e=1,it="uint",l=1,m=1,ret=1,rt="uint",so=1,t="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cacheFileTrack.html



-----------------------------------------

cacheFileTrack is undoable, queryable, and editable.

This command is used for inserting and removing tracks related to the caches
displayed in the trax editor. It can also be used to modify the track state,
for example, to lock or mute a track.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

it    : insertTrack     [uint] []
    This flag is used to insert a new empty track at the track index specified.

-----------------------------------------

l     : lock            [boolean] ['query', 'edit']
    This flag specifies whether clips on a track are to be locked or not.

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    This flag specifies whether clips on a track are to be muted or not.

-----------------------------------------

ret   : removeEmptyTracks [boolean] []
    This flag is used to remove all tracks that have no clips.

-----------------------------------------

rt    : removeTrack     [uint] []
    This flag is used to remove the track with the specified index. The track must have no clips on it before it can be removed.

-----------------------------------------

so    : solo            [boolean] ['query', 'edit']
    This flag specifies whether clips on a track are to be soloed or not.

-----------------------------------------

t     : track           [uint]
    Used to specify a new track index for a cache to be displayed. Track- indices are 1-based.

    """

def clearCache(all=1,c=1,d=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/clearCache.html



-----------------------------------------

clearCache is NOT undoable, NOT queryable, and NOT editable.

Even though dependency graph values are computed or dirty they may still
occupy space temporarily within the nodes. This command goes in to all of the
data that can be regenerated if required and removes it from the caches
(datablocks), thus clearing up space in memory.


-----------------------------------------


Return Value:

int  Number of items removed from caches


-----------------------------------------


Flags:

-----------------------------------------

all   : allNodes        [boolean] []
    If toggled then all nodes in the graph are cleared. Otherwise only those nodes that are selected are cleared.

-----------------------------------------

c     : computed        [boolean] []
    If toggled then remove all data that is computable. (Warning: If the data is requested for redraw then the recompute will immediately fill the data back in.)

-----------------------------------------

d     : dirty           [boolean]
    If toggled then remove all heavy data that is dirty.

    """

def convertUnit(f="string",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/convertUnit.html



-----------------------------------------

convertUnit is undoable, NOT queryable, and NOT editable.

This command converts values between different units of measure. The command
takes a string, because a string can incorporate unit names as well as values
(see examples).


-----------------------------------------


Return Value:

float  or string


-----------------------------------------


Flags:

-----------------------------------------

f     : fromUnit        [string] []
    The unit to convert from. If not supplied, it is assumed to be the system default. The from unit may also be supplied as part of the value e.g. 11.2m (11.2 meters).

-----------------------------------------

t     : toUnit          [string]
    The unit to convert to. If not supplied, it is assumed to be the system default

    """

def crashInfo(q=1,cf=1,sbc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/crashInfo.html



-----------------------------------------

crashInfo is undoable, queryable, and NOT editable.

Provides an interface to the crash file information.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cf    : crashFile       [boolean] ['query']
    Return the crash file full path name.

-----------------------------------------

sbc   : savedBeforeCrash [boolean]
    Return the saved file full path name before crash.

    """

def dagObjectCompare(a=1,b="string",c=1,n="string",r=1,s=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dagObjectCompare.html



-----------------------------------------

dagObjectCompare is NOT undoable, NOT queryable, and NOT editable.

dagObjectCompare can be used to compare to compare objects based on:

  * type - Currently supports transform nodes and shape nodes
  * relatives - Compares DAG objects' children and parents
  * connections - Checks to make sure the two dags are connected to the same sources and destinations
  * attributes - Checks to make sure that the properties of active attributes are the same


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : attribute       [boolean] []
    Compare dag object attributes

-----------------------------------------

b     : bail            [string] []
    Bail on first error or bail on category. Legal values are "never", "first", and "category".

-----------------------------------------

c     : connection      [boolean] []
    Compare dag connections

-----------------------------------------

n     : namespace       [string] []
    The baseline namespace

-----------------------------------------

r     : relative        [boolean] []
    dag relatives

-----------------------------------------

s     : short           [boolean] []
    Compress output to short form (not as verbose)

-----------------------------------------

t     : type            [boolean]
    Compare based on dag object type

    """

def date(d=1,f="string",sd=1,st=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/date.html



-----------------------------------------

date is NOT undoable, NOT queryable, and NOT editable.

Returns information about current time and date. Use the predefined formats,
or the -format flag to specify the output format.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

d     : date            [boolean] []
    Returns the current date. Format is YYYY/MM/DD

-----------------------------------------

f     : format          [string] []
    Specifies a string defining how the date and time should be represented. All occurences of the keywords below will be replaced with the corresponding values:  | Keyword| Becomes

-----------------------------------------

sd    : shortDate       [boolean] []
    Returns the current date. Format is MM/DD

-----------------------------------------

st    : shortTime       [boolean] []
    Returns the current time. Format is hh:mm

-----------------------------------------

t     : time            [boolean]
    Returns the current time. Format is hh:mm:ss

    """

def dbcount(enabled=1,f="string",k="string",l=1,md="uint",quick=1,r=1,s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dbcount.html



-----------------------------------------

dbcount is NOT undoable, NOT queryable, and NOT editable.

The dbcount command is used to print and manage a list of statistics collected
for counting operations. These statistics are displayed as a list of hits on a
particular location in code, with added reference information for
pointers/strings/whatever. If -reset is not specified then statistics are
printed.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

e     : enabled         [boolean] []
    Set the enabled state of the counters ('on' to enable, 'off' to disable). Returns the list of all counters affected.

-----------------------------------------

f     : file            [string] []
    Destination file of the enabled count objects. Use the special names stdout and stderr to redirect to your command window. As well, the special name msdev is available on NT to direct your output to the debug tab in the output window of Developer Studio.

-----------------------------------------

k     : keyword         [string] []
    Print only the counters whose name matches this keyword (default is all).

-----------------------------------------

l     : list            [boolean] []
    List all available counters and their current enabled status. (The only thing you can do when counters are disabled.)

-----------------------------------------

md    : maxdepth        [uint] []
    Maximum number of levels down to traverse and report. 0 is the default and it means continue recursing as many times as are requested.

-----------------------------------------

q     : quick           [boolean] []
    Display only a summary for each counter type instead of the full details.

-----------------------------------------

r     : reset           [boolean] []
    Reset all counters back to 0 and remove all but the top level counters. Returns the list of all counters affected.

-----------------------------------------

s     : spreadsheet     [boolean]
    Display in spreadsheet format instead of the usual nested braces. This will include a header row that contains 'Count Level1 Level2 Level3...', making the data suitable for opening directly in a spreadsheet table.

    """

def dbfootprint(q=1,all=1,of="string",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dbfootprint.html



-----------------------------------------

dbfootprint is NOT undoable, queryable, and NOT editable.

This command lets you explore the memory usage of specific parts of the scene.
Query the 'type' flag to see what all of the different types are, and query a
specific type to get a description of what information it will provide. All
output is in JSON format so that it can easily be processed and formatted to
highlight areas of interest.


-----------------------------------------


Return Value:

string  JSON data representing the memory usage of the requested objects    
string[]  List of types for which footprint measurements can be made (Query
with no flags)  
string  Description of what a particular type will measure (Query with a
'type' flag)  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : allObjects      [boolean] []
    Ignore any specified or selected objects and measure all applicable objects. The definition of "allObjects" will vary based on the type of objects being measured - see the type documentation for details on what it means for that type. By default if no objects are selected or specified then it will behave as though this flag were set.

-----------------------------------------

of    : outputFile      [string] []
    Specify the location of a file to which the information is to be dumped. Default will return the value from the command. Use the special names stdout, cout, stderr, or cerr to redirect to the standard output or error locations.

-----------------------------------------

t     : type            [string]
    Specify the type of object footprint to measure. The various types are registered at run time and can be listed by querying this flag without a value. If you query it with a value then you get a description of what that particular type is going to measure.  In query mode, this flag can accept a value.

    """

def dbmessage(f="string",l=1,m=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dbmessage.html



-----------------------------------------

dbmessage is NOT undoable, NOT queryable, and NOT editable.

The dbmessage command is used to install monitors for certain message types,
dumping debug information as they are sent so that the flow of messages can be
examined.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

f     : file            [string] []
    Destination file of the message monitoring information. Use the special names stdout and stderr to redirect to your command window. As well, the special name msdev is available on NT to direct your output to the debug tab in the output window of Developer Studio. Default value is stdout.

-----------------------------------------

l     : list            [boolean] []
    List all available message types and their current enabled status.

-----------------------------------------

m     : monitor         [boolean] []
    Set the monitoring state of the message type ('on' to enable, 'off' to disable). Returns the list of all message types being monitored after the change in state.

-----------------------------------------

t     : type            [string]
    Monitor only the messages whose name matches this keyword (default is all).

    """

def dbpeek(q=1,all=1,a="string",c="uint",eg=1,op="string",of="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dbpeek.html



-----------------------------------------

dbpeek is NOT undoable, queryable, and NOT editable.

The dbpeek command is used to analyze the Maya data for information of
interest. See a description of the flags for details on what types of things
can be analyzed.


-----------------------------------------


Return Value:

string[]  Query of operation yields a string array with available operations    
string[]  Query of argument yields a string array with available argument
definitions on the specified operation  
string  Query of specific operation without an output file returns a string
with help information for that operation  
int  Query of specific operation with an output file dumps the help
information for that operation to that file and returns the number of errors
encountered  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

all   : allObjects      [boolean] ['query']
    Ignore any specified or selected objects and peek into all applicable objects. The definition of "allObjects" will vary based on the peek operation being performed - see the flag documentation for details on what it means for a given operation. By default if no objects are selected or specified then it will behave as though this flag were set.

-----------------------------------------

a     : argument        [string] ['query']
    Specify one or more arguments to be passed to the operation. The acceptable values for the argument string are documented in the flag to which they will be applied. If the argument itself takes a value then the value will be of the form "argname=argvalue".  In query mode, this flag needs a value.

-----------------------------------------

c     : count           [uint] ['query']
    Specify a count to be used by the test. Different tests make different use of the count, query the operation to find out how it interprets the value. For example a performance test might use it as the number of iterations to run in the test, an output operation might use it to limit the amount of output it produces.

-----------------------------------------

eg    : evaluationGraph [boolean] ['query']
    Ignore any nodes that are not explicitly part of the evaluation graph. Usually this means nodes that are affected either directly or indirectly by animation. May also tailor the operation to be EM-specific in the areas where the structure of the DG differs from the structure of the EM, for example, plug configurations. This is a filter on the currently selected nodes, including the use of the "allObjects" flag.

-----------------------------------------

op    : operation       [string] ['query']
    Specify the peeking operation to perform. The various operations are registered at run time and can be listed by querying this flag without a value. If you query it with a value then you get the detail values that peek operation accepts and a description of what it does.  In query mode, this flag can accept a value.

-----------------------------------------

of    : outputFile      [string]
    Specify the location of a file to which the information is to be dumped. Default will return the value from the command. Use the special names stdout and stderr to redirect to your command window. The special name msdev is available when debugging on Windows to direct your output to the debug tab in the output window of Visual Studio.

    """

def dbtrace(q=1,f="string",i=1,k="string",m=1,off=1,o="string",tm=1,t="string",v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dbtrace.html



-----------------------------------------

dbtrace is NOT undoable, queryable, and NOT editable.

The dbtrace command is used to manipulate trace objects. The keyword is the
only mandatory argument, indicating which trace object is to be altered.

  * Trace Objects to affect (keyword KEY)
  * Optional filtering criteria (filter FILTER)
  * Function (off, output FILE, mark, title TITLE, timed : default operation is to enable traces)

You can use the query mode to find out which keywords are currently active
(query with no arguments) or inactive (query with the off argument). You can
enhance that query with or without a keyword argument to find out where their
output is going (query with the output argument), out what filters are
currently applied (query with the filter argument), or if their output will be
timestamped (query with the timed argument).


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

f     : filter          [string] ['query']
    Set the filter object for these trace objects (see 'dgfilter')

-----------------------------------------

i     : info            [boolean] ['query']
    In query mode return a brief description of the trace object.

-----------------------------------------

k     : keyword         [string] ['query']
    Keyword of the trace objects to affect  In query mode, this flag can accept a value.

-----------------------------------------

m     : mark            [boolean] []
    Display a mark for all outputs of defined trace objects

-----------------------------------------

      : off             [boolean] []
    Toggle the traces off. If omitted it will turn them on.

-----------------------------------------

o     : output          [string] ['query']
    Destination file of the affected trace objects. Use the special names stdout and stderr to redirect to your command window. The special name msdev is available on Windows to direct your output to the debug tab in the output window of Visual Studio.

-----------------------------------------

tm    : timed           [boolean] ['query']
    Turn on/off timing information in the output of the specified trace objects.

-----------------------------------------

t     : title           [string] []
    Display a title mark for all outputs of defined trace objects

-----------------------------------------

v     : verbose         [boolean]
    Include all traces in output and filter queries, not just those turned on.

    """

def dgdirty(q=1,a=1,c=1,i=1,l="string",p=1,st=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dgdirty.html



-----------------------------------------

dgdirty is NOT undoable, queryable, and NOT editable.

The dgdirty command is used to force a dependency graph dirty message on a
node or plug. Used for debugging to find evaluation problems. If no nodes are
specified then the current selection list is used. If the list flag is used it
will return the list of things currently marked as dirty (or clean if the
clean flag was also used). The returned values will be the names of plugs
either clean/dirty themselves, at both ends of a clean/dirty connection, or
representing the location of clean/dirty data on the node. Be careful using
this option in conjunction with the all flag, the list could be huge.


-----------------------------------------


Return Value:

string[]  List of dirty/clean plugs in list plug mode.    
string[]  List of plugs with dirty/clean data in list data mode.  
string[]  Pairs of dirty/clean connected plugs in list connection mode.  
int  Number of dirty/clean messages sent out in normal mode.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : allPlugs        [boolean] ['query']
    Ignore the selected or specified objects and dirty (or clean) all plugs.

-----------------------------------------

c     : clean           [boolean] ['query']
    If this flag is set then the attributes are cleaned. Otherwise they are set to dirty.

-----------------------------------------

i     : implicit        [boolean] ['query']
    If this flag is set then allow the implicit or default nodes to be processed as well. Otherwise they will be skipped for efficiency.

-----------------------------------------

l     : list            [string] ['query']
    When this flag is specified then instead of sending out dirty/clean messages the list of currently dirty/clean objects will be returned. The allPlugs and clean flags are respected to narrow guide the values to be returned. The value of the flag tells what will be reported.    * "data" or "d" = show plugs that have dirty/clean data   * "plug" or "p" = show plugs that have dirty/clean states   * "connection" or "c" = show plugs with connections that have dirty/clean states Query this flag to find all legal values of the flag. Query this flag with its value already set to get a description of what that value means.  Note that "p" and "c" modes are restricted to plugs that have connections or non-standard state information. Other attributes will not have state information to check, though they will have data. In the case of array attributes only the children that have values currently set will be considered. No attempt will be made to evaluate them in order to update the available child lists. e.g. if you have a DAG with transform T1 and shape S1 the instanced attribute S1.wm[0] will be reported. If in a script you create a second instance T2->S1 and immediately list the plugs again before evaluation you will still only see S1.wm[0]. The new S1.wm[1] won't be reported until it is created through an evaluation, usually caused by refresh, a specific getAttr command, or an editor update. Note that the list is only for selected nodes. Unlike when dirty messages are sent this does not travel downstream.

-----------------------------------------

p     : propagation     [boolean] ['query']
    If this flag is set then the ability of dirty messages to flow through the graph is left enabled.

-----------------------------------------

st    : showTiming      [boolean] ['query']
    If this flag is used then show how long the dirty messages took to propagate.

-----------------------------------------

v     : verbose         [boolean]
    Prints out all of the plugs being set dirty on stdout.

    """

def dgeval(src=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dgeval.html



-----------------------------------------

dgeval is undoable, NOT queryable, and NOT editable.

The dgeval command is used to force a dependency graph evaluate of a node or
plug. Used for debugging to find propagation problems.

Normally the selection list is used to determine which objects to evaluate,
but you can add to the selection list by specifying which objects you want on
the command line.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

src   : src             [boolean] []
    This flag is obsolete. Do not use.

-----------------------------------------

v     : verbose         [boolean]
    If this flag is used then the results of the evaluation(s) is/are printed on stdout.

    """

def dgfilter(atr="string",l=1,logicalAnd="[string, string]",logicalNot="string",logicalOr="[string, string]",n="string",nd="string",nt="string",p="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dgfilter.html



-----------------------------------------

dgfilter is NOT undoable, NOT queryable, and NOT editable.

The dgfilter command is used to define Dependency Graph filters that select DG
objects based on certain criteria. The command itself can be used to filter
objects or it can be attached to a dbtrace object to selectively filter what
output is traced. If objects are specified then apply the filter to those
objects and return a boolean indicating whether they passed or not, otherwise
return then name of the filter. An invalid filter will pass all objects. For
multiple objects the return value is the logical "AND" of all object's return
values.


-----------------------------------------


Return Value:

string  if creating filter or getting filter info    
string[]  if listing filters  
boolean  if applying filter


-----------------------------------------


Flags:

-----------------------------------------

atr   : attribute       [string] []
    Select objects whose attribute names match the pattern.

-----------------------------------------

l     : list            [boolean] []
    List the available filters. If used in conjunction with the -name flag it will show a description of what the filter is.

-----------------------------------------

logicalAnd : logicalAnd      [[string, string]] []
    Logical AND of two filters.

-----------------------------------------

logicalNot : logicalNot      [string] []
    Logical inverse of filter.

-----------------------------------------

logicalOr : logicalOr       [[string, string]] []
    Logical OR of two filters.

-----------------------------------------

n     : name            [string] []
    Use filter named FILTER (or create new filter with that name). If no objects are specified then the name given to the filter will be returned.

-----------------------------------------

nd    : node            [string] []
    Select objects whose node names match the pattern.

-----------------------------------------

nt    : nodeType        [string] []
    Select objects whose node type names match the pattern.

-----------------------------------------

p     : plug            [string]
    Select objects whose plug names match the pattern.

    """

def dgInfo(all=1,c=1,d=1,n=1,nd=1,of="string",p=1,s=1,sz=1,sub=1,nt="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dgInfo.html



-----------------------------------------

dgInfo is NOT undoable, NOT queryable, and NOT editable.

This command prints information about the DG in plain text. The scope of the
information printed is the entire graph if the all flag is used, the
nodes/plugs on the command line if they were specified, and the selection
list, in that order. Each plug on a connection will have two pieces of state
information displayed together at the end of the line on which they are
printed. There are two possible values for each of the two states displayed.
The values are updated when the DG pulls data across them, usually through
evaluation, or pushes a dirty message through them. There are some subtleties
in how the data is pulled through the connection but for simplicity it will be
referred to as "evaluation". The values displayed will be CLEAN or DIRTY
followed by PROP or BLOCK. The first keyword has these meanings:

  1. CLEAN means that evaluation of the plug's connection succeeded and no dirty messages have come through it since then. It also implies that the destination end of the connection has received the value from the source end. 
  2. DIRTY means that a dirty message has passed through the plug's connection since the last time an evaluation was made on the destination side of that connection. 

Note: the data on the node has its own dirty state that depends on other
factors so having a clean connection doesn't necessarily mean the plug's data
is clean, and vice versa. The second keyword has these meanings:

  1. PROP means that the connection will allow dirty messages to pass through and forwards them to all destinations. 
  2. BLOCK means that a dirty message will stop at this connection and not continue on to any destinations. This is an optimization that prevents excessive dirty flag propagation when many values are changing, for example, a frame change in an animated sequece. 

The combination CLEAN BLOCK should never be seen in a valid DG. This indicates
that while the plug connection has been evaluated since the last dirty message
it will not propagate any new dirty messages coming in to it. That in turn
means downstream nodes will not be notified that the graph is changing and
they will not evaluate properly. Recovering from this invalid state requires
entering the command dgdirty -a to mark everything dirty and restart proper
evaluation. Think of this command as the reset/reboot of the DG world. Both
state types behave differently depending on your connection type.

  1. Simple A -> B : Plugs at both ends of the connection share the same state information. The state information updates when an evaluation request comes to A from B, or a dirty message is sent from A to B. 
  2. Fan-Out A -> B, A -> C : Each of A, B, and C have their own unique state information. B and C behave as described above. A has its state information linked to B and C - it will have CLEAN only when both B and C have CLEAN, it will have BLOCK only when both B and C have BLOCK. 
  3. In-Out A -> B, C -> A : Each of A, B, and C have their own unique state information. B and C behave as described above. A has its state information linked to B and C. The CLEAN|DIRTY flag looks backwards, then forwards: 
    
        if( C == CLEAN ) A = CLEAN
    else if( B == CLEAN ) A = CLEAN
    

The BLOCK state is set when a dirty message passes through A, and the PROP
state is set either when A is set clean or an evaluation passes through A.

There are some other exceptions to these rules:

  1. All of this state change information only applies to dirty messages and evaluations that use the normal context. Any changes in other contexts, for example, through the getAttr -t TIME command, does not affect the state in the connections. 
  2. Param curves and other passive inputs, for example blend nodes coming from param curves, will not disable propagation. Doing so would make the keyframing workflow impossible. 
  3. Certain messages can choose to completely ignore the connection state information. For example when a node's state attribute changes a connection may change to a blocking one so the message has to be propagated at least one step further to all of its destinations. This way they can update their information. 
  4. Certain operations can globally disable the use of the propagaton state to reduce message flow. The simplest example is when the evaluation manager is building its graph. It has to visit all nodes so the propagation cannot be blocked. 
  5. The messaging system has safeguards against cyclic messages flowing through connections but sometimes a message bypasses the connection completely and goes directly to the node. DAG parents do this to send messages to their children. So despite connections into a node all having the BLOCK state it could still receive dirty messages.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

all   : allNodes        [boolean] []
    Use the entire graph as the context

-----------------------------------------

c     : connections     [boolean] []
    Print the connection information

-----------------------------------------

d     : dirty           [boolean] []
    Only print dirty/clean nodes/plugs/connections. Default is both

-----------------------------------------

n     : nodes           [boolean] []
    Print the specified nodes (or the entire graph if -all is used)

-----------------------------------------

nd    : nonDeletable    [boolean] []
    Include non-deletable nodes as well (normally not of interest)

-----------------------------------------

of    : outputFile      [string] []
    Send the output to the file FILE instead of STDERR

-----------------------------------------

p     : propagation     [boolean] []
    Only print propagating/not propagating nodes/plugs/connections. Default is both.

-----------------------------------------

s     : short           [boolean] []
    Print using short format instead of long

-----------------------------------------

sz    : size            [boolean] []
    Show datablock sizes for all specified nodes. Return value is tuple of all selected nodes (NumberOfNodes, NumberOfDatablocks, TotalDatablockMemory)

-----------------------------------------

sub   : subgraph        [boolean] []
    Print the subgraph affected by the node or plugs (or all nodes in the graph grouped in subgraphs if -all is used)

-----------------------------------------

nt    : type            [string]
    Filter output to only show nodes of type NODETYPE

    """

def dgmodified():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dgmodified.html



-----------------------------------------

dgmodified is NOT undoable, NOT queryable, and NOT editable.

The dgmodified command is used to find out which nodes in the dependency graph
have been modified. This is mostly useful for fixing instances where file new
asks you to save when no changes have been made to the scene.


-----------------------------------------


Return Value:

string[]  list of all nodes that have been modified
    """

def dgtimer(q=1,ct=1,hi="string",h=1,m="int",n="string",nh=1,o="string",oh=1,rgl="float",rgu="float",r=1,rc="string",rt="string",sh="string",sm="string",st="string",th="float",off=1,on=1,tr=1,t="string",un=1,uhm="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dgtimer.html



-----------------------------------------

dgtimer is NOT undoable, queryable, and NOT editable.

This command measures dependency graph node performance by managing timers on
a per-node basis. Logically, each DG node has a timer associated with it which
records the amount of real time spent in various operations on its plugs. The
time measurement includes the cost of copying data to the node on behalf of
the operation, MEL commands executed by an expression contained in an
expression invoked by the node, and includes any wait time such as when a
fileTexture node loads an image file from disk. Most DG operations are
reported including compute, draw, and dirty propagation.

The various operations we measure are called "metrics" and the types of timers
are called "timer types". The various metrics are always measured when timing
is on, but are only queried when specified via the -show and -hide flags. The
metrics currently supported are listed in detail under the -show flag below.
For each metric we support a standard set of timer types. There are three of
these: "self" for self time (the time specific to the node and not its
children), "inclusive" (time including children of the node), and "count"
(number of operations of the given metric on the node).

The timing mechanism which is used by dgtimer is built into the DG itself,
thus ALL depend nodes can be timed and there is no need for programmers
writing plug-ins using the OpenMaya API to add any special code in order for
their nodes to be timed -- its all handled transparently.

The dgtimer command allows node timers to be turned on, off, reset to zero,
and have their current value displayed, and these operations can be performed
globally on all nodes or on a specific set of nodes defined by name, type or
parentage. Note that all timer measurements are computed in "real time" (the
same time measurement you get from a wristwatch) as opposed to "CPU time"
(which only measures time when the processor is executing your code). All
times are displayed in seconds.

Use the -query flag to display the current timer values on a node,  
use -on to turn on timing,  
use -off to turn off timing,  
and -reset to reset timers to zero.

To display the values measured during timing, there are two approaches. The
first method is to use the -query flag can be used to report the information
which has been measured. The second method is to use the query methods
available on the OpenMaya class MFnDependencyNode (see the OpenMaya
documentation for details).

What follows is a description of what is generated via -query. The output is
broken out into several sections and these are described as follows:

SECTION 1:  
Section 1 of the dgtimer output contains global information. This section can
be disabled via the -hoHeader flag. These values are reset whenever a global
timer reset occurs (i.e. dgtimer -reset; is specified). The global values
which are reported are:

  * Total real time: the total wall-clock time since the last global timer reset. This is the actual time which has been spent as you might measure it measure it with your watch. On a multi-processing system, this value will always remain true to to real time (unlike user and sys time).
  * Total user time: the total time the CPU(s) spent processing Maya not including any system time since the last global timer reset.
  * Total sys time: the total time the CPU(s) spent in operating system calls on behalf of Maya since the last global timer reset. 
  * Summary of each metric for all nodes: a summary of self and count for each metric that we measure:
    * Real time in callbacks reports the self time and count for the "callback" metric.
    * Real time in compute reports the self time and count for the "compute" metric.
    * Real time in dirty propagation reports the self time and count for the "dirty" metric.
    * Real time in drawing reports the self time and count for the "draw" metric.
    * Real time fetching data from plugs reports the self time and count for the "fetch" metric.
  * Breakdown of select metrics in greater detail: a reporting of certain combinations of metrics that we measure:
  * Real time in compute invoked from callback reports the self time spent in compute when invoked either directly or indirectly by a callback.
  * Real time in compute not invoked from callback reports the self time spent in compute not invoked either directly or indirectly by a callback.

SECTION 2:  
Section 2 of the dgtimer -query output contains per-node information. There is
a header which describes the meaning of each column, followed by the actual
per-node data, and this is ultimately followed by a footer which summarises
the totals per column. Note that the data contained in the footer is the
global total for each metric and will include any nodes that have been deleted
since the last reset, so the value in the footer MAY exceed what you get when
you total the individual values in the column. To prevent the header and
footer from appearing, use the -noHeader flag to just display the per-node
data.

The columns which are displayed are as follows:

  * Rank: The order of this node in the sorted list of all nodes, where the list is sorted by -sortMetric and -sortType flag values (if these are omitted the default is to sort by self compute time).
  * ON: Tells you if the timer for that node is currently on or off. (With dgtimer, you have the ability to turn timing on and off on a per-node basis).
  * Per-metric information: various columns are reported for each metric. The name of the metric is reported at in the header in capital letters (e.g. "DRAW"). The standard columns for each metric are:
    * Self: The amount of real time (i.e. elapsed time as you might measure it with a stopwatch) spent performing the operation (thus if the metric is "DRAW", then this will be time spent drawing the node).
    * Inclusive: The amount of real time (i.e. elapsed time as you might measure it with a stopwatch) spent performing the operation including any child operations that were invoked on behalf of the operation (thus if the metric is "DRAW", then this will be the total time taken to draw the node including any child operations).
    * Count: The number of operations that occued on this node (thus if the metric is "DRAW", then the number of draw operations on the node will be reported).

    * Sort information if a column is the one being used to sort all the per-node dgtimer information, then that column is followed by a Percent and Cumulative column which describe a running total through the listing. Note that "-sortType none" prevents these two columns from appearing and implicitely sorts on "self" time.
  * After the per-metric columns, the node name and type are reported:
    * Type The node type.
    * Name The name of the node. If the node is file referenced and you are using namespaces, the namespace will be included. You can also force the dagpath to be displayed by specifying the -uniqueName flag.
    * Plug-in name If the node was implemented in an OpenMaya plug-in, the name of that plug-in is reported.

SECTION 3:  
Section 3 of the dgtimer -query output describes time spent in callbacks. Note
that section 3 only appears when the CALLBACK metric is shown (see the -show
flag).

The first part is SECTION 3.1 lists the time per callback with each entry
comprising:

  * The name of the callback, such as "attributeChangedMsg". These names are internal Maya names, and in the cases where the callback is available through the OpenMaya API, the API access to the callback is similarly named.
  * The name is followed by a breakdown per callbackId. The callbackId is an identifying number which is unique to each client that is registered to a callback and can be deduced by the user, such as through the OpenMaya API. You can cross-reference by finding the same callbackId value listed in SECTIONs 3.1 and 3.3.
    * Self time (i.e. real time spent within that callbackId type not including any child operations which occur while processing the callback).
    * Percent (see the -sortType flag). Note that the percent values are listed to sum up to 100% for that callback. This is not a global percent.
    * Cumulative (see the -sortType flag).
    * Inclusive time (i.e. real time spent within that callbackId including any child operations).
    * Count (number of times the callbackId was invoked).
    * API lists "Y" if the callbackId was defined through the OpenMaya API, and "N" if the callbackId was defined internally within Maya.
    * Node lists the name of the node this callbackId was associated with. If the callbackId was associated with more than one node, the string "*multiple*" is printed. If there was no node associated with the callbackId (or its a callback type in which the node is hard to deduce), the entry is blank.
  * After the callbackId entries are listed, a dashed line is printed followed by a single line listing the self, inclusive and count values for the callback. Note that the percent is relative to the global callback time.

At the bottom of SECTION 3.1 is the per-column total. The values printed match
the summation at the bottom of the listing in section 2. Note that the values
from SECTION 3.1 include any nodes that have been deleted since the last
reset. The thresholding parameters (-threshold, -rangeLower, -rangeUpper and
-maxDisplay) are honoured when generating the listing. The sorting of the rows
and display of the Percent and Cumulative columns obeys the -sortType flag. As
the listing can be long, zero entries are not displayed.

The second part is SECTION 3.2 which lists the data per callbackId. As noted
earlier, the callbackId is an identifying number which is unique to each
client that is registered to a callback and can be deduced by the user, such
as through the OpenMaya API. The entries in SECTION 3.2 appear as follows:

  * CallbackId the numeric identifier for the callback. You can cross reference by finding the same callbackId value listed in SECTIONs 3.1 and 3.3.
  * For each callbackId, the data is broken down per-callback:
    * Callback the name of the callback, e.g. "attributeChangedMsg".
    * Percent, Cumulative, Inclusive, Count, API and Node entries as described in SECTION 3.1.
  * After the callback entries are listed for the callbackId, a dashed followed by a summary line is printed. The summary line lists the self, inclusive and count values for the callback. Note that the percent is relative to the global callback time.

The third part is SECTION 3.3 which lists data per-callback per-node. The
nodes are sorted based on the -sortType flag, and for each node, the callbacks
are listed, also sorted based on the -sortType flag. As this listing can be
long, zero entries are not displayed. An important note for SECTION 3.3 is
that only nodes which still exist are displayed. If a node has been deleted,
no infromation is listed.


-----------------------------------------


Return Value:

float  By default, the total of self-compute time for all nodes. Can be
modified via the -returnType, -sortMetric and -sortType flags.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ct    : combineType     [boolean] ['query']
    Causes all nodes of the same type (e.g. animCurveTA) to be combined in the output display.

-----------------------------------------

hi    : hide            [string] ['query']
    This flag is the converse of -show. As with -show, it is a query-only flag which can be specified multiple times. If you do specify -hide, we display all columns except those listed by the -hide flags.

-----------------------------------------

h     : hierarchy       [boolean] ['query']
    Used to specify that a hierarchy of the dependency graph be affected, thus "-reset -hierarchy -name ball" will reset the timers on the node named "ball" and all of its descendents in the dependency graph.

-----------------------------------------

m     : maxDisplay      [int] ['query']
    Truncates the display so that only the most expenive "n" entries are printed in the output display.

-----------------------------------------

n     : name            [string] ['query']
    Used in conjunction with -reset or -query to specify the name of the node to reset or print timer values for. When querying a single timer, only a single line of output is generated (i.e. the global timers and header information is omitted). Note that one can force output to the script editor window via the "-outputFile MEL" option to make it easy to grab the values in a MEL script. Note: the -name and -type flag cannot be used together.

-----------------------------------------

nh    : noHeader        [boolean] ['query']
    Used in conjunction with -query to prevent any header or footer information from being printed. All that will be output is the per-node timing data. This option makes it easier to parse the output such as when you output the query to a file on disk using the -outputFile option.

-----------------------------------------

o     : outputFile      [string] ['query']
    Specifies where the output of timing or tracing is displayed. The flag takes a string argument which accepts three possible values:    1. The name of a file on disk.   2. Or the keyword "stdout", which causes output to be displayed on the terminal window (Linux and Macintosh), and the status window on Windows.   3. Or the keyword "MEL", which causes output to be displayed in the Maya Script Editor (only supported with -query).  The "stdout" setting is the default behaviour.  This flag can be used with the -query flag as well as the -trace flag.  When used with the -trace flag, any tracing output will be displayed on the destination specified by the -outputFile (or stdout if -outputFile is omitted). Tracing operations will continue to output to the destination until you specify the -trace and -outputFile flags again.  When used with the -query flag, timing output will be displayed to the destination specified by the -outputFile (or "stdout" if -outputFile is omitted).  Here are some examples of how to use the -query, -trace and -outputFile flags:  Example: output the timing information to a single file on disk:                dgtimer -on;                                       // Turn on timing     create some animated scene content;     play -wait;                                        // Play the scene through     dgtimer -query -outputFile "/tmp/timing.txt"       // Output node timing information to a file on disk       Example: output the tracing information to a single file on disk:                dgtimer -on;                                       // Turn on timing     create some animated scene content;     dgtimer -trace on -outputFile "/tmp/trace.txt"     // Turn on tracing and output the results to file     play -wait;                                        // Play the scene through; trace info goes to /tmp/trace.txt     dgtimer -query;                                    // But the timing info goes to the terminal window     play -wait;                                        // Play the scene again, trace info still goes to /tmp/trace.txt       Example: two runs, outputting the trace information and timing information to separate files:                dgtimer -on;                                       // Turn on timing     create some animated scene content;     dgtimer -trace on -outputFile "/tmp/trace1.txt"    // Turn on tracing and output the results to file     play -wait;                                        // Play the scene through     dgtimer -query -outputFile "/tmp/query1.txt"       // Output node timing information to another file     dgtimer -reset;     dgtimer -trace on -outputFile "/tmp/trace2.txt"    // Output tracing results to different file     play -wait;                                        // Play the scene through     dgtimer -query -outputFile "/tmp/query2.txt"       // Output node timing information to another file       Tips and tricks:    * Outputting the timing results to the script editor makes it easy to use the results in MEL e.g. string $timing[] = `dgtimer -query -outputFile MEL`.   * It is important to note that the -outputFile you specify with -trace is totally independent from the one you specify with -query.   * If the file you specify already exists, Maya will empty the file first before outputting data to it (and if the file is not writable, an error is generated instead).  In query mode, this flag needs a value.

-----------------------------------------

oh    : overhead        [boolean] ['query']
    Turns on and off the measurement of timing overhead. Under ordinary circumstances the amount of timing overhead is minimal compared with the events being measured, but in complex scenes, one might find the overhead to be measurable. By default this option is turned off. To enable it, specify "dgtimer -overhead true" prior to starting timing. When querying timing, the overhead is reported in SECTION 1.2 of the dgtimer output and is not factored out of each individual operation.

-----------------------------------------

rgl   : rangeLower      [float] []
    This flag can be specified to limit the range of nodes which are displayed in a query, or the limits of the heat map with -updateHeatMap. The value is the lower percentage cutoff for the nodes which are processed. There is also a -rangeLower flag which sets the lower range limit. The default value is 0, meaning that all nodes with timing value below the upper range limit are considered.

-----------------------------------------

rgu   : rangeUpper      [float] []
    This flag can be specified to limit the range of nodes which are displayed in a query, or the limits of the heat map with -updateHeatMap. The value is the upper percentage cutoff for the nodes which are processed. There is also a -rangeLower flag which sets the lower range limit. The default value is 100, meaning that all nodes with timing value above the lower range limit are considered.

-----------------------------------------

r     : reset           [boolean] []
    Resets the node timers to zero. By default, the timers on all nodes as well as the global timers are reset, but if specified with the -name or -type flags, only the timers on specified nodes are reset.

-----------------------------------------

rc    : returnCode      [string] ['query']
    This flag has been replaced by the more general -returnType flag. The -returnCode flag was unfortunately specific to the compute metric only. It exists only for backwards compatability purposes. It will be removed altogether in a future release.  Here are some handy equivalences:  To get the total number of nodes:   OLD WAY: dgtimer -rc nodecount -q;   // Result:325//    NEW WAY: dgtimer -returnType total -sortType none -q;   // Result:325//    OLD WAY: dgtimer -rc count -q;   // Result:1270//    To get the sum of the compute count column:   NEW WAY: dgtimer -returnType total -sortMetric compute -sortType count -q;   // Result:1270//    OLD WAY: dgtimer -rc selftime -q;   // Result:0.112898//    To get the sum of the compute self column:   NEW WAY: dgtimer -returnType total -sortMetric compute -sortType self -q;   // Result:0.112898//

-----------------------------------------

rt    : returnType      [string] ['query']
    This flag specifies what the double value returned by the dgtimer command represents. By default, the value returned is the global total as displayed in SECTION 1 for the column we are sorting on in the per-node output (the sort column can be specified via the -sortMetric and -sortType flags). However, instead of the total being returned, the user can instead request the individual entries for the column. This flag is useful mainly for querying without forcing any output. The flag accepts the values "total", to just display the column total, or "all" to display all entries individually.  For example, if you want to get the total of draw self time without any other output simply specify the following:   dgtimer -returnType total -sortMetric draw -sortType self -threshold 100 -noHeader -query;   // Result: 7718.01 //  To instead get each individual entry, change the above query to:   dgtimer -returnType all -sortMetric draw -sortType self -threshold 100 -noHeader -query;   // Result: 6576.01 21.91 11.17 1108.92 //  To get the inclusive dirty time for a specific node, use -name as well as -returnType all:   dgtimer -name "virginia" -returnType all -sortMetric dirty -sortType inclusive -threshold 100 -noHeader -query;    Note: to get the total number of nodes, use "-sortType none -returnType total". To get the on/off status for each node, use "-sortType none -returnType all".

-----------------------------------------

sh    : show            [string] ['query']
    Used in conjunction with -query to specify which columns are to be displayed in the per-node section of the output. -show takes an argument, which can be "all" (to display all columns), "callback" (to display the time spent during any callback processing on the node not due to evaluation), "compute" (to display the time spent in the node's compute methods), "dirty" (to display time spent propagating dirtiness on behalf of the node), "draw" (to display time spent drawing the node), "compcb" (to display time spent during callback processing on node due to compute), and "compncb" (to display time spent during callback processing on node NOT due to compute). The -show flag can be used multiple times, but cannot be specified with -hide. By default, if neither -show, -hide, or -sort are given, the effective display mode is: "dgtimer -show compute -query".

-----------------------------------------

sm    : sortMetric      [string] ['query']
    Used in conjunction with -query to specify which metric is to be sorted on when the per-node section of the output is generated, for example "draw" time. Note that the -sortType flag can also be specified to define which timer is sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will sort the output by the number of times each node was drawn. Both -sortMetric and -sortType are optional and you can specify one without the other. The -sortMetric flag can only be specified at most once. The flag takes the following arguments: "callback" (to sort on time spent during any callback processing on the node), "compute" (to sort on the time spent in the node's compute methods), "dirty" (to sort on the time spent propagating dirtiness on behalf of the node), "draw" (to sort on time spent drawing the node), "fetch" (to sort on time spent copying data from the datablock), The default, if -sortMetric is omitted, is to sort on the first displayed column. Note that the sortMetric is independent of which columns are displayed via -show and -hide. Sort on a hidden column is allowed. The column selected by -sortMetric and -sortType specifies which total is returned by the dgtimer command on the MEL command line. This flag is also used with -updateHeatMap to specify which metric to build the heat map for.

-----------------------------------------

st    : sortType        [string] ['query']
    Used in conjunction with -query to specify which timer is to be sorted on when the per-node section of the output is generated, for example "self" time. Note that the -sortMetric flag can also be specified to define which metric is sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will sort the output by the number of times each node was drawn. Both -sortMetric and -sortType are optional and you can specify one without the other. The -sortType flag can be specified at most once. The flag takes the following arguments: "self" (to sort on self time, which is the time specific to the node and not its children), "inclusive" (to sort on the time including children of the node), "count" (to sort on the number of times the node was invoked). and "none" (to sort on self time, but do not display the Percent and Cumulative columns in the per-node display, as well as cause the total number of nodes in Maya to be returned on the command line). The default, if -sortType is omitted, is to sort on self time. The column selected by -sortMetric and -sortType specifies which total is returned by the dgtimer command on the MEL command line. The global total as displayed in SECTION 1 of the listing is returned. The special case of "-sortType none" causes the number of nodes in Maya to instead be returned. This flag is also used with -updateHeatMap to specify which metric to build the heat map for.

-----------------------------------------

th    : threshold       [float] ['query']
    Truncates the display once the value falls below the threshold value. The threshold applies to whatever timer is being used for sorting. For example, if our sort key is self compute time (i.e. -sortMetric is "compute" and -sortType is "self") and the threshold parameter is 20.0, then only nodes with a compute self-time of 20.0 or higher will be displayed. (Note that -threshold uses absolute time. There are the similar -rangeUpper and -rangeLower parameters which specify a range using percentage).

-----------------------------------------

off   : timerOff        [boolean] ['query']
    Turns off node timing. By default, the timers on all nodes are turned off, but if specified with the -name or -type flags, only the timers on specified nodes are turned off. If the timers on all nodes become turned off, then global timing is also turned off as well.

-----------------------------------------

on    : timerOn         [boolean] ['query']
    Turns on node timing. By default, the timers on all nodes are turned on, but if specified with the -name or -type flags, only the timers on specified nodes are turned on. The global timers are also turned on by this command. Note that turning on timing does NOT reset the timers to zero. Use the -reset flag to reset the timers. The idea for NOT resetting the timers is to allow the user to arbitrarily turn timing on and off and continue to add to the existing timer values.

-----------------------------------------

tr    : trace           [boolean] []
    Turns on or off detailed execution tracing. By default, tracing is off. If enabled, each timeable operation is logged when it starts and again when it ends. This flag can be used in conjunction with -outputFile to specify where the output is generated to. The following example shows how the output is formatted:    dgtimer:begin: compute 3 particleShape1Deformed particleShape1Deformed.lastPosition  The above is an example of the output when -trace is true that marks the start of an operation. For specific details on each field: the "dgtimer:begin:" string is an identifying marker to flag that this is a begin operation record. The second argument, "compute" in our example, is the operation metric. You can view the output of each given metric via "dgtimer -q" by specifying the -show flag. The integer which follows (3 in this case) is the depth in the operation stack, and the third argument is the name of the node (particleShape1Deformed). The fourth argument is specific to the metric. For "compute", it gives the name of the plug being computed. For "callback", its the internal Maya name of the callback. For "dirty", its the name of the plug that dirtiness is being propagated from.    dgtimer:end: compute 3 particleShape1Deformed 0.000305685 0.000305685  The above is the end operation record. The "compute", "3" and "particleShapeDeformed" arguments were described in the "dgtimer:begin" overview earlier. The two floating-point arguments are self time and inclusive time for the operation measured in seconds. The inclusive measure lists the total time since the matching "dgtimer:begin:" entry for this operation, while the self measure lists the inclusive time minus any time consumed by child operations which may have occurred during execution of the current operation. As noted elsewhere in this document, these two times are "wall clock times", measuring elapsed time including any time in which Maya was idle or performing system calls.  Since dgtimer can measure some non-node qualities in Maya, such as global message callbacks, a "-" is displayed where the node name would ordinarily be displayed. The "-" means "not applicable".

-----------------------------------------

t     : type            [string] ['query']
    Used in conjunction with -reset or -query to specify the type of the node(s) (e.g. animCurveTA) to reset or print timer values for. When querying, use of the -combineType flag will cause all nodes of the same type to be combined into one entry, and only one line of output is generated (i.e. the global timers and header information is omitted). Note: the -name and -type flag cannot be used together.

-----------------------------------------

un    : uniqueName      [boolean] ['query']
    Used to specify that the DAG nodes listed in the output should be listed by their unique names. The full DAG path to the object will be printed out instead of just the node name.

-----------------------------------------

uhm   : updateHeatMap   [int]
    Forces Maya's heat map to rebuild based on the specified parameters. The heat map is an internal dgtimer structure used in mapping intensity values to colourmap entries during display by the HyperGraph Editor. There is one heat map shared by all editors that are using heat map display mode. Updating the heat map causes the timer values on all nodes to be analysed to compose the distribution of entries in the heat map. The parameter is the integer number of divisions in the map and should equal the number of available colours for displaying the heat map. This flag can be specified with the -rangeLower and -rangeUpper flags to limit the range of displayable to lie between the percentile range. The dgtimer command returns the maximum timing value for all nodes in Maya for the specified metric and type. Note: when the display range includes 0, the special zeroth (exactly zero) slot in the heat map is avilable.

    """

def dgValidateCurve(a=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dgValidateCurve.html



-----------------------------------------

dgValidateCurve is NOT undoable, NOT queryable, and NOT editable.

The dgValidateCurve command is used to make sure the curve internal status
matches their actual state. It forces checks on curves that might not be
tagged as static, even if they are. The DG tracks static curves in order to
optimize evaluation by not considering them animated. Once keys are added and
modified on the curve, it is no longer static. Certain operations on the curve
might make it flat / without animation, but the DG will not treat it as static
because it expects it to be modified again soon. This command allows to
explicitly request checks for the static state of animation curves.


-----------------------------------------


Return Value:

int  Number of curves which changed their static status.


-----------------------------------------


Flags:

-----------------------------------------

a     : allCurves       [boolean] []
    Ignore the selected or specified objects and work on all curves.

-----------------------------------------

v     : verbose         [boolean]
    Prints out all of the curves set static or not.

    """

def diskCache(q=1,a=1,ct="string",c="string",ca=1,d="string",da=1,empty="string",ea=1,eco=1,et="time",frt="string",os=1,sr="int",st="time",tmp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/diskCache.html



-----------------------------------------

diskCache is NOT undoable, queryable, and NOT editable.

Command to create, clear, or close disk cache(s).


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : append          [boolean] ['query']
    Append at the end and not to flush the existing cache

-----------------------------------------

ct    : cacheType       [string] ['query']
    Specifies the type of cache to overwrite. "mcfp" for particle playback cache, "mcfi" for particle initial cache. "mcj" for jiggle cache. This option is only activated during the cache creation.

-----------------------------------------

c     : close           [string] ['query']
    Close the cache given the disk cache node name. If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.

-----------------------------------------

ca    : closeAll        [boolean] ['query']
    Close all disk cache files. If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.

-----------------------------------------

d     : delete          [string] ['query']
    Delete the cache given the disk cache node name. If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.

-----------------------------------------

da    : deleteAll       [boolean] ['query']
    Delete all disk cache files. If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.

-----------------------------------------

e     : empty           [string] ['query']
    Clear the content of the disk cache with the given disk cache node name. If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.

-----------------------------------------

ea    : emptyAll        [boolean] ['query']
    Clear the content of all disk caches. If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.

-----------------------------------------

eco   : enabledCachesOnly [boolean] ['query']
    When present, this flag restricts the -ea/emptyAll, so that only "enabled" disk caches (i.e., disk cache nodes with the ".enable" attribute set to "true") are affected.

-----------------------------------------

et    : endTime         [time] ['query']
    Specifies the end frame of the cache range.

-----------------------------------------

frt   : frameRangeType  [string] ['query']
    Specifies the type of frame range to use, namely "Render Globals", "Time Slider", and "Start/End". In the case of "Time Slider", startFrame and endFrame need to be specified. (This flag is now obsolete. Please use the -startTime and -endTime flags to specify the frame range explicitly.)

-----------------------------------------

os    : overSample      [boolean] ['query']
    Over sample if true. Otherwise, under sample.

-----------------------------------------

sr    : samplingRate    [int] ['query']
    Specifies how frequently to sample relative to each frame. When over- sampling (-overSample has been specified), this parameter determines how many times per frame the runup will be evaluated. When under-sampling (the default, when -overSample has not been specified), the runup will evaluate only once per sr frames, where sr is the value specified to this flag.

-----------------------------------------

st    : startTime       [time] ['query']
    Specifies the start frame of the cache range.

-----------------------------------------

tmp   : tempDir         [boolean]
    Query-only flag for the location of temporary diskCache files.

    """

def dynamicLoad(q=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynamicLoad.html



-----------------------------------------

dynamicLoad is undoable, queryable, and NOT editable.

Dynamically load the DLL passed as argument.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.
    """

def error(n=1,sl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/error.html



-----------------------------------------

error is NOT undoable, NOT queryable, and NOT editable.

The error command is provided so that the user can issue error messages from
his/her scripts and control execution in the event of runtime errors.

The string argument is displayed in the command window (or stdout if running
in batch mode) after being prefixed with an error message heading and
surrounded by //.

The error command also causes execution to terminate with an error. Using
error is like raising an exception because the error will propagate up through
the call chain. You can use catch to handle the error from the caller side. If
you don't want execution to end, then you probably want to use the warning
command instead.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

n     : noContext       [boolean] []
    Do not include the context information with the error message.

-----------------------------------------

sl    : showLineNumber  [boolean]
    Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the script editor that enables line number display instead.

    """

def fcheck():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fcheck.html



-----------------------------------------

fcheck is NOT undoable, NOT queryable, and NOT editable.

Invokes the fcheck program to display images in a separate window.


-----------------------------------------


Return Value:

None
    """

def findType(d=1,exact=1,f=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/findType.html



-----------------------------------------

findType is NOT undoable, NOT queryable, and NOT editable.

The findType command is used to search through a dependency subgraph on a
certain node to find all nodes of the given type. The search can go either
upstream (input connections) or downstream (output connections). The
plug/attribute dependencies are not taken into account when searching for
matching nodes, only the connections.


-----------------------------------------


Return Value:

string[]  The list of node(s) of the requested type connected to the given
node(s)


-----------------------------------------


Flags:

-----------------------------------------

d     : deep            [boolean] []
    Find all nodes of the given type instead of just the first.

-----------------------------------------

e     : exact           [boolean] []
    Match node types exactly instead of any in a node hierarchy.

-----------------------------------------

f     : forward         [boolean] []
    Look forwards (downstream) through the graph rather than backwards (upstream) for matching nodes.

-----------------------------------------

t     : type            [string]
    Type of node to look for (e.g. "transform"). This flag is mandatory.

    """

def flushUndo():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/flushUndo.html



-----------------------------------------

flushUndo is undoable, NOT queryable, and NOT editable.

Removes everything from the undo queue, freeing up memory.


-----------------------------------------


Return Value:

None
    """

def hardware(brd=1,cpu=1,gfx=1,mhz=1,npr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hardware.html



-----------------------------------------

hardware is undoable, NOT queryable, and NOT editable.

Return description of the hardware available in the machine.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

brd   : brdType         [boolean] []
    Returns IP number identifying the CPU motherboard

-----------------------------------------

cpu   : cpuType         [boolean] []
    Returns type of CPU

-----------------------------------------

gfx   : graphicsType    [boolean] []
    Returns string identifying graphics hardware type

-----------------------------------------

mhz   : megaHertz       [boolean] []
    Returns string identifying the speed of the CPU chip

-----------------------------------------

npr   : numProcessors   [boolean]
    Returns string identifying the number of processors

    """

def help(q=1,doc=1,lng="string",l=1,pdt="uint",pm=1,ppt="uint",psm=1,rm=1,so=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/help.html



-----------------------------------------

help is undoable, queryable, and NOT editable.

With no arguments, help tells how to use help. If a command name is specified,
help will return the quick help for that command. Other flags can be used to
open the online documentation, or to list available commands based on a
pattern.

Pattern follows the following syntax:

    
    
    *            matches any string
    ?            matches any character
    [agj]        matches a, g or j
    [^0-9]       matches anything but a digit
    x+           matches any number of subsequent x
    a{3}         matches aaa
    a{3,}        matches aaa, aaaa, ...
    a{3,5}       matches aaa, aaaa, or aaaaa
    (ab)(CD)\2\1 matches abCDCDab (\1 to \9 available)


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

doc   : documentation   [boolean] []
    Use a browser to show the documentation associated with the single command name given. A pattern cannot be used with this flag. If no command name is specified, then this flag will go to the main documentation index.

-----------------------------------------

lng   : language        [string] []
    Show the help for this command in the specified language. Valid values are "mel" and "python". The default is Mel. Used with the doc flag.

-----------------------------------------

l     : list            [boolean] []
    List all the commands whose names match the regular expression. Pass the regular expression as the first argument to the command specified.

-----------------------------------------

pdt   : popupDisplayTime [uint] ['query']
    Set the amount of time, in seconds, that the popup help will be displayed. The default is 4 seconds. This flag is mutually exclusive of the list and doc flags.

-----------------------------------------

pm    : popupMode       [boolean] ['query']
    Turn on or off popup help mode. This flag is mutually exclusive of the list and doc flags.

-----------------------------------------

ppt   : popupPauseTime  [uint] ['query']
    Set the amount of time, in milliseconds, before the popup help will be displayed. The default is 800 milliseconds. This flag is mutually exclusive of the list and doc flags.

-----------------------------------------

psm   : popupSimpleMode [boolean] ['query']
    Turn on or off simple popup help mode. If set, ToolClips will display only name and keyboard shortcut.

-----------------------------------------

rm    : rolloverMode    [boolean] ['query']
    Turn on or off rollover help mode. This flag is mutually exclusive with the list and doc flags.

-----------------------------------------

so    : syntaxOnly      [boolean]
    When no other flag is specified, return only the syntax part of the quick help.

    """

def hitTest():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hitTest.html



-----------------------------------------

hitTest is NOT undoable, NOT queryable, and NOT editable.

The hitTest command hit-tests a point in the named control and returns a list
of items underneath the point. The point is specified in pixels with the
origin (0,0) at the top-left corner. This position is compatible with the
coordinates provided by a drop-callback. The types of items that may be
returned depends upon the specific control; not all controls currently support
hit-testing.


-----------------------------------------


Return Value:

string[]  items underneath the hit-point
    """

def memory(av=1,af=1,dbg=1,fr=1,gb=1,he=1,kb=1,mb=1,pf=1,pr=1,phy=1,pv=1,sum=1,swf=1,swl=1,swm=1,swp=1,swr=1,swv=1,sw=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/memory.html



-----------------------------------------

memory is undoable, NOT queryable, and NOT editable.

Used to query essential statistics on memory availability and usage.

By default memory sizes are returned in bytes. Since Maya's command engine
only supports 32-bit signed integers, any returned value which cannot fit into
31 bits will be truncated to 2,147,483,647 and a warning message displayed. To
avoid having memory sizes truncated use one of the memory size flags to return
the value in larger units (e.g. megabytes) or use the asFloat flag to return
the value as a float.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

av    : adjustedVirtualMemory [boolean] []
    Returns size of adjusted virtual memory allocated by the process. The adjustment is done by computing an offset when the application is launched that will be subtracted from the process virtual memory in order to give the adjusted value. The returned size is an approximation of the memory used by the process that can be more reliable in some cases, for instance on platforms where display drivers can reserve large ranges of memory addresses, therefore increasing the size of the process virtual memory, even though those addresses are actually not used.

-----------------------------------------

af    : asFloat         [boolean] []
    Causes numeric values to be returned as floats rather than ints. This can be useful if you wish to retain some of the significant digits lost when using the unit size flags.

-----------------------------------------

dbg   : debug           [boolean] []
    Print debugging statistics on arena memory (if it exists)

-----------------------------------------

fr    : freeMemory      [boolean] []
    Returns size of free memory

-----------------------------------------

gb    : gigaByte        [boolean] []
    Return memory sizes in gigabytes (1024*1024*1024 bytes)

-----------------------------------------

he    : heapMemory      [boolean] []
    Returns size of memory heap

-----------------------------------------

kb    : kiloByte        [boolean] []
    Return memory sizes in kilobytes (1024 bytes)

-----------------------------------------

mb    : megaByte        [boolean] []
    Return memory sizes in megabytes (1024*1024 bytes)

-----------------------------------------

pf    : pageFaults      [boolean] []
    Returns number of page faults

-----------------------------------------

pr    : pageReclaims    [boolean] []
    Returns number of page reclaims

-----------------------------------------

phy   : physicalMemory  [boolean] []
    Returns size of physical memory

-----------------------------------------

pv    : processVirtualMemory [boolean] []
    Returns size of virtual memory allocated by the process

-----------------------------------------

sum   : summary         [boolean] []
    Returns a summary of memory usage. The size flags are ignored and all memory sizes are given in megabytes.

-----------------------------------------

swf   : swapFree        [boolean] []
    Returns size of free swap

-----------------------------------------

swl   : swapLogical     [boolean] []
    Returns size of logical swap

-----------------------------------------

swm   : swapMax         [boolean] []
    Returns maximum swap size

-----------------------------------------

swp   : swapPhysical    [boolean] []
    Returns size of physical swap

-----------------------------------------

swr   : swapReserved    [boolean] []
    Returns size of reserved swap

-----------------------------------------

swv   : swapVirtual     [boolean] []
    Returns size of virtual swap

-----------------------------------------

sw    : swaps           [boolean]
    Returns number of swaps

    """

def ogs(q=1,di=1,drt=1,dt="string",hwi=1,fe="string",xml="string",gmt="int",gpu=1,lve=1,irs=1,p=1,rbt=1,rup="string",rlt=1,r=1,ss="string",ttp=1,trp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ogs.html



-----------------------------------------

ogs is NOT undoable, queryable, and NOT editable.

OGS is one of the viewport renderers. As there is a lot of effort involved in
migrating functionality it will evolve over several releases. As it evolves it
is prudent to provide safeguards to get the database back to a known state.
That is the function of this command, similar to how 'dgdirty' is used to
restore state to the dependency graph.


-----------------------------------------


Return Value:

string  Result of the operation    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

di    : deviceInformation [boolean] []
    If used then output the current device information.

-----------------------------------------

drt   : disposeReleasableTextures [boolean] []
    Clear up all the releasable file textures in GPU memory that are not required for rendering.

-----------------------------------------

dt    : dumpTexture     [string] []
    If used then dump GPU texture memory usage info (in MB), must be used with FLAG gpuMemoryUsed. The final info detail is specified by the string parameter. Current available values are: "full" , "total".

-----------------------------------------

hwi   : enableHardwareInstancing [boolean] []
    Enables/disables new gpu instancing of instanceable render items in OGS.

-----------------------------------------

fe    : fragmentEditor  [string] []
    If used then launch the fragment editor UI.

-----------------------------------------

xml   : fragmentXML     [string] []
    Get the fragment XML associated with a shading node.

-----------------------------------------

gmt   : gpuMemoryTotal  [int] ['query']
    Get or set the total amount of GPU memory which Maya is allowed to use (in MB).

-----------------------------------------

gpu   : gpuMemoryUsed   [boolean] []
    If used then output the estimated amount of GPU memory in use (in MB).

-----------------------------------------

lve   : isLegacyViewportEnabled [boolean] ['query']
    To query if the legacy viewport is enabled.

-----------------------------------------

irs   : isWinRemoteSession [boolean] ['query']
    Query if this is a remote session.

-----------------------------------------

p     : pause           [boolean] ['query']
    Toggle pausing VP2 display update

-----------------------------------------

rbt   : rebakeTextures  [boolean] []
    If used then re-bake all baked textures for OGS.

-----------------------------------------

rup   : regenerateUVTilePreview [string] []
    If used then regenerate all UV tiles preview textures for OGS.

-----------------------------------------

rlt   : reloadTextures  [boolean] []
    If used then reload all textures for OGS.

-----------------------------------------

r     : reset           [boolean] ['query']
    If used then reset the entire OGS database for all viewports using it. In query mode the number of viewports that would be affected is returned but the reset is not actually done. If no viewport is using OGS then OGS will stop listening to DG changes.

-----------------------------------------

ss    : shaderSource    [string] ['query']
    Get the shader source for the specified material.

-----------------------------------------

ttp   : toggleTexturePaging [boolean] []
    If used then toggle the default OGS Texture paging mechanism.

-----------------------------------------

trp   : traceRenderPipeline [boolean]
    Enable debug tracing of the renderer pipeline.

    """

def openGLExtension(ext="string",rnd=1,vnd=1,ver=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/openGLExtension.html



-----------------------------------------

openGLExtension is NOT undoable, NOT queryable, and NOT editable.

Command returns the extension name depending on whether a given OpenGL
extension is supported or not. The input is the extension string to the
-extension flag. If the -extension flag is not used, or if the string argument
to this flag is an empty string than all extension names are returned in a
single string. If the extension exists it is not necessary true that the
extension is supported. This command can only be used when a modeling view has
been created. Otherwise no extensions will have been initialized and the
resulting string will always be the empty string.


-----------------------------------------


Return Value:

string  The supported string(s)


-----------------------------------------


Flags:

-----------------------------------------

ext   : extension       [string] []
    Specifies the OpenGL extension to query.

-----------------------------------------

rnd   : renderer        [boolean] []
    Specifies to query the OpenGL renderer.

-----------------------------------------

vnd   : vendor          [boolean] []
    Specifies to query the company responsible for the OpenGL implementation.

-----------------------------------------

ver   : version         [boolean]
    Specifies to query the OpenGL version.

    """

def profiler(q=1,a="string",ac=1,b="int",ci="int",cin="int",cf="string",cn="string",cni="string",cr=1,cam=1,coi="int",eci=1,eca=1,eco=1,ec=1,ed=1,edu=1,ei="int",en=1,et=1,eti=1,instrumentMel=1,l="string",o="string",pd="string",pn="string",rc="string",r=1,s=1,sig=1,sim=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/profiler.html



-----------------------------------------

profiler is NOT undoable, queryable, and NOT editable.

The profiler is used to record timing information from key events within Maya,
as an aid in tuning the performance of scenes, scripts and plug-ins. User
written plug-ins and Python scripts can also generate profiling information
for their own code through the MProfilingScope (C++), MProfilingContextManager
(Python) and MProfiler classes in the API.

This command provides the ability to control the collection of profiling data
and to query information about the recorded events. The recorded information
can also be viewed graphically in the Profiler window.

The buffer size cannot be changed while sampling is active, it will return an
error The reset flag cannot be called while sampling is active, it will return
an error. Any changes to the buffer size will only be applied on start of the
next recording. You can't save and load in the same command, save has
priority, load would be ignored.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : addCategory     [string] []
    Add a new category for the profiler. Returns the index of the new category.

-----------------------------------------

ac    : allCategories   [boolean] ['query']
    Query the names of all categories. If the categoryInfo flag is set then alternate the name of the category with the description of the category.

-----------------------------------------

b     : bufferSize      [int] ['query']
    Toggled : change the buffer size to fit the specified number of events (requires that sampling is off) Query : return the current buffer size The new buffer size will only take effect when next sampling starts. When the buffer is full, the recording stops.

-----------------------------------------

ci    : categoryIndex   [int] ['query']
    Used in conjunction with other flags, to indicate the index of the category.  In query mode, this flag needs a value.

-----------------------------------------

cin   : categoryIndexToName [int] ['query']
    Returns the name of the category with a given index.  In query mode, this flag needs a value.

-----------------------------------------

cf    : categoryInfo    [string] ['query']
    When used with the addCategory flag set the description of the added profiler category. In query mode return the description of the category referenced by either the categoryIndex or categoryName flags.  In query mode, this flag can accept a value.

-----------------------------------------

cn    : categoryName    [string] ['query']
    Used in conjunction with other flags, to indicate the name of the category.  In query mode, this flag needs a value.

-----------------------------------------

cni   : categoryNameToIndex [string] ['query']
    Returns the index of the category with a given name.  In query mode, this flag needs a value.

-----------------------------------------

cr    : categoryRecording [boolean] ['query']
    Toggled : Enable/disable the recording of the category. Query : return if the recording of the category is On. Requires the -categoryIndex or -categoryName flag to specify the category to be queried.

-----------------------------------------

cam   : clearAllMelInstrumentation [boolean] []
    Clear all MEL command or procedure instrumentation.

-----------------------------------------

coi   : colorIndex      [int] []
    Used with "-instrumentMel true" to specify the color index to show the profiling result.

-----------------------------------------

eci   : eventCPUId      [boolean] ['query']
    Query the CPU ID of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

eca   : eventCategory   [boolean] ['query']
    Query the category index the event at the given index belongs to. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

eco   : eventColor      [boolean] ['query']
    Query the color of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

ec    : eventCount      [boolean] ['query']
    Query the number of events in the buffer

-----------------------------------------

ed    : eventDescription [boolean] ['query']
    Query the description of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

edu   : eventDuration   [boolean] ['query']
    Query the duration of the event at the given index, the time unit is microsecond. Note that a signal event has a 0 duration. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

ei    : eventIndex      [int] ['query']
    Used usually in conjunction with other flags, to indicate the index of the event.  In query mode, this flag needs a value.

-----------------------------------------

en    : eventName       [boolean] ['query']
    Query the name of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

et    : eventStartTime  [boolean] ['query']
    Query the time of the event at the given index, the time unit is microsecond. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

eti   : eventThreadId   [boolean] ['query']
    Query the thread ID of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.

-----------------------------------------

instrumentMel : instrumentMel   [boolean] []
    Enable/Diable the instrumentation of a MEL command or procedure. When the instrumentation is enabled, the execution of MEL command or procedure can be profiled and shown in the Profiler window. To enable the instrumentation requires the -procedureName, -colorIndex and -categoryIndex flags. To disable the instrumentation requires the -procedureName flag.

-----------------------------------------

l     : load            [string] ['query']
    Read the recorded events from the specified file

-----------------------------------------

o     : output          [string] ['query']
    Output the recorded events to the specified file

-----------------------------------------

pd    : procedureDescription [string] []
    Used with "-instrumentMel true" to provide a description of the MEL command or procedure being instrumented. This description can be viewed in the Profiler Tool window.

-----------------------------------------

pn    : procedureName   [string] []
    Used with -instrumentMel to specify the name of the procedure to be enabled/disabled the instrumentation.

-----------------------------------------

rc    : removeCategory  [string] []
    Remove an existing category for the profiler. Returns the index of the removed category.

-----------------------------------------

r     : reset           [boolean] ['query']
    reset the profiler's data (requires that sampling is off)

-----------------------------------------

s     : sampling        [boolean] ['query']
    Toggled : Enable/disable the recording of events Query : return if the recording of events is On.

-----------------------------------------

sig   : signalEvent     [boolean] ['query']
    Query if the event at the given index is a signal event. Requires the -eventIndex flag to specify the event to be queried. A Signal Event only remembers the start moment and has no knowledge about duration. It can be used in cases when the user does not care about the duration but only cares if this event does happen.

-----------------------------------------

sim   : signalMelEvent  [boolean]
    Used with "-instrumentMel true", inform profiler that this instrumented MEL command or procedure will be taken as a signal event during profiling. A Signal Event only remembers the start moment and has no knowledge about duration. It can be used in cases when the user does not care about the duration but only cares if this event does happen.

    """

def profilerTool(q=1,e=1,cat=1,cs=1,csr=1,cpu=1,dtr=1,et=1,ex=1,es=1,esr=1,fn=1,fp=1,fa=1,fs=1,isolateSegment="int",mk=1,mww=1,se="string",sc=1,sa=1,scp=1,ss=1,ssr=1,thd=1,uis=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/profilerTool.html



-----------------------------------------

profilerTool is NOT undoable, queryable, and editable.

This script is intended to be used by the profilerPanel to interact with the
profiler tool's view (draw region). It can be used to control some behaviors
about the profiler Tool.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cat   : categoryView    [boolean] ['edit']
    Change view mode to category view

-----------------------------------------

cs    : collapseSelectedEvents [boolean] ['edit']
    Hide all sub-events of selected events so that only top-level events show

-----------------------------------------

csr   : collapseSelectedEventsRepetition [boolean] ['edit']
    Hide all sub-events repetition of selected events based on their comment

-----------------------------------------

cpu   : cpuView         [boolean] ['edit']
    Change view mode to cpu view

-----------------------------------------

dtr   : destroy         [boolean] []
    Destroy the profiler tool Internal flag. Should not be used by user.

-----------------------------------------

et    : eventTypes      [boolean] ['query']
    Return JSON data containing the list of event types on currently existing events. If the value of the flag is true then show only event types for selected events, otherwise show them for all events. The JSON return string will contain the event type information in the following format:                {         "eventSummary" : [             { "type"        : EVENT_TYPE_NAME,             , "description" : EVENT_TYPE_DESCRIPTION,             , "color"       : [ RED_AS_FLOAT, GREEN_AS_FLOAT, BLUE_AS_FLOAT ]             , "category"    : CATEGORY_NAME             , "count"       : EVENT_TYPE_COUNT             }         ]     }       "type" and "description" may be omitted, indicating that the results correspond to anonymous events.

-----------------------------------------

ex    : exists          [boolean] ['query']
    Query if the profiler tool view exists. Profiler tool can only exist after "profilerTool -make" is called.

-----------------------------------------

es    : expandSelectedEvents [boolean] ['edit']
    Show all sub-events of selected events

-----------------------------------------

esr   : expandSelectedEventsRepetition [boolean] ['edit']
    Show all sub-events repetition of selected events based on their comment

-----------------------------------------

fn    : findNext        [boolean] ['query']
    This flag is used along with flag -searchEvent.

-----------------------------------------

fp    : findPrevious    [boolean] ['query']
    This flag is used along with flag -searchEvent.

-----------------------------------------

fa    : frameAll        [boolean] ['edit']
    Frame on all events in the profilerToolView

-----------------------------------------

fs    : frameSelected   [boolean] ['edit']
    Frame on all selected events in the profilerToolView

-----------------------------------------

isolateSegment : isolateSegment  [int] ['edit']
    Isolate a specified segment. A segment is a set of events that happened in one animation frame. You can use flag -segmentCount to query the number of segments in the event buffer. The segment index starts from 0. If the specified segment does not exist, an error will be thrown.

-----------------------------------------

mk    : make            [boolean] []
    Make the profiler tool and parent it to the most recent layout created Internal flag. Should not be used by user.

-----------------------------------------

mww   : matchWholeWord  [boolean] ['edit']
    Tells profiler tool if it should match whole word when searching event(s). The default value is false.

-----------------------------------------

se    : searchEvent     [string] ['query']
    Search event(s). You can set -matchWholeWord before you use -searchEvent. If -matchWholeWord has been set to true, the profiler tool will search event(s) whose name exactly matches with the string. If -matchWholeWord has been set to false, the profiler tool will search event(s) whose name contains the string. If -findNext is also used along with this flag, the profiler tool will find the first event next to the current selected event. If -findPrevious is also used along with this flag, the profiler tool will find the first event previous to the current selected event. If currently don't have a selected event or there are multiple selected events, the search will start at the first event in profiler buffer. If -findNext and -findPrevious are not used along with this flag, the profiler tool will find all events.  In query mode, this flag needs a value.

-----------------------------------------

sc    : segmentCount    [boolean] ['query']
    Returns the number of segments in the event buffer.

-----------------------------------------

sa    : showAllEvent    [boolean] ['edit']
    Show all events (if events were hidden by filtering) (true) or Hide all events (false)

-----------------------------------------

scp   : showCriticalPath [boolean] ['edit']
    Show critical path of selected frame

-----------------------------------------

ss    : showSelectedEvents [boolean] ['edit']
    Show only the selected events (true) or hide all selected events (false)

-----------------------------------------

ssr   : showSelectedEventsRepetition [boolean] ['edit']
    Show only the selected events repetition based on their comment (true) or Hide all selected events repetition based on their comment (false)

-----------------------------------------

thd   : threadView      [boolean] ['edit']
    Change view mode to thread view

-----------------------------------------

uis   : unisolateSegment [boolean]
    Unisolate current isolated segment. If no segment is currently isolated, nothing will happen.

    """

def redo():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/redo.html



-----------------------------------------

redo is undoable, NOT queryable, and NOT editable.

Takes the most recently undone command from the undo list and redoes it.


-----------------------------------------


Return Value:

None
    """

def shotTrack(q=1,e=1,it="uint",l=1,m=1,nt="uint",ret=1,rt="uint",sm=1,so=1,st="[uint, uint]",t="string",tr="uint",uso=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shotTrack.html



-----------------------------------------

shotTrack is undoable, queryable, and editable.

This command is used for inserting and removing tracks related to the shots
displayed in the Sequencer. It can also be used to modify the track state, for
example, to lock or mute a track.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

it    : insertTrack     [uint] []
    This flag is used to insert a new empty track at the track index specified.

-----------------------------------------

l     : lock            [boolean] ['query', 'edit']
    This flag specifies whether shots on a track are to be locked or not.

-----------------------------------------

m     : mute            [boolean] ['query', 'edit']
    This flag specifies whether shots on a track are to be muted or not.

-----------------------------------------

nt    : numTracks       [uint] ['query']
    To query the number of tracks

-----------------------------------------

ret   : removeEmptyTracks [boolean] []
    This flag is used to remove all tracks that have no clips.

-----------------------------------------

rt    : removeTrack     [uint] []
    This flag is used to remove the track with the specified index. The track must have no clips on it before it can be removed.

-----------------------------------------

sm    : selfmute        [boolean] ['query', 'edit']
    This flag specifies whether shots on a track are to be muted or not (unlike mute, this disregards soloing).

-----------------------------------------

so    : solo            [boolean] ['query', 'edit']
    This flag specifies whether shots on a track are to be soloed or not.

-----------------------------------------

st    : swapTracks      [[uint, uint]] []
    This flag is used to swap the contents of two specified tracks.

-----------------------------------------

t     : title           [string] ['query', 'edit']
    This flag specifies the title for the track.

-----------------------------------------

tr    : track           [uint] ['query', 'edit']
    Specify the track on which to operate by using the track's trackNumber.  In query mode, this flag needs a value.

-----------------------------------------

uso   : unsolo          [boolean]
    This flag specifies whether shots on a track are to be unsoloed or not.

    """

def showHelp(q=1,a=1,d=1,ht=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/showHelp.html



-----------------------------------------

showHelp is NOT undoable, queryable, and NOT editable.

Invokes a web browser to open the on-line documentation and help files. It
will open the help page for a given topic, or open a browser to a specific
URL.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    The specified "URL" is an absolute URL that should be passed directly to the web browser.

-----------------------------------------

d     : docs            [boolean] ['query']
    Use this flag to directly specify a help file relative to the on-line documentation root.

-----------------------------------------

ht    : helpTable       [boolean] ['query']
    Use this flag to specify which file will be used to search for help topics when the -d/docs and -a/absolute flags are not used. If only a file name is specified and not a path, then the file is assumed to be in the maya application directory.   If this flag does not accept an argument if it is queried.   The default value is "helpTable".

-----------------------------------------

v     : version         [boolean]
    Use this flag to get the Maya version that the showHelp command uses.

    """

def timer(endTimer=1,lap=1,n="string",s=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timer.html



-----------------------------------------

timer is NOT undoable, NOT queryable, and NOT editable.

Allow simple timing of scripts and commands. The resolution of this timer is
at the level of your OS's gettimeofday() function.

Note:This command does not handle stacked calls. For example, this code below
will give an incorrect answer on the second `timer -e` call.  

    
    
    timer -s;
    timer -s;
    timer -e;
    timer -e;
    

To do this use named timers:

    
    
    timer -s;
    timer -s -name "innerTimer";
    timer -e -name "innerTimer";
    timer -e;
    

  * I the -e flag or -lap flag return the time elapsed since the last 'timer -s' call.
  * I the -s flag has no return value.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

e     : endTimer        [boolean] []
    Stop the timer and return the time elapsed since the timer was started (in seconds). Once a timer is turned off it no longer exists, though it can be recreated with a new start

-----------------------------------------

lap   : lapTime         [boolean] []
    Get the lap time of the timer (time elapsed since start in seconds). Unlike the end flag this keeps the timer running.

-----------------------------------------

n     : name            [string] []
    Use a named timer for the operation. If this is omitted then the default timer is assumed.

-----------------------------------------

s     : startTimer      [boolean]
    Start the timer.

    """

def timerX(st="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/timerX.html



-----------------------------------------

timerX is undoable, NOT queryable, and NOT editable.

Used to calculate elapsed time. This command returns sub-second accurate time
values. It is useful from scripts for timing the length of operations. Call
this command before and after the operation you wish to time. On the first
call, do not use any flags. It will return the start time. Save this value.
After the operation, call this command a second time, and pass the saved start
time using the -st flag. The elapsed time will be returned.


-----------------------------------------


Return Value:

float  This command returns a different value depending on the flag used. If
no flag is used, then the start time is returned. If the "-st" flag is used,
then it returns the elapsed time since the start time.


-----------------------------------------


Flags:

-----------------------------------------

st    : startTime       [float]
    When this flag is used, the command returns the elapsed time since the specified start time.

    """

def undo():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/undo.html



-----------------------------------------

undo is undoable, NOT queryable, and NOT editable.

Takes the most recent command from the undo list and undoes it.


-----------------------------------------


Return Value:

None
    """

def undoInfo(q=1,cn="string",cck=1,infinity=1,l="uint",ock=1,pq=1,prq=1,rn="string",rqe=1,st=1,swf=1,un="string",uqe=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/undoInfo.html



-----------------------------------------

undoInfo is undoable, queryable, and NOT editable.

This command controls the undo/redo parameters.

In query mode, if invoked without flags (other than the query flag), this
command will return the number of items currently on the undo queue.


-----------------------------------------


Return Value:

string  If querying undoName or redoName    
int  If querying state, infinity, or length  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cn    : chunkName       [string] ['query']
    Sets the name used to identify a chunk for undo/redo purposes when opening a chunk.

-----------------------------------------

cck   : closeChunk      [boolean] []
    Closes the chunk that was opened earlier by openChunk. Once close chunk is called, all undoable operations in the chunk will undo as a single undo operation. Use with CAUTION!! Improper use of this command can leave the undo queue in a bad state.

-----------------------------------------

infinity : infinity        [boolean] ['query']
    Set the queue length to infinity.

-----------------------------------------

l     : length          [uint] ['query']
    Specifies the maximum number of items in the undo queue. The infinity flag overrides this one.

-----------------------------------------

ock   : openChunk       [boolean] []
    Opens a chunk so that all undoable operations after this call will fall into the newly opened chunk, until close chunk is called. Once close chunk is called, all undoable operations in the chunk will undo as a single undo operation. Use with CAUTION!! Improper use of this command can leave the undo queue in a bad state.

-----------------------------------------

pq    : printQueue      [boolean] ['query']
    Prints to the Script Editor the contents of the undo queue.

-----------------------------------------

prq   : printRedoQueue  [boolean] ['query']
    Prints to the Script Editor the contents of the redo queue.

-----------------------------------------

rn    : redoName        [string] ['query']
    Returns what will be redone (if anything)

-----------------------------------------

rqe   : redoQueueEmpty  [boolean] ['query']
    Return true if the redo queue is empty. Return false if there is at least one command in the queue to be redone.

-----------------------------------------

st    : state           [boolean] ['query']
    Turns undo/redo on or off.

-----------------------------------------

swf   : stateWithoutFlush [boolean] ['query']
    Turns undo/redo on or off without flushing the queue. Use with CAUTION!! Note that if you perform destructive operations while stateWithoutFlush is disabled, and you then enable it again, subsequent undo operations that try to go past the destructive operations may be unstable since undo will not be able to properly reconstruct the former state of the scene.

-----------------------------------------

un    : undoName        [string] ['query']
    Returns what will be undone (if anything)

-----------------------------------------

uqe   : undoQueueEmpty  [boolean]
    Return true if the undo queue is empty. Return false if there is at least one command in the queue to be undone.

    """

def warning(n=1,sl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/warning.html



-----------------------------------------

warning is NOT undoable, NOT queryable, and NOT editable.

The warning command is provided so that the user can issue warning messages
from his/her scripts. The string argument is displayed in the command window
(or stdout if running in batch mode) after being prefixed with a warning
message heading and surrounded by the appropriate language separators (# for
Python, // for Mel).


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

n     : noContext       [boolean] []
    Do not include the context information with the warning message.

-----------------------------------------

sl    : showLineNumber  [boolean]
    Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the script editor that enables line number display instead.

    """

def whatsNewHighlight(q=1,hc="[float, float, float]",ho=1,ssd=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/whatsNewHighlight.html



-----------------------------------------

whatsNewHighlight is undoable, queryable, and NOT editable.

This command is used to toggle the What's New highlighting feature, and the
display of the settings dialog for the feature that appears on startup.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

hc    : highlightColor  [[float, float, float]] ['query']
    Set the color of the What's New highlight. The arguments correspond to the red, green, and blue color components. Each color component ranges in value from 0.0 to 1.0.

-----------------------------------------

ho    : highlightOn     [boolean] ['query']
    Toggle the What's New highlighting feature. When turned on, menu items and buttons introduced in the latest version will be highlighted.

-----------------------------------------

ssd   : showStartupDialog [boolean]
    Set whether the settings dialog for this feature appears on startup.

    """

def xpmPicker(fn="string",p="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/xpmPicker.html



-----------------------------------------

xpmPicker is undoable, NOT queryable, and NOT editable.

Open a dialog and ask you to choose a xpm file


-----------------------------------------


Return Value:

string  The full name of the xpm file


-----------------------------------------


Flags:

-----------------------------------------

fn    : fileName        [string] []
    default filename to display in dialog

-----------------------------------------

p     : parent          [string]
    parent window for modal dialog

    """

