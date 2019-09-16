def assignViewportFactories(q=1,e=1,mf="string",nt="string",tf="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/assignViewportFactories.html



-----------------------------------------

assignViewportFactories is NOT undoable, queryable, and editable.

Sets viewport factories for displays as materials or textures.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

mf    : materialFactory [string] ['query', 'edit']
    Set or query the materialFactory for the node type.

-----------------------------------------

nt    : nodeType        [string] ['query', 'edit']
    The node type.

-----------------------------------------

tf    : textureFactory  [string]
    Set or query the textureFactory for the node type.

    """

def batchRender(f="string",mc="string",n="int",prc="string",rm="string",rco="string",si=1,st="string",um=1,us=1,v="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/batchRender.html



-----------------------------------------

batchRender is undoable, NOT queryable, and NOT editable.

The batchRender command is used to spawn off a separate rendering session of
the current maya file. If no mayaFile is specified, it'll ask you whether you
want the current job killed.

The batchRender will spawn a separate maya process in which commands will be
communicated to it through a commandPort. If Maya is unable to find an
available port an error will be produced. Maya will attempt to use ports 7835
through 7844.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

f     : filename        [string] []
    Filename to be rendered; if empty, a temporary filename will be created.

-----------------------------------------

mc    : melCommand      [string] []
    Mel command to execute to run a renderer other than the software renderer.

-----------------------------------------

n     : numProcs        [int] []
    Number of processors to use (0 means use all available processors).

-----------------------------------------

prc   : preRenderCommand [string] []
    Command to be run prior to invoking a batch render.

-----------------------------------------

rm    : remoteRenderMachine [string] []
    Name of remote render machine. Not available on Windows.

-----------------------------------------

rco   : renderCommandOptions [string] []
    Arguments to the render command for batch rendering.

-----------------------------------------

si    : showImage       [boolean] []
    Show progress of the current rendering job.

-----------------------------------------

st    : status          [string] []
    Status string for displaying the batch render status.

-----------------------------------------

um    : useRemoteRender [boolean] []
    If remote rendering is desired. Not available on Windows.

-----------------------------------------

us    : useStandalone   [boolean] []
    Batch rendering is to be done by exporting the scene and rendering with a standalone renderer.

-----------------------------------------

v     : verbosity       [int]
    Defines the verbosity level to report the batch rendering status:    * 1: display only one start message, then one message when all frames are rendered.   * 2: display only start and end frame messages.   * 3: display all messages (default).

    """

def binMembership(q=1,add="string",ex="string",ibn="name",ivn="string",lb=1,mke="string",nfc=1,rm="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/binMembership.html



-----------------------------------------

binMembership is undoable, queryable, and NOT editable.

Command to assign nodes to bins.


-----------------------------------------


Return Value:

boolean  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addToBin        [string] []
    Add the nodes in a node list to a bin.

-----------------------------------------

ex    : exists          [string] []
    Query if a node exists in a bin. The exists flag can take only one node.

-----------------------------------------

ibn   : inheritBinsFromNodes [name] []
    Let the node in the flag's argument inherit bins from nodes in the specified node list. The node list is specified as the object of the command.

-----------------------------------------

ivn   : isValidBinName  [string] []
    Query if the specified bin name is valid. If so, return true. Otherwise, return false.

-----------------------------------------

lb    : listBins        [boolean] ['query']
    Query and return a list of bins a list of nodes belong to. If a bin contains any of the nodes in the selection list, then it should be included in the returned bin list.

-----------------------------------------

mke   : makeExclusive   [string] []
    Make the specified nodes belong exclusively in the specified bin.

-----------------------------------------

nfc   : notifyChanged   [boolean] []
    This flag is used to notify that binMembership has been changed.

-----------------------------------------

rm    : removeFromBin   [string]
    Remove the nodes in a node list from a bin.

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

def checkDefaultRenderGlobals(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/checkDefaultRenderGlobals.html



-----------------------------------------

checkDefaultRenderGlobals is NOT undoable, queryable, and editable.

To query whether or not the defaultRenderGlobals node has been modified since
the last file save, use `ls -modified`. To force the scene to be dirty/clean
use `file -modified`


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.
    """

def convertSolidTx(q=1,e=1,al=1,aa=1,bc="[int, int, int]",bm="string",cam="name",cr=1,ds=1,fil="string",fin="string",fts=1,f=1,fur=1,n="string",pf="string",rx="int",ry="int",rdm=1,sp=1,spr="[float, float, float, float]",sh=1,ubi=1,uvr="[float, float, float, float]",uv="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/convertSolidTx.html



-----------------------------------------

convertSolidTx is undoable, queryable, and editable.

Command to convert a texture on a surface to a file texture. The first
argument is a rendering node or attribute. If only the node is specified, the
outColor attribute will be sampled. If the node does not have an outColor
attribute, the first attribute on the node which is: readable, not writable,
not hidden, connectable, and not a multi is used. If lighting is to be baked,
a shading group must be specified as the texture.

The current selection will be used if a texture and surface are not specified.

An image file will be generated for each object and stored in your image
segment of your project. The filename will be formatted using the texture and
surface names as follows:

{texture}-{surface}.{fileExtension}

However, if force is off and there is a name collision a version number will
be determined and the filename will be formatted as follows:

{texture}-{surface}.{version}.{fileExtension}

If uv/uvsetName option is specified the filename will include
{surface}-{uvname} instead of {surface}.


-----------------------------------------


Return Value:

string[]  File texture nodes    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : alpha           [boolean] []
    Specify whether to compute the transparency when baking lighting. The conversion will sample both the color and transparency of the shading network; the alpha channel of the file texture will be set to correspond to the result from sampling the transparency. By default transparency is not computed.

-----------------------------------------

aa    : antiAlias       [boolean] []
    Perform anti-aliasing on the resulting image. Convert solid texture will generally take four times longer than without anti-aliasing. By default this flag is off.

-----------------------------------------

bc    : backgroundColor [[int, int, int]] []
    Set the background color to a specific value. Default is to use the shader default color to fill the background. Valid values range from 0 to 255 if the pixel format is 8 bits per channel, or 0 to 65535 if the pixel format is 16 bits per channel. This flag automatically sets -backgroundMode to "color".   Default is black: 0 0 0.

-----------------------------------------

bm    : backgroundMode  [string] []
    Defines how the background of the texture should be filled. Three modes are available:   "shader" or 1: uses the default shader color.   "color" or 2: uses the color given by -backgroundColor flag.   "extend" or 3: extends outwards the color along the seam edges.   Default is "shader".

-----------------------------------------

cam   : camera          [name] []
    Specify a camera to use in baking lighting. If a camera is not specified the camera in the active view will be used.

-----------------------------------------

cr    : componentRange  [boolean] []
    If one or more components have been selected to use, then if this flag is set, then the uv range of the components is used to fit into the texture map resolution. By default this flag is set to false.

-----------------------------------------

ds    : doubleSided     [boolean] []
    Specify whether the sampler should flip the surface normal if the sample point faces away from the camera. Note: flipping the normal will make the result dependent on the camera (ie. one camera may flip normals where different camera wouldn't). It's not recommended that doubleSided be used in combination with shadows. By default this flag is false.

-----------------------------------------

fil   : fileFormat      [string] []
    File format to be used for output. IFF is the default if unspecified. Other valid formats are:    * als: Alias PIX   * cin: Cineon   * eps: EPS   * gif: GIF   * iff: Maya IFF   * jpg: JPEG   * yuv: Quantel   * rla: Wavefront RLA   * sgi: SGI   * si: SoftImage (.pic)   * tga: Targa   * tif: TIFF   * bmp: Windows Bitmap

-----------------------------------------

fin   : fileImageName   [string] []
    Specify the output path and name of file texture image. If the file name doesn't contain a directory separator, the image will be written to source images of the current project. The file will not be versioned if it already exists.

-----------------------------------------

fts   : fillTextureSeams [boolean] []
    Specify whether or not to overscan the polygon beyond its outer edges, when creating the file texture, in order to fill the texture seams.   Default is true.

-----------------------------------------

f     : force           [boolean] []
    If the output image already exists overwrite it. By default this flag is off.

-----------------------------------------

fur   : fullUvRange     [boolean] []
    Sample using the full uv range of the surface. This flag cannot be used with the -uvr flag. A 2D texture placement node will be created and connected to the file texture. The placement's translate and coverage will be set according to the full UV range of the surface.

-----------------------------------------

n     : name            [string] []
    Set the name of the file texture node. Name conflict resolution will be used to determine valid names when multiple objects are specified.

-----------------------------------------

pf    : pixelFormat     [string] []
    Specifies the pixel format of the image. Note that not all file formats support all pixel formats. Available options:   "8": 8 bits per channel, unsigned (0-255)   "16": 16 bits per channel, unsigned (0-65535)   Default is "8".

-----------------------------------------

rx    : resolutionX     [int] []
    Set the horizontal image resolution. If this flag is not specified, the resolution will be set to 256.

-----------------------------------------

ry    : resolutionY     [int] []
    Set the vertical image resolution. If this flag is not specified, the resolution will be set to 256.

-----------------------------------------

rdm   : reuseDepthMap   [boolean] []
    Specify whether or not to reuse all the generated dmaps.   Default is false.

-----------------------------------------

sp    : samplePlane     [boolean] []
    Specify whether to sample using a virtual plane. This virtual plane has texture coordinates in the rectangle defined by the -samplePlaneRange flag. If the -samplePlaneRange flag is not set then the virtual plane defaults to having texture coordinates in the (0,0) to (1,1) square. If this option is set than all surface based arguments will be ignored.

-----------------------------------------

spr   : samplePlaneRange [[float, float, float, float]] []
    Specify the uv range of the texture coordinates used to sample if the -samplePlane option is set. There are four arguments corresponding to uMin, uMax, vMin and vMax. By default the virtual plane is from uMin 0 to uMax 1, and vMin 0 to vMax 1.

-----------------------------------------

sh    : shadows         [boolean] []
    Specify whether to compute shadows when baking lighting. Disk based shadow maps will be used. Only lights with depth map shadows enabled will contribute to the shading. By default shadows are not computed.

-----------------------------------------

ubi   : uvBBoxIntersect [boolean] []
    This flag is obsolete.

-----------------------------------------

uvr   : uvRange         [[float, float, float, float]] []
    Specify the uv range in which samples will be computed. There are four arguments corresponding to uMin, uMax, vMin and vMax. Each value should be specified based on the surface's uv space. A 2D texture placement node will be created and connected to the file texture. The placement's frame translate and coverage will be set according to the uv range specified. By default the entire uv range of the surface will be used.

-----------------------------------------

uv    : uvSetName       [string]
    Specify which uv set has to be used as the driving parametrization for convert solid.

    """

def convertTessellation(acm=1,cam="name"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/convertTessellation.html



-----------------------------------------

convertTessellation is undoable, NOT queryable, and NOT editable.

Command to translate the basic tessellation attributes to advanced. If a
camera flag is specified the translation will be based on the distance the
surface is from the camera. The closer the surface is to the camera the more
triangles there will be in the tessellation. If the "-allCameras" flags is
specified, the renderable camera closest to the surface will be used to set
the tessellation. The camera tessellation estimate is also dependent on the
current render resolution; a higher resolution the result in a more finely
tessellated surface. Multiple NURB surfaces may be specified on the command
line, or if no command arguments are specified the surfaces on the active list
will be used. This command operates by calculating the chord height such that
smooth tessellation is achieved when the surface is rendered. The advanced
tessellation setting will be enabled on each surface specified, the primary
tessellation parameters will be set, and chord height will be used as the
secondary criteria.


-----------------------------------------


Return Value:

boolean  Success or Failure.


-----------------------------------------


Flags:

-----------------------------------------

acm   : allCameras      [boolean] []
    Specifies that all renderable cameras should be used in calculating the screen based tessellation.

-----------------------------------------

cam   : camera          [name]
    Specifies the camera which should be used in calculating the screen based tessellation.

    """

def displacementToPoly(q=1,e=1,fbb=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/displacementToPoly.html



-----------------------------------------

displacementToPoly is undoable, queryable, and editable.

Command bakes geometry with displacement mapping into a polygonal object.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

fbb   : findBboxOnly    [boolean]
    When used, only the bounding box scale for the displaced object is found.

    """

def doBlur(c="string",l="float",o="float",s="float",m="float",r=1,v="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/doBlur.html



-----------------------------------------

doBlur is undoable, NOT queryable, and NOT editable.

The doBlur command will invoke the blur2d, which is a Maya stand-alone
application to do 2.5 motion blur given the color image and the motion vector
file. For a given input colorFile name, e.g. "xxx.iff", the output blurred
image will be "xxx_blur.iff" in the same directory as the input colorFile.
There is currently no control over the name of the output blurred image.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

c     : colorFile       [string] []
    Name of the input color image to be blurred.

-----------------------------------------

l     : length          [float] []
    Scale applied on the motion vector. Ranges from 0 to infinity.

-----------------------------------------

o     : memCapSize      [float] []
    Size of the memory cap, in bytes

-----------------------------------------

s     : sharpness       [float] []
    Determines the shape of the blur filter. The higher the value, the narrower the filter, the sharper the blur. The lower the value, the wider the filter, the more spread out the blur. Ranges from 0 to infinity.

-----------------------------------------

m     : smooth          [float] []
    Filter size to smooth the blurred image. The higher the value, the more anti-aliased the alpha channel. Ranges from 1.0 to 5.0.

-----------------------------------------

r     : smoothColor     [boolean] []
    Whether to smooth the color or not.

-----------------------------------------

v     : vectorFile      [string]
    Name of the input motion vector file.

    """

def getRenderDependencies():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getRenderDependencies.html



-----------------------------------------

getRenderDependencies is NOT undoable, NOT queryable, and NOT editable.

Command to return dependencies of an image source. Image sources (such as
render targets) can depend on other upstream image sources that result from
renderings of 3D scene, or renderings of 2D compositing graphs. This command
returns these dependencies, so that they can be analyzed and rendered.


-----------------------------------------


Return Value:

string  Dependencies for argument image source
    """

def getRenderTasks(c="string",rl="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getRenderTasks.html



-----------------------------------------

getRenderTasks is NOT undoable, NOT queryable, and NOT editable.

Command to return render tasks to render an image source. Image source can
depend on upstream image sources that result from renderings of 3D scene, or
2D renderings (e.g. render targets). This command obtains the graph of image
source render dependencies, and creates render tasks according to these
dependencies. A render task has context, which can be camera, render layer,
and resolution, or other, renderer-specific context. Because of image source
overrides, the render task context depends on the path through the render
dependency graph, with the most upstream override for a context item applied.
As there can be multiple paths through a render dependency graph to a render
dependency, there can be multiple render tasks for a given render dependency.


-----------------------------------------


Return Value:

string[]  Render tasks (one per string) for argument render target.


-----------------------------------------


Flags:

-----------------------------------------

c     : camera          [string] []
    Camera node to use in the render context for the image source render task.

-----------------------------------------

rl    : renderLayer     [string]
    Render layer to use in the render context for the image source render task.

    """

def glRender(q=1,e=1,abp="int",alphaSource="string",aam="string",ci=1,cc="[float, float, float]",coi=1,ce=1,cf=1,ds="string",es="float",ei=1,fii=1,fc="string",fe="int",fi="int",fs="int",fr=1,gr=1,id="string",imageName="string",imageSize="[int, int, float]",li=1,lm="string",ls=1,os=1,rf="string",rs="string",sh="float",sa="float",txd=1,ti=1,uab=1,vp="[int, int, float]",wdm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/glRender.html



-----------------------------------------

glRender is undoable, queryable, and editable.

This command provides access to the Hardware Render Manager (HRM). There is
one-and-only-one HRM in maya. The HRM controls the rendering performed in the
hardware render buffer window. This command allows shell scripts, to modify
the render state, and to initiate a render request.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

abp   : accumBufferPasses [int] ['query', 'edit']
    Set the number of accum buffer render passes.

-----------------------------------------

alphaSource : alphaSource     [string] ['query', 'edit']
    Control the alpha source when writing image files. Valid values include: off, alpha, red, green, blue, luminance, clamp, invClamp.

-----------------------------------------

aam   : antiAliasMethod [string] ['query', 'edit']
    Set the method used for anti-aliasing polygons: off, uniform, gaussian.

-----------------------------------------

ci    : cameraIcons     [boolean] ['query', 'edit']
    Set display status of camera icons.

-----------------------------------------

cc    : clearClr        [[float, float, float]] ['query', 'edit']
    Set the viewport clear color (0 - 1).

-----------------------------------------

coi   : collisionIcons  [boolean] ['query', 'edit']
    Set display status of collison model icons.

-----------------------------------------

ce    : crossingEffect  [boolean] ['query', 'edit']
    Enable/disable image filtering with a convolution filter.

-----------------------------------------

cf    : currentFrame    [boolean] ['query']
    Returns the current frame being rendered.

-----------------------------------------

ds    : drawStyle       [string] ['query', 'edit']
    Set the object drawing style: boundingBox, points, wireframe, flatShaded, smoothShaded.

-----------------------------------------

es    : edgeSmoothness  [float] ['query', 'edit']
    Controls the amount of edge smoothing. A value of 0.0 gives no smoothing, 1.0 gives default smoothing, and any other value scales the amount of default smoothing. Must enable the accumulation buffer.

-----------------------------------------

ei    : emitterIcons    [boolean] ['query', 'edit']
    Set display status of emitter icons.

-----------------------------------------

fii   : fieldIcons      [boolean] ['query', 'edit']
    Set display status of field icons.

-----------------------------------------

fc    : flipbookCallback [string] ['query', 'edit']
    Register a procedure to be called after the render sequence has completed. Used to build the flipbook pulldown menu. See the example section for more details about how to build this procedure.

-----------------------------------------

fe    : frameEnd        [int] ['query', 'edit']
    Set the last frame to be rendered.

-----------------------------------------

fi    : frameIncrement  [int] ['query', 'edit']
    Set the frame increment during rendering.

-----------------------------------------

fs    : frameStart      [int] ['query', 'edit']
    Set the first frame to be rendered.

-----------------------------------------

fr    : fullResolution  [boolean] ['query', 'edit']
    Enable/disable rendering to full image output resolution. Must set a valid image output resolution (-is).

-----------------------------------------

gr    : grid            [boolean] ['query', 'edit']
    Set display status of the grid.

-----------------------------------------

id    : imageDirectory  [string] ['query', 'edit']
    Set the directory for the image files.

-----------------------------------------

imageName : imageName       [string] ['query', 'edit']
    Set the base name of the image files.

-----------------------------------------

imageSize : imageSize       [[int, int, float]] ['query', 'edit']
    Set the image output size. Takes width, height and aspect ratio. Pass 0,0,0 to use current port size. The image size must be equal to or greater then the viewport size. Large images will be tiled if full resolution rendering has been enabled (-fr/fullResolution).

-----------------------------------------

li    : lightIcons      [boolean] ['query', 'edit']
    Set display status of light icons.

-----------------------------------------

lm    : lightingMode    [string] ['query', 'edit']
    Set the lighting mode used for rendering: all, selected, default.

-----------------------------------------

ls    : lineSmoothing   [boolean] ['query', 'edit']
    Enable/disable anti-aliased lines.

-----------------------------------------

os    : offScreen       [boolean] ['query', 'edit']
    When set, this toggle allow HRM to use an offscreen buffer to render the view. This allows HRM to work when the application is iconified, or obscured

-----------------------------------------

rf    : renderFrame     [string] ['query', 'edit']
    Render the current frame. Requires the name of the view in which to render.

-----------------------------------------

rs    : renderSequence  [string] ['query', 'edit']
    Render the current frame sequence. Requires the name of the view in which to render.

-----------------------------------------

sh    : sharpness       [float] ['query', 'edit']
    Control the sharpness level of the convolution filter.

-----------------------------------------

sa    : shutterAngle    [float] ['query', 'edit']
    Set the shutter angle used for motion blur (0 - 1). A value of 0.0 gives no blurring, 0.5 gives correct blurring, and 1.0 gives continuous blurring. Must enable the accumulation buffer.

-----------------------------------------

txd   : textureDisplay  [boolean] ['query', 'edit']
    Enable/disable texture map display.

-----------------------------------------

ti    : transformIcons  [boolean] ['query', 'edit']
    Set display status of transform icons.

-----------------------------------------

uab   : useAccumBuffer  [boolean] ['query', 'edit']
    Enable/disable the accumulation buffer.

-----------------------------------------

vp    : viewport        [[int, int, float]] ['query', 'edit']
    Set the viewport size. Pass in the width, height and aspect ratio. This size will be used for all test rendering and image output size unless full resolution (-fr) has been set and a valid image output size (-is) has been set.

-----------------------------------------

wdm   : writeDepthMap   [boolean]
    Enable/disable writing of zdepth to image files.

    """

def glRenderEditor(q=1,e=1,ctl=1,dt="string",dtg="string",ex=1,f="string",fmc="string",hlc="string",lck=1,lt="string",mlc="string",pnl="string",p="string",slc="string",sts=1,up=1,ulk=1,upd=1,ut="string",vcn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/glRenderEditor.html



-----------------------------------------

glRenderEditor is undoable, queryable, and editable.

Create a glRender view. This is a special view used for hardware rendering.
This command is used to create and reparent the view as needed to support
panels. See the glRender command for controlling the specific behavior of the
hardware rendering.


-----------------------------------------


Return Value:

None

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

lt    : lookThru        [string] ['query', 'edit']
    Specify which camera the glRender view should be using.

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

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

vcn   : viewCameraName  [boolean]
    Returns the name of the current camera used by the glRenderPanel. This is a query only flag.

    """

def hwReflectionMap(q=1,e=1,bkn="string",bmn="string",cm=1,dm=1,en=1,ftn="string",ltn="string",rtn="string",smn="string",tpn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hwReflectionMap.html



-----------------------------------------

hwReflectionMap is undoable, queryable, and editable.

This command creates a hwReflectionMap node for having reflection on textured
surfaces that currently have their boolean attribute displayHWEnvironment set
to true.


-----------------------------------------


Return Value:

string  (name of the created hwReflectionMap node)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bkn   : backTextureName [string] ['query']
    This flag specifies the file texture name for the back side of the cube.   Default is none   When queried, this flag returns a string.

-----------------------------------------

bmn   : bottomTextureName [string] ['query']
    This flag specifies the file texture name for the bottom side of the cube.   Default is none   When queried, this flag returns a string.

-----------------------------------------

cm    : cubeMap         [boolean] ['query']
    If on, the reflection of the textures is done using the cube mapping.   Default is false. The reflection is done using sphere mapping.   When queried, this flag returns a boolean.

-----------------------------------------

dm    : decalMode       [boolean] ['query']
    If on, the reflection color replaces the surface shading.   Default is false. The reflection is multiplied to the surface shading.   When queried, this flag returns a boolean.

-----------------------------------------

en    : enable          [boolean] ['query']
    If on, enable the corresponding hwReflectionMap node.   Default is false.   When queried, this flag returns a boolean.

-----------------------------------------

ftn   : frontTextureName [string] ['query']
    This flag specifies the file texture name for the front side of the cube.   Default is none   When queried, this flag returns a string.

-----------------------------------------

ltn   : leftTextureName [string] ['query']
    This flag specifies the file texture name for the left side of the cube.   Default is none   When queried, this flag returns a string.

-----------------------------------------

rtn   : rightTextureName [string] ['query']
    This flag specifies the file texture name for the right side of the cube.   Default is none   When queried, this flag returns a string.

-----------------------------------------

smn   : sphereMapTextureName [string] ['query']
    This flag specifies the file texture name for the sphere mapping option.   Default is none   When queried, this flag returns a string.

-----------------------------------------

tpn   : topTextureName  [string]
    This flag specifies the file texture name for the top side of the cube.   Default is none   When queried, this flag returns a string.

    """

def hwRender(q=1,ams=1,atc=1,cam="string",cf=1,cv=1,eaa="[uint, uint]",fnp=1,f="float",frs=1,h="uint",ifn=1,l="name",lrs=1,lql=1,nrv=1,nwf=1,pg=1,rhw=1,reg="[uint, uint, uint, uint]",rs=1,res="uint",w="uint",a=1,d=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hwRender.html



-----------------------------------------

hwRender is NOT undoable, queryable, and NOT editable.

Renders an image or a sequence using the hardware rendering engine


-----------------------------------------


Return Value:

boolean  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ams   : acceleratedMultiSampleSupport [boolean] ['query']
    This flag when used with query will return whether the graphics supports hardware accelerated multi-sampling.

-----------------------------------------

atc   : activeTextureCount [boolean] ['query']
    This flag when used with query will return the number of textures that have been bound to the graphics by the hardware renderer.

-----------------------------------------

cam   : camera          [string] ['query']
    Specify the camera to use. Use the first available camera if the camera given is not found.

-----------------------------------------

cf    : currentFrame    [boolean] ['query']
    Render the current frame.

-----------------------------------------

cv    : currentView     [boolean] ['query']
    When turned on, only the current view will be rendered.

-----------------------------------------

eaa   : edgeAntiAliasing [[uint, uint]] ['query']
    Enables multipass rendering. Controls for the number of exposures rendered per frame are provided in the form of two associated flag arguments. The first specifies the sampling algorithm:    * 0 - Uniform Weighted Grid Sampling   * 1 - Rotated Grid Super Sampling (RGSS)   * 2 - Gaussian Weighted Sampling  Use of a sampling method other than the others listed above, will result in use of the default sample method of Uniform Weighted Grid Sampling. The second argument specifies a number of samples to use. For each sampling algorithm there is a fixed set of sample counts available:    * 0 - Uniform Weighted Grid Sampling     * 1 Sample     * 3 Samples     * 4 Samples     * 5 Samples     * 7 Samples     * 9 Samples     * 16 Samples     * 25 Samples     * 36 Samples   * 1 - Rotated Grid Super Sampling (RGSS)     * 1 Sample     * 4 Samples     * 5 Samples   * 2 - Gaussian Weighted Sampling     * 1 Sample     * 3 Samples     * 4 Samples     * 5 Samples     * 7 Samples     * 9 Samples     * 16 Samples     * 25 Samples     * 36 Samples  Using a sampling count other than the allowable options for the given sampling method will result in using the default sample count of 5. The values passed via the command will override settings stored in the hardwareRenderGlobals node.

-----------------------------------------

fnp   : fixFileNameNumberPattern [boolean] ['query']
    This flag allows the user to take the hardwareRenderGlobals filename as the initial filename pattern, fix the frame number pattern in the filename in a unique way, returns the new filename pattern. This does not change the hardwareRenderGlobals's filename.

-----------------------------------------

f     : frame           [float] []
    Specify the frame to render.

-----------------------------------------

frs   : fullRenderSupport [boolean] ['query']
    This flag may be used in the create or query context. In the create context, it will force the renderer to abort and not render any frames if the hardware is not fully supported. In the query context, it will return whether full quality rendering is supported on the current graphics system. Please see the graphics card qualification charts for an explanation of limited support.

-----------------------------------------

h     : height          [uint] ['query']
    Height. If not used, the height is taken from the render globals settings.

-----------------------------------------

ifn   : imageFileName   [boolean] ['query']
    This flag let people query the image name for a specified frame. The frame can be specified using the "-frame" flag. When no "-frame" is used, the current frame number is used.

-----------------------------------------

l     : layer           [name] ['query']
    Render the specified render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering.

-----------------------------------------

lrs   : limitedRenderSupport [boolean] ['query']
    This flag when used with query will return whether limited rendering is supported on the current graphics system. Please see the graphics card qualification charts for the current definition of limited support.

-----------------------------------------

lql   : lowQualityLighting [boolean] ['query']
    Disable lighting evaluation per pixel (fragment). Note: The values passed via the command will override settings stored in the hardware render globals node.

-----------------------------------------

nrv   : noRenderView    [boolean] ['query']
    When turned on, the render view is not updated after image computation

-----------------------------------------

nwf   : notWriteToFile  [boolean] ['query']
    This flag is set to true if the user does not want to write the image to a file. It is set to false, otherwise. The default value of the flag is "false".

-----------------------------------------

pg    : printGeometry   [boolean] ['query']
    Print the geomety objects as they get translated.

-----------------------------------------

rhw   : renderHardwareName [boolean] ['query']
    This flag will create a graphics context and return the name of the graphics hardware being used. The graphics hardware is determined by creating an off screen buffer and querying the GL_RENDERER string from OpenGL. If the off screen buffer cannot be created an empty string is returned.

-----------------------------------------

reg   : renderRegion    [[uint, uint, uint, uint]] ['query']
    Render region. The parameters are 4 integers, indicating left right bottom top of the region.

-----------------------------------------

rs    : renderSelected  [boolean] ['query']
    Only renders the selected objects.

-----------------------------------------

res   : textureResolution [uint] ['query']
    Specify the desired resolution of baked textures.

-----------------------------------------

w     : width           [uint] ['query']
    Width. If not used, the width is taken from the render globals settings.

-----------------------------------------

a     : writeAlpha      [boolean] ['query']
    Read the alpha channel of color buffer and return as tif file.

-----------------------------------------

d     : writeDepth      [boolean]
    Read the depth buffer and return as tif file.

    """

def hwRenderLoad():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hwRenderLoad.html



-----------------------------------------

hwRenderLoad is NOT undoable, NOT queryable, and NOT editable.

Empty command used to force the dynamic load of HR render


-----------------------------------------


Return Value:

None
    """

def iprEngine(q=1,e=1,cp="string",dt="string",dig=1,mem=1,ex=1,ipr="string",mvf=1,obj="name",r="[int, int, int, int]",rel=1,rii=1,res=1,sli="string",spb=1,st=1,spt=1,un="[int, int]",u=1,udf=1,ulg=1,umb=1,up="string",usg=1,us=1,usm=1,ut="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/iprEngine.html



-----------------------------------------

iprEngine is undoable, queryable, and editable.

Command to create or edit an iprEngine. A iprEngine is an object that watches
for changes to shading networks and automatically reshades to generate an up-
to-date image.


-----------------------------------------


Return Value:

string  \- the name of the ipr engine created or modified    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cp    : copy            [string] ['edit']
    Copies the deep raster file, as well as its related files, to the new location.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dig   : diagnostics     [boolean] ['edit']
    The diagnostics should be shown

-----------------------------------------

mem   : estimatedMemory [boolean] ['query']
    Displays the estimated memory being used by IPR.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

ipr   : iprImage        [string] ['query', 'edit']
    Specify the ipr image to use.

-----------------------------------------

mvf   : motionVectorFile [boolean] ['query']
    Returns the name of the motion vector file used by IPR.

-----------------------------------------

obj   : object          [name] ['query', 'edit']
    The objects to be tuned.

-----------------------------------------

r     : region          [[int, int, int, int]] ['query', 'edit']
    The coordinates of the region to be tuned. The integers are in the sequence left bottom right top or x1,y2 x2,y2

-----------------------------------------

rel   : relatedFiles    [boolean] ['query']
    Returns the names for the related files, e.g, the non-glow-non-blur image, the motion vector file, and the depth-map files.

-----------------------------------------

rii   : releaseIprImage [boolean] ['edit']
    The ipr image should be released and memory should be freed.

-----------------------------------------

res   : resolution      [boolean] ['query']
    The width and height of the ipr file.

-----------------------------------------

sli   : scanlineIncrement [string] ['query', 'edit']
    Set the scanline increment percentage. If the height of the region being update is 240 pixels, and the scanlineIncrement is 10% then the image will refresh blocks of 24 scanlines.

-----------------------------------------

spb   : showProgressBar [boolean] ['query', 'edit']
    Show progress bar during tuning.

-----------------------------------------

st    : startTuning     [boolean] ['query', 'edit']
    An ipr image has been specified and now changes to shading networks should force an image to be produced.

-----------------------------------------

spt   : stopTuning      [boolean] ['query', 'edit']
    Tuning should cease but ipr image should not be closed.

-----------------------------------------

un    : underPixel      [[int, int]] ['edit']
    Get list of objects under the pixel sprcified.

-----------------------------------------

u     : update          [boolean] ['edit']
    Force an update.

-----------------------------------------

udf   : updateDepthOfField [boolean] ['edit']
    Force a refresh of depth-of-field.

-----------------------------------------

ulg   : updateLightGlow [boolean] ['query', 'edit']
    Automatically update when light glow changes.

-----------------------------------------

umb   : updateMotionBlur [boolean] ['query', 'edit']
    Automatically update when 2.5D motion blur changes.

-----------------------------------------

up    : updatePort      [string] ['query', 'edit']
    The name of the port that is to be updated when pixel values are recomputed. (not currently supported)

-----------------------------------------

usg   : updateShaderGlow [boolean] ['query', 'edit']
    Automatically update when shader glow changes.

-----------------------------------------

us    : updateShading   [boolean] ['query', 'edit']
    Automatically update shading.

-----------------------------------------

usm   : updateShadowMaps [boolean] ['edit']
    Force the shadow maps to be generated and an update to occur.

-----------------------------------------

ut    : useTemplate     [string]
    Forces the command to use a command template other than the current one.

    """

def layeredShaderPort(q=1,e=1,ann="string",bgc="[float, float, float]",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,n="name",npm=1,p="string",pma=1,po=1,scc="string",stc="string",sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/layeredShaderPort.html



-----------------------------------------

layeredShaderPort is undoable, queryable, and editable.

This command creates a 3dPort that displays an image representing the layered
shader node specified.


-----------------------------------------


Return Value:

string  Full path name to the control.    
  
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

n     : node            [name] []
    Specifies the name of the newLayeredShader node this port will represent.

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

scc   : selectedColorControl [string] []
    Specifies the name of the UI-control that represents the currently selected layer's color.

-----------------------------------------

stc   : selectedTransparencyControl [string] []
    Specifies the name of the UI-control that represents the currently selected layer's transparency.

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

def layeredTexturePort(q=1,e=1,ann="string",bgc="[float, float, float]",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,n="name",npm=1,p="string",pma=1,po=1,sac="string",sbc="string",scc="string",svc="string",sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/layeredTexturePort.html



-----------------------------------------

layeredTexturePort is undoable, queryable, and editable.

This command creates a 3dPort that displays an image representing the layered
texture node specified.


-----------------------------------------


Return Value:

string  Full path name to the control.    
  
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

n     : node            [name] []
    Specifies the name of the newLayeredTexture node this port will represent.

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

sac   : selectedAlphaControl [string] []
    Specifies the name of the UI-control that represents the currently selected layer's alpha.

-----------------------------------------

sbc   : selectedBlendModeControl [string] []
    Specifies the name of the UI-control that represents the currently selected layer's blend mode.

-----------------------------------------

scc   : selectedColorControl [string] []
    Specifies the name of the UI-control that represents the currently selected layer's color.

-----------------------------------------

svc   : selectedIsVisibleControl [string] []
    Specifies the name of the UI-control that represents the currently selected layer's visibility.

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

def lsThroughFilter(it="string",na=1,rv=1,sl=1,so="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lsThroughFilter.html



-----------------------------------------

lsThroughFilter is undoable, NOT queryable, and NOT editable.

List all objects in the world that pass a given filter.


-----------------------------------------


Return Value:

string[]  List of nodes passing the filter


-----------------------------------------


Flags:

-----------------------------------------

it    : item            [string] []
    Run the filter on specified node(s), using the fast version of this command.

-----------------------------------------

na    : nodeArray       [boolean] []
    Fast version that runs an entire array of nodes through the filter at one time.

-----------------------------------------

rv    : reverse         [boolean] []
    Only available in conjunction with nodeArray flag. Reverses the order of nodes in the returned arrays if true.

-----------------------------------------

sl    : selection       [boolean] []
    Run the filter on selected nodes only, using the fast version of this command.

-----------------------------------------

so    : sort            [string]
    Only available in conjunction with nodeArray flag. Orders the nodes in the returned array. Current options are: "byName", "byType", and "byTime".

    """

def makebot(c=1,r="uint",i="string",nov=1,o="string",v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/makebot.html



-----------------------------------------

makebot is undoable, NOT queryable, and NOT editable.

The makebot command takes an image file and produces a block ordered texture
(BOT) file, to be used for texture caching. If a relative pathname is
specified for the input image file, project management rules apply. If a
relative pathname is specified for the output BOT file, project management
rules apply and gets put into the sourceImages directory.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

c     : checkdepends    [boolean] []
    the BOT file should only be generated if it doesn't already exists, or if it is older than the source file

-----------------------------------------

r     : checkres        [uint] []
    the BOT file should only be generated if its resolution (maximum of width and height) is larger than the minimum value specified by the argument

-----------------------------------------

i     : input           [string] []
    input image file

-----------------------------------------

nov   : nooverwrite     [boolean] []
    If -c and/or -r indicate that the BOT file should be generated but if already exists, then this flag will prevent the file from being overwritten

-----------------------------------------

o     : output          [string] []
    output BOT file

-----------------------------------------

v     : verbose         [boolean]
    Makebot will provide feedback if this flag is specified

    """

def mayaHasRenderSetup(q=1,e=1,ecs=1,edt=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/mayaHasRenderSetup.html



-----------------------------------------

mayaHasRenderSetup is NOT undoable, queryable, and editable.

This command controls and queries render setup states.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ecs   : enableCurrentSession [boolean] ['query', 'edit']
    Enables or disables render setup for this Maya session only. This flag should only be called during Maya intialization. This flag is for internal use only, may change at any time and is unsupported.

-----------------------------------------

edt   : enableDuringTests [boolean]
    Switches render setup for this Maya session only, as legacy render layer mode is assumed during testing. This flag is for internal use only, may change at any time and is unsupported.

    """

def nodeIconButton(q=1,e=1,al="string",ann="string",bgc="[float, float, float]",c="script",dt="string",di="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fx=1,fy=1,fn="string",fpn=1,h="int",hlc="[float, float, float]",i="string",i1="string",i2="string",i3="string",iol="string",io=1,l="string",lo="int",lt="string",m=1,mh="uint",mw="uint",nbg=1,npm=1,olb="[float, float, float, float]",olc="[float, float, float]",p="string",pma=1,po=1,rot="float",sbm="string",st="string",ua=1,ut="string",ver="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nodeIconButton.html



-----------------------------------------

nodeIconButton is undoable, queryable, and editable.

This control supports up to 3 icon images and 4 different display styles. The
icon image displayed is the one that best fits the current size of the control
given its current style.

This command creates a button that can be displayed with different icons, with
or without a text label. If the button is drag and dropped onto other controls
(e.g., HyperShade), the command will be executed and the return string will be
used as the name of a dropped node.


-----------------------------------------


Return Value:

string  The name of the button    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : align           [string] ['query', 'edit']
    The label alignment. Alignment values are "left", "right", and "center". By default, the label is aligned "center". Currently only available when -st/style is set to "iconAndTextCentered".

-----------------------------------------

ann   : annotation      [string] ['query', 'edit']
    Annotate the control with an extra string value.

-----------------------------------------

bgc   : backgroundColor [[float, float, float]] ['query', 'edit']
    The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.   When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.

-----------------------------------------

c     : command         [script] ['query', 'edit']
    Command executed when the control is pressed. The command should return a string which will be used to facilitate node drag and drop.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

di    : disabledImage   [string] ['query', 'edit']
    Image used when the button is disabled. Image size must be the same as the image specified with the i/image flag. This is a Windows only flag.

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

fx    : flipX           [boolean] ['query', 'edit']
    Is the image flipped horizontally?

-----------------------------------------

fy    : flipY           [boolean] ['query', 'edit']
    Is the image flipped vertically?

-----------------------------------------

fn    : font            [string] ['query', 'edit']
    The font for the text. Valid values are "boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont", "plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont", "smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".

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
    If you are not providing images with different sizes then you may use this flag for the control's image. If the "iconOnly" style is set, the icon will be scaled to the size of the control.

-----------------------------------------

i1    : image1          [string] ['query', 'edit']
    First of three possible icons. The icon that best fits the current size of the control will be displayed.

-----------------------------------------

i2    : image2          [string] ['query', 'edit']
    Second of three possible icons. The icon that best fits the current size of the control will be displayed.

-----------------------------------------

i3    : image3          [string] ['query', 'edit']
    Third of three possible icons. The icon that best fits the current size of the control will be displayed.

-----------------------------------------

iol   : imageOverlayLabel [string] ['query', 'edit']
    A short string, up to 6 characters, representing a label that will be displayed on top of the image.

-----------------------------------------

io    : isObscured      [boolean] ['query']
    Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.

-----------------------------------------

l     : label           [string] ['query', 'edit']
    The text that appears in the control.

-----------------------------------------

lo    : labelOffset     [int] ['query', 'edit']
    The label offset. Default is 0. Currently only available when -st/style is set to "iconAndTextCentered".

-----------------------------------------

lt    : ltVersion       [string] ['query', 'edit']
    This flag is used to specify the Maya LT version that this control feature was introduced, if the version flag is not specified, or if the version flag is specified but its argument is different. This value is only used by Maya LT, and otherwise ignored. The argument should be given as a string of the version number (e.g. "2013", "2014"). Currently only accepts major version numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").

-----------------------------------------

m     : manage          [boolean] ['query', 'edit']
    Manage state of the control. An unmanaged control is not visible, nor does it take up any screen real estate. All controls are created managed by default.

-----------------------------------------

mh    : marginHeight    [uint] ['query', 'edit']
    The number of pixels above and below the control content. The default value is 1 pixel.

-----------------------------------------

mw    : marginWidth     [uint] ['query', 'edit']
    The number of pixels on either side of the control content. The default value is 1 pixel.

-----------------------------------------

nbg   : noBackground    [boolean] ['edit']
    Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn. The state of this flag is inherited by children of this control.

-----------------------------------------

npm   : numberOfPopupMenus [boolean] ['query']
    Return the number of popup menus attached to this control.

-----------------------------------------

olb   : overlayLabelBackColor [[float, float, float, float]] ['query', 'edit']
    The RGBA color of the shadow behind the label defined by imageOverlayLabel. Default is 50% transparent black: 0 0 0 .5

-----------------------------------------

olc   : overlayLabelColor [[float, float, float]] ['query', 'edit']
    The RGB color of the label defined by imageOverlayLabel. Default is a light grey: .8 .8 .8

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

rot   : rotation        [float] ['query', 'edit']
    The rotation value of the image in radians.

-----------------------------------------

sbm   : statusBarMessage [string] ['edit']
    Extra string to display in the status bar when the mouse is over the control.

-----------------------------------------

st    : style           [string] ['query', 'edit']
    The draw style of the control. Valid styles are "iconOnly", "textOnly", "iconAndTextHorizontal", "iconAndTextVertical", and "iconAndTextCentered". (Note: "iconAndTextCentered" is only available on Windows). If the "iconOnly" style is set, the icon will be scaled to the size of the control.

-----------------------------------------

ua    : useAlpha        [boolean] ['query', 'edit']
    Is the image using alpha channel?

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

ver   : version         [string] ['query', 'edit']
    Specify the version that this control feature was introduced. The argument should be given as a string of the version number (e.g. "2013", "2014"). Currently only accepts major version numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").

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

def nodePreset(atr="string",ctm="string",delete="[name, string]",ex="[name, string]",ivn="string",ls="name",ld="[name, string]",sv="[name, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nodePreset.html



-----------------------------------------

nodePreset is NOT undoable, NOT queryable, and NOT editable.

Command to save and load preset settings for a node. This command allows you
to take a snapshot of the values of all attributes of a node and save it to
disk as a preset with user specified name. Later the saved preset can be
loaded and applied onto a different node of the same type. The end result is
that the node to which the preset is applied takes on the same values as the
node from which the preset was generated had at the time of the snapshot.


-----------------------------------------


Return Value:

boolean  if isValidName or exists is used.


-----------------------------------------


Flags:

-----------------------------------------

atr   : attributes      [string] []
    A white space separated string of the named attributes to save to the preset file. If not specified, all attributes will be stored.

-----------------------------------------

ctm   : custom          [string] []
    Specifies a MEL script for custom handling of node attributes that are not handled by the general save preset mechanism (ie. multis, dynamic attributes, or connections). The identifiers #presetName and #nodeName will be expanded before the script is run. The script must return an array of strings which will be saved to the preset file and issued as commands when the preset is applied to another node. The custom script can query #nodeName in determining what should be saved to the preset, or issue commands to query the selected node in deciding how the preset should be applied.

-----------------------------------------

delete : delete          [[name, string]] []
    Deletes the existing preset for the node specified by the first argument with the name specified by the second argument.

-----------------------------------------

ex    : exists          [[name, string]] []
    Returns true if the node specified by the first argument already has a preset with a name specified by the second argument. This flag can be used to check if the user is about to overwrite an existing preset and thereby provide the user with an opportunity to choose a different name.

-----------------------------------------

ivn   : isValidName     [string] []
    Returns true if the name consists entirely of valid characters for a preset name. Returns false if not. Because the preset name will become part of a file name and part of a MEL procedure name, some characters must be disallowed. Only alphanumeric characters and underscore are valid characters for the preset name.

-----------------------------------------

ls    : list            [name] []
    Lists the names of all presets which can be loaded onto the specified node.

-----------------------------------------

ld    : load            [[name, string]] []
    Sets the settings of the node specified by the first argument according to the preset specified by the second argument. Any attributes on the node which are the destinations of connections or whose children (multi children or compound children) are destinations of connections will not be changed by the preset.

-----------------------------------------

sv    : save            [[name, string]]
    Saves the current settings of the node specified by the first argument to a preset of the name specified by the second argument. If a preset for that node with that name already exists, it will be overwritten with no warning. You can use the -exists flag to check if the preset already exists. If an attribute of the node is the destination of a connection, the value of the attribute will not be written as part of the preset.

    """

def ogsRender(q=1,e=1,mst="string",cro="string",fpt="string",afp=1,amt=1,aro=1,cam="string",cf=1,cv=1,efp=1,ems=1,f="float",h="uint",l="name",nrv=1,w="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ogsRender.html



-----------------------------------------

ogsRender is NOT undoable, queryable, and editable.

Renders an image or a sequence using the OGS rendering engine


-----------------------------------------


Return Value:

boolean  Query result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

mst   : activeMultisampleType [string] ['query', 'edit']
    Query the current active multisample type.

-----------------------------------------

cro   : activeRenderOverride [string] ['query', 'edit']
    Set or query the current active render override.

-----------------------------------------

fpt   : activeRenderTargetFormat [string] ['query', 'edit']
    Query the current active floating point target format.

-----------------------------------------

afp   : availableFloatingPointTargetFormat [boolean] ['query', 'edit']
    Returns the names of available floating point render target format.

-----------------------------------------

amt   : availableMultisampleType [boolean] ['query', 'edit']
    Returns the names of available multisample type.

-----------------------------------------

aro   : availableRenderOverrides [boolean] ['query', 'edit']
    Returns the names of available render overrides.

-----------------------------------------

cam   : camera          [string] ['query', 'edit']
    Specify the camera to use. Use the first available camera if the camera given is not found.

-----------------------------------------

cf    : currentFrame    [boolean] ['query', 'edit']
    Render the current frame.

-----------------------------------------

cv    : currentView     [boolean] ['query', 'edit']
    When turned on, only the current view will be rendered.

-----------------------------------------

efp   : enableFloatingPointRenderTarget [boolean] ['query', 'edit']
    Enable/disable floating point render target.

-----------------------------------------

ems   : enableMultisample [boolean] ['query', 'edit']
    Enable/disable multisample.

-----------------------------------------

f     : frame           [float] ['edit']
    Specify the frame to render.

-----------------------------------------

h     : height          [uint] ['query', 'edit']
    The height flag pass the height to the ogsRender command. If not used, the height is taken from the render globals settings.

-----------------------------------------

l     : layer           [name] ['query', 'edit']
    Render the specified render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering.

-----------------------------------------

nrv   : noRenderView    [boolean] ['query', 'edit']
    When turned on, the render view is not updated after image computation

-----------------------------------------

w     : width           [uint]
    The width flag pass the width to the ogsRender command. If not used, the width is taken from the render globals settings.

    """

def preferredRenderer(q=1,f="string",mc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/preferredRenderer.html



-----------------------------------------

preferredRenderer is NOT undoable, queryable, and NOT editable.

Command to set the preferred renderer. This command can be used to query the
preferred renderer and to set the current renderer as the preferred one. It
also allows users to specify a preferred fallback renderer.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

f     : fallback        [string] ['query']
    Sets the preferred fallback renderer.

-----------------------------------------

mc    : makeCurrent     [boolean]
    Sets the current renderer as the preferred one.

    """

def prepareRender(q=1,e=1,dt="string",d="string",ior=1,iof=1,iol=1,irr=1,irf=1,irl=1,isu=1,lbl="string",lt=1,por="script",pof="script",pol="script",prr="script",prf="script",prl="script",rtr=1,sac=1,sui="script",stp=1,ts="string",tsi="script"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/prepareRender.html



-----------------------------------------

prepareRender is undoable, queryable, and editable.

This command is used to register, manage and invoke render traversals. Render
traversals are used to configure a scene to prepare it for rendering.

This command has special support for scene assembly nodes. To render scene
assembly nodes, a rendering traversal can activate an appropriate
representation, for each assembly node in the scene. When rendering is done,
this command can correspondingly restore the representation that was active
before rendering on each assembly. Render traversals are grouped into
traversal sets. A render traversal set includes callbacks, or render
traversals, for one or more of the following steps of rendering, ordered by
decreasing level of granularity. A render traversal callback is an arbitrary
script, either MEL or Python, that can transform the Maya scene for rendering
purposes.

preRender

    Traversal run once per render, before any rendering is performed.
postRender

    Traversal run once per render, after all rendering has been performed.
preRenderLayer

    Traversal run before rendering each render layer.
postRenderLayer

    Traversal run after rendering each render layer.
preRenderFrame

    Traversal run before rendering each frame.
postRenderFrame

    Traversal run after rendering each frame.
During a render view or batch render, Maya will run the render traversals from
the same traversal set, the default traversal set. Traversal sets are named,
so multiple traversal sets can be registered with this command, and the
default render traversal set can be switched to any one of these registered
traversal sets. When changing the default traversal set, the different render
traversal callbacks (preRender, preRenderLayer, preRenderFrame, postRender,
postRenderLayer, postRenderFrame) are switched as a unit.

At render time, the software rendering code invokes the callbacks of the
default traversal set. The prepareRender scripting capability allows for the
development of multiple rendering preparation scripts, including from plugins,
to provide extensibility rather than being constrained to a single
implementation.

A special traversal set is the "null" traversal set. It is the initial default
traversal set, and cannot be deregistered. It performs no work, and does not
save and restore the assembly node active representation configuration. It
will provide WYSIWYG (What You See Is What You Get) rendering of assembly
nodes, without switching to a different representation to render.

Render traversals are invoked by Maya using this command's create mode. This
is done by Maya's rendering infrastructure, and should not be required unless
developing new render views or batch render code. Most uses of this command
will simply use the edit mode to register render traversals into a render
traversal set, or the query mode to query the names of the render traversals
in a render traversal set.

## Render Traversals versus Render MEL Scripts

Render traversals are similar in intent to the user-specified pre- and post-
render, pre- and post-render layer, pre- and post-render frame MEL script
capability. The difference with the user MEL scripts is that prepareRender is
in addition to, and does not replace, the user MEL scripts, can register
multiple render traversal sets and switch them, and supports both MEL and
Python. The MEL render scripts are run inside the scope of the render
traversals, that is, the preRender traversal is run before the pre-render MEL
script and the postRender traversal is run after the post-render MEL script,
the preRenderLayer traversal is run before the pre-render layer MEL script and
the postRenderLayer traversal is run after the post-render layer MEL script,
and finally the preRenderFrame traversal is run before the pre-render frame
MEL script and the postRenderFrame traversal is run after the post-render
frame MEL script.

## Saving and Restoring State

The prepareRender command has support for saving and restoring the active
representation of assembly nodes in the scene. Use the saveAssemblyConfig flag
to indicate that the render traversal set requires saving the assembly node
active representation before rendering begins, and should restore the assembly
node active representation after rendering ends.

It is the responsibility of render traversals that modify the scene in ways
other than changing the active representation on assembly nodes to restore the
scene to its previous state, most likely using the postRender,
postRenderLayer, and postRenderFrame traversals.

Note that Maya does not call the prepareRender -restore command on batch
render completion, since batch rendering is done on a copy of the scene which
is discarded once rendering terminates. Implementors of render traversals may
wish to check whether they are running in batch mode, to implement the same
optimization.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dt    : defaultTraversalSet [string] ['query', 'edit']
    Set or query the default traversal set. The prepareRender command performs operations on the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

d     : deregister      [string] ['edit']
    Deregister a registered traversal set. If the deregistered traversal set is the default traversal set, the new default traversal set will be the "null" traversal set.

-----------------------------------------

ior   : invokePostRender [boolean] []
    Invoke the postRender render traversal for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

iof   : invokePostRenderFrame [boolean] []
    Invoke the postRenderFrame render traversal for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

iol   : invokePostRenderLayer [boolean] []
    Invoke the postRenderLayer render traversal for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

irr   : invokePreRender [boolean] []
    Invoke the preRender render traversal for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

irf   : invokePreRenderFrame [boolean] []
    Invoke the preRenderFrame render traversal for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

irl   : invokePreRenderLayer [boolean] []
    Invoke the preRenderLayer render traversal for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

isu   : invokeSettingsUI [boolean] []
    Invoke the settings UI callback to populate a layout with UI controls, for a given traversal set. The current UI parent will be a form layout, which the callback can query using the setParent command. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

lbl   : label           [string] ['query', 'edit']
    Set or query the label for a given traversal set. The label is used for UI display purposes, and can be localized. The traversal set will be the default, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

lt    : listTraversalSets [boolean] ['query']
    Query the supported render traversal sets.

-----------------------------------------

por   : postRender      [script] ['query', 'edit']
    Set or query the postRender render traversal for a given traversal set. This traversal is run after a render. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

pof   : postRenderFrame [script] ['query', 'edit']
    Set or query the postRenderFrame render traversal for a given traversal set. This traversal is run after the render of a single frame, with a render layer. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

pol   : postRenderLayer [script] ['query', 'edit']
    Set or query the postRenderLayer render traversal for a given traversal set. This traversal is run after a render layer is rendered, within a render. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

prr   : preRender       [script] ['query', 'edit']
    Set or query the preRender render traversal for a given traversal set. This traversal is run before a render. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

prf   : preRenderFrame  [script] ['query', 'edit']
    Set or query the preRenderFrame render traversal for a given traversal set. This traversal is run before the render of a single frame, with a render layer. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

prl   : preRenderLayer  [script] ['query', 'edit']
    Set or query the preRenderLayer render traversal for a given traversal set. This traversal is run before a render layer is rendered, within a render. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

rtr   : restore         [boolean] []
    Clean up after rendering, including restoring the assembly active representation configuration for the whole scene, if the saveAssemblyConfig flag for the traversal set is true. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

sac   : saveAssemblyConfig [boolean] ['query', 'edit']
    Set or query whether or not the assembly active representation configuration for the whole scene should be saved for a given traversal set. The traversal set will be the default, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

sui   : settingsUI      [script] ['query', 'edit']
    Set or query the settings UI callback for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

stp   : setup           [boolean] []
    Setup render preparation, including saving the assembly active representation configuration for the whole scene, if the saveAssemblyConfig flag for the traversal set is true. Any previously-saved configuration will be overwritten. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.

-----------------------------------------

ts    : traversalSet    [string] ['query', 'edit']
    Set or query properties for the specified registered traversal set.  In query mode, this flag needs a value.

-----------------------------------------

tsi   : traversalSetInit [script]
    Set or query the traversal set initialisation callback for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set. This callback is invoked whenever the specified traversal set becomes the default. traversal set.

    """

def projectionManip(q=1,fb=1,pt="int",st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/projectionManip.html



-----------------------------------------

projectionManip is undoable, queryable, and NOT editable.

Various commands to set the manipulator to interesting positions.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

fb    : fitBBox         [boolean] []
    Fit the projection manipulator size and position to the shading group bounding box. The orientation is not modified.

-----------------------------------------

pt    : projType        [int] []
    Set the projection type to the given value. Projection type values are:    * 1 = planar.   * 2 = spherical.   * 3 = cylindrical.   * 4 = ball.   * 5 = cubic.   * 6 = triplanar.   * 7 = concentric.   * 8 = camera.

-----------------------------------------

st    : switchType      [boolean]
    Loop over the allowed types. If the hardware shading is on, it loops over the hardware shadeable types (planar, cylindrical, spherical), otherwise, it loops over all the types. If there is no given value, it loops over the different projection types.

    """

def rampColorPort(q=1,e=1,ann="string",bgc="[float, float, float]",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,n="name",npm=1,p="string",pma=1,po=1,sc="string",si="string",sp="string",sbm="string",ut="string",vl=1,vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rampColorPort.html



-----------------------------------------

rampColorPort is undoable, queryable, and editable.

This command creates a control that displays an image representing the ramp
node specified, and supports editing of that node.


-----------------------------------------


Return Value:

string  The name of the port created or modified    
  
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

n     : node            [name] []
    Specifies the name of the newRamp texture node this port will represent.

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

sc    : selectedColorControl [string] ['edit']
    Set the name of the control (if any) which is to be used to show the color of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrColorSliderGrp.

-----------------------------------------

si    : selectedInterpControl [string] ['edit']
    Set the name of the control (if any) which is to be used to show the interpolation of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrEnumOptionMenuGrp.

-----------------------------------------

sp    : selectedPositionControl [string] ['edit']
    Set the name of the control (if any) which is to be used to show the position of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrFieldSliderGrp.

-----------------------------------------

sbm   : statusBarMessage [string] ['edit']
    Extra string to display in the status bar when the mouse is over the control.

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

vl    : verticalLayout  [boolean] ['query', 'edit']
    Set the preview's layout.

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

def render(amt=1,b=1,kpi=1,l="string",ngl=1,nsh=1,rep=1,x="int",y="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/render.html



-----------------------------------------

render is NOT undoable, NOT queryable, and NOT editable.

The render command is used to start off a MayaSoftware rendering session of
the currently active camera. If a rendering is already in progress, then this
command stops the rendering. This command is not undoable.


-----------------------------------------


Return Value:

string  The name of the rendered image.


-----------------------------------------


Flags:

-----------------------------------------

amt   : abortMissingTexture [boolean] []
    Abort renderer when encountered missing texture. Only available when -batch is set

-----------------------------------------

b     : batch           [boolean] []
    Run in batch mode. Compute the images for all renderable cameras. This is the mel equivalent of running maya in batch mode with the -render flag set. All other flags are ignored when -batch is used.

-----------------------------------------

kpi   : keepPreImage    [boolean] []
    Keep the renderings prior to post-process around. Only available when -batch is set

-----------------------------------------

l     : layer           [string] []
    Render the specified render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering.

-----------------------------------------

ngl   : nglowpass       [boolean] []
    Overwrite glow pass capabilities (can turn off glow pass globally by setting this value to false)

-----------------------------------------

nsh   : nshadows        [boolean] []
    Shadowing capabilities (can turn off shadow globally by setting this value to false)

-----------------------------------------

rep   : replace         [boolean] []
    Replace the rendered image if it already exists. Only available when -batch is set

-----------------------------------------

x     : xresolution     [int] []
    Overwrite x resolution

-----------------------------------------

y     : yresolution     [int]
    Overwrite y resolution

    """

def renderer(q=1,e=1,agn="string",agt="[string, string, string]",bro="string",bso="string",br="string",cbr="string",cir="string",cr="string",ex=1,gn=1,gtc=1,gtl=1,gtu=1,ipm="string",io="string",ips="string",ipr="string",irs="string",isr="string",lgc="string",log="string",mvl=1,mvp=1,mvs=1,ava=1,psi="string",pp="string",rfi="string",rd="string",rg="string",rm="string",ro="string",r="string",rr="string",rs="string",ui="string",res="string",brl="string",sbr="string",srl="string",sti="string",spi="string",scm=1,tb="string",unr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderer.html



-----------------------------------------

renderer is NOT undoable, queryable, and editable.

Command to register renders. This command allows you to specify the UI name
and procedure names for renderers. The command also allow you to query the UI
name and the procedure names for the registered renders.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

agn   : addGlobalsNode  [string] ['query', 'edit']
    This flag allows the user to add a globals node the specified renderer uses.

-----------------------------------------

agt   : addGlobalsTab   [[string, string, string]] ['edit']
    Add a tab associated with the specified renderer for the unified render globals window.

-----------------------------------------

bro   : batchRenderOptionsProcedure [string] ['query', 'edit']
    Set or query the batch render options procedure associated with the specified renderer.

-----------------------------------------

bso   : batchRenderOptionsStringProcedure [string] ['query', 'edit']
    Set or query the argument string that will be used with the command line utility 'Render' when doing a batch render

-----------------------------------------

br    : batchRenderProcedure [string] ['query', 'edit']
    Set or query the batch render procedure associated with the specified renderer.

-----------------------------------------

cbr   : cancelBatchRenderProcedure [string] ['query', 'edit']
    Set or query returns the cancel batch render procedure associated with the specified renderer.

-----------------------------------------

cir   : changeIprRegionProcedure [string] ['query', 'edit']
    Set or query the change IPR region procedure associated with the specified renderer.

-----------------------------------------

cr    : commandRenderProcedure [string] ['query', 'edit']
    Set or query the command line rendering procedure associated with the specified renderer.

-----------------------------------------

ex    : exists          [boolean] ['query', 'edit']
    The flag returns true if the specified renderer is registered in the registry, and it returns false otherwise.

-----------------------------------------

gn    : globalsNodes    [boolean] ['query', 'edit']
    This flag returns the list of render globals nodes the specified renderer uses.

-----------------------------------------

gtc   : globalsTabCreateProcNames [boolean] ['query', 'edit']
    This flag returns the names of procedures that are used to create the unified render globals window tabs that are associated with the specified renderer.

-----------------------------------------

gtl   : globalsTabLabels [boolean] ['query', 'edit']
    This flag returns the labels of unified render globals window tabs that are associated with the specified renderer.

-----------------------------------------

gtu   : globalsTabUpdateProcNames [boolean] ['query', 'edit']
    This flag returns the names of procedures that are used to update the unified render globals window tabs that are associated with the specified renderer.

-----------------------------------------

ipm   : iprOptionsMenuLabel [string] ['query', 'edit']
    Set or query the label for the IPR update options menu which is under the render view's IPR menu.

-----------------------------------------

io    : iprOptionsProcedure [string] ['query', 'edit']
    Set or query the IPR render options procedure associated with the specified renderer.

-----------------------------------------

ips   : iprOptionsSubMenuProcedure [string] ['query', 'edit']
    Set or query the procedure for creating the sub menu for the IPR update options menu which is under the render view's IPR menu.

-----------------------------------------

ipr   : iprRenderProcedure [string] ['query', 'edit']
    Set or query the IPR render command associated with the specified renderer.

-----------------------------------------

irs   : iprRenderSubMenuProcedure [string] ['query', 'edit']
    Set or query the procedure for creating the sub menu for the IPR render menu which is under the render view's IPR menu.

-----------------------------------------

isr   : isRunningIprProcedure [string] ['query', 'edit']
    Set or query the isRunningIpr command associated with the specified renderer.

-----------------------------------------

lgc   : logoCallbackProcedure [string] ['query', 'edit']
    Set or query the procedure which is a callback associated to the logo for the specified renderer. For example, the logo and the callback can be used in the unified render globals window beside the "Render Using" optionMenu.

-----------------------------------------

log   : logoImageName   [string] ['query', 'edit']
    Set or query the logo image name for the specified renderer. The logo is a image representing the renderer.

-----------------------------------------

mvl   : materialViewRendererList [boolean] ['query', 'edit']
    Returns the names of material view renderers that are currently registered.

-----------------------------------------

mvp   : materialViewRendererPause [boolean] ['query', 'edit']
    Specifies whether to pause the material viewer. Useful for globally halting updates to the material viewer. The material view renderer will remain suspended while the viewer is paused.

-----------------------------------------

mvs   : materialViewRendererSuspend [boolean] ['query', 'edit']
    Specifies whether to suspend or resume the material view renderer. Useful for temporarily stopping the material view renderer while another rendering task is running.

-----------------------------------------

ava   : namesOfAvailableRenderers [boolean] ['query', 'edit']
    Returns the names of renderers that are currently registered.

-----------------------------------------

psi   : pauseIprRenderProcedure [string] ['query', 'edit']
    Set or query the pause IPR render procedure associated with the specified renderer.

-----------------------------------------

pp    : polyPrelightProcedure [string] ['query', 'edit']
    Set or query the polygon prelight procedure associated with the specified renderer.

-----------------------------------------

rfi   : refreshIprRenderProcedure [string] ['query', 'edit']
    Set or query the refresh IPR render procedure associated with the specified renderer.

-----------------------------------------

rd    : renderDiagnosticsProcedure [string] ['query', 'edit']
    Set or query the render diagnostics procedure associated with the specified renderer.

-----------------------------------------

rg    : renderGlobalsProcedure [string] ['query', 'edit']
    This flag is obsolete. It will be removed in the next release.

-----------------------------------------

rm    : renderMenuProcedure [string] ['query', 'edit']
    This flag is obsolete. It will be removed in the next release.

-----------------------------------------

ro    : renderOptionsProcedure [string] ['query', 'edit']
    Set or query the render options procedure associated with the specified renderer.

-----------------------------------------

r     : renderProcedure [string] ['query', 'edit']
    Set or query the render command associated with the specified renderer.

-----------------------------------------

rr    : renderRegionProcedure [string] ['query', 'edit']
    Set or query the render region procedure associated with the specified renderer.

-----------------------------------------

rs    : renderSequenceProcedure [string] ['query', 'edit']
    Set or query the sequence rendering procedure associated with the specified renderer.

-----------------------------------------

ui    : rendererUIName  [string] ['query', 'edit']
    Set or query the rendererUIName for the specified renderer. The rendererUIName is the name of the renderer as it would appear in menus.

-----------------------------------------

res   : renderingEditorsSubMenuProcedure [string] ['query', 'edit']
    Set or query the procedure reponsible for creating renderer specific editors submenu under the "Rendering Editors" menu for the specified renderer.

-----------------------------------------

brl   : showBatchRenderLogProcedure [string] ['query', 'edit']
    Set or query the log file batch procedure associated with the specified renderer.

-----------------------------------------

sbr   : showBatchRenderProcedure [string] ['query', 'edit']
    Set or query the show batch render procedure associated with the specified renderer.

-----------------------------------------

srl   : showRenderLogProcedure [string] ['query', 'edit']
    Set or query the log file render procedure associated with the specified renderer.

-----------------------------------------

sti   : startIprRenderProcedure [string] ['query', 'edit']
    Set or query the start IPR render procedure associated with the specified renderer.

-----------------------------------------

spi   : stopIprRenderProcedure [string] ['query', 'edit']
    Set or query the stop IPR render procedure associated with the specified renderer.

-----------------------------------------

scm   : supportColorManagement [boolean] ['query', 'edit']
    Specifies whether the renderer supports color management.

-----------------------------------------

tb    : textureBakingProcedure [string] ['query', 'edit']
    Set or query the texture baking procedure associated with the specified renderer.

-----------------------------------------

unr   : unregisterRenderer [boolean]
    Unregister the specified renderer.

    """

def renderGlobalsNode(n="string",p="string",rq="string",rr="string",s=1,ss=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderGlobalsNode.html



-----------------------------------------

renderGlobalsNode is undoable, NOT queryable, and NOT editable.

This command creates a new node in the dependency graph of the specified type.

The renderGlobalsNode creates a render globals node and registers it with the
model. The createNode command will not register nodes of this type correctly.


-----------------------------------------


Return Value:

string  The name of the new node.    
string  The name of the render globals node


-----------------------------------------


Flags:

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.

-----------------------------------------

p     : parent          [string] []
    Specifies the parent in the DAG under which the new node belongs.

-----------------------------------------

rq    : renderQuality   [string] []
    Set the quality to be the renderQuality node with the given name.

-----------------------------------------

rr    : renderResolution [string] []
    Set the resolution to be the resolution node with the given name.

-----------------------------------------

s     : shared          [boolean] []
    This node is shared across multiple files, so only create it if it does not already exist.

-----------------------------------------

ss    : skipSelect      [boolean]
    This node is not to be selected after creation, the original selection will be preserved.

    """

def renderInfo(q=1,e=1,cs=1,ch="float",chr="float",ds=1,es=1,ms="float",n="string",o=1,ss=1,un="int",uch=1,ucr=1,udl=1,ums=1,ut="int",vn="int",vt="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderInfo.html



-----------------------------------------

renderInfo is undoable, queryable, and editable.

The renderInfo commands sets geometric properties of surfaces of the selected
object.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cs    : castShadows     [boolean] []
    Determines if object casts shadow or not.

-----------------------------------------

ch    : chordHeight     [float] []
    Tessellation subdivision criteria.

-----------------------------------------

chr   : chordHeightRatio [float] []
    Tessellation subdivision criteria.

-----------------------------------------

ds    : doubleSided     [boolean] []
    Determines if object double or single sided.

-----------------------------------------

es    : edgeSwap        [boolean] []
    Tessellation subdivision criteria.

-----------------------------------------

ms    : minScreen       [float] []
    Tessellation subdivision criteria.

-----------------------------------------

n     : name            [string] []
    Namespace to use.

-----------------------------------------

o     : opposite        [boolean] []
    Determines if the normals of the object is to be reversed.

-----------------------------------------

ss    : smoothShading   [boolean] []
    Determines if smooth shaded, or flat shaded - applies only to polysets.

-----------------------------------------

un    : unum            [int] []
    Tessellation subdivision criteria.

-----------------------------------------

uch   : useChordHeight  [boolean] []
    Tessellation subdivision criteria.

-----------------------------------------

ucr   : useChordHeightRatio [boolean] []
    Tessellation subdivision criteria.

-----------------------------------------

udl   : useDefaultLights [boolean] []
    Obsolete flag.

-----------------------------------------

ums   : useMinScreen    [boolean] []
    Tessellation subdivision criteria.

-----------------------------------------

ut    : utype           [int] []
    Tessellation subdivision criteria.

-----------------------------------------

vn    : vnum            [int] []
    Tessellation subdivision criteria.

-----------------------------------------

vt    : vtype           [int]
    Tessellation subdivision criteria.

    """

def renderManip(q=1,e=1,cam="[boolean, boolean, boolean, boolean, boolean]",lt="[boolean, boolean, boolean]",slt="[boolean, boolean, boolean, boolean, boolean, boolean, boolean]",st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderManip.html



-----------------------------------------

renderManip is undoable, queryable, and editable.

This command creates manipulators for cameras or lights.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cam   : camera          [[boolean, boolean, boolean, boolean, boolean]] ['query', 'edit']
    Query or edit the visiblity status of the component camera manipulators. The order of components are: cycling index, center of interest, pivot, clipping planes, and unused.

-----------------------------------------

lt    : light           [[boolean, boolean, boolean]] ['query', 'edit']
    Query or edit the visiblity status of the component light manipulators. The order of components are: cycling index, center of interest, and pivot.

-----------------------------------------

slt   : spotLight       [[boolean, boolean, boolean, boolean, boolean, boolean, boolean]] ['query', 'edit']
    Query or edit the visiblity status of the component spot light manipulators. The order of components are: cycling index, center of interest, pivot, cone angle, penumbra, look through barn doors, and decay regions.

-----------------------------------------

st    : state           [boolean]
    Query or edit the state of manipulators on an camera, ambient light, directional light, point light, or spot light. This flag's default value is on.

    """

def renderPartition(q=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderPartition.html



-----------------------------------------

renderPartition is undoable, queryable, and NOT editable.

Set or query the model's current partition. When flag q is not used, a partion
name must be passed as an argument. In this case the current partition is set
to that name.


-----------------------------------------


Return Value:

string  The render partition    
  
In query mode, return type is based on queried flag.
    """

def renderQualityNode(n="string",p="string",s=1,ss=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderQualityNode.html



-----------------------------------------

renderQualityNode is undoable, NOT queryable, and NOT editable.

This command creates a new node in the dependency graph of the specified type.

The renderQualityNode creates a render quality node and registers it with the
model. The createNode command will not register nodes of this type correctly.


-----------------------------------------


Return Value:

string  The name of the new node.    
string  The Name of the render quality node


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

def renderSettings(cam="string",cts="string",fin=1,fp=1,fpt=1,gin="string",ign=1,lin=1,lyr="string",lut=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderSettings.html



-----------------------------------------

renderSettings is NOT undoable, NOT queryable, and NOT editable.

Query interface to the common tab of the render settings


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

cam   : camera          [string] []
    Specify a camera that you want to replace the current renderable camera

-----------------------------------------

cts   : customTokenString [string] []
    Specify a custom key-value string to use to replace custom tokens in the file name. Use with firstImageName or lastImageName. Basic tokens (Scene, Layer, RenderLayer, Camera, Version, Extension) will be automatically expanded. Any other tokens must be specified here to be expanded. The format of the string is a space separated list of tokens-value pairs. For example, if the file name string is "myFile_<myToken>_<myOtherToken>_v" then the argument to this flag string should take the form "myToken=myTokenValue myOtherToken=myOtherTokenValue".

-----------------------------------------

fin   : firstImageName  [boolean] []
    Returns the first image name

-----------------------------------------

fp    : fullPath        [boolean] []
    Returns the full path for the image using the current project. Use with firstImageName, lastImageName, or genericFrameImageName.

-----------------------------------------

fpt   : fullPathTemp    [boolean] []
    Returns the full path for the preview render of the image using the current project. Use with firstImageName, lastImageName, or genericFrameImageName.

-----------------------------------------

gin   : genericFrameImageName [string] []
    Returns the generic frame image name with the custom specified frame index token

-----------------------------------------

ign   : imageGenericName [boolean] []
    Returns the image generic name

-----------------------------------------

lin   : lastImageName   [boolean] []
    Returns the last image name

-----------------------------------------

lyr   : layer           [string] []
    Specify a render layer name that you want to replace the current render layer

-----------------------------------------

lut   : leaveUnmatchedTokens [boolean]
    Do not remove unmatched tokens from the name string. Use with firstImageName or lastImageName.

    """

def renderThumbnailUpdate(q=1,fu="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderThumbnailUpdate.html



-----------------------------------------

renderThumbnailUpdate is undoable, queryable, and NOT editable.

Toggle the updating of object thumbnails. These are visible in tools like the
Attribute Editor and Hypershade. All thumbnails everywhere will not update to
reflect changes to the object until this command is used to toggle to true
unless a specific thumbnail is forced to render using the -forceUpdate flag.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

fu    : forceUpdate     [string]
    Force the thumbnail to update.

    """

def renderWindowEditor(q=1,e=1,ar=1,blm="int",cap="string",cc="[string, string, string, string]",cl="[int, int, float, float, float]",cme=1,com=1,cd="int",cif="string",ctl=1,crc="string",crg="string",dt="string",di="int",dvc="int",dst="string",dtg="string",dbf=1,da=1,en=1,ex=1,exp="float",f="string",fmc="string",fi=1,fr=1,ga="float",hlc="string",li="string",lck=1,mlc="string",mq="[float, float, float, float]",nim=1,nvi=1,ocm=1,pnl="string",p="string",pca="string",rs=1,ref=1,ra=1,ri=1,rr=1,rvi=1,si=1,sb="float",sg="float",sr="float",slc="string",srg="[int, int]",sbf=1,snp="[string, int, int]",snm=1,sts=1,s="int",sio="[string, string]",sm="string",tgl=1,up=1,ulk=1,upd=1,ut="string",vic="int",vtn="string",wi="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderWindowEditor.html



-----------------------------------------

renderWindowEditor is undoable, queryable, and editable.

Create a editor window that can receive the result of the rendering process


-----------------------------------------


Return Value:

string  The name of the editor    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ar    : autoResize      [boolean] ['query', 'edit']
    Lets the render view editor automatically resize the viewport or not.

-----------------------------------------

blm   : blendMode       [int] ['query', 'edit']
    Sets the blend mode for the render view. New image sent to the render view will be blended with the previous image in the render view, and the composited image will appear.

-----------------------------------------

cap   : caption         [string] ['query', 'edit']
    Sets the caption which appears at the bottom of the render view.

-----------------------------------------

cc    : changeCommand   [[string, string, string, string]] ['query', 'edit']
    Parameters:    * First string: command   * Second string: editorName   * Third string: editorCmd   * Fourth string: updateFunc  Call the command when something changes in the editor The command should have this prototype :   command(string $editor, string $editorCmd, string $updateFunc, int $reason)   The possible reasons could be :    * 0: no particular reason   * 1: scale color   * 2: buffer (single/double)   * 3: axis    * 4: image displayed   * 5: image saved in memory

-----------------------------------------

cl    : clear           [[int, int, float, float, float]] ['query', 'edit']
    Clear the image with the given color at the given resolution. Argumnets are respecively: width height red green blue.

-----------------------------------------

cme   : cmEnabled       [boolean] ['query', 'edit']
    Turn on or off applying color management in the View. If set, the color management configuration set in the current view is used.

-----------------------------------------

com   : colorManage     [boolean] ['edit']
    When used with the writeImage flag, causes the written image to be color-managed using the settings from the view color manager attached to the view.

-----------------------------------------

cd    : compDisplay     [int] ['query', 'edit']
    * 0 : disable compositing.   * 1 : displays the composited image immediately.    For example, when foreground layer tile is sent to the render view window, the composited tile is displayed in the render view window, and the original foreground layer tile is not displayed.    * 2 : display the un-composited image, and keep the composited image for the future command.    For example, when foreground layer tile is sent to the render view window, the original foreground layer tile is not displayed, and the composited tile is stored in a buffer.    * 3 : show the current composited image. If there is a composited image in the buffer, display it.

-----------------------------------------

cif   : compImageFile   [string] ['query', 'edit']
    Open the given image file and blend with the buffer as if the image was just rendered.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

crc   : currentCamera   [string] ['query', 'edit']
    Get or set the current camera. (used when redoing last render)

-----------------------------------------

crg   : currentCameraRig [string] ['query', 'edit']
    Get or set the current camera rig name. If a camera rig is specified, it will be used when redoing the last render as opposed to the currentCamera value, as the currentCamera value will hold the child camera last used for rendering the camera rig.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

di    : displayImage    [int] ['query', 'edit']
    Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.

-----------------------------------------

dvc   : displayImageViewCount [int] ['query']
    Query the number of views stored for a given image in the Editor Image Stack. This is not the same as querying using "viewImageCount" which returns the number of views for the current rendered image.

-----------------------------------------

dst   : displayStyle    [string] ['query', 'edit']
    Set the mode to display the image. Valid values are:    * "color" to display the basic RGB image   * "mask" to display the mask channel   * "lum" to display the luminance of the image

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

dbf   : doubleBuffer    [boolean] ['query', 'edit']
    Set the display in double buffer mode

-----------------------------------------

da    : drawAxis        [boolean] ['query', 'edit']
    Set or query whether the axis will be drawn.

-----------------------------------------

en    : editorName      [boolean] ['query']
    Returns the name of the editor, or an empty string if the editor has not been created yet.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

exp   : exposure        [float] ['query', 'edit']
    The exposure value used by the color management of the current view.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

fi    : frameImage      [boolean] ['query', 'edit']
    Frames the image inside the window.

-----------------------------------------

fr    : frameRegion     [boolean] ['query', 'edit']
    Frames the region inside the window.

-----------------------------------------

ga    : gamma           [float] ['query', 'edit']
    The gamma value used by the color management of the current view.

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

li    : loadImage       [string] ['edit']
    load an image from disk and set it as the current Editor Image

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

mq    : marquee         [[float, float, float, float]] ['query', 'edit']
    The arguments define the four corners of a rectangle: top left bottom right. The rectangle defines a marquee for the render computation.

-----------------------------------------

nim   : nbImages        [boolean] ['query']
    returns the number of images

-----------------------------------------

nvi   : nextViewImage   [boolean] ['edit']
    The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The nextViewImage flag tells the editor that it should prepare its internal image storage mechanism to store to the next view location.

-----------------------------------------

ocm   : outputColorManage [boolean] ['edit']
    When used with the writeImage flag, causes the written image to be color-managed using the outpute color space in the color preferences attached to the view.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

pca   : pcaption        [string] ['query', 'edit']
    Get or set the permanent caption which appears under the image that is currently showing in the render editor.

-----------------------------------------

rs    : realSize        [boolean] ['query', 'edit']
    Display the image with a one to one pixel match.

-----------------------------------------

ref   : refresh         [boolean] ['edit']
    requests a refresh of the current Editor Image.

-----------------------------------------

ra    : removeAllImages [boolean] ['edit']
    remove all the Editor Images from the Editor Image Stack

-----------------------------------------

ri    : removeImage     [boolean] ['edit']
    remove the current Editor Image from the Editor Image Stack

-----------------------------------------

rr    : resetRegion     [boolean] ['query', 'edit']
    Forces a reset of any marquee/region.

-----------------------------------------

rvi   : resetViewImage  [boolean] ['edit']
    The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The resetViewImage flag tells the editor that it should reset its internal image storage mechanism to the first image. This would happen at the very start of a render view render.

-----------------------------------------

si    : saveImage       [boolean] ['edit']
    save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the "di/displayImage" flag.

-----------------------------------------

sb    : scaleBlue       [float] ['query', 'edit']
    Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000

-----------------------------------------

sg    : scaleGreen      [float] ['query', 'edit']
    Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000

-----------------------------------------

sr    : scaleRed        [float] ['query', 'edit']
    Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

srg   : showRegion      [[int, int]] ['query', 'edit']
    Shows the current region at the given resolution. The two parameters define the width and height.

-----------------------------------------

sbf   : singleBuffer    [boolean] ['query', 'edit']
    Set the display in single buffer mode

-----------------------------------------

snp   : snapshot        [[string, int, int]] ['query', 'edit']
    Makes a copy of the camera of the model editor at the given size. First argument is the editor name, second is the width, third is the height.

-----------------------------------------

snm   : snapshotMode    [boolean] ['query', 'edit']
    Get or set the window's snapshot mode.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

s     : stereo          [int] ['query', 'edit']
    Puts the editor into stereo image mode. The effective resolution of the output image is twice the size of the horizontal size. The orientation of the images can be set using the stereoOrientation flag.

-----------------------------------------

sio   : stereoImageOrientation [[string, string]] ['query', 'edit']
    Specifies the orientation of stereo camera renders. The first argument specifies the orientation value for the firstleft image and the second argument specifies the orientation value for the right image. The orientation values are 'normal', the image appears as seen throught he camera, or 'mirrored', the image is mirrored horizontally.

-----------------------------------------

sm    : stereoMode      [string] ['query', 'edit']
    Specifies how the image is displayed in the view. By default the stereo is rendered with a side by side image. The rendered image is a single image that is twice the size of a normal image, 'both'. Users can also choose to display as 'redcyan', 'redcyanlum', 'leftonly', 'rightonly', or 'stereo'. both - displays both the left and right redcyan - displays the images as a red/cyan pair. redcyanlum - displays the luminance of the images as a red/cyan pair. leftonly - displays the left side only rightonly - displays the right side only stereo - mode that supports Crystal Eyes(tm) or Zscreen (tm) renders

-----------------------------------------

tgl   : toggle          [boolean] ['query', 'edit']
    Turns the ground plane display on/off.

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

vic   : viewImageCount  [int] ['query', 'edit']
    The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The viewImageCount flag tells the editor that it should prepare its internal image storage mechanism for a given number of views.

-----------------------------------------

vtn   : viewTransformName [string] ['query', 'edit']
    Sets/gets the view transform to be applied if color management is enabled in the current view.

-----------------------------------------

wi    : writeImage      [string]
    write the current Editor Image to disk

    """

def resolutionNode(n="string",p="string",s=1,ss=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/resolutionNode.html



-----------------------------------------

resolutionNode is undoable, NOT queryable, and NOT editable.

This command creates a new node in the dependency graph of the specified type.

The resolutionNode creates a render resolution node and registers it with the
model. The createNode command will not register nodes of this type correctly.


-----------------------------------------


Return Value:

string  The name of the new node.    
string  The name of the render resolution node


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

def sampleImage(f=1,r="[int, name]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sampleImage.html



-----------------------------------------

sampleImage is undoable, NOT queryable, and NOT editable.

The sampleImage command is used to control parameters of sample images, such
as swatches in the multilister. The fast option turns on or off some rendering
cheats which speed up the render but may cause edges to look ragged. The
resolution option specifies the width in pixels of the image which will be
rendered for the specified node. Note that the width of the image is also the
height of the image since sample images are square.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

f     : fastSample      [boolean] []
    If fast but rough rendering for sampleImage is to be used

-----------------------------------------

r     : resolution      [[int, name]]
    The first argument to this flag specifies a resolution in pixels. The second argument specifies a dependency node. The effect of this flag is that further sample image renderings for the specified node will be made at the specified resolution.

    """

def setDefaultShadingGroup(q=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setDefaultShadingGroup.html



-----------------------------------------

setDefaultShadingGroup is undoable, queryable, and NOT editable.

The setDefaultShadingGroup command is used to change which shading group is
considered the current default shading group. Subsequently created objects
will be assigned to the new default group.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.
    """

def shadingConnection(q=1,e=1,cs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shadingConnection.html



-----------------------------------------

shadingConnection is undoable, queryable, and editable.

Sets the connection state of a connection between nodes that are used in
shading. Specify the destination attribute of the connection.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cs    : connectionState [boolean]
    Specifies the state of the connection.   On/True/1 means the connection is still active.   Off/False/0 means the connection is inactive.

    """

def shadingNetworkCompare(q=1,nam=1,val=1,delete=1,eq=1,n1=1,n2=1,up=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shadingNetworkCompare.html



-----------------------------------------

shadingNetworkCompare is NOT undoable, queryable, and NOT editable.

This command allows you to compare two shading networks.


-----------------------------------------


Return Value:

string[] string int  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

nam   : byName          [boolean] []
    Indicates whether the comparison should consider node names. If true, two shading networks will be considered equivalent only if the names of corresponding nodes are the same, ignoring namespaces. If false, two shading networks will be considered equivalent even if corresponding nodes are named differently. Default is 'false'.

-----------------------------------------

val   : byValue         [boolean] []
    Indicates whether the comparison should consider the values of unconnected attributes. If true, two shading networks will be considered equivalent only if corresponding, unconnected attributes are the same type and have the same value. Only attributes of type 'int', 'bool', 'float', and 'string' will have their values compared. If false, two shading networks will be considered equivalent even if corresponding, unconnected attributes have different values or are different types. Default is 'true'.

-----------------------------------------

delete : delete          [boolean] []
    Deletes the specified comparison from memory.

-----------------------------------------

eq    : equivalent      [boolean] ['query']
    Returns an int. 1 if the shading networks in the specified comparison are equivalent. 0 otherwise.

-----------------------------------------

n1    : network1        [boolean] ['query']
    Returns a string[]. Returns an empty string array if the shading networks in the specified comparison are not equivalent. Otherwise returns the nodes in the first shading network.

-----------------------------------------

n2    : network2        [boolean] ['query']
    Returns a string[]. Returns an empty string array if the shading networks in the specified comparison are not equivalent. Otherwise returns the nodes in the second shading network.

-----------------------------------------

up    : upstreamOnly    [boolean]
    Indicates whether the comparison should consider nodes which are connected downstream from shading network nodes. If true, only those nodes which are upstream from the shading group will be considered. If, following only downstream connections, there is no connection path from a node to one of the shader attributes on the shading group, the node will not be considered. If false, a node will be considered if a connection path can found, following either upstream or downstream connections, which terminates with an input connection to one of the shading groups shader attributes. These dangling nodes do not directly contribute to the color, displacement, or volume characteristics of the shading group. Default is 'false'.

    """

def shadingNode(al=1,app=1,ar=1,asShader=1,at=1,au=1,icm=1,n="string",p="string",s=1,ss=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/shadingNode.html



-----------------------------------------

shadingNode is undoable, NOT queryable, and NOT editable.

This command creates a new node in the dependency graph of the specified type.

The shadingNode command classifies any DG node as a shader, texture light,
post process, or utility so that it can be properly organized in the multi-
lister. Recall that any DG node can be used a part of a a shader, texture or
light - regardless of how it is classified by this. command. These
classifications are provided for convenience in the UI.


-----------------------------------------


Return Value:

string  The name of the new node.    
string  (the name of the new node)


-----------------------------------------


Flags:

-----------------------------------------

al    : asLight         [boolean] []
    classify the current DG node as a light

-----------------------------------------

app   : asPostProcess   [boolean] []
    classify the current DG node as a post process

-----------------------------------------

ar    : asRendering     [boolean] []
    classify the current DG node as a rendering node

-----------------------------------------

asShader : asShader        [boolean] []
    classify the current DG node as a shader

-----------------------------------------

at    : asTexture       [boolean] []
    classify the current DG node as a texture

-----------------------------------------

au    : asUtility       [boolean] []
    classify the current DG node as a utility

-----------------------------------------

icm   : isColorManaged  [boolean] []
    classify the current DG node as being color managed

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

def showShadingGroupAttrEditor(q=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/showShadingGroupAttrEditor.html



-----------------------------------------

showShadingGroupAttrEditor is undoable, queryable, and NOT editable.

The showShadingGroupAttrEditor command opens up the attribute editor for the
current object's shading-group information.


-----------------------------------------


Return Value:

boolean  true if a shading group is displayed, otherwise false.    
  
In query mode, return type is based on queried flag.
    """

def soloMaterial(q=1,a="string",l=1,n="string",us=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/soloMaterial.html



-----------------------------------------

soloMaterial is undoable, queryable, and NOT editable.

Shows a preview of a specified material node output attribute.


-----------------------------------------


Return Value:

boolean  Success or Failure    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : attr            [string] ['query']
    The attr flag specifies a node attribute to solo.

-----------------------------------------

l     : last            [boolean] ['query']
    Whether to solo the last material node and attribute.

-----------------------------------------

n     : node            [string] ['query']
    The node flag specifies the node to solo.

-----------------------------------------

us    : unsolo          [boolean]
    Whether to remove soloing.

    """

def surfaceSampler(cam="name",ff="string",fn="string",fs="float",ft="uint",fu=1,fv=1,imf=1,it=1,mh="uint",mm=1,mo="string",sp="string",mw="uint",msd="linear",max="linear",os="uint",sc="string",sm="uint",so="linear",sh=1,s="string",sus="string",ss="uint",t="string",tus="string",ugn=1,uv="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/surfaceSampler.html



-----------------------------------------

surfaceSampler is undoable, NOT queryable, and NOT editable.

Maps surface detail from a source surface to a new texture map on a target
surface. Both objects must be selected when the command is invoked, with the
source surface selected first, and the target last.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cam   : camera          [name] []
    Specify the camera to use for camera specific lighting calculations such as specular highlights or reflections.

-----------------------------------------

ff    : fileFormat      [string] []
    The image format as a file extension (e.g. "dds"). This must be included once for every output map specified.

-----------------------------------------

fn    : filename        [string] []
    The filename to use when creating the map. This must be included once for every output map specified.

-----------------------------------------

fs    : filterSize      [float] []
    The filter size to use in pixels. Larger values (e.g. over 2.0) will produce smoother/softer results, while values closer to 1.0 will produce sharper results.

-----------------------------------------

ft    : filterType      [uint] []
    The filter type to use. 0 is a Guassian filter, 1 is a triangular filter, 2 is a box filter.

-----------------------------------------

fu    : flipU           [boolean] []
    Flip the U coordinate of the generated image.

-----------------------------------------

fv    : flipV           [boolean] []
    Flip the V coordinate of the generated image.

-----------------------------------------

imf   : ignoreMirroredFaces [boolean] []
    Stops reverse wound (i.e. mirrored) faces from contributing to the map generation.

-----------------------------------------

it    : ignoreTransforms [boolean] []
    Controls whether transforms are used (meaning the search is performed in worldspace), or not (meaning the search is performed in object space).

-----------------------------------------

mh    : mapHeight       [uint] []
    Pixel width of the generated map. This must be included once for every output map specified.

-----------------------------------------

mm    : mapMaterials    [boolean] []
    Where appropriate (e.g. normal maps), this controls whether the material should be included when sampling the map attribute. This must be included once for every output map specified.

-----------------------------------------

mo    : mapOutput       [string] []
    Specifies a new output map to create. One of "normal", "displacement" "diffuseRGB", "litAndShadedRGB", or "alpha"

-----------------------------------------

sp    : mapSpace        [string] []
    The space to generate the map in. Valid keyword is "object". Default is tangent space. This must be included once for every output map specified.

-----------------------------------------

mw    : mapWidth        [uint] []
    Pixel width of the generated map. Some output image formats require even or power of 2. This must be included once for every output map specified.

-----------------------------------------

msd   : maxSearchDistance [linear] []
    Controls the maximum distance away from a target surface that will be searched for source surfaces. A value of 0 indicates no limit. When generated maps include artifacts from the "other side" of an object, try setting this value to a distance approximately equal to the radius of the object. If this flag is included, it must be included once for every target.

-----------------------------------------

max   : maximumValue    [linear] []
    The maximum value to include in the map. This allows control of how floating point values (like displacement) are quantised into integer image formats.

-----------------------------------------

os    : overscan        [uint] []
    The number of additional pixels to render around UV borders. This will help to minimise texel filtering artifacts on UV seams. When mipmaps are going to be generated for the texture a higher value may be necessary (in addition to a filterSize greater than 1).

-----------------------------------------

sc    : searchCage      [string] []
    Specifies a search envelope surface to use as a search guide when looking for source surfaces. If this flag is included, it must be included once for every target.

-----------------------------------------

sm    : searchMethod    [uint] []
    Controls the search method used to match sample points on a target surface to points on the sources. 0 is closest to envelope, 1 is prefer any intersection inside envelope to intersections outside it, and 2 is only use intersections inside envelope.

-----------------------------------------

so    : searchOffset    [linear] []
    Specifies a fixed offset from a target surface to use as the starting point when looking for source surfaces. This value is only used when no search cage is specified for a given target. If this flag is included, it must be included once for every target.

-----------------------------------------

sh    : shadows         [boolean] []
    Where appropriate (e.g. lit and shaded), this controls whether shadows are included in the calculation. Currently only depth map shadows are supported.

-----------------------------------------

s     : source          [string] []
    Specifies a surface to use as a sampling source

-----------------------------------------

sus   : sourceUVSpace   [string] []
    Specifies that the transfer of data between the surfaces should be done in UV space and specifies the name of the UV set on the source surface(s) that should be used as the transfer space.

-----------------------------------------

ss    : superSampling   [uint] []
    Controls the number of sampling points calculated for each output value. The algorithm will use 2 ^ n squared samples for each point (so a value of 0 will use a single sample, while a value of 3 will calculate 64 samples for each point).

-----------------------------------------

t     : target          [string] []
    Specified a surface to sample output information for.

-----------------------------------------

tus   : targetUVSpace   [string] []
    Specifies that the transfer of data between the surfaces should be done in UV space and specifies the name of the UV set on the target surface(s) that should be used as the transfer space.

-----------------------------------------

ugn   : useGeometryNormals [boolean] []
    Controls whether geometry or surface normals are used for surface searching. Using geometry normals will ensure a smooth mapping but can introduce distorted mappings where there are large distances between the source and target surfaces. Surface normals can introduce overlapping or discontinuous mappings, but does allow map distortion to be influenced by surface normal direction.

-----------------------------------------

uv    : uvSet           [string]
    The name of the UV set to use when creating output maps. If this flag is included, it must be included once for every target.

    """

def surfaceShaderList(q=1,e=1,add="name",rm="name"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/surfaceShaderList.html



-----------------------------------------

surfaceShaderList is undoable, queryable, and editable.

Add/Remove a relationship between an object and the current shading group.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : add             [name] []
    add object(s) to shader group list.

-----------------------------------------

rm    : remove          [name]
    remove object(s) to shader group list.

    """

def swatchRefresh():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/swatchRefresh.html



-----------------------------------------

swatchRefresh is NOT undoable, NOT queryable, and NOT editable.

The swatchRefresh command causes image source node swatches to be refreshed on
screen. The purpose of this command is to provide a mechanism to trigger a
swatch refresh in cases that are not subject to dirty propagation in the
dependency graph. This command only works with imageSource-derived node types.
Invoking this command with no arguments will cause all imageSource swatches to
be refreshed.


-----------------------------------------


Return Value:

boolean  true if all arguments are valid image source nodes and the operation
succeded.
    """

def textureWindow(q=1,e=1,ast=1,axc="[float, float, float]",bfc="[float, float, float, float]",cpt="string",csn="int",cc="[string, string, string, string]",cc1="[float, float, float]",cc2="[float, float, float]",ccm="int",cd="int",cdt=1,cg1="[float, float, float]",cg2="[float, float, float]",cgo=1,ctc="[float, float, float]",ci=1,cme=1,ctl=1,dt="string",dax=1,dct=1,ddt=1,ddl=1,dgl=1,di="int",dih=1,dl=1,doh=1,dps=1,drh=1,dsm=1,dst="string",dtb=1,dsh=1,duh=1,dph=1,dta="float",dpo=1,d="int",dtg="string",dbf=1,da=1,dsr=1,ex=1,exp="float",f="string",fmc="string",frb=1,fa=1,fs=1,ffc="[float, float, float, float]",ga="float",glc="[float, float, float]",gnc="[float, float, float]",hlc="string",ibc="[float, float, float]",idm=1,id=1,imn=1,imageNumber="int",ip=1,imr=1,irv="float",imageSize=1,itr="[float, float, float, float]",iuf=1,internalFaces=1,lp="string",li="string",lck=1,mlc="string",mrs="int",mca="float",nim=1,nv=1,nuv=1,ni="int",nt="int",pnl="string",p="string",pv=1,rs=1,ref=1,rf=1,ra=1,ri=1,rds="string",r=1,si=1,sb="float",sg="float",sr="float",sif=1,srf=1,slc="string",suv="int",sbf=1,s="float",s3d=1,scs="int",sps=1,sp="float",sts=1,st="int",sdc="[float, float, float]",t3d=1,tbc="[float, float, float]",tbw="int",txn=1,tn="int",tlb=1,tlc="[float, float, float]",tgl=1,tge=1,tgg=1,up=1,ulk=1,upd=1,uf=1,ut="string",upr="[float, float, float, float]",uvs=1,vpi=1,vtn="string",wcc="[float, float, float, float]",woc="[float, float, float, float]",wi="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/textureWindow.html



-----------------------------------------

textureWindow is undoable, queryable, and editable.

This command is used to create a UV Editor and to query or edit the texture
editor settings.

The UV Editor displays texture mapped polygon objects in 2D texture space.
Only active objects are visible in this window.

The UV Editor has the ability to display two types of images. The Texture
Image is a visualisation of the current texture and associated placement
parameters. The Editor Image is a user specified image loaded from disk.

A UV Editor can be invoked by selecting the "Window -> UV Texture Editor..."
menu item from the main maya menu listing that appears at the top of the maya
window. It can also be invoked by selecting the "Panel -> UV Editor" item
under the "Panels" menu item that appears at the top right hand corner of the
view.

As a UV Editor typically exists at start-up time, and as only one of these can
exist at any given time, this command is normally used to query and edit the
editor settings.


-----------------------------------------


Return Value:

string  The name of the texture window    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ast   : activeSelectionOnTop [boolean] ['query', 'edit']
    Display the solid map / distortion of active selection on top of others.

-----------------------------------------

axc   : axesColor       [[float, float, float]] ['query', 'edit']
    The color of axes, default is 0.0 0.0 1.0

-----------------------------------------

bfc   : backFacingColor [[float, float, float, float]] ['query', 'edit']
    Sets or queries the RGBA back facing color.

-----------------------------------------

cpt   : capture         [string] ['edit']
    Perform an one-time capture of the viewport to the named image file on disk.

-----------------------------------------

csn   : captureSequenceNumber [int] ['edit']
    When a number greater or equal to 0 is specified each subsequent refresh will save an image file to disk if the capture flag has been enabled. The naming of the file is: {root name}.#.{extension} if the name {root name}.{extension} is used for the capture flag argument. The value of # starts at the number specified to for this argument and increments for each subsequent refresh. Sequence capture can be disabled by specifying a number less than 0 or an empty file name for the capture flag.

-----------------------------------------

cc    : changeCommand   [[string, string, string, string]] ['query', 'edit']
    Parameters:    * First string: command   * Second string: editorName   * Third string: editorCmd   * Fourth string: updateFunc  Call the command when something changes in the editor The command should have this prototype :   command(string $editor, string $editorCmd, string $updateFunc, int $reason)   The possible reasons could be :    * 0: no particular reason   * 1: scale color   * 2: buffer (single/double)   * 3: axis    * 4: image displayed   * 5: image saved in memory

-----------------------------------------

cc1   : checkerColor1   [[float, float, float]] ['query', 'edit']
    Sets the first color of the checker and identification pattern, when color mode is 2-colors.

-----------------------------------------

cc2   : checkerColor2   [[float, float, float]] ['query', 'edit']
    Sets the second color of the checker and identification pattern, when color mode is 2-colors.

-----------------------------------------

ccm   : checkerColorMode [int] ['query', 'edit']
    Sets the color mode of the checker and identification pattern. 0: multi- colors; 1: 2-colors;

-----------------------------------------

cd    : checkerDensity  [int] ['query', 'edit']
    Sets the density of the checker and identification pattern.

-----------------------------------------

cdt   : checkerDrawTileLabels [boolean] ['query', 'edit']
    Toggles the checker tile label display.

-----------------------------------------

cg1   : checkerGradient1 [[float, float, float]] ['query', 'edit']
    Sets the first gradient of the checker and identification pattern, when color mode is 2-colors.

-----------------------------------------

cg2   : checkerGradient2 [[float, float, float]] ['query', 'edit']
    Sets the second gradient of the checker and identification pattern, when color mode is 2-colors.

-----------------------------------------

cgo   : checkerGradientOverlay [boolean] ['query', 'edit']
    Toggle application of the gradient.

-----------------------------------------

ctc   : checkerTileLabelColor [[float, float, float]] ['query', 'edit']
    Sets the checker tile label color.

-----------------------------------------

ci    : clearImage      [boolean] ['edit']
    Clears the current Editor Image.

-----------------------------------------

cme   : cmEnabled       [boolean] ['query', 'edit']
    Turn on or off applying color management in the editor. If set, the color management configuration set in the current editor is used.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dax   : displayAxes     [boolean] ['query', 'edit']
    Specify true to display the grid axes.

-----------------------------------------

dct   : displayCheckered [boolean] ['query', 'edit']
    Display a unique checker and identification pattern for each UV tiles.

-----------------------------------------

ddt   : displayDistortion [boolean] ['query', 'edit']
    Display the layout in shaded colors to indentify areas with stretched/squashed UVs

-----------------------------------------

ddl   : displayDivisionLines [boolean] ['query', 'edit']
    Specify true to display the subdivision lines between grid lines.

-----------------------------------------

dgl   : displayGridLines [boolean] ['query', 'edit']
    Specify true to display the grid lines.

-----------------------------------------

di    : displayImage    [int] ['query', 'edit']
    Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.

-----------------------------------------

dih   : displayIsolateSelectHUD [boolean] ['query', 'edit']
    Show heads-up display of isolate selection

-----------------------------------------

dl    : displayLabels   [boolean] ['query', 'edit']
    Specify true to display the grid line numeric labels.

-----------------------------------------

doh   : displayOverlappingUVCountHUD [boolean] ['query', 'edit']
    Show heads-up display of overlapping UV count, as a part UV Statistics HUD

-----------------------------------------

dps   : displayPreselection [boolean] ['query', 'edit']
    Toggles the pre-selection display.

-----------------------------------------

drh   : displayReversedUVCountHUD [boolean] ['query', 'edit']
    Show heads-up display of UV Shells, as a part UV Statistics HUD

-----------------------------------------

dsm   : displaySolidMap [boolean] ['query', 'edit']
    Display a solid overlay for the active texture map.

-----------------------------------------

dst   : displayStyle    [string] ['query', 'edit']
    Set the mode to display the image. Valid values are:    * "color" to display the basic RGB image   * "mask" to display the mask channel   * "lum" to display the luminance of the image

-----------------------------------------

dtb   : displayTextureBorder [boolean] ['query', 'edit']
    Toggles the texture borders display.

-----------------------------------------

dsh   : displayUVShellCountHUD [boolean] ['query', 'edit']
    Show heads-up display of UV Shell count, as a part UV Statistics HUD

-----------------------------------------

duh   : displayUVStatisticsHUD [boolean] ['query', 'edit']
    Show heads-up display of UV Statistics

-----------------------------------------

dph   : displayUsedPercentageHUD [boolean] ['query', 'edit']
    Show heads-up display of used UV space percentage, as a part UV Statistics HUD

-----------------------------------------

dta   : distortionAlpha [float] ['query', 'edit']
    Set or query the distortion display alpha.

-----------------------------------------

dpo   : distortionPerObject [boolean] ['query', 'edit']
    Toggles the per-object distortion display.

-----------------------------------------

d     : divisions       [int] ['query', 'edit']
    Sets the number of subdivisions between main grid lines.

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

dbf   : doubleBuffer    [boolean] ['query', 'edit']
    Set the display in double buffer mode

-----------------------------------------

da    : drawAxis        [boolean] ['query', 'edit']
    Set or query whether the axis will be drawn.

-----------------------------------------

dsr   : drawSubregions  [boolean] ['query', 'edit']
    Toggles the subregion display.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

exp   : exposure        [float] ['query', 'edit']
    The exposure value used by the color management of the current editor.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

frb   : forceRebake     [boolean] ['edit']
    Forces the current cache texture to refresh.

-----------------------------------------

fa    : frameAll        [boolean] []
    This will zoom on the whole scene.

-----------------------------------------

fs    : frameSelected   [boolean] []
    This will zoom on the currently selected objects.

-----------------------------------------

ffc   : frontFacingColor [[float, float, float, float]] ['query', 'edit']
    Sets or queries the RGBA front facing color.

-----------------------------------------

ga    : gamma           [float] ['query', 'edit']
    The gamma value used by the color management of the current editor.

-----------------------------------------

glc   : gridLinesColor  [[float, float, float]] ['query', 'edit']
    The color of grid lines, default is 0.325 0.325 0.325

-----------------------------------------

gnc   : gridNumbersColor [[float, float, float]] ['query', 'edit']
    The color of grid numbers, default is 0.2 0.2 0.2

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

ibc   : imageBaseColor  [[float, float, float]] ['query', 'edit']
    The base color of the image, default is white 1.0 1.0 1.0

-----------------------------------------

idm   : imageDim        [boolean] ['query', 'edit']
    Toggles the image dimming.

-----------------------------------------

id    : imageDisplay    [boolean] ['query', 'edit']
    Toggles the Texture Image display.

-----------------------------------------

imn   : imageNames      [boolean] ['query']
    List image names for all Texture Images available for display, if any.

-----------------------------------------

imageNumber : imageNumber     [int] ['query', 'edit']
    Sets the number of Texture Images to display. This depends on the number of textures corresponding to the current selection. If there are N textures, then the possible Texture Image numbers are 0 to N-1.

-----------------------------------------

ip    : imagePixelSnap  [boolean] ['query', 'edit']
    Sets a mode so that UV transformations in the UV Texture Editor will cause UV values to snap to image pixel corners. Which pixels are used depends on whether a Texture Image or an Editor Image is being displayed. If both are displayed, the Texture Image pixels will be used.

-----------------------------------------

imr   : imageRatio      [boolean] ['query', 'edit']
    Sets the window to draw using the Texture Image's height versus width ratio. If the width is greater than the height, then the width is set to be 1 "unit" in the window, and the height is adjusted by width divided by height. This only affects the display of a Texture Image, not an Editor Image.

-----------------------------------------

irv   : imageRatioValue [float] ['query']
    Query current image ratio value in UV Editor.

-----------------------------------------

imageSize : imageSize       [boolean] ['query']
    Returns the size of the Texture Image currently being displayed. The values returned are width followed by height. Image size can only be queried.

-----------------------------------------

itr   : imageTileRange  [[float, float, float, float]] ['query', 'edit']
    Sets the UV range of the display. The 4 values specify the minimum U, V and maximum U, V in that order. When viewing a texture image, these values affect how many times the image is tiled based on appropriate parameters (e.g. Repeat UV, Mirror, Wrap, etc...) When viewing an Editor Image these values determine the visible size of the image. For example, setting the range to ( 0, 0, 2, 1 ) will cause the Editor Image to be loaded into a 2x1 rectangle, distorting it as necessary to fill the available space.

-----------------------------------------

iuf   : imageUnfiltered [boolean] ['query', 'edit']
    Sets the Texture Image to draw unfiltered. The image will appear "pixelated" when the display resolution is higher than the resolution of the image.

-----------------------------------------

internalFaces : internalFaces   [boolean] ['query', 'edit']
    Display contained faces by the selected components.

-----------------------------------------

lp    : labelPosition   [string] ['query', 'edit']
    The position of the grid's numeric labels. Valid values are "axis" and "edge".

-----------------------------------------

li    : loadImage       [string] ['edit']
    load an image from disk and set it as the current Editor Image

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

mrs   : maxResolution   [int] ['query', 'edit']
    This flag will set the current cached texture's maximum resolution.

-----------------------------------------

mca   : multiColorAlpha [float] ['query', 'edit']
    Sets the multi-color alpha of shaded UVs.

-----------------------------------------

nim   : nbImages        [boolean] ['query']
    returns the number of images

-----------------------------------------

nv    : nextView        [boolean] ['edit']
    Switches to the next view.

-----------------------------------------

nuv   : numUvSets       [boolean] ['query', 'edit']
    This flag will return the number of UV sets for selected objects in the texture window.

-----------------------------------------

ni    : numberOfImages  [int] ['query']
    The number of Texture Images currently available. for display.

-----------------------------------------

nt    : numberOfTextures [int] ['query']
    The number of textures currently available. for display.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

pv    : previousView    [boolean] ['edit']
    Switches to the previous view.

-----------------------------------------

rs    : realSize        [boolean] []
    This will display the image with the size of the internal buffer. Note: This argument no long has any affect on image display.

-----------------------------------------

ref   : refresh         [boolean] ['edit']
    requests a refresh of the current Editor Image.

-----------------------------------------

rf    : relatedFaces    [boolean] ['query', 'edit']
    Display connected faces by the selected components.

-----------------------------------------

ra    : removeAllImages [boolean] ['edit']
    remove all the Editor Images from the Editor Image Stack

-----------------------------------------

ri    : removeImage     [boolean] ['edit']
    remove the current Editor Image from the Editor Image Stack

-----------------------------------------

rds   : rendererString  [string] ['query', 'edit']
    Set or query the string describing the current renderer.

-----------------------------------------

r     : reset           [boolean] []
    Resets the ground plane to its default values.

-----------------------------------------

si    : saveImage       [boolean] ['edit']
    save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the "di/displayImage" flag.

-----------------------------------------

sb    : scaleBlue       [float] ['query', 'edit']
    Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000

-----------------------------------------

sg    : scaleGreen      [float] ['query', 'edit']
    Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000

-----------------------------------------

sr    : scaleRed        [float] ['query', 'edit']
    Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000

-----------------------------------------

sif   : selectInternalFaces [boolean] ['query', 'edit']
    Add to selectionList the faces which are contained by (internal to) selected components.

-----------------------------------------

srf   : selectRelatedFaces [boolean] []
    Add to selectionList the faces which are connected to (non-internally related to) selected components.

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

suv   : setUvSet        [int] ['edit']
    This flag will set the current UV set on one given selected object within the texture window.

-----------------------------------------

sbf   : singleBuffer    [boolean] ['query', 'edit']
    Set the display in single buffer mode

-----------------------------------------

s     : size            [float] ['query', 'edit']
    Sets the size of the grid.

-----------------------------------------

s3d   : solidMap3dView  [boolean] ['query', 'edit']
    Display a solid overlay for the active texture map in 3D viewport.

-----------------------------------------

scs   : solidMapColorSeed [int] ['query', 'edit']
    Sets the multi-color seed of shaded UVs.

-----------------------------------------

sps   : solidMapPerShell [boolean] ['query', 'edit']
    Display a solid overlay with a random color per shell.

-----------------------------------------

sp    : spacing         [float] []
    Sets the spacing between main grid lines.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

st    : style           [int] ['query', 'edit']
    This flag is obsolete and should not be used.

-----------------------------------------

sdc   : subdivisionLinesColor [[float, float, float]] ['query', 'edit']
    The color of subdivision lines, default is 0.25 0.25 0.25

-----------------------------------------

t3d   : textureBorder3dView [boolean] ['query', 'edit']
    Toggles the texture borders display in 3d viewport.

-----------------------------------------

tbc   : textureBorderColor [[float, float, float]] ['query', 'edit']
    Sets the display color of texture border.

-----------------------------------------

tbw   : textureBorderWidth [int] ['query', 'edit']
    Set the display edge width of texture border.

-----------------------------------------

txn   : textureNames    [boolean] ['query']
    Texture names for all Texture Images available for display, if any.

-----------------------------------------

tn    : textureNumber   [int] ['query', 'edit']
    Sets the number of textures to display This depends on the number of textures corresponding to the current selection. If there are N textures, then the possible Texture Image numbers are 0 to N-1.

-----------------------------------------

tlb   : tileLabels      [boolean] ['query', 'edit']
    Toggles the texture tile label display.

-----------------------------------------

tlc   : tileLinesColor  [[float, float, float]] ['query', 'edit']
    The color of tile lines, default is 0.0 0.0 0.0

-----------------------------------------

tgl   : toggle          [boolean] ['query', 'edit']
    Toggles the ground plane display.

-----------------------------------------

tge   : toggleExposure  [boolean] ['edit']
    Toggles between the current and the default exposure value of the editor.

-----------------------------------------

tgg   : toggleGamma     [boolean] ['edit']
    Toggles between the current and the default gamma value of the editor.

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

uf    : useFaceGroup    [boolean] ['query', 'edit']
    Display faces that are associated with the groupId that is set on the mesh node that is drawn. (The attribute "displayFacesWithGroupId")

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

upr   : usedPercentageHUDRange [[float, float, float, float]] ['query', 'edit']
    Sets the range when calculating used UV space percentage. The 4 values specify the minimum U, V and maximum U, V in that order., default is 0 0 1 1.

-----------------------------------------

uvs   : uvSets          [boolean] ['query', 'edit']
    This flag will return strings containing UV set and object name pairs for selected objects in the texture window. The syntax of each pair is "objectName | uvSetName", where | is a literal character.

-----------------------------------------

vpi   : viewPortImage   [boolean] ['edit']
    Toggles the view port/ caching Texture Images.

-----------------------------------------

vtn   : viewTransformName [string] ['query', 'edit']
    Sets the view pipeline to be applied if color management is enabled in the current editor.

-----------------------------------------

wcc   : wireframeComponentColor [[float, float, float, float]] ['query', 'edit']
    Sets or queries the RGBA component wireframe color.

-----------------------------------------

woc   : wireframeObjectColor [[float, float, float, float]] ['query', 'edit']
    Sets or queries the RGBA object wireframe color.

-----------------------------------------

wi    : writeImage      [string]
    write the current Editor Image to disk

    """

def uvLink(q=1,b=1,iv=1,m=1,qo="name",t="name",uvs="name"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/uvLink.html



-----------------------------------------

uvLink is undoable, queryable, and NOT editable.

This command is used to make, break and query UV linking relationships between
UV sets on objects and textures that use those UV sets.

If no make, break or query flag is specified and both uvSet and texture flags
are present, the make flag is assumed to be specified.

If no make, break or query flag is specified and only one of the uvSet and
texture flags is present, the query flag is assumed to be specified.

The term "texture" in the context of UV linking is a bit of an
oversimplification. In fact, UV sets can be linked to any node which takes UV
coordinates as input. However in most cases it will be a texture to which you
wish to link a UV set.


-----------------------------------------


Return Value:

string  or array of strings for query boolean for isValid    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : b               [boolean] []
    The presence of this flag on the command indicates that the command is being invoked to break links between UV sets and textures.

-----------------------------------------

iv    : isValid         [boolean] []
    This flag is used to verify whether or not a texture or UV set is valid for the purposes of UV linking. It should be used in conjunction with either the -texture flag or the -uvSet flag, but not both at the same time.

-----------------------------------------

m     : make            [boolean] []
    The presence of this flag on the command indicates that the command is being invoked to make links between UV sets and textures.

-----------------------------------------

qo    : queryObject     [name] []
    This flag should only be used in conjunction with a query of a texture. This flag is used to indicate that the results of the query should be limited to UV sets of the object specified by this flag.

-----------------------------------------

t     : texture         [name] []
    The argument to the texture flag specifies the texture to be used by the command in performing the action.

-----------------------------------------

uvs   : uvSet           [name]
    The argument to the uvSet flag specifies the UV set to be used by the command in performing the action.

    """

def vectorize(bv=1,bf="float",c="string",cfe=1,cf=1,ct="float",ce="string",dl="int",ec="[int, int, int]",ed=1,es="string",ew="float",ef="float",ff="string",fs="string",fv="int",fr="int",h="int",he=1,hl="int",hi=1,imageFormat="string",l="name",mea="float",oai=1,of="string",par="float",rd="int",rf=1,rl=1,ro="string",rv=1,scf=1,sh=1,sb=1,sf="float",sa="string",sc=1,w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/vectorize.html



-----------------------------------------

vectorize is NOT undoable, NOT queryable, and NOT editable.

This command renders Maya scenes to various vector and raster formats using
the Maya Vector renderer.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

bv    : browserView     [boolean] []
    Specifies whether to preview the render in the browser. This option is swf only.

-----------------------------------------

bf    : byFrame         [float] []
    Specifies the frame increment.

-----------------------------------------

c     : camera          [string] []
    Specifies the camera to render.

-----------------------------------------

cfe   : combineFillsEdges [boolean] []
    Specifies whether fills and edges should be combined as a single object in Flash. This option is swf only.

-----------------------------------------

cf    : currentFrame    [boolean] []
    Specifies whether to render the current frame only.

-----------------------------------------

ct    : curveTolerance  [float] []
    Specifies the curve tolerance. Valid values are in the range: 0.0 to 15.0. The curve tolerance determines how aggressively the renderer tries to fit a series of connected, consecutive line segments to a curve. A value of 0.0 causes all line segments to be drawn without curve fitting. A value of 15.0 causes aggressive curve fitting.

-----------------------------------------

ce    : customExtension [string] []
    Specifies a custom extension to use for the filename. Any non-empty string is valid.

-----------------------------------------

dl    : detailLevel     [int] []
    Specifies the detail level. Valid values are: 0 to 50. The smaller the value, the more polygons may be combined to produce smaller files. A higher value results in a more accurate render, but also larger files and longer render times.

-----------------------------------------

ec    : edgeColor       [[int, int, int]] []
    Specifies the red, green, and blue components of the edge color. Valid values are: 0 to 255 for each color component.

-----------------------------------------

ed    : edgeDetail      [boolean] []
    Specifies whether edge detail should be rendered; ie. edges that have an angle between the face normals of any two adjacent polygons sharing an edge that is greater than the minimum edge angle (specified by the -mea flag).

-----------------------------------------

es    : edgeStyle       [string] []
    Specifies the edge style. Valid values are: "Outline", "EntireMesh", "None".

-----------------------------------------

ew    : edgeWeight      [float] []
    Specifies the edge weight to be used for all edges in points. There are 72 points per inch. A value of 0.0 specifies hairline edge weight.

-----------------------------------------

ef    : endFrame        [float] []
    Specifies the end frame.

-----------------------------------------

ff    : filenameFormat  [string] []
    Specifies the file name format. Valid values are: "name", "name.ext", "name.#.ext", "name.ext.#", "name.#", "name#.ext", "name_#.ext".

-----------------------------------------

fs    : fillStyle       [string] []
    Specifies the fill style. Valid values are: "SingleColor", "TwoColor", "FourColor", "FullColor", "AverageColor", "AreaGradient", "MeshGradient", "None". AreaGradient and MeshGradient are not available for the eps and ai image formats.

-----------------------------------------

fv    : flashVersion    [int] []
    Specifies the Flash version of the swf output. Valid values are: 3, 4, 5\. This option is swf only.

-----------------------------------------

fr    : frameRate       [int] []
    Specifies the frame rate. This option is for svg and swf only.

-----------------------------------------

h     : height          [int] []
    Specifies the height of the output image in pixels.

-----------------------------------------

he    : hiddenEdges     [boolean] []
    Specifies whether hidden edges should be rendered; ie. edges that have are not visible from the camera.

-----------------------------------------

hl    : highlightLevel  [int] []
    Specifies the highlight level. Valid values are: 1 to 8. The value specifies how many concentric rings will be used to render an object's highlight. This option is for the SingleColor, AverageColor, and AreaGradient fill styles only.

-----------------------------------------

hi    : highlights      [boolean] []
    Specifies whether highlights should be rendered. This option has no effect for ai, eps, and svg. This option is for the SingleColor, AverageColor, and AreaGradient fill styles only.

-----------------------------------------

imageFormat : imageFormat     [string] []
    Specifies the image format to render. Valid values for the Windows and Mac platforms are: "swf", "eps", "ai", "svg", "jpg", "iff", "sgi", "tga", "tif", "bmp". Additional valid values for the Windows platform are: "als", "cin", "gif", "yuv", "rla", "si". Additional valid values for the Mac platform are: "pntg", "ps", "png", "pict", "qtif", "qt".

-----------------------------------------

l     : layer           [name] []
    Render the specified render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering.

-----------------------------------------

mea   : minEdgeAngle    [float] []
    Specifies the minimum edge angle in degrees. Valid values are: 0.0 to 90.0. This angle is the minimum angle between adjacent polygon face normals that is used to determine if the edge is rendered when the -ed flag is specified.

-----------------------------------------

oai   : outlinesAtIntersections [boolean] []
    Specifies if edges should be drawn when two polygons intersect. By default this flag is enabled.

-----------------------------------------

of    : outputFileName  [string] []
    Specifies the output file name.

-----------------------------------------

par   : pixelAspectRatio [float] []
    Specifes the pixel aspect ratio.

-----------------------------------------

rd    : reflectionDepth [int] []
    Specifies the reflection depth. Valid values are: 1 to 4. The value specifies how many levels of reflection will be applied. This option has no effect for ai, eps, and svg.

-----------------------------------------

rf    : reflections     [boolean] []
    Specifies whether reflections should be rendered. This option has no effect for ai, eps, and svg.

-----------------------------------------

rl    : renderLayers    [boolean] []
    Specifies whether render layers should be rendered into separate files.

-----------------------------------------

ro    : renderOptimization [string] []
    Specifies the render optimization. Valid values are: "Safe", "Good", "Aggressive". "Safe" will remove redundant geometry. "Good" removes redundant geometry as well as sub-pixel geometry that would not be visible without zooming into the high detail area. "Agressive" removes all of the geometry that "Good" removes but will also remove geometry at slightly above the single pixel level making it possible to visibly detect the removed geometry without zooming in on the affected region.

-----------------------------------------

rv    : renderView      [boolean] []
    Specifies whether to display the rendered image to the render view. This option is not applicable when batch rendering.

-----------------------------------------

scf   : secondaryCurveFitting [boolean] []
    Specifies whether to do secondary curve fitting.

-----------------------------------------

sh    : shadows         [boolean] []
    Specifies whether shadows should be rendered. This option has no effect for ai, eps, and svg.

-----------------------------------------

sb    : showBackFaces   [boolean] []
    Specifies whether back faces will should be rendered; ie. faces whose normals are pointed away from the camera.

-----------------------------------------

sf    : startFrame      [float] []
    Specifies the start frame.

-----------------------------------------

sa    : svgAnimation    [string] []
    Specifies the SVG animation type. Valid values are: "Native", "HTMLScript". This option is SVG only.

-----------------------------------------

sc    : svgCompression  [boolean] []
    Specifies whether the SVG output should be compressed. This option is svg only.

-----------------------------------------

w     : width           [int]
    Specifies the width of the output image in pixels.

    """

def camera(q=1,e=1,ar="float",cs="float",coi="linear",cp=1,dof=1,dfc=1,dfg=1,dfo=1,dfp=1,dgm=1,dr=1,dsa=1,dst=1,fs="float",fcp="linear",ffd="linear",ff="string",ffo="float",fro="string",frv="angle",fth="float",ftv="float",fl="float",fd="linear",hc="string",hfv="angle",hfa="float",hfo="float",hpn="float",hrp="float",hs="float",jc=1,lsr="float",lt=1,mb=1,n="string",ncp="linear",nfd="linear",o=1,ow="linear",ovr="float",pze=1,p="[linear, linear, linear]",pts="float",prs="float",rpz=1,rot="[angle, angle, angle]",se=1,so="float",soe=1,sa="angle",sc=1,hit="float",she=1,vfv="angle",vfa="float",vfo="float",vl=1,vpn="float",vrp="float",vs="float",wci="[linear, linear, linear]",wup="[linear, linear, linear]",zom="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/camera.html



-----------------------------------------

camera is undoable, queryable, and editable.

Create, edit, or query a camera with the specified properties.

The resulting camera can be repositioned using the viewPlace command. Many of
the camera settings only affect the resulting rendered image. E.g. the F/Stop,
shutter speed, the film related options, etc. Scaling the camera icon does not
change any camera properties.


-----------------------------------------


Return Value:

string[]  (transform name and shape name)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ar    : aspectRatio     [float] ['query', 'edit']
    The ratio of the film back width to the film back height.

-----------------------------------------

cs    : cameraScale     [float] ['query', 'edit']
    Scale the camera.

-----------------------------------------

coi   : centerOfInterest [linear] ['query', 'edit']
    Set the linear distance from the camera's eye point to the center of interest.

-----------------------------------------

cp    : clippingPlanes  [boolean] ['query', 'edit']
    Activate manual clipping planes.

-----------------------------------------

dof   : depthOfField    [boolean] ['query', 'edit']
    Determines whether a depth of field calculation is performed to give varying focus depending on the distance of the objects.

-----------------------------------------

dfc   : displayFieldChart [boolean] ['query', 'edit']
    Activate display of the video field chart when looking through the camera.

-----------------------------------------

dfg   : displayFilmGate [boolean] ['query', 'edit']
    Activate display of the film gate icons when looking through the camera.

-----------------------------------------

dfo   : displayFilmOrigin [boolean] ['query', 'edit']
    Activate the display of the film origin guide when looking through the camera.

-----------------------------------------

dfp   : displayFilmPivot [boolean] ['query', 'edit']
    Activate display of the film pivot guide when looking through the camera.

-----------------------------------------

dgm   : displayGateMask [boolean] ['query', 'edit']
    Display the gate mask, file or resolution, as a shaded area to the edge of the viewport.

-----------------------------------------

dr    : displayResolution [boolean] ['query', 'edit']
    Activate display of the current rendering resolution (as defined in the render globals) when looking through the camera.

-----------------------------------------

dsa   : displaySafeAction [boolean] ['query', 'edit']
    Activate display of the video Safe Action guide when looking through the camera.

-----------------------------------------

dst   : displaySafeTitle [boolean] ['query', 'edit']
    Activate display of the video Safe Title guide when looking through the camera.

-----------------------------------------

fs    : fStop           [float] ['query', 'edit']
    A real lens normally contains a diaphragm or other stop which blocks some of the light that would otherwise pass through it. This stop is usually approximately round, and its diameter as seen from the front of the lens is called the lens diameter. The lens diameter is often described by its relation to the focal length of the lens. A lens whose diameter is one-eighth its local length is said to have an F-stop of 8\. This is an optical property of the lens.

-----------------------------------------

fcp   : farClipPlane    [linear] ['query', 'edit']
    Specify the distance to the far clipping plane.

-----------------------------------------

ffd   : farFocusDistance [linear] ['query', 'edit']
    Linear distance to the far focus plane.

-----------------------------------------

ff    : filmFit         [string] ['query', 'edit']
    This describes how the digital image (in pixels) relates to the film back. Since the film back is defined in terms of real numbers with some arbitrary film aspect, and the digital image is defined in integer pixels with an equally arbitrary (and different) resolution, relating the two can get complicated. There are 4 choices:  horizontal      In this case the digital image is made to fit the film back exactly in the horizontal direction. This then gives each pixel a horizontal size = (film back width) / (horizontal resolution). The pixel height is then = (pixel width) / (pixel aspect ratio). Now that the pixel has a size, resolution gives us a complete image. That image will match the film back exactly in width. It will almost never match in height, either being too tall or too short. By playing with the numbers you can get it pretty close though. vertical      This is the same idea as horizontal fit, only applied vertically. Thus the digital image will match the film back exactly in height, but miss in width. fill      This is a convenience item. The system calculates both horizontal and vertical fits and then applies the one that makes the digital image larger than the film back. overscan      Overscanning the film gate in the camera view allows us to choreograph action outside of the frustum from within the camera view without having to resort to a dolly or zoom. This feature is also essential for animating image planes.

-----------------------------------------

ffo   : filmFitOffset   [float] ['query', 'edit']
    Since we know from the above that the digital image may not match the film back exactly, we now have the question of how to position one relative to the other. Thus fit offset. Normally the centers are aligned. Fit offset lets you move the smaller image within the larger one. Specify the distance for film offset (inches).

-----------------------------------------

fro   : filmRollOrder   [string] ['query', 'edit']
    Specifies how the roll is applied with respect to the pivot value.  Rotate-Translate      The film back is first rotated then translated by the pivot point value. Translate-Rotate      The film back is first translated then rotated by the film roll value.

-----------------------------------------

frv   : filmRollValue   [angle] ['query', 'edit']
    This specifies that amount of rotation around the film back. The roll value is specified in degrees. The rotation occurs around the specified pivot point. This value is used to compute a film roll matrix, which is a component of the post-projection matrix.

-----------------------------------------

fth   : filmTranslateH  [float] ['query', 'edit']
    The horizontal film translation. Values are normalized to the viewing area.

-----------------------------------------

ftv   : filmTranslateV  [float] ['query', 'edit']
    The vertical film translation. Values are normalized to the viewing area.

-----------------------------------------

fl    : focalLength     [float] ['query', 'edit']
    This is the distance along the lens axis between the lens and the film plane when "focal distance" is infinitely large. This is an optical property of the lens. This double precision parameter is always specified in millimeters.

-----------------------------------------

fd    : focusDistance   [linear] ['query', 'edit']
    Set the focus at a certain distance in front of the camera.

-----------------------------------------

hc    : homeCommand     [string] ['query', 'edit']
    Specify the command to execute when "viewSet -home" is applied to this camera. All occurances of "%camera" will be replaced with the cameras name before viewSet runs the command.

-----------------------------------------

hfv   : horizontalFieldOfView [angle] ['query', 'edit']
    This is the film back width as seen by the lens when focused at infinity (ie., focal length away) measured as an angle. Note that it has nothing to do with pixels or the digital image or any aspects. Angle of view is a derived field, that is, it is not used internally by Alias and can be completely determined from other information. It is included as a convenience for the user. Its derivation is aov = 2 * atan( fbw / (2 * f) ) where "aov" is the angle of view, "fbw" is the film back width and "f" is the focal length.

-----------------------------------------

hfa   : horizontalFilmAperture [float] ['query', 'edit']
    The horizontal width of the camera's film plane. The camera's film is located on the film plane. The extent of the film which will be exposed to an image of the scene in front of the lens is limited to a rectangular area described by the film back. This double precision parameter is always specified in inches.

-----------------------------------------

hfo   : horizontalFilmOffset [float] ['query', 'edit']
    Horizontal offset from the center of the film back. Normally the film back will be centered on the lens axis. However, this need not be so. Film offset is the displacement of the center of the film back from the lens axis, also measured in inches. Note that offsetting the film back will distort the image, but will not alter the focus. This double precision parameter is always specified in inches.

-----------------------------------------

hpn   : horizontalPan   [float] ['query', 'edit']
    Horizontal 2D camera pan (inches)

-----------------------------------------

hrp   : horizontalRollPivot [float] ['query', 'edit']
    The horizontal pivot point from the center of the film back. The pivot point is used during rotation of the film back. The pivot is the point where the rotation occurs around. This double precision parameter corresponds to the normalized viewport. This value is a part of the post projection matrix.

-----------------------------------------

hs    : horizontalShake [float] ['query', 'edit']
    Another horizontal offset from the center of the film back, which can be used and stored on the camera in addition to the horizonal film offset attribute. This allows for film-based camera shake internal to the camera. This works in exactly the same units and coordinates that the film offset attribute does. The effect of this attribute is toggled by the shake enabled attribute.

-----------------------------------------

jc    : journalCommand  [boolean] ['query', 'edit']
    Journal interactive camera commands. Commands can be undone when a camera is journaled.

-----------------------------------------

lsr   : lensSqueezeRatio [float] ['query', 'edit']
    This is presently just an information field in the camera editor is meant to convey the horizontal distortion of the anamorphic lens normally used with some film formats. If it were used, it would do something like pixel aspect. Remember however that lens distortion (intentional or not) is slightly different than the output hardware's quantization. The fact that a "net" distortion parameter could be used for both may or may not confuse the issue.

-----------------------------------------

lt    : lockTransform   [boolean] ['query', 'edit']
    Lock the camera. When a camera is locked, its transformation information, that is, its Translate and Rotate properties cannot be adjusted, and the center of interest point cannot be moved. For orthographic cameras, Orthographic Width is also locked. For camera groups, Aim and Up locator's translate is also locked. For stereo cameras, the root camera is locked.

-----------------------------------------

mb    : motionBlur      [boolean] ['query', 'edit']
    Determines whether the camera's image is motion blured (as opposed to an object's image). For example, if you want to blur the camera movement when you are performing a flyby.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name of the camera.

-----------------------------------------

ncp   : nearClipPlane   [linear] ['query', 'edit']
    Specify the distance to the NEAR clipping plane.

-----------------------------------------

nfd   : nearFocusDistance [linear] ['query', 'edit']
    Linear distance to the near focus plane.

-----------------------------------------

o     : orthographic    [boolean] ['query', 'edit']
    Activate the orthographic camera.

-----------------------------------------

ow    : orthographicWidth [linear] ['query', 'edit']
    Set the orthographic projection width.

-----------------------------------------

ovr   : overscan        [float] ['query', 'edit']
    Set the percent of overscan.

-----------------------------------------

pze   : panZoomEnabled  [boolean] ['query', 'edit']
    Toggle camera 2D pan and zoom

-----------------------------------------

p     : position        [[linear, linear, linear]] ['query', 'edit']
    Three linear values can be specified to translate the camera.

-----------------------------------------

pts   : postScale       [float] ['query', 'edit']
    The post-scale value. This value multiplied against the computed projection matrix. It is applied after the the film roll.

-----------------------------------------

prs   : preScale        [float] ['query', 'edit']
    The pre-scale value. The value is multiplied against the computed projection matrix. It is applied before the film roll.

-----------------------------------------

rpz   : renderPanZoom   [boolean] ['query', 'edit']
    Toggle camera 2D pan and zoom in render

-----------------------------------------

rot   : rotation        [[angle, angle, angle]] ['query', 'edit']
    Three angular values can be specified to rotate the camera.

-----------------------------------------

se    : shakeEnabled    [boolean] ['query', 'edit']
    Toggles the effect of the horizontal and vertical shake attributes.

-----------------------------------------

so    : shakeOverscan   [float] ['query', 'edit']
    Controls the amount of overscan in the output rendered image. For use when adding film-based camera shake. Acts as a multiplier to the film aperture on the camera.

-----------------------------------------

soe   : shakeOverscanEnabled [boolean] ['query', 'edit']
    Toggles the effect of the shake overscan attribute.

-----------------------------------------

sa    : shutterAngle    [angle] ['query', 'edit']
    Specify the shutter angle (degrees).

-----------------------------------------

sc    : startupCamera   [boolean] ['query', 'edit']
    A startup camera is marked undeletable and implicit. This flag can be used to set or query the startup state of a camera. There must always be at least one startup camera.

-----------------------------------------

hit   : stereoHorizontalImageTranslate [float] ['query', 'edit']
    A film-back offset for use in stereo camera rigs.

-----------------------------------------

she   : stereoHorizontalImageTranslateEnabled [boolean] ['query', 'edit']
    Toggles the effect of the stereo HIT attribute.

-----------------------------------------

vfv   : verticalFieldOfView [angle] ['query', 'edit']
    Set the vertical field of view.

-----------------------------------------

vfa   : verticalFilmAperture [float] ['query', 'edit']
    The vertical height of the camera's film plane. This double precision parameter is always specified in inches.

-----------------------------------------

vfo   : verticalFilmOffset [float] ['query', 'edit']
    Vertical offset from the center of the film back. This double precision parameter is always specified in inches.

-----------------------------------------

vl    : verticalLock    [boolean] ['query', 'edit']
    Lock the size of the vertical film aperture.

-----------------------------------------

vpn   : verticalPan     [float] ['query', 'edit']
    Vertical 2D camera pan (inches)

-----------------------------------------

vrp   : verticalRollPivot [float] ['query', 'edit']
    Vertical pivot point used for rotating the film back. This double precision parameter corresponds to the normalized viewport. This value is used to compute the film roll matrix, which is a component of the post projection matrix.

-----------------------------------------

vs    : verticalShake   [float] ['query', 'edit']
    Vertical offset from the center of the film back. See horizontal shake attribute description. This is toggled by the shake enabled attribute.

-----------------------------------------

wci   : worldCenterOfInterest [[linear, linear, linear]] ['query', 'edit']
    Camera world center of interest point.

-----------------------------------------

wup   : worldUp         [[linear, linear, linear]] ['query', 'edit']
    Camera world up vector.

-----------------------------------------

zom   : zoom            [float]
    The percent over the film viewable frustum to display

    """

def cameraSet(q=1,e=1,a=1,atl=1,cam="string",cd=1,da=1,d=1,ins=1,l="int",n="string",nl=1,os="string",o="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cameraSet.html



-----------------------------------------

cameraSet is undoable, queryable, and editable.

This command manages camera set nodes. Camera sets allow the users to break a
single camera shot into layers. Instead of drawing all objects with a single
camera, you can isolate the camera to only focus on certain objects and layer
another camera into the viewport that draws the other objects. The situation
to use camera sets primarily occurs when building stereoscopic scenes.

For example, a set of stereo parameters may make the background objects
divergent beyond the tolerable range of the human perceptual system. However,
you like the settings because the main focus is in the foreground and the
depth is important to the visual look of the scene. You can use camera sets to
break apart the shot into a foreground stereo camera and background stereo
camera. The foreground stereo camera will retain the original parameters;
however, it will only focus on the foreground elements. The background stereo
camera will have a different set of stereo parameters and will only draw the
background element.

Camera sets can be viewed using the stereo viewer and are currently only
designed to work with stereo camera rigs.


-----------------------------------------


Return Value:

string  The new cameraSet node (when in create mode)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : active          [boolean] ['query', 'edit']
    Gets / sets the active camera layer.

-----------------------------------------

atl   : appendTo        [boolean] ['edit']
    Append a new camera and/or object set to then end of the cameraSet layer list. This flag cannot be used in conjunction with insert flag. Additionally, it requires the camera and/or objectSet flag to be used.

-----------------------------------------

cam   : camera          [string] ['query', 'edit']
    Set/get the camera for a particular layer. When in query mode, You must specify the layer with the layer flag.

-----------------------------------------

cd    : clearDepth      [boolean] ['query', 'edit']
    Specifies if the drawing buffer should be cleared before beginning the draw for that layer.

-----------------------------------------

da    : deleteAll       [boolean] ['edit']
    Delete all camera layers

-----------------------------------------

d     : deleteLayer     [boolean] ['edit']
    Delete a layer from the camera set. You must specify the layer using the layer flag.

-----------------------------------------

ins   : insertAt        [boolean] ['edit']
    Inserts the specified camera and/or object set at the specified layer. This flag cannot be used in conjunction with the append flag. Additionally, this flag requires layer and camera (or objectSet) flag to be used.

-----------------------------------------

l     : layer           [int] ['query', 'edit']
    Specifies the layer index to be used when accessing layer information

-----------------------------------------

n     : name            [string] ['query']
    Gets or sets the name for the created camera set.

-----------------------------------------

nl    : numLayers       [boolean] ['query']
    Returns the number of layers defined in the specified cameraSet

-----------------------------------------

os    : objectSet       [string] ['query', 'edit']
    Set/get the objectSet for a particular layer. When in query mode, you must specify the layer with the layer flag.

-----------------------------------------

o     : order           [int]
    Set the order in which a particular layer is processed. This flag must be used in conjunction with the layer flag.

    """

def cameraView(e=1,ab=1,an=1,typ="int",c="name",n="string",rb=1,sc=1,sv=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cameraView.html



-----------------------------------------

cameraView is undoable, NOT queryable, and editable.

This command creates a preset view for a camera which is then independent of
the camera. The view stores a camera's eye point, center of interest point, up
vector, tumble pivot, horizontal aperture, vertical aperature, focal length,
orthographic width, and whether the camera is orthographic or perspective by
default. Or you can only store 2D pan/zoom attributes by setting the
bookmarkType to 1. These settings can be applied to any other camera through
the set camera flag.

This command can be used for creation or edit of camera view objects. This
command can only be executed with one of the add bookmark, or remove bookmark
and one of set camera, or the set view flags set.


-----------------------------------------


Return Value:

string  (name of the camera view)


-----------------------------------------


Flags:

-----------------------------------------

ab    : addBookmark     [boolean] ['edit']
    Associate this view with the camera specified or the camera in the active model panel. This flag can be used for creation or edit.

-----------------------------------------

an    : animate         [boolean] ['edit']
    Set the animation capability for view switches.

-----------------------------------------

typ   : bookmarkType    [int] []
    Specify the bookmark type, which can be: 0. 3D bookmark; 1. 2D Pan/Zoom bookmark.

-----------------------------------------

c     : camera          [name] ['edit']
    Specify the camera to use. This flag should be used in conjunction with the add bookmark, remove bookmark, set camera, or set view flags. If this flag is not specified the camera in the active model panel will be used.

-----------------------------------------

n     : name            [string] []
    Set the name of the view. This flag can only be used for creation.

-----------------------------------------

rb    : removeBookmark  [boolean] ['edit']
    Remove the association of this view with the camera specified or the camera in the active model panel. This can only be used with edit.

-----------------------------------------

sc    : setCamera       [boolean] ['edit']
    Set this view into a camera specified by the camera flag or the camera in the active model panel. This flag can only be used with edit.

-----------------------------------------

sv    : setView         [boolean]
    Set the camera view to match a camera specified or the active model panel. This flag can only be used with edit.

    """

def dolly(abs=1,d="linear",dtc=1,os="float",rel=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dolly.html



-----------------------------------------

dolly is undoable, NOT queryable, and NOT editable.

The dolly command moves a camera along the viewing direction in the world
space. The viewing-direction and up-direction of the camera are not altered.
There are two modes of operation:

Relative mode: for a perspective camera, the camera is moved along its viewing
direction, and the distance of travel is computed with respect to the current
position of the camera in the world space. In relative mode, when the camera
is moved, its COI is moved along with it, and is kept at the same distance, in
front of the camera, as before applying the dolly operation. For orthographic
camera, the viewing width of the camera is changed by scaling its ortho width
by the new value specified on the command line.

Absolute mode: for a perspective camera, the camera is moved along its viewing
direction, to the distance that is computed with respect to the current
position of the world center of interest (COI) of the camera. In the absolute
mode, when the camera is moved, the COI of the camera is not moved with the
camera, but it is fixed at its current location in space. For orthographic
camera, the viewing width of the camera is changed by replacing its ortho
width with the new value specified on the command line. This command may be
applied to more than one cameras; objects that are not cameras are ignored.
When no camera name supplied on the command line, this command is applied to
all currently active cameras.

The dolly command can be applied to either a perspective or an orthographic
camera.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

abs   : absolute        [boolean] []
    This flag modifies the behavior of the distance and orthoScale flags. When used in conjunction with the distance flag, the distance argument specifies how far the camera's eye point should be set from the camera's center of interest. When used with the orthoScale flag, the orthoScale argument specifies the camera's new ortho width.

-----------------------------------------

d     : distance        [linear] []
    Unit distance to dolly a perspective camera.

-----------------------------------------

dtc   : dollyTowardsCenter [boolean] []
    This flag controls whether the dolly is performed towards the center of the view (if true), or towards the point where the user clicks (if false). By default, dollyTowardsCenter is on.

-----------------------------------------

os    : orthoScale      [float] []
    Scale to change the ortho width of an orthographic camera.

-----------------------------------------

rel   : relative        [boolean]
    This flag modifies the behavior of the distance and orthoScale flags. When used in conjunction with the distance flag, the camera eye and center of interest are both moved by the amount specified by the distance flag's argument. When used with the orthoScale flag, the orthoScale argument is used multiply the camera's ortho width.By default the relative flag is always on.

    """

def imagePlane(q=1,e=1,c="string",cn=1,d=1,df=1,fn="string",fd="int",h="float",iz="[int, int]",lt="string",mr=1,n="string",nt=1,nf="int",qt=1,sia=1,tc="int",tt=1,ts="int",tf=1,w="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/imagePlane.html



-----------------------------------------

imagePlane is undoable, queryable, and editable.

The imagePlane command allows querying of various properties of an image plane
and any movie in use by the image plane. It also supports creating and edit.
The object passed to the command may either be an imagePlane node, or a
camera, in which case the command uses the image plane attached to the camera
(if any). If no object is passed in, the current selection is used. Currently,
most movie related queries work only on 64 bit Windows systems.


-----------------------------------------


Return Value:

boolean  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : camera          [string] ['query', 'edit']
    When creating, it will try to attach the created image plane to the specified camera. If the given camera is invalid, creating will fail. When querying, it will query which camera current image plane is attaching to. If it has no camera attached to (free image plane), it will return an empty string. When edit, it will make the image plane attach to the new specified camera. If the camera given is invalid, it will do nothing. When the image plane is attached to a camera, the image plane's transform node will be set identity. The detach command will not restore the original position of the image plane. but the undo command will restore the original position of the image plane.

-----------------------------------------

cn    : counter         [boolean] []
    Query the 'counter' flag of the movie's timecode format. If this is true, the timecode returned by the -timeCode flag will be a simple counter. If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).

-----------------------------------------

d     : detach          [boolean] ['edit']
    This flag can only be used in the edit mode, when this flag is used in edit, it will detach current image plane from any camera it attaches to and make it a free image plane.

-----------------------------------------

df    : dropFrame       [boolean] ['query']
    Query the 'drop frame' flag of the movie's timecode format.

-----------------------------------------

fn    : fileName        [string] ['edit']
    Set the image name for image plane to read.

-----------------------------------------

fd    : frameDuration   [int] ['query']
    Query the frame duration of the movie's timecode format.

-----------------------------------------

h     : height          [float] ['query', 'edit']
    Height of the image plane. When creating, if this flag is not specified, it will use 10.0 as default height.

-----------------------------------------

iz    : imageSize       [[int, int]] ['query']
    Get size of the loaded image.

-----------------------------------------

lt    : lookThrough     [string] ['query', 'edit']
    The camera currently used for image plane to look through.

-----------------------------------------

mr    : maintainRatio   [boolean] ['query', 'edit']
    Let the image plane respect the picture aspect ratio. When creating, if this flag is not specified, it will use true as default value.

-----------------------------------------

n     : name            [string] ['query']
    Set the image plane node name when creating or return the image plane name when querying.

-----------------------------------------

nt    : negTimesOK      [boolean] ['query']
    Query the 'neg times OK' flag of the movie's timecode format.

-----------------------------------------

nf    : numFrames       [int] ['query']
    Query the whole number of frames per second of the movie's timecode format.

-----------------------------------------

qt    : quickTime       [boolean] ['query']
    Query whether the image plane is using a QuickTime movie.

-----------------------------------------

sia   : showInAllViews  [boolean] ['query', 'edit']
    The flag is used to show the current image plane in all views or not.

-----------------------------------------

tc    : timeCode        [int] ['query']
    Query the whole number of frames per second of the movie's timecode format.

-----------------------------------------

tt    : timeCodeTrack   [boolean] ['query']
    Query whether the movie on the image plane has a timecode track.

-----------------------------------------

ts    : timeScale       [int] ['query']
    Query the timescale of the movie's timecode format.

-----------------------------------------

tf    : twentyFourHourMax [boolean] ['query']
    Query the '24 hour max' flag of the movie's timecode format.

-----------------------------------------

w     : width           [float]
    Width of the image plane. When creating, if this flag is not specified, it will use 10.0 as default width.

    """

def listCameras(o=1,p=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/listCameras.html



-----------------------------------------

listCameras is undoable, NOT queryable, and NOT editable.

Command to list all cameras. If no flags are given, both perspective and
orthographic cameras will be displayed. This command returns an array of
camera names. When the transform name uniquely identifies the camera it is
used, otherwise the shape name will be returned.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

o     : orthographic    [boolean] []
    Display all orthographic cameras.

-----------------------------------------

p     : perspective     [boolean]
    Display all perspective cameras.

    """

def lookThru(q=1,fc="float",nc="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lookThru.html



-----------------------------------------

lookThru is NOT undoable, queryable, and NOT editable.

This command sets a particular camera to look through in a view. This command
may also be used to view the negative z axis of lights or other DAG objects.
The standard camera tools can then be used to place the object.

Note: if there are multiple objects under the transform selected, cameras and
lights take precedence.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

fc    : farClip         [float] []
    Used when setting clip far plane for a new look thru camera. Will not affect the attributes of an existing camera. Clip values must come before shape or view.

-----------------------------------------

nc    : nearClip        [float]
    Used when setting near clip plane for a new look thru camera. Will not affect the attributes of an existing camera. Clip values must come before shape or view.

    """

def orbit(ha="angle",pp="[linear, linear, linear]",ra="[angle, angle]",va="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/orbit.html



-----------------------------------------

orbit is undoable, NOT queryable, and NOT editable.

The orbit command revolves the camera(s) horizontally and/or vertically in the
perspective window. The rotation axis is with respect to the camera.

To revolve horizontally: the rotation axis is the camera up direction vector.
To revolve vertically: the rotation axis is the camera left direction vector.

When both the horizontal and the vertical angles are supplied on the command
line, the camera is firstly revolved horizontally, then revolved vertically.

This command may be applied to more than one camera; objects that are not
cameras are ignored. When no camera name supplied, this command is applied to
all currently active cameras.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

ha    : horizontalAngle [angle] []
    Angle to revolve horizontally.

-----------------------------------------

pp    : pivotPoint      [[linear, linear, linear]] []
    Used as the pivot point in the world space.

-----------------------------------------

ra    : rotationAngles  [[angle, angle]] []
    Angle to revolve horizontally and vertically.

-----------------------------------------

va    : verticalAngle   [angle]
    Angle to revolve vertically.

    """

def panZoom(abs=1,d="float",l="float",rel=1,r="float",u="float",z="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/panZoom.html



-----------------------------------------

panZoom is undoable, NOT queryable, and NOT editable.

The panZoom command pans/zooms the 2D film.

The panZoom command can be applied to either a perspective or an orthographic
camera.

When no camera name is supplied, this command is applied to the camera in the
active view.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

abs   : absolute        [boolean] []
    This flag modifies the behavior of the distance and zoomRatio flags. If specified, the distance and zoomRatio value will be applied directly.

-----------------------------------------

d     : downDistance    [float] []
    Set the amount of down pan distance in inches

-----------------------------------------

l     : leftDistance    [float] []
    Set the amount of left pan distance in inches

-----------------------------------------

rel   : relative        [boolean] []
    This flag modifies the behavior of the distance and zoomRatio flags. If specified, the distance or zoomRatio value is used multiply the camera's existing value. By default the relative flag is always on.

-----------------------------------------

r     : rightDistance   [float] []
    Set the amount of right pan distance in inches

-----------------------------------------

u     : upDistance      [float] []
    Set the amount of up pan distance in inches

-----------------------------------------

z     : zoomRatio       [float]
    Set the amount of zoom ratio

    """

def perCameraVisibility(q=1,c="name",ex=1,hi=1,rm=1,ra=1,rc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/perCameraVisibility.html



-----------------------------------------

perCameraVisibility is NOT undoable, queryable, and NOT editable.

The perCameraVisibility command creates, queries and removes visibility
relationships between DAG objects and cameras. These relationships are applied
in any viewport that uses the cameras involved. (They are not used e.g. in
rendering.) Objects can be set to be exclusive to a camera (meaning they will
only be displayed in viewports using that camera; they will be hidden in other
viewports) or hidden from a camera (meaning they will be not visible in any
viewport using the camera).


-----------------------------------------


Return Value:

string[]  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : camera          [name] ['query']
    Specify the camera for the operation.

-----------------------------------------

ex    : exclusive       [boolean] ['query']
    Set objects as being exclusive to the given camera.

-----------------------------------------

hi    : hide            [boolean] ['query']
    Set objects as being hidden from the given camera.

-----------------------------------------

rm    : remove          [boolean] []
    Used with exclusive or hide, removes the objects instead of adding them.

-----------------------------------------

ra    : removeAll       [boolean] []
    Remove all exclusivity/hidden objects for all cameras.

-----------------------------------------

rc    : removeCamera    [boolean]
    Remove all exclusivity/hidden objects for the given camera.

    """

def roll(abs=1,d="angle",rel=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/roll.html



-----------------------------------------

roll is undoable, NOT queryable, and NOT editable.

The roll command rotates a camera about its viewing direction, a positive
angle produces clockwise camera rotation, while a negative angle produces
counter-clockwise camera rotation.

The default mode is relative and the rotation is applied with respect to the
current orientation of the camera. When mode is set to absolute, the rotation
is applied with respect to the plane constructed from the following three
vectors in the world space: the world up vector, the camera view vector, and
the camera up vector.

The rotation angle is specified in degrees.

The roll command can be applied to either a perspective or an orthographic
camera.

This command may be applied to more than one camera; objects that are not
cameras are ignored. When no camera name supplied, this command is applied to
all currently active cameras.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

abs   : absolute        [boolean] []
    Set to absolute mode.

-----------------------------------------

d     : degree          [angle] []
    Set the amount of the rotation angle.

-----------------------------------------

rel   : relative        [boolean]
    Set to relative mode.

    """

def stereoCameraView(q=1,e=1,acx=1,ace="string",acg="string",acl="string",aog="string",acr="string",ao=1,asg="string",ams=1,av=1,aob="string",addSelected=1,alo=1,bfc=1,bm="string",brz="[uint, uint]",cam="string",cn="string",cst="string",cs=1,ca=1,cpt="string",csn="int",ccm="string",cm=1,crz="[uint, uint]",ctl=1,cv=1,cov="string",d=1,dt="string",df=1,dim=1,da="string",dl="string",dm="string",dtx=1,dtg="string",dc=1,dy=1,ec="script",ex=1,f="string",fol=1,fl=1,fcl="[float, float, float, float]",fdn="float",fen="float",fmd="string",fsc="string",fst="float",fg=1,fo=1,fmc="string",gr=1,hs=1,ha=1,hud=1,h=1,hlc="string",hu=1,ipz=1,ikh=1,imp=1,i=1,ibc=1,dis=1,isFiltered=1,jx=1,j=1,lcm="string",lt=1,lw="float",lc=1,lck=1,lql=1,mlc="string",m=1,mct="float",mhl=1,mp="string",mt=1,ncl=1,npa=1,nr=1,nud=1,nc=1,ns=1,obf="script",ofl="script",ofu="script",ofs=1,obu="script",ocl=1,pnl="string",p="string",pv=1,pl=1,po="[string, boolean]",ps=1,pm=1,qpo="string",rs=1,rdn=1,rls=1,rlu=1,rnm="string",rol=1,rou=1,rom="string",rcc=1,rr="string",rcm="string",srf="string",slc="string",sel=1,ss=1,sml="int",sdw=1,soc=1,sot="float",swf=1,st=1,sts=1,sdm=1,str=1,sds=1,se=1,ta=1,tcp=1,td="string",tem=1,th=1,tms="int",tmu=1,ts="int",tx=1,tis=1,tal="string",tsl=1,up=1,ulk=1,ucm=1,upd=1,ubr=1,uci=1,ucb=1,udm=1,ui=1,ip=1,urr=1,ut="string",un="string",vc="[float, float, float, float]",vo=1,vs=1,vt=1,w=1,wbs=1,wos=1,xr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/stereoCameraView.html



-----------------------------------------

stereoCameraView is undoable, queryable, and editable.

Create, edit or query a model editor.

Note that some of the flags of this command may have different settings for
normal mode and for interactive/playback mode. For example, a modelEditor can
be set to use shaded mode normally, but to use wireframe during playback for
greater speed. Some flags also support having defaults set so that new model
editors will be created with those settings.

This is the main command for creating stereo editors. This commands only acts
as an interface to the actual viewport. It is derived off of
MPxModelEditorCommand. This command manages the set of stereo rig tools.


-----------------------------------------


Return Value:

string  the name of the editor.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

acx   : activeComponentsXray [boolean] ['query', 'edit']
    Turns on or off Xray mode for active components.

-----------------------------------------

ace   : activeCustomEnvironment [string] ['edit']
    Specifies a path to an image file to be used as environment map. It is only enabled when a valid scene render filter is specified.

-----------------------------------------

acg   : activeCustomGeometry [string] ['query', 'edit']
    Specifies an identifier for custom geometry to override the geometry to display. It is only enabled when a valid scene render filter is specified.

-----------------------------------------

acl   : activeCustomLighSet [string] ['query', 'edit']
    Specifies an identifier for the light set to use with a scene render filter. It is only enabled when a valid scene render filter is specified.

-----------------------------------------

aog   : activeCustomOverrideGeometry [string] ['query', 'edit']
    Specifies an identifier for an override on the custom geometry for a scene render filter.

-----------------------------------------

acr   : activeCustomRenderer [string] ['query', 'edit']
    Specifies an identifier for custom renderer to use when a valid scene render filter is also specified.

-----------------------------------------

ao    : activeOnly      [boolean] ['query', 'edit']
    Sets whether only active objects should appear shaded in shaded display.

-----------------------------------------

asg   : activeShadingGraph [string] ['query', 'edit']
    Specifies the shading graph to use to override material display. Only enabled when a valid scene render filter is specified.

-----------------------------------------

ams   : activeSupported [boolean] ['query']
    True if the viewer is capable of drawing in active mode which takes advantage of the graphics card's built-in stereoscopic support. This includes support for shutter glasses and stereo support in clone mode.

-----------------------------------------

av    : activeView      [boolean] ['query', 'edit']
    Sets this model editor to be the active view. Returns true if successful. On query this flag will return whether the view is the active view.

-----------------------------------------

aob   : addObjects      [string] ['edit']
    This flag causes the objects contained within the selection connection to be added to the list of objects visible in the view (if viewSelected is true).

-----------------------------------------

addSelected : addSelected     [boolean] ['edit']
    This flag causes the currently active objects to be added to the list of objects visible in the view (if viewSelected is true).

-----------------------------------------

alo   : allObjects      [boolean] ['query', 'edit']
    Turn on/off the display of all objects for the view of the model editor. This excludes NURBS, CVs, hulls, grids and manipulators.

-----------------------------------------

bfc   : backfaceCulling [boolean] ['query', 'edit']
    Turns on or off backface culling for the whole view. This setting overrides the culling settings of individual objects. All objects draw in the view will be backface culled. When backface culling is turned on, surfaces becomes invisible in areas where the normal is pointing away from the camera.

-----------------------------------------

bm    : bufferMode      [string] ['query', 'edit']
    Deprecated: this is not supported in Viewport 2.0. Sets the graphic buffer mode. Possible values are "single" or "double".

-----------------------------------------

brz   : bumpResolution  [[uint, uint]] ['query', 'edit']
    Set the resolution for "baked" bump map textures when using the hardware renderer. The default value is 512, 512 respectively.

-----------------------------------------

cam   : camera          [string] ['query', 'edit']
    Change or query the name of the camera in model editor.

-----------------------------------------

cn    : cameraName      [string] ['edit']
    Set the name of the panel's camera transform and shape. The shape name is computed by appending the string "Shape" to the transform name. This flag may not be queried.

-----------------------------------------

cst   : cameraSet       [string] ['query', 'edit']
    Name of the camera set

-----------------------------------------

cs    : cameraSetup     [boolean] ['query']
    Based on the model editor name passed in will returns a string list containing camera setups. A camera setup can contain one or more cameras which are associated with each other. Camera setups are defined as pairs of consecutive strings in the list. Each pair is comprised of: a string which identifies an active camera, and a string which defines a script to set up a given active camera. As many pairs of strings can be returned as the number of active cameras. If nothing is returned then it is assumed that no set up is required to activate a given camera.

-----------------------------------------

ca    : cameras         [boolean] ['query', 'edit']
    Turn on/off the display of cameras for the view of the model editor.

-----------------------------------------

cpt   : capture         [string] ['query', 'edit']
    Perform an one-time capture of the viewport to the named image file on disk.

-----------------------------------------

csn   : captureSequenceNumber [int] ['query', 'edit']
    When a number greater or equal to 0 is specified each subsequent refresh will save an image file to disk if the capture flag has been enabled. The naming of the file is: {root name}.#.{extension} if the name {root name}.{extension} is used for the capture flag argument. The value of # starts at the number specified to for this argument and increments for each subsequent refresh. Sequence capture can be disabled by specifying a number less than 0 or an empty file name for the capture flag.

-----------------------------------------

ccm   : centerCamera    [string] ['query']
    Only available in query mode: returns the current center camera of this view.

-----------------------------------------

cm    : colorMap        [boolean] ['query']
    Queries the color map style for the model panel. Possible values are "colorIndex" and "rgb".

-----------------------------------------

crz   : colorResolution [[uint, uint]] ['query', 'edit']
    Set the resolution for "baked" color textures when using the hardware renderer. The default value is 256, 256 respectively.

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

cv    : controlVertices [boolean] ['query', 'edit']
    Turn on/off the display of NURBS CVs for the view of the model editor.

-----------------------------------------

cov   : cullingOverride [string] ['query', 'edit']
    Set whether to override the culling attributes on objects when using the hardware renderer. The options are:    * "none" : Use the culling object attributes per object.   * "doubleSided" : Force all objects to be double sided.   * "singleSided": Force all objects to be single sided.  The default value is "none".

-----------------------------------------

d     : default         [boolean] ['query', 'edit']
    Causes this command to modify the default value of this setting. Newly created model editors will inherit the values. This flag may be used with the -interactive to set default interactive settings.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

df    : deformers       [boolean] ['query', 'edit']
    Turn on/off the display of deformer objects for the view of the model editor.

-----------------------------------------

dim   : dimensions      [boolean] ['query', 'edit']
    Turn on/off the display of dimension objects for the view of the model editor.

-----------------------------------------

da    : displayAppearance [string] ['query', 'edit']
    Sets the display appearance of the model panel. Possible values are "wireframe", "points", "boundingBox", "smoothShaded", "flatShaded". This flag may be used with the -interactive and -default flags. Note that only "wireframe", "points", and "boundingBox" are valid for the interactive mode.

-----------------------------------------

dl    : displayLights   [string] ['query', 'edit']
    Sets the lighting for shaded mode. Possible values are "selected", "active", "all", "default", "none".

-----------------------------------------

dm    : displayMode     [string] ['query', 'edit']
    Defines the display mode for this view. Some modes are available only for certain types of graphics hardware. Valid values are:    * active: uses the graphics card's built-in stereoscopic mode is available   * leftEye: displays only the view from the left camera.   * rightEye: displays only the view from the rigth camera.   * centerEye: displays only the view from the center camera.   * anaglyph: displays both left and right cameras, filtered using red and blue   * anaglyphLum: same as anaglyph, except the luminance is computed before the red and blue filtering   * interlace: displays an interlaced view of left and right cameras   * checkerboard: Same as interlace, except a checkerboard pattern is used to mix both images   * freeview: displays both left and right images, half size next to each other   * freeviewX: same as freeview, except left and right cameras are swapped

-----------------------------------------

dtx   : displayTextures [boolean] ['query', 'edit']
    Turns on or off display of textures in shaded mode

-----------------------------------------

dtg   : docTag          [string] ['query', 'edit']
    Attaches a tag to the editor.

-----------------------------------------

dc    : dynamicConstraints [boolean] ['query', 'edit']
    Turn on/off the display of dynamicConstraints for the view of the model editor.

-----------------------------------------

dy    : dynamics        [boolean] ['query', 'edit']
    Turn on/off the display of dynamics objects for the view of the model editor.

-----------------------------------------

ec    : editorChanged   [script] ['query', 'edit']
    An optional script callback which is called when the editors options have changed. This is useful in a situation where a scripted panel contains a modelEditor and wants to be notified when the contained editor changes its options.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

f     : filter          [string] ['query', 'edit']
    Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.

-----------------------------------------

fol   : filteredObjectList [boolean] ['query']
    For model editors with filtering on (either using an object filter, or isolate select), this flag returns a string list of the objects which are displayed in this editor. Note that this list does not take into account visibility (based on camera frustum or flags), it purely captures the objects which are considered when rendering the view.

-----------------------------------------

fl    : fluids          [boolean] ['query', 'edit']
    Turn on/off the display of fluids for the view of the model editor.

-----------------------------------------

fcl   : fogColor        [[float, float, float, float]] ['query', 'edit']
    The color used for hardware fogging.

-----------------------------------------

fdn   : fogDensity      [float] ['query', 'edit']
    Determines the density of hardware fogging.

-----------------------------------------

fen   : fogEnd          [float] ['query', 'edit']
    The end location of hardware fogging.

-----------------------------------------

fmd   : fogMode         [string] ['query', 'edit']
    This determines the drop-off mode for fog. The possibilities are:    * "linear" : linear drop-off   * "exponent" : exponential drop-off   * "exponent2" : squared exponential drop-off

-----------------------------------------

fsc   : fogSource       [string] ['query', 'edit']
    Set the type of fog algorithm to use. If the argument is "fragment" (default) then fog is computed per pixel. If the argument is "coordinate" then if the geometry has specified vertex fog coordinates, and the OpenGL extension for vertex fog is supported by the graphics system, then fog is computed per vertex.

-----------------------------------------

fst   : fogStart        [float] ['query', 'edit']
    The start location of hardware fogging.

-----------------------------------------

fg    : fogging         [boolean] ['query', 'edit']
    Set whether hardware fogging is enabled or not.

-----------------------------------------

fo    : follicles       [boolean] ['query', 'edit']
    Turn on/off the display of follicles for the view of the model editor.

-----------------------------------------

fmc   : forceMainConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.

-----------------------------------------

gr    : grid            [boolean] ['query', 'edit']
    Turn on/off the display of the grid for the view of the model editor.

-----------------------------------------

hs    : hairSystems     [boolean] ['query', 'edit']
    Turn on/off the display of hairSystems for the view of the model editor.

-----------------------------------------

ha    : handles         [boolean] ['query', 'edit']
    Turn on/off the display of select handles for the view of the model editor.

-----------------------------------------

hud   : headsUpDisplay  [boolean] ['query', 'edit']
    Sets whether the model panel will draw any enabled heads up display elements in this window (if true). Currently this requires the HUD elements to be globally enabled.

-----------------------------------------

h     : height          [boolean] ['query']
    Return the height of the associated viewport in pixels

-----------------------------------------

hlc   : highlightConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.

-----------------------------------------

hu    : hulls           [boolean] ['query', 'edit']
    Turn on/off the display of NURBS hulls for the view of the model editor.

-----------------------------------------

ipz   : ignorePanZoom   [boolean] ['query', 'edit']
    Sets whether the model panel will ignore the 2D pan/zoom value to give an overview of the scene.

-----------------------------------------

ikh   : ikHandles       [boolean] ['query', 'edit']
    Turn on/off the display of ik handles and end effectors for the view of the model editor.

-----------------------------------------

imp   : imagePlane      [boolean] ['query', 'edit']
    Turn on/off the display of image plane for the view

-----------------------------------------

i     : interactive     [boolean] ['query', 'edit']
    Causes this command to modify the interactive refresh settings of the view. In this way it is possible to change the behavior of the model editor during playback for improved performance.

-----------------------------------------

ibc   : interactiveBackFaceCull [boolean] ['query', 'edit']
    Define whether interactive backface culling should be on or not

-----------------------------------------

dis   : interactiveDisableShadows [boolean] ['query', 'edit']
    Define whether interactive shadows should be disabled or not

-----------------------------------------

isFiltered : isFiltered      [boolean] ['query']
    Returns true for model editors with filtering applied to their view of the scene. This could either be an explicit object filter, or a display option such as isolate select which filters the objects that are displayed.

-----------------------------------------

jx    : jointXray       [boolean] ['query', 'edit']
    Turns on or off Xray mode for joints.

-----------------------------------------

j     : joints          [boolean] ['query', 'edit']
    Turn on/off the display of joints for the view of the model editor.

-----------------------------------------

lcm   : leftCamera      [string] ['query']
    Only available in query mode: returns the current left camera of this view.

-----------------------------------------

lt    : lights          [boolean] ['query', 'edit']
    Turn on/off the display of lights for the view of the model editor.

-----------------------------------------

lw    : lineWidth       [float] ['query', 'edit']
    Set width of lines for display

-----------------------------------------

lc    : locators        [boolean] ['query', 'edit']
    Turn on/off the display of locator objects for the view of the model editor.

-----------------------------------------

lck   : lockMainConnection [boolean] ['edit']
    Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.

-----------------------------------------

lql   : lowQualityLighting [boolean] ['query', 'edit']
    Set whether to use "low quality lighting" when using the hardware renderer. The default value is false.

-----------------------------------------

mlc   : mainListConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.

-----------------------------------------

m     : manipulators    [boolean] ['query', 'edit']
    Turn on/off the display of manipulator objects for the view of the model editor.

-----------------------------------------

mct   : maxConstantTransparency [float] ['query', 'edit']
    Sets the maximum constant transparency. Setting this value remaps constant transparency values from the range [0.0, 1.0] to the range [0.0, maxConstantTransparency]. All transparency values are shifted linearly to the new range, so a fully transparency object (transparency 1.0) would appear with a transparency of maxConstantTransparency in the viewport, allowing highly transparent objects to be made visible. This flag only affects constant (non- textured) transparent objects.

-----------------------------------------

mhl   : maximumNumHardwareLights [boolean] ['query', 'edit']
    Define whether the hardware light maximum should be respected or not

-----------------------------------------

mp    : modelPanel      [string] []
    Allows the created model editor to be embedded in the named model panel. Intended for use with custom model editors created via the API (i.e. the flag would be used on the derived MPxModelEditorCommand), though the flag may also be used on the base modelEditor command to restore a default Maya model editor to the panel. Note that the model editor previously owned by the panel is deleted.

-----------------------------------------

mt    : motionTrails    [boolean] ['query', 'edit']
    Turn on/off the Motion Trail display in the Viewport.

-----------------------------------------

ncl   : nCloths         [boolean] ['query', 'edit']
    Turn on/off the display of nCloths for the view of the model editor.

-----------------------------------------

npa   : nParticles      [boolean] ['query', 'edit']
    Turn on/off the display of nParticles for the view of the model editor.

-----------------------------------------

nr    : nRigids         [boolean] ['query', 'edit']
    Turn on/off the display of nRigids for the view of the model editor.

-----------------------------------------

nud   : noUndo          [boolean] ['edit']
    This flag prevents some viewport operations (such as isolate select) from being added to the undo queue.

-----------------------------------------

nc    : nurbsCurves     [boolean] ['query', 'edit']
    Turn on/off the display of nurbs curves for the view of the model editor.

-----------------------------------------

ns    : nurbsSurfaces   [boolean] ['query', 'edit']
    Turn on/off the display of nurbs surfaces for the view of the model editor.

-----------------------------------------

obf   : objectFilter    [script] ['query', 'edit']
    Set or query the current object filter name. An object filter is required to have already been registered.

-----------------------------------------

ofl   : objectFilterList [script] ['query']
    Return a list of names of registered filters.

-----------------------------------------

ofu   : objectFilterListUI [script] ['query']
    Return a list of UI names of registered filters.

-----------------------------------------

ofs   : objectFilterShowInHUD [boolean] ['query', 'edit']
    Sets whether or not to display the object filter UI name in the heads up display when an object filter is active. This string is concatenated with the camera name.

-----------------------------------------

obu   : objectFilterUI  [script] ['query']
    Query the current object filter UI name. The object filter is required to have already been registered.

-----------------------------------------

ocl   : occlusionCulling [boolean] ['query', 'edit']
    Set whether to enable occlusion culling testing when using the hardware renderer. The default value is false.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

pv    : pivots          [boolean] ['query', 'edit']
    Turn on/off the display of transform pivots for the view of the model editor.

-----------------------------------------

pl    : planes          [boolean] ['query', 'edit']
    Turn on/off the display of sketch planes for the view of the model editor.

-----------------------------------------

po    : pluginObjects   [[string, boolean]] ['edit']
    Turn on/off the display of plug-in objects for the view. It depends on the plug-in implementation whether to respect this flag.

-----------------------------------------

ps    : pluginShapes    [boolean] ['edit']
    Turn on/off the display of plug-in shapes for the view. It depends on the plug-in implementation whether to respect this flag.

-----------------------------------------

pm    : polymeshes      [boolean] ['query', 'edit']
    Turn on/off the display of polygon meshes for the view of the model editor.

-----------------------------------------

qpo   : queryPluginObjects [string] ['query']
    Query the on/off state of plug-in objects display for the view. To set the on/off state, use -pluginObjects instead.

-----------------------------------------

rs    : removeSelected  [boolean] ['edit']
    This flag causes the currently active objects to be removed from the list of objects visible in the view (if viewSelected is true).

-----------------------------------------

rdn   : rendererDeviceName [boolean] ['query']
    Query for the name of the draw API used by the Viewport 2.0 renderer for a 3d modeling viewport. The possible return values are "VirtualDeviceGL" if Maya is set to use "OpenGL - Legacy" for Viewport 2.0, "VirtualDeviceGLCore" if Maya is set to use "OpenGL - Core Profile" (either Compatibility or Strict) for Viewport 2.0, or "VirtualDeviceDx11" if Maya is set to use DirectX for Viewport 2.0. If the renderer for the 3d modeling viewport is not Viewport 2.0, an empty string will be returned.

-----------------------------------------

rls   : rendererList    [boolean] ['query']
    Query for a list of the internal names for renderers available for use with the 3d modeling viewport. The default list contains at least "vp2Renderer", if supported. See rendererName for more details on these renderers. Any plug-in viewport renderers will also appear in this list.

-----------------------------------------

rlu   : rendererListUI  [boolean] ['query']
    Query for a list of the UI names for renderers available for use with the 3d modeling viewport. The default list consists of the UI name for "vp2Renderer", if it is supported. Any plug-in viewport renderer's UI names will also appear in this list. This list and the list returned from rendererList have a 1:1 correspondance.

-----------------------------------------

rnm   : rendererName    [string] ['query', 'edit']
    Set or get the renderer used for a 3d modeling viewport. The name provided should be an internal name of a renderer. The 'rendererList' flag can be used to query for a list of available names. The default renderer is "vp2Renderer": Viewport 2.0.

-----------------------------------------

rol   : rendererOverrideList [boolean] ['query']
    Query for a list of the internal names for renderer overrides for a 3d viewport renderer. Currently only the "Viewport 2" renderer supports renderer overrides.

-----------------------------------------

rou   : rendererOverrideListUI [boolean] ['query']
    Query for a list of the UI names for renderer overrides for a 3d viewport renderer. Currently only the "Viewport 2" renderer supports renderer overrides.

-----------------------------------------

rom   : rendererOverrideName [string] ['query', 'edit']
    Set or get the override used for a 3d viewport renderer. The name provided should be the internal name for an override. The 'rendererOverrideList' flag can be used to query for a list of available names. Currently only the "Viewport 2" renderer supports renderer overrides. Setting an empty string will unset any currently active override.

-----------------------------------------

rcc   : resetCustomCamera [boolean] ['edit']
    When specified will reset the camera transform for the active custom camera used for a scene render filter. It is only enabled when a valid scene render filter is specified.

-----------------------------------------

rr    : rigRoot         [string] ['query', 'edit']
    Defines the rig root associated with this view.

-----------------------------------------

rcm   : rightCamera     [string] ['query']
    Only available in query mode: returns the current right camera of this view.

-----------------------------------------

srf   : sceneRenderFilter [string] ['query', 'edit']
    Specifies the name of a scene render filter

-----------------------------------------

slc   : selectionConnection [string] ['query', 'edit']
    Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.

-----------------------------------------

sel   : selectionHiliteDisplay [boolean] ['query', 'edit']
    Sets whether the model panel will draw any selection hiliting on the objects in this window.

-----------------------------------------

ss    : setSelected     [boolean] ['edit']
    This flag causes the currently active objects to be the only objects visible in the view (if viewSelected is true).

-----------------------------------------

sml   : shadingModel    [int] ['query', 'edit']
    Shading model to use

-----------------------------------------

sdw   : shadows         [boolean] ['query', 'edit']
    Turn on/off the display of hardware shadows in shaded mode.

-----------------------------------------

soc   : smallObjectCulling [boolean] ['query', 'edit']
    Define whether small object culling should be enabled or not

-----------------------------------------

sot   : smallObjectThreshold [float] ['query', 'edit']
    Threshold used for small object culling

-----------------------------------------

swf   : smoothWireframe [boolean] ['query', 'edit']
    Turns on or off smoothing of wireframe lines and points

-----------------------------------------

st    : sortTransparent [boolean] ['query', 'edit']
    This flag turns on/off sorting of transparent objects during shaded mode refresh. Normally, objects are sorted according to their origin in camera space but when this flag is turned off they will be drawn according to their (depth-first traversal) order in the scene graph. This is a global flag that affects all model editors.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

sdm   : stereoDrawMode  [boolean] ['query', 'edit']
    If this flag is used then set stereo draw mode

-----------------------------------------

str   : strokes         [boolean] ['query', 'edit']
    Turn on/off the display of Paint Effects strokes for the view

-----------------------------------------

sds   : subdivSurfaces  [boolean] ['query', 'edit']
    Turn on/off the display of subdivision surfaces for the view of the model editor.

-----------------------------------------

se    : swapEyes        [boolean] ['query', 'edit']
    Swap the display of the left and right cameras. The left camera becomes the right draw pass and the right camera becomes the left draw pass.   This flag is intended for advanced users, for situations where the hardware uses the opposite left/right convention.

-----------------------------------------

ta    : textureAnisotropic [boolean] ['query', 'edit']
    Set whether to perform anisotropic texture filtering. Will work only if the anisotropic texture filtering extension is supported in OpenGL on the graphics system.

-----------------------------------------

tcp   : textureCompression [boolean] ['query', 'edit']
    Defines whether texture compression should be used or not

-----------------------------------------

td    : textureDisplay  [string] ['query', 'edit']
    Set the type of blending to use for textures. The blend is performed between the destination fragment and the texture fragment. The source is usually the material color. Argument options are: "modulate" : multiply the destination and texture fragment "decal" : overwrite the destination with the texture fragment

-----------------------------------------

tem   : textureEnvironmentMap [boolean] ['query', 'edit']
    If true then use a texture environment map

-----------------------------------------

th    : textureHilight  [boolean] ['query', 'edit']
    Set whether to show specular hilighting when the display is in shaded textured mode.

-----------------------------------------

tms   : textureMaxSize  [int] ['query', 'edit']
    Set maximum texture size for hardware texturing. The integer value must be a power of 2. Recommended values are 128 or 256. If the value specified is larger than the OpenGL maximim textures size for the graphics hardware it will be clamped to the OpenGL size. If many large textures are used in a scene reducing this value improves performance. On Impact texture memory is pinned in RAM so using large textures can cause reliability and performance problems. Again reducing this value will help. Software rendering does not use this value.  This flag is obsolete as of Maya 6.5. The maxTextureResolution/mtr argument on the displayPref command should be used instead.

-----------------------------------------

tmu   : textureMemoryUsed [boolean] ['query']
    Returns the total number of bytes used by all texture maps. This is typicly width*height*channels for all texture objects in the scene If the texture is mip mapped all mip map levels are included in the total though not never more than two level will be in use at one time

-----------------------------------------

ts    : textureSampling [int] ['query', 'edit']
    Set the type of sampling to be used for texture display. The argument can be either:    * 1 : means to perform point sample   * 2 : means to perform bilinear interpolation (default)

-----------------------------------------

tx    : textures        [boolean] ['query', 'edit']
    Turn on/off the display of texture objects for the view

-----------------------------------------

tis   : transpInShadows [boolean] ['query', 'edit']
    Set whether to enable display of transparency in shadows when using the hardware renderer. The default value is false.

-----------------------------------------

tal   : transparencyAlgorithm [string] ['query', 'edit']
    Set the transparency algorithm. The options are:    * 1) "frontAndBackCull" : Two pass front and back culling technique.   * 2) "perPolygonSort" : Draw transparent polygons in back-to-front order technique.  transparency pptions 1) and 2) are supported by the hardware renderer. Options 1) is supported by the interactive modeling viewports. The default value is "frontAndBackCull".

-----------------------------------------

tsl   : twoSidedLighting [boolean] ['query', 'edit']
    Turns on or off two sided lighting. This may be used with the -default flag.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

ulk   : unlockMainConnection [boolean] ['edit']
    Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.

-----------------------------------------

ucm   : updateColorMode [boolean] ['edit']
    Using this flag tells the model panel to check which color mode it should be in, and to switch accordingly. This flag may be used to update a model panel after a camera image plane has been added or removed.

-----------------------------------------

upd   : updateMainConnection [boolean] ['edit']
    Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.

-----------------------------------------

ubr   : useBaseRenderer [boolean] ['query', 'edit']
    Set whether to use the "base" renderer when using the hardware renderer and in "interactive display mode" (-useInteractiveMode) The default value is false.

-----------------------------------------

uci   : useColorIndex   [boolean] ['query', 'edit']
    Sets whether the model panel will attempt to use color index mode when possible. Color index mode can provide a performance increase for point, bounding box, and wireframe display modes. This may be used with the -default flag.

-----------------------------------------

ucb   : useCustomBackground [boolean] ['query', 'edit']
    When set to true, instead of using the standard background, draw a solid background using the viewColor.

-----------------------------------------

udm   : useDefaultMaterial [boolean] ['query', 'edit']
    Sets whether the model panel will draw all the shaded surfaces using the default material as opposed to using the material(s) currently assigned to the surfaces.

-----------------------------------------

ui    : useInteractiveMode [boolean] ['query', 'edit']
    Turns on or off the use of the special interaction settings during playback. This flag may be used with the -default flag.

-----------------------------------------

ip    : useRGBImagePlane [boolean] ['query', 'edit']
    Sets whether the model panel will be forced into RGB mode when there is an image plane attached to the panel's camera.

-----------------------------------------

urr   : useReducedRenderer [boolean] ['query', 'edit']
    Set true if using the reduced renderer

-----------------------------------------

ut    : useTemplate     [string] []
    Forces the command to use a command template other than the current one.

-----------------------------------------

un    : userNode        [string] ['query', 'edit']
    Allows the user to associate a node name with the modelEditor. The value is automatically updated in the event the node is deleted or renamed.

-----------------------------------------

vc    : viewColor       [[float, float, float, float]] ['query', 'edit']
    Specifies the background color for the stereoscopic model editor. The default value is black which provides optimal stereoscopic viewing. This only applies if 'useCustomBackground' is on (which is the default).

-----------------------------------------

vo    : viewObjects     [boolean] ['query']
    Returns the name (if any) of the objectSet which contains the list of objects visible in the view if viewSelected is true and the list of objects being displayed does not come from the active list.

-----------------------------------------

vs    : viewSelected    [boolean] ['query', 'edit']
    This flag turns on/off viewing of selected objects. When the flag is set to true, the currently active objects are captured and used as the list of objects to view.

-----------------------------------------

vt    : viewType        [boolean] ['query']
    Returns a string indicating the type of the model editor. For the default model editor, returns the empty string. For custom model editor types created via the API, returns the same string as is returned via the method MPx3dModelView::viewType().

-----------------------------------------

w     : width           [boolean] ['query']
    Return the width of the associated viewport in pixels.

-----------------------------------------

wbs   : wireframeBackingStore [boolean] ['query', 'edit']
    Sets whether a backing store is used to optimization the drawing of active objects. This mode can provide a performance increase in wireframe mode for certain scenes.

-----------------------------------------

wos   : wireframeOnShaded [boolean] ['query', 'edit']
    Sets whether the model panel will draw the wireframe on all shaded objects (if true) or only for active objects (if false).

-----------------------------------------

xr    : xray            [boolean]
    Turns on or off Xray mode. This may be used with the -default flag.

    """

def stereoRigManager(q=1,lr=1,rd="string",add="[string, string, string]",csf="[string, string]",cp="[string, string]",dr="string",d="string",l="[string, string]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/stereoRigManager.html



-----------------------------------------

stereoRigManager is undoable, queryable, and NOT editable.

This command manages the set of stereo rig tools.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

lr    : listRigs        [boolean] []
    When present, returns the list of all defined rigs. All other flags are ignored.

-----------------------------------------

rd    : rigDefinition   [string] []
    Returns the definition of a rig, in the same format as the add flag. A string array containing lang, create cameraSet. If an empty string is passed as the argument, then the default rig is used.

-----------------------------------------

add   : addRig          [[string, string, string]] []
    Adds a new stereo rig definition. This flag takes 3 arguments: name, language, create:    * name: A unique name for the rig type.   * lang: The language used for the callback. Valid values are "Python" and "MEL". Use the Python interface when possible.   * create: Procedure used to create a new rig of this type. This procedure takes no argument, and must return an array of strings. The first element is the root DAG node of the rig. The second and third elements are respectively the left and right cameras.

-----------------------------------------

csf   : cameraSetFunc   [[string, string]] []
    Specifies the function to call when a rig is about to be added to a camera set. This function must be the same language as originally defined by the tool.

-----------------------------------------

cp    : creationProcedure [[string, string]] []
    Changes the creation procedure of an existing rig definition. This flag takes 2 arguments: the name of the existing rig definition and the procedure.

-----------------------------------------

dr    : defaultRig      [string] ['query']
    Sets the default rig tool. The argument must be the name of one of the rigs added using the add flag. Returns True if the default could be set, False otherwise.

-----------------------------------------

d     : delete          [string] []
    Removes the definition of a stereo rig. The argument must be the name of one of the rigs added using the add flag.

-----------------------------------------

l     : language        [[string, string]]
    Changes the language of an existing rig definition. Valid values are "Python" and "MEL". This flag takes 2 arguments: the name of the existing rig definition and the language keyword.

    """

def track(d="linear",l="linear",r="linear",u="linear",up="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/track.html



-----------------------------------------

track is undoable, NOT queryable, and NOT editable.

The track command translates a camera horizontally or vertically in the world
space. The viewing-direction and up-direction of the camera are not altered.
There is no translation in the viewing direction.

The track command can be applied to either a perspective or an orthographic
camera.

When no camera name is supplied, this command is applied to the camera in the
active view.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

d     : down            [linear] []
    Set the amount of down translation in unit distance.

-----------------------------------------

l     : left            [linear] []
    Set the amount of left translation in unit distance.

-----------------------------------------

r     : right           [linear] []
    Set the amount of right translation in unit distance.

-----------------------------------------

u     : upDistance01    [linear] []
    Set the amount of up translation in unit distance. This is equivalent to using up/upDistance02 flag.

-----------------------------------------

up    : upDistance02    [linear]
    Set the amount of up translation in unit distance. This is equivalent to using u/upDistance01 flag.

    """

def tumble(aa="angle",ea="angle",lt="int",pp="[linear, linear, linear]",ra="[angle, angle]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/tumble.html



-----------------------------------------

tumble is undoable, NOT queryable, and NOT editable.

The tumble command revolves the camera(s) by varying the azimuth and elevation
angles in the perspective window. When both the azimuth and the elevation
angles are supplied on the command line, the camera is firstly tumbled for the
azimuth angle, then tumbled for the elevation angle.

When no camera name is supplied, this command is applied to the camera in the
active view.

The camera's rotate pivot will override a specified pivot point if the rotate
pivot is not at the camera's eye point.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

aa    : azimuthAngle    [angle] []
    Degrees to change the azimuth angle.

-----------------------------------------

ea    : elevationAngle  [angle] []
    Degrees to change the elevation angle.

-----------------------------------------

lt    : localTumble     [int] []
    Describes what point the camera will tumble around: 0 for the camera's tumble pivot, 1 for the camera's center of interest, and 2 for the camera's local axis, offset by its tumble pivot.

-----------------------------------------

pp    : pivotPoint      [[linear, linear, linear]] []
    Three dimensional point used as the pivot point in the world space.

-----------------------------------------

ra    : rotationAngles  [[angle, angle]]
    Two values in degrees to change the azimuth and elevation angles.

    """

def viewCamera(m="name",s=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/viewCamera.html



-----------------------------------------

viewCamera is undoable, NOT queryable, and NOT editable.

The viewCamera command is used to position a camera to look directly at the
side or top of another camera. This is primarily useful for the user when he
or she is setting depth-of-field and clipping planes, if they are being used.

The default behaviour: If no other flags are specified, the camera in the
active panel is moved and the -t is presumed. If there is a camera selected,
it is used as the target camera.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

m     : move            [name] []
    Specifies which camera needs to move.

-----------------------------------------

s     : sideView        [boolean] []
    Position camera to look at the side of the target camera.

-----------------------------------------

t     : topView         [boolean]
    Position camera to look at the top of the target camera (default).

    """

def viewClipPlane(q=1,acp=1,fcp="linear",ncp="linear",so=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/viewClipPlane.html



-----------------------------------------

viewClipPlane is undoable, queryable, and NOT editable.

The viewClipPlane command can be used to query or set a camera's clip planes.
If a camera is not specified, the camera in the active view will be used. The
near and far clip plane flags may be used in conjunction with the auto clip
plane flag.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

acp   : autoClipPlane   [boolean] ['query']
    Compute the clip planes such that all object's in the camera's viewing frustum will be visible.

-----------------------------------------

fcp   : farClipPlane    [linear] ['query']
    Set or query the far clip plane.

-----------------------------------------

ncp   : nearClipPlane   [linear] ['query']
    Set or query the near clip plane.

-----------------------------------------

so    : surfacesOnly    [boolean]
    This flag is to be used in conjunction with the auto clip plane flag. Only the bounding boxes of surfaces will be used to compute the camera's clipping planes.

    """

def viewFit(all=1,an=1,c=1,f="float",ns="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/viewFit.html



-----------------------------------------

viewFit is undoable, NOT queryable, and NOT editable.

The viewFit command positions the specified camera so its point-of-view
contains all selected objects other than itself. If no objects are selected,
everything is fit to the view (excepting cameras, lights, and sketching
plannes). The fit-factor, if specified, determines how much of the view should
be filled. If a camera is not specified, the camera in the active view will be
used. After the camera is moved, its center of interest is set to the center
of the bounding box of the objects.

Additionally, a list of objects can be passed as arguments. If a camera is
specified it must be the first argument. Objects passed as arguments to the
command will be used instead of the selected objects.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

all   : allObjects      [boolean] []
    Specifies that all objects are to be fit regardless of the active list.

-----------------------------------------

an    : animate         [boolean] []
    Specifies that the transition between camera positions should be animated.

-----------------------------------------

c     : center          [boolean] []
    Specifies that the camera moves to the center of the selected object, but does not move the camera closer.

-----------------------------------------

f     : fitFactor       [float] []
    Specifies how much of the view should be filled with the "fitted" items.

-----------------------------------------

ns    : namespace       [string]
    Specifies a namespace that should be excluded. All objects in the specified namespace will be excluded from the fit process.

    """

def viewHeadOn():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/viewHeadOn.html



-----------------------------------------

viewHeadOn is undoable, NOT queryable, and NOT editable.

The viewHeadOn command positions the specified camera so it is looking "down"
the normal of the live object, and fitted to the live object. If the live
object is a surface, an arbitrary normal is chosen.


-----------------------------------------


Return Value:

None
    """

def viewLookAt(pos="[linear, linear, linear]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/viewLookAt.html



-----------------------------------------

viewLookAt is undoable, NOT queryable, and NOT editable.

The viewLookAt command positions the specified camera so it is looking at the
centroid of all selected objects. If no objects are specified the camera will
look at the ground plane.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

pos   : position        [[linear, linear, linear]]
    Position in world space to make the camera look at.

    """

def viewPlace(an=1,eye="[linear, linear, linear]",fov="angle",la="[linear, linear, linear]",o=1,p=1,up="[linear, linear, linear]",vd="[linear, linear, linear]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/viewPlace.html



-----------------------------------------

viewPlace is undoable, NOT queryable, and NOT editable.

This command positions the camera as specified. The lookAt and viewDirection
flags are mutually exclusive, as are the ortho and perspective flags. If this
command switches a camera from ortho to perspective or the other way around
without specifying a new field of view, then one is calculated based on a
heuristic involving the selected objects.

If the camera is not specified on the command line, the command will check to
see if there is a camera on the active list.

The user should be aware that some positions will be unattainable. For
example, using a new camera located at the origin and specifying a lookAt of
[0 0 -5] and an up of [1 1 1]. In these cases, the camera will always aim at
the lookAt, and the new up direction will be determined by transforming the
specified up into camera space and then projecting this vector onto a plane
defined by the camera's up and right vectors. Using the example above, the new
up vector will be [1 1 0].


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

an    : animate         [boolean] []
    If set to true then animate the camera transition from current position to the final one.

-----------------------------------------

eye   : eyePoint        [[linear, linear, linear]] []
    The new eye point in world coordinates.

-----------------------------------------

fov   : fieldOfView     [angle] []
    The new field of view (in degrees, for perspective cameras, and in world distance for ortho cameras)

-----------------------------------------

la    : lookAt          [[linear, linear, linear]] []
    The new look-at point in world coordinates.

-----------------------------------------

o     : ortho           [boolean] []
    Sets the camera to be orthgraphic.

-----------------------------------------

p     : perspective     [boolean] []
    Sets the camera to be perspective.

-----------------------------------------

up    : upDirection     [[linear, linear, linear]] []
    The new up direction vector.

-----------------------------------------

vd    : viewDirection   [[linear, linear, linear]]
    The new view direction vector.

    """

def viewSet(q=1,an=1,b=1,bo=1,fit=1,ff="float",f=1,h=1,krs=1,ls=1,ns="string",nv=1,p=1,pv=1,rs=1,s=1,t=1,vnx=1,vny=1,vnz=1,vx=1,vy=1,vz=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/viewSet.html



-----------------------------------------

viewSet is undoable, queryable, and NOT editable.

This command positions the camera to one of the pre-defined positions. If the
fit flag is set in conjunction with persp, top, side, or front, the view is
"fit" based on the list of selected objects (if there are any) or on all the
objects if nothing is selected. Notice that the fit flag cannot be set in
conjunction with view along axis commands like viewX. If a camera is not
specified, the camera in the active view will be used. If no flag is
specified, the camera is set to the home position.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

an    : animate         [boolean] []
    Specifies that the transition between camera positions should be animated.

-----------------------------------------

b     : back            [boolean] []
    Moves the camera to the back position.

-----------------------------------------

bo    : bottom          [boolean] []
    Moves the camera to the bottom position.

-----------------------------------------

fit   : fit             [boolean] ['query']
    Apply a viewFit after positioning camera to persp, top, side, or front.

-----------------------------------------

ff    : fitFactor       [float] []
    Specifies how much of the view should be filled with the "fitted" items

-----------------------------------------

f     : front           [boolean] []
    Moves the camera to the front position.

-----------------------------------------

h     : home            [boolean] []
    Executes the camera's home attribute command. Before the string is executed, all occurances of "%camera" will be replaced by the camera's name. Use the camera command to set a camera's home command.

-----------------------------------------

krs   : keepRenderSettings [boolean] ['query']
    Retain the 'renderable' flag vaue on the view. Especially important if it switches from perspective to orthographic and then back again.

-----------------------------------------

ls    : leftSide        [boolean] []
    Moves the camera to the left side position.

-----------------------------------------

ns    : namespace       [string] []
    Specifies a namespace that should be excluded. All objects in the specified namespace will be excluded from the fit process.

-----------------------------------------

nv    : nextView        [boolean] ['query']
    Moves the camera to the next position.

-----------------------------------------

p     : persp           [boolean] []
    Moves the camera to the persp position.

-----------------------------------------

pv    : previousView    [boolean] ['query']
    Moves the camera to the previous position.

-----------------------------------------

rs    : rightSide       [boolean] []
    Moves the camera to the right side position.

-----------------------------------------

s     : side            [boolean] []
    Moves the camera to the (right) side position (deprecated).

-----------------------------------------

t     : top             [boolean] []
    Moves the camera to the top position.

-----------------------------------------

vnx   : viewNegativeX   [boolean] []
    Moves the camera to view along negative X axis.

-----------------------------------------

vny   : viewNegativeY   [boolean] []
    Moves the camera to view along negative Y axis.

-----------------------------------------

vnz   : viewNegativeZ   [boolean] []
    Moves the camera to view along negative Z axis.

-----------------------------------------

vx    : viewX           [boolean] []
    Moves the camera to view along X axis.

-----------------------------------------

vy    : viewY           [boolean] []
    Moves the camera to view along Y axis.

-----------------------------------------

vz    : viewZ           [boolean]
    Moves the camera to view along Z axis.

    """

def convertIffToPsd(q=1,ifn="string",pfn="string",xr="int",yr="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/convertIffToPsd.html



-----------------------------------------

convertIffToPsd is NOT undoable, queryable, and NOT editable.

Converts iff file to PSD file of given size


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ifn   : iffFileName     [string] ['query']
    Input iff file name

-----------------------------------------

pfn   : psdFileName     [string] ['query']
    Output file name

-----------------------------------------

xr    : xResolution     [int] ['query']
    X resolution of the image

-----------------------------------------

yr    : yResolution     [int]
    Y resolution of the image

    """

def createLayeredPsdFile(ifn="[string, string, string]",psf="string",xr="uint",yr="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/createLayeredPsdFile.html



-----------------------------------------

createLayeredPsdFile is undoable, NOT queryable, and NOT editable.

Creates a layered PSD file with image names as input to individual layers


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

ifn   : imageFileName   [[string, string, string]] []
    Layer name, blend mode, Image file name The image in the file will be transferred to layer specified. The image file specified can be in any of the formats supported by maya (ex. iff, jpg, gif, tif etc.). The blend mode options are : "Normal", "Dissolve", "Dark", "Multiply", "Color Burn", "Linear Burn", "Lighten", "Screen", "Color Dodge", "Linear Dogde", "Overlay", "Soft Light", "Hard Light", "Dissolve", "Vivid Light", "Linear Light", "Pin Light", "Hard Mix", "Difference", "Exclusion", "Hue", "Saturation", "Color", "Luminosity"

-----------------------------------------

psf   : psdFileName     [string] []
    PSD file name.

-----------------------------------------

xr    : xResolution     [uint] []
    X - resolution of the image.

-----------------------------------------

yr    : yResolution     [uint]
    Y - resolution of the image.

    """

def createRenderLayer(empty=1,g=1,mc=1,n="string",nr=1,num="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/createRenderLayer.html



-----------------------------------------

createRenderLayer is undoable, NOT queryable, and NOT editable.

Create a new render layer. The render layer number will be assigned based on
the first unassigned number not less than the base index number found in the
render layer global parameters. Normally all objects and their descendants
will be added to the new render layer but if '-noRecurse' is specified then
only the objects themselves will be added. Only transforms and geometry will
be added to the new render layer.


-----------------------------------------


Return Value:

string  Name of render layer node that was created


-----------------------------------------


Flags:

-----------------------------------------

e     : empty           [boolean] []
    If set then create an empty render layer. The global flag or specified member list will take precidence over use of this flag.

-----------------------------------------

g     : g               [boolean] []
    If set then create a layer that contains all DAG objects in the scene. Any future objects created will also automatically become members of this layer. The global flag will take precidence over use of the empty flag or specified member list.

-----------------------------------------

mc    : makeCurrent     [boolean] []
    If set then make the new render layer the current one.

-----------------------------------------

n     : name            [string] []
    Name of the new render layer being created.

-----------------------------------------

nr    : noRecurse       [boolean] []
    If set then only add specified objects to the render layer. Otherwise all descendants will also be added.

-----------------------------------------

num   : number          [int]
    Number for the new render layer being created.

    """

def editRenderLayerAdjustment(q=1,alg=1,lyr="name",nlg=1,r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerAdjustment.html



-----------------------------------------

editRenderLayerAdjustment is undoable, queryable, and NOT editable.

This command is used to create, edit, and query adjustments to render layers.
An adjustment allows different attribute values or connections to be used
depending on the active render layer.


-----------------------------------------


Return Value:

int  Number of adjustments applied    
string[]  Query: List of plugs adjustments to layer  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

alg   : attributeLog    [boolean] ['query']
    Output all adjustments for the specified layer sorted by attribute name.

-----------------------------------------

lyr   : layer           [name] ['query']
    Specified layer in which the adjustments will be modified. If not specified the active render layer will be used.

-----------------------------------------

nlg   : nodeLog         [boolean] ['query']
    Output all adjustments for the specified layer sorted by node name.

-----------------------------------------

r     : remove          [boolean]
    Remove the specified adjustments from the render layer. If an adjustment is removed from the current layer, the specified plug will revert back to it's master value determined by the default render layer.

    """

def editRenderLayerGlobals(q=1,bi="int",crl="name",eaa=1,mt="int",uc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerGlobals.html



-----------------------------------------

editRenderLayerGlobals is undoable, queryable, and NOT editable.

Edit the parameter values common to all render layers. Some of these
paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
currentRenderLayer, are stored in the file.


-----------------------------------------


Return Value:

boolean  Command success    
string  Current render layer name, when querying  
int  Merge type, when querying  
int  Base ID, when querying  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bi    : baseId          [int] ['query']
    Set base layer ID. This is the number at which new layers start searching for a unique ID.

-----------------------------------------

crl   : currentRenderLayer [name] ['query']
    Set current render layer. This will will update the renderLayerManger and all DAG objects to identify them as members of the render layer. This flag may also be used in conjunction with "useCurrent" to automatically add new DAG objects to the active layer. The "isCurrentRenderLayerChanging" condition can be used to determine when the current layer is being changed and adjustments are being applied to the scene.

-----------------------------------------

eaa   : enableAutoAdjustments [boolean] ['query']
    Set whether or not to enable automatic creation of adjustments when certain attributes (ie. surface render stats, shading group assignment, or render settings) are changed.

-----------------------------------------

mt    : mergeType       [int] ['query']
    Set file import merge type. Valid values are 0, none, 1, by number, and 2, by name.

-----------------------------------------

uc    : useCurrent      [boolean]
    Set whether or not to enable usage of the current render layer as the destination for all new nodes.

    """

def editRenderLayerMembers(q=1,fn=1,nr=1,r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerMembers.html



-----------------------------------------

editRenderLayerMembers is undoable, queryable, and NOT editable.

This command is used to query and edit memberships to render layers. Only
transform and geometry nodes may be members. At render time, all descendants
of the members of a render layer will also be included in the render layer.


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

nr    : noRecurse       [boolean] []
    If set then only add selected objects to the render layer. Otherwise all descendants of the selected objects will also be added. This flag may be applied to adding or removing objects from the layer.

-----------------------------------------

r     : remove          [boolean]
    Remove the specified objects from the render layer.

    """

def frameBufferName(a=1,c="string",l="string",p="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/frameBufferName.html



-----------------------------------------

frameBufferName is NOT undoable, NOT queryable, and NOT editable.

Returns the frame buffer name for a given renderPass renderLayer and camera
combination. Optionally, this command can apply a name truncation algorithm so
that the frameBuffer name will respect the maximum length imposed by the
destination file format, if applicable.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

a     : autoTruncate    [boolean] []
    use this flag to apply a name truncation algorithm so that the frameBuffer name will respect the maximum length imposed by the destination file format, if applicable.

-----------------------------------------

c     : camera          [string] []
    Specify a camera

-----------------------------------------

l     : renderLayer     [string] []
    Specify a renderer layer

-----------------------------------------

p     : renderPass      [string]
    Specify a renderer pass

    """

def psdChannelOutliner(q=1,e=1,ach="[string, string]",all=1,ann="string",bgc="[float, float, float]",dt="string",dtg="string",dcc="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,ni=1,npm=1,p="string",pma=1,po=1,ppa="string",ra=1,rc="string",sel="string",sc="string",si=1,sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/psdChannelOutliner.html



-----------------------------------------

psdChannelOutliner is undoable, queryable, and editable.

Create a psdChannelOutliner control which is capable of displaying a tree
structure upto one level.


-----------------------------------------


Return Value:

string  The full name of the psdChannelOutliner control    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ach   : addChild        [[string, string]] ['edit']
    This flag should be used along with the "-psdParent/ppa" flag. A string item gets added as a child to the parent specifed with "-psdParent/ppa" flag. The next string assigns an associated image name.

-----------------------------------------

all   : allItems        [boolean] ['query']
    Returns all the items in the form parent.child.

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

dtg   : docTag          [string] ['query', 'edit']
    Add a documentation flag to the control. The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)

-----------------------------------------

dcc   : doubleClickCommand [string] ['edit']
    Specify the command to be executed when an item is double clicked.

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

ni    : numberOfItems   [boolean] ['query']
    Total number of items in the control.

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

ppa   : psdParent       [string] ['edit']
    Adds an item string to the controls which is treated as parent.

-----------------------------------------

ra    : removeAll       [boolean] ['edit']
    Removes all the items from the control.

-----------------------------------------

rc    : removeChild     [string] ['edit']
    Deletes the particular child of the parent as specifed in "-psdParent/ppa" flag.

-----------------------------------------

sel   : select          [string] ['edit']
    Select the named item.

-----------------------------------------

sc    : selectCommand   [string] ['edit']
    Specify the command to be executed when an item is selected.

-----------------------------------------

si    : selectItem      [boolean] ['query']
    Returns the selected items.

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

def psdEditTextureFile(adc="string",acc="[string, float, float, float]",aci="[string, string]",deleteChannel="string",psf="string",ssi="string",uvt=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/psdEditTextureFile.html



-----------------------------------------

psdEditTextureFile is undoable, NOT queryable, and NOT editable.

Edits the existing PSD file. Addition and deletion of the channels (layer
sets) are supported.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

adc   : addChannel      [string] []
    Adds an empty layer set with the given name to a already existing PSD file.

-----------------------------------------

acc   : addChannelColor [[string, float, float, float]] []
    (M) Specifies the filled color of the layer which is created in a layer set given by the layer name.

-----------------------------------------

aci   : addChannelImage [[string, string]] []
    (M) Specifies the image file name whose image needs to be added as a layer to a given layer set which is the first string.

-----------------------------------------

deleteChannel : deleteChannel   [string] []
    (M) Deletes the channels (layer sets) from a PSD file. This is a multiuse flag.

-----------------------------------------

psf   : psdFileName     [string] []
    PSD file name.

-----------------------------------------

ssi   : snapShotImage   [string] []
    Image file name on the disk containing UV snapshot / reference image.

-----------------------------------------

uvt   : uvSnapPostionTop [boolean]
    Specifies the position of UV snapshot image layer in the PSD file. "True" positions this layer at the top and "False" positions the layer at the bottom next to the background layer in the PSD file

    """

def psdExport(q=1,aci="int",bpc="int",els=1,format="string",lyn="string",lsn="string",ofn="string",pma=1,ifn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/psdExport.html



-----------------------------------------

psdExport is NOT undoable, queryable, and NOT editable.

Writes the Photoshop file layer set into different formats. The output file
depth (bit per channel ) can be different from that of the input. If the input
is 16 bpc and output is 8 bpc, there will be data loss.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aci   : alphaChannelIdx [int] ['query']
    Index of the alpha channel to output, if not supplied, writes out the default alpha channel. The index is zero based. This is useful to write out specific alpha channels available as "Additional Alpha Channels" of Photoshop.

-----------------------------------------

bpc   : bytesPerChannel [int] ['query']
    Output file depth. Any of these keyword:    * 0 for choosing depth based on input   * 1 for 8 bits per channel   * 2 for 16 bits per channel  Default is 0.

-----------------------------------------

els   : emptyLayerSet   [boolean] ['query']
    Option to check if the given layer set is empty or not. This should be used in query mode and input file name and layer set names should be specified.

-----------------------------------------

format : format          [string] ['query']
    Output file format. Any of these keyword: "iff", "sgi", "pic", "tif", "als", "gif", "rla", "jpg"  Default is iff.

-----------------------------------------

lyn   : layerName       [string] ['query']
    Name of the layer to output.

-----------------------------------------

lsn   : layerSetName    [string] ['query']
    Name of the layer set to output, if not supplied, writes out the Composite image.  In query mode, this flag needs a value.

-----------------------------------------

ofn   : outFileName     [string] ['query']
    Name(with path) of the output file.

-----------------------------------------

pma   : preMultiplyAlpha [boolean] ['query']
    Option to multiply RGB colors with alpha values. If (r,g,b,a) is the value of pixel, it will be changed to (r*a, g*a, b*a, a) when this flag is used.

-----------------------------------------

ifn   : psdFileName     [string]
    Name(with path) of the input Photoshop file.  In query mode, this flag needs a value.

    """

def psdTextureFile(chc="[string, uint, uint, uint, uint]",chs="[string, uint, boolean]",ifn="[string, string, uint]",psf="string",ssi="string",uvt=1,xr="uint",yr="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/psdTextureFile.html



-----------------------------------------

psdTextureFile is undoable, NOT queryable, and NOT editable.

Creates a Photoshop file with UVSnap shot image and the layer set names as the
input.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

chc   : channelRGB      [[string, uint, uint, uint, uint]] []
    (M) Layer set names, index, red, green and blue values are given as input. Using this flag, the layers created can be filled with specified colors. This is a multi use flag. The index specifies the placement order of layer sets in the created file.

-----------------------------------------

chs   : channels        [[string, uint, boolean]] []
    (M) Layer set names and index are given as input. This is a multi use flag. A layer set with the given name will be created. The second argument is the index which specifies the placement order of layer sets in the created file. The third argument is a boolean, if "true" a layer is created inside the layer set , "false" creates an empty layer set

-----------------------------------------

ifn   : imageFileName   [[string, string, uint]] []
    Image file name, Layerset name and index. The image in the file will be transferred to layer set specified. The index specifies the placement order of layer sets in the created psd file. The image file specified can be in any of the formats supported by maya (ex. iff, jpg, gif, tif etc.)

-----------------------------------------

psf   : psdFileName     [string] []
    PSD file name.

-----------------------------------------

ssi   : snapShotImageName [string] []
    Image file name on the disk containing UV snapshot / reference image.

-----------------------------------------

uvt   : uvSnapPostionTop [boolean] []
    Specifies the position of UV snapshot image layer in the PSD file. "True" positions this layer at the top and "False" positions the layer at the bottom next to the background layer in the PSD file

-----------------------------------------

xr    : xResolution     [uint] []
    X - resolution of the image.

-----------------------------------------

yr    : yResolution     [uint]
    Y - resolution of the image.

    """

def renderLayerPostProcess(q=1,ki=1,sn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderLayerPostProcess.html



-----------------------------------------

renderLayerPostProcess is NOT undoable, queryable, and NOT editable.

Post process the results when rendering is done with. Presently this generates
a layered PSD file using individual iff files.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ki    : keepImages      [boolean] ['query']
    When set to on, the original iff images are kept after the conversion to PSD. Default is to remove them.

-----------------------------------------

sn    : sceneName       [string]
    Specifies the scene name for interactive batch rendering.

    """

def renderPassRegistry(ch="int",ips=1,pi="string",pn=1,r="string",scc=1,sdt=1,ps=1,spn=1,srp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/renderPassRegistry.html



-----------------------------------------

renderPassRegistry is NOT undoable, NOT queryable, and NOT editable.

query information related with render passes.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

ch    : channels        [int] []
    Specify the number of channels for query.

-----------------------------------------

ips   : isPassSupported [boolean] []
    Return whether the pass is supported by the renderer This flag must be specified by the flag -passID firstly. The renderer whose default value is the current renderer is specified by the flag renderer.

-----------------------------------------

pi    : passID          [string] []
    Specify the render pass ID for query.

-----------------------------------------

pn    : passName        [boolean] []
    Get the pass name for the passID. This flag must be specified by the flag -passID firstly.

-----------------------------------------

r     : renderer        [string] []
    Specify a renderer when using this command. By default the current renderer is specified.

-----------------------------------------

scc   : supportedChannelCounts [boolean] []
    List channel counts supported by the renderer(specified by the flag -renderer) and the specified pass ID. This flag must be specified by the flag -passID firstly.

-----------------------------------------

sdt   : supportedDataTypes [boolean] []
    List frame buffer types supported by the renderer(specified by the flag -renderer), the specified passID and channels. This flag must be specified by the flag -passID and -channels firstly.

-----------------------------------------

ps    : supportedPassSemantics [boolean] []
    List pass semantics supported by the specified passID. This flag must be specified by the flag -passId firstly.

-----------------------------------------

spn   : supportedRenderPassNames [boolean] []
    List render pass names supported by the renderer(specified by the flag -renderer).

-----------------------------------------

srp   : supportedRenderPasses [boolean]
    List render passes supported by the renderer(specified by the flag -renderer).

    """

def setRenderPassType(d=1,n="int",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setRenderPassType.html



-----------------------------------------

setRenderPassType is undoable, NOT queryable, and NOT editable.

This command will set the passID of a renderPass node and create the custom
attributes specified by the corresponding render pass definition. If the
render pass node already has a passID assigned to it, attributes that are no
longer required become hidden, and new attributes are unhidden and/or created
as needed. This allows passIDs to be changed back and forth without losing
attribute data. It also allows common attributes to be transported from one
render pass type to another.


-----------------------------------------


Return Value:

boolean  true/false


-----------------------------------------


Flags:

-----------------------------------------

d     : defaultDataType [boolean] []
    If set, the render pass will use its default data type.

-----------------------------------------

n     : numChannels     [int] []
    Specify the number of channels to use in the render pass. Note that this flag is only valid if there is an implementation supporting the requested number of channels.

-----------------------------------------

t     : type            [string]
    Specify the pass type to assign to the pass node(s).

    """

def ambientLight(q=1,e=1,ambientShade="float",drs="linear",exc=1,i="float",n="string",pos="[linear, linear, linear]",rgb="[float, float, float]",rot="[angle, angle, angle]",sc="[float, float, float]",sd="float",sh="int",ss=1,rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/ambientLight.html



-----------------------------------------

ambientLight is undoable, queryable, and editable.

TlightCmd is the base class for other light commands. The ambientLight command
is used to edit the parameters of existing ambientLights, or to create new
ones. The default behaviour is to create a new ambientlight.

This is the commmand that instantiates an ambientLight or edits the parameters
of an existing one. TambientLightCmd inherits from TlightCmd which defines
common flags like intensity, colour etc. See TlightCmd for a global picture of
the light commands. Note that the flag fAmbientLightUsed indicates whether the
command uses any ambient specific flags. That is, if a command doesn't use
flags defined here, the boolean fAmbientLightUsed is set to false and thus the
undo/redo information is not saved at this level.

TambientLightCmd behaves like any other command, it has flags, saves undo
information etc. the only slightly different behaviour is that it calls up to
TlightCmd to complete the functionality of the command. Example parseArgs:
TambientLightCmd defines ambientLight specific parameters like -ambientShade
however, several other parameters are available in TlightCmd such as
-intensity etc. So when parsing the arguments, a call is made to
TlightCmd::parseArgs to parse common parameters (like Intensity).


-----------------------------------------


Return Value:

double[]  when querying the rgb or shadowColor flags double when querying the
intensity flag boolean when querying the useRayTraceShadows or exclusive flags
linear[] when querying the position flag angle[] when querying the rotation
flag string when querying the name flag    
string  Light shape name  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ambientShade : ambientShade    [float] ['query', 'edit']
    ambientShade

-----------------------------------------

drs   : discRadius      [linear] ['query', 'edit']
    radius of the disc around the light

-----------------------------------------

exc   : exclusive       [boolean] ['query']
    True if the light is exclusively assigned

-----------------------------------------

i     : intensity       [float] ['query']
    Intensity of the light

-----------------------------------------

n     : name            [string] ['query']
    Name of the light

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query']
    Position of the light

-----------------------------------------

rgb   : rgb             [[float, float, float]] ['query']
    RGB colour of the light

-----------------------------------------

rot   : rotation        [[angle, angle, angle]] ['query']
    Rotation of the light for orientation, where applicable

-----------------------------------------

sc    : shadowColor     [[float, float, float]] ['query']
    Color of the light's shadow

-----------------------------------------

sd    : shadowDither    [float] ['query', 'edit']
    dither the shadow

-----------------------------------------

sh    : shadowSamples   [int] ['query', 'edit']
    number of shadow samples.

-----------------------------------------

ss    : softShadow      [boolean] ['query', 'edit']
    soft shadow

-----------------------------------------

rs    : useRayTraceShadows [boolean]
    True if ray trace shadows are to be used

    """

def defaultLightListCheckBox(q=1,e=1,ann="string",bgc="[float, float, float]",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,l="string",m=1,nbg=1,npm=1,p="string",pma=1,po=1,sg="name",sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/defaultLightListCheckBox.html



-----------------------------------------

defaultLightListCheckBox is undoable, queryable, and editable.

This command creates a checkBox that controls whether a shadingGroup is
connected/disconnected from the defaultLightList.


-----------------------------------------


Return Value:

string  Full name to the control    
  
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

l     : label           [string] ['edit']
    Value of the checkbox label

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

sg    : shadingGroup    [name] ['edit']
    The shading group that is to be connected/disconnected from the defaultLightList.

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

def directionalLight(q=1,e=1,d="int",drs="linear",exc=1,i="float",n="string",pos="[linear, linear, linear]",rgb="[float, float, float]",rot="[angle, angle, angle]",sc="[float, float, float]",sd="float",sh="int",ss=1,rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/directionalLight.html



-----------------------------------------

directionalLight is undoable, queryable, and editable.

TlightCmd is the base class for other light commands. TnonAmbientLightCmd is a
class that looks like a command but is not. It is a base class for the
extended/nonExtended lights. TnonExtendedLightCmd is a base class and not a
real command. It is inherited by several lights: TpointLight,
TdirectionalLight, TspotLight etc. The directionalLight command is used to
edit the parameters of existing directionalLights, or to create new ones. The
default behaviour is to create a new directionallight.

This is the commmand that instantiates an directionalLight or edits the
parameters of an existing one. TdirectionalLightCmd inherits from
TnonExtendedLightCmd which defines softShadow flags. See TlightCmd for a
global picture of the light commands.

TdirectionalLightCmd behaves like any other command, it has flags, saves undo
information etc. the only slightly different behaviour is that it calls up to
TnonExtendedLightCmd to complete the functionality of the command.


-----------------------------------------


Return Value:

double[]  when querying the rgb or shadowColor flags double when querying the
intensity flag boolean when querying the useRayTraceShadows or exclusive flags
linear[] when querying the position flag angle[] when querying the rotation
flag string when querying the name flag    
int  rate of light decay, when querying the decayRate flag  
int  Number of shadow samples, when querying the shadowSamples flag boolean
True if soft shadows are enabled, when querying the softShadow flag float
Shadow dithering value, when querying the shadowDither flag float Disc radius
value, when querying the discRadius flag  
string  Light shape name  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : decayRate       [int] []
    Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)

-----------------------------------------

drs   : discRadius      [linear] ['query']
    Radius of shadow disc.

-----------------------------------------

exc   : exclusive       [boolean] ['query']
    True if the light is exclusively assigned

-----------------------------------------

i     : intensity       [float] ['query']
    Intensity of the light

-----------------------------------------

n     : name            [string] ['query']
    Name of the light

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query']
    Position of the light

-----------------------------------------

rgb   : rgb             [[float, float, float]] ['query']
    RGB colour of the light

-----------------------------------------

rot   : rotation        [[angle, angle, angle]] ['query']
    Rotation of the light for orientation, where applicable

-----------------------------------------

sc    : shadowColor     [[float, float, float]] ['query']
    Color of the light's shadow

-----------------------------------------

sd    : shadowDither    [float] ['query']
    Shadow dithering value.

-----------------------------------------

sh    : shadowSamples   [int] ['query']
    Numbr of shadow samples to use

-----------------------------------------

ss    : softShadow      [boolean] ['query']
    True if soft shadowing is to be enabled

-----------------------------------------

rs    : useRayTraceShadows [boolean]
    True if ray trace shadows are to be used

    """

def exclusiveLightCheckBox(q=1,e=1,ann="string",bgc="[float, float, float]",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,l="string",lt="name",m=1,nbg=1,npm=1,p="string",pma=1,po=1,sbm="string",ut="string",vis=1,vcc="script",w="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/exclusiveLightCheckBox.html



-----------------------------------------

exclusiveLightCheckBox is undoable, queryable, and editable.

This command creates a checkBox that controls a light's exclusive non-
exclusive status. An exclusive light is one that is not hooked up to the
default-light-list, thus it does not illuminate all objects be default.
However an exclusive light can be linked to an object.


-----------------------------------------


Return Value:

string  Full name to the control    
  
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

l     : label           [string] ['edit']
    Value of the checkbox label

-----------------------------------------

lt    : light           [name] []
    The light that is to be made exclusive/non-exclusive.

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

def lightlink(q=1,b=1,h=1,l="name",m=1,o="name",set=1,shd=1,shp=1,t=1,ual=1,uao=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lightlink.html



-----------------------------------------

lightlink is undoable, queryable, and NOT editable.

This command is used to make, break and query light linking relationships
between lights/sets of lights and objects/sets of objects.

If no make, break or query flag is specified and both lights and objects flags
are present, the make flag is assumed to be specified.

If no make, break or query flag is specified and only one of the lights and
objects flags is present, the query flag is assumed to be specified.

You can specify as many lights and objects as you like, using the multiuse
-light and -object flags.

A better way to perform light linking is to make sets of lights and sets of
geometry. If you create a set which contains lights (such as the ceiling
lights in your scene) and a set which contains geometry (such as the geometry
of your character), you can then link the set containing lights with the set
containing geometry in order to get those lights to illuminate those pieces of
geometry. In addition, you can add and remove lights and geometry from their
respective sets without having to make and break light links.


-----------------------------------------


Return Value:

string  Single element command result    
string[]  Multi element command result  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : b               [boolean] []
    The presence of this flag on the command indicates that the command is being invoked to break links between lights and renderable objects.

-----------------------------------------

h     : hierarchy       [boolean] []
    When querying, specifies whether the result should include the hierarchy of transforms above shapes linked to the queried light/object. The transforms considered part of the hierarchy do not include the transform immediately above the shape. Default is true.

-----------------------------------------

l     : light           [name] []
    The argument to the light flag specifies a node to be used by the command in performing the action as if the node is a light. This is a multiuse flag -- many light nodes can be specified in a single invocation of the lightlink command.

-----------------------------------------

m     : make            [boolean] []
    The presence of this flag on the command indicates that the command is being invoked to make links between lights and renderable objects.

-----------------------------------------

o     : object          [name] []
    The argument to the object flag specifies a node to be used by the command in performing the action as if the node is an object. This is a multiuse flag -- many object nodes can be specified in a single invocation of the lightlink command.

-----------------------------------------

set   : sets            [boolean] []
    When querying, specifies whether the result should include sets linked to the queried light/object. Default is true.

-----------------------------------------

shd   : shadow          [boolean] []
    Specify that shadows are to be linked.

-----------------------------------------

shp   : shapes          [boolean] []
    When querying, specifies whether the result should include shapes linked to the queried light/object. Default is true.

-----------------------------------------

t     : transforms      [boolean] []
    When querying, specifies whether the result should include transforms immediately above shapes linked to the queried light/object. Default is true.

-----------------------------------------

ual   : useActiveLights [boolean] []
    Specify that active lights are to be used.

-----------------------------------------

uao   : useActiveObjects [boolean]
    Specify that active objects are to be used.

    """

def lightList(q=1,e=1,add="name",rm="name"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/lightList.html



-----------------------------------------

lightList is undoable, queryable, and editable.

Add/Remove a relationship between an object and the current light. Soon to be
replaced by the connect-attribute command.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : add             [name] []
    add object(s) to light list.

-----------------------------------------

rm    : remove          [name]
    remove object(s) to light list.

    """

def pointLight(q=1,e=1,d="int",drs="linear",exc=1,i="float",n="string",pos="[linear, linear, linear]",rgb="[float, float, float]",rot="[angle, angle, angle]",sc="[float, float, float]",sd="float",sh="int",ss=1,rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pointLight.html



-----------------------------------------

pointLight is undoable, queryable, and editable.

The pointLight command is used to edit the parameters of existing pointLights,
or to create new ones. The default behaviour is to create a new pointlight.


-----------------------------------------


Return Value:

string  Light shape name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

d     : decayRate       [int] ['query', 'edit']
    decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)

-----------------------------------------

drs   : discRadius      [linear] ['query', 'edit']
    radius of the disc around the light

-----------------------------------------

exc   : exclusive       [boolean] ['query', 'edit']
    This flag is obsolete.

-----------------------------------------

i     : intensity       [float] ['query', 'edit']
    intensity of the light (expressed as a percentage)

-----------------------------------------

n     : name            [string] ['query', 'edit']
    specify the name of the light

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    This flag is obsolete.

-----------------------------------------

rgb   : rgb             [[float, float, float]] ['query', 'edit']
    color of the light (0-1)

-----------------------------------------

rot   : rotation        [[angle, angle, angle]] ['query', 'edit']
    This flag is obsolete.

-----------------------------------------

sc    : shadowColor     [[float, float, float]] ['query', 'edit']
    the shadow color

-----------------------------------------

sd    : shadowDither    [float] ['query', 'edit']
    dither the shadow

-----------------------------------------

sh    : shadowSamples   [int] ['query', 'edit']
    number of shadow samples.

-----------------------------------------

ss    : softShadow      [boolean] ['query', 'edit']
    soft shadow

-----------------------------------------

rs    : useRayTraceShadows [boolean]
    ray trace shadows

    """

def spotLight(q=1,e=1,bd=1,bbd="angle",ca="angle",d="int",drs="linear",do="float",exc=1,i="float",lbd="angle",n="string",p="angle",pos="[linear, linear, linear]",rgb="[float, float, float]",rbd="angle",rot="[angle, angle, angle]",sc="[float, float, float]",sd="float",sh="int",ss=1,tbd="angle",rs=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/spotLight.html



-----------------------------------------

spotLight is undoable, queryable, and editable.

TlightCmd is the base class for other light commands. TnonAmbientLightCmd is a
class that looks like a command but is not. It is a base class for the
extended/nonExtended lights. TnonExtendedLightCmd is a base class and not a
real command. It is inherited by several lights: TpointLight,
TdirectionalLight, TspotLight etc. The spotLight command is used to edit the
parameters of existing spotLights, or to create new ones. The default
behaviour is to create a new spotlight.


-----------------------------------------


Return Value:

string  Light shape name boolean Barn door enabled state angle Left barn door
angle angle Right barn door angle angle Top barn door angle angle Bottom barn
door angle angle Cone angle angle Penumbra angle float Dropoff value    
double[]  when querying the rgb or shadowColor flags double when querying the
intensity flag boolean when querying the useRayTraceShadows or exclusive flags
linear[] when querying the position flag angle[] when querying the rotation
flag string when querying the name flag  
int  rate of light decay, when querying the decayRate flag  
int  Number of shadow samples, when querying the shadowSamples flag boolean
True if soft shadows are enabled, when querying the softShadow flag float
Shadow dithering value, when querying the shadowDither flag float Disc radius
value, when querying the discRadius flag  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bd    : barnDoors       [boolean] ['query', 'edit']
    Are the barn doors enabled?

-----------------------------------------

bbd   : bottomBarnDoorAngle [angle] ['query', 'edit']
    Angle of the bottom of the barn door.

-----------------------------------------

ca    : coneAngle       [angle] ['query', 'edit']
    angle of the spotLight

-----------------------------------------

d     : decayRate       [int] []
    Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)

-----------------------------------------

drs   : discRadius      [linear] ['query']
    Radius of shadow disc.

-----------------------------------------

do    : dropOff         [float] ['query', 'edit']
    dropOff of the spotLight

-----------------------------------------

exc   : exclusive       [boolean] ['query']
    True if the light is exclusively assigned

-----------------------------------------

i     : intensity       [float] ['query']
    Intensity of the light

-----------------------------------------

lbd   : leftBarnDoorAngle [angle] ['query', 'edit']
    Angle of the left of the barn door.

-----------------------------------------

n     : name            [string] ['query']
    Name of the light

-----------------------------------------

p     : penumbra        [angle] ['query', 'edit']
    specify penumbra region

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query']
    Position of the light

-----------------------------------------

rgb   : rgb             [[float, float, float]] ['query']
    RGB colour of the light

-----------------------------------------

rbd   : rightBarnDoorAngle [angle] ['query', 'edit']
    Angle of the right of the barn door.

-----------------------------------------

rot   : rotation        [[angle, angle, angle]] ['query']
    Rotation of the light for orientation, where applicable

-----------------------------------------

sc    : shadowColor     [[float, float, float]] ['query']
    Color of the light's shadow

-----------------------------------------

sd    : shadowDither    [float] ['query']
    Shadow dithering value.

-----------------------------------------

sh    : shadowSamples   [int] ['query']
    Numbr of shadow samples to use

-----------------------------------------

ss    : softShadow      [boolean] ['query']
    True if soft shadowing is to be enabled

-----------------------------------------

tbd   : topBarnDoorAngle [angle] ['query', 'edit']
    Angle of the top of the barn door.

-----------------------------------------

rs    : useRayTraceShadows [boolean]
    True if ray trace shadows are to be used

    """

def spotLightPreviewPort(q=1,e=1,ann="string",bgc="[float, float, float]",dt="string",dtg="string",dgc="script",dpc="script",en=1,ebg=1,ekf=1,ex=1,fpn=1,h="int",hlc="[float, float, float]",io=1,m=1,nbg=1,npm=1,p="string",pma=1,po=1,sl="name",sbm="string",ut="string",vis=1,vcc="script",w="int",wh="[int, int]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/spotLightPreviewPort.html



-----------------------------------------

spotLightPreviewPort is undoable, queryable, and editable.

This command creates a 3dPort that displays an image representing the
illumination provided by the spotLight. It is a picture of a plane being
illuminated by a light.

The optional argument is the name of the 3dPort.


-----------------------------------------


Return Value:

string  \- the name of the port created or modified    
  
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

sl    : spotLight       [name] []
    Name of the spotLight.

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

w     : width           [int] ['query', 'edit']
    The width of the control. The control will attempt to be this size if it is not overruled by parent layout conditions.

-----------------------------------------

wh    : widthHeight     [[int, int]]
    The width and height of the port.

    """

