def encodeString():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/encodeString.html



-----------------------------------------

encodeString is undoable, NOT queryable, and NOT editable.

This action will take a string and encode any character that would need to be
escaped before being sent to some other command. Such characters include:  

  * double quotes
  * newlines
  * tabs


-----------------------------------------


Return Value:

string  Command result
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

def sortCaseInsensitive():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sortCaseInsensitive.html



-----------------------------------------

sortCaseInsensitive is NOT undoable, NOT queryable, and NOT editable.

This command sorts all the strings of an array in a case insensitive way.


-----------------------------------------


Return Value:

string[]  string to sort
    """

def stringArrayIntersector(q=1,e=1,ad=1,dt="string",ex=1,i="string[]",r=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/stringArrayIntersector.html



-----------------------------------------

stringArrayIntersector is undoable, queryable, and editable.

The stringArrayIntersector command creates and edits an object which is able
to efficiently intersect large string arrays. The intersector object maintains
a sense of "the intersection so far", and updates the intersection when new
string arrays are provided using the -i/intersect flag.

Note that the string intersector object may be deleted using the deleteUI
command.


-----------------------------------------


Return Value:

string  The name of the intersector.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ad    : allowDuplicates [boolean] []
    Should the intersector allow duplicates in the input arrays (true), or combine all duplicate entries into a single, unique entry (false). This flag must be used when initially creating the intersector. Default is 'false'.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

i     : intersect       [string[]] ['edit']
    Intersect the specified string array with the current intersection being maintained by the intersector.

-----------------------------------------

r     : reset           [boolean] ['edit']
    Reset the intersector to begin a new intersection.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def stringArrayIntersector(q=1,e=1,ad=1,dt="string",ex=1,i="string[]",r=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/stringArrayIntersector.html



-----------------------------------------

stringArrayIntersector is undoable, queryable, and editable.

The stringArrayIntersector command creates and edits an object which is able
to efficiently intersect large string arrays. The intersector object maintains
a sense of "the intersection so far", and updates the intersection when new
string arrays are provided using the -i/intersect flag.

Note that the string intersector object may be deleted using the deleteUI
command.


-----------------------------------------


Return Value:

string  The name of the intersector.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ad    : allowDuplicates [boolean] []
    Should the intersector allow duplicates in the input arrays (true), or combine all duplicate entries into a single, unique entry (false). This flag must be used when initially creating the intersector. Default is 'false'.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

i     : intersect       [string[]] ['edit']
    Intersect the specified string array with the current intersection being maintained by the intersector.

-----------------------------------------

r     : reset           [boolean] ['edit']
    Reset the intersector to begin a new intersection.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def assignCommand(q=1,e=1,ad="string",alt=1,ann="string",c="script",cmd=1,ctl=1,da1="string",da2="string",da3="string",d="int",ds="string",ecr=1,fs=1,i="int",ka=1,k="string",kup=1,n=1,ndp="int",num=1,opt=1,sbk=1,suc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/assignCommand.html



-----------------------------------------

assignCommand is undoable, queryable, and editable.

This command allows the user to assign hotkeys and manipulate the internal
array of named command objects. Each object in the array has an 1-based index
which is used for referencing. Under expected usage you should not need to use
this command directly as the Hotkey Editor may be used to assign hotkeys.

This command is obsolete for setting new hotkeys, instead please use the
"hotkey" command.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ad    : addDivider      [string] ['edit']
    Appends an "annotated divider" item to the end of the list of commands.

-----------------------------------------

alt   : altModifier     [boolean] ['edit']
    This flag specifies if an alt modifier is used for the key.

-----------------------------------------

ann   : annotation      [string] ['query', 'edit']
    The string is the english name describing the command.

-----------------------------------------

c     : command         [script] ['query', 'edit']
    This is the command that is executed when this object is mapped to a key or menuItem.

-----------------------------------------

cmd   : commandModifier [boolean] ['edit']
    This flag specifies if a command modifier is used for the key. This is only available on systems which support a separate command key.

-----------------------------------------

ctl   : ctrlModifier    [boolean] ['edit']
    This flag specifies if a ctrl modifier is used for the key.

-----------------------------------------

da1   : data1           [string] ['query', 'edit']
    Optional, user-defined data strings may be attached to the nameCommand objects.

-----------------------------------------

da2   : data2           [string] ['query', 'edit']
    Optional, user-defined data strings may be attached to the nameCommand objects.

-----------------------------------------

da3   : data3           [string] ['query', 'edit']
    Optional, user-defined data strings may be attached to the nameCommand objects.

-----------------------------------------

d     : delete          [int] ['edit']
    This tells the Manager to delete the object at position index.

-----------------------------------------

ds    : dividerString   [string] ['query']
    If the passed index corresponds to a "divider" item, then the divider's annotation is returned. Otherwise, a null string is returned.

-----------------------------------------

ecr   : enableCommandRepeat [boolean] ['edit']
    This flag specifies whether command repeat is enabled.

-----------------------------------------

fs    : factorySettings [boolean] ['edit']
    This flag sets the manager back to factory settings.

-----------------------------------------

i     : index           [int] ['edit']
    The index of the object to operate on. The index value ranges from 1 to the number of name command objects.

-----------------------------------------

ka    : keyArray        [boolean] ['query']
    This flag returns all of the hotkeys on the command.

-----------------------------------------

k     : keyString       [string] ['query', 'edit']
    This specifies a key to assign a command to in edit mode. In query mode this flag returns the key string, modifiers and indicates if the command is mapped to keyUp or keyDown.

-----------------------------------------

kup   : keyUp           [boolean] ['edit']
    This flag specifies if the command is executed on keyUp or keyDown.

-----------------------------------------

n     : name            [boolean] ['query']
    The name of the command object.

-----------------------------------------

ndp   : numDividersPreceding [int] ['query']
    If the index of a namedCommand object C is passed in, then this flag returns the number of "divider" items preceding C when the namedCommands are sorted by category.

-----------------------------------------

num   : numElements     [boolean] ['query']
    This command returns the number of namedCommands in the system. This flag doesn't require the index to be specified.

-----------------------------------------

opt   : optionModifier  [boolean] ['edit']
    This flag specifies if an option modifier is used for the key.

-----------------------------------------

sbk   : sortByKey       [boolean] ['query', 'edit']
    This key tells the manager to sort by key or by order of creation.

-----------------------------------------

suc   : sourceUserCommands [boolean]
    This command sources the user named command file.

    """

def callbacks(ac="script",cac=1,cc=1,dh=1,dc=1,ec=1,h="string",lc=1,o="string",rc="script"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/callbacks.html



-----------------------------------------

callbacks is NOT undoable, NOT queryable, and NOT editable.

This command allows you to add callbacks at key times during UI creation so
that the Maya UI can be extended. The list of standard Maya hooks, as well as
the arguments which will be passed to the callback based on the context are
enumerated in the `describeHooks` section below. Custom hooks can also be
added if third parties want to add UI extensibility to their plugins.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

ac    : addCallback     [script] []
    Add a callback for the specified hook. The owner must also be specified when adding callbacks.

-----------------------------------------

cac   : clearAllCallbacks [boolean] []
    Clear all the callbacks for all hooks and owners. This is generally only used during plugin development and testing as it affects all callbacks registered by Maya and other third parties.

-----------------------------------------

cc    : clearCallbacks  [boolean] []
    Clear all the callbacks for the specified owner. If a hook is specified, only the callbacks for that hook and owner will be cleared.

-----------------------------------------

dh    : describeHooks   [boolean] []
    List the standard Maya hooks. Below is a list of the hooks and their associated arguments and return values. Custom hooks added by third parties are not listed.  hyperShadePanelBuildCreateMenu       This hook is called to add content to the Hypershade panel create menu. It will be called after the standard Maya node entries have been created.   This callback does not have any arguments or return values. In order to preserve the desired look in the Maya UI, these callbacks should add a menu item divider just before returning using: menuItem -divider true.  hyperShadePanelBuildCreateSubMenu       This hook is called to get a classification string for the custom renderer shading nodes, to prevent them from being listed with the standard Maya nodes.   This callback does not have any arguments.    * returns: a classification string, such as `rendernode/myrenderer`  hyperShadePanelPluginChange       This hook is called when a plugin change event (loading / unloading) has occurred to inform Maya whether the Hypershade panel needs to be rebuilt.     * classification (string): classification string belonging to a plugin node, possibly from another plugin   * changeType (string): either `loadPlugin` or `unloadPlugin`   * returns: (int) non-zero if your plugin is responsible for nodes of this classification, and a Hypershade rebuild is required  createRenderNodeSelectNodeCategories       This hook is called when the Create Render Node dialog is being constructed, and allows a third party to have their nodes selected by default. A flag of the form `-allWithMyRendererUp` is the standard form, and the selection can be set up in the tree lister in the callback.   There is no return value for this callback.    * flag (string): flag passed to the Create Render Node dialog command with the leading minus (-) removed   * treeLister (string): the tree lister widget which should be affected  For example, your callback might look like:                global proc myRendererCreateRenderNodeSelectNodeCategoriesCallback(string $flag, string $treeLister){         if($flag == "allWithMyRendererUp") {             treeLister -e -selectPath "myrenderer" $treeLister;         }     }       createRenderNodePluginChange       This hook is called when a plugin change event has occurred to decide if the Create Render Node dialog needs to be closed.     * classification (string): classification string belonging to a plugin node, possibly from another plugin   * returns: (int) non-zero if your plugin is responsible for nodes of this classification, and the Create Render Node dialog needs to be closed  renderNodeClassification       This hook is called to get a classification string for the custom renderer shading nodes. This is used to determine if a given node type belongs to a plugin renderer.   This callback does not have any arguments.    * returns: a classification string, such as `rendernode/myrenderer`  createRenderNodeCommand       This hook is called to give plugin renderers the chance to register their own command for creating their nodes from the render node treeLister and Node Editor. The callback should determine from the classification of the node type in question if it is theirs, and if so, return the appropriate command for creating new nodes of that type.     * postCommand (string): command to be run after the create command   * type (string): nodeType   * returns: (string) MEL create command  buildRenderNodeTreeListerContent       This hook is called to give plugin renderers the chance to add their content to the render node tree lister.     * renderNodeTreeLister (string): the render node tree lister   * postCommand (string): command to be run post-creation   * filterString (string): a space delimited list of filters  AETemplateCustomContent       This hook is called to give plugins a chance to add content to the Attribute Editor for nodes which source AEdependNodeTemplate.     * nodeName (string): the name of the node for which the Attribute Editor is being constructed  firstConnectedShader       This hook is called to determine the primary custom shader connected to the given Shading Engine.     * nodeName (string): the name of the Shading Engine   * returns (string): the name of the custom shader if applicable  allConnectedShaders       This hook is called to determine all the shaders connected to the given Shading Engine.     * nodeName (string): the name of the Shading Engine   * returns (string): a colon separated list of the connected custom shaders (shader1:shader2:shader3)  renderLayerPresetMenu       This hook is called to give plugins a chance to add presets to a renderLayer node.     * nodeName (string): the name of the renderLayer node  addBakingMenuItems       This hook is called to give plugins a chance to add baking menu items to the global Render - Lighting/Shading menu.     * menuItemAnchor (string): the name of the menuItem which the new baking menu items should be inserted after.   addVertexBakingMenuItems       This hook is called to give plugins a chance to add baking menu items to the global Polygon - Color menu.   addPrelightMenuItems       This hook is called to give plugins a chance to add pre-lighting menu items to the global Polygon - Color Set Editor menu.   addRMBBakingMenuItems       This hook is called to give plugins a chance to add baking menu items to the RMB menu.     * objectName (string): the name of the object the right mouse button event occured on.  addMayaRenderingPreferences       This hook is called to give plugins a chance to add custom preferences to the Maya's Rendering Preferences section.   updateMayaRenderingPreferences       This hook is called to give plugins a chance to update custom preferences of the Maya's Rendering Preferences section.   addMayaMuscleMenuItems       This hook is called to give plugins a chance to add menu items to the Maya muscle Displace menu.     * menuItemAnchor (string): the name of the menuItem which the new Maya muscle menu items should be inserted after.   addMayaMuscleShelfButtons       This hook is called to give plugins a chance to add items to the Maya muscle shelves.   addBackburnerRendererMenuItems       This hook is called to give plugins a chance to add items to Maya's Backburner list of available renderers. Note: The menuItem added must be named with the short name equivalent of the renderer. eg: The Maya software renderer adds a menuItem named 'sw'.   provideAETemplateForNodeType       This hook is called to give plugins a chance to provide a UI template for nodes which do not have a corresponding AE'nodeType'Template procedure.     * nodeType (string): the type of the node for which the AE is being constructed.    * returns (string): the name of a MEL command or procedure to use as the AETemplate for the requested node type.   AEnewMultiHandler       This hook is called to give plugins a chance to provide a UI creation handler for multi attributes.     * nodeName (string): the name of the node for which the AE is being constructed.    * atributeName (string): the name of the multi attribute.   * uiName (string): the UI name of the attribute.   * changedCommand (string): the MEL command or procedure to be executed when the value of the multi attribute is changed.   * elementIndexString (string): a colon separated list of indices at which the elements of the multi attribute live.   * returns (string): if the callback handled the attribute then it should return the full name of the topmost UI element that it created, otherwise it should return an empty string.  AEreplaceMultiHandler       This hook is called to give plugins a chance to provide an update handler for multi attributes.     * layoutName (string): the well defined name of the Maya UI component which represents the multi attribute (.   * nodeName (string): the name of the node for which the AE is being constructed.    * atributeName (string): the name of the multi attribute.   * changedCommand (string): the MEL command or procedure to be executed when the value of the multi attribute is changed.   * elementIndexString (string): a colon separated list of indices at which the elements of the multi attribute live.   * returns (int): Return 1 if the callback handled the multi attribute, Return 0 if Maya should provide its default handling.  AEnewAttributeHandler       This hook is called to give plugins a chance to provide a UI creation handler for attributes.     * nodeName (string): the name of the node for which the AE is being constructed.    * atributeName (string): the name of the attribute.   * uiName (string): the UI name of the attribute.   * changedCommand (string): the MEL command or procedure to be executed when the value of the attribute is changed.   * returns (string): if the callback handled the attribute then it should return the full name of the topmost UI element that it created, otherwise it should return an empty string.  AEreplaceAttributeHandler       This hook is called to give plugins a chance to provide an update handler for attributes.     * nodeName (string): the name of the node for which the AE is being constructed.    * atributeName (string): the name of the attribute.   * changedCommand (string): the MEL command or procedure to be executed when the value of the attribute is changed.   * returns (int): Return 1 if the callback handled the attribute, Return 0 if Maya should provide its default handling.  provideClassificationStrings       This hook must be supplied by all third parties that add nodes to the 'shader/surface' classification namespace.     * returns (string): a colon separated list representing the different plugin node classifications.  provideClassificationExclusionStrings       This hook is called to give plugins a chance to provide a list of classifications which should be filtered out from a nodeTreeLister category. For example a plugin might want to filter out nodes classified as both 'material' and 'legacy' out of the 'material' category.     * classification (string): the classification the nodeTreeBuilder is inquiring about.   * returns (string): a colon separated list representing the different classifications that should be excluded from the classification the nodeTreeBuilder is inquiring about.  provideClassificationStringsForFilteredTreeLister       This hook is called by 'createAssignNewMaterialTreeLister' and gives plugins a chance to append to the classification filter passed to the Tree Lister builder. It must return a string where each new classification is separated by a white space.     * currentFilterString (string): a white-space-separated string representing the current classifications.  nodeCanBeUsedAsMaterial       The hook is used by the RMB 'Assign Favorite Material' menu to determine which shading nodes can be used as materials. It must return 1 if the node can be used as a material node and 0 otherwise.     * nodeId (string): the node Id of the shading node being queried.   * nodeOwner (string): the name of the plugin the node belongs to.  addHeaderContentToMayaLambertianShadersAE       This hook is called to give plugins a chance to add content to the header of the Attribute Editor of Maya's Lambertian-​derived shaders.     * nodeName (string): the name of the node for which the Attribute Editor is being constructed.  provideNodeToAttrConnection       This hook is called to give plugins a chance to provide which output attribute should be used when a node is connected to an input attribute. If an input attribute type is given an output attribute of matching type should be returned. If no attribute type is specified (empty string) a preferred output attribute of any type can be returned. If no output attribute of matching type is available an empty string should be returned.     * nodeType (string): the node type of the node queried.   * attributeType (string): the data type of the input attribute.   * returns (string): the name of the output attribute to use.  provideNodeToNodeConnection       This hook is called to give plugins a chance to provide which attributes should be connected when a node to node connection is made. Both the source and destination attributes should be returned in a colon separated list, e.g. "src1:dst1:src2:dst2:src3:dst3"    * srcType (string): the node type of the source node.   * dstType (string): the node type of the destination node.   * returns (string): A colon separated list of source and destination attribute names.  provideOutputAttributeNameForTextureNode       This hook is called to give plugins a chance to provide a different output attribute name for Texture nodes. If this hook isn't provided 'outColor' is used.     * nodeName (string): the name of the texture node queried.   * returns (string): the output attribute name of the Texture node.  addItemsToHypergraphNodePopupMenu       This hook is called to give plugins a chance to add items to the Hypergraph node popup menu.     * nodeName (string): the name of the node for which the Hypergraph node menu is being constructed.  addItemsToRenderLayerEditorPopupMenu       This hook is called to give plugins a chance to add items to the Render Layer Editor popup menu.     * layerName (string): the name of the render layer for which the popup menu is being constructed.  preventMaterialDeletionFromCleanUpSceneCommand       This hook is called by the cleanUpScene command and gives the plugin a chance to communicate that a material node is still in use and shouldn't be deleted. The hook is called once per plug/connection pair of each shader instance.     * shader (string): the name of the shader node being deleted.   * plug (string): the name of the plug queried.   * connection (string): the name of the connection queried.  connectNodeToNodeOverrideCallback       This hook is called to give plugins a chance to redefine the behavior of drag and drop.     * srcNode (string): the name of the source node (the dragged node).   * dstNode (string): the name of the destination node (the dropped-on node).   * returns (int): Return 1 if Maya should perform the operation that would normally result from this connection. Return 0 to override and provide custom behavior.  prepareRenderChanged       This hook is called after an edit on a traversal set with the prepareRender command.   enableRenderPassMenuOfRenderView       This hook is called to give plugins a chance to tell Maya it should enable the render pass menu of the render view (under File->Load Render Pass). 'addRenderPassMenuItemsToRenderView' can be used to add items to this menu.     * returns (int): Return 1 if the plugin wants the render pass menu of the render view to be enabled. Return 0 otherwise.  addItemsToRenderPassMenuOfRenderView       This hook is called to give plugins a chance to add menu items to the 'render pass' menu of the render view (under File->Load Render Pass). 'enableRenderPassMenuOfRenderView' can be used to enable the render pass menu of the render view.   addItemsToRMBMenuOfTreeLister       This hook is called to give plugins a chance to populate the RMB menu of nodes listed in a tree lister. Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the RMB menu.     * nodeType (string): The node type of the tree lister node for which the RMB menu is being built.   * scriptCommand (string): The script command associated with the tree lister node for which the RMB menu is being built.   * returns (int): Return 0 if Maya should append its own items to the menu of the current node type. This should be the return value for all node types a plugin isn't explicitly interested in. Return 1 if Maya shouldn't add any of its items to the menu of the current node type. Note: All menu items related to managing the 'Favorites' section of the tree lister will always be added to the RMB menu regardless of the return value (those are treated as special cases).  saveCustomNodePresetAttributes       This hook is called to give plugins a chance to store extra commands in the node preset file being saved.     * presetNodeToSave (string): The name of the preset node being saved.   * returns (string): The custom procedure to use to generate the mel script to be appended to the nodePreset -custom flag of the current presetNode save event (see the documentation of the nodePreset command for more information on the format of the -custom flag).  addItemToFileMenu       This hook is called to give plugins a chance to add menu items to the main File menu.   addItemToCreateLightMenu       This hook is called to give plugins a chance to add menu items to the create light menu.  textureReload       This hook is called to give plugins a chance to update all nodes that reference the texture file.     * file (string): the file path of the texture to reload.  renderSettingsBuilt       This hook is called after the render settings window has been built.  rendererAddOneTabToGlobalsWindowCreateProc       This hook is called to allow renderers the opportunity to add renderer specific tabs to the unified render globals window (render settings window).     * createProc (string): the name of the procedure used to create the content of the tab.   shouldEarlyReturnFromUpdateMultiCameraBufferNamingMenu       This hook is called to allow users to early return from the updateMultiCameraBufferNamingMenu() function by returning "true" in the callback handler.     * returns (string): Returns "true" if the caller wishes to early return from the updateMultiCameraBufferNamingMenu() function.  shouldEarlyReturnFromUpdateMayaSoftwareImageFormatControl       This hook is called to allow users to early return from the updateMayaSoftwareImageFormatControl() function by returning "true" in the callback handler.     * returns (string): Returns "true" if the caller wishes to early return from the updateMayaSoftwareImageFormatControl() function.  shouldEarlyReturnFromUpdateDefaultTraversalSetMenu       This hook is called to allow users to early return from the updateDefaultTraversalSetMenu() function by returning "true" in the callback handler.     * returns (string): Returns "true" if the caller wishes to early return from the updateDefaultTraversalSetMenu() function.  shouldEarlyReturnFromShouldAppearInNodeCreateUI       This hook is called to allow users to early return from the shouldAppearInNodeCreateUI() function by returning "true" in the callback handler.     * returns (string): Returns "true" if the caller wishes to early return from the shouldAppearInNodeCreateUI() function.  updateAE       This hook is called at the end of the updateAE() function.

-----------------------------------------

dc    : dumpCallbacks   [boolean] []
    Gives a list of all the registered callbacks for all hooks and owners. Can be useful for debugging.

-----------------------------------------

ec    : executeCallbacks [boolean] []
    Execute the callbacks for the specified hook, passing the extra arguments to each callback when it is executed. Returns an array (MEL) or list (Python) containing the return values from each callback that was executed. If a callback returns no value, the array will contain an empty string (MEL) or None (Python).

-----------------------------------------

h     : hook            [string] []
    The name of the hook for which the callback should be registered.

-----------------------------------------

lc    : listCallbacks   [boolean] []
    Get the list of callbacks for the specified hook name. If the owner is specified, only callbacks for the specified hook and owner will be listed.

-----------------------------------------

o     : owner           [string] []
    The name of the owner registering the callback. This is typically a plugin name.

-----------------------------------------

rc    : removeCallback  [script]
    Remove an existing callback for the specified hook name. The owner must also be specified when removing a callback.

    """

def commandEcho(q=1,af="string[]",f="string[]",ln=1,st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/commandEcho.html



-----------------------------------------

commandEcho is undoable, queryable, and NOT editable.

This command controls what is echoed to the command window.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : addFilter       [string[]] []
    This flag allows you to append filters to the current list of filtered commands when echo all commands is enabled. Just like the filter flag, you can provide a partial command name, so all commands that start with a substring specified in the addFilter entry will be filtered out.

-----------------------------------------

f     : filter          [string[]] ['query']
    This flag allows you to filter out unwanted commands when echo all commands is enabled. You can provide a partial command name, so all commands that start with a substring specified in filter entry will be filtered out. If filter is empty, all commands are echoed to the command window.

-----------------------------------------

ln    : lineNumbers     [boolean] ['query']
    If true then file name and line number information is provided in error and warning messages. If false then no file name and line number information is provided in error and warning messages.

-----------------------------------------

st    : state           [boolean]
    If true then all commands are echoed to the command window. If false then only relevant commands are echoed.

    """

def condition(q=1,e=1,delete=1,d="string",i=1,s="string",st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/condition.html



-----------------------------------------

condition is undoable, queryable, and editable.

This command creates a new named condition object whose true/false value is
calculated by running a mel script. This new condition can then be used for
dimming, or controlling other scripts, or whatever.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

delete : delete          [boolean] []
    Deletes the condition.

-----------------------------------------

d     : dependency      [string] []
    Each -dependency flag specifies another condition that the new condition will be dependent on. When any of these conditions change, the new-state- script will run, and the state of this condition will be set accordingly. It is possible to define infinite loops, but they will be caught and handled correctly at run-time.

-----------------------------------------

i     : initialize      [boolean] []
    Initializes the condition, by forcing it to run its script as soon as it is created. If this flag is not specified, the script will not run until one of the dependencies is triggered.

-----------------------------------------

s     : script          [string] []
    The script that determines the new state of the condition.

-----------------------------------------

st    : state           [boolean]
    Sets the state of the condition. This can be used to create a manually triggered condition: you could create a condition without any dependencies and without a new-state-script. This condition would only change state in response to the -st/state flag.

    """

def connectControl(fi=1,index="uint",pcm=1,po=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/connectControl.html



-----------------------------------------

connectControl is undoable, NOT queryable, and NOT editable.

This command attaches a UI widget, specified as the first argument, to one or
more dependency node attributes. The attributes/nodes don't have to exist yet,
they will get looked up as needed. With no flag specified, this command works
on these kinds of controls: floatField, floatScrollBar, floatSlider, intField,
intScrollBar, intSlider, floatFieldGrp, intFieldGrp, checkBox,
radioCollection, and optionMenu. With the index flag, It will also work on the
individual components of all other groups.

This command sets up a two-way connection between the control and the (first-
specified) attribute. If this first attribute is changed in any way, the
control will be appropriately updated to match its value.

Summary: if you change the control, ALL the connected attributes change. If
you change the FIRST attribute attached to the control, then the control will
change.

NOTE: the two-way connection will not be established if the attributes do not
exist when the connectControl command is run. If the user later uses the
control, the connection will be established at that time.

To effectively use connectControl with radioCollections and optionMenus, you
must attach a piece of data to each radioButton and menuItem. This piece of
data (an integer) can be attached using the data flag in the radioButton and
menuItem commands. When the button/item is selected, the attribute will be set
to the value of its data. When the attribute is changed, the collection (or
optionMenu) will switch to the item that matches the new attribute value. If
no item matches, it will be left unchanged.

There are some specialized controls that have connection capability (and more)
built right into them. See attrFieldSliderGrp, attrFieldGrp, and
attrColorSliderGrp. Using these classes can be easier than using
connectControl.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

fi    : fileName        [boolean] []
    This flag causes the connection to be treated as a filename, and the conversion from internal to external filename representation is made as the data is copied. This only applies to connections to Tfield controls.

-----------------------------------------

index : index           [uint] []
    This flag enables you to pick out a sub-control from a group that contains a number of different controls. For example, you can connect one field of a floatFieldGrp. You must count each member of the group, including any text labels that may exist. For example, if you have a check box group with a label, the label will count as index 1, and the first check box as index 2. (Indices are 1-based)

-----------------------------------------

pcm   : preventContextualMenu [boolean] []
    If true, this flag will block the right mouse button menu of the associated control attribute.

-----------------------------------------

po    : preventOverride [boolean]
    If true, this flag disallows overriding the control's attribute via the control's right mouse button menu.

    """

def deleteUI(cl=1,ctl=1,ed=1,lay=1,m=1,mi=1,pnl=1,pc=1,ric=1,tc=1,uit=1,wnd=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/deleteUI.html



-----------------------------------------

deleteUI is undoable, NOT queryable, and NOT editable.

This command deletes UI objects such as windows and controls. Deleting a
layout or window will also delete all of its children. If a flag is used then
all objects being deleted must be of the specified type. This command may not
be edited or queried.

NOTE: it is recommended that the type flags be used to disambiguate different
kinds of objects with the same name.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cl    : collection      [boolean] []
    Object names for deletion are all radio or tool collections.

-----------------------------------------

ctl   : control         [boolean] []
    Object names for deletion are all controls.

-----------------------------------------

ed    : editor          [boolean] []
    Object names for deletion are all editors.

-----------------------------------------

lay   : layout          [boolean] []
    Object names for deletion are all layouts.

-----------------------------------------

m     : menu            [boolean] []
    Object names for deletion are all menus.

-----------------------------------------

mi    : menuItem        [boolean] []
    Object names for deletion are all menu items.

-----------------------------------------

pnl   : panel           [boolean] []
    Object names for deletion are all panels.

-----------------------------------------

pc    : panelConfig     [boolean] []
    Object names for deletion are panel configurations.

-----------------------------------------

ric   : radioMenuItemCollection [boolean] []
    Object names for deletion are all radio menu item collections.

-----------------------------------------

tc    : toolContext     [boolean] []
    Object names for deletion are all tool contexts.

-----------------------------------------

uit   : uiTemplate      [boolean] []
    Object names for deletion are all UI templates.

-----------------------------------------

wnd   : window          [boolean]
    Object names for deletion are all windows.

    """

def dimWhen(c=1,f=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dimWhen.html



-----------------------------------------

dimWhen is undoable, NOT queryable, and NOT editable.

This method attaches the named UI object (first argument) to the named
condition (second argument) so that the object will be dimmed when the
condition is in a particular state.

This command will fail if the object does not exist. If the condition does not
exist (yet), that's okay --- a placeholder will be used until such a condition
comes into existence.

The UI object should be one of two things, either a control or a menu item.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

c     : clear           [boolean] []
    Remove the condition on the specified dimmable.

-----------------------------------------

f     : false           [boolean] []
    Dim the object when the condition is false.

-----------------------------------------

t     : true            [boolean]
    Dim the object when the condition is true. (default)

    """

def disable(v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/disable.html



-----------------------------------------

disable is undoable, NOT queryable, and NOT editable.

This command enables or disables the control passed as argument.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

v     : value           [boolean]
    If true, this command disables the control. If false, this command enables the control. Default value is true (disable)

    """

def eval():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/eval.html



-----------------------------------------

eval is NOT undoable, NOT queryable, and NOT editable.

This function takes a string which contains MEL code and evaluates it using
the MEL interpreter. The result is converted into a Python data type and is
returned. If an error occurs during the execution of the MEL script, a Python
exception is raised with the appropriate error message.


-----------------------------------------


Return Value:

Any  depending on input.
    """

def evalDeferred(en=1,ls=1,low=1,lp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/evalDeferred.html



-----------------------------------------

evalDeferred is undoable, NOT queryable, and NOT editable.

This command takes the string it is given and evaluates it during the next
available idle time. It is useful for attaching commands to controls that can
change or delete the control.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

en    : evaluateNext    [boolean] []
    Specified that the command to be executed should be ran with the highest priority, ideally queued up next.

-----------------------------------------

ls    : list            [boolean] []
    Return a list of the command strings that are currently pending on the idle queue. By default, it will return the list of commands for all priorities. The -lowestPriority and -lowPriority can be used to restrict the list of commands to a given priority level.

-----------------------------------------

low   : lowPriority     [boolean] []
    Specified that the command to be executed should be deferred with the low priority. That is, it will be executed whenever Maya is idle.

-----------------------------------------

lp    : lowestPriority  [boolean]
    Specified that the command to be executed should be deferred with the lowest priority. That is, it will be executed when no other idle events are scheduled.

    """

def isTrue():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/isTrue.html



-----------------------------------------

isTrue is undoable, NOT queryable, and NOT editable.

This commmand returns the state of the named condition. If the condition is
true, it returns 1. Otherwise it returns 0.


-----------------------------------------


Return Value:

None
    """

def itemFilter(q=1,e=1,bk="string",bn="string",bs="string",bt="string",cat="string",cls="string",cbk=1,cbt=1,di="[string, string]",ex=1,intersect="[string, string]",lbf=1,lof=1,luf=1,neg=1,p="string",pym="string",ss="string",t="string",un="[string, string]",unn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/itemFilter.html



-----------------------------------------

itemFilter is undoable, queryable, and editable.

This command creates a named itemFilter object. This object can be attached to
selectionConnection objects, or to editors, in order to filter the item lists
going through them. Using union, intersection and difference filters, complex
composite filters can be created.


-----------------------------------------


Return Value:

string  Single command result    
string[]  Multiple command result  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bk    : byBin           [string] ['query', 'edit']
    The filter will only pass items whose bin list contains the given string as a bin name.   This is a multi-use flag.   If more than one occurance of this flag is used in a single command, the filter will accept a node if it matches at least one of the given bins (in other words, a union or logical or of all given bins.

-----------------------------------------

bn    : byName          [string] ['query', 'edit']
    The filter will only pass items whose names match the given regular expression string. This string can contain the special characters * and ?. '?' matches any one character, and '*' matches any substring.

-----------------------------------------

bs    : byScript        [string] ['query', 'edit']
    The filter will run a MEL script named by the given string on each item name. Items will pass the filter if the script returns a non-zero value. The script name string must be the name of a proc whose signature is:   global proc int procName( string $name )   or   def procName(*args, **keywordArgs)   if -pym/pythonModule is specified. Note that if -secondScript is also used, it will always take precedence.

-----------------------------------------

bt    : byType          [string] ['query', 'edit']
    The filter will only pass items whose typeName matches the given string. The typeName of an object can be found using the nodeType command. This is a multi-use flag. If more than one occurance of this flag is used in a single command, the filter will accept a node if it matches at least one of the given types (in other words, a union or logical or of all given types.

-----------------------------------------

cat   : category        [string] ['query', 'edit']
    A string for categorizing the filter.

-----------------------------------------

cls   : classification  [string] ['query', 'edit']
    Indicates whether the filter is a built-in or user filter. The string argument must be either "builtIn" or "user". The "other" classification is deprecated. Use "user" instead. Filters will not be deleted by a file new, and filter nodes will be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and will not be accessible from the command-line.

-----------------------------------------

cbk   : clearByBin      [boolean] ['edit']
    This flag will clear any existing bins associated with this filter.

-----------------------------------------

cbt   : clearByType     [boolean] ['edit']
    This flag will clear any existing typeNames associated with this filter.

-----------------------------------------

di    : difference      [[string, string]] ['query', 'edit']
    The filter will consist of the set difference of two other filters, whose names are the given strings. Items will pass this filter if and only if they pass the first filter but not the second filter.

-----------------------------------------

ex    : exists          [boolean] []
    Returns true|false depending upon whether the specified object exists. Other flags are ignored.

-----------------------------------------

intersect : intersect       [[string, string]] ['query', 'edit']
    The filter will consist of the intersection of two other filters, whose names are the given strings. Items will pass this filter if and only if they pass both of the contained filters.

-----------------------------------------

lbf   : listBuiltInFilters [boolean] ['query']
    Returns an array of all item filters with classification "builtIn".

-----------------------------------------

lof   : listOtherFilters [boolean] ['query']
    The "other" classification is deprecated. Use "user" instead. Returns an array of all item filters with classification "other".

-----------------------------------------

luf   : listUserFilters [boolean] ['query']
    Returns an array of all item filters with classification "user".

-----------------------------------------

neg   : negate          [boolean] ['query', 'edit']
    This flag can be used to cause the filter to invert itself, and reverse what passes and what fails.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Optional. If specified, the filter's life-span is linked to that of the parent. When the parent goes out of scope, so does the filter. If not specified, the filter will exist until explicitly deleted.

-----------------------------------------

pym   : pythonModule    [string] ['query', 'edit']
    Treat -bs/byScript and -ss/secondScript as Python functions located in the specified module.

-----------------------------------------

ss    : secondScript    [string] ['query', 'edit']
    Cannot be used in conjunction with the -bs flag. The second script is for filtering whole lists at once, rather than individually. Its signature must be:   global proc string[] procName( string[] $name )   or   def procName(*args, **keywordArgs)   if -pym/pythonModule is specified. It should take in a list of items, and return a filtered list of items.

-----------------------------------------

t     : text            [string] ['query', 'edit']
    Defines an annotation string to be stored with the filter

-----------------------------------------

un    : union           [[string, string]] ['query', 'edit']
    The filter will consist of the union of two other filters, whose names are the given strings. Items will pass this filter if they pass at least one of the contained filters.

-----------------------------------------

unn   : uniqueNodeNames [boolean]
    Returns unique node names to script filters so there are no naming conflicts.

    """

def itemFilterAttr(q=1,e=1,bn="string",bns="string",bs="string",cls="string",dy=1,ex=1,hc=1,hdk=1,he=1,h=1,intersect="[string, string]",k=1,lbf=1,lof=1,luf=1,neg=1,p="string",pub=1,r=1,srt=1,ss="string",t="string",un="[string, string]",w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/itemFilterAttr.html



-----------------------------------------

itemFilterAttr is undoable, queryable, and editable.

This command creates a named itemFilterAttr object. This object can be
attached to editors, in order to filter the attributes going through them.
Using union and intersection filters, complex composite filters can be
created.


-----------------------------------------


Return Value:

string  Single command result    
string[]  Multiple command result  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bn    : byName          [string] ['query', 'edit']
    The filter will only pass items whose names match the given regular expression string. This string can contain the special characters * and ?. '?' matches any one character, and '*' matches any substring.   This flag cannot be used in conjunction with the -byScript or -secondScript flags.

-----------------------------------------

bns   : byNameString    [string] ['query', 'edit']
    The filter will only pass items whose names match the given string. This is a multi-use flag which allows the user to specify several strings. The filter will pass items that match any of the strings.   This flag cannot be used in conjunction with the -byScript or -secondScript flags.

-----------------------------------------

bs    : byScript        [string] ['query', 'edit']
    The filter will run a MEL script named by the given string on each attribute name. Attributes will pass the filter if the script returns a non- zero value. The script name string must be the name of a proc whose signature is:   global proc int procName( string $nodeName string $attrName )      This flag cannot be used in conjunction with the -byName or -byNameString flags.

-----------------------------------------

cls   : classification  [string] ['query', 'edit']
    Indicates whether the filter is a built-in or user filter. The string argument must be either "builtIn" or "user". The "other" filter classification is deprecated. Use "user" instead. Filters created by Maya should be classified as "builtIn". Filters created by plugins or user scripts should be classified as "user". Filters will not be deleted by a file new. Filter nodes will be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and will not be accessible from the command-line.

-----------------------------------------

dy    : dynamic         [boolean] ['query', 'edit']
    The filter will only pass dynamic attributes

-----------------------------------------

ex    : exists          [boolean] ['query', 'edit']
    The filter will only pass attributs that exist

-----------------------------------------

hc    : hasCurve        [boolean] ['query', 'edit']
    The filter will only pass attributes that are driven by animation curves.

-----------------------------------------

hdk   : hasDrivenKey    [boolean] ['query', 'edit']
    The filter will only pass attributes that are driven by driven keys

-----------------------------------------

he    : hasExpression   [boolean] ['query', 'edit']
    The filter will only pass attributes that are driven by expressions

-----------------------------------------

h     : hidden          [boolean] ['query', 'edit']
    The filter will only pass attributes that are hidden to the user

-----------------------------------------

intersect : intersect       [[string, string]] ['query', 'edit']
    The filter will consist of the intersection of two other filters, whose names are the given strings. Attributes will pass this filter if and only if they pass both of the contained filters.

-----------------------------------------

k     : keyable         [boolean] ['query', 'edit']
    The filter will only pass attributes that are keyable

-----------------------------------------

lbf   : listBuiltInFilters [boolean] ['query']
    Returns an array of all attribute filters with classification "builtIn".

-----------------------------------------

lof   : listOtherFilters [boolean] ['query']
    The "other" classification has been deprecated. Use "user" instead. Returns an array of all attribute filters with classification "other".

-----------------------------------------

luf   : listUserFilters [boolean] ['query']
    Returns an array of all attribute filters with classification "user".

-----------------------------------------

neg   : negate          [boolean] ['query', 'edit']
    This flag can be used to cause the filter to invert itself, and reverse what passes and what fails.

-----------------------------------------

p     : parent          [string] []
    This flag is no longer supported.

-----------------------------------------

pub   : published       [boolean] ['query', 'edit']
    The filter will only pass attributes that are published on the container.

-----------------------------------------

r     : readable        [boolean] ['query', 'edit']
    The filter will only pass attributes that are readable (outputs)

-----------------------------------------

srt   : scaleRotateTranslate [boolean] ['query', 'edit']
    The filter will show only SRT attributes: scale, rotate, translate and their children

-----------------------------------------

ss    : secondScript    [string] ['query', 'edit']
    Can be used in conjunction with the -bs flag. The second script is for filtering whole lists at once, rather than individually. Its signature must be:   global proc string[] procName( string[] $nodeName string[] $attrName )   It should take in a list of attributes, and return a filtered list of attributes.   This flag cannot be used in conjunction with the -byName or -byNameString flags.

-----------------------------------------

t     : text            [string] ['query', 'edit']
    Defines an annotation string to be stored with the filter

-----------------------------------------

un    : union           [[string, string]] ['query', 'edit']
    The filter will consist of the union of two other filters, whose names are the given strings. Attributes will pass this filter if they pass at least one of the contained filters.

-----------------------------------------

w     : writable        [boolean]
    The filter will only pass attributes that are writable (inputs)

    """

def itemFilterType(q=1,e=1,t="string",typ=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/itemFilterType.html



-----------------------------------------

itemFilterType is undoable, queryable, and editable.

This command queries a named itemFilter object. This object can be attached to
selectionConnection objects, or to editors, in order to filter the item lists
going through them. Using union and intersection filters, complex composite
filters can be created.


-----------------------------------------


Return Value:

string  Single command result    
string[]  Multiple command result  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

t     : text            [string] ['query', 'edit']
    Defines an annotation string to be stored with the filter

-----------------------------------------

typ   : type            [boolean]
    Query the type of the filter object. Possible return values are: itemFilter, attributeFilter, renderFilter, or unknownFilter.

    """

def lsUI(ct=1,col=1,ctx=1,cl=1,ctl=1,dw=1,ed=1,hd="int",l=1,mi=1,m=1,nw=1,p=1,rmc=1,tl="int",typ="string",wnd=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lsUI.html



-----------------------------------------

lsUI is undoable, NOT queryable, and NOT editable.

This command returns the names of UI objects.


-----------------------------------------


Return Value:

string[]  The names of the object arguments.


-----------------------------------------


Flags:

-----------------------------------------

ct    : cmdTemplates    [boolean] []
    UI command templates created using ELF UI commands.

-----------------------------------------

col   : collection      [boolean] []
    Control collections created using ELF UI commands.

-----------------------------------------

ctx   : contexts        [boolean] []
    Tool contexts created using ELF UI commands.

-----------------------------------------

cl    : controlLayouts  [boolean] []
    Control layouts created using ELF UI commands [e.g. formLayouts, paneLayouts, etc.]

-----------------------------------------

ctl   : controls        [boolean] []
    Controls created using ELF UI commands. [e.g. buttons, checkboxes, etc]

-----------------------------------------

dw    : dumpWidgets     [boolean] []
    Dump all QT widgets used by Maya.

-----------------------------------------

ed    : editors         [boolean] []
    All currently existing editors.

-----------------------------------------

hd    : head            [int] []
    The parameter specifies the maximum number of elements to be returned from the beginning of the list of items. (Note: each flag will return at most this many items so if multiple flags are specified then the number of items returned will be greater than the value specified).

-----------------------------------------

l     : long            [boolean] []
    Use long pathnames instead of short non-path names.

-----------------------------------------

mi    : menuItems       [boolean] []
    Menu items created using ELF UI commands.

-----------------------------------------

m     : menus           [boolean] []
    Menus created using ELF UI commands.

-----------------------------------------

nw    : numWidgets      [boolean] []
    Reports the number of QT widgets used by Maya.

-----------------------------------------

p     : panels          [boolean] []
    All currently existing panels.

-----------------------------------------

rmc   : radioMenuItemCollections [boolean] []
    Menu item collections created using ELF UI commands.

-----------------------------------------

tl    : tail            [int] []
    The parameter specifies the maximum number of elements to be returned from the end of the list of items. (Note: each flag will return at most this many items so if multiple flags are specified then the number of items returned will be greater than the value specified).

-----------------------------------------

typ   : type            [string] []
    List all objects of a certain type specified by the string argument. For example, "window", "menu", "control", or "controlLayout".

-----------------------------------------

wnd   : windows         [boolean]
    Windows created using ELF UI commands.

    """

def melOptions(q=1,dvw=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/melOptions.html



-----------------------------------------

melOptions is NOT undoable, queryable, and NOT editable.

Set and query options that affect the behavior of Maya's Embedded Language
(MEL).


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dvw   : duplicateVariableWarnings [boolean]
    When turned on, this option will cause a warning to be generated whenever a MEL variable is declared within the same scope as another variable with the same name. The warnings will be generated when the script is sourced, not when it is executed. Usually these warnings indicate an error in the script.  On query the current setting of the option will be returned.  The corresponding preference optionVar is melDuplicateVariableWarnings.

    """

def objectTypeUI(i="string",la=1,sc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/objectTypeUI.html



-----------------------------------------

objectTypeUI is undoable, NOT queryable, and NOT editable.

This command returns the type of UI element such as button, sliders, etc.


-----------------------------------------


Return Value:

string  The type of the specified object.


-----------------------------------------


Flags:

-----------------------------------------

i     : isType          [string] []
    Returns true|false if the object is of the specified type.

-----------------------------------------

la    : listAll         [boolean] []
    Returns a list of all known UI commands and their respective types. Each entry contains three strings which are the command name, ui type and class name. Note that the class name is internal and is subject to change.

-----------------------------------------

sc    : superClasses    [boolean]
    Returns a list of the names of all super classes for the given object. Note that all class names are internal and are subject to change.

    """

def optionVar(q=1,arraySize="string",ca="string",ex="string",fv="[string, float]",fva="[string, float]",iv="[string, int]",iva="[string, int]",l=1,rm="string",rfa="[string, int]",sv="[string, string]",sva="[string, string]",v="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/optionVar.html



-----------------------------------------

optionVar is undoable, queryable, and NOT editable.

This command allows you to set and query variables which are persistent
between different invocations of Maya. These variables are stored as part of
the preferences.


-----------------------------------------


Return Value:

int  0 or 1 for the exists option    
string[]  When the list option is used  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

arraySize : arraySize       [string] []
    returns the size of the array named "string". If no such variable exists, it returns 0. If the variable is not an array, it returns 1.

-----------------------------------------

ca    : clearArray      [string] []
    If there is an array named "string", it is set to be empty. Empty arrays are not saved.

-----------------------------------------

ex    : exists          [string] []
    returns 1 if a variable named "string" exists, 0 otherwise. All other flags will be ignored if this is used. (Query has higher precedence)

-----------------------------------------

fv    : floatValue      [[string, float]] []
    creates a new variable named "string" with double value "float". If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different)

-----------------------------------------

fva   : floatValueAppend [[string, float]] []
    adds this value to the end of the array of floats named "string". If no such array exists, one is created. If there was a float value with this name before, it becomes the first element of the array. If any other kind of value existed, it is overridden.

-----------------------------------------

iv    : intValue        [[string, int]] []
    creates a new variable named "string" with integer value "int". If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).

-----------------------------------------

iva   : intValueAppend  [[string, int]] []
    adds this value to the end of the array of ints named "string". If no such array exists, one is created. If there was an int value with this name before, it becomes the first element of the array. If any other kind of value existed, it is overridden.

-----------------------------------------

l     : list            [boolean] []
    this returns a list of all the defined variable names. All other flags will be ignored if this one is used. (Query and exists flags have a higher precedence).

-----------------------------------------

rm    : remove          [string] []
    removes the variable named "string", if one exists.   Note: all removals are done before any value setting, if both the -r and other (-sv, -iv, -fv) flags are used in the same command.

-----------------------------------------

rfa   : removeFromArray [[string, int]] []
    removes the element numbered "int" in the array named "string". Everything beyond it then gets shuffled down.

-----------------------------------------

sv    : stringValue     [[string, string]] []
    creates a new variable named using the first string with value given by the second string. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different)

-----------------------------------------

sva   : stringValueAppend [[string, string]] []
    adds the value given by the second string to the end of the array of strings named by the first string. If no such array exists, one is created. If there was a string value with this name before, it becomes the first element of the array. If any other kind of value existed, it is overridden.

-----------------------------------------

v     : version         [int]
    Preferences version number to warn about incompatbile preference files

    """

def pause(sec="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pause.html



-----------------------------------------

pause is undoable, NOT queryable, and NOT editable.

Pause for a specified number of seconds for canned demos or for test scripts
to allow user to view results.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

sec   : seconds         [int]
    Pause for the specified number of seconds.

    """

def refresh(cv=1,fe="string",fn="string",f=1,su=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/refresh.html



-----------------------------------------

refresh is undoable, NOT queryable, and NOT editable.

This command is used to force a redraw during script execution. Normally,
redraw is suspended while scripts are executing but sometimes it is useful to
show intermediate results for purposes such as capturing images from the
screen.

If the -cv flag is specified, then only the current active view is redrawn.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cv    : currentView     [boolean] []
    Redraw only the current view (default redraws all views).

-----------------------------------------

fe    : fileExtension   [string] []
    Specify the type of file to save using the filename flag.

-----------------------------------------

fn    : filename        [string] []
    Specify the name of a file in which to save a snapshot of the viewports, or just the current one if the currentView flag is set.

-----------------------------------------

f     : force           [boolean] []
    Force the refresh regardless of the state of the model.

-----------------------------------------

su    : suspend         [boolean]
    Suspends or resumes Maya's handling of refresh events. Specify "on" to suspend refreshing, and "off" to resume refreshing. Note that resuming refresh does not itself cause a refresh -- the next natural refresh event in Maya after "refresh -suspend off" is issued will cause the refresh to occur. Use this flag with caution: although it provides opportunities to enhance performance, much of Maya's dependency graph evaluation in interactive mode is refresh driven, thus use of this flag may lead to slight solve differences when you have a complex dependency graph with interrelations.

    """

def renameUI():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renameUI.html



-----------------------------------------

renameUI is undoable, NOT queryable, and NOT editable.

This command renames the UI object passed as first arument to the new name
specified as second argument. If the new name is a duplicate, or not valid,
then re-naming fails and the old name is returned.

## Notes

This command does not update other objects or commands that reference this
object by name, so use this command at your own risk.


-----------------------------------------


Return Value:

string  The new name, or the old name if re-naming fails.
    """

def resourceManager(nf="string",s="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/resourceManager.html



-----------------------------------------

resourceManager is NOT undoable, NOT queryable, and NOT editable.

List resources matching certain properties.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

nf    : nameFilter      [string] []
    List only resources matching the name. Argument may contain ? and * characters.

-----------------------------------------

s     : saveAs          [[string, string]]
    Saves a copy of the resource (first parameter) as a separate file (second parameter).

    """

def scriptJob(alc=1,aa="[string, script]",ac="[string, script]",ad="[string, script]",cu=1,cc="[string, script]",cf="[string, script]",ct="[string, script]",con="[string, script]",dri=1,event="[string, script]",ex="int",f=1,ie="script",k="int",ka=1,kws=1,lc=1,le=1,lj=1,nd="[string, script]",nnc="[string, script]",ovc="[string, script]",p="string",per=1,pro=1,rp=1,ro=1,tc="script",uid="[string, script]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/scriptJob.html



-----------------------------------------

scriptJob is undoable, NOT queryable, and NOT editable.

This command creates a "script job", which is a MEL command or script. This
job is attached to the named condition, event, or attribute. Each time the
condition switches to the desired state (or the trigger is triggered, etc),
the script is run.

Script jobs are tied to the event loop in the interactive application. They
are run during idle events. This means that script jobs do not exist in the
batch application. The scriptJob command does nothing in batch mode.

This triggering happens very frequently so for speed considerations no events
are forwarded during playback. This means that you cannot use scriptJob -tc
tcCallback; to alter animation behaviour. Use an expression instead, or the
rendering callbacks "preRenderMel" and "postRenderMel".

When setting up jobs for conditions, it is invalid to setup jobs for the true
state, false state, and state change at the same time. The behaviour is
undefined. The user can only setup jobs for the true and/or false state, or
only for the state change, but not three at the same time. i.e. if you do:

    
    
    
    
    
    // Set up a job that runs for the life of the application.
    // This job cannot be deleted with the "kill" command no matter what.
    scriptJob -e "SelectionChanged" "print \"Annoying Message!\\n\"" -permanent;
    
    
    
    // set up a job for the true state
    scriptJob -ct "playingBack" playBackCallback;
    
    
    
    
    
    // set up a job for the false state
    scriptJob -cf "playingBack" playBackCallback;
    
    
    
    
    
    then you should NOT do
    scriptJob -cc "playingBack" playBackCallback;
    otherwise it will lead to undefined behaviour.
    

This command can also be used to list available conditions and events, and to
kill running jobs.


-----------------------------------------


Return Value:

int  The job number, which can be used to kill the job. The job number will be
a value greater than or equal to zero    
string[]  A string list when the list flag is used  
boolean  For the exists flag.


-----------------------------------------


Flags:

-----------------------------------------

alc   : allChildren     [boolean] []
    This flag can only be used in conjunction with the -ac/attributeChange flag. If it is specified, and the job is attached to a compound attribute, then the job will run due to changes to the specified attribute as well as changes to its children.

-----------------------------------------

aa    : attributeAdded  [[string, script]] []
    Run the script when the named attribute is added. The string must identify both the dependency node and the particular attribute. If the dependency node is deleted, this job is killed (even if the deletion is undoable).

-----------------------------------------

ac    : attributeChange [[string, script]] []
    Run the script when the named attribute changes value. The string must identify both the dependency node and the particular attribute. If the dependency node is deleted, this job is killed (even if the deletion is undoable).

-----------------------------------------

ad    : attributeDeleted [[string, script]] []
    Run the script when the named attribute is deleted. The string must identify both the dependency node and the particular attribute. If the dependency node is deleted, this job is killed (even if the deletion is undoable).

-----------------------------------------

cu    : compressUndo    [boolean] []
    If this is set to true, and the scriptJob is undoable, then its action will be bundled with the last user action for undo purposes. For example; if the scriptJob was triggered by a selection change, then pressing undo will undo both the scriptJob and the selection change at the same time.

-----------------------------------------

cc    : conditionChange [[string, script]] []
    Run the script when the named condition changes state. The string must be the name of a pre-defined, or a user-defined boolean condition. To get a list of what conditions exist, use the -listConditions flag.

-----------------------------------------

cf    : conditionFalse  [[string, script]] []
    Run the script when the named condition becomes false. The string must be the name of a pre-defined, or a user-defined boolean condition. To get a list of what conditions exist, use the -listConditions flag.

-----------------------------------------

ct    : conditionTrue   [[string, script]] []
    Run the script when the named condition becomes true. The string must be the name of a pre-defined, or a user-defined boolean condition. To get a list of what conditions exist, use the -listConditions flag.

-----------------------------------------

con   : connectionChange [[string, script]] []
    Run the script when the named attribute changes its connectivity. The string must identify both the dependency node and the particular attribute. If the dependency node is deleted, this job is killed (even if the deletion is undoable).

-----------------------------------------

dri   : disregardIndex  [boolean] []
    This flag can only be used in conjunction with the -ac/attributeChange flag. If it is specified, and the job is attached to a multi (indexed) attribute, then the job will run no matter which attribute in the multi changes.

-----------------------------------------

e     : event           [[string, script]] []
    Run the script when the named event occurs. This string must be the name of a pre-defined maya event. To get a list of what events exist, use the -listEvents flag.

-----------------------------------------

ex    : exists          [int] []
    Returns true if a scriptJob with the specified "job number" exists, and false otherwise. The "job number" should be a value that was returned on creation of a new scriptJob.

-----------------------------------------

f     : force           [boolean] []
    This flag can only be used with -kill, -killAll, or -replacePrevious. It enables the deletion of protected jobs.

-----------------------------------------

ie    : idleEvent       [script] []
    Run the script every time maya is idle. WARNING, as long as an idle event is is registered, the application will keep calling it and will use up all available CPU time. Use idleEvents with caution.

-----------------------------------------

k     : kill            [int] []
    Kills the job with the specified job number. Permanent jobs cannot be killed, however, and protected jobs can only be killed if the -force flag is used in the command.

-----------------------------------------

ka    : killAll         [boolean] []
    Kills all jobs. Permanent jobs will not be deleted, and protected jobs will only be deleted if the -force flag is used.

-----------------------------------------

kws   : killWithScene   [boolean] []
    Attaches the job to the current scene, and when the scene is emptied. The current scene is emptied by opening a new or existing scene.

-----------------------------------------

lc    : listConditions  [boolean] []
    This causes the command to return a string array containing the names of all existing conditions. Below is the descriptions for all the existing conditions:  ### Events Based on Available Maya Features  These events are true when the given feature is available.  | Event Name |  Maya Feature

-----------------------------------------

le    : listEvents      [boolean] []
    This causes the command to return a string array containing the names of all existing events. Below is the descriptions for all the existing events:  angularToleranceChanged:      when the tolerance on angular units is changed. This tolerance can be changed by:    1. using the MEL command, "tolerance" with the "-angular" flag   2. changing the pref under Options->GeneralPreferences-> Modeling tab->Tangential Tolerance  angularUnitChanged:      when the user changes the angular unit. axisAtOriginChanged:      when the axis changes at the origin.  axisInViewChanged:      when the axis changes at a particular view. ColorIndexChanged:      when the color index values change. constructionHistoryChanged:      when construction history is turned on or off. currentContainerChanged:      when the user set or unset the current container. currentSoundNodeChanged:      whenever the sound displayed in the time slider changes due to:    1. the sound being removed (or no longer displayed) [RMB in the time slider]   2. a new sound being displayed [RMB in the time slider]   3. sound display being toggled [animation options]   4. sound display mode being changed [animation options]  DagObjectCreated:      when a new DAG object is created. deleteAll:      when a file new occurs DisplayColorChanged:      when the display color changes. displayLayerChange:      when a layer has been created or destroyed. displayLayerManagerChange:      when the display layer manager has changed. DisplayRGBColorChanged:      when the RGB display color changes. glFrameTrigger:      for internal use only. ChannelBoxLabelSelected:      when Channel Box label(first column) selection changes. gridDisplayChanged:      for internal use only. idle:      when Maya is idle and there are no high priority idle tasks idleHigh:      when Maya is idle. This is called before low priority idle tasks. You should almost always use "idle" instead. lightLinkingChanged:      when any change occurs which modifies light linking relationships. lightLinkingChangedNonSG:      when any change occurs which modifies light linking relationships, except when the change is a change of shading assignment. linearToleranceChanged:       when the linear tolerance has been changed. This tolerance can be changed by:    * using the MEL command, "tolerance" with the "-linear" flag   * changing the pref under Options->GeneralPreferences-> Modeling tab->Positional Tolerance  linearUnitChanged:      when the user changes the linear unit through the Options menu. MenuModeChanged:      when the user changes the menu set for the menu bar in the main Maya window (for example, from "Modeling" to "Animation"). RecentCommandChanged:      for internal use only. NewSceneOpened:      when a new scene has been opened. PostSceneRead:      after a scene has been read. Specifically after a file open, import or all child references have been read. nurbsToPolygonsPrefsChanged:       when any of the nurbs-to-polygons prefs have changed. These prefs can be changed by:    * using the Mel command, "nurbsToPolygonsPref"   * changing the prefs under Polygons->Nurbs To Polygons->Option Box  playbackRangeChanged:      when the playback keyframe range changes. playbackRangeSliderChanged:      when the animation start/end range (i.e. the leftmost or rightmost entry cells in the time slider range, the inner ones adjust the playback range) change preferredRendererChanged:      when the preferred renderer changes. quitApplication:      when the user has chosen to quit, either through the quit MEL command, or through the Exit menu item. Redo:      when user has selected redo from the menu and there was something to redo. This callback can be used for updating UI or local storage. Do not change the state of the scene or DG during this callback. renderLayerChange:      when creation or deletion of a render layer node has occured. renderLayerManagerChange:      when the current render layer has changed. RebuildUIValues:      for internal use only. SceneOpened:      when a scene has been opened. SceneSaved:      when a scene has been saved. SelectionChanged:      when a new selection is made. SelectModeChanged:      when the selection mode changes. SelectPreferenceChanged:      for internal use only. SelectPriorityChanged:      when the selection priority changes. SelectTypeChanged:      when the selection type changes. setEditorChanged:      obsolete. No longer used. SetModified:      when the set command is used to modify a set SequencerActiveShotChanged:      when the active sequencer shot is changed. snapModeChanged:      when the snap mode changes. E.g. changes to grid snapping.  timeChanged:      when the time changes. timeUnitChanged:      when the user changes the time unit. ToolChanged:      when the user changes the tool/context. PostToolChanged:      after the user changes the tool/context. NameChanged:      when the user changes the name of an object with the rename command. Undo:      when user has selected undo from the menu and there was something to undo. This callback can be used for updating UI or local storage. Do not change the state of the scene or DG during this callback. modelEditorChanged:      when the user changes the options of a model editor. colorMgtEnabledChanged:      when the global per-scene color management enabled flag changes. colorMgtConfigFileEnableChanged:      when the global per-scene color management OCIO configuration enabled flag changes. colorMgtPrefsViewTransformChanged:      when the global per-scene color management view transform preferences transform changes. colorMgtWorkingSpaceChanged:      when the global per-scene color management working space changes. colorMgtConfigFilePathChanged:      when the global per-scene color management OCIO configuration file path changes. colorMgtConfigChanged:      when the color management mode changes from native to OCIO, or when a different OCIO configuration is loaded. colorMgtPrefsReloaded:      when all the global per-scene color management settings are reloaded. colorMgtUserPrefsChanged:      when any user-level color management preference has changed. colorMgtOutputChanged:      when the color management transform, or its enabled state, has changed. colorMgtOCIORulesChanged:      when the type of rules in OCIO mode has changed. colorMgtRefreshed:      when the color management is refreshed to trap environment variable changes. metadataVisualStatusChanged:      for internal use only. shapeEditorTreeviewSelectionChanged:      when a new selection in shape editor's treeview is made . RenderViewCameraChanged:      when the Render View's current camera is changed.

-----------------------------------------

lj    : listJobs        [boolean] []
    This causes the command to return a string array containing a description of all existing jobs, along with their job numbers. These numbers can be used to kill the jobs later.

-----------------------------------------

nd    : nodeDeleted     [[string, script]] []
    Run the script when the named node is deleted

-----------------------------------------

nnc   : nodeNameChanged [[string, script]] []
    Run the script when the name of the named node changes

-----------------------------------------

ovc   : optionVarChanged [[string, script]] []
    Run the script when the named optionVar changes value. If the optioNVar is deleted, this job is killed (even if the deletion is undoable).

-----------------------------------------

p     : parent          [string] []
    Attaches this job to a piece of maya UI. When the UI is destroyed, the job will be killed along with it.

-----------------------------------------

per   : permanent       [boolean] []
    Makes the job un-killable. Permanent jobs exist for the life of the application, or for the life of their parent object. The -killWithScene flag does apply to permanent jobs.

-----------------------------------------

pro   : protected       [boolean] []
    Makes the job harder to kill. Protected jobs must be killed or replaced intentionally by using the -force flag. The -killWithScene flag does apply to protected jobs.

-----------------------------------------

rp    : replacePrevious [boolean] []
    This flag can only be used with the -parent flag. Before the new scriptJob is created, any existing scriptJobs that have the same parent are first deleted.

-----------------------------------------

ro    : runOnce         [boolean] []
    If this is set to true, the script will only be run a single time. If false (the default) the script will run every time the triggering condition/event occurs. If the -uid or -nd flags are used, runOnce is turned on automatically.

-----------------------------------------

tc    : timeChange      [script] []
    Run the script whenever the current time changes. The script will not be executed if the time is changed by clicking on the time slider, whereas scripts triggered by the "timeChanged" condition will be executed.

-----------------------------------------

uid   : uiDeleted       [[string, script]]
    Run the script when the named piece of UI is deleted.

    """

def selectionConnection(q=1,e=1,atc=1,acl=1,act=1,addScript="script",add="string",cl=1,clr=1,lst=1,dt="string",d="name",ed="string",ex=1,f="string",fo="name",g=1,hl=1,id=1,key=1,lck=1,mdl=1,obj="name",p="string",rm="string",rs="script",s="name",sl=1,sw=1,ut="string",wl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/selectionConnection.html



-----------------------------------------

selectionConnection is undoable, queryable, and editable.

This command creates a named selectionConnection object. This object is simply
a shared selection list. It may be used by editors to share their highlight
data. For example, an outliner may attach its selected list to one of these
objects, and a graph editor may use the same object as a list source. Then,
the graph editor would only display objects that are selected in the outliner.

Selection connections are UI objects which contain a list of model objects.
Selection connections are useful for specifying which objects are to be
displayed within a particular editor. Editor's have three plug sockets where a
selection connection may be attached. They are:

mainListConnection

    an input socket which contains a list of objects that are to be displayed within the editor

selectionConnection

    an output socket which contains a list of objects that are selected within the editor

highlightConnection

    an input socket which contains a list of objects that are to be highlighted within the editor

There are several different types of selection connections that may be
created. They include:

activeList

    a selection connection which contains a list of everything in the model which is active (which includes geometry objects and keys)

modelList

    a selection connection which contains a list of all the geometry (i.e. excluding keys) objects that are currently active

keyframeList

    a selection connection which contains a list of all the keys that are currently active

worldList

    a selection connection which contains a list of all the objects in the world

objectList

    a selection connection which contains one model object (which may be a set)

listList

    a selection connection which contains a list of selection connections

editorList

    a selection connection which contains a list of objects that are attached to the mainListConnection of the specified editor

setList

    a selection connection which contains a list of all the sets in the world

characterList

    a selection connection which contains a list of all the characters in the world

highlightList

    a selection connection which contains a list of objects to be highlighted in some fashion

Below is an example selectionConnection network between two editors. Editor 1
is setup to display objects on the activeList. Editor 2 is setup to display
objects which are selected within Editor 1, and objects that are selected in
Editor 2 are highlighted within Editor 1:

    
    
    -- Editor 1--       -- Editor 2--
    inputList-->| main |      |  |->| main |      |
    |      | sele |--|  |      | sele |--|
    |->| high |      |     | high |      |  |
    |   -------------       -------------   |
    |------------- fromEditor2 -------------|
    

The following commands will establish this network:

    
    
    selectionConnection -activeList inputList;
    selectionConnection fromEditor1;
    selectionConnection fromEditor2;
    editor -edit -mainListConnection inputList Editor1;
    editor -edit -selectionConnection fromEditor1 Editor1;
    editor -edit -mainListConnection fromEditor1 Editor2;
    editor -edit -selectionConnection fromEditor2 Editor2;
    editor -edit -highlightConnection fromEditor2 Editor1;
    

Note: to delete a selection connection use the deleteUI command  
Note: commands which expect objects may be given a selection connection
instead, and the command will operate upon the objects wrapped by the
selection connection  
Note: the graph editor and the dope sheet are the only editors which can use
the editor connection to the highlightConnection of another editor  
WARNING: some flag combinations may not behave as you expect. The command is
really intended for internal use for managing the outliner used by the various
editors.


-----------------------------------------


Return Value:

string  Value of the queried flag    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

atc   : activeCacheList [boolean] []
    Specifies that this connection should reflect the cache that objects on the active list belong to.

-----------------------------------------

acl   : activeCharacterList [boolean] []
    Specifies that this connection should reflect the characters that objects on the active list belong to.

-----------------------------------------

act   : activeList      [boolean] []
    Specifies that this connection should reflect the active list (geometry objects and keys).

-----------------------------------------

addScript : addScript       [script] ['query', 'edit']
    Specify a script to be called when something is added to the selection.

-----------------------------------------

add   : addTo           [string] ['edit']
    The name of a selection connection that should be added to this list of connections.

-----------------------------------------

cl    : characterList   [boolean] []
    Specifies that this connection should reflect all the characters in the world.

-----------------------------------------

clr   : clear           [boolean] ['edit']
    Remove everything from the selection connection.

-----------------------------------------

lst   : connectionList  [boolean] ['query']
    Specifies that this connection should contain a list of selection connections.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

d     : deselect        [name] ['edit']
    Remove something from the selection.

-----------------------------------------

ed    : editor          [string] ['query', 'edit']
    Specifies that this connection should reflect the -mainListConnection of the specified editor.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Optionally specifies an itemFilter for this connection. An empty string ("") clears the current filter. If a filter is specified, all the information going into the selectionConnection must first pass through the filter before being accepted. NOTE: filters can only be attached to regular selectionConnections. They cannot be attached to any connection created using the -act, -mdl, -key, -wl, -sl, -cl, -lst, -obj, or -ren flags. We strongly recommend that you do not attach filters to a selectionConnection --- it is better to attach your filter to the editor that is using the selectionConnection instead.

-----------------------------------------

fo    : findObject      [name] ['query']
    Find a selection connection in this list that wraps the specified object.

-----------------------------------------

g     : g               [boolean] ['query', 'edit']
    A global selection connection cannot be deleted by any script commands.

-----------------------------------------

hl    : highlightList   [boolean] []
    Specifies that this connection is being used as a highlight list.

-----------------------------------------

id    : identify        [boolean] ['query']
    Find out what type of selection connection this is. May be: activeList | modelList | keyframeList | worldList | objectList listList | editorList | connection | unknown

-----------------------------------------

key   : keyframeList    [boolean] []
    Specifies that this connection should reflect the animation portion of the active list.

-----------------------------------------

lck   : lock            [boolean] ['query', 'edit']
    For activeList connections, locking the connection means that it will not listen to activeList changes.

-----------------------------------------

mdl   : modelList       [boolean] []
    Specifies that this connection should reflect the modeling (i.e. excluding keys) portion of the active list.

-----------------------------------------

obj   : object          [name] ['query', 'edit']
    Specifies that this connection should wrap around the specified object (which may be a set). Query will return all the members of the selection connection (if the connection wraps a set, the set members will be returned)

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    The name of a UI object this should be attached to. When the parent is destroyed, the selectionConnection will auto-delete. If no parent is specified, the connection is created in the current controlLayout.

-----------------------------------------

rm    : remove          [string] ['edit']
    The name of a selection connection that should be removed from this list of connections.

-----------------------------------------

rs    : removeScript    [script] ['query', 'edit']
    Specify a script to be called when something is removed from the selection.

-----------------------------------------

s     : select          [name] ['edit']
    Add something to the selection. This does not replace the existing selection.

-----------------------------------------

sl    : setList         [boolean] []
    Specifies that this connection should reflect all the sets in the world.

-----------------------------------------

sw    : switch          [boolean] ['query']
    Acts as a modifier to -connectionList which sets the list of objects to be the first non-empty selection connection. selection connections are tested in the order in which they are added.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

wl    : worldList       [boolean]
    Specifies that this connection should reflect all objects in the world.

    """

def setParent(q=1,dt="string",m=1,top=1,u=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setParent.html



-----------------------------------------

setParent is undoable, queryable, and NOT editable.

This command changes the default parent to be the specified parent. Two
special parents are "|" which indicates the top level layout of the window
hierarchy, or ".." which indicates one level up in the hierarchy. Trying to
move above the top level has no effect.

A control must be parented to a control layout. A control layout may be
parented to another control layout or a window. A menu may be parented to a
window or a menu bar layout. For all of these cases the setParent command
(with no flags) will indicate the current default parent.

A menu item must be parented to a menu. To specify the default menu parent use
the command setParent -m/menu. Note that all menu item objects created using
the -sm/subMenu may also be treated as menu objects.

The default parent is ignored by any object that explicitly sets the -p/parent
flag when it is created.


-----------------------------------------


Return Value:

string  Name of the parent if the parent changes. Empty string if the parent
doesn't change.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dt    : defineTemplate  [string] []
    Put a command in a mode where any other flags and args are parsed and added to the command template with the given name. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

m     : menu            [boolean] ['query']
    Parent menu for menu items.

-----------------------------------------

top   : topLevel        [boolean] []
    Move to the top level layout in the hierarchy. Equivalent to use "|"

-----------------------------------------

u     : upLevel         [boolean] []
    Move up one level in the hierarchy. Equivalent to use ".."

-----------------------------------------

ut    : useTemplate     [string]
    Will force the command to use a command template given by the name other than the current one.

    """

def setUITemplate(q=1,ppt=1,pst=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setUITemplate.html



-----------------------------------------

setUITemplate is undoable, queryable, and NOT editable.

This command sets the current(default) command template for the ELF commands.
The special name NONE can be used to set no templates current. See
"uiTemplate" command also.


-----------------------------------------


Return Value:

string  The name of the currently selected command template.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ppt   : popTemplate     [boolean] []
    Pop the current template off of the stack and sets the next template on the stack to be current.

-----------------------------------------

pst   : pushTemplate    [boolean]
    Push the current template onto a stack that can later be popped.

    """

def uiTemplate(q=1,e=1,dt="string",ex=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/uiTemplate.html



-----------------------------------------

uiTemplate is undoable, queryable, and editable.

This command creates a new command template object. Template objects can hold
default flag arguments for multiple UI commands. The command arguments are
specified with the individual commands using the -defineTemplate flag and the
desired flags and arguments. See also setUITemplate.


-----------------------------------------


Return Value:

string  The name of the uiTemplate created.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def waitCursor(q=1,st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/waitCursor.html



-----------------------------------------

waitCursor is undoable, queryable, and NOT editable.

This command sets/resets a wait cursor for the entire Maya application. This
works as a stack, such that for each waitCursor -state on command executed
there should be a matching waitCursor -state off command pending.

Warning: If a script fails that has turned the wait cursor on, the wait cursor
may be left on. You need to turn it off manually from the command line by
entering and executing the command 'waitCursor -state off'.


-----------------------------------------


Return Value:

boolean  True if the wait cursor is on.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

st    : state           [boolean]
    Set or reset the wait cursor for the entire Maya application.

    """

