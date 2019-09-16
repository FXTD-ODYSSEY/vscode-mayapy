def addMetadata(q=1,cn="string",cht="string",idt="string",scn=1,stn="string",str="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/addMetadata.html



-----------------------------------------

addMetadata is undoable, queryable, and NOT editable.

Defines the attachment of a metadata structure to one or more selected
objects. This creates a placeholder with an empty metadata Stream for later
population through the editMetadata command. It's similar in concept to the
addAttr command for nodes - a data description is added but no data is
actually set.

When assigning a metadata structure you must specify these flags \-
channelName is the metadata channel type (e.g. "vertex"), streamName is the
name of the metadata stream to be created, and structure is the name of the
structure type defining the contents of the metadata. The indexType flag is
optional. If it is not present then the index will be presumed to be a
standard numerical value.

You can query metadata information at a variety of levels. See the table below
for a full list of the queryable arguments. In each case the specification of
any of the non-queried arguments filters the list of metadata to be examined
during the query. For all queries a single object must be selected for
querying.

For example querying the channelName flag with no other arguments will return
the list of all Channel types on the selected object that contain any
metadata. Querying the channelName flag with the indexType flag specified will
return only those channel types containing metadata streams that use that
particular type of index.

  * Query the channelName flag to return the list of any channel types that have metadata.
  * Specify the channelName and streamName flags and query the structure flag to return the name of the structure assigned to the given stream (if any).
  * Specify a channelName and query the streamName to return the list of all streams assigned to that particular channel type.
  * If you query the streamName without a specific channelName then it returns a list of pairs of (channelName, streamName) for all metadata streams.

Flag Combinations:

    
    
    ChannelName IndexType StreamName Structure   Create   Can Query
         0          0          0         0         X        ChannelName, StreamName, Structure
         0          0          0         1         X        ChannelName, StreamName, IndexType
         0          0          1         0         X        ChannelName, Structure, IndexType
         0          0          1         1         X        ChannelName, IndexType
         0          1          0         0         X        ChannelName, StreamName, Structure
         0          1          0         1         X        ChannelName, StreamName
         0          1          1         0         X        ChannelName, Structure
         0          1          1         1         X        ChannelName
         1          0          0         0         X        StreamName, Structure, IndexType
         1          0          0         1         X        StreamName, IndexType
         1          0          1         0         X        Structure, IndexType
         1          0          1         1        (a)       IndexType
         1          1          0         0         X        StreamName, Structure
         1          1          0         1         X        StreamName
         1          1          1         0         X        Structure
         1          1          1         1        (b)       X
        (a) Assign an empty metadata stream with default index type
        (b) Assign an empty metadata stream with the named index type


-----------------------------------------


Return Value:

string[]  List of nodes to which a new Stream was successfully added (create
mode)    
string[]  List of channel types containing metadata on an object when querying
the channelName flag  
string[]  List of stream names on an object when querying the streamName flag  
string[]  List of structures used by an object's metadata Streams when
querying the structure flag  
string[]  List of index types used by an object when querying the indexType
flag  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cn    : channelName     [string] ['query']
    Name of the Channel type to which the structure is to be added (e.g. "vertex").  In query mode, this flag can accept a value.

-----------------------------------------

cht   : channelType     [string] ['query']
    Obsolete - use the 'channelName' flag instead.  In query mode, this flag can accept a value.

-----------------------------------------

idt   : indexType       [string] ['query']
    Name of the index type the new Channel should be using. If not specified this defaults to a simple numeric index. Of the native types only a mesh "vertexFace" channel is different, using a "pair" index type.  In query mode, this flag can accept a value.

-----------------------------------------

scn   : scene           [boolean] ['query']
    Use this flag when you want to add metadata to the scene as a whole rather than to any individual nodes. If you use this flag and have nodes selected the nodes will be ignored and a warning will be displayed.

-----------------------------------------

stn   : streamName      [string] ['query']
    Name of the empty stream being created. In query mode not specifying a value will return a list of streams on the named channel type.  In query mode, this flag can accept a value.

-----------------------------------------

str   : structure       [string]
    Name of the structure which defines the metadata to be attached to the object. In query mode this will return the name of the structure attached at a given stream.  In query mode, this flag can accept a value.

    """

def applyMetadata(fmt="string",scn=1,v="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/applyMetadata.html



-----------------------------------------

applyMetadata is undoable, NOT queryable, and NOT editable.

Define the values of a particular set of metadata on selected objects. This
command is used in preservation of metadata through Maya file formats
(.ma/.mb). If any metadata already exists it will be kept and merged with the
new metadata, overwriting duplicate entries. (i.e. if this command specifies
data at index N and you already have a value at index N then the one this
command specifies will be the new value and the old one will cease to exist.)

Unlike the editMetadata command it is not necessary to first use the
addMetadata command or API equivalent to attach a metadata stream to the
object, this command will do both assignment of structure and of metadata
values. You do have to use the dataStructure command or API equivalent to
create the structure being assigned first though.

The formatted input will be in a form expected by the data associations
serializer (see adsk::Data::AssociationsSerializer for more information). The
specific serialization type will be the default 'raw' if the format flag is
not used.

For example the "raw" format input string "channel
face\n[STREAMDATA]\nendChannels\nendAssociations" with no flags is equivalent
to the input "[STREAMDATA]\nendChannels" with the channel flag set to 'face'


-----------------------------------------


Return Value:

Boolean  True if the application succeeded


-----------------------------------------


Flags:

-----------------------------------------

fmt   : format          [string] []
    Name of the data association format type to use in the value flag parsing. Default value is "raw".

-----------------------------------------

scn   : scene           [boolean] []
    Use this flag when you want to apply metadata to the scene as a whole rather than to any individual nodes. If you use this flag and have nodes selected the nodes will be ignored and a warning will be displayed. Scene metadata is incompatible with referenced scenes. Node associated metadata from referenced files will still be readable from master scenes but scene specific metadata of referenced files will not be accessible from a any master scene. This will ensure that referenced files metadata will not end up corrupting the master file scene-metadata.

-----------------------------------------

v     : value           [string]
    String containing all of the metadata to be assigned to the selected object.

    """

def blindDataType(dt="string",ldn="string",ln=1,query=1,sdn="string",sn=1,id="int",tn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/blindDataType.html



-----------------------------------------

blindDataType is undoable, NOT queryable, and NOT editable.

This command creates a blind data type, which is represented by a
blindDataTemplate node in the DG. A blind data type can have one or more
attributes. On the command line, the attributes should be ordered by type for
best memory utilization, largest first: string, binary, double, float, int,
and finally boolean. Once a blind data type is created, blind data of that
type may be assigned using the polyBlindData command. Note that as well as
polygon components, blind data may be assigned to objects and to NURBS
patches. A blind data type may not be modified after it is created: in order
to do so it must be deleted and recreated. Any existing blind data of that
type would also need to be deleted and recreated. When used with the query
flag, this command will return information about the attributes of the
specified blind data type.


-----------------------------------------


Return Value:

string  Name of nodes created


-----------------------------------------


Flags:

-----------------------------------------

dt    : dataType        [string] []
    Specifies the dataTypes that are part of BlindData node being created. Allowable strings are "int", "float", "double", "string", "boolean" and "binary". Must be used togeter with the -ldn and -sdn flags to specify each attribute.

-----------------------------------------

ldn   : longDataName    [string] []
    Specifies the long names of the datas that are part of BlindData node being created. Must be used togeter with the -dt and -sdn flags to specify each attribute.

-----------------------------------------

ln    : longNames       [boolean] []
    Specifies that for a query command the long attributes names be listed.

-----------------------------------------

q     : query           [boolean] []
    Specifies that this is a special query type command.

-----------------------------------------

sdn   : shortDataName   [string] []
    Specifies the short names of the data that are part of BlindData node being created. Must be used togeter with the -dt and -ldn flags to specify each attribute.

-----------------------------------------

sn    : shortNames      [boolean] []
    Specifies that for a query command the short attribute names be listed.

-----------------------------------------

id    : typeId          [int] []
    Specifies the typeId of the BlindData type being created.

-----------------------------------------

tn    : typeNames       [boolean]
    Specifies that for a query command the data types be listed.

    """

def dataStructure(q=1,af="string",asString="string",dt=1,fmt="string",lmn="string",n="string",rem=1,ral=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dataStructure.html



-----------------------------------------

dataStructure is undoable, queryable, and NOT editable.

Takes in a description of the structure and creates it, adding it to the list
of available data structures. The structure definition can either be supplied
in the asString flag or exist in a file that is referenced by the asFile flag.

If the remove flag is specified with a name flag then the data structure will
be removed. This is to keep all structure operations in a single command
rather than create separate commands to create, remove, and query the data
structures. When you use the removeAll flag then every existing metadata
structure is removed. Use with care! Note that removed structures may still be
in use in metadata Streams after removal, they are just no longer available
for the creation of new Streams.

Both the creation modes and the remove mode are undoable.

Creation of an exact duplicate of an existing structure (including name) will
succeed silently without actually creating a new structure. Attempting to
create a new non-duplicate structure with the same name as an existing
structure will fail as there is no way to disambiguate two structures with the
same name.

Querying modes are defined to show information both on the created structures
and the structure serialization formats that have been registered. The
serialization formats preserve the structure information as text (e.g. raw,
XML, JSON). Since the raw structure type is built in it will be assumed when
none are specified.

General query with no flags will return the list of names of all currently
existing structures.

Querying the format flag will return the list of all registered structure
serialization formats.

Querying with the format supplied before the query flag will show the detailed
description of that particular structure serialization format.

Querying the asString flag with a structure name and serialization format
supplied before the query flag will return a string representing the named
data structure in the serialization format specified by the format flag. Even
if the format is the same as the one that created the structure the query
return string may not be identical since the queried value is formatted in a
standard way - original formatting is not preserved.

Querying the asFile flag with a structure name supplied before the query flag
will return the original file from which the structure was generated. If the
structure was created using the asString flag or through the API then an empty
string will be returned.

Querying the name flag returns the list of all structures created so far.


-----------------------------------------


Return Value:

string  Name of the resulting structure, should match the name defined in the
structure description    
string[]  Name(s) of the removed structures.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

af    : asFile          [string] ['query']
    Specify a file that contains the serialized data which describes the structure. The format of the data is specified by the 'format' flag.

-----------------------------------------

asString : asString        [string] ['query']
    Specify the string containing the serialized data which describes the structure. The format of the data is specified by the 'format' flag.

-----------------------------------------

dt    : dataType        [boolean] ['query']
    Used with the flag 'listMemberNames' to query the type of the member. The type is appended after each relative member in the array. For example, if the format is "name=idStructure:int32=id:string=name" the returned array is "id int32 name string".

-----------------------------------------

fmt   : format          [string] ['query']
    Format of data to expect in the structure description. "raw" is supported natively and will be assumed if the format type is omitted. Others are available via plug-in. You can query the available formats by using this flag in query mode.  In query mode, this flag can accept a value.

-----------------------------------------

lmn   : listMemberNames [string] ['query']
    Query the member names in the dataStructure. The member names will be returned in an array. The name of the data structure will not be returned. To get the type of each member, use 'dataType' together. Then the type of the member will be appended in the array after their relative member. For example, if the format is "name=idStructure:int32=id:string=name" the returned array is "id int32 name string".

-----------------------------------------

n     : name            [string] ['query']
    Query mode only. Name of the data structure to be queried, or set to list the available names.  In query mode, this flag can accept a value.

-----------------------------------------

rem   : remove          [boolean] []
    Remove the named data structure. It's an error if it doesn't exist.

-----------------------------------------

ral   : removeAll       [boolean]
    Remove all metadata structures. This flag can not be used in conjunction with any other flags.

    """

def editMetadata(mn="string",rem=1,sv="string",v="float",cn="string",cht="string",eix="string",idx="string",idt="string",scn=1,six="string",stn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/editMetadata.html



-----------------------------------------

editMetadata is undoable, NOT queryable, and NOT editable.

This command is used to set metadata elements onto or remove metadata elements
from an object. Before using this command you must first attach a metadata
stream type to the object using the addMetadata command or an API equivalent.
The command has four basic variations:

  1. Set per-component metadata on meshes
  2. Remove per-component metadata on meshes
  3. Set generic metadata on any object
  4. Remove generic metadata on any object

The difference between the set and remove variations (1,3 vs. 2,4) is that set
requires both a member name to be set and a new value to be set. (The reason
removal doesn't use a member name is that you can only remove an entire
metadata structural element, you cannot remove only a single member from it.)

When metadata values are set or removed the action is performed on every
selected component or index. This provides an easy method to set or remove a
bunch of metadata en masse.

The general usage (variations 3, 4) lets you select specific pieces of
metadata through the channelName and index flags. Note that since index is a
multi-use flag you can select many different elements from the same Channel
and set or remove the metadata on all of them in one command.

Metadata on meshes is special in that the Channel types "vertex", "edge",
"face", and "vertexFace" are directly connected to the components of the same
name. To make setting these metadata Channels easier you can simply select or
specify on the command line the corresponding components rather than using the
channelName and index flags. For example the selection "myMesh.vtx[8:10]"
corresponds to channelName = vertex and index = 8, 9, 10 (as a multi-use
flag).

Note that the metadata is assigned to an object and except in the special case
of mesh geometry does not flow through the dependency graph. In meshes the
metadata will move from node to node wherever the geometry is connected,
although it will not adjust itself automatically for changes in topology.
Internal data is arranged to minimize the amount of copying no matter how many
other nodes are connected to it.

Only a single node or scene, component type, channel type, and value type are
allowed in a single command. This keeps the data simple at the possible cost
of requiring multiple calls to the command to set more than one structure
member's value.

Certain nodes have metadata supplied by input attributes. If you edit one of
those with an incoming connection on such an attribute then the metadata edit
will not be applied directly it will be put into an 'editMetadata' node for
application during DG evaluation. Since the details of the metadata are not
known until the evaluation happens less rigorous compatibility checking is
performed. The editMetadata node has its own facilities for verifying and
reporting illegal metadata edits. Successive edits to the same metadata in
this way appends each edit to the same editMetadata node.


-----------------------------------------


Return Value:

string  Name of the node where the new edits reside, empty string if edits
failed. It will be an editMetadata node if construction history was present.


-----------------------------------------


Flags:

-----------------------------------------

mn    : memberName      [string] []
    Name of the Structure member being edited. The names of the members are set up in the Structure definition, either through the description passed in through the "dataStructure" command or via the API used to create that Structure.

-----------------------------------------

rem   : remove          [boolean] []
    If the remove flag is set then the metadata will be removed rather than have values set. In this mode the "memberName", "value", and "stringValue" flags are ignored. "memberName" is ignored because when deleting metadata all members of a structure must be removed as a group. The others are ignored since when deleting you don't need a value to be set.

-----------------------------------------

sv    : stringValue     [string] []
    String value to be set into the specified metadata locations. This flag can only be used when the data member is a numeric type. If the member has N dimensions (e.g. string[2]) then this flag must appear N times (e.g. 2 times) The same values are applied to the specified metadata member on all affected components or metadata indices. Only one of the value, and stringValue flags can be specified at once and the type must match the type of the structure member named by the "member" flag.

-----------------------------------------

v     : value           [float] []
    Numeric value to be set into the specified metadata locations. This flag can only be used when the data member is a numeric type. If the member has N dimensions (e.g. float[3]) then this flag must appear N times (e.g. 3 times) The same values are applied to the specified metadata member on all affected components or metadata indices. All numeric member types should use this type of value specification, i.e. everything except string and matrix types. Only one of the value, and stringValue flags can be specified at once and the type must match the type of the structure member named by the "member" flag.

-----------------------------------------

cn    : channelName     [string] ['query']
    Filter the metadata selection to only recognize metadata belonging to the specified named Channel (e.g. "vertex"). This flag is ignored if the components on the selection list are being used to specify the metadata of interest.  In query mode, this flag can accept a value.

-----------------------------------------

cht   : channelType     [string] ['query']
    Obsolete - use the 'channelName' flag instead.  In query mode, this flag can accept a value.

-----------------------------------------

eix   : endIndex        [string] []
    The metadata is stored in a Stream, which is an indexed list. If you have mesh components selected then the metadata indices are implicit in the list of selected components. If you select only the node or scene then this flag may be used in conjunction with the startIndex flag to specify a range of indices from which to retrieve the metadata. It is an error to have the value of startIndex be greater than that of endIndex.  See also the index flag for an alternate way to specify multiple indices. This flag can only be used on index types that support a range (e.g. integer values - it makes no sense to request a range between two strings)  In query mode, this flag can accept a value.

-----------------------------------------

idx   : index           [string] ['query']
    In the typical case metadata is indexed using a simple integer value. Certain types of data may use other index types. e.g. a "vertexFace" component will use a "pair" index type, which is two integer values; one for the face ID of the component and the second for the vertex ID.  The index flag takes a string, formatted in the way the specified indexType requires. All uses of the index flag have the same indexType. If the type was not specified it is assumed to be a simple integer value.  In query mode, this flag can accept a value.

-----------------------------------------

idt   : indexType       [string] ['query']
    Name of the index type the new Channel should be using. If not specified this defaults to a simple integer index. Of the native types only a mesh "vertexFace" channel is different, using a "pair" index type.  In query mode, this flag can accept a value.

-----------------------------------------

scn   : scene           [boolean] ['query']
    Use this flag when you want to add metadata to the scene as a whole rather than to any individual nodes. If you use this flag and have nodes selected the nodes will be ignored and a warning will be displayed.

-----------------------------------------

six   : startIndex      [string] []
    The metadata is stored in a Stream, which is an indexed list. If you have mesh components selected then the metadata indices are implicit in the list of selected components. If you select only the node or scene then this flag may be used in conjunction with the endIndex flag to specify a range of indices from which to retrieve the metadata. It is an error to have the value of startIndex be greater than that of endIndex.  See also the index flag for an alternate way to specify multiple indices. This flag can only be used on index types that support a range (e.g. integer values - it makes no sense to request a range between two strings)  In query mode, this flag can accept a value.

-----------------------------------------

stn   : streamName      [string]
    Name of the metadata Stream. Depending on context it could be the name of a Stream to be created, or the name of the Stream to pass through the filter.  In query mode, this flag can accept a value.

    """

def geomToBBox(ba=1,cm=1,et="time",ko=1,n="string",ns="string",sb="time",sc="[float, float, float]",s=1,st="time"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/geomToBBox.html



-----------------------------------------

geomToBBox is undoable, NOT queryable, and NOT editable.

Create polygonal mesh bounding boxes for geometry. Can also create a single
bounding box per hierarchy.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

ba    : bakeAnimation   [boolean] []
    Bake the animation. Can be used with startTime, endTime and sampleBy flags. If used alone, the time slider will be used to specify the startTime and endTime.

-----------------------------------------

cm    : combineMesh     [boolean] []
    Combine resulting bounding boxes. Mutually exclusive with -s/single option.

-----------------------------------------

et    : endTime         [time] []
    Used with bakeAnimation flag. Specifies the end time of the baking process.

-----------------------------------------

ko    : keepOriginal    [boolean] []
    Do not remove the selected nodes used to create the bounding boxes.

-----------------------------------------

n     : name            [string] []
    Specifies the bounding box name.

-----------------------------------------

ns    : nameSuffix      [string] []
    Specifies the bounding box name suffix.

-----------------------------------------

sb    : sampleBy        [time] []
    Used with bakeAnimation flag. Specifies the animation evaluation time increment.

-----------------------------------------

sc    : shaderColor     [[float, float, float]] []
    Set the color attribute of the Lambert material associate with the bounding box. The RGB values should be defined between 0 to 1.0. Default value is 0.5 0.5 0.5.

-----------------------------------------

s     : single          [boolean] []
    Create a single bounding box per hierarchy selected.

-----------------------------------------

st    : startTime       [time]
    Used with bakeAnimation flag. Specifies the start time of the baking process.

    """

def getMetadata(dt=1,lcn=1,lmn=1,lsn=1,mn="string",cn="string",cht="string",eix="string",idx="string",idt="string",scn=1,six="string",stn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getMetadata.html



-----------------------------------------

getMetadata is NOT undoable, NOT queryable, and NOT editable.

This command is used to retrieve the values of metadata elements from a node
or scene. It is restricted to returning a single structure member at a time.
For convenience the detail required is only enough to find a single Member of
a single Structure on a single metadata Channel.

In the simplest case if there is a single Stream on one metadata Channel which
uses a Structure with only one Member then all that is required is the name of
the object containing the metadata. In the most complex case the
'channelName', 'streamName', and 'memberName' are all required to narrow down
the metadata to a single unique Member.

In general for scripting it's a good idea to use all flags anyway since there
could be metadata added anywhere. The shortcuts are mainly for quick entry
when entering commands directly in the script editor or command line.

When an Index is specified where data is not present the command fails with a
message telling you which Index or Indices didn't have values. Use the
hasMetadata command first to determine where metadata exists if you need to
know in advance where to find valid metadata. Filter Flags

  * channelName \- Only look for metadata on one particular Channel type
  * streamName \- Only look for metadata on one particular named Stream. When used in conjunction with channelName then ignore Streams with a matching name but a different Channel type
  * index \- Only look for metadata on one or more specific Index values of a Stream. Requires use of the streamName flag. Does not require the indexType flag as that will be inferred by the streamName.
  * startIndex/endIndex \- Same as index but using an entire range of Index values rather than a single one. Not valid for index types not supporting ranges (e.g. strings)
  * indexType \- Only look for metadata using a particular Index type. Can have its scope narrowed by other filter flags as well.
  * memberName \- The particular Member in the metadata in a Structure to retrieve. If this is not specified the Structure can only have a single Member.

Metadata on meshes is special in that the Channel types "vertex", "edge",
"face", and "vertexFace" are directly connected to the components of the same
name. To make getting these metadata Channels easier you can simply select or
specify on the command line the corresponding components rather than using the
channelName and index/startIndex/endIndex flags. For example the selection
"myMesh.vtx[8:10]" corresponds to channelName = vertex and either index = 8,
9, 10 as a multi-use flag or setIndex = 8, endIndex=10.

Only a single node or scene and unique metadata Structure Member are allowed
in a single command. This keeps the data simple at the possible cost of
requiring multiple calls to the command to get more than one Structure
Member's value.

When the data is returned it will be in Index order with an entire Member
appearing together. For example if you were retrieving float[3] metadata on
three components you would get the nine values back in the order:
index[0]-float[0], index[0]-float[1], index[0]-float[2], index[1]-float[0],
index[1]-float[1], index[1]-float[2], index[2]-float[0], index[2]-float[1],
index[2]-float[2]. In the Python implementation the float[3] values will be an
array each so you would get back three float[3] arrays.


-----------------------------------------


Return Value:

int[]  List of integer values from the metadata member    
float[]  List of real values from the metadata member  
string[]  List of string values from the metadata member


-----------------------------------------


Flags:

-----------------------------------------

dt    : dataType        [boolean] []
    Used with the flag 'streamName' and 'memberName' to query the dataType of the specfied member.

-----------------------------------------

lcn   : listChannelNames [boolean] []
    Query the channel names on the shape. This flag can be used with some flags to filter the results. It can be used with the flag 'streamName' to get the channel with the specfied stream and the flag 'memberName' to get the channel in which the stream contains the specified member. It cannot be used with the flag 'channelName'.

-----------------------------------------

lmn   : listMemberNames [boolean] []
    Query the member names on the shape. This flag can be used with some flags to filter the results. It can be used with 'streamName' to get the member which is in the specified stream and the flag 'channelName' to get the member which is used in the specfied channel. It cannot be used with the flag 'memberName'.

-----------------------------------------

lsn   : listStreamNames [boolean] []
    Query the stream names on the shape. This flag can be used with some flags to filter the results. It can be used with the flag 'channelName' to get the stream names on the specified channel and the flag 'memberName' to get the stream names which has the specified member. It cannot be used with the flag 'streamName'.

-----------------------------------------

mn    : memberName      [string] []
    Name of the Structure member being retrieved. The names of the members are set up in the Structure definition, either through the description passed in through the "dataStructure" command or via the API used to create that Structure. This flag is only necessary when selected Structures have more than one member.

-----------------------------------------

cn    : channelName     [string] ['query']
    Filter the metadata selection to only recognize metadata belonging to the specified named Channel (e.g. "vertex"). This flag is ignored if the components on the selection list are being used to specify the metadata of interest.  In query mode, this flag can accept a value.

-----------------------------------------

cht   : channelType     [string] ['query']
    Obsolete - use the 'channelName' flag instead.  In query mode, this flag can accept a value.

-----------------------------------------

eix   : endIndex        [string] []
    The metadata is stored in a Stream, which is an indexed list. If you have mesh components selected then the metadata indices are implicit in the list of selected components. If you select only the node or scene then this flag may be used in conjunction with the startIndex flag to specify a range of indices from which to retrieve the metadata. It is an error to have the value of startIndex be greater than that of endIndex.  See also the index flag for an alternate way to specify multiple indices. This flag can only be used on index types that support a range (e.g. integer values - it makes no sense to request a range between two strings)  In query mode, this flag can accept a value.

-----------------------------------------

idx   : index           [string] ['query']
    In the typical case metadata is indexed using a simple integer value. Certain types of data may use other index types. e.g. a "vertexFace" component will use a "pair" index type, which is two integer values; one for the face ID of the component and the second for the vertex ID.  The index flag takes a string, formatted in the way the specified indexType requires. All uses of the index flag have the same indexType. If the type was not specified it is assumed to be a simple integer value.  In query mode, this flag can accept a value.

-----------------------------------------

idt   : indexType       [string] ['query']
    Name of the index type the new Channel should be using. If not specified this defaults to a simple integer index. Of the native types only a mesh "vertexFace" channel is different, using a "pair" index type.  In query mode, this flag can accept a value.

-----------------------------------------

scn   : scene           [boolean] ['query']
    Use this flag when you want to add metadata to the scene as a whole rather than to any individual nodes. If you use this flag and have nodes selected the nodes will be ignored and a warning will be displayed.

-----------------------------------------

six   : startIndex      [string] []
    The metadata is stored in a Stream, which is an indexed list. If you have mesh components selected then the metadata indices are implicit in the list of selected components. If you select only the node or scene then this flag may be used in conjunction with the endIndex flag to specify a range of indices from which to retrieve the metadata. It is an error to have the value of startIndex be greater than that of endIndex.  See also the index flag for an alternate way to specify multiple indices. This flag can only be used on index types that support a range (e.g. integer values - it makes no sense to request a range between two strings)  In query mode, this flag can accept a value.

-----------------------------------------

stn   : streamName      [string]
    Name of the metadata Stream. Depending on context it could be the name of a Stream to be created, or the name of the Stream to pass through the filter.  In query mode, this flag can accept a value.

    """

def hasMetadata(al=1,id=1,mn="string",cn="string",cht="string",eix="string",idx="string",idt="string",scn=1,six="string",stn="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hasMetadata.html



-----------------------------------------

hasMetadata is NOT undoable, NOT queryable, and NOT editable.

This command is used to query for the presence of metadata elements on a node,
components, or scene. The command works at all levels of metadata presence,
from the existence of any metadata at all on a node or scene right down to the
presence of metadata values set on a particular metadata Stream index. Filter
Flags

  * channelName \- Only look for metadata on one particular Channel type
  * streamName \- Only look for metadata on one particular named Stream. When used in conjunction with channelName then ignore Streams with a matching name but a different Channel type
  * index \- Only look for metadata on one or more specific Index values of a Stream. Requires use of the streamName flag. Does not require the indexType flag as that will be inferred by the streamName.
  * startIndex/endIndex \- Same as index but using an entire range of Index values rather than a single one
  * indexType \- Only look for metadata using a particular Index type. Can have its scope narrowed by other filter flags as well.
  * ignoreDefault \- Treat any metadata that still has the default value (e.g. 0 for numerics, "" for strings) the same as metadata that isn't present. This means that any metadata with default values will not be reported. It is useful for quickly finding values that you have changed. When this flag is set you can also use the memberName filter to narrow down the check to a particular member of the metadata Structure. Without that filter it will only skip over metadata where every member of the Structure has a non-default value.
  * memberName \- Only look at one particular Member in the metadata in a Structure. Only used when checking for non-default values as existence is based on the entire Structure, not any particular Member.

Operation Flags

  * normal mode \- Return True for every specified location containing metadata. This combines with the filter flags as follows:
    * no flag \- True if there is any metadata at all on the node or scene
    * channelName \- True if there is any metadata at all on the Channel with the given name
    * streamName \- True if there is any metadata at all on the Stream with the given name
    * index/startIndex/endIndex \- An array of booleans ordered the same as the natural ordering of the Index values (i.e. specifying index 3, 2, and 4 in that order will still return booleans in the order for indices 2,3,4) where True means that there is metadata assigned at that Index. This form is better suited with the asList modification since with that variation it is easier to tell exactly which indices have the metadata.
  * asList \- Adding this flag switches the return values from a single boolean or array of booleans to an array of strings indicating exactly which metadata elements have values. The return values of the command are changed to be the following:
    * no flag \- List of Channel names with metadata
    * channelName \- List of Stream names in the Channel with metadata
    * streamName \- List of Index values on the Stream with metadata
    * index/startIndex/endIndex \- List of Index values with metadata, restricted to the set of specified Index values.


-----------------------------------------


Return Value:

string[]  List of indexes in the filtered list which contain metadata    
boolean[]  List of answers to whether the specified item(s) have metadata


-----------------------------------------


Flags:

-----------------------------------------

al    : asList          [boolean] []
    Use this flag when you want to return string values indicating where the metadata lives rather than boolean values. See the command description for more details on what this flag will return.

-----------------------------------------

id    : ignoreDefault   [boolean] []
    Use this flag when you want to skip over any metadata that has only default values. i.e. the metadata may exist but it hasn't had a new value set yet (non-zero for numerics, non-empty strings, etc.) See the command description for more details on how this flag filters the search.

-----------------------------------------

mn    : memberName      [string] []
    Name of the Structure member being checked. The names of the members are set up in the Structure definition, either through the description passed in through the "dataStructure" command or via the API used to create that Structure. As the assignment of metadata is on a per-structure basis this flag only needs to be specified when querying for non-default values. If you query for non-default values and omit this flag then it checks that any of the members have a non-default value.

-----------------------------------------

cn    : channelName     [string] ['query']
    Filter the metadata selection to only recognize metadata belonging to the specified named Channel (e.g. "vertex"). This flag is ignored if the components on the selection list are being used to specify the metadata of interest.  In query mode, this flag can accept a value.

-----------------------------------------

cht   : channelType     [string] ['query']
    Obsolete - use the 'channelName' flag instead.  In query mode, this flag can accept a value.

-----------------------------------------

eix   : endIndex        [string] []
    The metadata is stored in a Stream, which is an indexed list. If you have mesh components selected then the metadata indices are implicit in the list of selected components. If you select only the node or scene then this flag may be used in conjunction with the startIndex flag to specify a range of indices from which to retrieve the metadata. It is an error to have the value of startIndex be greater than that of endIndex.  See also the index flag for an alternate way to specify multiple indices. This flag can only be used on index types that support a range (e.g. integer values - it makes no sense to request a range between two strings)  In query mode, this flag can accept a value.

-----------------------------------------

idx   : index           [string] ['query']
    In the typical case metadata is indexed using a simple integer value. Certain types of data may use other index types. e.g. a "vertexFace" component will use a "pair" index type, which is two integer values; one for the face ID of the component and the second for the vertex ID.  The index flag takes a string, formatted in the way the specified indexType requires. All uses of the index flag have the same indexType. If the type was not specified it is assumed to be a simple integer value.  In query mode, this flag can accept a value.

-----------------------------------------

idt   : indexType       [string] ['query']
    Name of the index type the new Channel should be using. If not specified this defaults to a simple integer index. Of the native types only a mesh "vertexFace" channel is different, using a "pair" index type.  In query mode, this flag can accept a value.

-----------------------------------------

scn   : scene           [boolean] ['query']
    Use this flag when you want to add metadata to the scene as a whole rather than to any individual nodes. If you use this flag and have nodes selected the nodes will be ignored and a warning will be displayed.

-----------------------------------------

six   : startIndex      [string] []
    The metadata is stored in a Stream, which is an indexed list. If you have mesh components selected then the metadata indices are implicit in the list of selected components. If you select only the node or scene then this flag may be used in conjunction with the endIndex flag to specify a range of indices from which to retrieve the metadata. It is an error to have the value of startIndex be greater than that of endIndex.  See also the index flag for an alternate way to specify multiple indices. This flag can only be used on index types that support a range (e.g. integer values - it makes no sense to request a range between two strings)  In query mode, this flag can accept a value.

-----------------------------------------

stn   : streamName      [string]
    Name of the metadata Stream. Depending on context it could be the name of a Stream to be created, or the name of the Stream to pass through the filter.  In query mode, this flag can accept a value.

    """

def manipOptions(q=1,esd=1,ese=1,fr=1,hs="float",hmc=1,hms=1,hsc=1,lp="float",ls="float",mm=1,pro="int",pho="int",ps="float",psh=1,rm="int",r=1,rah=1,rhs=1,s="float",ses=1,spr=1,sph=1,sdt="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipOptions.html



-----------------------------------------

manipOptions is undoable, queryable, and NOT editable.

Changes the global manipulator parameters


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

esd   : enableSmartDuplicate [boolean] ['query']
    Enables Shift-Duplicate option on t/r/s manips.

-----------------------------------------

ese   : enableSmartExtrude [boolean] ['query']
    Enables Shift-Extrude option on t/r/s manips.

-----------------------------------------

fr    : forceRefresh    [boolean] []
    Force a refresh if there is any deferred evaluation.

-----------------------------------------

hs    : handleSize      [float] ['query']
    Sets the maximum handles size in pixels, for small handles

-----------------------------------------

hmc   : hideManipOnCtrl [boolean] ['query']
    Hide transform manip when the Ctrl key is pressed.

-----------------------------------------

hms   : hideManipOnShift [boolean] ['query']
    Hide transform manip when the Shift key is pressed.

-----------------------------------------

hsc   : hideManipOnShiftCtrl [boolean] ['query']
    Hide transform manip when the Shift and Ctrl keys are both pressed.

-----------------------------------------

lp    : linePick        [float] ['query']
    Set the width of picking zone for long handles

-----------------------------------------

ls    : lineSize        [float] ['query']
    Set the width of long handles (drawn as lines)

-----------------------------------------

mm    : middleMouseRepositioning [boolean] ['query']
    Specify if the middle mouse should reposition

-----------------------------------------

pro   : pivotRotateHandleOffset [int] ['query']
    Set the offset of the pivot rotation handle.

-----------------------------------------

pho   : planeHandleOffset [int] ['query']
    Set the offset of the planar drag handles.

-----------------------------------------

ps    : pointSize       [float] ['query']
    Set the size of points (used to display previous states)

-----------------------------------------

psh   : preselectHighlight [boolean] ['query']
    Set whether manip handles should be highlighted when moving mouse.

-----------------------------------------

rm    : refreshMode     [int] ['query']
    Set the global refresh mode.

-----------------------------------------

r     : relative        [boolean] []
    All values are interpreted as multiplication factors instead of final values.

-----------------------------------------

rah   : rememberActiveHandle [boolean] ['query']
    Set whether manip handles should be remembered after selection change.

-----------------------------------------

rhs   : rememberActiveHandleAfterToolSwitch [boolean] ['query']
    Set whether manip handles should be remembered after manipulator change.

-----------------------------------------

s     : scale           [float] ['query']
    Global scaling factor of all manipulators

-----------------------------------------

ses   : showExtrudeSliders [boolean] ['query']
    Specify if the extrude sliders are to be shown on the manip

-----------------------------------------

spr   : showPivotRotateHandle [boolean] ['query']
    Toggles the visibility of the pivot rotation handle.

-----------------------------------------

sph   : showPlaneHandles [boolean] ['query']
    Toggles the visibility of the planar drag handles.

-----------------------------------------

sdt   : smartDuplicateType [int]
    Change Shift-Duplicate or Shift-Extrude between Copy and Instance on t/r/s manips.

    """

def manipPivot(q=1,mto="int",o="[float, float, float]",ov=1,pin=1,p="[float, float, float]",pv=1,r=1,ro=1,rp=1,rto="int",sto="int",so=1,sp=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/manipPivot.html



-----------------------------------------

manipPivot is undoable, queryable, and NOT editable.

Changes transform component pivot used by the move/rotate/scale manipulators.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

mto   : moveToolOri     [int] []
    Change move tool's axis orientation to the specified mode. This flag is the same as using "manipMoveContext -e -mode" on the Move tool except that this command is undoable.

-----------------------------------------

o     : ori             [[float, float, float]] ['query']
    Component pivot orientation in world-space.

-----------------------------------------

ov    : oriValid        [boolean] ['query']
    Returns true if component pivot orientation is valid.

-----------------------------------------

pin   : pinPivot        [boolean] ['query']
    Pin component pivot. Selection changes will not reset the pivot position/orientation when a custom pivot is set and pinning is on.

-----------------------------------------

p     : pos             [[float, float, float]] ['query']
    Component pivot position in world-space.

-----------------------------------------

pv    : posValid        [boolean] ['query']
    Returns true if component pivot position is valid.

-----------------------------------------

r     : reset           [boolean] []
    Clear the saved component pivot position and orientation.

-----------------------------------------

ro    : resetOri        [boolean] []
    Clear the saved component pivot orientation.

-----------------------------------------

rp    : resetPos        [boolean] []
    Clear the saved component pivot position.

-----------------------------------------

rto   : rotateToolOri   [int] []
    Change rotate tool's axis orientation to the specified mode. This flag is the same as using "manipRotateContext -e -mode" on the Rotate tool except that this command is undoable.

-----------------------------------------

sto   : scaleToolOri    [int] []
    Change scale tool's axis orientation to the specified mode. This flag is the same as using "manipScaleContext -e -mode" on the Scale tool except that this command is undoable.

-----------------------------------------

so    : snapOri         [boolean] ['query']
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

-----------------------------------------

sp    : snapPos         [boolean] ['query']
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

-----------------------------------------

v     : valid           [boolean]
    Returns true if component pivot position or orientation is valid.

    """

def polyAppend(q=1,e=1,a="[[, float, float, float, ]]",ch=1,ed="int",hl=1,n="string",p="[float, float, float]",s="int",tx="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyAppend.html



-----------------------------------------

polyAppend is undoable, queryable, and editable.

Appends a new face to the selected polygonal object. The first argument must
be a border edge. The new face will be automatically closed.  
Only works with one object selected.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : append          [[[, float, float, float, ]]] []
    Appends to the given polygon object. The append flag should be used multiple times to specify the edges, points, and holes that make up the new face that is being added. You may specify an edge by passing a single argument which will be the edges index. A point is specified with three arguments which are the coordinates of the point in the objects local space. Pass no arguments indicates that the values which follow shall specify a hole. In Python, pass an empty tuple to specify no arguments.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ed    : edge            [int] []
    Adds the given edge of the selected object to the new face. This edge must be a border, which will be then shared by the new face and the neighboring one. The new face is oriented according to the orientation of the given edge(s). Note that this flag should be avoided in Python. You may use the "append" flag instead and pass one argument.

-----------------------------------------

hl    : hole            [boolean] []
    Add a hole. The following points and edges will define a hole. Note that this flag should be avoided in Python. You may use the "append" flag instead and pass an empty tuple ().

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

p     : point           [[float, float, float]] []
    Adds a new point to the new face. Coordinates of free points are given in the local object reference. Note that this flag should be avoided in Python. You may use the "append" flag instead and pass three arguments.

-----------------------------------------

s     : subdivision     [int] ['query', 'edit']
    This flag specifies the level of subdivisions. Automatically subdivides new edges into the given number of edges. Existing edges cannot be subdivided.   C : Default is 1 (no subdivision).   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [int]
    Specifies how new faces are mapped.   0 - None; 1 - Normalize; 2 - Unitize   C: Default is 0 (no mapping).   Q: When queried, this flag returns an int

    """

def polyAppendVertex(q=1,e=1,a="[[, float, float, float, ]]",ch=1,h=1,n="string",p="[float, float, float]",tx="int",v="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyAppendVertex.html



-----------------------------------------

polyAppendVertex is undoable, queryable, and editable.

Appends a new face to the selected polygonal object. The direction of the
normal is given by the vertex order: the face normal points towards the user
when the vertices rotate counter clockwise. Note that holes must be described
in the opposite direction.  
Only works with one object selected.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : append          [[[, float, float, float, ]]] []
    Append a vertex or a point to the selected object, or mark the start of a hole.   This flag may also be used in place of the "hole", "vertex" and "point" flags. If no argument is passed to the "append" flag, then it marks the beginning of a hole (use an empty tuple in Python '()'). If one argument is passed, then the argument is considered to be an index into the vertices of the selected object, as with the "vertex" flag. If three arguments are passed, then it is interpreted as the coordinates of a new point which will be inserted, as with the "point" flag.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

h     : hole            [boolean] []
    Add a hole. The following points and edges will define a hole. Note that this flag should be avoided in Python. You may use the "append" flag instead and pass an empty tuple '()' to specify the start of a hole.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

p     : point           [[float, float, float]] []
    Adds a new point to the new face. Coordinates of free points are given in the local object reference. Note that this flag should be avoided in Python. You may use the "append" flag instead and pass three arguments.

-----------------------------------------

tx    : texture         [int] ['query', 'edit']
    Specifies how new faces are mapped.   0 - None; 1 - Normalize; 2 - Unitize   C: Default is 0 (no mapping).   Q: When queried, this flag returns an int

-----------------------------------------

v     : vertex          [int]
    Adds the given vertex of the selected object to the new face. Note that this flag should be avoided in Python. You may use the "append" flag instead and pass one argument.

    """

def polyAutoProjection(q=1,e=1,lm="int",pvt="[linear, linear, linear]",pvx="linear",pvy="linear",pvz="linear",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",s="[float, float, float]",sx="float",sy="float",sz="float",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",cch=1,ch=1,cm=1,ibd=1,l="int",n="string",nds="int",o="int",ps="float",p="int",pb=1,sc="int",si=1,uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyAutoProjection.html



-----------------------------------------

polyAutoProjection is undoable, queryable, and editable.

Projects a map onto an object, using several orthogonal projections
simultaneously.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

lm    : layoutMethod    [int] ['query', 'edit']
    Set which layout method to use:   0 Block Stacking.   1 Shape Stacking.

-----------------------------------------

pvt   : pivot           [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the pivot for scaling and rotation.   C: Default is 0.0 0.0 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

pvx   : pivotX          [linear] ['query', 'edit']
    This flag specifies the X pivot for scaling and rotation.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pvy   : pivotY          [linear] ['query', 'edit']
    This flag specifies the Y pivot for scaling and rotation.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pvz   : pivotZ          [linear] ['query', 'edit']
    This flag specifies the Z pivot for scaling and rotation.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    This flag specifies the rotation angles around X, Y, Z.   C: Default is 0.0 0.0 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    This flag specifies the rotation angle around X.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    This flag specifies the rotation angle around Y.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    This flag specifies the rotation angle around Z.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    This flag specifies the scaling vector.   C: Default is 1.0 1.0 1.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

sx    : scaleX          [float] ['query', 'edit']
    This flag specifies X for scaling vector.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

sy    : scaleY          [float] ['query', 'edit']
    This flag specifies Y for scaling vector.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

sz    : scaleZ          [float] ['query', 'edit']
    This flag specifies Z for scaling vector.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

t     : translate       [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the translation vector.   C: Default is 0.0 0.0 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

tx    : translateX      [linear] ['query', 'edit']
    This flag specifies the X translation vector.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ty    : translateY      [linear] ['query', 'edit']
    This flag specifies the Y translation vector.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

tz    : translateZ      [linear] ['query', 'edit']
    This flag specifies the Z translation vector.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] []
    Set to true if a new map should be created

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    Set to true if the new node created should inserted before any deformer nodes.

-----------------------------------------

l     : layout          [int] ['query', 'edit']
    What layout algorithm should be used:   0 UV pieces are set to no layout.   1 UV pieces are aligned along the U axis.   2 UV pieces are moved in a square shape.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : optimize        [int] ['query', 'edit']
    Use two different flavors for the cut generation.   0 Every face is assigned to the best plane. This optimizes the map distortion.   1 Small UV pieces are incorporated into larger ones, when the extra distortion introduced is reasonable. This tends to produce fewer UV pieces.

-----------------------------------------

ps    : percentageSpace [float] ['query', 'edit']
    When layout is set to square, this value is a percentage of the texture area which is added around each UV piece. It can be used to ensure each UV piece uses different pixels in the texture.   Maximum value is 5 percent.

-----------------------------------------

p     : planes          [int] ['query', 'edit']
    Number of intermediate projections used. Valid numbers are 4, 5, 6, 8, and 12.   C: Default is 6.

-----------------------------------------

pb    : projectBothDirections [boolean] ['query', 'edit']
    This flag specifies which reference to use. If "on" : projections are mirrored on directly opposite faces. If "off" : projections are not mirrored on opposite faces.   C: Default is "off".   Q: When queried, this flag returns an integer.

-----------------------------------------

sc    : scaleMode       [int] ['query', 'edit']
    How to scale the pieces, after projections:   0 No scale is applied.   1 Uniform scale to fit in unit square.   2 Non proportional scale to fit in unit square.

-----------------------------------------

si    : skipIntersect   [boolean] ['query', 'edit']
    When on, self intersection of UV pieces are not tested. This makes the projection faster and produces fewer pieces, but may lead to overlaps in UV space.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyAverageNormal(azn=1,d="float",pon=1,prn=1,xyz="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyAverageNormal.html



-----------------------------------------

polyAverageNormal is undoable, NOT queryable, and NOT editable.

Set normals of vertices or vertex-faces to an average value when the vertices
within a given threshold. First, it sorts out the containing edges, and set
them to be soft, if it is possible, so to let the normals appear to be
"merged". The remained components then are sorted into lumps where vertices in
each lump are within the given threshold. For all vertices and vertex-faces,
set their normals to the average normal in the lump. Selected vertices may or
may not on the same object. If objects are selected, it is assumed that all
vertices are selected. If edges or faces are selected, it is assumed that the
related vertex-faces are selected.


-----------------------------------------


Return Value:

string  of the node name.


-----------------------------------------


Flags:

-----------------------------------------

azn   : allowZeroNormal [boolean] []
    Specifies whether to allow zero normals to be created. By default it is false. If it is false, replaceNormal is needed.

-----------------------------------------

d     : distance        [float] []
    Specifies the distance threshold. All vertices within the threshold are considered when computing an average normal. By default it is 0.0.

-----------------------------------------

pon   : postnormalize   [boolean] []
    Specifies whether to normalize the resulting normals. By default it is true.

-----------------------------------------

prn   : prenormalize    [boolean] []
    Specifies whether to normalize the normals before averaging. By default it is true.

-----------------------------------------

xyz   : replaceNormalXYZ [[float, float, float]]
    If the allowZeroNormal is false, this value is used to replace the zero normals. By default it is (1, 0, 0).

    """

def polyAverageVertex(q=1,e=1,cch=1,ch=1,i="int",n="string",nds="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyAverageVertex.html



-----------------------------------------

polyAverageVertex is undoable, queryable, and editable.

Moves the selected vertices of a polygonal object to round its shape.
Translate, move, rotate or scale vertices.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

i     : iterations      [int] ['query', 'edit']
    Number of rounding steps.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyBevel(q=1,e=1,at="float",af=1,cch=1,ch=1,mvt="linear",mv=1,ma="float",n="string",nds="int",o="linear",oaf=1,r="float",sg="int",sa="float",sn=1,com=1,ua="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyBevel.html



-----------------------------------------

polyBevel is undoable, queryable, and editable.

Bevel edges.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : angleTolerance  [float] ['query', 'edit']
    Angular tolerance for creation of extra triangles Note this attribute is for compatability only and should not be modified in Maya 7.0 files   Default: 20.0

-----------------------------------------

af    : autoFit         [boolean] ['query', 'edit']
    If autoFit is on, it computes a smooth roundness : new facets round off a smooth angle.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

mvt   : mergeVertexTolerance [linear] ['query', 'edit']
    Tolerance within which to merge vertices   Default: 0.0

-----------------------------------------

mv    : mergeVertices   [boolean] ['query', 'edit']
    Merge vertices within a tolerance   Default: false

-----------------------------------------

ma    : miteringAngle   [float] ['query', 'edit']
    Miter faces that have angles less than this value   Default: 0.0

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : offset          [linear] ['query', 'edit']
    The offset for bevel.   Default: 0.2

-----------------------------------------

oaf   : offsetAsFraction [boolean] ['query', 'edit']
    If on, the offset value is treated as a fraction between zero and one.   Default: false

-----------------------------------------

r     : roundness       [float] ['query', 'edit']
    The roundness of bevel, it is taken into account when autoFit is off.   Default: 0.5

-----------------------------------------

sg    : segments        [int] ['query', 'edit']
    The number of segments used for beveling.   Default: 1

-----------------------------------------

sa    : smoothingAngle  [float] ['query', 'edit']
    Create new edges as hard edges if the angle between adjacent faces exceeds this value   Default: 0.0

-----------------------------------------

sn    : subdivideNgons  [boolean] ['query', 'edit']
    Subdivide new faces with more than 4 edges   Default: false

-----------------------------------------

com   : useLegacyBevelAlgorithm [boolean] ['query', 'edit']
    If on, bevel is done the way maya 2014 did   Default: false

-----------------------------------------

ua    : uvAssignment    [int] ['query', 'edit']
    Technique used to compute UVs on new faces 0 computes new UVs by projecting along surface normal of original mesh onto new mesh 1 computes new UVs by projecting along surface normal of new mesh onto original mesh   Default: 0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyBevel3(q=1,e=1,at="float",af=1,cch=1,c=1,ch=1,d="float",fn=1,mvt="linear",mv=1,mia="int",m="int",ma="float",n="string",nds="int",o="linear",oaf=1,r="float",sg="int",sa="float",ua="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyBevel3.html



-----------------------------------------

polyBevel3 is undoable, queryable, and editable.

Bevel edges.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : angleTolerance  [float] ['query', 'edit']
    Angular tolerance for creation of extra triangles Note this attribute is for compatability only and should not be modified in Maya 7.0 files   Default: 20.0

-----------------------------------------

af    : autoFit         [boolean] ['query', 'edit']
    If autoFit is on, it computes a smooth roundness : new facets round off a smooth angle.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

c     : chamfer         [boolean] ['query', 'edit']
    If chamfer is on, the surface is smoothed out at bevels. When it is off, the shape of the surface remains the same.   Default: true

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

d     : depth           [float] ['query', 'edit']
    The depth of bevel. One means a smooth surface, -1 means maximum depth.   Default: 1.0

-----------------------------------------

fn    : fillNgons       [boolean] ['query', 'edit']
    Subdivide new faces with more than 4 edges   Default: false

-----------------------------------------

mvt   : mergeVertexTolerance [linear] ['query', 'edit']
    Tolerance within which to merge vertices   Default: 0.0

-----------------------------------------

mv    : mergeVertices   [boolean] ['query', 'edit']
    Merge vertices within a tolerance   Default: false

-----------------------------------------

mia   : miterAlong      [int] ['query', 'edit']
    Controls in which direction new vertices should we offseted.   Default: 0

-----------------------------------------

m     : mitering        [int] ['query', 'edit']
    Controls how the topology should look like at corners.   Default: 0

-----------------------------------------

ma    : miteringAngle   [float] ['query', 'edit']
    Miter faces that have angles less than this value   Default: 0.0

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : offset          [linear] ['query', 'edit']
    The offset for bevel.   Default: 0.2

-----------------------------------------

oaf   : offsetAsFraction [boolean] ['query', 'edit']
    If on, the offset value is treated as a fraction between zero and one.   Default: false

-----------------------------------------

r     : roundness       [float] ['query', 'edit']
    The roundness of bevel, it is taken into account when autoFit is off.   Default: 0.5

-----------------------------------------

sg    : segments        [int] ['query', 'edit']
    The number of segments used for beveling.   Default: 1

-----------------------------------------

sa    : smoothingAngle  [float] ['query', 'edit']
    Create new edges as hard edges if the angle between adjacent faces exceeds this value   Default: 0.0

-----------------------------------------

ua    : uvAssignment    [int] ['query', 'edit']
    Technique used to compute UVs on new faces 0 computes new UVs by projecting along surface normal of original mesh onto new mesh 1 computes new UVs by projecting along surface normal of new mesh onto original mesh   Default: 0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyBlendColor(q=1,e=1,bcn="string",bfn="int",bwa="float",bwb="float",bwc="float",bwd="float",cch=1,ch=1,dst="string",n="string",nds="int",src="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyBlendColor.html



-----------------------------------------

polyBlendColor is undoable, queryable, and editable.

Takes two color sets and blends them together into a third specified color
set.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bcn   : baseColorName   [string] ['query', 'edit']
    Name of the color set to blend from

-----------------------------------------

bfn   : blendFunc       [int] ['query', 'edit']
    Type of blending function to use

-----------------------------------------

bwa   : blendWeightA    [float] ['query', 'edit']
    Blend weight for linear and bilinear blending functions

-----------------------------------------

bwb   : blendWeightB    [float] ['query', 'edit']
    Blend weight for bilinear and channel blending functions

-----------------------------------------

bwc   : blendWeightC    [float] ['query', 'edit']
    Blend weight for channel functions

-----------------------------------------

bwd   : blendWeightD    [float] ['query', 'edit']
    Blend weight for channel functions

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

dst   : dstColorName    [string] ['query', 'edit']
    Name of the color set to copy to

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

src   : srcColorName    [string]
    Name of the color set to copy from

    """

def polyBlindData(e=1,at="string",bnd="string",bd=1,delete=1,dbd="float",lid="int64",ind="int",ldn="string",res=1,rst=1,sh=1,sdn="string",sd="string",id="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyBlindData.html



-----------------------------------------

polyBlindData is undoable, NOT queryable, and editable.

Command creates blindData types (basically creates an instance of
TdnPolyBlindData). When used with the query flag, it returns the data types
that define this blindData type. This command is to be used create a blindData
node *and* to edit the same.. The associationType flag *has* to be specified
at all times.. This is because if an instance of the specified BD typeId
exists in the history chain but if the associationType is not the same, then a
new polyBlindData node is created.. For object level blind data, only the
object itself must be specified. A new compound attribute BlindDataNNNN will
be created on the object. Blind data attribute names must be unique across
types for object level blind data. So, the command will require the following
to be specified: \- typeId, \- associationType \- longDataName or
shortDataName of data being edited. \- The actual data being specified. \- The
components that this data is to be attached to.


-----------------------------------------


Return Value:

string  Name of nodes created


-----------------------------------------


Flags:

-----------------------------------------

at    : associationType [string] ['edit']
    Specifies the dataTypes that are part of BlindData node being created. Allowable associations are "object" for any object, and "vertex" "edge" and "face" for mesh objects. Other associations for other geometry types may be added.

-----------------------------------------

bnd   : binaryData      [string] ['edit']
    Specifies the data type is a binary data value

-----------------------------------------

bd    : booleanData     [boolean] ['edit']
    Specifies the data type is a boolean logic value

-----------------------------------------

delete : delete          [boolean] ['edit']
    Specifies that this will remove the blind data if found

-----------------------------------------

dbd   : doubleData      [float] ['edit']
    Specifies the data type is a floating point double value

-----------------------------------------

lid   : int64Data       [int64] ['edit']
    Specifies the data type is an 64-bit integer value

-----------------------------------------

ind   : intData         [int] ['edit']
    Specifies the data type is an integer value

-----------------------------------------

ldn   : longDataName    [string] ['edit']
    Specifies the long name of the data that is being modified by this command.

-----------------------------------------

res   : rescan          [boolean] ['edit']
    Enables a rescan of blind data nodes for cached information

-----------------------------------------

rst   : reset           [boolean] ['edit']
    Specifies that this command will reset the given attribute to default value

-----------------------------------------

sh    : shape           [boolean] ['edit']
    For object association only, apply blind data to the shape(s) below this node instead of the node itself

-----------------------------------------

sdn   : shortDataName   [string] ['edit']
    Specifies the short name of the data that is being modified by this command.

-----------------------------------------

sd    : stringData      [string] ['edit']
    Specifies the data type is a string value

-----------------------------------------

id    : typeId          [int]
    Specifies the typeId of the BlindData type being created

    """

def polyBoolOp(q=1,e=1,fat="linear",op="int",pcr=1,uth=1,vdt="linear",cch=1,muv="int",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyBoolOp.html



-----------------------------------------

polyBoolOp is undoable, queryable, and editable.

This command creates a new poly as the result of a boolean operation on input
polys : union, intersection, difference.  
Only for difference, the order of the selected objects is important :  
result = object1 - object2.  
If no objects are specified in the command line, then the objects from the
active list are used.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

fat   : faceAreaThreshold [linear] ['query', 'edit']
    Area threshold to determine whether faces should be collapsed before boolean. Attribute is ignored unless useThresholds is set to true   Default: 0.0001

-----------------------------------------

op    : operation       [int] ['query', 'edit']
    Boolean operation type. 1=union, 2=difference, 3=intersection. Default type is union.   Default: kBoolOpUnion

-----------------------------------------

pcr   : preserveColor   [boolean] ['query', 'edit']
    If true, boolean op will compute color for the new mesh. If false, the new mesh won't have any color set.   Default: false

-----------------------------------------

uth   : useThresholds   [boolean] ['query', 'edit']
    If true, merge vertices with separations less then vertexDistanceThreshold and collapse faces with areas less then faceAreaThreshold. If false, do not merge vertices or collapse faces   Default: false

-----------------------------------------

vdt   : vertexDistanceThreshold [linear] ['query', 'edit']
    Tolerance to determine whether vertices (and edges) should be merged before boolean operation is applied. Attribute is ignored unless useThresholds is set to true   Default: 0.001

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

muv   : mergeUVSets     [int] ['query', 'edit']
    Specify how UV sets will be merged on the output mesh.    * 0 = "No Merge": Each UV set on each mesh will become a new UV set in the output.   * 1 = "Merge By Name": UV sets with the same name will be merged.   * 2 = "Merge By UV Links": UV sets will be merged so that UV linking on the input meshes continues to work.  The default is merge by name.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyBridgeEdge(q=1,e=1,bo="int",cch=1,ch=1,ctp="int",dv="int",inc="name",n="string",nds="int",sma="angle",sv1="int",sv2="int",tp="float",cfv="float",ci="int",cp="float",twt="angle",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyBridgeEdge.html



-----------------------------------------

polyBridgeEdge is undoable, queryable, and editable.

Bridges two sets of edges.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bo    : bridgeOffset    [int] ['query', 'edit']
    Add offset to which vertices are connected.   Default: 0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ctp   : curveType       [int] ['query', 'edit']
    Format: 0 - Linear, 1 - Blend, 2 - Curve   Default: TdnpolyBridgeEdge::Linear

-----------------------------------------

dv    : divisions       [int] ['query', 'edit']
    The number of subdivisions in the bridging faces (resulting in (divisions+1) row of faces).   Default: 1

-----------------------------------------

inc   : inputCurve      [name] []
    This flag specifies the name of the curve to be used as input for the operation.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

sma   : smoothingAngle  [angle] ['query', 'edit']
    Angle below which new edges will be smoothed   Default: kPi/6.0

-----------------------------------------

sv1   : startVert1      [int] ['query', 'edit']
    The start vertex from the first set of edges   Default: -1

-----------------------------------------

sv2   : startVert2      [int] ['query', 'edit']
    The start vertex from the second set of edges   Default: -1

-----------------------------------------

tp    : taper           [float] ['query', 'edit']
    Taper or Scale along the extrusion path   Default: 1.0

-----------------------------------------

cfv   : taperCurve_FloatValue [float] ['query', 'edit']
    Value for taperCurve; Curve control for taper along extrusion Using this curve, the taper along extrusion can be changed from a simple linear scaling to custom scaling along the extrusion path.

-----------------------------------------

ci    : taperCurve_Interp [int] ['query', 'edit']
    Interpolation type for taperCurve; Curve control for taper along extrusion Using this curve, the taper along extrusion can be changed from a simple linear scaling to custom scaling along the extrusion path.

-----------------------------------------

cp    : taperCurve_Position [float] ['query', 'edit']
    Position for taperCurve; Curve control for taper along extrusion Using this curve, the taper along extrusion can be changed from a simple linear scaling to custom scaling along the extrusion path.

-----------------------------------------

twt   : twist           [angle] ['query', 'edit']
    Twist or Rotation along the extrusion path   Default: 0.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyCacheMonitor(chv=1,nm="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCacheMonitor.html



-----------------------------------------

polyCacheMonitor is NOT undoable, NOT queryable, and NOT editable.

When the cacheInput attribute has a positive value the midModifier node caches
the output mesh improving performance in computations of downstream nodes.
When the counter has a zero value the midModifier releases the cached data.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

chv   : cacheValue      [boolean] []
    Flag to indicate whether the node's cache counter should be incremented or decremented. True increments the counter, false decrements the counter.

-----------------------------------------

nm    : nodeName        [string]
    Name of the node whose cache counter needs to be changed.

    """

def polyCanBridgeEdge():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCanBridgeEdge.html



-----------------------------------------

polyCanBridgeEdge is undoable, NOT queryable, and NOT editable.

Returns true if the specified poly edges can be bridged using polyBridgeEdge.


-----------------------------------------


Return Value:

boolean  Success or Failure.
    """

def polyCBoolOp(q=1,e=1,cls="int",fat="linear",op="int",pcr=1,ucb=1,uth=1,vdt="linear",cch=1,muv="int",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCBoolOp.html



-----------------------------------------

polyCBoolOp is undoable, queryable, and editable.

This command creates a new poly as the result of a boolean operation on input
polys : union, intersection, difference.  
Only for difference, the order of the selected objects is important :  
result = object1 - object2.  
If no objects are specified in the command line, then the objects from the
active list are used.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cls   : classification  [int] ['query', 'edit']
    Changes how intersections of open and closed manifolds are treated. 1 for "Edge", 2 for "Normal".

-----------------------------------------

fat   : faceAreaThreshold [linear] ['query', 'edit']
    Area threshold to determine whether faces should be collapsed before boolean. Attribute is ignored unless useThresholds is set to true   Default: 0.0001

-----------------------------------------

op    : operation       [int] ['query', 'edit']
    Boolean operation type. 1=union, 2=difference, 3=intersection. Default type is union.   Default: kBoolOpUnion

-----------------------------------------

pcr   : preserveColor   [boolean] ['query', 'edit']
    If true, boolean op will compute color for the new mesh. If false, the new mesh won't have any color set.   Default: false

-----------------------------------------

ucb   : useCarveBooleans [boolean] ['query', 'edit']
    If true, use the Carve Boolean library

-----------------------------------------

uth   : useThresholds   [boolean] ['query', 'edit']
    If true, merge vertices with separations less then vertexDistanceThreshold and collapse faces with areas less then faceAreaThreshold. If false, do not merge vertices or collapse faces   Default: false

-----------------------------------------

vdt   : vertexDistanceThreshold [linear] ['query', 'edit']
    Tolerance to determine whether vertices (and edges) should be merged before boolean operation is applied. Attribute is ignored unless useThresholds is set to true   Default: 0.001

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

muv   : mergeUVSets     [int] ['query', 'edit']
    Specify how UV sets will be merged on the output mesh.    * 0 = "No Merge": Each UV set on each mesh will become a new UV set in the output.   * 1 = "Merge By Name": UV sets with the same name will be merged.   * 2 = "Merge By UV Links": UV sets will be merged so that UV linking on the input meshes continues to work.  The default is merge by name.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyCheck(edge=1,f=1,fo=1,of="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCheck.html



-----------------------------------------

polyCheck is undoable, NOT queryable, and NOT editable.

Dumps a description of internal memory representation of poly objects.  
If no objects are specified in the command line, the objects from the active
list are used.  
Default behaviour is to print only a summary. Use the flags above to get more
details on a specific part of the object.


-----------------------------------------


Return Value:

int  The number of errors.


-----------------------------------------


Flags:

-----------------------------------------

e     : edge            [boolean] []
    Check edge descriptions. If no flag is set, a complete check is performed.

-----------------------------------------

f     : face            [boolean] []
    Check face descriptions. If no flag is set, a complete check is performed.

-----------------------------------------

fo    : faceOffset      [boolean] []
    Check face offset descriptions. If no flag is set, a complete check is performed.

-----------------------------------------

of    : openFile        [string]
    Opens a file that contains a poly description, as dumped out by the debug commands.

    """

def polyChipOff(q=1,e=1,att="float",cch=1,ch=1,dup=1,ga="float",g="[linear, linear, linear]",gx="linear",gy="linear",gz="linear",kft=1,xft=1,lc="int",ld="[linear, linear, linear]",ldx="linear",ldy="linear",ldz="linear",lr="[angle, angle, angle]",lrx="angle",lry="angle",lrz="angle",ls="[float, float, float]",lsx="float",lsy="float",lsz="float",lt="[linear, linear, linear]",ltx="linear",lty="linear",ltz="linear",mx="linear",my="linear",mz="linear",m="[linear, linear, linear]",n="string",nds="int",off="float",pvt="[linear, linear, linear]",pvx="linear",pvy="linear",pvz="linear",ran="float",s="[float, float, float]",sx="float",sy="float",sz="float",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",w="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyChipOff.html



-----------------------------------------

polyChipOff is undoable, queryable, and editable.

Extract facets. Faces can be extracted separately or together, and
manipulations can be performed either in world or object space.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attraction      [float] ['query', 'edit']
    Attraction, related to magnet. The range is [-2.0, 2.0].   Default: 0.0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

dup   : duplicate       [boolean] ['query', 'edit']
    If "on", facets are duplicated, otherwise original facets are removed.   C: Default is "on".   Q: When queried, this flag returns an int.

-----------------------------------------

ga    : gain            [float] ['query', 'edit']
    Gain factor per component. Can be painted using Artisan.   Default: 1.0

-----------------------------------------

g     : gravity         [[linear, linear, linear]] ['query', 'edit']
    The gravity vector.   Default: 0.0, -1.0, 0.0

-----------------------------------------

gx    : gravityX        [linear] ['query', 'edit']
    Gravity X coord.

-----------------------------------------

gy    : gravityY        [linear] ['query', 'edit']
    Gravity Y coord.

-----------------------------------------

gz    : gravityZ        [linear] ['query', 'edit']
    Gravity Z coord.

-----------------------------------------

kft   : keepFacesTogether [boolean] ['query', 'edit']
    How to extrude edges. If "on", extruded faces produced from the edges being extruded will be kept together. Otherwise they are pulled independently.   Default: true

-----------------------------------------

xft   : keepFacetTogether [boolean] ['query', 'edit']
    How to extrude edges. If "on", extruded faces produced from the edges being extruded will be kept together. Otherwise they are pulled independently.   Default: true

-----------------------------------------

lc    : localCenter     [int] ['query', 'edit']
    Local center on the edge : 0=Middle point, 1=Start point, 2=End point.   Default: 0

-----------------------------------------

ld    : localDirection  [[linear, linear, linear]] ['query', 'edit']
    Direction to determine X axis for local space.   Default: 1.0, 0.0, 0.0

-----------------------------------------

ldx   : localDirectionX [linear] ['query', 'edit']
    X coord of the X axis.

-----------------------------------------

ldy   : localDirectionY [linear] ['query', 'edit']
    Y coord of the X axis.

-----------------------------------------

ldz   : localDirectionZ [linear] ['query', 'edit']
    Z coord of the X axis.

-----------------------------------------

lr    : localRotate     [[angle, angle, angle]] ['query', 'edit']
    The local rotations.   Default: 0.0, 0.0, 0.0

-----------------------------------------

lrx   : localRotateX    [angle] ['query', 'edit']
    Local rotate X coord. The range is [0, 360].

-----------------------------------------

lry   : localRotateY    [angle] ['query', 'edit']
    Local rotate Y coord. The range is [0, 360].

-----------------------------------------

lrz   : localRotateZ    [angle] ['query', 'edit']
    Local rotate Z coord : Rotation along the normal. The range is [0, 360].

-----------------------------------------

ls    : localScale      [[float, float, float]] ['query', 'edit']
    Local Scale.   Default: 1.0, 1.0, 1.0

-----------------------------------------

lsx   : localScaleX     [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

lsy   : localScaleY     [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

lsz   : localScaleZ     [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

lt    : localTranslate  [[linear, linear, linear]] ['query', 'edit']
    Local translate.   Default: 0.0, 0.0, 0.0

-----------------------------------------

ltx   : localTranslateX [linear] ['query', 'edit']
    Local translation X coord.

-----------------------------------------

lty   : localTranslateY [linear] ['query', 'edit']
    Local translation Y coord.

-----------------------------------------

ltz   : localTranslateZ [linear] ['query', 'edit']
    Local translation Z coord : Move along the normal.

-----------------------------------------

mx    : magnX           [linear] ['query', 'edit']
    Magnet X coord.

-----------------------------------------

my    : magnY           [linear] ['query', 'edit']
    Magnet Y coord.

-----------------------------------------

mz    : magnZ           [linear] ['query', 'edit']
    Magnet Z coord.

-----------------------------------------

m     : magnet          [[linear, linear, linear]] ['query', 'edit']
    The magnet vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

off   : offset          [float] ['query', 'edit']
    Local offset. Faces are moved this distance towards the inside of the face.   Default: 0.0

-----------------------------------------

pvt   : pivot           [[linear, linear, linear]] ['query', 'edit']
    The pivot for scaling and rotation.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pvx   : pivotX          [linear] ['query', 'edit']
    Pivot X coord.

-----------------------------------------

pvy   : pivotY          [linear] ['query', 'edit']
    Pivot Y coord.

-----------------------------------------

pvz   : pivotZ          [linear] ['query', 'edit']
    Pivot Z coord.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    Random value for all parameters.   Default: 0.0

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    Scaling vector.   Default: 1.0, 1.0, 1.0

-----------------------------------------

sx    : scaleX          [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

sy    : scaleY          [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

sz    : scaleZ          [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

t     : translate       [[linear, linear, linear]] ['query', 'edit']
    Translation vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

tx    : translateX      [linear] ['query', 'edit']
    Translation X coord.

-----------------------------------------

ty    : translateY      [linear] ['query', 'edit']
    Translation Y coord.

-----------------------------------------

tz    : translateZ      [linear] ['query', 'edit']
    Translation Z coord.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    The weight, related to gravity.   Default: 0.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyCircularize(q=1,e=1,al="int",cch=1,ch=1,cc=1,ed=1,inc="name",n="string",nds="int",nor="int",ro="float",sa="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCircularize.html



-----------------------------------------

polyCircularize is undoable, queryable, and editable.

Mirror all the faces of the selected object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : alignment       [int] ['query', 'edit']
    How the circle should be oriented relative to the surface   Default: 0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cc    : createCurve     [boolean] []
    If true then the operation can create a curve.

-----------------------------------------

ed    : evenlyDistribute [boolean] ['query', 'edit']
    Should the point be evenly distributed around the circle   Default: true

-----------------------------------------

inc   : inputCurve      [name] []
    This flag specifies the name of the curve to be used as input for the operation.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nor   : normalOrientation [int] ['query', 'edit']
    What calculation to use to get circle plane normal   Default: 0

-----------------------------------------

ro    : radialOffset    [float] ['query', 'edit']
    The amount the circle points should be translated along radius   Default: 0.0

-----------------------------------------

sa    : smoothingAngle  [float] ['query', 'edit']
    The angle that decides which resulting faces are hard or soft   Default: 30.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyCircularizeEdge(q=1,e=1,al="int",cch=1,ch=1,cc=1,ed=1,inc="name",n="string",nds="int",nor="int",ro="float",sa="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCircularizeEdge.html



-----------------------------------------

polyCircularizeEdge is undoable, queryable, and editable.

Mirror all the faces of the selected object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : alignment       [int] ['query', 'edit']
    How the circle should be oriented relative to the surface   Default: 0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cc    : createCurve     [boolean] []
    If true then the operation can create a curve.

-----------------------------------------

ed    : evenlyDistribute [boolean] ['query', 'edit']
    Should the point be evenly distributed around the circle   Default: true

-----------------------------------------

inc   : inputCurve      [name] []
    This flag specifies the name of the curve to be used as input for the operation.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nor   : normalOrientation [int] ['query', 'edit']
    What calculation to use to get circle plane normal   Default: 0

-----------------------------------------

ro    : radialOffset    [float] ['query', 'edit']
    The amount the circle points should be translated along radius   Default: 0.0

-----------------------------------------

sa    : smoothingAngle  [float] ['query', 'edit']
    The angle that decides which resulting faces are hard or soft   Default: 30.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyCircularizeFace(q=1,e=1,al="int",cch=1,ch=1,cc=1,ed=1,inc="name",n="string",nds="int",nor="int",ro="float",sa="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCircularizeFace.html



-----------------------------------------

polyCircularizeFace is undoable, queryable, and editable.

Mirror all the faces of the selected object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : alignment       [int] ['query', 'edit']
    How the circle should be oriented relative to the surface   Default: 0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cc    : createCurve     [boolean] []
    If true then the operation can create a curve.

-----------------------------------------

ed    : evenlyDistribute [boolean] ['query', 'edit']
    Should the point be evenly distributed around the circle   Default: true

-----------------------------------------

inc   : inputCurve      [name] []
    This flag specifies the name of the curve to be used as input for the operation.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nor   : normalOrientation [int] ['query', 'edit']
    What calculation to use to get circle plane normal   Default: 0

-----------------------------------------

ro    : radialOffset    [float] ['query', 'edit']
    The amount the circle points should be translated along radius   Default: 0.0

-----------------------------------------

sa    : smoothingAngle  [float] ['query', 'edit']
    The angle that decides which resulting faces are hard or soft   Default: 30.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyClean(q=1,e=1,cch=1,ce=1,cpm=1,cuv=1,cv=1,ch=1,fzn=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyClean.html



-----------------------------------------

polyClean is undoable, queryable, and editable.

polyClean will attempt to remove components that are invalid in the
description of a poly mesh.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ce    : cleanEdges      [boolean] ['query', 'edit']
    If true, the operation will look for and delete edges that are not associated with any face in the mesh.

-----------------------------------------

cpm   : cleanPartialUVMapping [boolean] ['query', 'edit']
    If true, the operation will look for any faces on the mesh that do not have complete UV mapping. Maya requires that all vertices that make up a mesh face have valid UV data associated with them, or that none of the vertices withing the face have associated UVs.

-----------------------------------------

cuv   : cleanUVs        [boolean] ['query', 'edit']
    If true, the operation will look for and delete UVs that are not associated with any face in the mesh.

-----------------------------------------

cv    : cleanVertices   [boolean] ['query', 'edit']
    If true, the operation will look for and delete vertices that are not associated with any face in the mesh.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

fzn   : frozen          [boolean] ['query', 'edit']
    Toggle frozen state for a particular node to keep current evaluation state and prevent any other indirect changes to it.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyClipboard(cl=1,clr=1,cp=1,ps=1,sh=1,uv=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyClipboard.html



-----------------------------------------

polyClipboard is undoable, NOT queryable, and NOT editable.

The command allows the user to copy and paste certain polygonal attributes to
a clipboard. These attributes are: 1) Shader (shading engine) assignment. 2)
Texture coordinate (UV) assignment. 3) Color value assignment. Any combination
of attributes can be chosen for the copy or paste operation. If the attribute
has not been copied to the clipboard, then naturally it cannot be pasted from
the clipboard. The copy option will copy the attribute assignments from a
single source polygonal dag object or polygon component. If the source does
not have the either UV or color attributes, then nothing will be copied to the
clipboard. The paste option will paste the attribute assignments to one or
more polygon components or polygonal dag objects. If the destination does not
have either UV or color attributes, then new values will be assigned as
needed. Additionally, there is the option to clear the clipboard contents


-----------------------------------------


Return Value:

boolean  Success or Failure


-----------------------------------------


Flags:

-----------------------------------------

cl    : clear           [boolean] []
    When used, will mean to clear the specified attribute argument(s).

-----------------------------------------

clr   : color           [boolean] []
    When used, will be to copy or paste color attributes

-----------------------------------------

cp    : copy            [boolean] []
    When used, will mean to copy the specified attribute argument(s).

-----------------------------------------

ps    : paste           [boolean] []
    When used, will mean to paste the specified attribute argument(s).

-----------------------------------------

sh    : shader          [boolean] []
    When used, will be to copy or paste shader attributes

-----------------------------------------

uv    : uvCoordinates   [boolean]
    When used, will be to copy or paste texture coordinate attributes

    """

def polyCloseBorder(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCloseBorder.html



-----------------------------------------

polyCloseBorder is undoable, queryable, and editable.

Closes open borders of objects. For each border edge given, a face is created
to fill the hole the edge lies on.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyCollapseEdge(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCollapseEdge.html



-----------------------------------------

polyCollapseEdge is undoable, queryable, and editable.

Turns each selected edge into a point.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyCollapseFacet(q=1,e=1,at="float",cch=1,ch=1,n="string",nds="int",uat=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCollapseFacet.html



-----------------------------------------

polyCollapseFacet is undoable, queryable, and editable.

Turns each selected facet into a point.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : areaThreshold   [float] ['query', 'edit']
    Area threshold to determine whether faces should be collapsed. Attribute is ignored unless useAreaThreshold is set to true.   Default: 0.1

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

uat   : useAreaThreshold [boolean]
    If true only collapse faces with area less than the area threshold, otherwise collapse all faces regardless of area   Default: false

    """

def polyCollapseTweaks(q=1,hvt=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCollapseTweaks.html



-----------------------------------------

polyCollapseTweaks is undoable, queryable, and NOT editable.

A command that updates a mesh's vertex tweaks by applying its tweak data
(stored on the mesh node) onto its respective vertex data.

This command is only useful in cases where no construction history is
associated with the shape node.

If a mesh name is not specified as input, a singly selected mesh (if any) will
have its tweaked vertices baked.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

hvt   : hasVertexTweaks [boolean]
    Determines whether an individual mesh has vertex tweaks.

    """

def polyColorBlindData(amb="float",amg="float",amr="float",n="string",bmb="float",bmg="float",bmr="float",ccb="float",ccg="float",ccr="float",cb="float",cg="float",cr="float",dt="string",efc=1,mxb="float",mxg="float",mxr="float",mxv="float",mnb="float",mng="float",mnr="float",mnv="float",m="int",ncb="float",ncg="float",ncr="float",num="int",queryMode=1,id="int",umx=1,umn=1,v="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyColorBlindData.html



-----------------------------------------

polyColorBlindData is NOT undoable, NOT queryable, and NOT editable.

This command applies false color to the selected polygonal components and
objects, depending on whether or not blind data exists for the selected
components (or, in the case of poly objects, dynamic attributes), and,
depending on the color mode indicated, what the values are. It is possible to
color objects based on whether or not the data exists, if the data matches a
specific value or range of values, or grayscale color the data according to
what the actual value is in relation to the specified min and max. This
command also has a query mode in which the components and/or objects are
returned in a string array to allow for selection filtering.


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

amb   : aboveMaxColorBlue [float] []
    Specifies blue component of color to use for data that is above max

-----------------------------------------

amg   : aboveMaxColorGreen [float] []
    Specifies green component of color to use for data that is above max

-----------------------------------------

amr   : aboveMaxColorRed [float] []
    Specifies red component of color to use for data that is above max

-----------------------------------------

n     : attrName        [string] []
    Specifies the name of the data that is being examined by this command.

-----------------------------------------

bmb   : belowMinColorBlue [float] []
    Specifies blue component of color to use for data that is below min

-----------------------------------------

bmg   : belowMinColorGreen [float] []
    Specifies green component of color to use for data that is below min

-----------------------------------------

bmr   : belowMinColorRed [float] []
    Specifies red component of color to use for data that is below min

-----------------------------------------

ccb   : clashColorBlue  [float] []
    Specifies blue component color to use for data which clashes

-----------------------------------------

ccg   : clashColorGreen [float] []
    Specifies green component color to use for data which clashes

-----------------------------------------

ccr   : clashColorRed   [float] []
    Specifies red component color to use for data which clashes

-----------------------------------------

cb    : colorBlue       [float] []
    Specifies blue component of color to use for given data

-----------------------------------------

cg    : colorGreen      [float] []
    Specifies green component of color to use for given data

-----------------------------------------

cr    : colorRed        [float] []
    Specifies red component of color to use for given data

-----------------------------------------

dt    : dataType        [string] []
    Specifies the type for this id

-----------------------------------------

efc   : enableFalseColor [boolean] []
    Turns false coloring on or off for all poly objects in the scene

-----------------------------------------

mxb   : maxColorBlue    [float] []
    Specifies blue component of color to use for max value for grayscale

-----------------------------------------

mxg   : maxColorGreen   [float] []
    Specifies green component of color to use for max value for grayscale

-----------------------------------------

mxr   : maxColorRed     [float] []
    Specifies red component of color to use for max value for grayscale

-----------------------------------------

mxv   : maxValue        [float] []
    Specifies the max value for grayscale or discrete range data

-----------------------------------------

mnb   : minColorBlue    [float] []
    Specifies blue component of color to use for min value for grayscale

-----------------------------------------

mng   : minColorGreen   [float] []
    Specifies green component of color to use for min value for grayscale

-----------------------------------------

mnr   : minColorRed     [float] []
    Specifies red component of color to use for min value for grayscale

-----------------------------------------

mnv   : minValue        [float] []
    Specifies the min value for grayscale or discrete range data

-----------------------------------------

m     : mode            [int] []
    Specifies the mode:    * 0 : binary - only components and objects that have the data will be colored   * 1 : discrete value - a value is specified. Data that matches this value will be colored   * 2 : discrete range - values that fall within the given range will be colored   * 3 : unsigned set mode - if ( givenValue & actualValue ) then data will be colored   * 4 : unsigned not set mode - if ( !(givenValue & actualValue) ) then data will be colored   * 5 : unsigned equal mode - if ( givenValue == actualValue ) then data will be colored   * 6 : grayscale mode - a min value, max value, min color, max color, below min color, and above max color are given. Data is colored according to how it relates to these values.   * 7 : as color mode - if the blind data consists of 3 doubles, ranged 0-1, the components are colored as the data specifies

-----------------------------------------

ncb   : noColorBlue     [float] []
    Specifies blue component of color to use for no data assigned

-----------------------------------------

ncg   : noColorGreen    [float] []
    Specifies green component of color to use for no data assigned

-----------------------------------------

ncr   : noColorRed      [float] []
    Specifies red component of color to use for no data assigned

-----------------------------------------

num   : numIdTypes      [int] []
    Specifies how many attrs are in this id type

-----------------------------------------

q     : queryMode       [boolean] []
    If on, do not color and return selection as string array instead. Any data that would be colored normally (except for 'no color' and out of range colors) is returned

-----------------------------------------

id    : typeId          [int] []
    Specifies the typeId of the BlindData type being created

-----------------------------------------

umx   : useMax          [boolean] []
    Specifies whether the max should be used for discrete ranges

-----------------------------------------

umn   : useMin          [boolean] []
    Specifies whether the min should be used for discrete ranges

-----------------------------------------

v     : value           [string]
    The value of the data

    """

def polyColorDel(q=1,e=1,cch=1,cls="string",ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyColorDel.html



-----------------------------------------

polyColorDel is undoable, queryable, and editable.

Deletes color from selected components.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cls   : colorSetName    [string] ['query', 'edit']
    The name of the color set to work on

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyColorMod(q=1,e=1,afv="float",ai="int",ap="float",bcn="string",bfv="float",bi="int",bp="float",cch=1,ch=1,gfv="float",gi="int",gp="float",h="float",nfv="float",ni="int",np="float",n="string",nds="int",rfv="float",ri="int",rp="float",s="float",v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyColorMod.html



-----------------------------------------

polyColorMod is undoable, queryable, and editable.

Modifies the attributes of a poly color set.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

afv   : alphaScale_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

ai    : alphaScale_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

ap    : alphaScale_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

bcn   : baseColorName   [string] []
    The name of the color set to be modified.

-----------------------------------------

bfv   : blueScale_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

bi    : blueScale_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

bp    : blueScale_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

gfv   : greenScale_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

gi    : greenScale_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

gp    : greenScale_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

h     : huev            [float] ['query', 'edit']
    Hue rotates hue value of the final color.   Default: 0.0

-----------------------------------------

nfv   : intensityScale_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

ni    : intensityScale_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

np    : intensityScale_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rfv   : redScale_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

ri    : redScale_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

rp    : redScale_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

s     : satv            [float] ['query', 'edit']
    Sat scales the staturation of the final color.   Default: 1.0

-----------------------------------------

v     : value           [float]
    Value scales the final color value.   Default: 1.0

    """

def polyColorPerVertex(q=1,e=1,a="float",cla=1,b="float",cdo=1,g="float",r="float",rgb="[float, float, float]",nun=1,rel=1,rem=1,rpt="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyColorPerVertex.html



-----------------------------------------

polyColorPerVertex is undoable, queryable, and editable.

Command associates color(rgb and alpha) with vertices on polygonal objects.
When used with the query flag, it returns the color associated with the
specified components.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : alpha           [float] ['query', 'edit']
    Specifies the alpha channel of color

-----------------------------------------

cla   : clamped         [boolean] ['query', 'edit']
    This flag specifies if the color set will truncate any value that is outside 0 to 1 range.

-----------------------------------------

b     : colorB          [float] ['query', 'edit']
    Specifies the B channel of color

-----------------------------------------

cdo   : colorDisplayOption [boolean] ['query', 'edit']
    Change the display options on the mesh to display the vertex colors.

-----------------------------------------

g     : colorG          [float] ['query', 'edit']
    Specifies the G channel of color

-----------------------------------------

r     : colorR          [float] ['query', 'edit']
    Specifies the R channel of color

-----------------------------------------

rgb   : colorRGB        [[float, float, float]] ['query', 'edit']
    Specifies the RGB channels of color

-----------------------------------------

nun   : notUndoable     [boolean] ['query', 'edit']
    Execute the command, but without having the command be undoable. This option will greatly improve performance for large numbers of object. This will make the command not undoable regardless of whether undo has been enabled or not.

-----------------------------------------

rel   : relative        [boolean] ['query', 'edit']
    When used, the color values specified are added relative to the current values.

-----------------------------------------

rem   : remove          [boolean] ['query', 'edit']
    When used, the color values are removed from the selected or specified objects or components. This option only supports meshes with no construction history, or meshes whose construction history includes a recent polyColorPerVertexNode. For meshes whose construction history includes a polgon operation the polyColorPerVertexNode, consider using the polyColorDel command instead

-----------------------------------------

rpt   : representation  [int]
    This flag corresponds to the color channels to used, for example A(alpha only), RGB, and RGBA.

    """

def polyColorSet(q=1,e=1,acs=1,cla=1,cs="string",cp=1,cr=1,ccs=1,cpi=1,d=1,nc="string",pi=1,rn=1,rpt="string",si=1,us=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyColorSet.html



-----------------------------------------

polyColorSet is undoable, queryable, and editable.

Command to do the following to color sets: \- delete an existing color set. \-
rename an existing color set. \- create a new empty color set. \- set the
current color set to a pre-existing color set. \- modify sharing between
instances of per-instance color sets \- query the current color set. \- query
the names of all color sets. \- query the name(s) along with representation
value(s) or clamped value(s) of all color sets \- query the representation
value or clamped value of the current color set


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

acs   : allColorSets    [boolean] ['query', 'edit']
    This flag when used in a query will return a list of all of the color set names

-----------------------------------------

cla   : clamped         [boolean] ['query', 'edit']
    This flag specifies if the color set will truncate any value that is outside 0 to 1 range.

-----------------------------------------

cs    : colorSet        [string] ['query', 'edit']
    Specifies the name of the color set that this command needs to work on. This flag has to be specified for this command to do anything meaningful other than query the current color set.

-----------------------------------------

cp    : copy            [boolean] ['query', 'edit']
    This flag when used will result in the copying of the color set corresponding to name specified with the colorSet flag to the colorSet corresponding to the name specified with the newcolorSet flag

-----------------------------------------

cr    : create          [boolean] ['query', 'edit']
    This flag when used will result in the creation of an empty color set corresponding to the name specified with the colorSet flag. If a color set with that name already exists, then no new color set will be created.

-----------------------------------------

ccs   : currentColorSet [boolean] ['query', 'edit']
    This flag when used will set the current color set that the object needs to work on, to be the color set corresponding to the name specified with the colorSet flag. This does require that a colorSet with the specified name exist. When queried, this returns the current color set.

-----------------------------------------

cpi   : currentPerInstanceSet [boolean] ['query', 'edit']
    This is a query-only flag for use when the current color set is a per- instance color set family. This returns the member of the set family that corresponds to the currently select instance.

-----------------------------------------

d     : delete          [boolean] ['query', 'edit']
    This flag when used will result in the deletion of the color set corresponding to the name specified with the colorSet flag.

-----------------------------------------

nc    : newColorSet     [string] ['query', 'edit']
    Specifies the name that the color set corresponding to the name specified with the colorSet flag, needs to be renamed to.

-----------------------------------------

pi    : perInstance     [boolean] ['query', 'edit']
    This flag can be used in conjunction with the create flag to indicate whether or not the color set is per-instance. When you create a per-instance color set, the set will be applied as shared between all selected instances of the shape unless the unshared flag is used. The perInstance flag can be used in query mode with the currentColorSet or allColorSets flag to indicate that the set family names (i.e. not containing instance identifiers) will be returned by the query.  In query mode, this flag can accept a value.

-----------------------------------------

rn    : rename          [boolean] ['query', 'edit']
    This flag when used will result in the renaming of the color set corresponding to the name specified with the colorSet flag to the name specified using the newColorSet flag.

-----------------------------------------

rpt   : representation  [string] ['query', 'edit']
    This flag corresponds to the color channels to used, for example A(alpha only), RGB, and RGBA.

-----------------------------------------

si    : shareInstances  [boolean] ['query', 'edit']
    This flag is used to modify the sharing of per-instance color sets within a given color set family so that all selected instances share the specified set. In query mode, it returns a list of the instances that share the set specified by the colorSet flag.

-----------------------------------------

us    : unshared        [boolean]
    This flag can be used in conjunction with the create and perInstance flags to indicate that the newly created per-instance set should be created with a separate set per instance.

    """

def polyCompare(ic=1,c=1,edges=1,fd=1,un=1,iuv=1,uv=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCompare.html



-----------------------------------------

polyCompare is undoable, NOT queryable, and NOT editable.

Compares two Polygonal Geometry objects with a fine control on what to
compare.  
If no objects are specified in the command line, then the objects from the
active list are used.  
Default behaviour is to compare all flags.  
Use MEL script polyCompareTwoObjects.mel to get formatted output from this
command.


-----------------------------------------


Return Value:

int  0 if successful, non-zero if poly1 and poly2 are not determined to be
equal based on requested flags. The non-zero value depends on which attributes
are different:  
Vertices = 1  
Edges = 2  
Face Descriptions = 4  
UV Sets = 8  
UV Indices = 16  
Color Sets = 32  
Color Indices = 64  
User Normals = 128  
So a return value of 3, for example, indicates both vertices and edges are
different.


-----------------------------------------


Flags:

-----------------------------------------

ic    : colorSetIndices [boolean] []
    Compare poly1, poly2 for matching Color Indices.

-----------------------------------------

c     : colorSets       [boolean] []
    Compare poly1, poly2 for matching Color Sets.

-----------------------------------------

e     : edges           [boolean] []
    Compare poly1, poly2 for matching Edges.

-----------------------------------------

fd    : faceDesc        [boolean] []
    Compare poly1, poly2 for matching Face Descriptions. Face descriptions describe the topology of a face, for example number and orientation of edges, number of topology of any holes in the face etc.

-----------------------------------------

un    : userNormals     [boolean] []
    Compare poly1, poly2 for matching User Normals.

-----------------------------------------

iuv   : uvSetIndices    [boolean] []
    Compare poly1, poly2 for matching UV Indices.

-----------------------------------------

uv    : uvSets          [boolean] []
    Compare poly1, poly2 for matching UV Sets.

-----------------------------------------

v     : vertices        [boolean]
    Compare poly1, poly2 for matching Vertices.

    """

def polyCone(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv="int",h="linear",n="string",nds="int",o=1,r="linear",rcp=1,sa="int",sc="int",sh="int",sx="int",sy="int",sz="int",tx=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCone.html



-----------------------------------------

polyCone is undoable, queryable, and editable.

The cone command creates a new polygonal cone.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the cone.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [int] ['query', 'edit']
    Create UVs or not.    * 0: No UVs   * 1: No Normalization   * 2: Normalize   * 3: Normalize and Preserve Aspect Ratio     Default: 2

-----------------------------------------

h     : height          [linear] ['query', 'edit']
    Height of the cone.   Default: 2.0

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    Radius of the cone.   Default: 1.0

-----------------------------------------

rcp   : roundCap        [boolean] ['query', 'edit']
    To indicate whether we need a round cap   Default: false

-----------------------------------------

sa    : subdivisionsAxis [int] ['query', 'edit']
    Subdivisions around the axis.   Default: 20

-----------------------------------------

sc    : subdivisionsCap [int] ['query', 'edit']
    Subdivisions on the bottom cap.   Default: 0

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height.   Default: 1

-----------------------------------------

sx    : subdivisionsX   [int] ['query', 'edit']
    This specifies the number of subdivisions in the X direction for the cone.   C: Default is 20.   Q: When queried, this flag returns an int.

-----------------------------------------

sy    : subdivisionsY   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Y direction for the cone.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

sz    : subdivisionsZ   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Z direction for the cone.   C: Default is 0.   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [boolean]
    Apply texture or not.   Default: true

    """

def polyConnectComponents(q=1,e=1,aef="float",cch=1,ch=1,ief=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyConnectComponents.html



-----------------------------------------

polyConnectComponents is undoable, queryable, and editable.

Splits polygon edges according to the selected components. The selected
components are gathered into connected 'paths' that define continuous splits.
Mixed components (vertices, edges and faces) can be used at once. The
connection rules are: * Edges can connect to other edges in the same face or
to vertices in the same face (that are not in the edge itself) or to faces
connected to other edges in the same face. * Vertices can connect to edges (as
above) or to vertices in the same face (that are not joined to the first
vertex by an edge) or to faces adjacent to a face that uses the vertex (except
those that also use the vertex). * Faces can connect to vertices or edges (as
above) or to adjacent faces.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aef   : adjustEdgeFlow  [float] ['query', 'edit']
    The weight value of the edge vertices to be positioned.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ief   : insertWithEdgeFlow [boolean] ['query', 'edit']
    True to enable edge flow. Otherwise, the edge flow is disabled.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyContourProjection(q=1,e=1,cch=1,ch=1,cm=1,fr=1,ibd=1,m="int",n="string",nds="int",o0="linear",o1="linear",o2="linear",o3="linear",rs="float",s0="float",s1="float",s2="float",s3="float",udc=1,uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyContourProjection.html



-----------------------------------------

polyContourProjection is undoable, queryable, and editable.

Performs a contour stretch UV projection onto an object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] []
    Set to true if a new map should be created

-----------------------------------------

fr    : flipRails       [boolean] ['query', 'edit']
    If true, flip which curves are the rails of the birail surface.

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    Set to true if the new node created should inserted before any deformer nodes.

-----------------------------------------

m     : method          [int] ['query', 'edit']
    Sets which projection method to use. Valid values are   0: Walk Contours   1: NURBS Projection

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o0    : offset0         [linear] ['query', 'edit']
    Sets the offset on edge 0 of the NURBS surface.

-----------------------------------------

o1    : offset1         [linear] ['query', 'edit']
    Sets the offset on edge 1 of the NURBS surface.

-----------------------------------------

o2    : offset2         [linear] ['query', 'edit']
    Sets the offset on edge 2 of the NURBS surface.

-----------------------------------------

o3    : offset3         [linear] ['query', 'edit']
    Sets the offset on edge 3 of the NURBS surface.

-----------------------------------------

rs    : reduceShear     [float] ['query', 'edit']
    Sets the 'reduce shear' parameter of the projection.

-----------------------------------------

s0    : smoothness0     [float] ['query', 'edit']
    Sets the smoothness of edge 0 of the NURBS surface.

-----------------------------------------

s1    : smoothness1     [float] ['query', 'edit']
    Sets the smoothness of edge 1 of the NURBS surface.

-----------------------------------------

s2    : smoothness2     [float] ['query', 'edit']
    Sets the smoothness of edge 2 of the NURBS surface.

-----------------------------------------

s3    : smoothness3     [float] ['query', 'edit']
    Sets the smoothness of edge 3 of the NURBS surface.

-----------------------------------------

udc   : userDefinedCorners [boolean] ['query', 'edit']
    If true, the four vertices specified by user will be taken as corners to do the projection.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyCopyUV(q=1,e=1,cch=1,ch=1,cm=1,n="string",nds="int",uvs="string",uvi="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCopyUV.html



-----------------------------------------

polyCopyUV is undoable, queryable, and editable.

Copy some UVs from a UV set into another.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] []
    Set to true if a new map should be created

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

uvi   : uvSetNameInput  [string] ['query', 'edit']
    Specifies name of the input uv set to read the UV description from. Default is the current UV set.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyCrease(q=1,e=1,ch=1,op="uint",rv="float",v="float",vv="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCrease.html



-----------------------------------------

polyCrease is undoable, queryable, and editable.

Command to set the crease values on the edges or vertices of a poly. The
crease values are used by the smoothing algorithm.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ch    : createHistory   [boolean] ['query', 'edit']
    For objects that have no construction history, this flag can be used to force the creation of construction history for creasing. By default, history is not created if the object has no history. Regardless of this flag, history is always created if the object already has history.

-----------------------------------------

op    : operation       [uint] ['query', 'edit']
    Operation to perform. Valid values are: 0: Crease the specified components. 1: Remove the crease values for the specified components. 2: Remove all crease values from the mesh. Default is 0.

-----------------------------------------

rv    : relativeValue   [float] ['query', 'edit']
    Specifies a new relative value for all selected vertex and edge components. This flag can not be used at the same time as either the value or vertexValue flags.

-----------------------------------------

v     : value           [float] ['query', 'edit']
    Specifies the crease value for the selected edge components. When specified multiple times, the values are assigned respectively to the specified edges.

-----------------------------------------

vv    : vertexValue     [float]
    Specifies the crease value for the selected vertex components. When specified multiple times, the values are assigned respectively to the specified vertices.

    """

def polyCreateFacet(q=1,e=1,ch=1,hl=1,n="string",p="[[, float, float, float, ]]",s="int",tx="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCreateFacet.html



-----------------------------------------

polyCreateFacet is undoable, queryable, and editable.

Create a new polygonal object with the specified face, which will be closed.
List of arguments must have at least 3 points.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

hl    : hole            [boolean] []
    Add a hole. The following points will define a hole. Holes can be defined either clockwise or counterclockwise. Note that this flag is not recommended for use in Python. When specifying facets with the point flag in Python, pass in an empty point "()" when you want to start specifying a hole.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

p     : point           [[[, float, float, float, ]]] []
    Adds a new point to the face. Coordinates of points are given in world reference. The point flag may also be passed with no arguments. That indicates that the following points will specify a hole. Passing the point flag with no arguments is the same as using the "hole" flag, except that it will work in Python.

-----------------------------------------

s     : subdivision     [int] ['query', 'edit']
    This flag specifies the level of subdivision. Subdivides edges into the given number of edges.   C: Default is 1 (no subdivision).   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [int]
    Specifies how the face is mapped.   0 - None; 1 - Normalize; 2 - Unitize   C: Default is 0 (no mapping).   Q: When queried, this flag returns an int

    """

def polyCube(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv="int",d="linear",h="linear",n="string",nds="int",o=1,sd="int",sh="int",sw="int",sx="int",sy="int",sz="int",tx="int",w="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCube.html



-----------------------------------------

polyCube is undoable, queryable, and editable.

The cube command creates a new polygonal cube.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the cube.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [int] ['query', 'edit']
    Create UVs or not.    * 0: No UVs   * 1: No Normalization   * 2: Normalize Each Face Separately   * 3: Normalize Collectively   * 4: Normalize and Preserve Aspect Ratio     Default: 3

-----------------------------------------

d     : depth           [linear] ['query', 'edit']
    Depth of the cube.   Default: 1.0

-----------------------------------------

h     : height          [linear] ['query', 'edit']
    Height of the cube.   Default: 1.0

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

sd    : subdivisionsDepth [int] ['query', 'edit']
    Subdivisions along the depth of the cube.   Default: 1

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height of the cube.   Default: 1

-----------------------------------------

sw    : subdivisionsWidth [int] ['query', 'edit']
    Subdivisions along the width of the cube.   Default: 1

-----------------------------------------

sx    : subdivisionsX   [int] ['query', 'edit']
    This specifies the number of subdivisions in the X direction for the cube.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

sy    : subdivisionsY   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Y direction for the cube.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

sz    : subdivisionsZ   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Z direction for the cube.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [int] ['query', 'edit']
    What texture mechanism to be applied 0=No textures; 1=Object; 2=Faces   Default: 1

-----------------------------------------

w     : width           [linear]
    Width of the cube.   Default: 1.0

    """

def polyCut(q=1,e=1,cch=1,ch=1,pc="[linear, linear, linear]",pcx="linear",pcy="linear",pcz="linear",ph="linear",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",ps="[linear, linear]",pw="linear",cd="string",df=1,ef=1,eo="[linear, linear, linear]",eox="linear",eoy="linear",eoz="linear",n="string",nds="int",oo=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCut.html



-----------------------------------------

polyCut is undoable, queryable, and editable.

This command splits a mesh, or a set of poly faces, along a plane. The
position and orientation of the plane can be adjusted using the appropriate
flags listed above. In addition, the cut operation can also delete the faces
lying on one side of the cutting plane, or extract those faces by an offset
amount.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

pc    : cutPlaneCenter  [[linear, linear, linear]] ['query', 'edit']
    The position of the cutting plane.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pcx   : cutPlaneCenterX [linear] ['query', 'edit']
    Cutting plane center X coord.

-----------------------------------------

pcy   : cutPlaneCenterY [linear] ['query', 'edit']
    Cutting plane center Y coord.

-----------------------------------------

pcz   : cutPlaneCenterZ [linear] ['query', 'edit']
    Cutting plane center Z coord.

-----------------------------------------

ph    : cutPlaneHeight  [linear] ['query', 'edit']
    The height of the cutting plane

-----------------------------------------

ro    : cutPlaneRotate  [[angle, angle, angle]] ['query', 'edit']
    The orientation of the cutting plane.   Default: 0.0, 0.0, 0.0

-----------------------------------------

rx    : cutPlaneRotateX [angle] ['query', 'edit']
    cutting plane X rotate angle.

-----------------------------------------

ry    : cutPlaneRotateY [angle] ['query', 'edit']
    cutting plane Y rotate angle.

-----------------------------------------

rz    : cutPlaneRotateZ [angle] ['query', 'edit']
    cutting plane Z rotate angle.

-----------------------------------------

ps    : cutPlaneSize    [[linear, linear]] ['query', 'edit']
    The width and the height of the cutting plane   Default: 1.0, 1.0

-----------------------------------------

pw    : cutPlaneWidth   [linear] ['query', 'edit']
    The width of the cutting plane

-----------------------------------------

cd    : cuttingDirection [string] []
    This flag specifies the direction of the cutting plane. Valid values are "x", "y", "z" A value of "x" will cut the object along the YZ plane cutting through the center of the bounding box. A value of "y" will cut the object along the ZX plane cutting through the center of the bounding box. A value of "z" will cut the object along the XY plane cutting through the center of the bounding box.

-----------------------------------------

df    : deleteFaces     [boolean] ['query', 'edit']
    whether to delete the one-half of the cut-faces of the poly. If true, they are deleted.   Default: false

-----------------------------------------

ef    : extractFaces    [boolean] ['query', 'edit']
    whether to extract the cut-faces of the poly into a separate shell. If true, they are extracted.   Default: false

-----------------------------------------

eo    : extractOffset   [[linear, linear, linear]] ['query', 'edit']
    The displacement offset of the cut faces.   Default: 0.5, 0.5, 0.5

-----------------------------------------

eox   : extractOffsetX  [linear] ['query', 'edit']
    The X-displacement offset of the cut faces.

-----------------------------------------

eoy   : extractOffsetY  [linear] ['query', 'edit']
    The Y-displacement offset of the cut faces.

-----------------------------------------

eoz   : extractOffsetZ  [linear] ['query', 'edit']
    The Z-displacement offset of the cut faces.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

oo    : onObject        [boolean] ['query', 'edit']
    whether to act on the entire polyObject or its selected face components   Default: true

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyCylinder(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv="int",h="linear",n="string",nds="int",o=1,r="linear",rcp=1,sa="int",sc="int",sh="int",sx="int",sy="int",sz="int",tx="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCylinder.html



-----------------------------------------

polyCylinder is undoable, queryable, and editable.

The cylinder command creates a new polygonal cylinder.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the cylinder.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [int] ['query', 'edit']
    Create UVs or not.    * 0: No UVs   * 1: No Normalization   * 2: Normalize   * 3: Normalize and Preserve Aspect Ratio     Default: 2

-----------------------------------------

h     : height          [linear] ['query', 'edit']
    Height of the cylinder.   Default: 2.0

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    Radius of the cylinder.   Default: 1.0

-----------------------------------------

rcp   : roundCap        [boolean] ['query', 'edit']
    To indicate whether we need a round cap   Default: false

-----------------------------------------

sa    : subdivisionsAxis [int] ['query', 'edit']
    Subdivisions around the axis.   Default: 20

-----------------------------------------

sc    : subdivisionsCaps [int] ['query', 'edit']
    Subdivisions on the caps   Default: 0

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height.   Default: 1

-----------------------------------------

sx    : subdivisionsX   [int] ['query', 'edit']
    This specifies the number of subdivisions in the X direction for the cylinder.   C: Default is 20.   Q: When queried, this flag returns an int.

-----------------------------------------

sy    : subdivisionsY   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Y direction for the cylinder.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

sz    : subdivisionsZ   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Z direction for the cylinder.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [int]
    What texture mechanism to be applied 0=No textures, 1=Object, 2=Faces   Default: 2

    """

def polyCylindricalProjection(q=1,e=1,cch=1,ch=1,cm=1,ic="[float, float]",icx="float",icy="float",imageScale="[float, float]",isu="float",isv="float",ibd=1,kir=1,md="string",n="string",nds="int",pi=1,pc="[linear, linear, linear]",pcx="linear",pcy="linear",pcz="linear",ph="linear",phs="linear",ps="[linear, linear]",psu="linear",psv="linear",r="linear",ra="angle",sc=1,sf=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyCylindricalProjection.html



-----------------------------------------

polyCylindricalProjection is undoable, queryable, and editable.

TpolyProjCmdBase is a base class for the command to create a mapping on the
selected polygonal faces. Projects a cylindrical map onto an object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] ['query']
    This flag when set true will create a new map with a the name passed in, if the map does not already exist.

-----------------------------------------

ic    : imageCenter     [[float, float]] ['query', 'edit']
    The center point of the 2D model layout.   Default: 0.5, 0.5

-----------------------------------------

icx   : imageCenterX    [float] ['query', 'edit']
    Image center X coord.

-----------------------------------------

icy   : imageCenterY    [float] ['query', 'edit']
    Image center Y coord.

-----------------------------------------

imageScale : imageScale      [[float, float]] ['query', 'edit']
    Specifies the UV scale : Enlarges or reduces the 2D version of the model in U or V space relative to the 2D centerpoint.   Default: 1.0, 1.0

-----------------------------------------

isu   : imageScaleU     [float] ['query', 'edit']
    Specifies the UV scale : Enlarges or reduces the 2D version of the model in U or V space relative to the 2D centerpoint.

-----------------------------------------

isv   : imageScaleV     [float] ['query', 'edit']
    The V scale : Enlarges or reduces the 2D version of the model in V space relative to the 2D centerpoint.

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    This flag specifies if the projection node should be inserted before or after deformer nodes already applied to the shape. Inserting the projection after the deformer leads to texture swimming during animation and is most often undesirable.   C: Default is on.

-----------------------------------------

kir   : keepImageRatio  [boolean] []
    True means keep any image ratio

-----------------------------------------

md    : mapDirection    [string] []
    This flag specifies the mapping direction.   'x', 'y' and 'z' projects the map along the corresponding axis.   'c' projects along the current camera viewing direction.   'p' does perspective projection if current camera is perspective.   'b' projects along the best plane fitting the objects selected.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pi    : perInstance     [boolean] []
    True if the new map is per-instance, otherwise it is shared.

-----------------------------------------

pc    : projectionCenter [[linear, linear, linear]] ['query', 'edit']
    The origin point from which the map is projected.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pcx   : projectionCenterX [linear] ['query', 'edit']
    Projection center X coord.

-----------------------------------------

pcy   : projectionCenterY [linear] ['query', 'edit']
    Projection center Y coord.

-----------------------------------------

pcz   : projectionCenterZ [linear] ['query', 'edit']
    Projection center Z coord.

-----------------------------------------

ph    : projectionHeight [linear] ['query', 'edit']
    The height of the map relative to the 3D projection axis

-----------------------------------------

phs   : projectionHorizontalSweep [linear] ['query', 'edit']
    The angle swept by the 3D projection axis

-----------------------------------------

ps    : projectionScale [[linear, linear]] ['query', 'edit']
    The width and the height of the map relative to the 3D projection axis.   Default: 180.0, 1.0

-----------------------------------------

psu   : projectionScaleU [linear] ['query', 'edit']
    The width of the map relative to the 3D projection axis.

-----------------------------------------

psv   : projectionScaleV [linear] ['query', 'edit']
    The height of the map relative to the 3D projection axis.

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    Used by the UI : Manipulator.   Default: 10.0

-----------------------------------------

ra    : rotationAngle   [angle] ['query', 'edit']
    The for the rotation. When the angle is positive, then the map rotates counterclockwise on the mapped model, whereas when it is negative then the map rotates lockwise on the mapped model.   Default: 0.0

-----------------------------------------

sc    : seamCorrect     [boolean] ['query', 'edit']
    Used to indicate fixing UV seams.   Default: false

-----------------------------------------

sf    : smartFit        [boolean] []
    True means use the smart fit algorithm

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyDelEdge(q=1,e=1,cch=1,cv=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyDelEdge.html



-----------------------------------------

polyDelEdge is undoable, queryable, and editable.

Deletes selected edges, and merges neighboring faces. If deletion leaves
winged vertices, they may be deleted as well.  
Notice : only non border edges can be deleted.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cv    : cleanVertices   [boolean] ['query', 'edit']
    If on : delete resulting winged vertices.   C: Default is "off".   Q: When queried, this flag returns an int.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyDelFacet(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyDelFacet.html



-----------------------------------------

polyDelFacet is undoable, queryable, and editable.

Deletes faces. If the result is split into disconnected pieces, the pieces
(so-called shells) are still considered to be one object.  
Notice : The last face cannot be deleted.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyDelVertex(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyDelVertex.html



-----------------------------------------

polyDelVertex is undoable, queryable, and editable.

Deletes vertices. Joins two edges which have a common vertex. The vertices
must be connected to exactly two edges (so-called "winged").


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyDuplicateAndConnect(ros=1,rc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyDuplicateAndConnect.html



-----------------------------------------

polyDuplicateAndConnect is undoable, NOT queryable, and NOT editable.

This command duplicates the input polygonal object, connects up the outMesh
attribute of the original polygonal shape to the inMesh attribute of the newly
created duplicate shape and copies over the shader assignments from the
original shape to the new duplicated shape.

The command will fail if no objects are selected or sent as argument or if the
object sent as argument is not a polygonal object.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

ros   : removeOriginalFromShaders [boolean] []
    Used to specify if the original object should be removed from the shaders (shadingGroups) that it is a member of. The shader associations will get transferred to the duplicated object, before they are removed from the original. If this flag is specified then the original polygonal object will be drawn in wireframe mode even if all objects are being drawn in shaded mode.

-----------------------------------------

rc    : renameChildren  [boolean]
    rename the children nodes of the hierarchy, to make them unique.

    """

def polyDuplicateEdge(q=1,e=1,aef="float",de=1,evo="float",ief=1,of="float",sma="angle",stp="int",svo="float",cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyDuplicateEdge.html



-----------------------------------------

polyDuplicateEdge is undoable, queryable, and editable.

Duplicates a series of connected edges (edgeLoop)


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aef   : adjustEdgeFlow  [float] ['query', 'edit']
    The weight value of the edge vertices to be positioned.

-----------------------------------------

de    : deleteEdge      [boolean] ['query', 'edit']
    When true, the end edges are deleted so the end triangles are converted to quads.

-----------------------------------------

evo   : endVertexOffset [float] ['query', 'edit']
    Weight value controlling the offset of the end vertex of the edgeloop.

-----------------------------------------

ief   : insertWithEdgeFlow [boolean] ['query', 'edit']
    True to enable edge flow. Otherwise, the edge flow is disabled.

-----------------------------------------

of    : offset          [float] []
    Weight value controlling the relative positioning of the new edges. The range of values is [0.0, 1.0].

-----------------------------------------

sma   : smoothingAngle  [angle] ['query', 'edit']
    Angle below which new edges will be smoothed

-----------------------------------------

stp   : splitType       [int] ['query', 'edit']
    Format: 0 - Absolute, 1 - Relative, 2 - Multi

-----------------------------------------

svo   : startVertexOffset [float] ['query', 'edit']
    Weight value controlling the offset of the start vertex of the edgeloop.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyEditEdgeFlow(q=1,e=1,aef="float",cch=1,ch=1,ef=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyEditEdgeFlow.html



-----------------------------------------

polyEditEdgeFlow is undoable, queryable, and editable.

Edit edges of a polygonal object to respect surface curvature.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aef   : adjustEdgeFlow  [float] []
    The weight value of the edge vertices to be positioned.   <0: Concave   0: Middle point   1: Surface continuity   >1: Convex   Default is 1.0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ef    : edgeFlow        [boolean] []
    True to enable edge flow. Otherwise, the edge flow is disabled.   Default is true.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyEditUV(q=1,a="float",pu="float",pv="float",r=1,rr="float",rot=1,s=1,su="float",sv="float",u="float",uvs="string",v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyEditUV.html



-----------------------------------------

polyEditUV is undoable, queryable, and NOT editable.

Command edits uvs on polygonal objects. When used with the query flag, it
returns the uv values associated with the specified components.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [float] ['query']
    Specifies the angle value (in degrees) that the uv values are to be rotated by.

-----------------------------------------

pu    : pivotU          [float] ['query']
    Specifies the pivot value, in the u direction, about which the scale or rotate is to be performed.

-----------------------------------------

pv    : pivotV          [float] ['query']
    Specifies the pivot value, in the v direction, about which the scale or rotate is to be performed.

-----------------------------------------

r     : relative        [boolean] ['query']
    Specifies whether this command is editing the values relative to the currently existing values. Default is true;

-----------------------------------------

rr    : rotateRatio     [float] ['query']
    Specifies the ratio value that the uv values are to be rotated by Default is 1.0

-----------------------------------------

rot   : rotation        [boolean] ['query']
    Specifies whether this command is editing the values with rotation values

-----------------------------------------

s     : scale           [boolean] ['query']
    Specifies whether this command is editing the values with scale values

-----------------------------------------

su    : scaleU          [float] ['query']
    Specifies the scale value in the u direction.

-----------------------------------------

sv    : scaleV          [float] ['query']
    Specifies the scale value in the v direction.

-----------------------------------------

u     : uValue          [float] ['query']
    Specifies the value, in the u direction - absolute if relative flag is false..

-----------------------------------------

uvs   : uvSetName       [string] ['query']
    Specifies the name of the uv set to edit uvs on. If not specified will use the current uv set if it exists.

-----------------------------------------

v     : vValue          [float]
    Specifies the value, in the v direction - absolute if relative flag is false..

    """

def polyEditUVShell(q=1,a="float",pu="float",pv="float",r=1,rr="float",rot=1,s=1,su="float",sv="float",u="float",uvs="string",v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyEditUVShell.html



-----------------------------------------

polyEditUVShell is undoable, queryable, and NOT editable.

Command edits uv shells on polygonal objects. When used with the query flag,
it returns the transformation values associated with the specified components.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [float] ['query']
    Specifies the angle value (in degrees) that the uv values are to be rotated by.

-----------------------------------------

pu    : pivotU          [float] ['query']
    Specifies the pivot value, in the u direction, about which the scale or rotate is to be performed.

-----------------------------------------

pv    : pivotV          [float] ['query']
    Specifies the pivot value, in the v direction, about which the scale or rotate is to be performed.

-----------------------------------------

r     : relative        [boolean] ['query']
    Specifies whether this command is editing the values relative to the currently existing values. Default is true;

-----------------------------------------

rr    : rotateRatio     [float] ['query']
    Specifies the ratio value that the uv values are to be rotated by Default is 1.0

-----------------------------------------

rot   : rotation        [boolean] ['query']
    Specifies whether this command is editing the values with rotation values

-----------------------------------------

s     : scale           [boolean] ['query']
    Specifies whether this command is editing the values with scale values

-----------------------------------------

su    : scaleU          [float] ['query']
    Specifies the scale value in the u direction.

-----------------------------------------

sv    : scaleV          [float] ['query']
    Specifies the scale value in the v direction.

-----------------------------------------

u     : uValue          [float] ['query']
    Specifies the value, in the u direction - absolute if relative flag is false..

-----------------------------------------

uvs   : uvSetName       [string] ['query']
    Specifies the name of the uv set to edit uvs on. If not specified will use the current uv set if it exists.

-----------------------------------------

v     : vValue          [float]
    Specifies the value, in the v direction - absolute if relative flag is false..

    """

def polyEvaluate(ae=1,activeShells=1,aus=1,a=1,b=1,b2=1,bc=1,bc2=1,ds=1,edge=1,ec=1,f=1,fa=1,fc=1,fmt=1,s=1,t=1,tc=1,uva=1,uvc=1,uep=1,ufa=1,uvs="string",us=1,usi=1,uv=1,uis="int",v=1,vc=1,wa=1,wfa=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyEvaluate.html



-----------------------------------------

polyEvaluate is undoable, NOT queryable, and NOT editable.

Returns the required counts on the specified objects.  
If no objects are specified in the command line, then the objects from the
active list are used.

In MEL, the values are returned in the same order as the flags are set. Under
Python, there is no concept of argument ordering, so the items are returned in
a dictionary keyed by the name of the flag. In Python, if only one item is
requested, then it will not be returned in a dictionary.  
For user convenience, if no flag is set, then all values are echoed.

All flags (except -fmt/format) are in fact query-flags. For user convenience,
the -q flag may be ommitted.

Some comments for non-formatted output :  

  * 3d bounding boxes are returned as 3 couples of floats, 2d ones as 2 couples of floats.
  * if a bounding box is queried and cannot be computed (for example the component bounding box when no component is selected, or 2d bounding box for and unmapped object) 0 is returned for each array element, so that indices in the output array remain consistent.
  * int values (queried by topological flags) cannot be mixed with float values (queried by bounding box flags). Thus if no flag is set, only int values are returned.


-----------------------------------------


Return Value:

Any  a MEL array of values, a Python dictionary, or a string, depending on the
format requested and the language called from.


-----------------------------------------


Flags:

-----------------------------------------

ae    : accurateEvaluation [boolean] []
    used to get accurate results for the bounding box computation For objects with large vertex counts, accurate evaluation takes more time

-----------------------------------------

activeShells : activeShells    [boolean] []
    returns the indices of active shells as an array of int

-----------------------------------------

aus   : activeUVShells  [boolean] []
    returns the indices of active UV shells (for the current map if one is not specified) as an array of int

-----------------------------------------

a     : area            [boolean] []
    returns the surface area of the object's faces in local space as a float

-----------------------------------------

b     : boundingBox     [boolean] []
    returns the object's bounding box in 3d space as 6 floats in MEL: xmin xmax ymin ymax zmin zmax, or as a tuple of three pairs in Python: ((xmin,xmax), (ymin,ymax), (zmin,zmax))

-----------------------------------------

b2    : boundingBox2d   [boolean] []
    returns the object's uv bounding box (for the current map if one is not specified) in 2d space as 4 floats in MEL : xmin xmax ymin ymax, or as a tuple of three pairs in Python: ((xmin,xmax), (ymin,ymax), (zmin,zmax))

-----------------------------------------

bc    : boundingBoxComponent [boolean] []
    returns the bounding box of selected components in 3d space as 6 floats in MEL : xmin xmax ymin ymax zmin zmax, or as a tuple of three pairs in Python: ((xmin,xmax), (ymin,ymax), (zmin,zmax))

-----------------------------------------

bc2   : boundingBoxComponent2d [boolean] []
    returns the bounding box of selected/specified components uv coordinates in 2d space as 4 floats in MEL : xmin xmax ymin ymax, or as a tuple of two pairs in Python: ((xmin,xmax), (ymin,ymax))

-----------------------------------------

ds    : displayStats    [boolean] []
    toggles the display of poly statistics for the active View. All other flags are ignored if this flag is specified (Obsolete \- refer to the headsUpDisplay command)

-----------------------------------------

e     : edge            [boolean] []
    returns the number of edges as an int

-----------------------------------------

ec    : edgeComponent   [boolean] []
    returns the object's number of selected edges as an int

-----------------------------------------

f     : face            [boolean] []
    returns the number of faces as an int

-----------------------------------------

fa    : faceArea        [boolean] []
    returns the surface area of selected/specified faces in local space as an array of float

-----------------------------------------

fc    : faceComponent   [boolean] []
    returns the object's number of selected faces as an int

-----------------------------------------

fmt   : format          [boolean] []
    used to display the results as an explicit sentence

-----------------------------------------

s     : shell           [boolean] []
    returns the number of shells (disconnected pieces) as an int

-----------------------------------------

t     : triangle        [boolean] []
    returns the number of triangles as an int

-----------------------------------------

tc    : triangleComponent [boolean] []
    returns the number of triangles of selected components as an int

-----------------------------------------

uva   : uvArea          [boolean] []
    returns the UV area of the object's faces in 2d space as a float

-----------------------------------------

uvc   : uvComponent     [boolean] []
    returns the object's number of selected uv coordinates as an int

-----------------------------------------

uep   : uvEdgePairs     [boolean] []
    returns the pairs of UVs that are on the selected/specified edges

-----------------------------------------

ufa   : uvFaceArea      [boolean] []
    returns the UV area of selected/specified faces in 2d space as an array of float

-----------------------------------------

uvs   : uvSetName       [string] []
    used when querying texture vertices to specify the uv set. If a uv set is not specified then the current map for the object will be used

-----------------------------------------

us    : uvShell         [boolean] []
    returns the number of UV shells (for the current map if one is not specified) as an int

-----------------------------------------

usi   : uvShellIds      [boolean] []
    returns the UV shell indices for selected/specified faces or UVs as an array of int (for the current map if one is not specified), one shell index per each face/UV.

-----------------------------------------

uv    : uvcoord         [boolean] []
    returns the number of uv coordinates (for the current map if one is not specified) as an int

-----------------------------------------

uis   : uvsInShell      [int] []
    returns all UVs inside specified shell(for the current map if one is not specified), use activeUVShells to get shell indices for current selection, use uvShellIds to get shell indices for specified faces or UVs

-----------------------------------------

v     : vertex          [boolean] []
    returns the number of vertices as an int

-----------------------------------------

vc    : vertexComponent [boolean] []
    returns the object's number of selected vertices as an int

-----------------------------------------

wa    : worldArea       [boolean] []
    returns the surface area of the object's faces in world space as a float

-----------------------------------------

wfa   : worldFaceArea   [boolean]
    returns the surface area of selected/specified faces in world space as an array of float

    """

def polyExtrudeEdge(q=1,e=1,cch=1,ch=1,cc=1,d="int",ga="float",inc="name",kft=1,lc="int",ld="[linear, linear, linear]",ldx="linear",ldy="linear",ldz="linear",lr="[angle, angle, angle]",lrx="angle",lry="angle",lrz="angle",ls="[float, float, float]",lsx="float",lsy="float",lsz="float",lt="[linear, linear, linear]",ltx="linear",lty="linear",ltz="linear",n="string",nds="int",off="float",pvt="[linear, linear, linear]",pvx="linear",pvy="linear",pvz="linear",ran="float",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",s="[float, float, float]",sx="float",sy="float",sz="float",sma="angle",tp="float",cfv="float",ci="int",cp="float",tk="float",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",twt="angle",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyExtrudeEdge.html



-----------------------------------------

polyExtrudeEdge is undoable, queryable, and editable.

Extrude edges separately or together.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cc    : createCurve     [boolean] []
    If true then the operation can create a curve.

-----------------------------------------

d     : divisions       [int] ['query', 'edit']
    How many internal edges are creating when pulling.   Default: 1

-----------------------------------------

ga    : gain            [float] ['query', 'edit']
    Gain factor per component. Can be painted using Artisan.   Default: 1.0

-----------------------------------------

inc   : inputCurve      [name] []
    This flag specifies the name of the curve to be used as input for the operation.

-----------------------------------------

kft   : keepFacesTogether [boolean] ['query', 'edit']
    How to extrude edges. If "on", extruded faces produced from the edges being extruded will be kept together. Otherwise they are pulled independently.   Default: true

-----------------------------------------

lc    : localCenter     [int] ['query', 'edit']
    Local center on the edge : 0=Middle point, 1=Start point, 2=End point.   Default: 0

-----------------------------------------

ld    : localDirection  [[linear, linear, linear]] ['query', 'edit']
    Direction to determine X axis for local space.   Default: 1.0, 0.0, 0.0

-----------------------------------------

ldx   : localDirectionX [linear] ['query', 'edit']
    X coord of the X axis.

-----------------------------------------

ldy   : localDirectionY [linear] ['query', 'edit']
    Y coord of the X axis.

-----------------------------------------

ldz   : localDirectionZ [linear] ['query', 'edit']
    Z coord of the X axis.

-----------------------------------------

lr    : localRotate     [[angle, angle, angle]] ['query', 'edit']
    The local rotations.   Default: 0.0, 0.0, 0.0

-----------------------------------------

lrx   : localRotateX    [angle] ['query', 'edit']
    Local rotate X coord. The range is [0, 360].

-----------------------------------------

lry   : localRotateY    [angle] ['query', 'edit']
    Local rotate Y coord. The range is [0, 360].

-----------------------------------------

lrz   : localRotateZ    [angle] ['query', 'edit']
    Local rotate Z coord : Rotation along the normal. The range is [0, 360].

-----------------------------------------

ls    : localScale      [[float, float, float]] ['query', 'edit']
    Local Scale.   Default: 1.0, 1.0, 1.0

-----------------------------------------

lsx   : localScaleX     [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

lsy   : localScaleY     [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

lsz   : localScaleZ     [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

lt    : localTranslate  [[linear, linear, linear]] ['query', 'edit']
    Local translate.   Default: 0.0, 0.0, 0.0

-----------------------------------------

ltx   : localTranslateX [linear] ['query', 'edit']
    Local translation X coord.

-----------------------------------------

lty   : localTranslateY [linear] ['query', 'edit']
    Local translation Y coord.

-----------------------------------------

ltz   : localTranslateZ [linear] ['query', 'edit']
    Local translation Z coord : Move along the normal.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

off   : offset          [float] ['query', 'edit']
    Edges are moved this distance in the opposite direction of the edge.   Default: 0.0

-----------------------------------------

pvt   : pivot           [[linear, linear, linear]] ['query', 'edit']
    The pivot for scaling and rotation.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pvx   : pivotX          [linear] ['query', 'edit']
    Pivot X coord.

-----------------------------------------

pvy   : pivotY          [linear] ['query', 'edit']
    Pivot Y coord.

-----------------------------------------

pvz   : pivotZ          [linear] ['query', 'edit']
    Pivot Z coord.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    Random value for all parameters.   Default: 0.0

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    Rotation angles around X, Y, Z.   Default: 0.0, 0.0, 0.0

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    Rotation angle around X.

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    Rotation angle around Y.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    Rotation angle around Z.

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    Scaling vector.   Default: 1.0, 1.0, 1.0

-----------------------------------------

sx    : scaleX          [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

sy    : scaleY          [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

sz    : scaleZ          [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

sma   : smoothingAngle  [angle] ['query', 'edit']
    Angle below which new edges will be smoothed   Default: kPi/6.0

-----------------------------------------

tp    : taper           [float] ['query', 'edit']
    Taper or Scale along the extrusion path   Default: 1.0

-----------------------------------------

cfv   : taperCurve_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

ci    : taperCurve_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

cp    : taperCurve_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

tk    : thickness       [float] ['query', 'edit']
    Edges are moved this distance in the direction of the connected face normals.   Default: 0.0f

-----------------------------------------

t     : translate       [[linear, linear, linear]] ['query', 'edit']
    Translation vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

tx    : translateX      [linear] ['query', 'edit']
    Translation X coord.

-----------------------------------------

ty    : translateY      [linear] ['query', 'edit']
    Translation Y coord.

-----------------------------------------

tz    : translateZ      [linear] ['query', 'edit']
    Translation Z coord.

-----------------------------------------

twt   : twist           [angle] ['query', 'edit']
    Twist or Rotation along the extrusion path   Default: 0.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyExtrudeFacet(q=1,e=1,att="float",cch=1,ch=1,cc=1,d="int",ga="float",g="[linear, linear, linear]",gx="linear",gy="linear",gz="linear",inc="name",kft=1,xft=1,lc="int",ld="[linear, linear, linear]",ldx="linear",ldy="linear",ldz="linear",lr="[angle, angle, angle]",lrx="angle",lry="angle",lrz="angle",ls="[float, float, float]",lsx="float",lsy="float",lsz="float",lt="[linear, linear, linear]",ltx="linear",lty="linear",ltz="linear",mx="linear",my="linear",mz="linear",m="[linear, linear, linear]",n="string",nds="int",off="float",pvt="[linear, linear, linear]",pvx="linear",pvy="linear",pvz="linear",ran="float",raf=1,ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",s="[float, float, float]",sx="float",sy="float",sz="float",sma="angle",tp="float",cfv="float",ci="int",cp="float",tk="float",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",twt="angle",w="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyExtrudeFacet.html



-----------------------------------------

polyExtrudeFacet is undoable, queryable, and editable.

Extrude faces. Faces can be extruded separately or together, and manipulations
can be performed either in world or object space.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attraction      [float] ['query', 'edit']
    Attraction, related to magnet. The range is [-2.0, 2.0].   Default: 0.0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cc    : createCurve     [boolean] []
    If true then the operation can create a curve.

-----------------------------------------

d     : divisions       [int] ['query', 'edit']
    How many divisions should the extrusion be broken-up into.   Default: 1

-----------------------------------------

ga    : gain            [float] ['query', 'edit']
    Gain factor per component. Can be painted using Artisan.   Default: 1.0

-----------------------------------------

g     : gravity         [[linear, linear, linear]] ['query', 'edit']
    The gravity vector.   Default: 0.0, -1.0, 0.0

-----------------------------------------

gx    : gravityX        [linear] ['query', 'edit']
    Gravity X coord.

-----------------------------------------

gy    : gravityY        [linear] ['query', 'edit']
    Gravity Y coord.

-----------------------------------------

gz    : gravityZ        [linear] ['query', 'edit']
    Gravity Z coord.

-----------------------------------------

inc   : inputCurve      [name] []
    This flag specifies the name of the curve to be used as input for the operation.

-----------------------------------------

kft   : keepFacesTogether [boolean] ['query', 'edit']
    How to extrude faces. If "on", faces are pulled together (connected ones stay connected), otherwise they are pulled independently.   Default: true

-----------------------------------------

xft   : keepFacetTogether [boolean] ['query', 'edit']
    How to extrude edges. If "on", extruded faces produced from the edges being extruded will be kept together. Otherwise they are pulled independently.   Default: true

-----------------------------------------

lc    : localCenter     [int] ['query', 'edit']
    Local center on the edge : 0=Middle point, 1=Start point, 2=End point.   Default: 0

-----------------------------------------

ld    : localDirection  [[linear, linear, linear]] ['query', 'edit']
    Direction to determine X axis for local space.   Default: 1.0, 0.0, 0.0

-----------------------------------------

ldx   : localDirectionX [linear] ['query', 'edit']
    X coord of the X axis.

-----------------------------------------

ldy   : localDirectionY [linear] ['query', 'edit']
    Y coord of the X axis.

-----------------------------------------

ldz   : localDirectionZ [linear] ['query', 'edit']
    Z coord of the X axis.

-----------------------------------------

lr    : localRotate     [[angle, angle, angle]] ['query', 'edit']
    The local rotations.   Default: 0.0, 0.0, 0.0

-----------------------------------------

lrx   : localRotateX    [angle] ['query', 'edit']
    Local rotate X coord. The range is [0, 360].

-----------------------------------------

lry   : localRotateY    [angle] ['query', 'edit']
    Local rotate Y coord. The range is [0, 360].

-----------------------------------------

lrz   : localRotateZ    [angle] ['query', 'edit']
    Local rotate Z coord : Rotation along the normal. The range is [0, 360].

-----------------------------------------

ls    : localScale      [[float, float, float]] ['query', 'edit']
    Local Scale.   Default: 1.0, 1.0, 1.0

-----------------------------------------

lsx   : localScaleX     [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

lsy   : localScaleY     [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

lsz   : localScaleZ     [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

lt    : localTranslate  [[linear, linear, linear]] ['query', 'edit']
    Local translate.   Default: 0.0, 0.0, 0.0

-----------------------------------------

ltx   : localTranslateX [linear] ['query', 'edit']
    Local translation X coord.

-----------------------------------------

lty   : localTranslateY [linear] ['query', 'edit']
    Local translation Y coord.

-----------------------------------------

ltz   : localTranslateZ [linear] ['query', 'edit']
    Local translation Z coord : Move along the normal.

-----------------------------------------

mx    : magnX           [linear] ['query', 'edit']
    Magnet X coord.

-----------------------------------------

my    : magnY           [linear] ['query', 'edit']
    Magnet Y coord.

-----------------------------------------

mz    : magnZ           [linear] ['query', 'edit']
    Magnet Z coord.

-----------------------------------------

m     : magnet          [[linear, linear, linear]] ['query', 'edit']
    The magnet vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

off   : offset          [float] ['query', 'edit']
    Local offset. Faces are moved this distance towards the inside of the face.   Default: 0.0

-----------------------------------------

pvt   : pivot           [[linear, linear, linear]] ['query', 'edit']
    The pivot for scaling and rotation.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pvx   : pivotX          [linear] ['query', 'edit']
    Pivot X coord.

-----------------------------------------

pvy   : pivotY          [linear] ['query', 'edit']
    Pivot Y coord.

-----------------------------------------

pvz   : pivotZ          [linear] ['query', 'edit']
    Pivot Z coord.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    Random value for all parameters.   Default: 0.0

-----------------------------------------

raf   : reverseAllFaces [boolean] ['query', 'edit']
    If "on", original faces are reversed in case of extruding all faces.   Default: true

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    Rotation angles around X, Y, Z.   Default: 0.0, 0.0, 0.0

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    Rotation angle around X.

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    Rotation angle around Y.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    Rotation angle around Z.

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    Scaling vector.   Default: 1.0, 1.0, 1.0

-----------------------------------------

sx    : scaleX          [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

sy    : scaleY          [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

sz    : scaleZ          [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

sma   : smoothingAngle  [angle] ['query', 'edit']
    Angle below which new edges will be smoothed   Default: kPi/6.0

-----------------------------------------

tp    : taper           [float] ['query', 'edit']
    Taper or Scale along the extrusion path   Default: 1.0

-----------------------------------------

cfv   : taperCurve_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

ci    : taperCurve_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

cp    : taperCurve_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

tk    : thickness       [float] ['query', 'edit']
    Faces are moved outwards from their original position to give the object a consistent thickess.   Default: 0.0f

-----------------------------------------

t     : translate       [[linear, linear, linear]] ['query', 'edit']
    Translation vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

tx    : translateX      [linear] ['query', 'edit']
    Translation X coord.

-----------------------------------------

ty    : translateY      [linear] ['query', 'edit']
    Translation Y coord.

-----------------------------------------

tz    : translateZ      [linear] ['query', 'edit']
    Translation Z coord.

-----------------------------------------

twt   : twist           [angle] ['query', 'edit']
    Twist or Rotation along the extrusion path   Default: 0.0

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    The weight, related to gravity.   Default: 0.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyExtrudeVertex(q=1,e=1,cch=1,ch=1,d="int",l="float",n="string",nds="int",w="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyExtrudeVertex.html



-----------------------------------------

polyExtrudeVertex is undoable, queryable, and editable.

Command that extrudes selected vertices outwards.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

d     : divisions       [int] ['query', 'edit']
    This flag specifies the number of subdivisions.   C: Default is 1   Q: When queried, this flag returns an int.

-----------------------------------------

l     : length          [float] ['query', 'edit']
    This flag specifies the length of the vertex extrusion.   C: Default is 0   Q: When queried, this flag returns a float.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

w     : width           [float] ['query', 'edit']
    This flag specifies the width of the vertex extrusion.   C: Default is 0   Q: When queried, this flag returns a float.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyFlipEdge(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyFlipEdge.html



-----------------------------------------

polyFlipEdge is undoable, queryable, and editable.

Command to flip the edges shared by 2 adjacent triangles. When used with the
edit flag, new edges can be added to the same node, instead of creating a
separate node in the chain.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.
    """

def polyFlipUV(q=1,e=1,cch=1,ch=1,cm=1,cut=1,ft="int",ibd=1,l=1,n="string",nds="int",pu="float",pv="float",up=1,uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyFlipUV.html



-----------------------------------------

polyFlipUV is undoable, queryable, and editable.

Flip (mirror) the UVs (in texture space) of input polyFaces, about either the
U or V axis..


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] []
    Set to true if a new map should be created

-----------------------------------------

cut   : cutUV           [boolean] ['query', 'edit']
    Cut UV edges when flipping some components on a UV shell   C: Default is on.   Q: When queried, returns an int.

-----------------------------------------

ft    : flipType        [int] ['query', 'edit']
    Flip along U or V direction.  | 0 | Horizontal

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    Set to true if the new node created should inserted before any deformer nodes.

-----------------------------------------

l     : local           [boolean] ['query', 'edit']
    Flips in the local space of the input faces.   C: Default is on.   Q: When queried, returns an int.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pu    : pivotU          [float] ['query', 'edit']
    Specifies the pivot value, in the U direction.

-----------------------------------------

pv    : pivotV          [float] ['query', 'edit']
    Specifies the pivot value, in the V direction.

-----------------------------------------

up    : usePivot        [boolean] ['query', 'edit']
    Flip using pivot or not.   C: Default is off.   Q: When queried, returns an int.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyForceUV(cp=1,cm=1,fh=1,fv=1,g=1,l=1,nor="string",ni="uint",par=1,uni=1,u=1,uvs="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyForceUV.html



-----------------------------------------

polyForceUV is undoable, NOT queryable, and NOT editable.

A set of functionalities can be called through this command. The input for
this command is a set of faces. Based on the arguments passed, the UVs for
these selected faces can be created.  
Project UVs based on the camera: (UV creation)  
Based on the current view direction/orientation, the UVs are generated and
assigned to the faces. Any previously assigned UV information will be lost.  
Best Plane Projection: (UV creation)  
The UVs are computed based on the plane defined by the user, and is applied to
the selected faces. This tool has 2 phases. In the first phase, the faces to
be mapped (faces to which UVs are to be created) are selected. In the second
phase, the points (vertices, CVs) that define the projecting plane are
selected. Any previously assigned UV information will be lost.  
Unitize: (UV creation)  
A new set of unitized UVs are generated and assigned to the faces. Any
previously assigned UV information will be lost.  
Unshare: (UV creation)  
Force the specified UV to be unshared by possibly creating new UVs. Any
previously assigned UV information will be lost.


-----------------------------------------


Return Value:

boolean  true/false


-----------------------------------------


Flags:

-----------------------------------------

cp    : cameraProjection [boolean] []
    Project the UVs based on the camera position/orientation

-----------------------------------------

cm    : createNewMap    [boolean] []
    Create new map if it does not exist.

-----------------------------------------

fh    : flipHorizontal  [boolean] []
    OBSOLETE flag. Use polyFlipUV instead.

-----------------------------------------

fv    : flipVertical    [boolean] []
    OBSOLETE flag. Use polyFlipUV instead.

-----------------------------------------

g     : g               [boolean] []
    OBSOLETE flag.

-----------------------------------------

l     : local           [boolean] []
    OBSOLETE flag.

-----------------------------------------

nor   : normalize       [string] []
    OBSOLETE flag. Use polyNormalizeUV instead.

-----------------------------------------

ni    : numItems        [uint] []
    This flag is only used for the best plane texturing of polygonal faces. This flag should be followed by a selection list. If not specified, the selected objects will be used (in the order they were selected).   This flag specifies the number of items (leading) in the selection list that should be used for the mapping. The trailing items will be used for computing the plane (See example below). The best plane texturing is better suited for using interactively from within its context. You can type "BestPlaneTexturingTool" in the command window OR (EditPolygons->Texture->BestPlaneTexturing from the Menu) to enter its context.

-----------------------------------------

par   : preserveAspectRatio [boolean] []
    OBSOLETE flag.

-----------------------------------------

uni   : unitize         [boolean] []
    To unitize the UVs of the selected faces

-----------------------------------------

u     : unshare         [boolean] []
    To unshare tye specified UV

-----------------------------------------

uvs   : uvSetName       [string]
    Specifies name of the uv set to work on

    """

def polyGeoSampler(e=1,abl="string",ac=1,amx="float",amn="float",cmx="[float, float, float]",cmn="[float, float, float]",cbl="string",cdo=1,cs=1,dg=1,fs=1,ids=1,lo=1,rs=1,bf=1,sf="float",su=1,ul=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyGeoSampler.html



-----------------------------------------

polyGeoSampler is undoable, NOT queryable, and editable.

This command performs a render sampling of surface color and transparency for
each selected vertex or face and stores the sampled data as either the color
value, or uses the sampled data to displace the affected vertices or faces by
a sampled data value. Transparency is not used for displacement, and
displacement is performed along vertex normals. The sampled data value used
can be pre-scaled by a user defined amount. Additionally, the normals chosen
for sampling can be overridden using a "flat" shading option. This option
basically means to always use the normals of the faces when computing sampling
values. This may be a desired if the user wishes to override an edge
smoothness factor. Basically with the "flat" shading option on, edges are
always considered to be hard. Note that displacement sampling will result in
the -sampleByFace option to be turned off, since a displacement of a vertex
always affects the faces the vertex is connected to. Finally, it is possible
to force the storage of shared colors per vertex, and / or force the usage of
unshared UV values. The computation of the resulting color is as follows:

    
    
            resulting-RGB = (sampled-RGB * scale-factor);
            if (color blend is none)
                    resulting-RGB = geometry-RGB
            else if (color blend is add)
                    resulting-RGB = geometry-RGB + sampled-RGB;
            else if (color blend is subtract)
                    resulting-RGB = geometry-RGB - sampled-RGB;
            else if (color blend is multiply)
                    resulting-RGB = geometry-RGB * sampled-RGB;
            else if (color blend is divide)
                    resulting-RGB = geometry-RGB / sampled-RGB;
            else if (color blend is average)
                    resulting-RGB = (geometry-RGB * 1/2) + (sampled-RGB * 1/2);
            if (clamp option set)
                    clamp resulting-RGB between minimum-RGB and maximum-RGB,
    

The analogous computation is done for computing the resulting alpha value. The
command requires that there be a camera selected in your scene in order to
work properly in -batch or -prompt mode.


-----------------------------------------


Return Value:

boolean  Success or Failure


-----------------------------------------


Flags:

-----------------------------------------

abl   : alphaBlend      [string] ['edit']
    When specified, indicates the type of alpha blend to be applied. Options are: "none", "overwrite", "add", "subtract", "multiply", "divide", "average". This option only applies when colors are being set. The default if this argument is not specified is "overwrite". The "none" options to not overwrite the existing value.

-----------------------------------------

ac    : averageColor    [boolean] ['edit']
    When used, will mean to force the storage of shared colors for vertex level sampling. By default vertex level sampling stores unshared colors.

-----------------------------------------

amx   : clampAlphaMax   [float] ['edit']
    When used, will mean to clamp the storage of alpha to a maximum

-----------------------------------------

amn   : clampAlphaMin   [float] ['edit']
    When used, will mean to clamp the storage of alpha to a minimum

-----------------------------------------

cmx   : clampRGBMax     [[float, float, float]] ['edit']
    When used, will mean to clamp the storage of RGB color to a maximum

-----------------------------------------

cmn   : clampRGBMin     [[float, float, float]] ['edit']
    When used, will mean to clamp the storage of RGB color to a minimum

-----------------------------------------

cbl   : colorBlend      [string] ['edit']
    When specified, indicates the type of color blend to be applied. Options are: "none", "overwrite", "add", "subtract", "multiply", "divide", "average". This option only applies when colors are being set. The default if this argument is not specified is "overwrite". The "none" options to not overwrite the existing value.

-----------------------------------------

cdo   : colorDisplayOption [boolean] ['edit']
    Change the display options on the mesh to display the vertex colors.

-----------------------------------------

cs    : computeShadows  [boolean] ['edit']
    When used, shadow maps will be computed, saved, and reused during the sampling process.

-----------------------------------------

dg    : displaceGeometry [boolean] ['edit']
    When used, geometry will be displaced along the normals at the sampling positions, as opposed to storing color values. The default is to store colors.

-----------------------------------------

fs    : flatShading     [boolean] ['edit']
    When used, flat shaded sampling will be computed. The default is smooth shading.

-----------------------------------------

ids   : ignoreDoubleSided [boolean] ['edit']
    When specified, the double sided flag will be ignored for prelighting.

-----------------------------------------

lo    : lightingOnly    [boolean] ['edit']
    When used, incoming illumination will be computed as opposed to surface color an tranparency

-----------------------------------------

rs    : reuseShadows    [boolean] ['edit']
    When used, if shadow maps were previosly computed and saved, then they will be reused during the sampling process. The computeShadows option must be enabled for this option to apply.

-----------------------------------------

bf    : sampleByFace    [boolean] ['edit']
    When used, sample will occur at a per face level versus a per vertex level, which is the default behaviour

-----------------------------------------

sf    : scaleFactor     [float] ['edit']
    When used, will scale the sampled value by the specified amount. The default scale factor is 1.0. Negative values are acceptable for displacement, but not for color values.

-----------------------------------------

su    : shareUV         [boolean] ['edit']
    When used, UVs are shared at a vertex when sampled. By default UVs are forced to be unshared.

-----------------------------------------

ul    : useLightShadows [boolean]
    When used, will use each lights shadow map options. Otherwise these options will be overrridden when the computeShadows, and/or reusedShadows option is enabled.

    """

def polyHelix(q=1,e=1,cch=1,c="float",ch=1,cuv="int",d="int",h="linear",n="string",nds="int",o=1,r="linear",rcp=1,sa="int",sc="int",sco="int",tx="int",oib=1,w="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyHelix.html



-----------------------------------------

polyHelix is undoable, queryable, and editable.

The polyHelix command creates a new polygonal helix.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

c     : coils           [float] ['query', 'edit']
    Number of coils.   Default: 3

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [int] ['query', 'edit']
    Create UVs or not.    * 0: No UVs   * 1: No Normalization   * 2: Normalize   * 3: Normalize and Preserve Aspect Ratio     Default: 2

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    What should be the direction of the coil. 0=Clockwise; 1=Counterclockwise   Default: 1

-----------------------------------------

h     : height          [linear] ['query', 'edit']
    Height of the helix.   Default: 2.0

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    Radius of tube.   Default: 0.4

-----------------------------------------

rcp   : roundCap        [boolean] ['query', 'edit']
    To indicate whether we need a round cap   Default: false

-----------------------------------------

sa    : subdivisionsAxis [int] ['query', 'edit']
    Subdivisions around the axis.   Default: 8

-----------------------------------------

sc    : subdivisionsCaps [int] ['query', 'edit']
    Subdivisions along the thickness caps.   Default: 0

-----------------------------------------

sco   : subdivisionsCoil [int] ['query', 'edit']
    Subdivisions along the coil.   Default: 50

-----------------------------------------

tx    : texture         [int] ['query', 'edit']
    What texture mechanism to be applied 0=No textures; 1=Object; 2=Faces   Default: 2

-----------------------------------------

oib   : useOldInitBehaviour [boolean] ['query', 'edit']
    Create the helix with base on the origin as in Maya V8.0 and below Otherwise create helix centred at origin   Default: false

-----------------------------------------

w     : width           [linear]
    Width of the helix.   Default: 2.0

    """

def polyHole(q=1,e=1,ah=1,ch=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyHole.html



-----------------------------------------

polyHole is undoable, queryable, and editable.

Command to set and clear holes on given faces.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ah    : assignHole      [boolean] ['query', 'edit']
    Assign the selected faces to be hole or unassign the hole faces to be non-hole. By default, the command will assign faces to be hole.

-----------------------------------------

ch    : createHistory   [boolean]
    For objects that have no construction history, this flag can be used to force the creation of construction history for hole. By default, history is not created if the object has no history. Regardless of this flag, history is always created if the object already has history.

    """

def polyInfo(ef=1,ev=1,fn=1,fe=1,fv=1,ie=1,iv=1,lf=1,nme=1,nue=1,nuv=1,nmv=1,ve=1,vf=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyInfo.html



-----------------------------------------

polyInfo is NOT undoable, NOT queryable, and NOT editable.

Command queries topological information on polygonal objects and components.
So, the command will require the following to be specified: \- selection list
to query


-----------------------------------------


Return Value:

string  Components


-----------------------------------------


Flags:

-----------------------------------------

ef    : edgeToFace      [boolean] []
    Returns the faces that share the specified edge. Requires edges to be selected.

-----------------------------------------

ev    : edgeToVertex    [boolean] []
    Returns the vertices defining an edge. Requires edges to be selected.

-----------------------------------------

fn    : faceNormals     [boolean] []
    Returns face normals of the specified object. If faces are selected the command returns the face normals of selected faces. Else it returns the face normals of all the faces of the object.

-----------------------------------------

fe    : faceToEdge      [boolean] []
    Returns the edges defining a face. Requires faces to be selected.

-----------------------------------------

fv    : faceToVertex    [boolean] []
    Returns the vertices defining a face. Requires faces to be selected.

-----------------------------------------

ie    : invalidEdges    [boolean] []
    Find all edges that are not associated with any face in the mesh.

-----------------------------------------

iv    : invalidVertices [boolean] []
    Find all vertices that are not associated with any face in the mesh.

-----------------------------------------

lf    : laminaFaces     [boolean] []
    Find all lamina faces in the specified objects.

-----------------------------------------

nme   : nonManifoldEdges [boolean] []
    Find all non-manifold edges in the specified objects.

-----------------------------------------

nue   : nonManifoldUVEdges [boolean] []
    Find all non-manifold UV edges in the specified objects.

-----------------------------------------

nuv   : nonManifoldUVs  [boolean] []
    Find all non-manifold UVs in the specified objects.

-----------------------------------------

nmv   : nonManifoldVertices [boolean] []
    Find all non-manifold vertices in the specified objects.

-----------------------------------------

ve    : vertexToEdge    [boolean] []
    Returns the Edges connected to a vertex. Requires vertices to be selected.

-----------------------------------------

vf    : vertexToFace    [boolean]
    Returns the faces that share the specified vertex. Requires vertices to be selected.

    """

def polyInstallAction(q=1,cn=1,cs=1,ic=1,id=1,ki=1,uc=1,ud=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyInstallAction.html



-----------------------------------------

polyInstallAction is undoable, queryable, and NOT editable.

Installs/uninstalls several things to help the user to perform the specified
action :

  * Pickmask
  * Internal selection constraints
  * Display attributes


-----------------------------------------


Return Value:

string[]  When installing constraint, returns as an array of strings the items
on which the installed command will act on. otherwise, returns nothing    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cn    : commandName     [boolean] ['query']
    return as a string the name of the command previously installed

-----------------------------------------

cs    : convertSelection [boolean] []
    convert all polys selected in object mode into their full matching component selection. For example : if a polyMesh is selected,   polyInstallAction -cs polyCloseBorder   will select all border edges.

-----------------------------------------

ic    : installConstraint [boolean] ['query']
    C: install selection pickmask and internal constraints for actionname   Q: returns 1 if any internal constraint is set for current action

-----------------------------------------

id    : installDisplay  [boolean] ['query']
    C: install display attributes for actionname   Q: returns 1 if any display is set for current action

-----------------------------------------

ki    : keepInstances   [boolean] []
    Convert components for all selected instances rather than only the first selected instance.

-----------------------------------------

uc    : uninstallConstraint [boolean] []
    uninstall internal constraints previously installed

-----------------------------------------

ud    : uninstallDisplay [boolean]
    uninstall display attributes previously installed

    """

def polyLayoutUV(q=1,e=1,cch=1,ch=1,fr=1,l="int",lm="int",n="string",nds="int",ps="float",rbf="int",sc="int",se="int",uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyLayoutUV.html



-----------------------------------------

polyLayoutUV is undoable, queryable, and editable.

Move UVs in the texture plane to avoid overlaps.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

fr    : flipReversed    [boolean] ['query', 'edit']
    If this flag is turned on, the reversed UV pieces are fliped.

-----------------------------------------

l     : layout          [int] ['query', 'edit']
    How to move the UV pieces, after cuts are applied:   0 No move is applied.   1 Layout the pieces along the U axis.   2 Layout the pieces in a square shape.

-----------------------------------------

lm    : layoutMethod    [int] ['query', 'edit']
    Which layout method to use:   0 Block Stacking.   1 Shape Stacking.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ps    : percentageSpace [float] ['query', 'edit']
    When layout is set to square, this value is a percentage of the texture area which is added around each UV piece. It can be used to ensure each UV piece uses different pixels in the texture.   Maximum value is 5 percent.

-----------------------------------------

rbf   : rotateForBestFit [int] ['query', 'edit']
    0 No rotation is applied. 1 Only allow 90 degree rotations. 2 Allow free rotations.

-----------------------------------------

sc    : scale           [int] ['query', 'edit']
    How to scale the pieces, after move and cuts:   0 No scale is applied.   1 Uniform scale to fit in unit square.   2 Non proportional scale to fit in unit square.

-----------------------------------------

se    : separate        [int] ['query', 'edit']
    Which UV edges should be cut:   0 No cuts.   1 Cut only along folds.   2 Make all necessary cuts to avoid all intersections.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyListComponentConversion(bo=1,fe=1,ff=1,fuv=1,fv=1,fvf=1,internal=1,te=1,tf=1,tuv=1,tv=1,tvf=1,uvs=1,vfa=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyListComponentConversion.html



-----------------------------------------

polyListComponentConversion is undoable, NOT queryable, and NOT editable.

This command converts poly components from one or more types to another one or
more types, and returns the list of the conversion. It does not change
anything of the current database.


-----------------------------------------


Return Value:

selectionItem[]  List of poly components


-----------------------------------------


Flags:

-----------------------------------------

bo    : border          [boolean] []
    Indicates that the converted components must be on the border of the selection. If it is not provided, the converted components will be the related ones.

-----------------------------------------

fe    : fromEdge        [boolean] []
    

-----------------------------------------

ff    : fromFace        [boolean] []
    

-----------------------------------------

fuv   : fromUV          [boolean] []
    

-----------------------------------------

fv    : fromVertex      [boolean] []
    

-----------------------------------------

fvf   : fromVertexFace  [boolean] []
    Indicates the component type to convert from. If none of them is provided, it is assumed to be all of them, including poly objects.

-----------------------------------------

internal : internal        [boolean] []
    Indicates that the converted components must be totally envolved by the source components. E.g. a converted face must have all of its surrounding vertices being given. If it is not provided, the converted components will be the related ones.

-----------------------------------------

te    : toEdge          [boolean] []
    

-----------------------------------------

tf    : toFace          [boolean] []
    

-----------------------------------------

tuv   : toUV            [boolean] []
    

-----------------------------------------

tv    : toVertex        [boolean] []
    

-----------------------------------------

tvf   : toVertexFace    [boolean] []
    Indicates the component type to convert to. If none of them is provided, it is assumed to the object.

-----------------------------------------

uvs   : uvShell         [boolean] []
    Will return UV components within the same UV shell. Only works with -tuv and -fuv flags.

-----------------------------------------

vfa   : vertexFaceAllEdges [boolean]
    When converting from face vertices to edges, indicates that all edges with an end at the face vertex should be included. Without this flag, the default behaviour is to only include one edge per face vertex.

    """

def polyMapCut(q=1,e=1,cch=1,ch=1,mvr="float",n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMapCut.html



-----------------------------------------

polyMapCut is undoable, queryable, and editable.

Cut along edges of the texture mapping. The cut edges become map borders.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

mvr   : moveratio       [float] ['query', 'edit']
    Cut open ratio related to the neighbor edge length of cut edge.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyMapDel(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMapDel.html



-----------------------------------------

polyMapDel is undoable, queryable, and editable.

Deletes texture coordinates (UVs) from selected faces.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyMapSew(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMapSew.html



-----------------------------------------

polyMapSew is undoable, queryable, and editable.

Sew border edges in texture space. Selected edges must be map borders.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyMapSewMove(q=1,e=1,cch=1,ch=1,lps=1,n="string",nds="int",nf="int",uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMapSewMove.html



-----------------------------------------

polyMapSewMove is undoable, queryable, and editable.

This command can be used to Move and Sew together separate UV pieces along
geometric edges. UV pieces that correspond to the same geometric edge, are
merged together by moving the smaller piece to the larger one.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

lps   : limitPieceSize  [boolean] ['query', 'edit']
    When on, this flag specifies that the face number limit described above should be used.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nf    : numberFaces     [int] ['query', 'edit']
    Maximum number of faces in a UV piece. When trying to combine two UV pieces into a single one, the merge operation is rejected if the smaller piece has more faces than the number specified by this flag.   This flag is only used when limitPieceSize is set to on.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyMergeEdge(q=1,e=1,cch=1,ch=1,fe="int",mm="int",mt=1,n="string",nds="int",se="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMergeEdge.html



-----------------------------------------

polyMergeEdge is undoable, queryable, and editable.

Sews two border edges together.  
The new edge is located either on the first, last, or between both selected
edges, depending on the mode.

Both edges must belong to the same object, and orientations must match (i.e.
normals on corresponding faces must point in the same direction).  
Edge flags are mandatory.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

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

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

se    : secondEdge      [int]
    Second edge to merge. Invalid default value to force the value to be set.   Default: -1

    """

def polyMergeFacet(q=1,e=1,cch=1,ch=1,ff="int",mm="int",n="string",nds="int",sf="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMergeFacet.html



-----------------------------------------

polyMergeFacet is undoable, queryable, and editable.

The second face becomes a hole in the first face.  
The new holed face is located either on the first, last, or between both
selected faces, depending on the mode.

Both faces must belong to the same object.  
Facet flags are mandatory.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

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

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

sf    : secondFacet     [int]
    The number of the second (hole) face to merge.

    """

def polyMergeUV(q=1,e=1,cch=1,ch=1,d="float",n="string",nds="int",uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMergeUV.html



-----------------------------------------

polyMergeUV is undoable, queryable, and editable.

Merge UVs of an object based on their distance. UVs are merge only if they
belong to the same 3D vertex.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

d     : distance        [float] ['query', 'edit']
    This flag specifies the maximum distance to merge UVs.   C: Default is 0.0.   Q: When queried, this flag returns a double.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyMergeVertex(q=1,e=1,am=1,cch=1,ch=1,d="linear",mtc="string",n="string",nds="int",tx=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMergeVertex.html



-----------------------------------------

polyMergeVertex is undoable, queryable, and editable.

Merge vertices within a given threshold.  
Since this allows merging any vertices that lie on the same object it is
possible for the resulting geometry to be non-manifold.  

First, perform comparison of pairs of selected vertices. Pairs that lie within
given distance of one another are merged, along with the edge between them.  

Second, any selected vertices which share an edge are merged if the distance
between them is within the specified distance.  

Unlike Merge Edges, Merge Vertices will perform the merge even if the edges
adjoining the vertices do not have matching orientation (i.e. normals of
adjacent faces do not point in the same direction). As this restriction is not
enforced while merging vertices, resulting geometry can be non-manifold.  

If alwaysMergeTwoVertices is set and there are only two vertices, tolerance is
ignored and the vertices will be merged.  

Resulting mesh may have extra vertices or edges to ensure geometry is valid.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

am    : alwaysMergeTwoVertices [boolean] ['query', 'edit']
    This flag specifies whether to always merge if only two vertices are selected regardless of distance.   C: Default is false.   Q: When queried, this flag returns a boolean.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

d     : distance        [linear] ['query', 'edit']
    This flag specifies the distance within which vertices will be merged.   C: Default is 0.0 (i.e. vertices are coincident).   Q: When queried, this flag returns a double.

-----------------------------------------

mtc   : mergeToComponents [string] ['query', 'edit']
    Optionally defines the position to merge all of the vertices to. If set, the distance flag will be ignored, and instead the center point of the set components will be calculated and all vertices will be merged to that location.   C: Default is empty string.   Q: When queried, this flag returns a string.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tx    : texture         [boolean] ['query', 'edit']
    This flag specifies whether the texture is sewn in addition to the 3d edge   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyMirrorFace(q=1,e=1,a="int",ad="int",cch=1,ch=1,d="int",mm="int",mt="linear",mtt="int",ma="int",mps="linear",n="string",nds="int",p="[linear, linear, linear]",px="linear",py="linear",pz="linear",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMirrorFace.html



-----------------------------------------

polyMirrorFace is undoable, queryable, and editable.

Mirror all the faces of the selected object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : axis            [int] ['query', 'edit']
    Axis to mirror the object along   Default: 0

-----------------------------------------

ad    : axisDirection   [int] ['query', 'edit']
    Direction to mirror the object along   Default: 1

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    Direction to mirror the object along   Default: 0

-----------------------------------------

mm    : mergeMode       [int] ['query', 'edit']
    Merge mode to apply   Default: 1

-----------------------------------------

mt    : mergeThreshold  [linear] ['query', 'edit']
    Tolerance to determine whether vertices should be merged.   Default: 0.001

-----------------------------------------

mtt   : mergeThresholdType [int] ['query', 'edit']
    Merge mode to apply   Default: 0

-----------------------------------------

ma    : mirrorAxis      [int] ['query', 'edit']
    Mirror axis type selection   Default: 2

-----------------------------------------

mps   : mirrorPosition  [linear] ['query', 'edit']
    Custom mirror axis position   Default: 0.0

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    Pivot point of the mirror plane.   Default: 0.0, 0.0, 0.0

-----------------------------------------

px    : pivotX          [linear] ['query', 'edit']
    Translation X coord.

-----------------------------------------

py    : pivotY          [linear] ['query', 'edit']
    Translation Y coord.

-----------------------------------------

pz    : pivotZ          [linear] ['query', 'edit']
    Translation Z coord.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyMoveEdge(q=1,e=1,cch=1,ch=1,ga="float",lc="int",ld="[linear, linear, linear]",ldx="linear",ldy="linear",ldz="linear",lr="[angle, angle, angle]",lrx="angle",lry="angle",lrz="angle",ls="[float, float, float]",lsx="float",lsy="float",lsz="float",lt="[linear, linear, linear]",ltx="linear",lty="linear",ltz="linear",n="string",nds="int",pvt="[linear, linear, linear]",pvx="linear",pvy="linear",pvz="linear",ran="float",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",s="[float, float, float]",sx="float",sy="float",sz="float",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMoveEdge.html



-----------------------------------------

polyMoveEdge is undoable, queryable, and editable.

Modifies edges of a polygonal object. Translate, move, rotate or scale edges.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ga    : gain            [float] ['query', 'edit']
    Gain factor per component. Can be painted using Artisan.   Default: 1.0

-----------------------------------------

lc    : localCenter     [int] ['query', 'edit']
    Local center on the edge : 0=Middle point, 1=Start point, 2=End point.   Default: 0

-----------------------------------------

ld    : localDirection  [[linear, linear, linear]] ['query', 'edit']
    Direction to determine X axis for local space.   Default: 1.0, 0.0, 0.0

-----------------------------------------

ldx   : localDirectionX [linear] ['query', 'edit']
    X coord of the X axis.

-----------------------------------------

ldy   : localDirectionY [linear] ['query', 'edit']
    Y coord of the X axis.

-----------------------------------------

ldz   : localDirectionZ [linear] ['query', 'edit']
    Z coord of the X axis.

-----------------------------------------

lr    : localRotate     [[angle, angle, angle]] ['query', 'edit']
    The local rotations.   Default: 0.0, 0.0, 0.0

-----------------------------------------

lrx   : localRotateX    [angle] ['query', 'edit']
    Local rotate X coord. The range is [0, 360].

-----------------------------------------

lry   : localRotateY    [angle] ['query', 'edit']
    Local rotate Y coord. The range is [0, 360].

-----------------------------------------

lrz   : localRotateZ    [angle] ['query', 'edit']
    Local rotate Z coord : Rotation along the normal. The range is [0, 360].

-----------------------------------------

ls    : localScale      [[float, float, float]] ['query', 'edit']
    Local Scale.   Default: 1.0, 1.0, 1.0

-----------------------------------------

lsx   : localScaleX     [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

lsy   : localScaleY     [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

lsz   : localScaleZ     [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

lt    : localTranslate  [[linear, linear, linear]] ['query', 'edit']
    Local translate.   Default: 0.0, 0.0, 0.0

-----------------------------------------

ltx   : localTranslateX [linear] ['query', 'edit']
    Local translation X coord.

-----------------------------------------

lty   : localTranslateY [linear] ['query', 'edit']
    Local translation Y coord.

-----------------------------------------

ltz   : localTranslateZ [linear] ['query', 'edit']
    Local translation Z coord : Move along the normal.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pvt   : pivot           [[linear, linear, linear]] ['query', 'edit']
    The pivot for scaling and rotation.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pvx   : pivotX          [linear] ['query', 'edit']
    Pivot X coord.

-----------------------------------------

pvy   : pivotY          [linear] ['query', 'edit']
    Pivot Y coord.

-----------------------------------------

pvz   : pivotZ          [linear] ['query', 'edit']
    Pivot Z coord.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    Random value for all parameters.   Default: 0.0

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    Rotation angles around X, Y, Z.   Default: 0.0, 0.0, 0.0

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    Rotation angle around X.

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    Rotation angle around Y.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    Rotation angle around Z.

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    Scaling vector.   Default: 1.0, 1.0, 1.0

-----------------------------------------

sx    : scaleX          [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

sy    : scaleY          [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

sz    : scaleZ          [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

t     : translate       [[linear, linear, linear]] ['query', 'edit']
    Translation vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

tx    : translateX      [linear] ['query', 'edit']
    Translation X coord.

-----------------------------------------

ty    : translateY      [linear] ['query', 'edit']
    Translation Y coord.

-----------------------------------------

tz    : translateZ      [linear] ['query', 'edit']
    Translation Z coord.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyMoveFacet(q=1,e=1,att="float",cch=1,ch=1,ga="float",g="[linear, linear, linear]",gx="linear",gy="linear",gz="linear",lc="int",ld="[linear, linear, linear]",ldx="linear",ldy="linear",ldz="linear",lr="[angle, angle, angle]",lrx="angle",lry="angle",lrz="angle",ls="[float, float, float]",lsx="float",lsy="float",lsz="float",lt="[linear, linear, linear]",ltx="linear",lty="linear",ltz="linear",mx="linear",my="linear",mz="linear",m="[linear, linear, linear]",n="string",nds="int",off="float",pvt="[linear, linear, linear]",pvx="linear",pvy="linear",pvz="linear",ran="float",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",s="[float, float, float]",sx="float",sy="float",sz="float",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",w="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMoveFacet.html



-----------------------------------------

polyMoveFacet is undoable, queryable, and editable.

Modifies facet of a polygonal object. Translate, move, rotate or scale facets.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attraction      [float] ['query', 'edit']
    Attraction, related to magnet. The range is [-2.0, 2.0].   Default: 0.0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ga    : gain            [float] ['query', 'edit']
    Gain factor per component. Can be painted using Artisan.   Default: 1.0

-----------------------------------------

g     : gravity         [[linear, linear, linear]] ['query', 'edit']
    The gravity vector.   Default: 0.0, -1.0, 0.0

-----------------------------------------

gx    : gravityX        [linear] ['query', 'edit']
    Gravity X coord.

-----------------------------------------

gy    : gravityY        [linear] ['query', 'edit']
    Gravity Y coord.

-----------------------------------------

gz    : gravityZ        [linear] ['query', 'edit']
    Gravity Z coord.

-----------------------------------------

lc    : localCenter     [int] ['query', 'edit']
    Local center on the edge : 0=Middle point, 1=Start point, 2=End point.   Default: 0

-----------------------------------------

ld    : localDirection  [[linear, linear, linear]] ['query', 'edit']
    Direction to determine X axis for local space.   Default: 1.0, 0.0, 0.0

-----------------------------------------

ldx   : localDirectionX [linear] ['query', 'edit']
    X coord of the X axis.

-----------------------------------------

ldy   : localDirectionY [linear] ['query', 'edit']
    Y coord of the X axis.

-----------------------------------------

ldz   : localDirectionZ [linear] ['query', 'edit']
    Z coord of the X axis.

-----------------------------------------

lr    : localRotate     [[angle, angle, angle]] ['query', 'edit']
    The local rotations.   Default: 0.0, 0.0, 0.0

-----------------------------------------

lrx   : localRotateX    [angle] ['query', 'edit']
    Local rotate X coord. The range is [0, 360].

-----------------------------------------

lry   : localRotateY    [angle] ['query', 'edit']
    Local rotate Y coord. The range is [0, 360].

-----------------------------------------

lrz   : localRotateZ    [angle] ['query', 'edit']
    Local rotate Z coord : Rotation along the normal. The range is [0, 360].

-----------------------------------------

ls    : localScale      [[float, float, float]] ['query', 'edit']
    Local Scale.   Default: 1.0, 1.0, 1.0

-----------------------------------------

lsx   : localScaleX     [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

lsy   : localScaleY     [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

lsz   : localScaleZ     [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

lt    : localTranslate  [[linear, linear, linear]] ['query', 'edit']
    Local translate.   Default: 0.0, 0.0, 0.0

-----------------------------------------

ltx   : localTranslateX [linear] ['query', 'edit']
    Local translation X coord.

-----------------------------------------

lty   : localTranslateY [linear] ['query', 'edit']
    Local translation Y coord.

-----------------------------------------

ltz   : localTranslateZ [linear] ['query', 'edit']
    Local translation Z coord : Move along the normal.

-----------------------------------------

mx    : magnX           [linear] ['query', 'edit']
    Magnet X coord.

-----------------------------------------

my    : magnY           [linear] ['query', 'edit']
    Magnet Y coord.

-----------------------------------------

mz    : magnZ           [linear] ['query', 'edit']
    Magnet Z coord.

-----------------------------------------

m     : magnet          [[linear, linear, linear]] ['query', 'edit']
    The magnet vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

off   : offset          [float] ['query', 'edit']
    Local offset. Faces are moved this distance towards the inside of the face.   Default: 0.0

-----------------------------------------

pvt   : pivot           [[linear, linear, linear]] ['query', 'edit']
    The pivot for scaling and rotation.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pvx   : pivotX          [linear] ['query', 'edit']
    Pivot X coord.

-----------------------------------------

pvy   : pivotY          [linear] ['query', 'edit']
    Pivot Y coord.

-----------------------------------------

pvz   : pivotZ          [linear] ['query', 'edit']
    Pivot Z coord.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    Random value for all parameters.   Default: 0.0

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    Rotation angles around X, Y, Z.   Default: 0.0, 0.0, 0.0

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    Rotation angle around X.

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    Rotation angle around Y.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    Rotation angle around Z.

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    Scaling vector.   Default: 1.0, 1.0, 1.0

-----------------------------------------

sx    : scaleX          [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

sy    : scaleY          [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

sz    : scaleZ          [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

t     : translate       [[linear, linear, linear]] ['query', 'edit']
    Translation vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

tx    : translateX      [linear] ['query', 'edit']
    Translation X coord.

-----------------------------------------

ty    : translateY      [linear] ['query', 'edit']
    Translation Y coord.

-----------------------------------------

tz    : translateZ      [linear] ['query', 'edit']
    Translation Z coord.

-----------------------------------------

w     : weight          [float] ['query', 'edit']
    The weight, related to gravity.   Default: 0.0

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyMoveFacetUV(q=1,e=1,l="[float, float]",lx="float",ly="float",cch=1,ch=1,n="string",nds="int",pvt="[float, float]",pvu="float",pvv="float",ran="float",ra="angle",s="[float, float]",su="float",sv="float",t="[float, float]",tu="float",tv="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMoveFacetUV.html



-----------------------------------------

polyMoveFacetUV is undoable, queryable, and editable.

Modifies the map by moving all UV values associated with the selected face(s).

The UV coordinates of the model are manipulated without changing the vertices
of the 3D object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : axisLen         [[float, float]] ['query', 'edit']
    Axis Length vector, used to draw the manip handles.   C: Default is 1.0, 1.0   Q: When queried, this flag returns a float[2].

-----------------------------------------

lx    : axisLenX        [float] ['query', 'edit']
    Axis Length in X, used to draw the manip handles.   C: Default is 1.0   Q: When queried, this flag returns a float.

-----------------------------------------

ly    : axisLenY        [float] ['query', 'edit']
    Axis Length in Y, used to draw the manip handles.   C: Default is 1.0   Q: When queried, this flag returns a float.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pvt   : pivot           [[float, float]] ['query', 'edit']
    This flag specifies the pivot for scaling and rotation.   C: Default is 0.0 0.0.   Q: When queried, this flag returns a float[2].

-----------------------------------------

pvu   : pivotU          [float] ['query', 'edit']
    This flag specifies U for the pivot for scaling and rotation.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pvv   : pivotV          [float] ['query', 'edit']
    This flag specifies V for the pivot for scaling and rotation.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    This flag specifies the random value for all parameters.   C: Default is 0.0. The range is [-10.0, 10.0].   Q: When queried, this flag returns a float.

-----------------------------------------

ra    : rotationAngle   [angle] ['query', 'edit']
    Angle of rotation.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

s     : scale           [[float, float]] ['query', 'edit']
    This flag specifies the scaling vector.   C: Default is 1.0 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

su    : scaleU          [float] ['query', 'edit']
    This flag specifies U for the scaling vector.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

sv    : scaleV          [float] ['query', 'edit']
    This flag specifies V for the scaling vector.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

t     : translate       [[float, float]] ['query', 'edit']
    This flag specifies the translation vector.   C: Default is 0.0 0.0.   Q: When queried, this flag returns a float[2].

-----------------------------------------

tu    : translateU      [float] ['query', 'edit']
    This flag specifies the U translation vector.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

tv    : translateV      [float]
    This flag specifies the V translation vector.   C: Default is 0.0.   Q: When queried, this flag returns a float.

    """

def polyMoveUV(q=1,e=1,l="[float, float]",lx="float",ly="float",cch=1,ch=1,n="string",nds="int",pvt="[float, float]",pvu="float",pvv="float",ran="float",ra="angle",s="[float, float]",su="float",sv="float",t="[float, float]",tu="float",tv="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMoveUV.html



-----------------------------------------

polyMoveUV is undoable, queryable, and editable.

Moves selected UV coordinates in 2D space. As the selected UVs are adjusted,
the way the image is mapped onto the object changes accordingly. This command
manipulates the UV values without changing the 3D geometry of the object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : axisLen         [[float, float]] ['query', 'edit']
    AxisLen vector, used to draw the manip handles.   Default: 1.0, 1.0

-----------------------------------------

lx    : axisLenX        [float] ['query', 'edit']
    AxisLen X coord.

-----------------------------------------

ly    : axisLenY        [float] ['query', 'edit']
    AxisLen Y coord.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pvt   : pivot           [[float, float]] ['query', 'edit']
    The pivot for scaling and rotation.   Default: 0.5, 0.5

-----------------------------------------

pvu   : pivotU          [float] ['query', 'edit']
    Pivot U coord.

-----------------------------------------

pvv   : pivotV          [float] ['query', 'edit']
    Pivot V coord.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    Random value, added to all parameters.   Default: 0.0

-----------------------------------------

ra    : rotationAngle   [angle] ['query', 'edit']
    Angle of rotation.   Default: 0.0

-----------------------------------------

s     : scale           [[float, float]] ['query', 'edit']
    Scaling vector.   Default: 1.0, 1.0

-----------------------------------------

su    : scaleU          [float] ['query', 'edit']
    Scaling U coord.

-----------------------------------------

sv    : scaleV          [float] ['query', 'edit']
    Scaling V coord.

-----------------------------------------

t     : translate       [[float, float]] ['query', 'edit']
    Translation vector.   Default: 0.0, 0.0

-----------------------------------------

tu    : translateU      [float] ['query', 'edit']
    Translation U coord.

-----------------------------------------

tv    : translateV      [float]
    Translation V coord.

    """

def polyMoveVertex(q=1,e=1,cch=1,ch=1,ga="float",ld="[linear, linear, linear]",ldx="linear",ldy="linear",ldz="linear",lt="[linear, linear, linear]",ltx="linear",lty="linear",ltz="linear",n="string",nds="int",pvt="[linear, linear, linear]",pvx="linear",pvy="linear",pvz="linear",ran="float",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",s="[float, float, float]",sx="float",sy="float",sz="float",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMoveVertex.html



-----------------------------------------

polyMoveVertex is undoable, queryable, and editable.

Modifies vertices of a polygonal object. Translate, rotate or scale vertices
in local or world space.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ga    : gain            [float] ['query', 'edit']
    Gain factor per component. Can be painted using Artisan.   Default: 1.0

-----------------------------------------

ld    : localDirection  [[linear, linear, linear]] ['query', 'edit']
    Direction to determine X axis for local space.   Default: 1.0, 0.0, 0.0

-----------------------------------------

ldx   : localDirectionX [linear] ['query', 'edit']
    X coord of the X axis.

-----------------------------------------

ldy   : localDirectionY [linear] ['query', 'edit']
    Y coord of the X axis.

-----------------------------------------

ldz   : localDirectionZ [linear] ['query', 'edit']
    Z coord of the X axis.

-----------------------------------------

lt    : localTranslate  [[linear, linear, linear]] ['query', 'edit']
    Local translate.   Default: 0.0, 0.0, 0.0

-----------------------------------------

ltx   : localTranslateX [linear] ['query', 'edit']
    Local translation X coord.

-----------------------------------------

lty   : localTranslateY [linear] ['query', 'edit']
    Local translation Y coord.

-----------------------------------------

ltz   : localTranslateZ [linear] ['query', 'edit']
    Local translation Z coord : Move along the normal.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pvt   : pivot           [[linear, linear, linear]] ['query', 'edit']
    The pivot for scaling and rotation.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pvx   : pivotX          [linear] ['query', 'edit']
    Pivot X coord.

-----------------------------------------

pvy   : pivotY          [linear] ['query', 'edit']
    Pivot Y coord.

-----------------------------------------

pvz   : pivotZ          [linear] ['query', 'edit']
    Pivot Z coord.

-----------------------------------------

ran   : random          [float] ['query', 'edit']
    Random value for all parameters.   Default: 0.0

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    Rotation angles around X, Y, Z.   Default: 0.0, 0.0, 0.0

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    Rotation angle around X.

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    Rotation angle around Y.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    Rotation angle around Z.

-----------------------------------------

s     : scale           [[float, float, float]] ['query', 'edit']
    Scaling vector.   Default: 1.0, 1.0, 1.0

-----------------------------------------

sx    : scaleX          [float] ['query', 'edit']
    Scale X coord.

-----------------------------------------

sy    : scaleY          [float] ['query', 'edit']
    Scale Y coord.

-----------------------------------------

sz    : scaleZ          [float] ['query', 'edit']
    Scale Z coord.

-----------------------------------------

t     : translate       [[linear, linear, linear]] ['query', 'edit']
    Translation vector.   Default: 0.0, 0.0, 0.0

-----------------------------------------

tx    : translateX      [linear] ['query', 'edit']
    Translation X coord.

-----------------------------------------

ty    : translateY      [linear] ['query', 'edit']
    Translation Y coord.

-----------------------------------------

tz    : translateZ      [linear] ['query', 'edit']
    Translation Z coord.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyMultiLayoutUV(fr=1,gu="int",gv="int",l="int",lm="int",ou="float",ov="float",ps="float",psc="int",rbf="int",sc="int",su="float",sv="float",uvs="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyMultiLayoutUV.html



-----------------------------------------

polyMultiLayoutUV is undoable, NOT queryable, and NOT editable.

place the UVs of the selected polygonal objects so that they do not overlap.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

fr    : flipReversed    [boolean] []
    If this flag is turned on, the reversed UV pieces are fliped.

-----------------------------------------

gu    : gridU           [int] []
    The U size of the grids.

-----------------------------------------

gv    : gridV           [int] []
    The V size of the grids.

-----------------------------------------

l     : layout          [int] []
    How to move the UV pieces, after cuts are applied:   0 No move is applied.   1 Layout the pieces along the U axis.   2 Layout the pieces in a square shape.   3 Layout the pieces in grids.   4 Layout the pieces in nearest regions.

-----------------------------------------

lm    : layoutMethod    [int] []
    // -lm/layoutMethod layoutMethod integer // (C, E, Q) Which layout method to use: //   0 Block Stacking. //   1 Shape Stacking.

-----------------------------------------

ou    : offsetU         [float] []
    Offset the layout in the U direction by the given value.

-----------------------------------------

ov    : offsetV         [float] []
    Offset the layout in the V direction by the given value.

-----------------------------------------

ps    : percentageSpace [float] []
    When layout is set to square, this value is a percentage of the texture area which is added around each UV piece. It can be used to ensure each UV piece uses different pixels in the texture.   Maximum value is 5 percent.

-----------------------------------------

psc   : prescale        [int] []
    Prescale the shell before laying it out.   0 No scale is applied.   1 Object space scaling applied.   2 World space scaling applied.

-----------------------------------------

rbf   : rotateForBestFit [int] []
    How to rotate the pieces, before move:   0 No rotation is applied.   1 Only allow 90 degree rotations.   2 Allow free rotations.

-----------------------------------------

sc    : scale           [int] []
    How to scale the pieces, after move:   0 No scale is applied.   1 Uniform scale to fit in unit square.   2 Non proportional scale to fit in unit square.

-----------------------------------------

su    : sizeU           [float] []
    Scale the layout in the U direction by the given value.

-----------------------------------------

sv    : sizeV           [float] []
    Scale the layout in the V direction by the given value.

-----------------------------------------

uvs   : uvSetName       [string]
    Specifies the name of the uv set to edit uvs on. If not specified will use the current uv set if it exists.

    """

def polyNormal(q=1,e=1,cch=1,ch=1,n="string",nds="int",nm="int",unm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyNormal.html



-----------------------------------------

polyNormal is undoable, queryable, and editable.

Control the normals of an object. This command works on faces or polygonal
objects.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nm    : normalMode      [int] ['query', 'edit']
    Normal mode : 0=reverse, 1=propagate, 2=conform, 3=reverseAndCut, 4=reverseAndPropagate   Default: 0

-----------------------------------------

unm   : userNormalMode  [boolean]
    Determines if user normals needs to be reversed as well.   Default: true

    """

def polyNormalizeUV(q=1,e=1,cot=1,nd="int",nt="int",pa=1,cch=1,ch=1,cm=1,ibd=1,n="string",nds="int",uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyNormalizeUV.html



-----------------------------------------

polyNormalizeUV is undoable, queryable, and editable.

Normalizes the UVs of input polyFaces. The existing UVs of the faces are
normalized between 0 and 1.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cot   : centerOnTile    [boolean] ['query', 'edit']
    If true, will center UV's on the UV tile they are most over. If false, will center UV's in the 0-1 region.

-----------------------------------------

nd    : normalizeDirection [int] ['query', 'edit']
    Scale along U or V or both.  | 0 | UV

-----------------------------------------

nt    : normalizeType   [int] ['query', 'edit']
    Options for normalize.  | 0 | Separate

-----------------------------------------

pa    : preserveAspectRatio [boolean] ['query', 'edit']
    Scale uniform along u and v.   C: Default is on.   Q: When queried, returns an int.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] []
    Set to true if a new map should be created

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    Set to true if the new node created should inserted before any deformer nodes.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyNormalPerVertex(q=1,e=1,al=1,deformable=1,fn=1,x="float",xyz="[float, float, float]",y="float",z="float",rel=1,ufn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyNormalPerVertex.html



-----------------------------------------

polyNormalPerVertex is undoable, queryable, and editable.

Command associates normal(x, y, z) with vertices on polygonal objects. When
used with the query flag, it returns the normal associated with the specified
components. However, when queried, the command returns all normals (all vtx-
face combinations) on the vertex, regardless of whether they are shared or
not.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : allLocked       [boolean] ['query', 'edit']
    Queries if all normals on the selected vertices are locked (frozen) or not

-----------------------------------------

deformable : deformable      [boolean] ['query', 'edit']
    DEFAULT true OBSOLETE flag. This flag will be removed in the next release.

-----------------------------------------

fn    : freezeNormal    [boolean] ['query', 'edit']
    Specifies that the normal values be frozen (locked) at the current value.

-----------------------------------------

x     : normalX         [float] ['query', 'edit']
    Specifies the x value normal

-----------------------------------------

xyz   : normalXYZ       [[float, float, float]] ['query', 'edit']
    Specifies the xyz values normal If this flag is used singly, the specified normal xyz values are used for all selected components. If the flag is used multiple times, the number of uses must match the number of selected components, and each use specifies the normal of one component.

-----------------------------------------

y     : normalY         [float] ['query', 'edit']
    Specifies the y value normal

-----------------------------------------

z     : normalZ         [float] ['query', 'edit']
    Specifies the z value normal

-----------------------------------------

rel   : relative        [boolean] ['query', 'edit']
    When used, the normal values specified are added relative to the current value.

-----------------------------------------

ufn   : unFreezeNormal  [boolean]
    Specifies that the normal values that were frozen at the current value be un-frozen (un-locked).

    """

def polyOptions(q=1,ao=1,ae=1,bcv=1,bc=1,cm="string",cs=1,dal=1,db=1,dc=1,dce=1,dcv=1,dg=1,dif=1,din="[boolean, boolean, boolean, boolean]",dmb=1,dmt="[boolean, boolean, boolean]",dn=1,dsc=1,dtn=1,dt=1,uvt=1,duv=1,dv=1,dw=1,f=1,fb=1,gl=1,hb=1,he=1,hec=1,mb="string",np=1,pt=1,pf=1,r=1,rt=1,sb="float",sn="float",suv="float",sv="float",sdt="int",se=1,vnm="int",wbc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyOptions.html



-----------------------------------------

polyOptions is undoable, queryable, and NOT editable.

Changes the global display polygonal attributes.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ao    : activeObjects   [boolean] ['query']
    Apply user choices for all active objects.

-----------------------------------------

ae    : allEdges        [boolean] ['query']
    Display all edges in solid line.

-----------------------------------------

bcv   : backCullVertex  [boolean] ['query']
    BackCull vertices.

-----------------------------------------

bc    : backCulling     [boolean] ['query']
    Display with no back culling.

-----------------------------------------

cm    : colorMaterialChannel [string] ['query']
    If colorShadedDisplay is true, then determines which material channel to display color per vertex in. The options are:    * "none" : disable material shading   * "ambient" : ambient material channel   * "ambientDiffuse" : ambient and diffuse material channel   * "diffuse" : diffuse material channel   * "specular" : specular material channel   * "emission" : emission material channel

-----------------------------------------

cs    : colorShadedDisplay [boolean] ['query']
    Use color per vertex display in shaded mode.

-----------------------------------------

dal   : displayAlphaAsGreyScale [boolean] ['query']
    Display alpha as grey scale.

-----------------------------------------

db    : displayBorder   [boolean] ['query']
    Highlight border edge.

-----------------------------------------

dc    : displayCenter   [boolean] ['query']
    Display facet centers.

-----------------------------------------

dce   : displayCreaseEdge [boolean] ['query']
    Highlight creased edges

-----------------------------------------

dcv   : displayCreaseVertex [boolean] ['query']
    Highlight creased vertices

-----------------------------------------

dg    : displayGeometry [boolean] ['query']
    Display geometry.

-----------------------------------------

dif   : displayInvisibleFaces [boolean] ['query']
    Highlight invisible faces

-----------------------------------------

din   : displayItemNumbers [[boolean, boolean, boolean, boolean]] ['query']
    Displays item numbers (vertices edges facets uvs)

-----------------------------------------

dmb   : displayMapBorder [boolean] ['query']
    Highlight map border edge.

-----------------------------------------

dmt   : displayMetadata [[boolean, boolean, boolean]] ['query']
    Displays component metadata (vertices edges facets vertexFaces)

-----------------------------------------

dn    : displayNormal   [boolean] ['query']
    Display normals.

-----------------------------------------

dsc   : displaySubdComps [boolean] ['query']
    Display subdivided components when in Smooth Mesh Preview mode.

-----------------------------------------

dtn   : displayTangent  [boolean] ['query']
    Display tangent.

-----------------------------------------

dt    : displayTriangle [boolean] ['query']
    Display triangulation.

-----------------------------------------

uvt   : displayUVTopology [boolean] ['query']
    Option on UV display to display UVs topologically.

-----------------------------------------

duv   : displayUVs      [boolean] ['query']
    Display UVs.

-----------------------------------------

dv    : displayVertex   [boolean] ['query']
    Display vertices.

-----------------------------------------

dw    : displayWarp     [boolean] ['query']
    Highlight warped facets.

-----------------------------------------

f     : facet           [boolean] ['query']
    For use with -dn flag. Set the normal display style to facet display.

-----------------------------------------

fb    : fullBack        [boolean] ['query']
    Display with full back culling.

-----------------------------------------

gl    : gl              [boolean] ['query']
    Apply user choices for all objects.

-----------------------------------------

hb    : hardBack        [boolean] ['query']
    Backculled hard edges only for backculled faces.

-----------------------------------------

he    : hardEdge        [boolean] ['query']
    Display only hard edges.

-----------------------------------------

hec   : hardEdgeColor   [boolean] ['query']
    Display hard edges as separate color.

-----------------------------------------

mb    : materialBlend   [string] ['query']
    The options are: "overwrite" "add" "subtract" "multiply" "divide" "average" "modulate2x"

-----------------------------------------

np    : newPolymesh     [boolean] ['query']
    Set component display state of new polymesh objects.

-----------------------------------------

pt    : point           [boolean] ['query']
    For use with -dn flag. Set the normal display style to vertex display.

-----------------------------------------

pf    : pointFacet      [boolean] ['query']
    For use with -dn flag. Set the normal display style to vertex and face display.

-----------------------------------------

r     : relative        [boolean] ['query']
    When this flag is used with flags dealing with size, the value (size) is a multiplication factor : i.e for flags : -sizeNormal, -sizeBorder. When this flag is used with flags dealing with a boolean value, the boolean value is toggled : i.e for flags : displayVertex, displayCenter, displayTriangle, displayBorder, backCullVertex, displayWarp, displayItemNumbers.

-----------------------------------------

rt    : reuseTriangles  [boolean] ['query']
    Avoid regenerating triangles, by reusing the old triangles upstream in the construction history. The construction history is searched upstream and downstream for other mesh nodes, and the given boolean value is set on those mesh nodes. Note, that this command does not set the value on the given mesh node. That has to be done using the setAttr command. This option would affect only the interactive 3d viewport. The batch-rendering would use the properly computed triangles. This is useful only for interactive performance such as skinning playback, when the display mode is shaded (or wireframe with triangles displayed) Using this option for wireframe display mode is not recomended.

-----------------------------------------

sb    : sizeBorder      [float] ['query']
    Set the size of the polygonal border edges.

-----------------------------------------

sn    : sizeNormal      [float] ['query']
    Set the size of the polygonal normals.

-----------------------------------------

suv   : sizeUV          [float] ['query']
    Set the size of the polygonal UV.

-----------------------------------------

sv    : sizeVertex      [float] ['query']
    Set the size of the polygonal vertex.

-----------------------------------------

sdt   : smoothDrawType  [int] ['query']
    This setting only works with the newPolymesh flag. Sets a new default attribute value for the smoothDrawType attribute on a polymesh object. Options are: 0: Catmull-Clark 1: Linear 2: OpenSubdiv Catmull-Clark Uniform 3: OpenSubdiv Catmull-Clark Adaptive

-----------------------------------------

se    : softEdge        [boolean] ['query']
    Display soft edges in dotted lines.

-----------------------------------------

vnm   : vertexNormalMethod [int] ['query']
    This setting only works with the newPolymesh flag. Sets a new default attribute value for the vertexNormalMethod attribute on a polymesh object. Options are: 0: Unweighted 1: Angle Weighted 2: Area Weighted 3: Angle And Area Weighted

-----------------------------------------

wbc   : wireBackCulling [boolean]
    Backculled faces are in wireframe.

    """

def polyOptUvs(q=1,e=1,applyToShell=1,aw="float",cch=1,ch=1,gb="float",gmb="float",i="int",n="string",nds="int",oa="int",ps=1,pub=1,s="float",ss="float",us=1,uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyOptUvs.html



-----------------------------------------

polyOptUvs is undoable, queryable, and editable.

Optimizes selected UVs.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

applyToShell : applyToShell    [boolean] []
    Specifies where the whole object or just shells that are selected or pinned should be affected.

-----------------------------------------

aw    : areaWeight      [float] []
    Surface driven importance. 0 treat all faces equal. 1 gives more importance to large ones.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

gb    : globalBlend     [float] []
    This allows the user to blend between a local optimization method (globalBlend = 0.0) and a global optimization method (globalBlend = 1.0). The local optimization method looks at the ratio between the triangles on the object and the triangles in UV space. It has a side affect that it can sometimes introduce tapering problems. The global optimization is much slower, but takes into consideration the entire object when optimizing uv placement.

-----------------------------------------

gmb   : globalMethodBlend [float] []
    The global optimization method uses two functions to compute a minimization. The first function controls edge stretch by using edges lengths between xyz and uv. The second function penalizes the first function by preventing configurations where triangles would overlap. For every surface there is a mix between these two functions that will give the appropriate response. Values closer to 1.0 give more weight to the edge length function. Values closer to 0.0 give more weight to surface area. The default value of '0.5' is a even mix between these two values.

-----------------------------------------

i     : iterations      [int] []
    Maximum number of iterations for each connected UV piece.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

oa    : optimizeAxis    [int] []
    Degree of freedom for optimization: 0=Optimize freely, 1=Move vertically only, 2=Move horzontally only

-----------------------------------------

ps    : pinSelected     [boolean] []
    Specifies that the selected components should be pinned instead of the unselected components.

-----------------------------------------

pub   : pinUvBorder     [boolean] []
    Specifies that the UV border should be pinned when doing the solve. By default only unselected components are pinned.

-----------------------------------------

s     : scale           [float] []
    Ratio between 2d and 3d space.

-----------------------------------------

ss    : stoppingThreshold [float] []
    Minimum distorsion improvement between two steps in %.

-----------------------------------------

us    : useScale        [boolean] []
    Adjust the scale or not.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyOutput(a=1,c=1,cd=1,edge=1,ef=1,f=1,fn=1,fo=1,g=1,no=1,nd=1,of="string",t=1,uvd=1,uv=1,v=1,ve=1,vn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyOutput.html



-----------------------------------------

polyOutput is undoable, NOT queryable, and NOT editable.

Dumps a description of internal memory representation of poly objects. If no
objects are specified in the command line, then the objects from the active
list are used. If information on the geometry in the history of a poly shape
is desired, then the plug of interest needs to be specified in the command
line. Default behaviour is to print only a summary. Use the flags above to get
more details on a specific part of the object.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

a     : allValues       [boolean] []
    Shortcut for setting all the flags above

-----------------------------------------

c     : color           [boolean] []
    Prints the color per vertex. In case of multiple sets, all sets are printed.

-----------------------------------------

cd    : colorDesc       [boolean] []
    Print the color per vertex description. Each integer is an entry in the color array.

-----------------------------------------

e     : edge            [boolean] []
    Print the edge description.

-----------------------------------------

ef    : edgeFace        [boolean] []
    Prints the edge to face adjascency list. Only available if the information is already computed on the object.

-----------------------------------------

f     : face            [boolean] []
    Print the faces description

-----------------------------------------

fn    : faceNorm        [boolean] []
    Prints the normals per face. Only available if the information is already computed on the object.

-----------------------------------------

fo    : force           [boolean] []
    Force evaluation of missing pieces before printing.

-----------------------------------------

g     : group           [boolean] []
    Print the groups of the object.

-----------------------------------------

no    : noOutput        [boolean] []
    Dont output any data. Would be useful if you want to just evaluate the data, for testing purposes.

-----------------------------------------

nd    : normDesc        [boolean] []
    Prints the normals per vertex description. Each integer is an entry in the vertNorm array. Only available if the information is already computed on the object.

-----------------------------------------

of    : outputFile      [string] []
    Location of the output file.

-----------------------------------------

t     : triangle        [boolean] []
    Prints the triangles per face. Only available if the information is already computed on the object.

-----------------------------------------

uvd   : uvDesc          [boolean] []
    Print the UV description. Each integer is an entry in the uvValue array.

-----------------------------------------

uv    : uvValue         [boolean] []
    Prints the UV positions. In case of multiple UV sets, all sets are printed.

-----------------------------------------

v     : vert            [boolean] []
    Prints the vertex positions.

-----------------------------------------

ve    : vertEdge        [boolean] []
    Prints the vertex to edge adjascency list. Only available if the information is already computed on the object.

-----------------------------------------

vn    : vertNorm        [boolean]
    Prints the normals per vertex. Only available if the information is already computed on the object.

    """

def polyPinUV(q=1,e=1,ch=1,op="uint",unp=1,uvs="string",v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPinUV.html



-----------------------------------------

polyPinUV is undoable, queryable, and editable.

This command is used to pin and unpin UVs. A "pinned" UV is one which should
not be modified.

Each UV has an associated pin weight, that defaults to 0.0 meaning that the UV
is not pinned. If pin weight is set to 1.0 then it becomes fully pinned and UV
tools should not modify that UV. If the pin weight is set to a value between
0.0 and 1.0 then UV tools should weight their changes to that UV accordingly.

UV pinning is not enforced by the shape node: it is up to each tool to decide
whether it will obey the pin weights.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ch    : createHistory   [boolean] ['query', 'edit']
    For objects that have no construction history, this flag can be used to force the creation of construction history for pinning. By default, history is not created if the object has no history. Regardless of this flag, history is always created if the object already has history.

-----------------------------------------

op    : operation       [uint] ['query', 'edit']
    Operation to perform. Valid values are: 0: Set pin weights on the selected UVs. 1: Set pin weights to zero for the selected UVs. 2: Remove pin weights from the entire mesh. 3: Invert pin weights of the entire mesh. Default is 0.

-----------------------------------------

unp   : unpinned        [boolean] ['query', 'edit']
    List all selected UVs which are not pinned.

-----------------------------------------

uvs   : uvSetName       [string] ['query', 'edit']
    Specifies the name of the UV set to edit UVs on. If not specified the current UV set will be used if it exists.

-----------------------------------------

v     : value           [float]
    Specifies the pin value for the selected UV components. When specified multiple times, the values are assigned respectively to the specified UVs.

    """

def polyPipe(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv=1,h="linear",n="string",nds="int",o=1,r="linear",rcp=1,sa="int",sc="int",sh="int",tx=1,t="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPipe.html



-----------------------------------------

polyPipe is undoable, queryable, and editable.

The polyPipe command creates a new polygonal pipe.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the pipe.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [boolean] ['query', 'edit']
    Create UVs or not.   Default: true

-----------------------------------------

h     : height          [linear] ['query', 'edit']
    Height of the pipe.   Default: 2.0

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    Radius of the pipe.   Default: 1.0

-----------------------------------------

rcp   : roundCap        [boolean] ['query', 'edit']
    To indicate whether we need a round cap   Default: false

-----------------------------------------

sa    : subdivisionsAxis [int] ['query', 'edit']
    Subdivisions around the axis.   Default: 20

-----------------------------------------

sc    : subdivisionsCaps [int] ['query', 'edit']
    Subdivisions along the thickness caps.   Default: 1

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height.   Default: 1

-----------------------------------------

tx    : texture         [boolean] ['query', 'edit']
    Apply texture or not. this is an old attribute. This is unsupported and would be removed in a future release.   Default: true

-----------------------------------------

t     : thickness       [linear]
    Thickness of the pipe.   Default: 0.5

    """

def polyPlanarProjection(q=1,e=1,phs="linear",sc=1,cch=1,ch=1,cm=1,ic="[float, float]",icx="float",icy="float",imageScale="[float, float]",isu="float",isv="float",ibd=1,kir=1,md="string",n="string",nds="int",pi=1,pc="[linear, linear, linear]",pcx="linear",pcy="linear",pcz="linear",ph="linear",ps="[linear, linear]",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",ra="angle",sf=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPlanarProjection.html



-----------------------------------------

polyPlanarProjection is undoable, queryable, and editable.

TpolyProjCmdBase is a base class for the command to create a mapping on the
selected polygonal faces. Projects a map onto an object, using an orthogonal
projection. The piece of the map defined from isu, isv, icx, icy area, is
placed at pcx, pcy, pcz location.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

phs   : projectionHorizontalSweep [linear] ['query', 'edit']
    The angle swept horizontally by the projection. The range is [0, 360].

-----------------------------------------

sc    : seamCorrect     [boolean] ['query', 'edit']
    This flag specifies to perform a seam correction on the mapped faces.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] ['query']
    This flag when set true will create a new map with a the name passed in, if the map does not already exist.

-----------------------------------------

ic    : imageCenter     [[float, float]] ['query', 'edit']
    The center point of the 2D model layout.   Default: 0.5, 0.5

-----------------------------------------

icx   : imageCenterX    [float] ['query', 'edit']
    Image center X coord.

-----------------------------------------

icy   : imageCenterY    [float] ['query', 'edit']
    Image center Y coord.

-----------------------------------------

imageScale : imageScale      [[float, float]] ['query', 'edit']
    Specifies the UV scale : Enlarges or reduces the 2D version of the model in U or V space relative to the 2D centerpoint.   Default: 1.0, 1.0

-----------------------------------------

isu   : imageScaleU     [float] ['query', 'edit']
    The the U scale : Enlarges or reduces the 2D version of the model in U space relative to the 2D centerpoint.

-----------------------------------------

isv   : imageScaleV     [float] ['query', 'edit']
    The V scale : Enlarges or reduces the 2D version of the model in V space relative to the 2D centerpoint.

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    This flag specifies if the projection node should be inserted before or after deformer nodes already applied to the shape. Inserting the projection after the deformer leads to texture swimming during animation and is most often undesirable.   C: Default is on.

-----------------------------------------

kir   : keepImageRatio  [boolean] []
    True means keep any image ratio

-----------------------------------------

md    : mapDirection    [string] []
    This flag specifies the mapping direction.   'x', 'y' and 'z' projects the map along the corresponding axis.   'c' projects along the current camera viewing direction.   'p' does perspective projection if current camera is perspective.   'b' projects along the best plane fitting the objects selected.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pi    : perInstance     [boolean] []
    True if the new map is per-instance, otherwise it is shared.

-----------------------------------------

pc    : projectionCenter [[linear, linear, linear]] ['query', 'edit']
    The point on the object that will be the center of the projection.   Default: 0.0, 0.0, 0.0

-----------------------------------------

pcx   : projectionCenterX [linear] ['query', 'edit']
    Projection center X coord.

-----------------------------------------

pcy   : projectionCenterY [linear] ['query', 'edit']
    Projection center Y coord.

-----------------------------------------

pcz   : projectionCenterZ [linear] ['query', 'edit']
    Projection center Z coord.

-----------------------------------------

ph    : projectionHeight [linear] ['query', 'edit']
    The height of the map relative to the 3D projection axis.

-----------------------------------------

ps    : projectionScale [[linear, linear]] ['query', 'edit']
    The width and the height of the map relative to the 3D projection axis.   Default: 1.0, 1.0

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    The mapping rotate angles.   Default: 0.0, 0.0, 0.0

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    X mapping rotate angle.

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    Y mapping rotate angle.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    Z mapping rotate angle.

-----------------------------------------

ra    : rotationAngle   [angle] ['query', 'edit']
    The angle for the rotation. When the angle is positive, then the map rotates counterclockwise on the mapped model; if negative, the map rotates clockwise.   Default: 0.0

-----------------------------------------

sf    : smartFit        [boolean] []
    True means use the smart fit algorithm

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyPlane(q=1,e=1,ax="[linear, linear, linear]",cuv="int",h="linear",sh="int",sw="int",sx="int",sy="int",tx="int",w="linear",cch=1,ch=1,n="string",nds="int",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPlane.html



-----------------------------------------

polyPlane is undoable, queryable, and editable.

Create a new polygonal plane.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the plane.

-----------------------------------------

cuv   : createUVs       [int] ['query', 'edit']
    Create UVs or not.    * 0: No UVs   * 1: No Normalization   * 2: Normalize and Preserve Aspect Ratio     Default: 1

-----------------------------------------

h     : height          [linear] ['query', 'edit']
    Height of the plane.   Default: 1.0

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height of the sphere.

-----------------------------------------

sw    : subdivisionsWidth [int] ['query', 'edit']
    Subdivisions along the width of the plane.   Default: 10

-----------------------------------------

sx    : subdivisionsX   [int] ['query', 'edit']
    This specifies the number of subdivisions in the X direction for the plane.   Default is 5.

-----------------------------------------

sy    : subdivisionsY   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Y direction for the plane.   Default is 5.

-----------------------------------------

tx    : texture         [int] ['query', 'edit']
    What texture mechanism to be applied. 0=No textures; 1=stretch to fit; 2=preserve aspect ratio   Default: 1

-----------------------------------------

w     : width           [linear] ['query', 'edit']
    Width of the plane.   Default: 1.0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node (where applicable).

    """

def polyPlatonicSolid(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv="int",n="string",nds="int",o=1,r="linear",l="linear",st="int",tx="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPlatonicSolid.html



-----------------------------------------

polyPlatonicSolid is undoable, queryable, and editable.

The polyPlatonicSolid command creates a new polygonal platonic solid.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the platonic solid.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [int] []
    This flag alows a specific UV mechanism to be selected, while creating.   The valid values are 0, 1, 2 ,3 or 4.   0 implies that no UVs will be generated (No texture to be applied).      1 implies UVs should be created for the object as a whole without any normalization.   The solid will be unwrapped and then the texture will be applied   without any distortion.   In the unwrapped solid, the shared edges will have shared UVs.      2 implies UVs are created separately for each of the faces of the solid.      3 implies the UVs should be normalized. This will normalize the   U and V direction separately, thereby resulting in distortion of textures.      4 implies UVs are created so that the texture will not be distorted when applied.   The texture lying outside the UV range will be truncated (since that cannot be   squeezed in, without distorting the texture.      For better understanding of these options, you may have to open the   texture view window      C: Default is 4

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    This flag specifies the radius of the platonic solid.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

l     : sideLength      [linear] ['query', 'edit']
    This flag specifies the side length of platonic solid.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

st    : solidType       [int] []
    This flag allows a specific platonic solid to be selected for creation of mesh,   The valid values are 0, 1, 2 and 3.   0 implies dodecahedron to be created.   1 implies icosahedron to be created.   2 implies octahedron to be created.   3 implies tertrahedron to be created.      C: Default is 0

-----------------------------------------

tx    : texture         [int]
    This flag is obsolete and will be removed in the next release. The -cuv/createUVs flag should be used instead.

    """

def polyPoke(q=1,e=1,cch=1,ch=1,lt="[linear, linear, linear]",ltx="linear",lty="linear",ltz="linear",n="string",nds="int",t="[linear, linear, linear]",tx="linear",ty="linear",tz="linear",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPoke.html



-----------------------------------------

polyPoke is undoable, queryable, and editable.

Introduces a new vertex in the middle of the selected face, and connects it to
the rest of the vertices of the face.


-----------------------------------------


Return Value:

string  The node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

lt    : localTranslate  [[linear, linear, linear]] []
    Translate the new vertex in the local face coordinate.

-----------------------------------------

ltx   : localTranslateX [linear] []
    Translate the new vertex in the local face coordinate along X.

-----------------------------------------

lty   : localTranslateY [linear] []
    Translate the new vertex in the local face coordinate along Y.

-----------------------------------------

ltz   : localTranslateZ [linear] []
    Translate the new vertex in the local face coordinate along Z.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

t     : translate       [[linear, linear, linear]] []
    Translate the new vertex in the world space.

-----------------------------------------

tx    : translateX      [linear] []
    Translate the new vertex in the world space along X.

-----------------------------------------

ty    : translateY      [linear] []
    Translate the new vertex in the world space along Y.

-----------------------------------------

tz    : translateZ      [linear] []
    Translate the new vertex in the world space along Z.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyPrimitive(q=1,e=1,ax="[linear, linear, linear]",cuv="int",pt="int",r="linear",l="linear",tx="int",cch=1,ch=1,n="string",nds="int",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPrimitive.html



-----------------------------------------

polyPrimitive is undoable, queryable, and editable.

Create a polygon primative


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the primitive polygon.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cuv   : createUVs       [int] ['query', 'edit']
    Create UVs or not.    * 0: No UVs   * 1: No Normalization   * 2: Normalize Each Face Separately   * 3: Normalize Collectively   * 4: Normalize and Preserve Aspect Ratio

-----------------------------------------

pt    : polyType        [int] []
    This flag allows a specific primitive poly to be selected for creation of mesh,   The valid values is 0   0 implies soccer ball to be created.   C: Default is 0

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    This flag specifies the radius of the primitive polygon.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

l     : sideLength      [linear] ['query', 'edit']
    This flag specifies the side length of primitive polygon.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

tx    : texture         [int] ['query', 'edit']
    What texture mechanism to be applied 0=No textures, 1=Object, 2=Faces

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node (where applicable).

    """

def polyPrism(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv="int",l="linear",n="string",nds="int",ns="int",nsi="int",o=1,w="linear",sc="int",sh="int",tx="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPrism.html



-----------------------------------------

polyPrism is undoable, queryable, and editable.

The prism command creates a new polygonal prism.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the prism.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [int] []
    This flag alows a specific UV mechanism to be selected, while creating the primitive.   The valid values are 0, 1, 2 or 3.   0 implies that no UVs will be generated (No texture to be applied).      1 implies UVs should be created for the object as a whole without any normalization.   The primitive will be unwrapped and then the texture will be applied   without any distortion.   In the unwrapped primitive, the shared edges will have shared UVs.      2 implies the UVs should be normalized. This will normalize the   U and V direction separately, thereby resulting in distortion of textures.      3 implies UVs are created so that the texture will not be distorted when applied.   The texture lying outside the UV range will be truncated (since that cannot be   squeezed in, without distorting the texture.      For better understanding of these options, you may have to open the   texture view window      C: Default is 2.

-----------------------------------------

l     : length          [linear] ['query', 'edit']
    This flag specifies the length of the prism.   C: Default is 2.0.   Q: When queried, this flag returns a float.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ns    : numberOfSides   [int] ['query', 'edit']
    This specifies the number of sides for the prism.   C: Default is 3.   Q: When queried, this flag returns an int.

-----------------------------------------

nsi   : numderOfSides   [int] ['query', 'edit']
    This specifies the number of sides for the prism.   C: Default is 3.   Q: When queried, this flag returns an int.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

w     : sideLength      [linear] ['query', 'edit']
    This flag specifies the edge length of the prism.   C: Default is 2.0.   Q: When queried, this flag returns a float.

-----------------------------------------

sc    : subdivisionsCaps [int] ['query', 'edit']
    This flag specifies the subdivisions on the caps for the prism.   C: Default is 2.   Q: When queried, this flag returns an int.

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    This specifies the subdivisions along the height for the prism.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [int]
    This flag is obsolete and will be removed in the next release. The -cuv/createUVs flag should be used instead.

    """

def polyProjectCurve(q=1,e=1,aut=1,cch=1,d="[linear, linear, linear]",dx="linear",dy="linear",dz="linear",nds="int",tol="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyProjectCurve.html



-----------------------------------------

polyProjectCurve is undoable, queryable, and editable.

The polyProjectCurve command creates curves by projecting a selected curve
onto a selected poly mesh. The direction of projection will be the current
view direction unless the direction vector is specified with the -direction/-d
flag.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aut   : addUnderTransform [boolean] []
    True if the resulting curve should be added under the source transform

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : direction       [[linear, linear, linear]] ['query', 'edit']
    Direction of projection.

-----------------------------------------

dx    : directionX      [linear] ['query', 'edit']
    X direction of projection.

-----------------------------------------

dy    : directionY      [linear] ['query', 'edit']
    Y direction of projection.

-----------------------------------------

dz    : directionZ      [linear] ['query', 'edit']
    Z direction of projection.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tol   : tolerance       [linear]
    Tolerance to fit to.

    """

def polyProjection(ch=1,cm=1,icx="float",icy="float",isu="float",isv="float",ibd=1,kir=1,md="string",pcx="float",pcy="float",pcz="float",psu="float",psv="float",rx="float",ry="float",rz="float",ra="float",sc=1,sf=1,t="string",uvs="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyProjection.html



-----------------------------------------

polyProjection is undoable, NOT queryable, and NOT editable.

Creates a mapping on the selected polygonal faces. When construction history
is created, the name of the new node is returned. In other cases, the command
returns nothing.


-----------------------------------------


Return Value:

string  Name of node created


-----------------------------------------


Flags:

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off (where applicable).

-----------------------------------------

cm    : createNewMap    [boolean] []
    Create new map if it does not exist.

-----------------------------------------

icx   : imageCenterX    [float] []
    Specifies the X (U) translation of the projected UVs. Default is 0.5.

-----------------------------------------

icy   : imageCenterY    [float] []
    Specifies the Y (V) translation of the projected UVs. Default is 0.5.

-----------------------------------------

isu   : imageScaleU     [float] []
    Specifies the U scale factor of the projected UVs. Default is 1.

-----------------------------------------

isv   : imageScaleV     [float] []
    Specifies the V scale factor of the projected UVs. Default is 1.

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    Specifies if the projection node should be inserted before or after deformer nodes already applied to the shape. Inserting the projection after the deformer leads to texture swimming during animation and is most often undesirable. Default is on.

-----------------------------------------

kir   : keepImageRatio  [boolean] []
    Specifies if the xy scaling in the planar projection has to be uniform. By setting this flag, the texture aspect ratio is preserved. This flag is ignored for cylindrical and spherical projections.

-----------------------------------------

md    : mapDirection    [string] []
    Specifies the direction of the projection. By specifying this flag, the projection placement values (pcx, pcy, pcz, rx, ry, rz, psu, psv) are internally computed. If both this flag and the projection values are specified, the projection values are ignored. Valid Values are : X Projects along the X Axis Y Projects along the Y Axis Z Projects along the Z Axis bestPlane Projects on the best plane fitting the object camera Projects along the viewing direction perspective Creates perspective projection if current camera is perspective Default is bestPlane.

-----------------------------------------

pcx   : projectionCenterX [float] []
    Specifies the X coordinate of the center of the projection manipulator.

-----------------------------------------

pcy   : projectionCenterY [float] []
    Specifies the Y coordinate of the center of the projection manipulator.

-----------------------------------------

pcz   : projectionCenterZ [float] []
    Specifies the Z coordinate of the center of the projection manipulator.

-----------------------------------------

psu   : projectionScaleU [float] []
    Specifies the U scale component of the projection manipulator.

-----------------------------------------

psv   : projectionScaleV [float] []
    Specifies the V scale component of the projection manipulator.

-----------------------------------------

rx    : rotateX         [float] []
    Specifies the X-axis rotation of the projection manipulator.

-----------------------------------------

ry    : rotateY         [float] []
    Specifies the Y-axis rotation of the projection manipulator.

-----------------------------------------

rz    : rotateZ         [float] []
    Specifies the Z-axis rotation of the projection manipulator.

-----------------------------------------

ra    : rotationAngle   [float] []
    Specifies the rotation of the projected UVs in the UV space. Default is 0.

-----------------------------------------

sc    : seamCorrect     [boolean] []
    Specifies if seam correction has to be done for spherical and cylindrical projections. This flag is ignored, if the planar projection is specified.

-----------------------------------------

sf    : smartFit        [boolean] []
    Specifies if the projection manipulator has to be placed fitting the object. Used for cylindrical and spherical projections. For smart fitting the planar projection, the mapDirection flag has to be used, since there are several options for smart fitting a planar projection.

-----------------------------------------

t     : type            [string] []
    Specify the type of mapping to be performed. Valid values for the STRING are "planar" "cylindrical" "spherical" Default is planar.

-----------------------------------------

uvs   : uvSetName       [string]
    Specifies name of the uv set to work on.

    """

def polyPyramid(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv="int",n="string",nds="int",ns="int",nsi="int",o=1,w="linear",sc="int",sh="int",tx=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyPyramid.html



-----------------------------------------

polyPyramid is undoable, queryable, and editable.

The pyramid command creates a new polygonal pyramid.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the pyramid.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [int] ['query', 'edit']
    Create UVs or not.    * 0: No UVs   * 1: No Normalization   * 2: Normalize   * 3: Normalize and Preserve Aspect Ratio     Default: 2

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ns    : numberOfSides   [int] ['query', 'edit']
    Number of sides of Pyramid.   Default: 4

-----------------------------------------

nsi   : numderOfSides   [int] ['query', 'edit']
    Number of sides of Pyramid.   Default: 4

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

w     : sideLength      [linear] ['query', 'edit']
    Side length of the Pyramid.   Default: 1.0

-----------------------------------------

sc    : subdivisionsCaps [int] ['query', 'edit']
    Subdivisions on bottom cap   Default: 0

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height.   Default: 1

-----------------------------------------

tx    : texture         [boolean]
    Apply texture or not.   Default: true

    """

def polyQuad(q=1,e=1,a="angle",cch=1,ch=1,kgb=1,khe=1,ktb=1,n="string",nds="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyQuad.html



-----------------------------------------

polyQuad is undoable, queryable, and editable.

Merges selected triangles of a polygonal object into four-sided faces.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [angle] ['query', 'edit']
    Angle threshold above which two triangles are not merged.   C: Default is 30 degrees. The range is [0.0, 180.0].   Q: When queried, this flag returns a float.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

kgb   : keepGroupBorder [boolean] ['query', 'edit']
    Keep facet group border : If "on", the borders of selected faces are maintained, otherwise the borders of selected facets may be modified.   C: Default is "on".   Q: When queried, this flag returns an int.

-----------------------------------------

khe   : keepHardEdges   [boolean] ['query', 'edit']
    Keep hard edges : If "on", the hard edges of selected faces are maintained, otherwise they may be deleted between two triangles.   C: Default is "on".   Q: When queried, this flag returns an int.

-----------------------------------------

ktb   : keepTextureBorders [boolean] ['query', 'edit']
    Keep texture border : If "on", the borders of texture maps are maintained, otherwise the boreders of texture maps may be modified.   C: Default is "on".   Q: When queried, this flag returns an int.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyQueryBlindData(at="string",bnd="string",bd=1,dbd="float",ind="int",ldn="string",max="float",min="float",sdn="string",sc=1,sd="string",ss="string",id="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyQueryBlindData.html



-----------------------------------------

polyQueryBlindData is NOT undoable, NOT queryable, and NOT editable.

Command query's blindData associated with particular polygonal components. So,
the command will require the following to be specified: \- selection list to
query Optional are the: \- typeId \- associationType \- longDataName or
shortDataName of data being queried. \- The actual data being specified. \-
showComponent flag Note that for object level blind data, the showComponent
flag will be ignored. If no components are selected, the assocation flag will
be ignored and object level data will be queried.


-----------------------------------------


Return Value:

string  Blind data


-----------------------------------------


Flags:

-----------------------------------------

at    : associationType [string] []
    Specifies the dataTypes that are part of BlindData node being queried. Allowable associations are "object" for any object, and "vertex" "edge" and "face" for mesh objects.

-----------------------------------------

bnd   : binaryData      [string] []
    Specifies the binary string value to search for

-----------------------------------------

bd    : booleanData     [boolean] []
    Specifies the string value to search for

-----------------------------------------

dbd   : doubleData      [float] []
    Specifies the double/float value to search for

-----------------------------------------

ind   : intData         [int] []
    Specifies the integer value to search for

-----------------------------------------

ldn   : longDataName    [string] []
    Specifies the long name of the data that is being queried by this command.

-----------------------------------------

max   : maxValue        [float] []
    Specifies the maximum value to search for. This option will query float, double, and integer types of blind data.

-----------------------------------------

min   : minValue        [float] []
    Specifies the minimum value to search for. This option will query float, double and integer types of blind data.

-----------------------------------------

sdn   : shortDataName   [string] []
    Specifies the short name of the data that is being queried by this command.

-----------------------------------------

sc    : showComp        [boolean] []
    The showComponent option controls whether the object.[component].attribute name is output preceeding the actual value. If the showComponent option is used then the restriction of only returning 1 type of blind data (i.e. one of integer, float, double... is removed, as the return for all are strings. If the association is object and not component, then this option will still cause all the attribute names to be printed

-----------------------------------------

sd    : stringData      [string] []
    Specifies the string value to search for

-----------------------------------------

ss    : subString       [string] []
    Specifies the substring that should be checked against a STRING type blind data. If the sub string is found query is successful. Will not look at non String type blind data elements.

-----------------------------------------

id    : typeId          [int]
    Specifies the typeId of the BlindData type being queried. If the typeId is not specified, then all of the components that match the query will be output. The typeId of the elements found will be output if the ShowComponents option is used. Will be in the format "object.component.attribute::typeId". If the typeId is specifed then the "::typeId" portion will not be output with the ShowComponents option.

    """

def polyReduce(q=1,e=1,cch=1,cr=1,cwt="float",com="float",ch=1,gwt="float",iwt=1,kb=1,kbw="float",kcb=1,kcw="float",kce=1,cew="float",kfb=1,kfw="float",khe=1,khw="float",kmb=1,kmw="float",kev=1,kqw="float",n="string",nds="int",p="float",pl=1,top=1,rpo=1,shp="float",sw="float",sx="float",sy="float",sz="float",stl="float",trm="int",tct="int",t=1,uvs="int",uwt="float",ver="int",vct="int",vmp="string",vwc="float",wc="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyReduce.html



-----------------------------------------

polyReduce is undoable, queryable, and editable.

Simplify a polygonal object by reducing geometry while preserving the overall
shape of the mesh.

The algorithm for polyReduce was changed in 2014 to use a new algorithm
derived from Softimage. However, the command still defaults to using the old
algorithm for backwards compatibility. Therefore, we recommend setting the
version flag to 1 for best results as the new algorithm is better at
preserving geometry features. Additionally, some flags only apply to a
specific algorithm and this is documented for each flag.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cr    : cachingReduce   [boolean] ['query', 'edit']
    Cache intermediate reductions for speed at the expense of memory. It is recommended that caching be enabled when using the new algorithm. (-version 1) However, caching is not recommended when using then old algorithm because it can cause stability issues.   C: Default is false.   Q: When queried, this flag returns a boolean.

-----------------------------------------

cwt   : colorWeights    [float] ['query', 'edit']
    This flag only applies when using the old algorithm and is provided for backwards compatibility. How much consideration vertex color is given in the reduction algorithm. A higher weight means the reduction will try harder to preserve vertex coloring.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

com   : compactness     [float] ['query', 'edit']
    This flag only applies when using the old algorithm and is provided for backwards compatibility. Tolerance for compactness for the generated triangles A value of 0 will accept all triangles during decimation A value close to 0 will attempt to eliminate triangles that have collinear edges (zero area triangles) A value closer to 1 will attempt to eliminate triangles that are not strictly equilateral (of equal lengths) The closer to 1.0, the more expensive the computation   Q: When queried, this flag returns a float.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

gwt   : geomWeights     [float] ['query', 'edit']
    This flag only applies when using the old algorithm and is provided for backwards compatibility. How much consideration vertex positions are given in the reduction algorithm. A higher weight means the reduction will try harder to preserve geometry.   C: Default is 1.   Q: When queried, this flag returns a float.

-----------------------------------------

iwt   : invertVertexWeights [boolean] ['query', 'edit']
    This flag controls how weight map values are interpreted. If true, a vertex weight of 1.0 means a vertex is unlikely to be reduced. If false, a vertex weight of 0.0 means a vertex is unlikely to be reduced. This flag only applies when using the new algorithm. (-version 1)   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

kb    : keepBorder      [boolean] ['query', 'edit']
    If true, reduction will try to retain geometric borders and the border of the selection.   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

kbw   : keepBorderWeight [float] ['query', 'edit']
    If keepBorder is on, this flag specifies the weight to assign to borders. Setting this value to 0 will disable border preservation and a value of 1 will exactly preserve all border vertices which is useful for matching adjacent meshes. This flag only applies when using the new algorithm. (-version 1)   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

kcb   : keepColorBorder [boolean] ['query', 'edit']
    If true, reduction will try to retain color borders. These are determined according to color Ids. This flag only applies when using the new algorithm. (-version 1)   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

kcw   : keepColorBorderWeight [float] ['query', 'edit']
    If keepColorBorder is on, this flag specifies the weight to assign to color borders. Setting this value to 0 will disable color border preservation and a value of 1 will exactly preserve all color borders. This flag only applies when using the new algorithm. (-version 1)   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

kce   : keepCreaseEdge  [boolean] ['query', 'edit']
    If true, reduction will try to retain crease edges.   C: Default is true. This flag only applies when using the new algorithm. (-version 1)   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

cew   : keepCreaseEdgeWeight [float] ['query', 'edit']
    If keepCreaseEdge is on, this flag specifies the weight to assign to crease edges. Setting this value to 0 will disable crease edge preservation and a value of 1 will exactly preserve all crease edges. This flag only applies when using the new algorithm. (-version 1)   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

kfb   : keepFaceGroupBorder [boolean] ['query', 'edit']
    If true, reduction will try to retain borders of face groups, which are mostly used to define material assignments. This flag only applies when using the new algorithm. (-version 1)   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

kfw   : keepFaceGroupBorderWeight [float] ['query', 'edit']
    If keepFaceGroupBorder is on, this flag specifies the weight to assign to material borders. Setting this value to 0 will disable group border preservation and a value of 1 will exactly preserve all group borders. This flag only applies when using the new algorithm. (-version 1)   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

khe   : keepHardEdge    [boolean] ['query', 'edit']
    If true, reduction will try to retain hard edges.   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

khw   : keepHardEdgeWeight [float] ['query', 'edit']
    If keepHardEdge is on, this flag specifies the weight to assign to hard edges. Setting this value to 0 will disable hard edge preservation and a value of 1 will exactly preserve all hard edges. This flag only applies when using the new algorithm. (-version 1)   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

kmb   : keepMapBorder   [boolean] ['query', 'edit']
    If true, reduction will try to retain UV borders. A UV border is present if the faces on either side of the edge do not share UV Ids.   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

kmw   : keepMapBorderWeight [float] ['query', 'edit']
    If keepMapBorder is on, this flag specifies the weight to assign to UV map borders. Setting this value to 0 will disable UV map border preservation and a value of 1 will exactly preserve all UV borders. This flag only applies when using the new algorithm. (-version 1)   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

kev   : keepOriginalVertices [boolean] ['query', 'edit']
    This flag only applies when using the old algorithm and is provided for backwards compatibility. If true, vertices will try to retain their original positions and will not be repositioned for optimal shape.   NOTE: In the newer algorithm vertices always retain their exact original positions. (though the Ids will change)   C: Default is false.   Q: When queried, this flag returns a boolean.

-----------------------------------------

kqw   : keepQuadsWeight [float] ['query', 'edit']
    This flag controls how much consideration is given to oreserving quad faces during reduction. A higher weight means the reduction will try harder to keep quad faces and avoid creation of triangles. If the version flag is set to 1 (-version 1) and the keepQuadsWeight flag is set to 1.0 then a special quad reduction algorithm is used that does a better job of preserving quads. Howver, this special quad reduction algorithm does not support symmetry so those flags will be ignored when the keepQuadsWeight flag is set to 1.0.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : percentage      [float] ['query', 'edit']
    This flag specifies how many vertices to remove during reduction as a percentage of the original mesh. This flag only applies if the termination flag is set to 0 or when using the old algorithm.   C: Default is 0. 100 will remove every possible vertex, 0 will remove none.   Q: When queried, this flag returns a float.

-----------------------------------------

pl    : preserveLocation [boolean] []
    This flag guarantees that if the original geometry is preserved, the new geometry will have the same location.   C: Default is false.

-----------------------------------------

top   : preserveTopology [boolean] ['query', 'edit']
    this flag guarantees that the topological type will be preserved during reduction. In particular, if the input is manifold then the output will be manifold. This option also prevents holes in the mesh from being closed off. This flag only applies when using the new algorithm. (-version 1)   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

rpo   : replaceOriginal [boolean] []
    Create "in place" (i.e., replace) (not available in all commands). NOTE: This flag is intended for use by the "Reduce" menu item. If 'polyReduce -rpo 0' is executed from the command line, Shader information will not be copied from the original mesh to the result.

-----------------------------------------

shp   : sharpness       [float] ['query', 'edit']
    Sharpness controls the balance between preserving small, sharp details versus larger shapes. At low values, details that are small relative to the general shape of the object are more likely to be collapsed. At high values, they are more likely to be kept. This flag only applies when using the new algorithm. (-version 1)   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

sw    : symmetryPlaneW  [float] ['query', 'edit']
    W value of the symmetry plane. This flag only applies when using the new algorithm (-version 1) and the useVirtualSymmetry flag is set to 2.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

sx    : symmetryPlaneX  [float] ['query', 'edit']
    X value of the symmetry plane. This flag only applies when using the new algorithm (-version 1) and the useVirtualSymmetry flag is set to 2.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

sy    : symmetryPlaneY  [float] ['query', 'edit']
    Y value of the symmetry plane. This flag only applies when using the new algorithm (-version 1) and the useVirtualSymmetry flag is set to 2.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

sz    : symmetryPlaneZ  [float] ['query', 'edit']
    Z value of the symmetry plane. This flag only applies when using the new algorithm (-version 1) and the useVirtualSymmetry flag is set to 2.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

stl   : symmetryTolerance [float] ['query', 'edit']
    Tolerance to use when applying symmetry. For each vertex of the mesh, we find its exact symmetric point, then we look for the closest vertex to the exact symmetry up to the tolerance distance. Higher values risk finding more spurious symmetries, lower values might miss symmetries. The value is distance in object space. This flag only applies when using the new algorithm (-version 1) and the useVirtualSymmetry flag is not set to 0.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

trm   : termination     [int] ['query', 'edit']
    This flag specifies the termination condition to use when reducing the mesh. This flag only applies to the new algorithm. (-version 1)   0 Percentage   1 Vertex count   2 Triangle count   C: Default is 0.   Q: When queried, this flag returns an integer.

-----------------------------------------

tct   : triangleCount   [int] ['query', 'edit']
    This flag specifies a target number of triangles to retain after reduction. Note that other factors such as quad and feature preservation may take precendence and cause the actual number of triangles to be different. This flag only applies when using the new algorithm (-version 1) and the termination flag is set to 2.   C: Default is 0.   Q: When queried, this flag returns an integer.

-----------------------------------------

t     : triangulate     [boolean] ['query', 'edit']
    This flag only applies when using the old algorithm and is provided for backwards compatibility. This attribute specifies if the geometry or the selected faces has to be triangulated, before performing reduction.   C: Default is true.   Q: When queried, this flag returns a boolean.

-----------------------------------------

uvs   : useVirtualSymmetry [int] ['query', 'edit']
    This flag controls whether symmetry is preserved during the reduction. This flag only applies when using the new algorithm (-version 1) and the keepQuadsWeight flag is less than 1.0.   0 No symmetry preservation   1 Automatic. Try to find suitable symmetry during reduction.   2 Plane. Specify a symmetry plane to use during reduction.   C: Default is 0.   Q: When queried, this flag returns an integer.

-----------------------------------------

uwt   : uvWeights       [float] ['query', 'edit']
    This flag only applies when using the old algorithm and is provided for backwards compatibility. How much consideration uv positions are given in the reduction algorithm. A higher weight means the reduction will try harder to preserve uv positions.   C: Default is 0.   Q: When queried, this flag returns a float.

-----------------------------------------

ver   : version         [int] ['query', 'edit']
    Version of the poly reduce algorithm to use.   0 Old algorithm used in Maya 2013 and prior for backwards compatibility   1 New algorithm derived from Softimage and used in Maya 2014 and later   The default is 0 for backwards compatibility but for best results it is recommended that the new algorithm is used as it is better at preserving mesh details. Some flags only apply to a specific algorithm and this is documented for each flag.   C: Default is 0 for backwards compatibility.   Q: When queried, this flag returns an integer.

-----------------------------------------

vct   : vertexCount     [int] ['query', 'edit']
    This flag specifies a target number of vertices to retain after reduction. Note that other factors such as quad and feature preservation may take precendence and cause the actual number of vertices to be different. This flag only applies when using the new algorithm (-version 1) and the termination flag is set to 1.   C: Default is 0.   Q: When queried, this flag returns an integer.

-----------------------------------------

vmp   : vertexMapName   [string] ['query']
    Name of a color set to be added to the output mesh that stores a mapping from vertices in the output mesh to vertices in the input mesh. The color set is RGB. The original vertex Id that maps to an output vertex is of a vertex is 65536*r + g where r and g are the red and green channel at a vertex. The blue channel is always zero. Each vertex in the output mesh has a shared color. This flag only applies when using the new algorithm. (-version 1)   Q: When queried, this flag returns a string.

-----------------------------------------

vwc   : vertexWeightCoefficient [float] ['query', 'edit']
    This flag specifies a constant value to multiply to each weight map value. A value of zero turns off the weight map. This flag only applies when using the new algorithm. (-version 1)   C: Default is 1.   Q: When queried, this flag returns a float.

-----------------------------------------

wc    : weightCoefficient [float]
    This flag only applies when using the old algorithm and is provided for backwards compatibility. The weight of each vertex is multiplied with this coefficient when the reduction is performed. This value does not have to be edited, normally. It gives finer control over the weighted reduction. This attribute is replaced by vertexWeightCoefficient in the new algorithm when the version flag is set to 1.   C: Default is 10000.   Q: When queried, this flag returns a float.

    """

def polyRemesh(q=1,e=1,cch=1,ch=1,ipt="int",n="string",nds="int",rdt="float",rft="float",smt="float",tsb=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyRemesh.html



-----------------------------------------

polyRemesh is undoable, queryable, and editable.

Triangulates, then remeshes the given mesh through edge splitting and
collapsing. Edges longer than the specified refinement threshold are split,
and edges shorter than the reduction threshold are collapsed.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

ipt   : interpolationType [int] ['query', 'edit']
    Algorithm used for interpolating new vertices

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rdt   : reduceThreshold [float] ['query', 'edit']
    A percentage of the refineThreshold. Edges shorter than this percentage will be reduced to a single vertex.

-----------------------------------------

rft   : refineThreshold [float] ['query', 'edit']
    Triangle edges longer than this value will be split into two edges.

-----------------------------------------

smt   : smoothStrength  [float] ['query', 'edit']
    Amount of smoothing applied to the vertices after remeshing.

-----------------------------------------

tsb   : tessellateBorders [boolean]
    Specifies if the borders of the selected region are allowed to be remeshed.

    """

def polyRetopo(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyRetopo.html



-----------------------------------------

polyRetopo is undoable, queryable, and editable.

Retopologize a polygonial surface.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.
    """

def polyRetopoCtx(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyRetopoCtx.html



-----------------------------------------

polyRetopoCtx is undoable, queryable, and editable.

Create a new context to manipulate reform nodes


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.
    """

def polySelect(q=1,add=1,af=1,ass=1,d=1,eb="uint",ebp="[int, int]",bpt="[int, int]",el="uint",elb="uint",lbp="[int, int]",elp="[int, int]",lpt="[int, int]",er="uint",erp="[int, int]",rpt="[int, int]",euv="uint",en="uint",ets="uint",ns=1,r=1,sep="[int, int]",spu="[int, int]",sfp="[int, int]",tgl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySelect.html



-----------------------------------------

polySelect is undoable, queryable, and NOT editable.

This command makes different types of poly component selections. The return
value is an integer array containing the id's of the components in the
selection in order. If a given type of selection loops back on itself then
this is indicated by the start id appearing twice, once at the start and once
at the end.


-----------------------------------------


Return Value:

int[]  List of selected components.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : add             [boolean] ['query']
    Indicates that the specified items should be added to the active list without removing existing items from the active list.

-----------------------------------------

af    : addFirst        [boolean] ['query']
    Indicates that the specified items should be added to the front of the active list without removing existing items from the active list.

-----------------------------------------

ass   : asSelectString  [boolean] ['query']
    Changes the return type from an integer array to a string array which can be used as a selection string.

-----------------------------------------

d     : deselect        [boolean] ['query']
    Indicates that the specified items should be removed from the active list if they are on the active list.

-----------------------------------------

eb    : edgeBorder      [uint] ['query']
    Select all conected border edges starting at the given edge.  In query mode, this flag needs a value.

-----------------------------------------

ebp   : edgeBorderPath  [[int, int]] ['query']
    Given two edges on the same border, this will select the edges on the border in the path between them.  In query mode, this flag needs a value.

-----------------------------------------

bpt   : edgeBorderPattern [[int, int]] ['query']
    Given two edges on the same border, this will check how many edges there are between the given edges and then continue that pattern of selection around the border.  In query mode, this flag needs a value.

-----------------------------------------

el    : edgeLoop        [uint] ['query']
    Select an edge loop starting at the given edge.  In query mode, this flag needs a value.

-----------------------------------------

elb   : edgeLoopOrBorder [uint] ['query']
    Select an edge loop or all conected border edges, depending on whether the edge is on a border or not, starting at the given edge.  In query mode, this flag needs a value.

-----------------------------------------

lbp   : edgeLoopOrBorderPattern [[int, int]] ['query']
    Given two edges either on the same edge loop or on the same edge border, this will check how many edges there are between the given edges and then continue that pattern of selection around the edge loop or edge border.  In query mode, this flag needs a value.

-----------------------------------------

elp   : edgeLoopPath    [[int, int]] ['query']
    Given two edges that are on the same edge loop, this will select the shortest path between them on the loop.  In query mode, this flag needs a value.

-----------------------------------------

lpt   : edgeLoopPattern [[int, int]] ['query']
    Given two edges on the same edge loop, this will check how many edges there are between the given edges and then continue that pattern of selection around the edge loop.  In query mode, this flag needs a value.

-----------------------------------------

er    : edgeRing        [uint] ['query']
    Select an edge ring starting at the given edge.  In query mode, this flag needs a value.

-----------------------------------------

erp   : edgeRingPath    [[int, int]] ['query']
    Given two edges that are on the same edge ring, this will select the shortest path between them on the ring.  In query mode, this flag needs a value.

-----------------------------------------

rpt   : edgeRingPattern [[int, int]] ['query']
    Given two edges on the same edge ring, this will check how many edges there are between the given edges and then continue that pattern of selection around the edge ring.  In query mode, this flag needs a value.

-----------------------------------------

euv   : edgeUVLoopOrBorder [uint] ['query']
    Select an edge loop or border, terminating at UV borders.  In query mode, this flag needs a value.

-----------------------------------------

en    : everyN          [uint] []
    Number of elements to stride over. If less than 1 then use 1, meaning every element. 2 means every second one, etc.

-----------------------------------------

ets   : extendToShell   [uint] ['query']
    Select the poly shell given a face id.  In query mode, this flag needs a value.

-----------------------------------------

ns    : noSelection     [boolean] ['query']
    If this flag is used then the selection is not changed at all.

-----------------------------------------

r     : replace         [boolean] ['query']
    Indicates that the specified items should replace the existing items on the active list.

-----------------------------------------

sep   : shortestEdgePath [[int, int]] ['query']
    Given two vertices, this will select the shortest path between them in the 3d object space.  In query mode, this flag needs a value.

-----------------------------------------

spu   : shortestEdgePathUV [[int, int]] ['query']
    Given two UVs, this will select the shortest path between them in the 2d texture space.  In query mode, this flag needs a value.

-----------------------------------------

sfp   : shortestFacePath [[int, int]] ['query']
    Given two faces, this will select the shortest path between them in the 3d object space.  In query mode, this flag needs a value.

-----------------------------------------

tgl   : toggle          [boolean]
    Indicates that those items on the given list which are on the active list should be removed from the active list and those items on the given list which are not on the active list should be added to the active list.

    """

def polySelectConstraint(q=1,a="int",ap=1,at="float",ab="[angle, angle]",bo=1,bp=1,c="int",cr=1,dis=1,d="int",da="[float, float, float]",db="[float, float]",dp="[float, float, float]",ed="uint",ga="int",gab="[float, float]",h="int",l="int",lb="[float, float]",lp=1,m2a="float",m3a="float",m="int",nm="int",oe=1,order="int",orb="[int, int]",o="int",oa="[float, float, float]",ob="[float, float]",p="int",pp="int",r="int",rr="float",rs=1,rp=1,sh=1,sz="int",sm="int",sts=1,tx="int",ta="int",tab="[float, float]",ts="int",tp="int",t="int",ubs=1,uvc=1,ulp=1,urp=1,ufo="int",uv=1,v="int",va="angle",vp="[float, float, float]",w="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySelectConstraint.html



-----------------------------------------

polySelectConstraint is undoable, queryable, and NOT editable.

Changes the global polygonal selection constraints.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [int] ['query']
    0(off) 1(on).

-----------------------------------------

ap    : anglePropagation [boolean] ['query']
    If true, selection will be extended to all connected components whose normal is close to any of the normals of the original selection (see angleTolerance)

-----------------------------------------

at    : angleTolerance  [float] ['query']
    When angle propagation is turned on, this controls what is the maximum difference of the normal vectors where the selection propagates.

-----------------------------------------

ab    : anglebound      [[angle, angle]] ['query']
    min and max angles. The given value should be in the current units that Maya is using. See the examples for how to check the current unit.   For vertices : angle between the 2 edges owning the vertex.   For edges : angle between the 2 faces owning the edge.

-----------------------------------------

bo    : border          [boolean] ['query']
    Use "-uvConstraint true" to edit/query UV view constraint. If true, selection will be extended to all connected border components so that the whole "loop" is selected. It also removes all nonborder components from the existing selection (compatibility mode)

-----------------------------------------

bp    : borderPropagation [boolean] ['query']
    If true, selection will be extended to all connected border components so that the whole "loop" is selected.

-----------------------------------------

c     : convexity       [int] ['query']
    0(off) 1(concave) 2(convex).

-----------------------------------------

cr    : crease          [boolean] ['query']
    If true, selection will be extended to all connected creased components.

-----------------------------------------

dis   : disable         [boolean] []
    Toggles off all constraints for all component types, but leaves the other constraint parameters.   This flag may be used together with other ones toggling some constraints on : if so, all constraints are disabled first (no matter the position of the -disable flag in the command line) then the specified ones are activated.

-----------------------------------------

d     : dist            [int] ['query']
    0(off) 1(to point) 2(to axis) 3(to plane).

-----------------------------------------

da    : distaxis        [[float, float, float]] ['query']
    axis. (Normal to the plane in case of distance to plane).

-----------------------------------------

db    : distbound       [[float, float]] ['query']
    min and max distances.

-----------------------------------------

dp    : distpoint       [[float, float, float]] ['query']
    point. (Axis/plane origin in case of distance to axis/plane).

-----------------------------------------

ed    : edgeDistance    [uint] []
    Maximum distance (number of edges) to extend the edge selection for "Contiguous Edges" propagate mode. 0 means to ignore the distance constraint.

-----------------------------------------

ga    : geometricarea   [int] ['query']
    0(off) 1(on).

-----------------------------------------

gab   : geometricareabound [[float, float]] ['query']
    min and max areas.

-----------------------------------------

h     : holes           [int] ['query']
    0(off) 1(holed) 2(non holed).

-----------------------------------------

l     : length          [int] ['query']
    0(off) 1(on).

-----------------------------------------

lb    : lengthbound     [[float, float]] ['query']
    min and max lengths.

-----------------------------------------

lp    : loopPropagation [boolean] ['query']
    If true, edge selection will be extended to a loop.

-----------------------------------------

m2a   : max2dAngle      [float] []
    Maximum angle between two consecutive edges in the 2d tangent plane for "Contiguous Edges" propagate mode.

-----------------------------------------

m3a   : max3dAngle      [float] []
    Maximum angle between two consecutive edges in 3d space for "Contiguous Edges" propagate mode.

-----------------------------------------

m     : mode            [int] ['query']
    0(Off) 1(Next) 2(Current and Next) 3(All and Next).   Off : no constraints are used at all.   Next : constraints will be used to filter next selections.   Current and Next : constraints will be aplied on current selection and then used to filter next selections.   All and Next : all items satisfying constraints are selected.

-----------------------------------------

nm    : nonmanifold     [int] ['query']
    0(off) 1(on)

-----------------------------------------

oe    : oppositeEdges   [boolean] []
    Use the opposite edges

-----------------------------------------

order : order           [int] ['query']
    0(off) 1(on).

-----------------------------------------

orb   : orderbound      [[int, int]] ['query']
    min and max orders. number of owning edges.

-----------------------------------------

o     : orient          [int] ['query']
    0(off) 1(orientation) 2(direction).

-----------------------------------------

oa    : orientaxis      [[float, float, float]] ['query']
    axis.

-----------------------------------------

ob    : orientbound     [[float, float]] ['query']
    min and max angles. The given value should be in the current units that Maya is using. See the examples for how to check the current unit.

-----------------------------------------

p     : planarity       [int] ['query']
    0(off) 1(non planar) 2(planar).

-----------------------------------------

pp    : propagate       [int] ['query']
    0(Off) 1(More) 2(Less) 3(Border) 4(Contiguous Edges) 5(Grow Along Loop) 6(Shrink Along Loop).   More : will add current selection border to current selection.   Less : will remove current selection border from current selection.   Border : will keep only current selection border.   Contiguous Edges : Add edges aligned with the current edges selected. The direction and number of edges selected is controlled by the -m2a, -m3a, and -ed flags.   Grow Along Loop: Will grow current selection along loop, support face, edge, vertex and UV.   Shrink Along Loop: Will shrink current selection along loop, support face, edge, vertex and UV.

-----------------------------------------

r     : random          [int] ['query']
    0(off) 1(on).

-----------------------------------------

rr    : randomratio     [float] ['query']
    ratio [0,1].

-----------------------------------------

rs    : returnSelection [boolean] []
    If true, current selection will not be modified, instead the new selection will be returned as result.

-----------------------------------------

rp    : ringPropagation [boolean] ['query']
    If true, edge selection will be extended to a ring.

-----------------------------------------

sh    : shell           [boolean] ['query']
    If true, selection will be extended to all connected components so that the whole piece of object is selected.

-----------------------------------------

sz    : size            [int] ['query']
    0(off) 1(triangles) 2(quads) 3(nsided).

-----------------------------------------

sm    : smoothness      [int] ['query']
    0(off) 1(hard) 2(smooth).

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that would restore all the current settings.

-----------------------------------------

tx    : textured        [int] ['query']
    0(off) 1(mapped) 2(unmapped).

-----------------------------------------

ta    : texturedarea    [int] ['query']
    0(off) 1(Area specified is unsigned) 2(Area specified is signed).

-----------------------------------------

tab   : texturedareabound [[float, float]] ['query']
    min and max areas.

-----------------------------------------

ts    : textureshared   [int] ['query']
    0(off) 1(on). This option will select any UVs on the currentMap which are shared by more than one vertex

-----------------------------------------

tp    : topology        [int] ['query']
    0(off) 1(non triangulatable) 2(lamina) 3(non triangulatable and lamina)

-----------------------------------------

t     : type            [int] ['query']
    0x0000(none)   0x0001(vertex)   0x8000(edge)   0x0008(face)   0x0010(texture coordinates)

-----------------------------------------

ubs   : uvBorderSelection [boolean] ['query']
    This flag only works on UV view If true, selection will be extended to all UV border components It also removes all components not on UV border from the existing selection

-----------------------------------------

uvc   : uvConstraint    [boolean] []
    If true, applicable constraint flags will work on UV view.  In query mode, this flag can accept a value.

-----------------------------------------

ulp   : uvEdgeLoopPropagation [boolean] ['query']
    Use "-uvConstraint true" to edit/query UV view constraint. If true, UV edge selection will be extended to a loop.

-----------------------------------------

urp   : uvEdgeRingPropagation [boolean] ['query']
    This flag only works on UV view If true, UV edge selection will be extended to a ring.

-----------------------------------------

ufo   : uvFaceOrientation [int] ['query']
    This flag only works on UV view 0(Off) 1(Front Face) 2(Back Face).

-----------------------------------------

uv    : uvShell         [boolean] ['query']
    If true, selection will be extended to all connected components in UV space

-----------------------------------------

v     : visibility      [int] ['query']
    0(off) 1(on).

-----------------------------------------

va    : visibilityangle [angle] ['query']
    angle [0,360].

-----------------------------------------

vp    : visibilitypoint [[float, float, float]] ['query']
    point.

-----------------------------------------

w     : where           [int] ['query']
    0(off) 1(on border) 2(inside).

-----------------------------------------

ws    : wholeSensitive  [boolean]
    Tells how to select faces : either   by picking anywhere inside the face (if true)   or by picking on the face center marker (if false).

    """

def polySelectConstraintMonitor(cc="[string, string]",c=1,d=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySelectConstraintMonitor.html



-----------------------------------------

polySelectConstraintMonitor is undoable, NOT queryable, and NOT editable.

Manage the window to display/edit the polygonal selection constraint
parameters


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cc    : changeCommand   [[string, string]] []
    Specifies the mel callback to refresh the window. First argument is the callback, second is the window name.

-----------------------------------------

c     : create          [boolean] []
    Specifies the Monitor should be created

-----------------------------------------

d     : delete          [boolean]
    Specifies that the Monitor should be removed

    """

def polySeparate(q=1,e=1,cch=1,nds="int",rs=1,sss="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySeparate.html



-----------------------------------------

polySeparate is undoable, queryable, and editable.

This command creates new objects from the given poly. A new object will be
created for each section of the mesh that is distinct (no edges connect it to
the rest of the mesh).  
This command can only separate one object at a time.


-----------------------------------------


Return Value:

string[]  Object name(s) and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rs    : removeShells    [boolean] []
    Remove the shells after creation.

-----------------------------------------

sss   : separateSpecificShell [int]
    List of shell ids to be separated.

    """

def polySetToFaceNormal(su=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySetToFaceNormal.html



-----------------------------------------

polySetToFaceNormal is undoable, NOT queryable, and NOT editable.

This command takes selected polygonal vertices or vertex-faces and changes
their normals. If the option  userNormal  is used, the new normal values will
be the face normals arround the vertices/vertex-faces. Otherwise the new
normal values will be default values according to the internal calculation.


-----------------------------------------


Return Value:

string  of the node name


-----------------------------------------


Flags:

-----------------------------------------

su    : setUserNormal   [boolean]
    when this flag is presented, user normals will be created on each vertex face and the values will be the face normal value. Otherwise the normal values will be the internal computing results. Default is false.

    """

def polySewEdge(q=1,e=1,cch=1,ch=1,n="string",nds="int",tx=1,t="linear",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySewEdge.html



-----------------------------------------

polySewEdge is undoable, queryable, and editable.

Merge border edges within a given threshold.  

Perform pair-wise comparison of selected edges. Pairs whose corresponding
vertices meet threshold conditions and whose orientations are aligned (i.e.
their respective normals point in the same direction) are merged, as are the
vertices (in other words, vertices are shared).

Resulting mesh may have extra vertices or edges to ensure geometry is valid.  
Edges must be on the same object to be merged.  
Default : share only vertices lying exactly at the same place. (polySewEdge -t
0.0)


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tx    : texture         [boolean] ['query', 'edit']
    If true : texture is sewn as well as the 3d edge.   C: Default is true.   Q: When queried, this flag returns an int.

-----------------------------------------

t     : tolerance       [linear] ['query', 'edit']
    The tolerance to sew edges (edge distance)   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polySlideEdge(a=1,d="uint",ed="float",sym=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySlideEdge.html



-----------------------------------------

polySlideEdge is undoable, NOT queryable, and NOT editable.

Moves an edge loop selection along the edges connected to the sides of its
vertices.


-----------------------------------------


Return Value:

boolean  Success value


-----------------------------------------


Flags:

-----------------------------------------

a     : absolute        [boolean] []
    This flag specifies whether or not the command uses absolute mode If in absolute then all vertices will move the same distance (the specified percentage of the smallest edge)   C: Default is off

-----------------------------------------

d     : direction       [uint] []
    This flag specifies the direction of the slide edge movement 0: is left direction (relative) 1: is right direction (relative) 2: is normal direction (relative)   C: Default is 0

-----------------------------------------

ed    : edgeDirection   [float] []
    This flag specifies the relative percentage to move along the edges on either side of the vertices along the edge loop   C: Default is 0.0

-----------------------------------------

sym   : symmetry        [boolean]
    This flag specifies whether or not the command will do a symmetrical slide. Only takes effect when symmetry is enabled.   C: Default is off

    """

def polySmooth(q=1,e=1,cch=1,ch=1,n="string",nds="int",c="float",deg="int",dv="int",dpe="int",kb=1,khe=1,kmb="int",ksb=1,xkt=1,kt=1,mth="int",ocr="int",ofb="int",ofc=1,ost=1,ovb="int",peh=1,ps="float",ro="float",suv=1,sl="int",sdt="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySmooth.html



-----------------------------------------

polySmooth is undoable, queryable, and editable.

Smooth a polygonal object. This command works on polygonal objects or faces.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

c     : continuity      [float] ['query', 'edit']
    This flag specifies the smoothness parameter. The minimum value of 0.0 specifies that the faces should only be subdivided. Maximum value of 1.0 smooths the faces as much as possible.   C: Default is 1.0   Q: When queried, this flag returns a float.

-----------------------------------------

deg   : degree          [int] []
    Degree of the resulting limit surface

-----------------------------------------

dv    : divisions       [int] ['query', 'edit']
    This flag specifies the number of recursive smoothing steps.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

dpe   : divisionsPerEdge [int] []
    Number of subdivisions along one edge for each step.

-----------------------------------------

kb    : keepBorder      [boolean] ['query', 'edit']
    If on, the border of the object will not move during smoothing operation.   C: Default is "on".   Q: When queried, this flag returns an int.

-----------------------------------------

khe   : keepHardEdge    [boolean] ['query', 'edit']
    If true, vertices on hard edges will not be modified.   C: Default is false.   Q: When queried, this flag returns a boolean.

-----------------------------------------

kmb   : keepMapBorders  [int] []
    Treatment of UV map borders 0 - all map border edges will be smoothed 1 - map borders that are also geometry borders will be smoothed 2 - no map borders will be smoothed

-----------------------------------------

ksb   : keepSelectionBorder [boolean] ['query', 'edit']
    If true, vertices on border of the selection will not be modified.   C: Default is false.   Q: When queried, this flag returns a boolean.

-----------------------------------------

xkt   : keepTesselation [boolean] []
    If true: the object will be smoothed consistently from frame to frame. This is best when the object is being deformed or animated . If false: non- starlike faces will be triangulated before being smoothed. This avoids self- overlapping faces, but could lead to a change in topology (number of vertices/faces) from frame to frame, during an animated deformation.

-----------------------------------------

kt    : keepTessellation [boolean] []
    If true: the object will be smoothed consistently from frame to frame. This is best when the object is being deformed or animated . If false: non- starlike faces will be triangulated before being smoothed. This avoids self- overlapping faces, but could lead to a change in topology (number of vertices/faces) from frame to frame, during an animated deformation.

-----------------------------------------

mth   : method          [int] []
    Type of smoothing algorithm to use 0 - exponential - traditional smoothing 1 - linear - number of faces per edge grows linearly

-----------------------------------------

ocr   : osdCreaseMethod [int] ['query', 'edit']
    Controls how boundary edges and vertices are interpolated.

-----------------------------------------

ofb   : osdFvarBoundary [int] ['query', 'edit']
    Controls how boundaries are treated for face-varying data (UVs and Vertex Colors).

-----------------------------------------

ofc   : osdFvarPropagateCorners [boolean] ['query', 'edit']
    

-----------------------------------------

ost   : osdSmoothTriangles [boolean] ['query', 'edit']
    Apply a special subdivision rule be applied to all triangular faces that was empirically determined to make triangles subdivide more smoothly.

-----------------------------------------

ovb   : osdVertBoundary [int] ['query', 'edit']
    Controls how boundary edges and vertices are interpolated.

-----------------------------------------

peh   : propagateEdgeHardness [boolean] ['query', 'edit']
    If true, edges which are a result of smoothed edges will be given the same value for their edge hardness. New subdivided edges will always be smooth.   C: Default is false.   Q: When queried, this flag returns a boolean.

-----------------------------------------

ps    : pushStrength    [float] []
    COMMENT 0.0 is approximation, 1.0 is interpolation scheme

-----------------------------------------

ro    : roundness       [float] []
    When 1.0, push vectors are renormalized to keep length constant

-----------------------------------------

suv   : smoothUVs       [boolean] []
    If true: UVs as well as geometry will be smoothed

-----------------------------------------

sl    : subdivisionLevels [int] []
    Number of times the subdivide and smooth operation is run.

-----------------------------------------

sdt   : subdivisionType [int]
    The subdivision method used for smoothing.   C: Default is 0.   0: Maya Catmull-Clark   1: OpenSubdiv Catmull-Clark

    """

def polySoftEdge(q=1,e=1,a="angle",cch=1,ch=1,n="string",nds="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySoftEdge.html



-----------------------------------------

polySoftEdge is undoable, queryable, and editable.

Selectively makes edges soft or hard.

  
An edge will be made hard if the angle between two owning faces is sharper
(larger) than the smoothing angle.  
An edge wil be made soft if the angle between two owning facets is flatter
(smaller) than the smoothing angle.


-----------------------------------------


Return Value:

string  The name of the polySoftEdge node.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [angle] ['query', 'edit']
    Smoothing angle.   C: Default is 30 degrees.   Q: When queried, this flag returns a float.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polySphere(q=1,e=1,ax="[linear, linear, linear]",cuv="int",r="linear",sa="int",sh="int",sx="int",sy="int",tx="int",cch=1,ch=1,n="string",nds="int",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySphere.html



-----------------------------------------

polySphere is undoable, queryable, and editable.

The sphere command creates a new polygonal sphere.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the sphere.   Q: When queried, this flag returns a float[3].

-----------------------------------------

cuv   : createUVs       [int] []
    This flag alows a specific UV mechanism to be selected, while creating the sphere.   The valid values are 0, 1, or 2.   0 implies that no UVs will be generated (No texture to be applied).      1 implies UVs are created with pinched at poles      2 implies UVs are created with sawtooth at poles      For better understanding of these options, you may have to open the   texture view window      C: Default is 2

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    This flag specifies the radius of the sphere.   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

sa    : subdivisionsAxis [int] ['query', 'edit']
    Subdivisions around the axis.

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height of the sphere.

-----------------------------------------

sx    : subdivisionsX   [int] ['query', 'edit']
    This specifies the number of subdivisions in the X direction for the sphere.   C: Default is 20.   Q: When queried, this flag returns an int.

-----------------------------------------

sy    : subdivisionsY   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Y direction for the sphere.   C: Default is 20.   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [int] []
    This flag is obsolete and will be removed in the next release. The -cuv/createUVs flag should be used instead.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node (where applicable).

    """

def polySphericalProjection(q=1,e=1,ic="[float, float]",icx="float",icy="float",imageScale="[float, float]",isu="float",isv="float",pc="[linear, linear, linear]",pcx="linear",pcy="linear",pcz="linear",phs="linear",ps="[linear, linear]",psu="linear",psv="linear",r="linear",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",ra="angle",sc=1,cch=1,ch=1,cm=1,ibd=1,kir=1,md="string",n="string",nds="int",pi=1,sf=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySphericalProjection.html



-----------------------------------------

polySphericalProjection is undoable, queryable, and editable.

TpolyProjCmdBase is a base class for the command to create a mapping on the
selected polygonal faces. Projects a spherical map onto an object.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ic    : imageCenter     [[float, float]] ['query', 'edit']
    This flag specifies the center point of the 2D model layout.   C: Default is 0.5 0.5.   Q: When queried, this flag returns a float[2].

-----------------------------------------

icx   : imageCenterX    [float] ['query', 'edit']
    This flag specifies X for the center point of the 2D model layout.   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

icy   : imageCenterY    [float] ['query', 'edit']
    This flag specifies Y for the center point of the 2D model layout.   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

imageScale : imageScale      [[float, float]] ['query', 'edit']
    This flag specifies the UV scale : Enlarges or reduces the 2D version of the model in U or V space relative to the 2D centerpoint.   C: Default is 1.0 1.0.   Q: When queried, this flag returns a float[2].

-----------------------------------------

isu   : imageScaleU     [float] ['query', 'edit']
    This flag specifies the U scale : Enlarges or reduces the 2D version of the model in U space relative to the 2D centerpoint.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

isv   : imageScaleV     [float] ['query', 'edit']
    This flag specifies the V scale : Enlarges or reduces the 2D version of the model in V space relative to the 2D centerpoint.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pc    : projectionCenter [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the origin point from which the map is projected.   C: Default is 0.0 0.0 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

pcx   : projectionCenterX [linear] ['query', 'edit']
    This flag specifies X for the origin point from which the map is projected.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pcy   : projectionCenterY [linear] ['query', 'edit']
    This flag specifies Y for the origin point from which the map is projected.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pcz   : projectionCenterZ [linear] ['query', 'edit']
    This flag specifies Z for the origin point from which the map is projected.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

phs   : projectionHorizontalSweep [linear] ['query', 'edit']
    The angle swept horizontally by the projection. The range is [0, 360].

-----------------------------------------

ps    : projectionScale [[linear, linear]] ['query', 'edit']
    This flag specifies the width and the height of the map relative to the 3D projection axis.   C: Default is 180.0 90.0.   Q: When queried, this flag returns a float[2].

-----------------------------------------

psu   : projectionScaleU [linear] ['query', 'edit']
    This flag specifies the width of the map relative to the 3D projection axis : the scale aperture. The range is [0, 360].   C: Default is 180.0.   Q: When queried, this flag returns a float.

-----------------------------------------

psv   : projectionScaleV [linear] ['query', 'edit']
    This flag specifies the height of the map relative to the 3D projection axis : the scale height.   C: Default is 90.0.   Q: When queried, this flag returns a float.

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    Used by the UI : Manipulator.

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    This flag specifies the mapping rotate angles.   C: Default is 0.0 0.0 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    This flag specifies X mapping rotate angle.   C: Default is 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    This flag specifies Y mapping rotate angle.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    This flag specifies Z mapping rotate angle.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ra    : rotationAngle   [angle] ['query', 'edit']
    This flag specifies the rotation angle in the mapping space. When the angle is positive, then the map rotates counterclockwise on the mapped model, whereas when it is negative then the map rotates clockwise on the mapped model.   C: Default is 10.0.   Q: When queried, this flag returns a float.

-----------------------------------------

sc    : seamCorrect     [boolean] ['query', 'edit']
    This flag specifies to perform a seam correction on the mapped faces.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cm    : createNewMap    [boolean] ['query']
    This flag when set true will create a new map with a the name passed in, if the map does not already exist.

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    This flag specifies if the projection node should be inserted before or after deformer nodes already applied to the shape. Inserting the projection after the deformer leads to texture swimming during animation and is most often undesirable.   C: Default is on.

-----------------------------------------

kir   : keepImageRatio  [boolean] []
    True means keep any image ratio

-----------------------------------------

md    : mapDirection    [string] []
    This flag specifies the mapping direction.   'x', 'y' and 'z' projects the map along the corresponding axis.   'c' projects along the current camera viewing direction.   'p' does perspective projection if current camera is perspective.   'b' projects along the best plane fitting the objects selected.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pi    : perInstance     [boolean] []
    True if the new map is per-instance, otherwise it is shared.

-----------------------------------------

sf    : smartFit        [boolean] []
    True means use the smart fit algorithm

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polySplit(q=1,e=1,aef="float",de=1,ep="[int, float]",fp="[int, float, float, float]",ief=1,ip="[int, float, [, float, float, ]]",pc="name",pct="float",sma="angle",s="int",ch=1,n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySplit.html



-----------------------------------------

polySplit is undoable, queryable, and editable.

Split facets/edges of a polygonal object.

The first and last arguments must be edges. Intermediate points may lie on
either a shared face or an edge which neighbors the previous point.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aef   : adjustEdgeFlow  [float] ['query', 'edit']
    The weight value of the edge vertices to be positioned.

-----------------------------------------

de    : detachEdges     [boolean] []
    Value of the detachEdges attribute for the resulting poly split node.

-----------------------------------------

ep    : edgepoint       [[int, float]] []
    The given edge is split into two new edges by inserting a new vertex located the given percentage along the edge.   Note: This flag is not recommended for use from Python. See the insertpoint flag instead.

-----------------------------------------

fp    : facepoint       [[int, float, float, float]] []
    A new vertex is inserted, lying at the given coordinates inside the given face. Coordinates are given in the local object space.   Note: This flag is not recommended for use from Python. See the insertpoint flag instead.

-----------------------------------------

ief   : insertWithEdgeFlow [boolean] ['query', 'edit']
    True to enable edge flow. Otherwise, the edge flow is disabled.

-----------------------------------------

ip    : insertpoint     [[int, float, [, float, float, ]]] []
    This flag allows the caller to insert a new vertex into an edge or a face.   To insert a new vertex in an edge, pass the index of the edge and a percentage along the edge at which to insert the new vertex. When used to insert a vertex into an edge, this flag takes two arguments.   To insert a new vertex into a face, pass the index of the face and three values which define the coordinates for the insertion in local object space. When used to insert a vertex into a face, this flag takes four arguments.   This flag replaces the edgepoint and facepoint flags.

-----------------------------------------

pc    : projectedCurve  [name] []
    Curves to be projected.

-----------------------------------------

pct   : projectedCurveTolerance [float] []
    Tolerance for curve projection.

-----------------------------------------

sma   : smoothingangle  [angle] []
    Subdivide new edges will be soft if less then this angle.   C: Default is 0.0

-----------------------------------------

s     : subdivision     [int] ['query', 'edit']
    Subdivide new edges into the given number of sections. Edges involving free points won't be subdivided.   C: Default is 1 (no subdivision).   Q: When queried, this flag returns an int.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string]
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

    """

def polySplitEdge(q=1,e=1,op="int",cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySplitEdge.html



-----------------------------------------

polySplitEdge is undoable, queryable, and editable.

Split Edges.  

There are two operations for this command depending on the value of the
-operation flag.

If -operation is set to 1 then this command will split apart faces along all
selected manifold edges.

If -operation is set to 0 then this command will split non-manifold edges so
as to make them manifold edges. It creates the minimum number of edges that
can be created to make the edge manifold.

The default value for -operation is 1, operate on manifold edges.

Resulting mesh may have extra vertices or edges to ensure geometry is valid.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

op    : operation       [int] ['query', 'edit']
    0 means use a Non-Manifold method, 1 means use a Manifold method

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polySplitRing(q=1,e=1,aef="float",cch=1,ch=1,dr=1,div="int",epc=1,fq=1,ief=1,n="string",nds="int",pio="float",pis="float",pfv="float",pi="int",pp="float",re="int",sma="angle",stp="int",uem=1,fne=1,wt="float",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySplitRing.html



-----------------------------------------

polySplitRing is undoable, queryable, and editable.

Splits a series of ring edges of connected quads and inserts connecting edges
between them.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aef   : adjustEdgeFlow  [float] ['query', 'edit']
    The weight value of the edge vertices to be positioned.   Default: 1.0f

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

dr    : direction       [boolean] ['query', 'edit']
    This attribute is used when doing an absolute split. If true then the distance is taken from the start vertex of the root edge. If false the distance is taken from the end vertext of the root edge.   Default: true

-----------------------------------------

div   : divisions       [int] ['query', 'edit']
    Number of divisions.   Default: 2

-----------------------------------------

epc   : enableProfileCurve [boolean] ['query', 'edit']
    Enables the use of the profile curve.   Default: true

-----------------------------------------

fq    : fixQuads        [boolean] ['query', 'edit']
    Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.   Default: false

-----------------------------------------

ief   : insertWithEdgeFlow [boolean] ['query', 'edit']
    True to enable edge flow. Otherwise, the edge flow is disabled.   Default: false

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pio   : profileCurveInputOffset [float] ['query', 'edit']
    Changes the offset to the multisplit profile curve. eg. if the profile curve values go between 0 and 1 and this value is set to -1 then the profile curves values will be adjusted to go between -1 and 0.   Default: 0.0f

-----------------------------------------

pis   : profileCurveInputScale [float] ['query', 'edit']
    Changes the range of values that the profile curve represents. eg. if the profile curve values go between 0 and 1 and this value is set to 2 then the profile curves values will be adjusted to go between 0 and 2.   Default: 1.0f

-----------------------------------------

pfv   : profileCurve_FloatValue [float] ['query', 'edit']
    ?????

-----------------------------------------

pi    : profileCurve_Interp [int] ['query', 'edit']
    ?????   Default: 0

-----------------------------------------

pp    : profileCurve_Position [float] ['query', 'edit']
    ?????

-----------------------------------------

re    : rootEdge        [int] ['query', 'edit']
    The weight attribute uses the start vertex of this edge to determine where the new split occurs.   Default: -1

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

fne   : useFaceNormalsAtEnds [boolean] ['query', 'edit']
    When doing a multisplit on a set of non-closed edge ring this will toggle the normals at the ends of the split to be calculated as the edge normal or the face normal.   Default: true

-----------------------------------------

wt    : weight          [float] ['query', 'edit']
    Weight value controlling the relative positioning of the new points on existing edges. Range is [0.0, 1.0]. Value of 0.1 indicates the new edges will be placed closer to the start vertex of the first edge of the sequence of edges.   Default: 0.5

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polySplitVertex(q=1,e=1,cch=1,ch=1,n="string",nds="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySplitVertex.html



-----------------------------------------

polySplitVertex is undoable, queryable, and editable.

Use this command to split one or more vertices.

A mesh is made up of one or more faces. The faces are defined by edges which
connect vertices together. Typically a face will share vertices and edges with
adjacent faces in the same mesh. Sharing vertices and edges helps reduce the
amount of memory used by a mesh. It also ensures that when a face is moved,
all the connected faces move together.  
Sometimes you may want to separate a face from its connected faces so that it
may be moved in isolation. There are three ways to accomplish this depending
upon which parts of the face you want to extract:  
polySplitVertex | split one or more vertices so that each face that shared the
vertex acquires its own copy of the vertex  
---|---  
polySplitEdge | split one or more edges so that each face that shared the
vertex acquires its own copy of the edge  
polyChipOff | completely extract the face so that it has its own vertices and
edges  
  
Notice that the area of affect of each operation is different. polySplitVertex
will affect all the edges and faces that shared the vertex. This is the
broadest effect. polySplitEdge will only affect the faces which shared the
edge and polyChipOff will affect a specific face. If we just count vertices to
measure the effect of each command when splitting all components of a face,
starting from a 3x3 plane which has 16 vertices and we were to split the
middle face:  
polySplitVertex applied to the four vertices would end up creating 12 new
vertices  
---  
polySplitEdge applied to the four edges would end up creating 4 new vertices  
polyChipOff applied to the middle face would end up creating 4 new vertices  
  
Note that polySplitVertex may create non-manifold geometry as a part of this
operation. You can use Polygons->Cleanup afterwards to to clean up any non-
manifold geometry.


-----------------------------------------


Return Value:

string  The polySplitVert node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polyStraightenUVBorder(q=1,e=1,bo="float",cch=1,ch=1,c="float",gt="int",n="string",nds="int",pl="float",uvs="string",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyStraightenUVBorder.html



-----------------------------------------

polyStraightenUVBorder is undoable, queryable, and editable.

Move border UVs along a simple curve.


-----------------------------------------


Return Value:

string  The node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bo    : blendOriginal   [float] ['query']
    Interpolation factor between the target and original UV shape. When the value is 0, the UVs will exactly fit the target curve. When the value is 1, no UV move.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

c     : curvature       [float] ['query']
    How curved the UV path will be. 0 is a straight line. When the values is 1, the mid point of the curve will be moved away from a straight line by 1/2 the length of the UV segment.

-----------------------------------------

gt    : gapTolerance    [int] ['query']
    When non 0, Small gaps between UV selection are filled. The integer number represent how many UVs must be traversed to connect togeterh selected pieces.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pl    : preserveLength  [float] ['query']
    How much we want to respect the UV edge ratios. When the value is 1, we build new UV position along the desired curve, respecting the original UV spacings. When the value is 0, new UVs are equally spaced along the curve.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the UV set to be created

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polySubdivideEdge(q=1,e=1,cch=1,ch=1,dv="int",n="string",nds="int",s="linear",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySubdivideEdge.html



-----------------------------------------

polySubdivideEdge is undoable, queryable, and editable.

Subdivides an edge into two or more subedges.

  
Default : divide edge into two edges of equal length.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

dv    : divisions       [int] ['query', 'edit']
    The maximum number of vertices to be inserted in each edge. This number may be reduced if it creates edges shorter than the specified minimum length.   C: Default is 1 (divide edges in half).   Q: When queried, this flag returns an int.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

s     : size            [linear] ['query', 'edit']
    The minimum length of each subedge created. If the given subdivision creates edges that are shorter than this length, the number of divisions is changed to respect min length.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def polySubdivideFacet(q=1,e=1,dv="int",duv="int",dvv="int",m="int",sbm="int",cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polySubdivideFacet.html



-----------------------------------------

polySubdivideFacet is undoable, queryable, and editable.

Subdivides a face into quads or triangles.

  
In quad mode, a center point is introduced at the center of each face and
midpoints are inserted on all the edges of each face. New faces (all
quadrilaterals) are built by adding edges from the midpoints towards the
center.  
In triangle mode, only the center point is created; new faces (all triangles)
are created by connecting the center point to all the existing vertices of the
face.  
Default : one subdivision step in quad mode (polySubdFacet -dv 1 -m 0;)


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

dv    : divisions       [int] ['query', 'edit']
    This number specifies how many times to recursively subdivide the selected faces. For example, with divisions set to 3 in quad mode, each initial quadrilateral will be recursively subdivided into 4 subfaces 3 times, yielding a total of 4 * 4 * 4 = 64 faces.   C: Default is 1.   Q: When queried, this flag returns an int.

-----------------------------------------

duv   : divisionsU      [int] ['query', 'edit']
    The number of subdivision steps to perform along the U direction. A square face will be subdivided into 4^(divisions) faces in quad mode, 4*3^(divisions-1) in triangle mode.

-----------------------------------------

dvv   : divisionsV      [int] ['query', 'edit']
    The number of subdivision steps to perform along the V direction. A square face will be subdivided into 4^(divisions) faces in quad mode, 4*3^(divisions-1) in triangle mode.

-----------------------------------------

m     : mode            [int] ['query', 'edit']
    The subdivision mode.   0: subdivision into quads   1: subdivision into triangles   C: Default is 0.   Q: When queried, this flag returns an int.

-----------------------------------------

sbm   : subdMethod      [int] ['query', 'edit']
    Type of subdivision to use: 0 - exponential - traditional subdivision 1 - linear - number of faces per edge grows linearly

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyTorus(q=1,e=1,ax="[linear, linear, linear]",cch=1,ch=1,cuv=1,n="string",nds="int",o=1,r="linear",sr="linear",sa="int",sh="int",sx="int",sy="int",tx=1,tw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyTorus.html



-----------------------------------------

polyTorus is undoable, queryable, and editable.

The torus command creates a new polygonal torus.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the primitive axis used to build the torus.   Q: When queried, this flag returns a vector.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

cuv   : createUVs       [boolean] ['query', 'edit']
    Create UVs or not.   Default: true

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node (where applicable).

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    Radius of the torus.   Default: 1.0

-----------------------------------------

sr    : sectionRadius   [linear] ['query', 'edit']
    Section of the torus.   Default: 0.50

-----------------------------------------

sa    : subdivisionsAxis [int] ['query', 'edit']
    Subdivisions about the vertical axis.   Default: 20

-----------------------------------------

sh    : subdivisionsHeight [int] ['query', 'edit']
    Subdivisions along the height.   Default: 20

-----------------------------------------

sx    : subdivisionsX   [int] ['query', 'edit']
    This specifies the number of subdivisions in the X direction for the torus (number of sections).   C: Default is 20.   Q: When queried, this flag returns an int.

-----------------------------------------

sy    : subdivisionsY   [int] ['query', 'edit']
    This flag specifies the number of subdivisions in the Y direction for the torus (number of segments per section).   C: Default is 20.   Q: When queried, this flag returns an int.

-----------------------------------------

tx    : texture         [boolean] ['query', 'edit']
    Apply texture or not. this is an old attribute. This is unsupported and would be removed in a future release.   Default: true

-----------------------------------------

tw    : twist           [angle]
    Twist angle of the torus.   Default: 0.0

    """

def polyTransfer(q=1,e=1,ao="string",cch=1,ch=1,n="string",nds="int",uv=1,vc=1,v=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyTransfer.html



-----------------------------------------

polyTransfer is undoable, queryable, and editable.

Transfer information from one polygonal object to another one. Both objects
must have identical topology, that is same vertex, edge, and face numbering.
The flags specify which of the vertices, UV sets or vertex colors will be
copied.


-----------------------------------------


Return Value:

string  representing the node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ao    : alternateObject [string] ['query', 'edit']
    Name of the alternate object.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

uv    : uvSets          [boolean] ['query', 'edit']
    When true, the UV sets are copied from the alternate object.   C: Default is "on".

-----------------------------------------

vc    : vertexColor     [boolean] ['query', 'edit']
    When true, the colors per vertex are copied from the alternate object.   C: Default is "off".

-----------------------------------------

v     : vertices        [boolean]
    When true, the vertices positions are copied from the alternate object.   C: Default is "off".

    """

def polyTriangulate(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyTriangulate.html



-----------------------------------------

polyTriangulate is undoable, queryable, and editable.

Triangulation breaks polygons down into triangles, ensuring that all faces are
planar and non-holed. Triangulation of models can be beneficial in many areas.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyUnite(q=1,e=1,cch=1,muv="int",nds="int",cp=1,op=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyUnite.html



-----------------------------------------

polyUnite is undoable, queryable, and editable.

This command creates a new poly as an union of a list of polys If no objects
are specified in the command line, then the objects from the active list are
used.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

muv   : mergeUVSets     [int] []
    Specify how UV sets will be merged on the output mesh. The choices are 0 | 1 | 2. 0 = Do not merge. Each UV set on each mesh will become a new UV set in the output. 1 = Merge by name. UV sets with the same name will be merged. 2 = Merge by UV links. UV sets will be merged so that UV linking on the input meshes continues to work. The default is 1 (merge by name).

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

cp    : centerPivot     [boolean] []
    Set the resulting object's pivot to the center of the selected objects bounding box.

-----------------------------------------

op    : objectPivot     [boolean]
    Set the resulting object's pivot to last selected object's pivot.

    """

def polyUVCoverage(ur="[float, float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyUVCoverage.html



-----------------------------------------

polyUVCoverage is undoable, NOT queryable, and NOT editable.

Return the UV space coverage of the specified components.  
If no objects are specified in the command line, then components from
selection list will be used.


-----------------------------------------


Return Value:

float[]  UV space coverage percentage


-----------------------------------------


Flags:

-----------------------------------------

ur    : uvRange         [[float, float, float, float]]
    UV space range for calculating the coverage The 4 values specify the minimum U, V and maximum U, V in that order. Default is 0.0 0.0 1.0 1.0.

    """

def polyUVOverlap(noc=1,oc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyUVOverlap.html



-----------------------------------------

polyUVOverlap is undoable, NOT queryable, and NOT editable.

Return the required result on the specified components.  
If no objects are specified in the command line, then components from
selection list will be used.


-----------------------------------------


Return Value:

selectionItem[]  List of poly components


-----------------------------------------


Flags:

-----------------------------------------

noc   : nonOverlappingComponents [boolean] []
    Return non-overlapping components based on selected/specified components

-----------------------------------------

oc    : overlappingComponents [boolean]
    Return overlapping components based on selected/specified components

    """

def polyUVRectangle(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyUVRectangle.html



-----------------------------------------

polyUVRectangle is undoable, queryable, and editable.

Given two vertices, does one of the following: 1) If the vertices define
opposite corners of a rectangular area of quads, assigns a grid of UVs
spanning the 0-1 area to that rectangle. 2) If the vertices define an edge in
a rectangular and topologically cylindrical area of quads, assigns UVs
spanning the 0-1 area to that cylindrical patch, using the defined edge as the
U=0 edge.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def polyUVSet(q=1,e=1,auv=1,uvn=1,awc=1,cp=1,cr=1,luv=1,cpi=1,cuv=1,d=1,gen=1,nuv="string",pi=1,pr=1,rn=1,ro=1,si=1,us=1,uvs="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyUVSet.html



-----------------------------------------

polyUVSet is undoable, queryable, and editable.

Command to do the following to uv sets: \- delete an existing uv set. \-
rename an existing uv set. \- create a new empty uv set. \- copy the values
from one uv set to a another pre-existing uv set. \- reorder two uv sets \-
set the current uv set to a pre-existing uv set. \- modify sharing between
instances of per-instance uv sets \- query the current uv set. \- set the
current uv set to the last uv set added to an object. \- query the names of
all uv sets.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

auv   : allUVSets       [boolean] ['query', 'edit']
    This flag when used in in a query will return a list of all of the uv set names

-----------------------------------------

uvn   : allUVSetsIndices [boolean] ['query', 'edit']
    This flag when queried will return a list of the logical plug indices of all the uv sets in the sparse uv set array.

-----------------------------------------

awc   : allUVSetsWithCount [boolean] ['query', 'edit']
    This flag when used in a query will return a list of all of the uv set family names, with a count appended to the perInstance sets indicating the number of instances in the uv set shared by the specified or selected shape.

-----------------------------------------

cp    : copy            [boolean] ['query', 'edit']
    This flag when used will result in the copying of the uv set corresponding to name specified with the uvSet flag to the uvset corresponding to the name specified with the newUVSet flag

-----------------------------------------

cr    : create          [boolean] ['query', 'edit']
    This flag when used will result in the creation of an empty uv set corresponding to the name specified with the uvSet flag. If a uvSet with that name already exists, then no new uv set will be created.

-----------------------------------------

luv   : currentLastUVSet [boolean] ['query', 'edit']
    This flag when used will set the current uv set that the object needs to work on, to be the last uv set added to the object. If no uv set exists for the object, then no uv set name will be returned.

-----------------------------------------

cpi   : currentPerInstanceUVSet [boolean] ['query', 'edit']
    This is a query-only flag for use when the current uv set is a per- instance uv set family. This returns the member of the set family that corresponds to the currently select instance.

-----------------------------------------

cuv   : currentUVSet    [boolean] ['query', 'edit']
    This flag when used will set the current uv set that the object needs to work on, to be the uv set corresponding to the name specified with the uvSet flag. This does require that a uvSet with the specified name exist. When queried, this returns the current uv set.

-----------------------------------------

d     : delete          [boolean] ['query', 'edit']
    This flag when used will result in the deletion of the uv set corresponding to the name specified with the uvSet flag.

-----------------------------------------

gen   : genNewUVSet     [boolean] ['query', 'edit']
    This is a query-only flag to generate a new unique name.

-----------------------------------------

nuv   : newUVSet        [string] ['query', 'edit']
    Specifies the name that the uv set corresponding to the name specified with the uvSet flag, needs to be renamed to.

-----------------------------------------

pi    : perInstance     [boolean] ['query', 'edit']
    This flag can be used in conjunction with the create flag to indicate whether or not the uv set is per-instance. When you create a per-instance uv set, the set will be applied as shared between all selected instances of the shape unless the unshared flag is used. The perInstance flag can be used in query mode with the currentUVSet or allUVSets flag to indicate that the set family names (i.e. not containing instance identifiers) will be returned by the query.  In query mode, this flag can accept a value.

-----------------------------------------

pr    : projections     [boolean] ['query', 'edit']
    This flag when used in a query will return a list of polygon uv projection node names. The order of the list is from most-recently-applied to least-recently-applied.

-----------------------------------------

rn    : rename          [boolean] ['query', 'edit']
    This flag when used will result in the renaming of the uv set corresponding to the name specified with the uvSet flag to the name specified using the newUVSet flag.

-----------------------------------------

ro    : reorder         [boolean] ['query', 'edit']
    This flag when used will result in the reordering of two uv sets corresponding to name specified with the uvSet flag, and the uvset corresponding to the name specified with the newUVSet flag

-----------------------------------------

si    : shareInstances  [boolean] ['query', 'edit']
    This flag is used to modify the sharing of per-instance uv sets within a given uv set family so that all selected instances share the specified set. In query mode, it returns a list of the instances that share the set specified by the uvSet flag.

-----------------------------------------

us    : unshared        [boolean] ['query', 'edit']
    This flag can be used in conjunction with the create and perInstance flags to indicate that the newly created per-instance set should be created with a separate set per instance.

-----------------------------------------

uvs   : uvSet           [string]
    Specifies the name of the uv set that this command needs to work on. This flag has to be specified for this command to do anything meaningful other than query the current uv set.  In query mode, this flag needs a value.

    """

def polyUVStackSimilarShells(om=1,to="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyUVStackSimilarShells.html



-----------------------------------------

polyUVStackSimilarShells is undoable, NOT queryable, and NOT editable.

Stack Similar UV Shells.


-----------------------------------------


Return Value:

string[]  UVs of stacked UV Shells or target UV shells.


-----------------------------------------


Flags:

-----------------------------------------

om    : onlyMatch       [boolean] []
    If this flag is true, only match UV shells and return UVs of target UV shells but don't stack.

-----------------------------------------

to    : tolerance       [float]
    The tolerance setting for stacking how similar UV shells.

    """

def polyWedgeFace(q=1,e=1,ax="[float, float, float]",cch=1,cen="[float, float, float]",ch=1,d="int",ed="int",n="string",nds="int",wa="angle",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyWedgeFace.html



-----------------------------------------

polyWedgeFace is undoable, queryable, and editable.

Extrude faces about an axis. The axis is the average of all the selected
edges. If the edges are not aligned, the wedge may not look intuitive. To
separately wedge faces about different wedge axes, the command should be
issued as many times as the wedge axes. (as in the second example)


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[float, float, float]] []
    This flag (along with -center) can be used instead of the -edge flag to specify the axis about which the wedge is performed. The flag expects three coordinates that form a vector about which the rotation is performed.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cen   : center          [[float, float, float]] []
    This flag (along with -axis) can be used instead of the -edge flag to specify the location about which the wedge is performed. The flag expects three coordinates that define the center of rotation.

-----------------------------------------

ch    : constructionHistory [boolean] ['query']
    Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.   Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.

-----------------------------------------

d     : divisions       [int] []
    This flag specifies the number of subdivisions along the extrusion.

-----------------------------------------

ed    : edge            [int] []
    This flag specifies the edgeId that should be used to perform the wedge about. Multiple edges can be specified. The wedge operation is performed about an axis that is the average of all the edges. It is recommended that only colinear edges are used, otherwise the result may not look intuitive.  Instead of specifying the -edge flag, the wedge can be performed about a point and axis. See the -center and -axis flags for details.

-----------------------------------------

n     : name            [string] []
    Give a name to the resulting node.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

wa    : wedgeAngle      [angle] []
    This flag specifies the angle of rotation.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is off.   Q: When queried, this flag returns an int.

    """

def setXformManip(q=1,su=1,s=1,urp=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setXformManip.html



-----------------------------------------

setXformManip is undoable, queryable, and NOT editable.

This command changes some of the settings of the xform manip, to control its
appearance.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

su    : showUnits       [boolean] ['query']
    If set to true, the xform manip displays current units; otherwise, the manip hides them.

-----------------------------------------

s     : suppress        [boolean] ['query']
    If set to true, the xform manip is suppressed and therefore not visible or usable.

-----------------------------------------

urp   : useRotatePivot  [boolean] ['query']
    If set to true, the xform manip uses the rotate pivot; otherwise, the manip uses the bounding-box center. Defaults false.

-----------------------------------------

ws    : worldSpace      [boolean]
    If set to true, the xform manip is always in world space. If false, the manip is in object space. (Note: when multiple objects are selected the manip is always in world space, no matter what this is set to)

    """

def showMetadata(q=1,a=1,dt="string",i=1,ia=1,las=1,lm=1,lvm=1,lvs=1,mb="string",m="string",off=1,r="[float, float]",rs="float",s="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/showMetadata.html



-----------------------------------------

showMetadata is undoable, queryable, and NOT editable.

This command is used to show metadata values which is in the specified
channels "vertex", "edge", "face", and "vertexFace" in the viewport. You can
view the data by three ways:

  1. "color": draw color on the components. 
  2. "ray": draw a ray on the components. 
  3. "string": draw 2d strings on the components. 

For example, if the metadata of "shape.vtx[1]" is (1, 0, 0), you can turn on
the visualization with all three modes. On "color" mode, you can see a red
vertex which is on the position of "shape.vtx[1]". On "ray" mode, you can see
a ray with the direction (1, 0, 0). On "string" mode, you can see strings "1 0
0" below the vertex in the viewport.

To use "color" or "ray" mode, you should make the member of the data structure
with three or less items, such as float[3]. The three items are mapped to
"RGB" as a color, or "XYZ" as a vector. The structure with two items works
similarly. The only difference is that the third value will always be zero.
However, if the structure has only one item, the value is mapped to all three
variables. That means if the structure is "int" and its value is 1, the color
will be white(1, 1, 1) and the vector will be (1, 1, 1).

You can get the current status of the flags on the query mode (using
"-query"). But you can query only the status of one flag in a single command
and you cannot set values on the query mode.

You can use the command on some specified objects, or run it with no arguments
to make changes on all objects in the scene. The object must be a mesh shape.
Components are not allowed as the command arguments.


-----------------------------------------


Return Value:

string  result of the operation or the queried status    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : auto            [boolean] ['query']
    Similar to the flag "-range", but uses the min/max value from the metadata in the same stream and member instead of the specified input value. In query mode, you can use the flag to query if "auto" is on.

-----------------------------------------

dt    : dataType        [string] ['query']
    In create mode, when used with the flags "stream" and "member", specify a member to show. If the flag "off" is used, specify the member to turn off. In query mode, when used with the flags "stream" and "member", query the visualization state of the specified member. Only one member of each shape can be visualized at a time.  In query mode, this flag can accept a value.

-----------------------------------------

i     : interpolation   [boolean] ['query']
    In create mode, enable/disable interpolation for "color" method. When interpolation is on, the components will be displayed in the interpolated color, which is computed by averaging their metadata values. In query mode, query the current state of interpolation flag of the selected objects.

-----------------------------------------

ia    : isActivated     [boolean] ['query']
    Used to check if the given stream is activated. If some shapes are selected, query their states. If no shape is selected, query the states of all shapes in the scene.

-----------------------------------------

las   : listAllStreams  [boolean] ['query']
    Used with object names to list all streams of the specified objects. no matter if they are visible in the viewport. Or you can use the flag individually to list all streams in the scene. Due to the fact that different objects may have the same stream name, the returned list will merge the duplicated stream names automatically.

-----------------------------------------

lm    : listMembers     [boolean] ['query']
    Used with the flag 'stream' to get the member list in the specified stream.

-----------------------------------------

lvm   : listValidMethods [boolean] ['query']
    List the valid visual methods that can be set for the current stream and member. Some data type cannot be displayed by some methods. For example, if the data type is "string", it cannot be displayed by "color" or by "ray". In other words, only the method "string" will be returned when you list the methods.

-----------------------------------------

lvs   : listVisibleStreams [boolean] ['query']
    Used with object names to list the name of the current visible streams of the specified object. Or you can use the flag with no object name to list all visible streams in the scene.

-----------------------------------------

mb    : member          [string] ['query']
    In create mode, when used with the flags "stream" and "dataType", specify a member to show. If the flag "off" is on, specify the member to turn off. In query mode, when used with the flags "stream" and "dataType", query the visualization state of the specified member. Only one member of each shape can be visualized at a time.  In query mode, this flag can accept a value.

-----------------------------------------

m     : method          [string] ['query']
    Determine the method of visualization: "color" convert metadata to a color value and draw the components with the color "ray" convert metadata to a vector and draw this vector line which starts from the center of the component "string" display the metadata through 2d string beside the component in the viewport The argument must be a string and must be one of the three words. The default method is "color". If the data type is string, you can only show it with "string" method. In query mode, you can use the flag with no arguments to query the method of a specified stream and member.

-----------------------------------------

      : off             [boolean] ['query']
    In create mode, turn off the member which is specified by the flags "stream", "member" and "dataType".

-----------------------------------------

r     : range           [[float, float]] ['query']
    Specify the range of data to use. The value which is out of the range will be clamped to the min/max value. If the method of visualization is "color", the range will be mapped to the color. That means the min value will be displayed in black while the max value will be in white. In query mode, you can use the flag individually to query the current range.

-----------------------------------------

rs    : rayScale        [float] ['query']
    Specify the scale of the ray to display it with a proper length.

-----------------------------------------

s     : stream          [string]
    In create mode, when used with the flags "member" and "dataType", specify a member to show. If the flag "off" is used, specify the member to turn off. In query mode, when used with the flags "member" and "dataType", query the visualization state of the specified member. When used with the flag "listMembers", query the members in the specified stream. Only one member of each shape can be visualized at a time.  In query mode, this flag can accept a value.

    """

def transferAttributes(q=1,e=1,af=1,ar=1,bf=1,clb="uint",dt=1,ex="string",fuv="uint",foc=1,g="string",gi=1,ignoreSelected=1,ihs=1,mch="uint",n="string",par=1,pr=1,rm=1,spa="uint",sm="uint",ssx="float",ssy="float",ssz="float",scs="string",suv="string",sus="string",sp=1,tcs="string",tuv="string",tus="string",col="uint",nml="uint",pos="uint",uvs="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/transferAttributes.html



-----------------------------------------

transferAttributes is undoable, queryable, and editable.

Samples the attributes of a source surface (first argument) and transfers them
onto a target surface (second argument).


-----------------------------------------


Return Value:

string  The node name.    
  
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

clb   : colorBorders    [uint] ['edit']
    Controls whether color borders are preserved when transferring color data. If this is non-zero, any color borders will be mapped onto the nearest edge on the target geometry. 0 means any color borders will be smoothly blended onto the vertices of the target geometry.

-----------------------------------------

dt    : deformerTools   [boolean] ['query']
    Returns the name of the deformer tool objects (if any) as string string ...

-----------------------------------------

ex    : exclusive       [string] ['query']
    Puts the deformation set in a deform partition.

-----------------------------------------

fuv   : flipUVs         [uint] ['edit']
    Controls how sampled UV data is flipped before being transferred to the target. 0 means no flipping; 1 means UV data is flipped in the U direction; 2 means UV data is flipped in the V direction; and 3 means it is flipped in both directions. In conjunction with mirroring, this allows the creation of symmetric UV mappings (e.g. the left hand side of the character on one side of the UV map, the right hand side on the other).

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

mch   : matchChoice     [uint] ['edit']
    When using topological component matching, selects between possible matches. If the meshes involved in the transfer operation have symmetries in their topologies, there may be more than one possible topological match. Maya scores the possible matches (by comparing the shapes of the meshes) and assigns them an index, starting at zero. Match zero, the default, is considered the best, but in the event that Maya chooses the wrong one, changing this value will allow the user to explore the other matches.

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

spa   : sampleSpace     [uint] ['edit']
    Selects which space the attribute transfer is performed in. 0 is world space, 1 is model space, 4 is component-based, 5 is topology-based. The default is world space.

-----------------------------------------

sm    : searchMethod    [uint] ['edit']
    Specifies which search method to use when correlating points. 0 is closest along normal, 3 is closest to point. The default is closest to point.

-----------------------------------------

ssx   : searchScaleX    [float] ['edit']
    Specifies an optional scale that should be applied to the x-axis of the target model before transferring data. A value of 1.0 (the default) means no scaling; a value of -1.0 would indicate mirroring along the x-axis.

-----------------------------------------

ssy   : searchScaleY    [float] ['edit']
    Specifies an optional scale that should be applied to the y-axis of the target model before transferring data. A value of 1.0 (the default) means no scaling; a value of -1.0 would indicate mirroring along the y-axis.

-----------------------------------------

ssz   : searchScaleZ    [float] ['edit']
    Specifies an optional scale that should be applied to the z-axis of the target model before transferring data. A value of 1.0 (the default) means no scaling; a value of -1.0 would indicate mirroring along the z-axis.

-----------------------------------------

scs   : sourceColorSet  [string] []
    Specifies the name of a single color set on the source surface(s) that should be transferred to the target. This value is only used when the operation is configured to transfer a single color set (see the transferColors flag).

-----------------------------------------

suv   : sourceUvSet     [string] []
    Specifies the name of a single UV set on the source surface(s) that should be transferred to the target. This value is only used when the operation is configured to transfer a single UV set (see the transferUVs flag).

-----------------------------------------

sus   : sourceUvSpace   [string] []
    Specifies the name of the UV set on the source surface(s) that should be used as the transfer space. This value is only used when the operation is configured to transfer attributes in UV space.

-----------------------------------------

sp    : split           [boolean] ['edit']
    Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).

-----------------------------------------

tcs   : targetColorSet  [string] []
    Specifies the name of a single color set on the target surface that should be receive the sampled color data. This value is only used when the operation is configured to transfer a single color set (see the transferColors flag).

-----------------------------------------

tuv   : targetUvSet     [string] []
    Specifies the name of a single UV set on the target surface that should be receive the sampled UV data. This value is only used when the operation is configured to transfer a single UV set (see the transferUVs flag).

-----------------------------------------

tus   : targetUvSpace   [string] []
    Specifies the name of the UV set on the target surface( that should be used as the transfer space. This value is only used when the operation is configured to transfer attributes in UV space.

-----------------------------------------

col   : transferColors  [uint] ['edit']
    Controls color set transfer. 0 means no color sets are transferred, 1 means that a single color set (specified by sourceColorSet and targetColorSet) is transferred, and 2 means that all color sets are transferred.

-----------------------------------------

nml   : transferNormals [uint] ['edit']
    A non-zero value indicates vertex normals should be sampled and written into user normals on the target surface.

-----------------------------------------

pos   : transferPositions [uint] ['edit']
    A non-zero value indicates vertex position should be sampled, causing the target surface to "wrap" to the source surface(s).

-----------------------------------------

uvs   : transferUVs     [uint]
    Controls UV set transfer. 0 means no UV sets are transferred, 1 means that a single UV set (specified by sourceUVSet and targetUVSet) is transferred, and 2 means that all UV sets are transferred.

    """

def transferShadingSets(q=1,e=1,spa="uint",sm="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/transferShadingSets.html



-----------------------------------------

transferShadingSets is undoable, queryable, and editable.

Command to transfer shading set assignments between meshes. The last mesh in
the list receives the shading assignments from the other meshes.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

spa   : sampleSpace     [uint] ['query', 'edit']
    Selects which space the attribute transfer is performed in. 0 is world space, 1 is model space. The default is world space.

-----------------------------------------

sm    : searchMethod    [uint]
    Specifies which search method to use when correlating points. 0 is closest along normal, 3 is closest to point. The default is closest to point.

    """

def unfold(applyToShell=1,aw="float",gb="float",gmb="float",i="int",oa="int",ps=1,pub=1,s="float",ss="float",us=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/unfold.html



-----------------------------------------

unfold is undoable, NOT queryable, and NOT editable.

None


-----------------------------------------


Return Value:

int  the number of relaxation iterations carried out


-----------------------------------------


Flags:

-----------------------------------------

applyToShell : applyToShell    [boolean] []
    Specifies that the selected components should be only work on shells that have something have been selected or pinned.

-----------------------------------------

aw    : areaWeight      [float] []
    Surface driven importance. 0 treat all faces equal. 1 gives more importance to large ones.

-----------------------------------------

gb    : globalBlend     [float] []
    This allows the user to blend between a local optimization method (globalBlend = 0.0) and a global optimization method (globalBlend = 1.0). The local optimization method looks at the ratio between the triangles on the object and the triangles in UV space. It has a side affect that it can sometimes introduce tapering problems. The global optimization is much slower, but takes into consideration the entire object when optimizing uv placement.

-----------------------------------------

gmb   : globalMethodBlend [float] []
    The global optimization method uses two functions to compute a minimization. The first function controls edge stretch by using edges lengths between xyz and uv. The second function penalizes the first function by preventing configurations where triangles would overlap. For every surface there is a mix between these two functions that will give the appropriate response. Values closer to 1.0 give more weight to the edge length function. Values closer to 0.0 give more weight to surface area. The default value of '0.5' is a even mix between these two values.

-----------------------------------------

i     : iterations      [int] []
    Maximum number of iterations for each connected UV piece.

-----------------------------------------

oa    : optimizeAxis    [int] []
    Degree of freedom for optimization 0=Optimize freely, 1=Move vertically only, 2=Move horzontally only

-----------------------------------------

ps    : pinSelected     [boolean] []
    Specifies that the selected components should be pinned instead the unselected components.

-----------------------------------------

pub   : pinUvBorder     [boolean] []
    Specifies that the UV border should be pinned when doing the solve. By default only unselected components are pinned.

-----------------------------------------

s     : scale           [float] []
    Ratio between 2d and 3d space.

-----------------------------------------

ss    : stoppingThreshold [float] []
    Minimum distorsion improvement between two steps in %.

-----------------------------------------

us    : useScale        [boolean]
    Adjust the scale or not.

    """

def untangleUV(mb="string",mri="int",pb=1,ps=1,pu=1,r="string",rt="float",sd="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/untangleUV.html



-----------------------------------------

untangleUV is undoable, NOT queryable, and NOT editable.

This command will aid in the creation of non-overlapping regions (i.e.
polygons) in texture space by untangling texture UVs. This is done in two
stages:  
1) Use this command to map the UV border determined by the current selection
or passed component into a shape that is more suitable for subsequent
relaxation.  
2) Relax all the internal texture UVs by performing a length minimization
algorithm on all edges in texture space.


-----------------------------------------


Return Value:

int  the number of relaxation iterations carried out


-----------------------------------------


Flags:

-----------------------------------------

mb    : mapBorder       [string] []
    Map the border containing the selected UV into a variety of shapes that may be more amenable to UV relaxation operations. There are various types of mapping available. All the resulting mappings are fit inside the unit square.      Valid values for the STRING are:   circular \- a circular mapping with picked UV closest to (0,0)   square \- map to unit square with picked UV at (0,0)   shape \- a mapping which attempts to reflect the actual shape of the object where the picked UV is placed on the line from (0,0) -> (0.5,0.5)   shape_circular \- shape mapping which will interpolate to a circular mapping just enough to prevent self-intersections of the mapped border   shape_square \- shape mapping which will interpolate to a square mapping just enough to prevent self-intersections of the mapped border

-----------------------------------------

mri   : maxRelaxIterations [int] []
    The relaxation process is an iterative algorithm. Using this flag will put an upper limit on the number of iterations that will be performed.

-----------------------------------------

pb    : pinBorder       [boolean] []
    If this is true, then the relevant texture borders are pinned in place during any relaxation

-----------------------------------------

ps    : pinSelected     [boolean] []
    If this is true, then then any selected UVs are pinned in place during any relaxation

-----------------------------------------

pu    : pinUnselected   [boolean] []
    If this is true, then all unselected UVs in each mesh are pinned in place during any relaxation

-----------------------------------------

r     : relax           [string] []
    Relax all UVs in the shell of the selected UV's. The relaxation is done by simulating a spring system where each UV edge is treated as a spring. There are a number of different methods characterized by the way the UV edges are weighted in the spring system. These weightings are determined by STRING. Valid values for STRING are:   uniform \- every edge is weighted the same. This is the fastest method.   inverse_length \- every edge weight is inversely proportional to it's world space length.   inverse_sqrt_length \- every edge weight is inversely proportional the the square root of it's world space length.   harmonic \- this weighting can yield near optimal results in matching the UV's with the geometry, but can also take a long time.

-----------------------------------------

rt    : relaxTolerance  [float] []
    This sets the tolerance which is used to determine when the relaxation process can stop. Smaller tolerances yield better results but can take much longer.

-----------------------------------------

sd    : shapeDetail     [float]
    If the mapBorder flag is set to circular or square, then this flag will control how much of the border's corresponding surface shape should be retained in the final mapped border.

    """

def uvSnapshot(aa=1,b="int",euv=1,ff="string",g="int",n="string",o=1,r="int",umx="float",umn="float",uvs="string",vmx="float",vmn="float",xr="int",yr="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/uvSnapshot.html



-----------------------------------------

uvSnapshot is NOT undoable, NOT queryable, and NOT editable.

Builds an image containg the UVs of the selected objects.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

aa    : antiAliased     [boolean] []
    When this flag is set, lines are antialiased.

-----------------------------------------

b     : blueColor       [int] []
    Blue component of line drawing. Default is 255.

-----------------------------------------

euv   : entireUVRange   [boolean] []
    When this flag is set, the generated image will contain the entire uv range. Default is UV in 0-1 range.

-----------------------------------------

ff    : fileFormat      [string] []
    Output file format. Any of those keyword: "iff", "sgi", "pic", "tif", "als", "gif", "rla", "jpg" Default is iff.

-----------------------------------------

g     : greenColor      [int] []
    Green component of line drawing. Default is 255.

-----------------------------------------

n     : name            [string] []
    Name of the file to be created.

-----------------------------------------

o     : overwrite       [boolean] []
    When this flag is set, existing file can be ovewritten.

-----------------------------------------

r     : redColor        [int] []
    Red component of line drawing. Default is 255.

-----------------------------------------

umx   : uMax            [float] []
    Optional User Specified Max value for U. Default value is 1. This will take precedence over the "entire range" -euv flag.

-----------------------------------------

umn   : uMin            [float] []
    Optional User Specified Min value for U. Default value is 0. This will take precedence over the "entire range" -euv flag.

-----------------------------------------

uvs   : uvSetName       [string] []
    Name of the uv set to use. Default is the current one.

-----------------------------------------

vmx   : vMax            [float] []
    Optional User Specified Max value for V. Default value is 1. This will take precedence over the "entire range" -euv flag.

-----------------------------------------

vmn   : vMin            [float] []
    Optional User Specified Min value for V. Default value is 0. This will take precedence over the "entire range" -euv flag.

-----------------------------------------

xr    : xResolution     [int] []
    Horizontal size of the image. Default is 512.

-----------------------------------------

yr    : yResolution     [int]
    Vertical size of the image. Default is 512.

    """

def alignSurface(q=1,e=1,cch=1,cc=1,cs1="float",cs2="float",du=1,jnp="float",nds="int",pc=1,pct="int",rv1=1,rv2=1,sw1=1,sw2=1,tc=1,tct="int",ts1="float",ts2="float",tw=1,at=1,ch=1,kmk=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/alignSurface.html



-----------------------------------------

alignSurface is undoable, queryable, and editable.

The surface align command is used to align surfaces in maya. The main
alignment options are positional, tangent and curvature continuity. Curvature
continuity implies tangent continuity.

NOTE: this tool is based on Studio's align tool.

Positional continuity means the surfaces (move) or the ends of the surfaces
(modify) are changed.

Tangent continuity means one of the surfaces is modified to be tangent at the
points where they meet.

Curvature continuity means one of the surfaces is modified to be curvature
continuous as well as tangent.

The default behaviour, when no surfaces or flags are passed, is to only do
positional and tangent continuity on the active list with the end of the first
surface and the start of the other surface used for alignment.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cc    : curvatureContinuity [boolean] ['query', 'edit']
    Curvature continuity is on if true and off otherwise.   Default: false

-----------------------------------------

cs1   : curvatureScale1 [float] ['query', 'edit']
    Curvature scale applied to curvature of first surface for curvature continuity.   Default: 0.0

-----------------------------------------

cs2   : curvatureScale2 [float] ['query', 'edit']
    Curvature scale applied to curvature of second surface for curvature continuity.   Default: 0.0

-----------------------------------------

du    : directionU      [boolean] ['query', 'edit']
    If true use U direction of surface and V direction otherwise.   Default: true

-----------------------------------------

jnp   : joinParameter   [float] ['query', 'edit']
    Parameter on reference surface where modified surface is to be aligned to.   Default: 123456.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pc    : positionalContinuity [boolean] ['query', 'edit']
    Positional continuity is on if true and off otherwise.   Default: true

-----------------------------------------

pct   : positionalContinuityType [int] ['query', 'edit']
    Positional continuity type legal values: 1 - move first surface, 2 - move second surface, 3 - move both surfaces, 4 - modify first surface, 5 - modify second surface, 6 - modify both surfaces   Default: 1

-----------------------------------------

rv1   : reverse1        [boolean] ['query', 'edit']
    If true, reverse the direction (specified by directionU) of the first input surface before doing align. Otherwise, do nothing to the first input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

rv2   : reverse2        [boolean] ['query', 'edit']
    If true, reverse the direction (specified by directionU) of the second input surface before doing align. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

sw1   : swap1           [boolean] ['query', 'edit']
    If true, swap the UV directions of the first input surface before doing align. Otherwise, do nothing to the first input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

sw2   : swap2           [boolean] ['query', 'edit']
    If true, swap the UV directions of the second input surface before doing align. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

tc    : tangentContinuity [boolean] ['query', 'edit']
    Tangent continuity is on if true and off otherwise.   Default: true

-----------------------------------------

tct   : tangentContinuityType [int] ['query', 'edit']
    Tangent continuity type legal values: 1 - do tangent continuity on first surface, 2 - do tangent continuity on second surface   Default: 1

-----------------------------------------

ts1   : tangentScale1   [float] ['query', 'edit']
    Tangent scale applied to tangent of first surface for tangent continuity.   Default: 1.0

-----------------------------------------

ts2   : tangentScale2   [float] ['query', 'edit']
    Tangent scale applied to tangent of second surface for tangent continuity.   Default: 1.0

-----------------------------------------

tw    : twist           [boolean] ['query', 'edit']
    If true, reverse the second surface in the opposite direction (specified by directionU) before doing align. This will avoid twists in the aligned surfaces. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

at    : attach          [boolean] []
    Should surfaces be attached after alignment?

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

kmk   : keepMultipleKnots [boolean] []
    Should multiple knots be kept?

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def angleBetween(cch=1,ch=1,er=1,nds="int",v1="[linear, linear, linear]",v1x="linear",v1y="linear",v1z="linear",v2="[linear, linear, linear]",v2x="linear",v2y="linear",v2z="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/angleBetween.html



-----------------------------------------

angleBetween is undoable, NOT queryable, and NOT editable.

Returns the axis and angle required to rotate one vector onto another. If the
construction history (ch) flag is ON, then the name of the new dependency node
is returned.


-----------------------------------------


Return Value:

float[]  3 Euler angles or axis and angle    
string  When constructionHistory flag is used.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] []
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

er    : euler           [boolean] []
    return the rotation as 3 Euler angles instead of axis + angle

-----------------------------------------

nds   : nodeState       [int] []
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

v1    : vector1         [[linear, linear, linear]] []
    vector from which to compute the rotation

-----------------------------------------

v1x   : vector1X        [linear] []
    X coordinate of the vector from which to compute the rotation

-----------------------------------------

v1y   : vector1Y        [linear] []
    Y coordinate of the vector from which to compute the rotation

-----------------------------------------

v1z   : vector1Z        [linear] []
    Z coordinate of the vector from which to compute the rotation

-----------------------------------------

v2    : vector2         [[linear, linear, linear]] []
    vector to which to compute the rotation

-----------------------------------------

v2x   : vector2X        [linear] []
    X coordinate of the vector to which to compute the rotation

-----------------------------------------

v2y   : vector2Y        [linear] []
    Y coordinate of the vector to which to compute the rotation

-----------------------------------------

v2z   : vector2Z        [linear]
    Z coordinate of the vector to which to compute the rotation

    """

def arubaNurbsToPoly(q=1,e=1,cch=1,ch=1,ls=1,n="string",nds="int",o=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/arubaNurbsToPoly.html



-----------------------------------------

arubaNurbsToPoly is undoable, queryable, and editable.

This command tesselates a NURBS surface and produces a polygonal surface. The
name of the new polygonal surface is returned. If construction history is ON,
then the name of the new dependency node is returned as well.


-----------------------------------------


Return Value:

string[]  The polygon and optionally the dependency node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

ls    : localSpace      [boolean] []
    Tesselate in local space

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

ws    : worldSpace      [boolean]
    Tesselate in world space

    """

def attachSurface(q=1,e=1,bb="float",bki=1,cch=1,du=1,kmk=1,m="int",nds="int",p="float",rv1=1,rv2=1,sw1=1,sw2=1,tw=1,ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/attachSurface.html



-----------------------------------------

attachSurface is undoable, queryable, and editable.

This attach command is used to attach surfaces. Once the surfaces are
attached, there will be multiple knots at the joined point(s). These can be
kept or removed if the user wishes.

The end of the first surface is attached to the start of the second surface in
the specified direction.

Note: if the command is done with Keep Original off there will be an extra
surface in the model (the second surface). The command does not delete it. The
first surface is replaced by the attached surface.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bb    : blendBias       [float] ['query', 'edit']
    Skew the result toward the first or the second curve depending on the blend factory being smaller or larger than 0.5.   Default: 0.5

-----------------------------------------

bki   : blendKnotInsertion [boolean] ['query', 'edit']
    If set to true, insert a knot in one of the original curves (relative position given by the parameter attribute below) in order to produce a slightly different effect.   Default: false

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

du    : directionU      [boolean] ['query', 'edit']
    If true attach in U direction of surface and V direction otherwise.   Default: true

-----------------------------------------

kmk   : keepMultipleKnots [boolean] ['query', 'edit']
    If true, keep multiple knots at the join parameter. Otherwise remove them.   Default: true

-----------------------------------------

m     : method          [int] ['query', 'edit']
    Attach method (connect-0, blend-1)   Default: 0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    The parameter value for the positioning of the newly inserted knot.   Default: 0.1

-----------------------------------------

rv1   : reverse1        [boolean] ['query', 'edit']
    If true, reverse the direction (specified by directionU) of the first input surface before doing attach. Otherwise, do nothing to the first input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

rv2   : reverse2        [boolean] ['query', 'edit']
    If true, reverse the direction (specified by directionU) of the second input surface before doing attach. Otherwise, do nothing to the second input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

sw1   : swap1           [boolean] ['query', 'edit']
    If true, swap the UV directions of the first input surface before doing attach. Otherwise, do nothing to the first input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

sw2   : swap2           [boolean] ['query', 'edit']
    If true, swap the UV directions of the second input surface before doing attach. Otherwise, do nothing to the second input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

tw    : twist           [boolean] ['query', 'edit']
    If true, reverse the second surface in the opposite direction (specified by directionU) before doing attach. This will avoid twists in the attached surfaces. Otherwise, do nothing to the second input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def bevel(q=1,e=1,bst="int",cch=1,ct="int",d="linear",ed="linear",nds="int",tol="linear",w="linear",ch=1,js=1,n="string",ns="int",o=1,po="int",rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bevel.html



-----------------------------------------

bevel is undoable, queryable, and editable.

The bevel command creates a new bevel surface for the specified curve. The
curve can be any nurbs curves.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bst   : bevelShapeType  [int] ['query', 'edit']
    Shape type: 1 - straight cut, 2 - curve out, 3 - curve in   Default: 1

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ct    : cornerType      [int] ['query', 'edit']
    Corner type: 1 - linear, 2 - circular   Default: 2

-----------------------------------------

d     : depth           [linear] ['query', 'edit']
    The depth for bevel   Default: 0.5

-----------------------------------------

ed    : extrudeDepth    [linear] ['query', 'edit']
    The extrude depth for bevel   Default: 1.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance for bevel offsets   Default: 0.01

-----------------------------------------

w     : width           [linear] ['query', 'edit']
    The width for bevel   Default: 0.5

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

js    : joinSurfaces    [boolean] ['query', 'edit']
    Attach bevelled surfaces into one surface for each input curve.   Default:true

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

ns    : numberOfSides   [int] ['query', 'edit']
    How to apply the bevel.    * 1 - no bevels   * 2 - bevel at start only   * 3 - bevel at end only   * 4 - bevel at start and end     Default: 4

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def bevelPlus(q=1,e=1,bin=1,cap="int",ch=1,innerStyle="int",js=1,n="string",no=1,ns="int",os="int",po="int",rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bevelPlus.html



-----------------------------------------

bevelPlus is undoable, queryable, and editable.

The bevelPlus command creates a new bevel surface for the specified curves
using a given style curve. The first curve should be the "outside" curve, and
the (optional) rest of them should be inside of the first one. For predictable
results, the curves should be planar and all in the same plane.


-----------------------------------------


Return Value:

string[]  Object name(s) and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bin   : bevelInside     [boolean] ['query', 'edit']
    If true, ensure surface always remains within the original profile curve   Default: false

-----------------------------------------

cap   : capSides        [int] ['query']
    How to cap the bevel.    * 1 - no caps   * 2 - cap at start only   * 3 - cap at end only   * 4 - cap at start and end     Default:4

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

innerStyle : innerStyle      [int] ['query', 'edit']
    Similar to outerStyle, this style is applied to all but the first (outer) curve specified.

-----------------------------------------

js    : joinSurfaces    [boolean] ['query', 'edit']
    Attach bevelled surfaces into one surface for each input curve.   Default:true

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

no    : normalsOutwards [boolean] ['query', 'edit']
    If enabled, the normals point outwards on the resulting NURBS or poly surface.

-----------------------------------------

ns    : numberOfSides   [int] ['query', 'edit']
    How to apply the bevel.    * 1 - no bevels   * 2 - bevel at start only   * 3 - bevel at end only   * 4 - bevel at start and end     Default: 4

-----------------------------------------

os    : outerStyle      [int] ['query', 'edit']
    Choose a style to use for the bevel of the first (outer) curve. There are 15 predefined styles (values 0 to 14 can be used to select them). For those experienced with MEL, you can, after the fact, specify a custom curve and use it for the style curve. See the documentation for styleCurve node to see what requirements a style curve must satisfy.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def bezierAnchorPreset(p="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bezierAnchorPreset.html



-----------------------------------------

bezierAnchorPreset is undoable, NOT queryable, and NOT editable.

This command provides a queryable interface for Bezier curve shapes.


-----------------------------------------


Return Value:

int  (number of modified anchors)


-----------------------------------------


Flags:

-----------------------------------------

p     : preset          [int]
    Selects a preset to apply to selected Bezier anchors. Valid arguments are: 0: Bezier 1: Bezier Corner 2: Corner

    """

def bezierAnchorState(ev=1,sm=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bezierAnchorState.html



-----------------------------------------

bezierAnchorState is undoable, NOT queryable, and NOT editable.

The bezierAnchorState command provides an easy interface to modify anchor
states:

\- Smooth/Broken anchor tangents \- Even/Uneven weighted anchor tangents


-----------------------------------------


Return Value:

int  (number of modified anchors)


-----------------------------------------


Flags:

-----------------------------------------

ev    : even            [boolean] []
    Sets selected anchors (or attached tangent handles) to even weighting when true, uneven otherwise.

-----------------------------------------

sm    : smooth          [boolean]
    Sets selected anchors (or attached tangent handles) to smooth when true, broken otherwise.

    """

def bezierCurveToNurbs():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bezierCurveToNurbs.html



-----------------------------------------

bezierCurveToNurbs is undoable, NOT queryable, and NOT editable.

The bezierCurveToNurbs command attempts to convert an existing NURBS curve to
a Bezier curve.


-----------------------------------------


Return Value:

string[]  (object name and node name)
    """

def bezierInfo(afc="int",cfa="int",ias=1,its=1,oas=1,ots=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/bezierInfo.html



-----------------------------------------

bezierInfo is undoable, NOT queryable, and NOT editable.

This command provides a queryable interface for Bezier curve shapes.


-----------------------------------------


Return Value:

int  Queried value


-----------------------------------------


Flags:

-----------------------------------------

afc   : anchorFromCV    [int] []
    Returns the Bezier anchor index from a given CV index

-----------------------------------------

cfa   : cvFromAnchor    [int] []
    Returns the CV index for a given Bezier anchor index

-----------------------------------------

ias   : isAnchorSelected [boolean] []
    Returns 1 if an anchor CV is currently selected. 0, otherwise.

-----------------------------------------

its   : isTangentSelected [boolean] []
    Returns 1 if a tangent CV is currently selected. 0, otherwise.

-----------------------------------------

oas   : onlyAnchorsSelected [boolean] []
    Returns 1 if the only CV components selected are anchor CVs. 0, otherwise.

-----------------------------------------

ots   : onlyTangentsSelected [boolean]
    Returns 1 if the only CV components selected are tangent CVs. 0, otherwise.

    """

def blend2(q=1,e=1,aa=1,an=1,cch=1,fln=1,frn=1,la="float",le="float",ls="float",mk=1,nds="int",pt="float",rvl=1,rvr=1,ra="float",re="float",rs="float",tt="float",ch=1,cfr="int",n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/blend2.html



-----------------------------------------

blend2 is undoable, queryable, and editable.

This command creates a surface by blending between given curves. This is an
enhancement (more user control) compared to blend which is now obsolete.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aa    : autoAnchor      [boolean] ['query', 'edit']
    If true and both paths are closed, automatically determine the value on the right rail so that they match   Default: true

-----------------------------------------

an    : autoNormal      [boolean] ['query', 'edit']
    If true, the direction of each starting tangent is computed based on given geometry.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

fln   : flipLeftNormal  [boolean] ['query', 'edit']
    If true, flip the starting tangent off the left boundary.   Default: false

-----------------------------------------

frn   : flipRightNormal [boolean] ['query', 'edit']
    If true, flip the starting tangent off the right boundary.   Default: false

-----------------------------------------

la    : leftAnchor      [float] ['query', 'edit']
    The reference parameter on the left boundary where the blend surface starts in the case of the closed rail.   Default: 0.0

-----------------------------------------

le    : leftEnd         [float] ['query', 'edit']
    The reference parameter on the left boundary where the blend surface ends.   Default: 1.0

-----------------------------------------

ls    : leftStart       [float] ['query', 'edit']
    The reference parameter on the left boundary where the blend surface starts.   Default: 0.0

-----------------------------------------

mk    : multipleKnots   [boolean] ['query', 'edit']
    If true, use the new blend which produces fully multiple interior knots   Default: true

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pt    : positionTolerance [float] ['query', 'edit']
    The positional C(0) tolerance of the blend surface to the adjacent surfaces.   Default: 0.1

-----------------------------------------

rvl   : reverseLeft     [boolean] ['query', 'edit']
    If true, reverse the direction off the left boundary. autoDirection must be false for this value to be considered.   Default: false

-----------------------------------------

rvr   : reverseRight    [boolean] ['query', 'edit']
    If true, reverse the direction of the right boundary. autoDirection must be false for this value to be considered.   Default: false

-----------------------------------------

ra    : rightAnchor     [float] ['query', 'edit']
    The reference parameter on the right boundary where the blend surface starts in the case of the closed rail.   Default: 0.0

-----------------------------------------

re    : rightEnd        [float] ['query', 'edit']
    The reference parameter on the right boundary where the blend surface ends.   Default: 1.0

-----------------------------------------

rs    : rightStart      [float] ['query', 'edit']
    The reference parameter on the right boundary where the blend surface starts.   Default: 0.0

-----------------------------------------

tt    : tangentTolerance [float] ['query', 'edit']
    The tangent G(1) continuity tolerance of the blend surface to the adjacent surfaces.   Default: 0.1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cfr   : crvsInFirstRail [int] ['query', 'edit']
    Number of curves in the first rail of the blend.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def boundary(q=1,e=1,cch=1,ep=1,ept="linear",nds="int",order=1,ch=1,n="string",o=1,po="int",rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/boundary.html



-----------------------------------------

boundary is undoable, queryable, and editable.

This command produces a boundary surface given 3 or 4 curves. This resulting
boundary surface passes through two of the given curves in one direction,
while in the other direction the shape is defined by the remaining curve(s).
If the "endPoint" option is on, then the curve endpoints must touch before a
surface will be created. This is the usual situation where a boundary surface
is useful.

Note that there is no tangent continuity option with this command. Unless all
the curve end points are touching, the resulting surface will not pass through
all curves. Instead, use the birail command.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ep    : endPoint        [boolean] ['query', 'edit']
    True means the curve ends must touch before a surface will be created.   Default: false

-----------------------------------------

ept   : endPointTolerance [linear] ['query', 'edit']
    Tolerance for end points, only used if endPoint attribute is true.   Default: 0.1

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

order : order           [boolean] ['query', 'edit']
    True if the curve order is important.   Default: true

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def canCreateManip():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/canCreateManip.html



-----------------------------------------

canCreateManip is undoable, NOT queryable, and NOT editable.

This command returns true if there can be a manipulator made for the specified
selection, false otherwise.


-----------------------------------------


Return Value:

boolean  Command result
    """

def circularFillet(q=1,e=1,cch=1,nds="int",pt="float",pr="linear",sr="linear",tt="float",ch=1,cos=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/circularFillet.html



-----------------------------------------

circularFillet is undoable, queryable, and editable.

The cmd is used to compute the rolling ball surface fillet ( circular fillet )
between two given NURBS surfaces. To generate trim curves on the surfaces, use
-cos true.


-----------------------------------------


Return Value:

string[]  Object name, node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pt    : positionTolerance [float] ['query', 'edit']
    C(0) Tolerance For Fillet Surface   Default: 0.01

-----------------------------------------

pr    : primaryRadius   [linear] ['query', 'edit']
    primary Radius   Default: 1.0

-----------------------------------------

sr    : secondaryRadius [linear] ['query', 'edit']
    secondary Radius   Default: 1.0

-----------------------------------------

tt    : tangentTolerance [float] ['query', 'edit']
    G(1) Tolerance For Fillet Surface   Default: 0.01

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def closeSurface(q=1,e=1,bb="float",bki=1,cch=1,d="int",nds="int",p="float",ps="int",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/closeSurface.html



-----------------------------------------

closeSurface is undoable, queryable, and editable.

The closeSurface command closes a surface in the U, V, or both directions,
making it periodic. The close direction is controlled by the direction flag.
If a surface is not specified in the command, then the first selected surface
will be used.

The pathname to the newly closed surface and the name of the resulting
dependency node are returned.

This command also handles selected surface isoparms. For example, if an
isoparm is specified, surface1.u[0.33], then the surface will be closed in V,
regardless of the direction flag.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bb    : blendBias       [float] ['query', 'edit']
    Skew the result toward the first or the second surface depending on the blend value being smaller or larger than 0.5.   Default: 0.5

-----------------------------------------

bki   : blendKnotInsertion [boolean] ['query', 'edit']
    If set to true, insert a knot in one of the original surfaces (relative position given by the parameter attribute below) in order to produce a slightly different effect.   Default: false

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    The direction in which to close: 0 - U, 1 - V, 2 - Both U and V   Default: 0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    The parameter value for the positioning of the newly inserted knot.   Default: 0.1

-----------------------------------------

ps    : preserveShape   [int] ['query', 'edit']
    0 - without preserving the shape 1 - preserve shape 2 - blend   Default: 1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def cone(q=1,e=1,ax="[linear, linear, linear]",cch=1,d="int",esw="angle",hr="float",nds="int",p="[linear, linear, linear]",r="linear",s="int",nsp="int",ssw="angle",tol="linear",oib=1,ut=1,ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cone.html



-----------------------------------------

cone is undoable, queryable, and editable.

The cone command creates a new cone and/or a dependency node that creates one,
and returns their names.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    The primitive's axis

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface: 1 - linear, 3 - cubic   Default: 3

-----------------------------------------

esw   : endSweep        [angle] ['query', 'edit']
    The angle at which to end the surface of revolution. Default is 2Pi radians, or 360 degrees.   Default: 6.2831853

-----------------------------------------

hr    : heightRatio     [float] ['query', 'edit']
    Ratio of "height" to "width"   Default: 2.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    The primitive's pivot point

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    The radius of the object   Default: 1.0

-----------------------------------------

s     : sections        [int] ['query', 'edit']
    The number of sections determines the resolution of the surface in the sweep direction. Used only if useTolerance is false.   Default: 8

-----------------------------------------

nsp   : spans           [int] ['query', 'edit']
    The number of spans determines the resolution of the surface in the opposite direction.   Default: 1

-----------------------------------------

ssw   : startSweep      [angle] ['query', 'edit']
    The angle at which to start the surface of revolution   Default: 0

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to build the surface. Used only if useTolerance is true   Default: 0.01

-----------------------------------------

oib   : useOldInitBehaviour [boolean] ['query', 'edit']
    Create the cone with base on the origin as in Maya V8.0 and below Otherwise create cone centred at origin   Default: false

-----------------------------------------

ut    : useTolerance    [boolean] ['query', 'edit']
    Use the specified tolerance to determine resolution. Otherwise number of sections will be used.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def constructionHistory(q=1,tgl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/constructionHistory.html



-----------------------------------------

constructionHistory is undoable, queryable, and NOT editable.

This command turns construction history on or off.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

tgl   : toggle          [boolean]
    Turns construction history on or off.

    """

def cylinder(q=1,e=1,ax="[linear, linear, linear]",cch=1,d="int",esw="angle",hr="float",nds="int",p="[linear, linear, linear]",r="linear",s="int",nsp="int",ssw="angle",tol="linear",ut=1,ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/cylinder.html



-----------------------------------------

cylinder is undoable, queryable, and editable.

The cylinder command creates a new cylinder and/or a dependency node that
creates one, and returns their names.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    The primitive's axis

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface: 1 - linear, 3 - cubic   Default: 3

-----------------------------------------

esw   : endSweep        [angle] ['query', 'edit']
    The angle at which to end the surface of revolution. Default is 2Pi radians, or 360 degrees.   Default: 6.2831853

-----------------------------------------

hr    : heightRatio     [float] ['query', 'edit']
    Ratio of "height" to "width"   Default: 2.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    The primitive's pivot point

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    The radius of the object   Default: 1.0

-----------------------------------------

s     : sections        [int] ['query', 'edit']
    The number of sections determines the resolution of the surface in the sweep direction. Used only if useTolerance is false.   Default: 8

-----------------------------------------

nsp   : spans           [int] ['query', 'edit']
    The number of spans determines the resolution of the surface in the opposite direction.   Default: 1

-----------------------------------------

ssw   : startSweep      [angle] ['query', 'edit']
    The angle at which to start the surface of revolution   Default: 0

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to build the surface. Used only if useTolerance is true   Default: 0.01

-----------------------------------------

ut    : useTolerance    [boolean] ['query', 'edit']
    Use the specified tolerance to determine resolution. Otherwise number of sections will be used.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def detachSurface(q=1,e=1,cch=1,d="int",k=1,nds="int",p="float",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/detachSurface.html



-----------------------------------------

detachSurface is undoable, queryable, and editable.

The detachSurface command detaches a surface into pieces, given a list of
parameter values and a direction. You can also specify which pieces to keep
and which to discard using the "-k" flag. The names of the newly detached
surface(s) are returned. If history is on, the name of the resulting
dependency node is also returned.

You can only detach in either U or V (not both) with a single detachSurface
operation.

You can use this command to open a closed surface at a particular parameter
value. You would use this command with only one "-p" flag.

If you are specifying "-k" flags, then you must specify one, none or all "-k"
flags. If you are specifying all "-k" flags, there must be one more "-k" flag
than "-p" flags.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    Direction in which to detach: 0 - V direction, 1 - U direction   Default: 1

-----------------------------------------

k     : keep            [boolean] ['query', 'edit']
    Keep the detached pieces.   Default: true

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    Parameter at which to detach.   Default: 0.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def doubleProfileBirailSurface(q=1,e=1,bl="float",cch=1,nds="int",tp1=1,tp2=1,tm="int",ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/doubleProfileBirailSurface.html



-----------------------------------------

doubleProfileBirailSurface is undoable, queryable, and editable.

The arguments are 4 cuves called "profile1" "profile2" "rail1" "rail2".

This command builds a railed surface by sweeping profile "profile1" along the
two given rail curves "rail1", "rail2" until "profile2" is reached. By using
the -blend control, the railed surface creation could be biased more towards
one of the two profile curves. The curves ( both profiles and rails ) could
also be surface curves ( isoparams, curve on surfaces ). If the profile curves
are surface curves the surface constructed could be made tangent continuous to
the surfaces underlying the profiles using the flags -tp1, -tp2 respectively.
Current Limitation: Its necessary that the two profile curves intersect the
rail curves for successful surface creation.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bl    : blendFactor     [float] ['query', 'edit']
    A blend factor applied in between the two profiles. The amount of influence 'inputProfile1' has in the surface creation.   Default: 0.5

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tp1   : tangentContinuityProfile1 [boolean] ['query', 'edit']
    Need tangent continuity across the input profile at inputProfile1.   Default: false

-----------------------------------------

tp2   : tangentContinuityProfile2 [boolean] ['query', 'edit']
    Need tangent continuity across the input curve at inputProfile2.   Default: false

-----------------------------------------

tm    : transformMode   [int] ['query', 'edit']
    transform mode ( Non proportional, proportional ). Non proportional is default value.   Default: 0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def duplicateSurface(q=1,e=1,cch=1,ch=1,fcu="int",fcv="int",ffu="int",ffv="int",l=1,mi=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/duplicateSurface.html



-----------------------------------------

duplicateSurface is undoable, queryable, and editable.

The duplicateSurface command takes a surface patch (face) and and returns the
3D surface. Connected patches are returned as a single surface.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

fcu   : faceCountU      [int] ['query', 'edit']
    Number of faces in U direction   Default: 1

-----------------------------------------

fcv   : faceCountV      [int] ['query', 'edit']
    Number of faces in V direction   Default: 1

-----------------------------------------

ffu   : firstFaceU      [int] ['query', 'edit']
    First face (U direction index)   Default: 0

-----------------------------------------

ffv   : firstFaceV      [int] ['query', 'edit']
    First face (V direction index)   Default: 0

-----------------------------------------

l     : local           [boolean] []
    Copy the transform of the surface and connect to the local space version instead.

-----------------------------------------

mi    : mergeItems      [boolean] []
    Merge component results where possible. For example, instead of returning a[1] and a[2], return a[1:2].

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def extendSurface(q=1,e=1,cch=1,d="linear",ed="int",em="int",es="int",et="int",jn=1,nds="int",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/extendSurface.html



-----------------------------------------

extendSurface is undoable, queryable, and editable.

This command extends a surface or creates a new surface as an extension.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : distance        [linear] ['query', 'edit']
    The distance to extend (for by distance only)   Default: 1

-----------------------------------------

ed    : extendDirection [int] ['query', 'edit']
    Which parametric direction of the surface to extend ( 0 - U, 1 - V, 2 - both )   Default: 0

-----------------------------------------

em    : extendMethod    [int] ['query', 'edit']
    The extend method (0 - distance)   Default: 0

-----------------------------------------

es    : extendSide      [int] ['query', 'edit']
    Which end of the surface to extend ( 0 - end, 1 - start, 2 - both )   Default: 1

-----------------------------------------

et    : extensionType   [int] ['query', 'edit']
    The type of extension (0 - tangent, 2 - extrapolate)   Default: 0

-----------------------------------------

jn    : join            [boolean] ['query', 'edit']
    Join extension to original   Default: true

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def extrude(q=1,e=1,cch=1,dl="int",d="[linear, linear, linear]",dx="linear",dy="linear",dz="linear",et="int",fpt=1,l="linear",nds="int",p="[linear, linear, linear]",rsp=1,ro="angle",sc="float",scs=1,ucp="int",upn=1,ch=1,mi=1,n="string",o=1,po="int",rn=1,rb=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/extrude.html



-----------------------------------------

extrude is undoable, queryable, and editable.

This command computes a surface given a profile curve and possibly a path
curve. There are three ways to extrude a profile curve. The most basic method
is called a "distance" extrude where direction and length are specified. No
path curve is necessary in this case. The second method is called "flat"
extrude. This method sweeps the profile curve down the path curve without
changing the orientation of the profile curve. Finally, the third method is
called "tube" extrude. This method sweeps a profile curve down a path curve
while the profile curve rotates so that it maintains a relationship with the
path curve.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

dl    : degreeAlongLength [int] ['query', 'edit']
    Surface degree along the distance when a distance extrude is performed   Default: 1

-----------------------------------------

d     : direction       [[linear, linear, linear]] ['query', 'edit']
    The direction in which to extrude. Use only for distance extrudeType and useProfileNormal off

-----------------------------------------

dx    : directionX      [linear] ['query', 'edit']
    X of the direction   Default: 0

-----------------------------------------

dy    : directionY      [linear] ['query', 'edit']
    Y of the direction   Default: 1

-----------------------------------------

dz    : directionZ      [linear] ['query', 'edit']
    Z of the direction   Default: 0

-----------------------------------------

et    : extrudeType     [int] ['query', 'edit']
    The extrude type (distance-0, flat-1, or tube-2)   Default: 2

-----------------------------------------

fpt   : fixedPath       [boolean] ['query', 'edit']
    If true, the resulting surface will be placed at the path curve. Otherwise, the resulting surface will be placed at the profile curve.   Default: false

-----------------------------------------

l     : length          [linear] ['query', 'edit']
    The distance to extrude. Use only for distance extrudeType   Default: 1

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    The pivot point used for tube extrudeType

-----------------------------------------

rsp   : reverseSurfaceIfPathReversed [boolean] ['query', 'edit']
    If true, extrude type is tube (2) and path has been internally reversed then computed surface is reversed in the direction corresponding to the path.   Default: false

-----------------------------------------

ro    : rotation        [angle] ['query', 'edit']
    Amount to rotate the profile curve as it sweeps along the path curve.   Default: 0.0

-----------------------------------------

sc    : scale           [float] ['query', 'edit']
    Amount to scale the profile curve as it sweeps along the path curve.   Default: 1.0

-----------------------------------------

scs   : subCurveSubSurface [boolean] ['query', 'edit']
    If true, curve range on the path will get applied to the resulting surface instead of cut before the extrude.   Default: false

-----------------------------------------

ucp   : useComponentPivot [int] ['query', 'edit']
    Use closest endpoint of the path - 0, component pivot - 1 or the center of the bounding box of the profile - 2   Default: 0

-----------------------------------------

upn   : useProfileNormal [boolean] ['query', 'edit']
    If true, use the profile curve normal for the direction in which to extrude. Use only for distance or tube extrudeType.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

mi    : mergeItems      [boolean] []
    Merge component results where possible. For example, instead of returning a[1] and a[2], return a[1:2].

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean] []
    Force a curve range on complete input curve.

-----------------------------------------

rb    : rebuild         [boolean]
    Rebuild the input curve(s) before using them in the operation. Use nurbsCurveRebuildPref to set the parameters for the conversion.

    """

def filterExpand(ex=1,fp=1,sm="int",sma=1,smn=1,smp=1,sms=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filterExpand.html



-----------------------------------------

filterExpand is undoable, NOT queryable, and NOT editable.

Based on selected components (or components specified on the command line),
the command filters and/or expands the list given the options. Returns a
string array containing all matching selection items. Selection masks are as
follows:

Object Type | Mask  
---|---  
Handle |  0  
Nurbs Curves |  9  
Nurbs Surfaces |  10  
Nurbs Curves On Surface |  11  
Polygon |  12  
Locator XYZ |  22  
Orientation Locator |  23  
Locator UV |  24  
Control Vertices (CVs) |  28  
Edit Points |  30  
Polygon Vertices |  31  
Polygon Edges |  32  
Polygon Face |  34  
Polygon UVs |  35  
Subdivision Mesh Points |  36  
Subdivision Mesh Edges |  37  
Subdivision Mesh Faces |  38  
Curve Parameter Points |  39  
Curve Knot |  40  
Surface Parameter Points |  41  
Surface Knot |  42  
Surface Range |  43  
Trim Surface Edge |  44  
Surface Isoparms |  45  
Lattice Points |  46  
Particles |  47  
Scale Pivots |  49  
Rotate Pivots |  50  
Select Handles |  51  
Subdivision Surface |  68  
Polygon Vertex Face |  70  
NURBS Surface Face |  72  
Subdivision Mesh UVs |  73


-----------------------------------------


Return Value:

string[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

ex    : expand          [boolean] []
    Each item is a single entity if this is true. Default is true.

-----------------------------------------

fp    : fullPath        [boolean] []
    If this is true and the selection item is a DAG object, return its full selection path, instead of the name of the object only when this value is false. Default is false.

-----------------------------------------

sm    : selectionMask   [int] []
    Specify the selection mask

-----------------------------------------

sma   : symActive       [boolean] []
    If symmetry is enabled only return the components on the active symmetry side of the object. This flag has no effect if symmetry is not active.

-----------------------------------------

smn   : symNegative     [boolean] []
    If symmetry is enabled only return the components on the negative side of the object relative to the current symmetry plane. This flag has no effect if symmetry is not active.

-----------------------------------------

smp   : symPositive     [boolean] []
    If symmetry is enabled only return the components on the positive side of the object relative to the current symmetry plane. This flag has no effect if symmetry is not active.

-----------------------------------------

sms   : symSeam         [boolean]
    If symmetry is enabled only return the components that lie equally on both sides of the object relative to the current symmetry plane. This flag has no effect if symmetry is not active.

    """

def freeFormFillet(q=1,e=1,b="float",cch=1,d="float",nds="int",pt="float",tt="float",ch=1,n="string",o=1,po="int",rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/freeFormFillet.html



-----------------------------------------

freeFormFillet is undoable, queryable, and editable.

This command creates a free form surface fillet across two surface trim edges
or isoparms or curve on surface. The fillet surface creation has blend
controls in the form of bias and depth. The bias value scales the tangents at
the two ends across the two selected curves. The depth values controls the
curvature of the fillet across the two selected curves. The default values of
depth, bias are 0.5 and 0.5 respectively.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : bias            [float] ['query', 'edit']
    Bias value for fillet   Default: 0.5

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : depth           [float] ['query', 'edit']
    Depth value for fillet   Default: 0.5

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pt    : positionTolerance [float] ['query', 'edit']
    C(0) Tolerance For Filleted Surface creation   Default: 0.1

-----------------------------------------

tt    : tangentTolerance [float] ['query', 'edit']
    G(1) continuity Tolerance For Filleted Surface creation   Default: 0.1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def globalStitch(q=1,e=1,cch=1,lk=1,ms="linear",mr="float",nds="int",sam="int",sc="int",se="int",spe=1,ss="int",ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/globalStitch.html



-----------------------------------------

globalStitch is undoable, queryable, and editable.

This command computes a globalStitch of NURBS surfaces. There should be at
least one NURBS surface. The NURBS surface(s) should be untrimmed.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

lk    : lockSurface     [boolean] ['query', 'edit']
    Keep the NURBS surface at the specified multi index unchanged by the fitting.   Default: false

-----------------------------------------

ms    : maxSeparation   [linear] ['query', 'edit']
    Maximum separation that will still be stitched.   Default: 0.1

-----------------------------------------

mr    : modificationResistance [float] ['query', 'edit']
    Modification resistance weight for surface CVs.   Default: 1e-1

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

sam   : sampling        [int] ['query', 'edit']
    Sampling when stitching edges.   Default: 1

-----------------------------------------

sc    : stitchCorners   [int] ['query', 'edit']
    Stitch corners of surfaces. 0 - off 1 - closest point 2 - closest knot   Default: 1

-----------------------------------------

se    : stitchEdges     [int] ['query', 'edit']
    Stitch edges of surfaces. 0 - off 1 - closest point 2 - matching params   Default: 1

-----------------------------------------

spe   : stitchPartialEdges [boolean] ['query', 'edit']
    Toggle on (off) partial edge stitching.   Default: false

-----------------------------------------

ss    : stitchSmoothness [int] ['query', 'edit']
    Set type of smoothness of edge join. 0 - off 1 - tangent 2 - normal   Default: 0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def grid(q=1,df=1,da=1,dab=1,ddl=1,dgl=1,dol=1,dpl=1,d="uint",olp="string",plp="string",r=1,s="linear",sp="linear",st="uint",tgl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/grid.html



-----------------------------------------

grid is undoable, queryable, and NOT editable.

This command changes the size and spacing of lines on the ground plane
displayed in the perspective and orthographic views.

This command lets you reset the ground plane, change its size and grid line
spacing, grid subdivisions and display options.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

df    : default         [boolean] ['query']
    Used to specify/query default values.

-----------------------------------------

da    : displayAxes     [boolean] ['query']
    Specify true to display the grid axes.

-----------------------------------------

dab   : displayAxesBold [boolean] ['query']
    Specify true to accent the grid axes by drawing them with a thicker line.

-----------------------------------------

ddl   : displayDivisionLines [boolean] ['query']
    Specify true to display the subdivision lines between grid lines.

-----------------------------------------

dgl   : displayGridLines [boolean] ['query']
    Specify true to display the grid lines.

-----------------------------------------

dol   : displayOrthographicLabels [boolean] ['query']
    Specify true to display the grid line numeric labels in the orthographic views.

-----------------------------------------

dpl   : displayPerspectiveLabels [boolean] ['query']
    Specify true to display the grid line numeric labels in the perspective view.

-----------------------------------------

d     : divisions       [uint] ['query']
    Sets the number of subdivisions between major grid lines. The default is 5. If the spacing is 5 units, setting divisions to 5 will cause division lines to appear 1 unit apart.

-----------------------------------------

olp   : orthographicLabelPosition [string] ['query']
    The position of the grid's numeric labels in orthographic views. Valid values are "axis" and "edge".

-----------------------------------------

plp   : perspectiveLabelPosition [string] ['query']
    The position of the grid's numeric labels in perspective views. Valid values are "axis" and "edge".

-----------------------------------------

r     : reset           [boolean] []
    Resets the ground plane to its default values

-----------------------------------------

s     : size            [linear] ['query']
    Sets the size of the grid in linear units. The default is 12 units.

-----------------------------------------

sp    : spacing         [linear] ['query']
    Sets the spacing between major grid lines in linear units. The default is 5 units.

-----------------------------------------

st    : style           [uint] ['query']
    This flag is obsolete and should not be used.

-----------------------------------------

tgl   : toggle          [boolean]
    Turns the ground plane display off in all windows, including orthographic windows. Default is true.

    """

def insertKnotSurface(q=1,e=1,add=1,cch=1,d="int",ib=1,nds="int",nk="int",p="float",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/insertKnotSurface.html



-----------------------------------------

insertKnotSurface is undoable, queryable, and editable.

The insertKnotSurface command inserts knots (aka isoparms) into a surface
given a list of parameter values. The number of knots to add at each parameter
value and whether the knots are added or complemented can be specified. The
name of the surface is returned and if history is on, the name of the
resulting dependency node is also returned.

You must specify one, none or all number of knots with the "-nk" flag. eg. if
you specify none, then the default (one) knot will be added at each specified
parameter value. If you specify one "-nk" value then that number of knots will
be added at each parameter value. Otherwise, you must specify the same number
of "-nk" flags as "-p" flags, defining the number of knots to be added at each
specified parameter value.

You can insert up to "degree" knots at a parameter value that isn't already an
isoparm. eg. for a degree 3 surface, you can insert up to 3 knots.

Use this operation if you need more CVs in a local area of the surface. Use
this operation if you want to create a corner in the surface.

Note: A single insertKnotSurface command cannot insert in both directions at
once; you must use two separate commands to do this.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addKnots        [boolean] ['query', 'edit']
    Whether to add knots or complement. Complement means knots will be added to reach the specified number of knots.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    Direction in which to insert knot: 0 - V direction, 1 - U direction   Default: 1

-----------------------------------------

ib    : insertBetween   [boolean] ['query', 'edit']
    If set to true, and there is more than one parameter value specified, the knots will get inserted at equally spaced intervals between the given parameter values, rather than at the parameter values themselves.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nk    : numberOfKnots   [int] ['query', 'edit']
    How many knots to insert   Default: 1

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    Parameter value(s) where knots are added   Default: 0.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def intersect(q=1,e=1,cch=1,fs=1,nds="int",tol="linear",ch=1,cos=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/intersect.html



-----------------------------------------

intersect is undoable, queryable, and editable.

The intersect command creates a curve on surface where all surfaces intersect
with each other. By default, the curve on surface is created for both
surfaces. However, by using the -fs flag, only the first surface will have a
curve on surface. Also, the intersection curve can be created as a 3D curve
rather than a curve on surface.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

fs    : firstSurface    [boolean] ['query', 'edit']
    Creates a curve-on-surface on the first surface only or on all surfaces (default).

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance to fit to.   Default: 0.01

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def loft(q=1,e=1,ar=1,cch=1,c=1,cc=1,d="int",nds="int",r=1,rsn=1,ss="int",u=1,ch=1,n="string",o=1,po="int",rn=1,rb=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/loft.html



-----------------------------------------

loft is undoable, queryable, and editable.

This command computes a skinned (lofted) surface passing through a number of
NURBS curves. There must be at least two curves present. The NURBS curves may
be surface isoparms, curve on surfaces, trimmed edges or polygon edges.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ar    : autoReverse     [boolean] ['query', 'edit']
    If set to true, the direction of the curves for the loft is computed automatically. If set to false, the values of the multi-use reverse flag are used instead.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

c     : close           [boolean] ['query', 'edit']
    If set to true, the resulting surface will be closed (periodic) with the start (end) at the first curve. If set to false, the surface will remain open.   Default: false

-----------------------------------------

cc    : createCusp      [boolean] ['query', 'edit']
    Multi-use flag; each occurence of the flag refers to the matching curve in the loft operation; if the flag is set the particular profile will have a cusp (tangent break) in the resulting surface.   Default: false

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface   Default: 3

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

r     : reverse         [boolean] ['query', 'edit']
    Multi-use flag; each occurence of the flag refers to the matching curve in the loft operation; if the flag is set the particular curve will be reversed before being used in the loft operation.   Default: false

-----------------------------------------

rsn   : reverseSurfaceNormals [boolean] ['query', 'edit']
    If set, the surface normals on the output NURBS surface will be reversed. This is accomplished by swapping the U and V parametric directions.   Default: false

-----------------------------------------

ss    : sectionSpans    [int] ['query', 'edit']
    The number of surface spans between consecutive curves in the loft.   Default: 1

-----------------------------------------

u     : uniform         [boolean] ['query', 'edit']
    If set to true, the resulting surface will have uniform parameterization in the loft direction. If set to false, the parameterization will be chord length.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean] []
    Force a curve range on complete input curve.

-----------------------------------------

rb    : rebuild         [boolean]
    Rebuild the input curve(s) before using them in the operation. Use nurbsCurveRebuildPref to set the parameters for the conversion.

    """

def makeSingleSurface(q=1,e=1,cch=1,ch=1,n="string",nds="int",o=1,st="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/makeSingleSurface.html



-----------------------------------------

makeSingleSurface is undoable, queryable, and editable.

This command performs a stitch and tessellate operation.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

st    : stitchTolerance [float]
    Stitch tolerance.   Default: 0.1

    """

def moveVertexAlongDirection(d="[float, float, float]",m="linear",n="linear",u="linear",uvn="[linear, linear, linear]",v="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/moveVertexAlongDirection.html



-----------------------------------------

moveVertexAlongDirection is undoable, NOT queryable, and NOT editable.

The command moves the selected vertex ( control vertex ) in the specified unit
direction by the given magnitude. The vertex(ices) may also be moved in the
direction of unit normal ( -n flag ). For NURBS surface vertices the direction
of movement could also be either in tangent along U or tangent along V. The
flags -n, -u, -v and -d are mutually exclusive, ie. the selected vertices can
be all moved in only -n or -u or -v or -d.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

d     : direction       [[float, float, float]] []
    move the vertex along the direction as specified. The direction is normalized.

-----------------------------------------

m     : magnitude       [linear] []
    move by the specified magnitude in the direction vector.

-----------------------------------------

n     : normalDirection [linear] []
    move components in the direction of normal by the given magnitude at the respective components. The normal is 'normalized'.

-----------------------------------------

u     : uDirection      [linear] []
    move components in the direction of tangent along U at the respective components where appropriate. The flag is ignored for polygons, NURBS curves. The u direction is normalized.

-----------------------------------------

uvn   : uvNormalDirection [[linear, linear, linear]] []
    move in the triad space [u,v,n] at the respective components by the specified displacements. The flag is ignored for polygons, NURBS curves.

-----------------------------------------

v     : vDirection      [linear]
    move components in the direction of tangent along V at the respective components where appropriate. The flag is ignored for polygons, NURBS curves.

    """

def multiProfileBirailSurface(q=1,e=1,cch=1,nds="int",tp1=1,tp2=1,tm="int",ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/multiProfileBirailSurface.html



-----------------------------------------

multiProfileBirailSurface is undoable, queryable, and editable.

The cmd creates a railed surface by sweeping the profiles using two rail
curves. The two rails are the last two arguments. For examples, if 5 curves
are specified, they will correspond to "curve1" "curve2" "curve3" "rail1"
"rail2".

In this case, the cmd creates a railed surface by sweeping the profile
"curve1" to profile "curve2", profile "curve2" to profile "curve3" along the
two rail curves "rail1", "rail2". There must be atleast 3 profile curves
followed by the two rail curves. The profile curves must intersect the two
rail curves. The constructed may be made tangent continuous to the first and
last profile using the flags -tp1, -tp2 provided the profiles are surface
curves i.e. isoparms, curve on surface or trimmed edge.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tp1   : tangentContinuityProfile1 [boolean] ['query', 'edit']
    Tangent continuous across the first profile. The profile must be a surface curve.   Default: false

-----------------------------------------

tp2   : tangentContinuityProfile2 [boolean] ['query', 'edit']
    Tangent continuous across the last profile. The profile must be a surface curve.   Default: false

-----------------------------------------

tm    : transformMode   [int] ['query', 'edit']
    transform mode ( Non proportional, proportional ). Non proportional is default value.   Default: 0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def nurbsBoolean(q=1,e=1,cch=1,nds="int",op="int",tlb="linear",ch=1,n="string",nsf="int",o=1,sc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsBoolean.html



-----------------------------------------

nurbsBoolean is undoable, queryable, and editable.

This command performs a boolean operation.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

op    : operation       [int] ['query', 'edit']
    Type of Boolean operation.   Default: 0

-----------------------------------------

tlb   : tolerance       [linear] ['query', 'edit']
    fitting tolerance.   Default: 0.01

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nsf   : nsrfsInFirstShell [int] []
    The number of selection items comprising the first shell.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

sc    : smartConnection [boolean]
    Look for any of the selection items having a boolean operation as history.   Default is true.

    """

def nurbsCopyUVSet(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsCopyUVSet.html



-----------------------------------------

nurbsCopyUVSet is undoable, queryable, and editable.

This is only a sample command for debugging purposes, which makes a copy of
the implicit st parameterization on a nurbs surface to be the 1st explicit
uvset.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.
    """

def nurbsCube(q=1,e=1,ax="[linear, linear, linear]",cch=1,d="int",hr="float",lr="float",nds="int",u="int",v="int",p="[linear, linear, linear]",w="linear",ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsCube.html



-----------------------------------------

nurbsCube is undoable, queryable, and editable.

The nurbsCube command creates a new NURBS Cube made up of six planes. It
creates an unit cube with center at origin by default.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    The primitive's axis

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface. 1 - linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic   Default: 3

-----------------------------------------

hr    : heightRatio     [float] ['query', 'edit']
    Ratio of "height" to "width"   Default: 1.0

-----------------------------------------

lr    : lengthRatio     [float] ['query', 'edit']
    Ratio of "length" to "width"   Default: 1.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

u     : patchesU        [int] ['query', 'edit']
    Number of sections in U   Default: 1

-----------------------------------------

v     : patchesV        [int] ['query', 'edit']
    Number of sections in V   Default: 1

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    The primitive's pivot point

-----------------------------------------

w     : width           [linear] ['query', 'edit']
    Width of the object   Default: 1.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def nurbsCurveToBezier():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsCurveToBezier.html



-----------------------------------------

nurbsCurveToBezier is undoable, NOT queryable, and NOT editable.

The nurbsCurveToBezier command attempts to convert an existing NURBS curve to
a Bezier curve.


-----------------------------------------


Return Value:

string[]  (object name and node name)
    """

def nurbsEditUV(q=1,a="float",pu="float",pv="float",r=1,rr="float",rot=1,s=1,su="float",sv="float",u="float",v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsEditUV.html



-----------------------------------------

nurbsEditUV is undoable, queryable, and NOT editable.

Command Edits UVs on NURBS objects. When used with the query flag, it returns
the UV values associated with the specified components.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [float] ['query']
    Specifies the angle value (in degrees) by which the UV values are to be rotated.

-----------------------------------------

pu    : pivotU          [float] ['query']
    Specifies the pivot value, in the u direction, about which the scale or rotate is to be performed.

-----------------------------------------

pv    : pivotV          [float] ['query']
    Specifies the pivot value, in the v direction, about which the scale or rotate is to be performed.

-----------------------------------------

r     : relative        [boolean] ['query']
    Specifies whether this command is editing the values relative to the currently existing values. Default is true;

-----------------------------------------

rr    : rotateRatio     [float] ['query']
    Specifies the ratio value by which the UV values are to be rotated. Default is 1.0

-----------------------------------------

rot   : rotation        [boolean] ['query']
    Specifies whether this command is editing the values with rotation values

-----------------------------------------

s     : scale           [boolean] ['query']
    Specifies whether this command is editing the values with scale values

-----------------------------------------

su    : scaleU          [float] ['query']
    Specifies the scale value in the u direction.

-----------------------------------------

sv    : scaleV          [float] ['query']
    Specifies the scale value in the v direction.

-----------------------------------------

u     : uValue          [float] ['query']
    Specifies the value, in the u direction - absolute if relative flag is false..

-----------------------------------------

v     : vValue          [float]
    Specifies the value, in the v direction - absolute if relative flag is false..

    """

def nurbsPlane(q=1,e=1,ax="[linear, linear, linear]",cch=1,d="int",lr="float",nds="int",u="int",v="int",p="[linear, linear, linear]",w="linear",ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsPlane.html



-----------------------------------------

nurbsPlane is undoable, queryable, and editable.

The nurbsPlane command creates a new NURBS Plane and return the name of the
new surface. It creates an unit plane with center at origin by default.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    The primitive's axis

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface 1 - linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic   Default: 3

-----------------------------------------

lr    : lengthRatio     [float] ['query', 'edit']
    The ratio of "length" to "width" of the plane.   Default: 1.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

u     : patchesU        [int] ['query', 'edit']
    The number of spans in the U direction.   Default: 1

-----------------------------------------

v     : patchesV        [int] ['query', 'edit']
    The number of spans in the V direction.   Default: 1

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    The primitive's pivot point

-----------------------------------------

w     : width           [linear] ['query', 'edit']
    The width of the plane   Default: 1.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def nurbsSelect(bs=1,bb=1,gs="int",lb=1,rb=1,ss="int",tb=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsSelect.html



-----------------------------------------

nurbsSelect is NOT undoable, NOT queryable, and NOT editable.

Performs selection operations on NURBS objects.  
If any of the border flags is set, then the appropriate borders are selected.
Otherwise the current CV selection is used, or all CVs if the surfaces is
selected as an object.  
The growSelection, shrinkSelection, borderSelection flags are then applied in
that order.  
In practice, it is recommended to use one flag at a time, except for the
border flags.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

bs    : borderSelection [boolean] []
    Extract the border of the current CV selection.

-----------------------------------------

bb    : bottomBorder    [boolean] []
    Selects the bottom border of the surface (V=0).

-----------------------------------------

gs    : growSelection   [int] []
    Grows the CV selection by the given number of CV

-----------------------------------------

lb    : leftBorder      [boolean] []
    Selects the left border of the surface (U=0).

-----------------------------------------

rb    : rightBorder     [boolean] []
    Selects the right border of the surface (U=MAX).

-----------------------------------------

ss    : shrinkSelection [int] []
    Shrinks the CV selection by the given number of CV

-----------------------------------------

tb    : topBorder       [boolean]
    Selects the top border of the patches (V=MAX).

    """

def nurbsToPoly(q=1,e=1,cch=1,ch=1,cvt="int",eta=1,n="string",nds="int",o=1,ues=1,esr="float",nuf="float",nvf="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsToPoly.html



-----------------------------------------

nurbsToPoly is undoable, queryable, and editable.

This command tesselates a NURBS surface and produces a polygonal surface. The
name of the new polygonal surface is returned. If construction history is ON,
then the name of the new dependency node is returned as well.


-----------------------------------------


Return Value:

string[]  The polygon and optionally the dependency node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cvt   : curvatureTolerance [int] ['query', 'edit']
    Presets for level of secondary criteria curvature tolerance: 0 = highest tolerance, 1 = high tolerance, 2 = medium tolerance, 3 = no tolerance   Default: 2

-----------------------------------------

eta   : explicitTessellationAttributes [boolean] ['query', 'edit']
    specify advanced or novice mode for tessellation parameters   Default: true

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

ues   : smoothEdge      [boolean] ['query', 'edit']
    Specifies if the decision to continue tessellation should be based on the nurbs edge smoothness   Default: false

-----------------------------------------

esr   : smoothEdgeRatio [float] ['query', 'edit']
    Specifies the edge smooth ratio. The higher the value, the smoother the edge will be.   Default: 0.99

-----------------------------------------

nuf   : uDivisionsFactor [float] ['query', 'edit']
    Specifies the tessellation increase factor in U for novice mode   Default: 1.5

-----------------------------------------

nvf   : vDivisionsFactor [float]
    Specifies the tessellation increase factor in V for novice mode   Default: 1.5

    """

def nurbsToPolygonsPref(q=1,cht="float",chr="float",d="float",es=1,f="uint",ft="float",mrt="uint",m="uint",mt="float",mel="float",pc="uint",pt="uint",un="uint",ut="uint",uch=1,ucr=1,vn="uint",vt="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsToPolygonsPref.html



-----------------------------------------

nurbsToPolygonsPref is undoable, queryable, and NOT editable.

This command sets the values used by the nurbs-to-polygons (or "tesselate")
preference. This preference is used by Maya menu items and is saved between
Maya sessions. To query any of the flags, use the "-query" flag. For more
information on the flags, see the node documentation for the "nurbsTessellate"
node.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cht   : chordHeight     [float] ['query']
    

-----------------------------------------

chr   : chordHeightRatio [float] ['query']
    

-----------------------------------------

d     : delta3D         [float] ['query']
    

-----------------------------------------

es    : edgeSwap        [boolean] ['query']
    

-----------------------------------------

f     : format          [uint] ['query']
    Valid values are 0, 1 and 2.

-----------------------------------------

ft    : fraction        [float] ['query']
    

-----------------------------------------

mrt   : matchRenderTessellation [uint] ['query']
    

-----------------------------------------

m     : merge           [uint] ['query']
    

-----------------------------------------

mt    : mergeTolerance  [float] ['query']
    

-----------------------------------------

mel   : minEdgeLen      [float] ['query']
    

-----------------------------------------

pc    : polyCount       [uint] ['query']
    

-----------------------------------------

pt    : polyType        [uint] ['query']
    

-----------------------------------------

un    : uNumber         [uint] ['query']
    

-----------------------------------------

ut    : uType           [uint] ['query']
    

-----------------------------------------

uch   : useChordHeight  [boolean] ['query']
    

-----------------------------------------

ucr   : useChordHeightRatio [boolean] ['query']
    

-----------------------------------------

vn    : vNumber         [uint] ['query']
    

-----------------------------------------

vt    : vType           [uint]
    

    """

def nurbsUVSet(q=1,e=1,c=1,ue=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsUVSet.html



-----------------------------------------

nurbsUVSet is undoable, queryable, and editable.

Allows user to toggle between implicit and explicit UVs on a NURBS object.
Also provides a facility to create, delete, rename and set the current
explicit UVSet. An implicit UVSet is non-editable. It uses the parametric
make-up of the NURBS object to determine the location of UVs (isoparm
intersections). NURBS objects also support explicit UVSets which are similar
to the UVs of a polygonal object. UVs are created at the knots (isoparm
intersections) of the object and are fully editable. In order to access UV
editing capabilities on a NURBS object an explicit UVSet must be created and
set as the current UVSet.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : create          [boolean] ['query', 'edit']
    Creates an explicit UV set on the specified surface. If the surface already has an explicit UV set this flag will do nothing. Use the -ue/useExplicit flag to set/unset the explicit UV set as the current UV set.

-----------------------------------------

ue    : useExplicit     [boolean]
    Toggles the usage of explicit/implicit UVs. When true, explicit UVs will be used, otherwise the object will use implicit UVs.

    """

def offsetSurface(q=1,e=1,cch=1,d="linear",m="int",nds="int",ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/offsetSurface.html



-----------------------------------------

offsetSurface is undoable, queryable, and editable.

The offset command creates new offset surfaces from the selected surfaces. The
default method is a surface offset, which offsets relative to the surface
itself. The CV offset method offsets the CVs directly rather than the surface,
so is usually slightly less accurate but is faster. The offset surface will
always have the same degree, number of CVs and knot spacing as the original
surface.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : distance        [linear] ['query', 'edit']
    Offset distance   Default: 1.0

-----------------------------------------

m     : method          [int] ['query', 'edit']
    Offset method 0 - Surface Fit 1 - CV Fit   Default: 0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def planarSrf(q=1,e=1,cch=1,d="int",ko=1,nds="int",tol="linear",ch=1,n="string",o=1,po="int",rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/planarSrf.html



-----------------------------------------

planarSrf is undoable, queryable, and editable.

This command computes a planar trimmed surface given planar boundary curves
that form a closed region.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface: 1 - linear, 3 - cubic   Default: 3

-----------------------------------------

ko    : keepOutside     [boolean] ['query', 'edit']
    If true, keep the regions outside the given curves.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The distance tolerance for the cvs of the curves to be in the same plane.   Default: 0.01

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def plane(l="linear",n="string",p="[linear, linear, linear]",r="[angle, angle, angle]",s="linear",w="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/plane.html



-----------------------------------------

plane is undoable, NOT queryable, and NOT editable.

The command creates a sketch plane (also known as a "construction plane") in
space. To create an object (such as a NURBS curve, joint chain or polygon) on
a construction plane, you need to first make the plane live. See also the
makeLive command.


-----------------------------------------


Return Value:

string  (name of the new plane)


-----------------------------------------


Flags:

-----------------------------------------

l     : length          [linear] []
    The length of plane. "linear" means that this flag can handle values with units.

-----------------------------------------

n     : name            [string] []
    Name the resulting object.

-----------------------------------------

p     : position        [[linear, linear, linear]] []
    3D position where the centre of the plane is positioned. "linear" means that this flag can handle values with units.

-----------------------------------------

r     : rotation        [[angle, angle, angle]] []
    The rotation of plane. "angle" means that this flag can handle values with units.

-----------------------------------------

s     : size            [linear] []
    The combined size (size x size) of plane. "linear" means that this flag can handle values with units.

-----------------------------------------

w     : width           [linear]
    The width of plane. "linear" means that this flag can handle values with units.

    """

def pointOnSurface(q=1,e=1,cch=1,ch=1,nds="int",no=1,nn=1,ntu=1,ntv=1,u="float",v="float",p=1,tu=1,tv=1,top=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pointOnSurface.html



-----------------------------------------

pointOnSurface is undoable, queryable, and editable.

This command returns information for a point on a surface. If no flag is
specified, this command assumes p/position by default. If more than one flag
is specifed, then a string array is returned.


-----------------------------------------


Return Value:

float[3]  Vector query result    
string  String query result  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

no    : normal          [boolean] ['query', 'edit']
    Returns the (x,y,z) normal of the specified point on the surface

-----------------------------------------

nn    : normalizedNormal [boolean] ['query', 'edit']
    Returns the (x,y,z) normalized normal of the specified point on the surface

-----------------------------------------

ntu   : normalizedTangentU [boolean] ['query', 'edit']
    Returns the (x,y,z) normalized U tangent of the specified point on the surface

-----------------------------------------

ntv   : normalizedTangentV [boolean] ['query', 'edit']
    Returns the (x,y,z) normalized V tangent of the specified point on the surface

-----------------------------------------

u     : parameterU      [float] ['query', 'edit']
    The U parameter value on surface   Default: 0.0

-----------------------------------------

v     : parameterV      [float] ['query', 'edit']
    The V parameter value on surface   Default: 0.0

-----------------------------------------

p     : position        [boolean] ['query', 'edit']
    Returns the (x,y,z) positon of the specified point on the surface

-----------------------------------------

tu    : tangentU        [boolean] ['query', 'edit']
    Returns the (x,y,z) U tangent of the specified point on the surface

-----------------------------------------

tv    : tangentV        [boolean] ['query', 'edit']
    Returns the (x,y,z) V tangent of the specified point on the surface

-----------------------------------------

top   : turnOnPercentage [boolean]
    Whether the parameter is normalized (0,1) or not   Default: false

    """

def pointPosition(l=1,w=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pointPosition.html



-----------------------------------------

pointPosition is undoable, NOT queryable, and NOT editable.

This command returns the world or local space position for any type of point
object. Valid selection items are: \- curve and surface CVs \- poly vertices
\- lattice points \- particles \- curve and surface edit points \- curve and
surface parameter points \- poly uvs \- rotate/scale/joint pivots \- selection
handles \- locators, param locators and arc length locators

It works on the selected object or you can specify the object in the command.
By default, if no flag is specified then the world position is returned.


-----------------------------------------


Return Value:

float[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

l     : local           [boolean] []
    Return the point in local space coordinates.

-----------------------------------------

w     : world           [boolean]
    Return the point in world space coordinates.

    """

def projectCurve(q=1,e=1,cch=1,d="[linear, linear, linear]",dx="linear",dy="linear",dz="linear",nds="int",tol="linear",un=1,ch=1,n="string",o=1,rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/projectCurve.html



-----------------------------------------

projectCurve is undoable, queryable, and editable.

The projectCurve command creates curves on surface where all selected curves
project onto the selected surfaces. Projection can be done using the surface
normals or the user can specify the vector to project along. Note: the user
does not have to specify the curves and surfaces in any particular order in
the command line.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : direction       [[linear, linear, linear]] ['query', 'edit']
    Direction of projection. Available only if useNormal is false.

-----------------------------------------

dx    : directionX      [linear] ['query', 'edit']
    X direction of projection.   Default: 0.0

-----------------------------------------

dy    : directionY      [linear] ['query', 'edit']
    Y direction of projection.   Default: 0.0

-----------------------------------------

dz    : directionZ      [linear] ['query', 'edit']
    Z direction of projection.   Default: 1.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance to fit to.   Default: 0.01

-----------------------------------------

un    : useNormal       [boolean] ['query', 'edit']
    True if the surface normal is to be used and false if the direction vector should be used instead.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def propMove(p="float",px="float",py="float",pz="float",pi="[float, float, float]",r="[angle, angle, angle]",s="[float, float, float]",t="[linear, linear, linear]",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/propMove.html



-----------------------------------------

propMove is undoable, NOT queryable, and NOT editable.

Performs a proportional translate, scale or rotate operation on any number of
objects. The percentages to rotate, scale or translate by can be specified
using either the -p flags or -px, -py, -pz flags. Each selected object must
have a corresponding -p or -px, -py, -pz flag. The rotate, scale or translate
performed is relative.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

p     : percent         [float] []
    The percentage effect that the specified x,y,z has on an object. This flag must be specified once for each object, ie. if there are 4 objects specified, there must be 4 "-p" flags, (otherwise a percentage of 1.0 will be used). This flag generally has a range between 0.0 and 1.0, but can be any float value.

-----------------------------------------

px    : percentX        [float] []
    The percentage effect that the specified x has on an object. This flag is specified one per object. The value ranges between 0.0 and 1.0, but can be any float value. If the -p flag has been specified, this flag usage is invalid.

-----------------------------------------

py    : percentY        [float] []
    The percentage effect that the specified y has on an object. This flag is specified one per object. The value ranges between 0.0 and 1.0, but can be any float value. If the -p flag has been specified, this flag usage is invalid.

-----------------------------------------

pz    : percentZ        [float] []
    The percentage effect that the specified z has on an object. This flag is specified one per object. The value ranges between 0.0 and 1.0, but can be any float value. If the -p flag has been specified, this flag usage is invalid.

-----------------------------------------

pi    : pivot           [[float, float, float]] []
    Specify the pivot about which a rotation or scale will occur. The change in pivot lasts only as long as the current 'propMove' command, and so must be used in conjunction with one of the above move flags for any effect to be noticeable.

-----------------------------------------

r     : rotate          [[angle, angle, angle]] []
    Proportionally rotate each object by the given angles. The rotation values are scaled by the percentage specified by that object's corresponding "-percent" flag. All angles are in degrees. The rotation is about the pivot specified by the "-pivot" flag, or (0, 0, 0) if the "-pivot" flag is not present.

-----------------------------------------

s     : scale           [[float, float, float]] []
    Proportionally scale each object by the given amounts. The scale values are scaled by the percentage specified by that object's corresponding "-percent" flag. The position and size of each object is measured relative to the pivot specified by the "-pivot" flag, and defaults to each object's individual pivot. In the case of control vertices, or some other object component, the default is the parent object's pivot.

-----------------------------------------

t     : translate       [[linear, linear, linear]] []
    Proportionally translate each object by the given amounts. The translation values are scaled by the percentage specified by that object's corresponding "-percent" flag. The "-pivot" flag has no effect on translation.

-----------------------------------------

ws    : worldSpace      [boolean]
    Use worldspace for the calculations.

    """

def rebuildSurface(q=1,e=1,cch=1,du="int",dv="int",dir="int",end="int",fr="int",kcp=1,kc=1,kr="int",nds="int",rt="int",su="int",sv="int",tol="linear",ch=1,n="string",o=1,po="int",rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rebuildSurface.html



-----------------------------------------

rebuildSurface is undoable, queryable, and editable.

This command rebuilds a surface by modifying its parameterization. In some
cases the shape of the surface may also change. The rebuildType (-rt)
attribute determines how the surface is rebuilt.

The optional second surface can be used to specify a reference
parameterization.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

du    : degreeU         [int] ['query', 'edit']
    The degree of the resulting surface in the u direction 0 - maintain current, 1 - linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic   Default: 3

-----------------------------------------

dv    : degreeV         [int] ['query', 'edit']
    The degree of the resulting surface in the v direction 0 - maintain current, 1 - linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic   Default: 3

-----------------------------------------

dir   : direction       [int] ['query', 'edit']
    The direction in which to rebuild: 0 - U, 1 - V, 2 - Both U and V   Default: 2

-----------------------------------------

end   : endKnots        [int] ['query', 'edit']
    End conditions for the surface 0 - uniform end knots, 1 - multiple end knots,   Default: 0

-----------------------------------------

fr    : fitRebuild      [int] ['query', 'edit']
    Specify the type of rebuild method to be used: 0 - Convert Classic, the default and original convert method. 1 - Fit using the least squares fit method. 2 - Convert Match, alternate matching convert method. 3 - Convert Grid, uses a grid-based fit algorithm.   Default: 0

-----------------------------------------

kcp   : keepControlPoints [boolean] ['query', 'edit']
    Use the control points of the input surface. This forces uniform parameterization unless rebuildType is 2 (match knots)   Default: false

-----------------------------------------

kc    : keepCorners     [boolean] ['query', 'edit']
    The corners of the resulting surface will not change from the corners of the input surface.   Default: true

-----------------------------------------

kr    : keepRange       [int] ['query', 'edit']
    Determine the parameterization for the resulting surface. 0 - reparameterize the resulting surface from 0 to 1; 1 - keep the original surface parameterization; 2 - reparameterize the result from 0 to number of spans   Default: 1

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rt    : rebuildType     [int] ['query', 'edit']
    The rebuild type: 0 - uniform, 1 - reduce spans, 2 - match knots, 3 - remove multiple knots, 4 - force non rational 5 - rebuild ends 6 - trim convert (uniform) 7 - into Bezier mesh   Default: 0

-----------------------------------------

su    : spansU          [int] ['query', 'edit']
    The number of spans in the u direction in resulting surface. Used only when rebuildType is 0 - uniform. If 0, keep the same number of spans as the original surface.   Default: 4

-----------------------------------------

sv    : spansV          [int] ['query', 'edit']
    The number of spans in the v direction in resulting surface. Used only when rebuildType is 0 - uniform. If 0, keep the same number of spans as the original surface.   Default: 4

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to rebuild   Default: 0.01

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def reverseSurface(q=1,e=1,cch=1,d="int",nds="int",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/reverseSurface.html



-----------------------------------------

reverseSurface is undoable, queryable, and editable.

The reverseSurface command reverses one or both directions of a surface or can
be used to "swap" the U and V directions (this creates the effect of reversing
the surface normal). The name of the newly reversed surface and the name of
the resulting dependency node is returned. The resulting surface has the same
parameter ranges as the original surface.

This command also handles selected surface isoparms. For a selected isoparm,
imagine that the isoparm curve is reversed after the operation. E.g.
reverseSurface surface.v[0.1] will reverse in the U direction.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    The direction to reverse the surface in: 0 - U, 1 - V, 2 - Both U and V, 3 - Swap   Default: 0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def revolve(q=1,e=1,acn=1,ax="[linear, linear, linear]",aco="int",axx="linear",axy="linear",axz="linear",br=1,cch=1,cpa="int",d="int",esw="angle",nds="int",p="[linear, linear, linear]",px="linear",py="linear",pz="linear",r="linear",ra="float",s="int",ssw="angle",tol="linear",ut=1,ch=1,n="string",o=1,po="int",rn=1,rb=1,ulp=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/revolve.html



-----------------------------------------

revolve is undoable, queryable, and editable.

This command creates a revolved surface by revolving the given profile curve
about an axis. The profile curve can be a curve, curve-on-surface, surface
isoparm, or trim edge.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

acn   : autoCorrectNormal [boolean] ['query', 'edit']
    If this is set to true we will attempt to reverse the direction of the axis in case it is necessary to do so for the surface normals to end up pointing to the outside of the object.   Default: false

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    Revolve axis

-----------------------------------------

aco   : axisChoice      [int] ['query', 'edit']
    Only used for computed axis/pivot case. As we are computing the axis for a planar curve, we have two choices for the major axis based axis. We will choose the axis corresponding to the longer dimension of the object (0), or explicitly choose one or the other (choices 1 and 2).   Default: 0

-----------------------------------------

axx   : axisX           [linear] ['query', 'edit']
    X of the axis   Default: 1

-----------------------------------------

axy   : axisY           [linear] ['query', 'edit']
    Y of the axis   Default: 0

-----------------------------------------

axz   : axisZ           [linear] ['query', 'edit']
    Z of the axis   Default: 0

-----------------------------------------

br    : bridge          [boolean] ['query', 'edit']
    If true, we will close a partial revolve to get a pie shaped surface. The surface will be closed, but not periodic the way it is in the full revolve case.   Default: false

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cpa   : computePivotAndAxis [int] ['query', 'edit']
    If this is set to 2, we will compute the axis, use the curve position and radius to compute the pivot for the revolve internally. The value of the pivot and axis attributes are ignored. If this is set to 1, we will take the supplied axis, but compute the pivot. If this is set to 0, we will take both the supplied axis and pivot.   Default: 0

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface.   Default: 3

-----------------------------------------

esw   : endSweep        [angle] ['query', 'edit']
    The value for the end sweep angle, in the current units. This must be no more than the maximum, 360 degrees, or 2 Pi radians.   Default: 6.2831853

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    Revolve pivot point

-----------------------------------------

px    : pivotX          [linear] ['query', 'edit']
    X of the pivot   Default: 0

-----------------------------------------

py    : pivotY          [linear] ['query', 'edit']
    Y of the pivot   Default: 0

-----------------------------------------

pz    : pivotZ          [linear] ['query', 'edit']
    Z of the pivot   Default: 0

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    The pivot point will be this distance away from the bounding box of the curve, if computedPivot is set to true. The value of the pivot attribute is ignored.   Default: 1

-----------------------------------------

ra    : radiusAnchor    [float] ['query', 'edit']
    The position on the curve for the anchor point so that we can compute the pivot using the radius value. If in 0 - 1 range, its on the curve, normalized parameter range. If < 0 or > 1, its computed based on the bounding box.   Default: -1

-----------------------------------------

s     : sections        [int] ['query', 'edit']
    Number of sections of the resulting surface (if tolerance is not used).   Default: 8

-----------------------------------------

ssw   : startSweep      [angle] ['query', 'edit']
    The value for the start sweep angle, in the current units. This must be no more than the maximum, 360 degrees, or 2 Pi radians.   Default: 0

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance to build to (if useTolerance attribute is set)   Default: 0.01

-----------------------------------------

ut    : useTolerance    [boolean] ['query', 'edit']
    Use the tolerance, or the number of sections to control the sections.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int] []
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

-----------------------------------------

rn    : range           [boolean] []
    Force a curve range on complete input curve.

-----------------------------------------

rb    : rebuild         [boolean] []
    Rebuild the input curve(s) before using them in the operation. Use nurbsCurveRebuildPref to set the parameters for the conversion.

-----------------------------------------

ulp   : useLocalPivot   [boolean]
    If true, then the pivot of the profile curve is used as the start point of the axis of revolution.

    """

def roundConstantRadius(q=1,e=1,a=1,ch=1,n="string",o=1,rad="linear",s="[string, int]",sa="int",sb="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/roundConstantRadius.html



-----------------------------------------

roundConstantRadius is undoable, queryable, and editable.

This command generates constant radius NURBS fillets and NURBS corner surfaces
for matching edge pairs on NURBS surfaces. An edge pair is a matching pair of
surface isoparms or trim edges. This command can handle more than one edge
pair at a time. This command can also handle compound edges, which is where an
edge pair is composed of more than two surfaces. Use the "-sa" and "-sb" flags
in this case.

The results from this command are three surface var groups plus the name of
the new roundConstantRadius dependency node, if history was on. The 1st var
group contains trimmed copies of the original surfaces. The 2nd var group
contains the new NURBS fillet surfaces. The 3rd var group contains the new
NURBS corners (if any).

A simple example of an edge pair is an edge of a NURBS cube, where two faces
of the cube meet. This command generates a NURBS fillet at the edge and trims
back the faces.

Another example is a NURBS cylinder with a planar trim surface cap. This
command will create a NURBS fillet where the cap meets the the cylinder and
will trim back the cap and the cylinder.

Another example involves all 12 edges of a NURBS cube. NURBS fillets are
created where any face meets another face. NURBS corners are created whenever
3 edges meet at a corner.


-----------------------------------------


Return Value:

string[]  (resulting NURBS surfaces' names and node name)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : append          [boolean] []
    If true, then an edge pair is being added to an existing round dependency node. Default is false. When this flag is true, an existing round dependency node must be specified. See example below.

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rad   : radiuss         [linear] []
    Use this flag to specify radius. This overrides the "r/radius" flag. If only one "rad" flag is used, then it is applied to all edge pairs. If more than one "rad" flag is used, then the number of "-rad" flags must equal the number of edge pairs. For example, for four edge pairs, zero, one or four "rad" flags must be specified.

-----------------------------------------

s     : side            [[string, int]] []
    Use this flag for compound edges. It replaces the sidea/sideb flags and is compatible with Python. The first argument must be either "a" or "b". The same number of "a" values as "b" values must be specified. If no sides are specified with the "side" flag (or sidea/sideb flags), then the edges are assumed to be in pairs. See also examples below. For example, two faces of a cube meet at an edge pair. Suppose one of the faces is then split in two pieces at the middle of the edge, so that there is one face on side "A", and two pieces on side "B". In this case the flag combination: -side "a" 1 -side "b" 2 would be used. The edges must be specified in the corresponding order: // MEL roundConstantRadius -side "a" 1 -side "b" 2 isoA isoB1 isoB2; # Python maya.cmds.roundConstantRadius( 'isoA', 'isoB1', 'isoB2', side=[("a",1), ("b",2)] )

-----------------------------------------

sa    : sidea           [int] []
    Use this flag for compound edges in conjunction with the following "-sb" flag. This flag is not intended for use from Python. Please see "side" flag instead. The same number of "-sa" flags as "-sb" flags must be specified. If no "-sa" nor "-sb" flags are specified, then the edges are assumed to be in pairs. See also examples below. For example, two faces of a cube meet at an edge pair. Suppose one of the faces is then split in two pieces at the middle of the edge, so that there is one face on side "A", and two pieces on side "B". In this case, the flag combination: -sidea 1 -sideb 2 would be used. The edges must be specified in the corresponding order: roundConstantRadius -sidea 1 -sideb 2 isoA isoB1 isoB2;

-----------------------------------------

sb    : sideb           [int]
    Use this flag for compound edges in conjunction with the "-sa" flag. See description for the "-sa" flag. This flag is not intended for use from Python. Please see "side" flag instead.

    """

def singleProfileBirailSurface(q=1,e=1,cch=1,nds="int",tp1=1,tm="int",ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/singleProfileBirailSurface.html



-----------------------------------------

singleProfileBirailSurface is undoable, queryable, and editable.

This cmd creates a railed surface by sweeping the profile curve along the two
rail curves. One of the requirements for surface creation is the profile curve
must intersect the two rail curves. If the profile is a surface curve i.e.
isoparm, curve on surface or trimmed edge then tangent continuity across the
surface underlying the profile may be enabled using the flag -tp1 true.

The first argument represetns the profile curve, the second and third the
rails.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tp1   : tangentContinuityProfile1 [boolean] ['query', 'edit']
    Need to be tangent continuous across the profile. The profile must be a surface curve.   Default: false

-----------------------------------------

tm    : transformMode   [int] ['query', 'edit']
    transform mode ( Non proportional, proportional ). Non proportional is default value.   Default: 0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def smoothTangentSurface(q=1,e=1,cch=1,d="int",nds="int",p="float",s="int",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/smoothTangentSurface.html



-----------------------------------------

smoothTangentSurface is undoable, queryable, and editable.

The smoothTangentSurface command smooths the surface along an isoparm at each
parameter value. The name of the surface is returned and if history is on, the
name of the resulting dependency node is also returned. This command only
applies to parameter values with a multiple knot value. (If the given
parameter value has no multiple knot associated with it, then the dependency
node is created but the surface doesn't change.)  
  
When would you use this? If you have a surface consisting of a number of
Bezier patches or any isoparms with more than a single knot multiplicity, you
could get into a situation where a tangent break occurs. So, it only makes
sense to do this operation on the knot isoparms, and not anywhere in between,
because the surface is already smooth everywhere in between.  
  
If you have a cubic or higher degree surface, asking for the maximal
smoothness will give you tangent, curvature, etc. up to the degree-1
continuity. Asking for tangent will just give you tangent continuity.  
  
It should be mentioned that this is "C", not "G" continuity we're talking
about, so technically, you can still see visual tangent breaks if the surface
is degenerate.

Note: A single smoothTangentSurface command cannot smooth in both directions
at once; you must use two separate commands to do this.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : direction       [int] ['query', 'edit']
    Direction in which to smooth knot: 0 - V direction, 1 - U direction   Default: 1

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    Parameter value(s) where knots are added   Default: 0.0

-----------------------------------------

s     : smoothness      [int] ['query', 'edit']
    Smoothness to get: 0 - Tangent, 1 - Maximum (based on the degree)   Default: 1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def sphere(q=1,e=1,ax="[linear, linear, linear]",cch=1,d="int",esw="angle",hr="float",nds="int",p="[linear, linear, linear]",r="linear",s="int",nsp="int",ssw="angle",tol="linear",ut=1,ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/sphere.html



-----------------------------------------

sphere is undoable, queryable, and editable.

The sphere command creates a new sphere. The number of spans in the in each
direction of the sphere is determined by the useTolerance attribute. If -ut is
true then the -tolerance attribute will be used. If -ut is false then the
-sections attribute will be used.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    The primitive's axis

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface: 1 - linear, 3 - cubic   Default: 3

-----------------------------------------

esw   : endSweep        [angle] ['query', 'edit']
    The angle at which to end the surface of revolution. Default is 2Pi radians, or 360 degrees.   Default: 6.2831853

-----------------------------------------

hr    : heightRatio     [float] ['query', 'edit']
    Ratio of "height" to "width"   Default: 2.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    The primitive's pivot point

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    The radius of the object   Default: 1.0

-----------------------------------------

s     : sections        [int] ['query', 'edit']
    The number of sections determines the resolution of the surface in the sweep direction. Used only if useTolerance is false.   Default: 8

-----------------------------------------

nsp   : spans           [int] ['query', 'edit']
    The number of spans determines the resolution of the surface in the opposite direction.   Default: 1

-----------------------------------------

ssw   : startSweep      [angle] ['query', 'edit']
    The angle at which to start the surface of revolution   Default: 0

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to build the surface. Used only if useTolerance is true   Default: 0.01

-----------------------------------------

ut    : useTolerance    [boolean] ['query', 'edit']
    Use the specified tolerance to determine resolution. Otherwise number of sections will be used.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def squareSurface(q=1,e=1,cch=1,ct1="int",ct2="int",ct3="int",ct4="int",cfc="int",ept="linear",nds="int",rc1=1,rc2=1,rc3=1,rc4=1,ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/squareSurface.html



-----------------------------------------

squareSurface is undoable, queryable, and editable.

This command produces a square surface given 3 or 4 curves. This resulting
square surface is created within the intersecting region of the selected
curves. The order of selection is important and the curves must intersect or
their ends must meet.  

You must specify one continuity type flag for each selected curve. If
continuity type is 1 (fixed, no tangent continuity) then the
curveFitCheckpoints flag (cfc) is not required.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ct1   : continuityType1 [int] ['query', 'edit']
    Continuity type legal values for curve 1: 1 - fixed boundary 2 - tangent continuity 3 - implied tangent continuity   Default: 2

-----------------------------------------

ct2   : continuityType2 [int] ['query', 'edit']
    Continuity type legal values for curve 2: 1 - fixed boundary 2 - tangent continuity 3 - implied tangent continuity   Default: 2

-----------------------------------------

ct3   : continuityType3 [int] ['query', 'edit']
    Continuity type legal values for curve 3: 1 - fixed boundary 2 - tangent continuity 3 - implied tangent continuity   Default: 2

-----------------------------------------

ct4   : continuityType4 [int] ['query', 'edit']
    Continuity type legal values for curve 4: 1 - fixed boundary 2 - tangent continuity 3 - implied tangent continuity   Default: 2

-----------------------------------------

cfc   : curveFitCheckpoints [int] ['query', 'edit']
    The number of points per span to check the tangency deviation between the boundary curve and the created tangent square surface. Only available for the tangent continuity type.   Default: 5

-----------------------------------------

ept   : endPointTolerance [linear] ['query', 'edit']
    Tolerance for end points, only used if endPoint attribute is true.   Default: 0.1

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rc1   : rebuildCurve1   [boolean] ['query', 'edit']
    A boolean to determine if input curve 1 should be rebuilt (with curvature continuity).   Default: false

-----------------------------------------

rc2   : rebuildCurve2   [boolean] ['query', 'edit']
    A boolean to determine if input curve 2 should be rebuilt (with curvature continuity).   Default: false

-----------------------------------------

rc3   : rebuildCurve3   [boolean] ['query', 'edit']
    A boolean to determine if input curve 3 should be rebuilt (with curvature continuity).   Default: false

-----------------------------------------

rc4   : rebuildCurve4   [boolean] ['query', 'edit']
    A boolean to determine if input curve 4 should be rebuilt (with curvature continuity).   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def stitchSurface(q=1,e=1,b="float",cch=1,ci="int",cj="int",fb=1,nds="int",u="float",v="float",pc=1,sc="int",tc=1,tpn=1,tpp=1,tt=1,tol="linear",c=1,ch=1,kg0=1,kg1=1,n="string",ns="int",o=1,rpo=1,wt0="float",wt1="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/stitchSurface.html



-----------------------------------------

stitchSurface is undoable, queryable, and editable.

The stitchSurface command aligns two surfaces together to be G(0) and/or G(1)
continuous by ajusting only the Control Vertices of the surfaces. The two
surfaces can be stitched by specifying the two isoparm boundary edges that are
to stitched together. The edge to which the two surfaces are stitched together
is obtained by doing a weighted average of the two edges. The weights for the
two edges is specified using the flags -wt0, -wt1 respectively.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : bias            [float] ['query', 'edit']
    Blend CVs in between input surface and result from stitch. A value of 0.0 returns the input surface.   Default: 1.0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ci    : cvIthIndex      [int] ['query', 'edit']
    The ith boundary CV index on the input surface.   Default: -1

-----------------------------------------

cj    : cvJthIndex      [int] ['query', 'edit']
    The jth boundary CV index on the input surface.   Default: -1

-----------------------------------------

fb    : fixBoundary     [boolean] ['query', 'edit']
    Fix Boundary CVs while solving for any G1 constraints.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

u     : parameterU      [float] ['query', 'edit']
    The U parameter value on surface for a point constraint.   Default: -10000

-----------------------------------------

v     : parameterV      [float] ['query', 'edit']
    The V parameter value on surface for a point constraint.   Default: -10000

-----------------------------------------

pc    : positionalContinuity [boolean] ['query', 'edit']
    Toggle on (off) G0 continuity at edge corresponding to multi index.   Default: true

-----------------------------------------

sc    : stepCount       [int] ['query', 'edit']
    Step count for the number of discretizations.   Default: 20

-----------------------------------------

tc    : tangentialContinuity [boolean] ['query', 'edit']
    Toggle on (off) G1 continuity across edge corresponding to multi index.   Default: false

-----------------------------------------

tpn   : togglePointNormals [boolean] ['query', 'edit']
    Toggle on (off) normal point constraints on the surface.   Default: false

-----------------------------------------

tpp   : togglePointPosition [boolean] ['query', 'edit']
    Toggle on (off) position point constraints on the surface.   Default: true

-----------------------------------------

tt    : toggleTolerance [boolean] ['query', 'edit']
    Toggle on (off) so as to use Tolerance or specified steps for discretization.   Default: false

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance to use while discretizing the edge.   Default: 0.1

-----------------------------------------

c     : cascade         [boolean] []
    Cascade the created stitch node. (Only if the surface has a stitch history)   Default is 'false'.

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

kg0   : keepG0Continuity [boolean] []
    Stitch together with positional continuity.   Default is 'true'.

-----------------------------------------

kg1   : keepG1Continuity [boolean] []
    Stitch together with tangent continuity.   Default is 'false'.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

ns    : numberOfSamples [int] []
    The number of samples on the edge.   Default is 20.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean] []
    Create "in place" (i.e., replace).

-----------------------------------------

wt0   : weight0         [float] []
    The weighting factor for the first edge.   Default is 0.5.

-----------------------------------------

wt1   : weight1         [float]
    The weighting factor for the second edge.   Default is 0.5.

    """

def stitchSurfacePoints(q=1,e=1,b="float",cch=1,ci="int",cj="int",fb=1,nds="int",u="float",v="float",pc=1,sc="int",tc=1,tpn=1,tpp=1,tt=1,tol="linear",c=1,ch=1,ewt=1,kg0=1,kg1=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/stitchSurfacePoints.html



-----------------------------------------

stitchSurfacePoints is undoable, queryable, and editable.

The stitchSurfacePoints command aligns two or more surface points along the
boundaries together to a single point. In the process, a node to average the
points is created. The points are averaged together in a weighted fashion. The
points may be control vertices along the boundaries. If the points are CVs
then they are stitched together only with positional continuity.

Note: No two points can lie on the same surface.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : bias            [float] ['query', 'edit']
    Blend CVs in between input surface and result from stitch. A value of 0.0 returns the input surface.   Default: 1.0

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ci    : cvIthIndex      [int] ['query', 'edit']
    The ith boundary CV index on the input surface.   Default: -1

-----------------------------------------

cj    : cvJthIndex      [int] ['query', 'edit']
    The jth boundary CV index on the input surface.   Default: -1

-----------------------------------------

fb    : fixBoundary     [boolean] ['query', 'edit']
    Fix Boundary CVs while solving for any G1 constraints.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

u     : parameterU      [float] ['query', 'edit']
    The U parameter value on surface for a point constraint.   Default: -10000

-----------------------------------------

v     : parameterV      [float] ['query', 'edit']
    The V parameter value on surface for a point constraint.   Default: -10000

-----------------------------------------

pc    : positionalContinuity [boolean] ['query', 'edit']
    Toggle on (off) G0 continuity at edge corresponding to multi index.   Default: true

-----------------------------------------

sc    : stepCount       [int] ['query', 'edit']
    Step count for the number of discretizations.   Default: 20

-----------------------------------------

tc    : tangentialContinuity [boolean] ['query', 'edit']
    Toggle on (off) G1 continuity across edge corresponding to multi index.   Default: false

-----------------------------------------

tpn   : togglePointNormals [boolean] ['query', 'edit']
    Toggle on (off) normal point constraints on the surface.   Default: false

-----------------------------------------

tpp   : togglePointPosition [boolean] ['query', 'edit']
    Toggle on (off) position point constraints on the surface.   Default: true

-----------------------------------------

tt    : toggleTolerance [boolean] ['query', 'edit']
    Toggle on (off) so as to use Tolerance or specified steps for discretization.   Default: false

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance to use while discretizing the edge.   Default: 0.1

-----------------------------------------

c     : cascade         [boolean] []
    Cascade the created stitch node. (Only if the surface has a stitch history)   Default is 'false'.

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

ewt   : equalWeight     [boolean] []
    Assign equal weights to all the points being stitched together.   Default is 'true'. If false, the first point is assigned a weight of 1.0 and the rest are assigned 0.0.

-----------------------------------------

kg0   : keepG0Continuity [boolean] []
    Stitch together the points with positional continuity.   Default is 'true'.

-----------------------------------------

kg1   : keepG1Continuity [boolean] []
    Stitch together the points with tangent continuity.   Default is 'false'.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def surface(du="int",dv="int",fu="string",fv="string",ku="float",kv="float",n="string",ob=1,p="[linear, linear, linear]",pw="[linear, linear, linear, linear]",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/surface.html



-----------------------------------------

surface is undoable, NOT queryable, and NOT editable.

The cmd creates a NURBS spline surface (rational or non rational). The surface
is created by specifying control vertices (CV's) and knot sequences in the U
and V direction. You cannot query the properties of the surface using this
command. See examples below.


-----------------------------------------


Return Value:

string  The path to the new surface


-----------------------------------------


Flags:

-----------------------------------------

du    : degreeU         [int] []
    Degree in surface U direction. Default is degree 3.

-----------------------------------------

dv    : degreeV         [int] []
    Degree in surface V direction. Default is degree 3.

-----------------------------------------

fu    : formU           [string] []
    The string for open is "open" , for closed is "closed" or for periodic is "periodic" in U.

-----------------------------------------

fv    : formV           [string] []
    The string for open is "open" , for closed is "closed" or for periodic is "periodic" in V.

-----------------------------------------

ku    : knotU           [float] []
    Knot value(s) in U direction. One flag per knot value. There must be (numberOfPointsInU + degreeInU - 1) knots and the knot vector must be non- decreasing.

-----------------------------------------

kv    : knotV           [float] []
    Knot value(s) in V direction. One flag per knot value. There must be (numberOfPointsInV + degreeInV - 1) knots and the knot vector must be non- decreasing.

-----------------------------------------

n     : name            [string] []
    Name to use for new transforms.

-----------------------------------------

ob    : objectSpace     [boolean] []
    Should the operation happen in objectSpace?

-----------------------------------------

p     : point           [[linear, linear, linear]] []
    To specify non rational CV with (x, y, z) values. "linear" means that this flag can take values with units. Note that you must specify (degree+1) surface points in any direction to create a visible surface span. eg. if the surface is degree 3 in the U direction, you must specify 4 CVs in the U direction. Points are specified in rows of U and columns of V. If you want to incorporate units, add the unit name to the value, eg. "-p 3.3in 5.5ft 6.6yd"

-----------------------------------------

pw    : pointWeight     [[linear, linear, linear, linear]] []
    To specify rational CV with (x, y, z, w) values. "linear" means that this flag can take values with units. Note that you must specify (degree+1) surface points in any direction to create a visible surface span. eg. if the surface is degree 3 in the U direction, you must specify 4 CVs in the U direction. Points are specified in rows of U and columns of V.

-----------------------------------------

ws    : worldSpace      [boolean]
    Should the operation happen in worldSpace?

    """

def tolerance(q=1,a="angle",l="linear"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/tolerance.html



-----------------------------------------

tolerance is undoable, queryable, and NOT editable.

This command sets tolerances used by modelling operations that require a
tolerance, such as surface fillet. Linear tolerance is also known as
"positional" tolerance. Angular tolerance is also known as "tangential"
tolerance.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angular         [angle] ['query']
    Sets the angular, or "tangential" tolerance.

-----------------------------------------

l     : linear          [linear]
    Sets the linear, or "positonal" tolerance.

    """

def torus(q=1,e=1,ax="[linear, linear, linear]",cch=1,d="int",esw="angle",hr="float",msw="angle",nds="int",p="[linear, linear, linear]",r="linear",s="int",nsp="int",ssw="angle",tol="linear",ut=1,ch=1,n="string",o=1,po="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/torus.html



-----------------------------------------

torus is undoable, queryable, and editable.

The torus command creates a new torus and/or a dependency node that creates
one, and returns their names.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ax    : axis            [[linear, linear, linear]] ['query', 'edit']
    The primitive's axis

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting surface: 1 - linear, 3 - cubic   Default: 3

-----------------------------------------

esw   : endSweep        [angle] ['query', 'edit']
    The angle at which to end the surface of revolution. Default is 2Pi radians, or 360 degrees.   Default: 6.2831853

-----------------------------------------

hr    : heightRatio     [float] ['query', 'edit']
    Ratio of "height" to "width"   Default: 2.0

-----------------------------------------

msw   : minorSweep      [angle] ['query', 'edit']
    The sweep angle for the minor circle in the torus   Default: 6.2831853

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : pivot           [[linear, linear, linear]] ['query', 'edit']
    The primitive's pivot point

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    The radius of the object   Default: 1.0

-----------------------------------------

s     : sections        [int] ['query', 'edit']
    The number of sections determines the resolution of the surface in the sweep direction. Used only if useTolerance is false.   Default: 8

-----------------------------------------

nsp   : spans           [int] ['query', 'edit']
    The number of spans determines the resolution of the surface in the opposite direction.   Default: 1

-----------------------------------------

ssw   : startSweep      [angle] ['query', 'edit']
    The angle at which to start the surface of revolution   Default: 0

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to build the surface. Used only if useTolerance is true   Default: 0.01

-----------------------------------------

ut    : useTolerance    [boolean] ['query', 'edit']
    Use the specified tolerance to determine resolution. Otherwise number of sections will be used.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

po    : polygon         [int]
    The value of this argument controls the type of the object created by this operation    * 0: nurbs surface   * 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)   * 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)   * 3: Bezier surface   * 4: subdivision surface solid (use nurbsToSubdivPref to set the parameters for the conversion)

    """

def trim(q=1,e=1,cch=1,lu="float",lv="float",nds="int",sl="int",sh=1,tol="linear",ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/trim.html



-----------------------------------------

trim is undoable, queryable, and editable.

This command trims a surface to its curves on surface by first splitting the
surface and then selecting which regions to keep or discard.


-----------------------------------------


Return Value:

string[]  Object name and node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

lu    : locatorU        [float] ['query', 'edit']
    u parameter value to position a locator on the surface.   Default: 0.5

-----------------------------------------

lv    : locatorV        [float] ['query', 'edit']
    v parameter value to position a locator on the surface.   Default: 0.5

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

sl    : selected        [int] ['query', 'edit']
    Specify whether to keep or discard selected regions.   Default: 0

-----------------------------------------

sh    : shrink          [boolean] ['query', 'edit']
    If true, shrink underlying surface to outer boundaries of trimmed surface.   Default: false

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to trim.   Default: 0.001

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def untrim(q=1,e=1,cch=1,nds="int",ch=1,cos=1,n="string",nc=1,o=1,rpo=1,all=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/untrim.html



-----------------------------------------

untrim is undoable, queryable, and editable.

Untrim the surface.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nc    : noChanges       [boolean] ['query', 'edit']
    If set then the operation node will be automatically put into pass- through mode.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean] []
    Create "in place" (i.e., replace).

-----------------------------------------

all   : untrimAll       [boolean]
    if true, untrim all the trims for the surface else untrim only the last trim

    """

def alignCurve(q=1,e=1,cch=1,cc=1,cs1="float",cs2="float",jnp="float",nds="int",pc=1,pct="int",rv1=1,rv2=1,tc=1,tct="int",ts1="float",ts2="float",at=1,ch=1,kmk=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/alignCurve.html



-----------------------------------------

alignCurve is undoable, queryable, and editable.

The curve align command is used to align curves in maya. The main alignment
options are positional, tangent and curvature continuity. Curvature continuity
implies tangent continuity.

Positional continuity means the curves (move) or the ends of the curves
(modify) are changed.

Tangent continuity means one of the curves is modified to be tangent at the
points where they meet.

Curvature continuity means one of the curves is modified to be curvature
continuous as well as tangent.

The default behaviour, when no curves or flags are passed, is to only do
positional and tangent continuity on the active list with the end of the first
curve and the start of the other curve used for alignment.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cc    : curvatureContinuity [boolean] ['query', 'edit']
    Curvature continuity is on if true and off otherwise.   Default: false

-----------------------------------------

cs1   : curvatureScale1 [float] ['query', 'edit']
    Curvature scale applied to curvature of first curve for curvature continuity.   Default: 0.0

-----------------------------------------

cs2   : curvatureScale2 [float] ['query', 'edit']
    Curvature scale applied to curvature of second curve for curvature continuity.   Default: 0.0

-----------------------------------------

jnp   : joinParameter   [float] ['query', 'edit']
    Parameter on reference curve where modified curve is to be aligned to.   Default: 123456.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pc    : positionalContinuity [boolean] ['query', 'edit']
    Positional continuity is on if true and off otherwise.   Default: true

-----------------------------------------

pct   : positionalContinuityType [int] ['query', 'edit']
    Positional continuity type legal values: 1 - move first curve, 2 - move second curve, 3 - move both curves, 4 - modify first curve, 5 - modify second curve, 6 - modify both curves   Default: 1

-----------------------------------------

rv1   : reverse1        [boolean] ['query', 'edit']
    If true, reverse the first input curve before doing align. Otherwise, do nothing to the first input curve before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

rv2   : reverse2        [boolean] ['query', 'edit']
    If true, reverse the second input curve before doing align. Otherwise, do nothing to the second input curve before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

tc    : tangentContinuity [boolean] ['query', 'edit']
    Tangent continuity is on if true and off otherwise.   Default: true

-----------------------------------------

tct   : tangentContinuityType [int] ['query', 'edit']
    Tangent continuity type legal values: 1 - do tangent continuity on first curve, 2 - do tangent continuity on second curve   Default: 1

-----------------------------------------

ts1   : tangentScale1   [float] ['query', 'edit']
    Tangent scale applied to tangent of first curve for tangent continuity.   Default: 1.0

-----------------------------------------

ts2   : tangentScale2   [float] ['query', 'edit']
    Tangent scale applied to tangent of second curve for tangent continuity.   Default: 1.0

-----------------------------------------

at    : attach          [boolean] []
    True if the curve is to be attached

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

kmk   : keepMultipleKnots [boolean] []
    True if multiple knots should be left as-is.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def arclen(q=1,e=1,cch=1,ch=1,nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/arclen.html



-----------------------------------------

arclen is undoable, queryable, and editable.

This command returns the arclength of a curve if the history flag is not set
(the default). If the history flag is set, a node is created that can produce
the arclength, and is connected and its name returned. Having the construction
history option on makes this command useful for expressions.


-----------------------------------------


Return Value:

float  Length in non history mode.    
string  Node name, in history mode.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def arcLengthDimension():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/arcLengthDimension.html



-----------------------------------------

arcLengthDimension is undoable, NOT queryable, and NOT editable.

This command is used to create an arcLength dimension to display the arcLength
of a curve/surface at a specified point on the curve/surface.


-----------------------------------------


Return Value:

string  Name of the arcLengthDimension node created
    """

def attachCurve(q=1,e=1,bb="float",bki=1,cch=1,kmk=1,m="int",nds="int",p="float",rv1=1,rv2=1,ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/attachCurve.html



-----------------------------------------

attachCurve is undoable, queryable, and editable.

This attach command is used to attach curves. Once the curves are attached,
there will be multiple knots at the joined point(s). These can be kept or
removed if the user wishes.

If there are two curves, the end of the first curve is attached to the start
of the second curve. If there are more than two curves, closest endpoints are
joined.

Note: if the command is done with Keep Original off, the first curve is
replaced by the attached curve. All other curves will remain, the command does
not delete them.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bb    : blendBias       [float] ['query', 'edit']
    Skew the result toward the first or the second curve depending on the blend factory being smaller or larger than 0.5.   Default: 0.5

-----------------------------------------

bki   : blendKnotInsertion [boolean] ['query', 'edit']
    If set to true, insert a knot in one of the original curves (relative position given by the parameter attribute below) in order to produce a slightly different effect.   Default: false

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

kmk   : keepMultipleKnots [boolean] ['query', 'edit']
    If true, keep multiple knots at the join parameter. Otherwise remove them.   Default: true

-----------------------------------------

m     : method          [int] ['query', 'edit']
    Attach method (connect-0, blend-1)   Default: 0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    The parameter value for the positioning of the newly inserted knot.   Default: 0.1

-----------------------------------------

rv1   : reverse1        [boolean] ['query', 'edit']
    If true, reverse the first input curve before doing attach. Otherwise, do nothing to the first input curve before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

rv2   : reverse2        [boolean] ['query', 'edit']
    If true, reverse the second input curve before doing attach. Otherwise, do nothing to the second input curve before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def circle(q=1,e=1,cch=1,c="[linear, linear, linear]",cx="linear",cy="linear",cz="linear",d="int",fp="[linear, linear, linear]",fpx="linear",fpy="linear",fpz="linear",fc=1,nds="int",nr="[linear, linear, linear]",nrx="linear",nry="linear",nrz="linear",r="linear",s="int",sw="angle",tol="linear",ut=1,ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/circle.html



-----------------------------------------

circle is undoable, queryable, and editable.

The circle command creates a circle or partial circle (arc)


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

c     : center          [[linear, linear, linear]] ['query', 'edit']
    The center point of the circle.

-----------------------------------------

cx    : centerX         [linear] ['query', 'edit']
    X of the center point.   Default: 0

-----------------------------------------

cy    : centerY         [linear] ['query', 'edit']
    Y of the center point.   Default: 0

-----------------------------------------

cz    : centerZ         [linear] ['query', 'edit']
    Z of the center point.   Default: 0

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting circle: 1 - linear, 3 - cubic   Default: 3

-----------------------------------------

fp    : first           [[linear, linear, linear]] ['query', 'edit']
    The start point of the circle if fixCenter is false. Determines the orientation of the circle if fixCenter is true.

-----------------------------------------

fpx   : firstPointX     [linear] ['query', 'edit']
    X of the first point.   Default: 1

-----------------------------------------

fpy   : firstPointY     [linear] ['query', 'edit']
    Y of the first point.   Default: 0

-----------------------------------------

fpz   : firstPointZ     [linear] ['query', 'edit']
    Z of the first point.   Default: 0

-----------------------------------------

fc    : fixCenter       [boolean] ['query', 'edit']
    Fix the center of the circle to the specified center point. Otherwise the circle will start at the specified first point.   Default: true

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nr    : normal          [[linear, linear, linear]] ['query', 'edit']
    The normal of the plane in which the circle will lie.

-----------------------------------------

nrx   : normalX         [linear] ['query', 'edit']
    X of the normal direction.   Default: 0

-----------------------------------------

nry   : normalY         [linear] ['query', 'edit']
    Y of the normal direction.   Default: 0

-----------------------------------------

nrz   : normalZ         [linear] ['query', 'edit']
    Z of the normal direction.   Default: 1

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    The radius of the circle.   Default: 1.0

-----------------------------------------

s     : sections        [int] ['query', 'edit']
    The number of sections determines the resolution of the circle. Used only if useTolerance is false.   Default: 8

-----------------------------------------

sw    : sweep           [angle] ['query', 'edit']
    The sweep angle determines the completeness of the circle. A full circle is 2Pi radians, or 360 degrees.   Default: 6.2831853

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to build a circle. Used only if useTolerance is true   Default: 0.01

-----------------------------------------

ut    : useTolerance    [boolean] ['query', 'edit']
    Use the specified tolerance to determine resolution. Otherwise number of sections will be used.   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def closeCurve(q=1,e=1,bb="float",bki=1,cch=1,nds="int",p="float",ps="int",ch=1,cos=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/closeCurve.html



-----------------------------------------

closeCurve is undoable, queryable, and editable.

The closeCurve command closes a curve, making it periodic. The pathname to the
newly closed curve and the name of the resulting dependency node are returned.
If a curve is not specified in the command, then the first active curve will
be used.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

bb    : blendBias       [float] ['query', 'edit']
    Skew the result toward the first or the second curve depending on the blend value being smaller or larger than 0.5.   Default: 0.5

-----------------------------------------

bki   : blendKnotInsertion [boolean] ['query', 'edit']
    If set to true, insert a knot in one of the original curves (relative position given by the parameter attribute below) in order to produce a slightly different effect.   Default: false

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    The parameter value for the positioning of the newly inserted knot.   Default: 0.1

-----------------------------------------

ps    : preserveShape   [int] ['query', 'edit']
    0 - without preserving the shape 1 - preserve shape 2 - blend   Default: 1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def curve(a=1,bez=1,d="float",ep="[linear, linear, linear]",k="float",n="string",os=1,per=1,p="[linear, linear, linear]",pw="[linear, linear, linear, float]",r=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curve.html



-----------------------------------------

curve is undoable, NOT queryable, and NOT editable.

The curve command creates a new curve from a list of control vertices (CVs). A
string is returned containing the pathname to the newly created curve. You can
create a curve from points either in world space or object (local) space,
either with weights or without. You can replace an existing curve by using the
"-r/replace" flag. You can append a point to an existing curve by using the
"-a/append" flag.

To create a curve-on-surface, use the curveOnSurface command.

To change the degree of a curve, use the rebuildCurve command.

To change the of parameter range curve, use the rebuildCurve command.


-----------------------------------------


Return Value:

string  The path to the new curve or the replaced curve


-----------------------------------------


Flags:

-----------------------------------------

a     : append          [boolean] []
    Appends point(s) to the end of an existing curve. If you use this flag, you must specify the name of the curve to append to, at the end of the command. (See examples below.)

-----------------------------------------

bez   : bezier          [boolean] []
    The created curve will be a bezier curve.

-----------------------------------------

d     : degree          [float] []
    The degree of the new curve. Default is 3. Note that you need (degree+1) curve points to create a visible curve span. eg. you must place 4 points for a degree 3 curve.

-----------------------------------------

ep    : editPoint       [[linear, linear, linear]] []
    The x, y, z position of an edit point. "linear" means that this flag can take values with units. This flag can not be used with the -point or the -pointWeight flags.

-----------------------------------------

k     : knot            [float] []
    A knot value in a knot vector. One flag per knot value. There must be (numberOfPoints + degree - 1) knots and the knot vector must be non- decreasing.

-----------------------------------------

n     : name            [string] []
    Name of the curve

-----------------------------------------

os    : objectSpace     [boolean] []
    Points are in object, or "local" space. This is the default. You cannot specify both "-os" and "-ws" in the same command.

-----------------------------------------

per   : periodic        [boolean] []
    If on, creates a curve that is periodic. Default is off.

-----------------------------------------

p     : point           [[linear, linear, linear]] []
    The x, y, z position of a point. "linear" means that this flag can take values with units.

-----------------------------------------

pw    : pointWeight     [[linear, linear, linear, float]] []
    The x,y,z and w values of a point, where the w is a weight value. A rational curve will be created if this flag is used. "linear" means that this flag can take values with units.

-----------------------------------------

r     : replace         [boolean] []
    Replaces an entire existing curve. If you use this flag, you must specify the name of the curve to replace, at the end of the command. (See examples below.)

-----------------------------------------

ws    : worldSpace      [boolean]
    Points are in world space. The default is "-os". You cannot specify both "-os" and "-ws" in the same command.

    """

def curveIntersect(q=1,e=1,cch=1,ch=1,d="[linear, linear, linear]",dx="linear",dy="linear",dz="linear",nds="int",tol="linear",ud=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveIntersect.html



-----------------------------------------

curveIntersect is undoable, queryable, and editable.

You must specify two curves to intersect.

This command either returns the parameter values at which the given pair of
curves intersect, or returns a dependency node that provides the intersection
information. If you want to find the intersection of the curves in a specific
direction you must use BOTH the "-useDirection" flag and the "direction" flag.


-----------------------------------------


Return Value:

string  the parameter values at which two curves intersect.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

d     : direction       [[linear, linear, linear]] ['query', 'edit']
    The direction that the input curves are projected in before intersecting. This vector is only used if "useDirection" flag is true.

-----------------------------------------

dx    : directionX      [linear] ['query', 'edit']
    The X component of the direction that the input curves are projected in before intersecting. This vector is only used if "useDirection" flag is true.

-----------------------------------------

dy    : directionY      [linear] ['query', 'edit']
    The Y component of the direction that the input curves are projected in before intersecting. This vector is only used if "useDirection" flag is true.

-----------------------------------------

dz    : directionZ      [linear] ['query', 'edit']
    The Z component of the direction that the input curves are projected in before intersecting. This vector is only used if "useDirection" flag is true.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance that the intersection is calculated with. For example, given two curves end-to-end, the ends must be within tolerance for an intersection to be returned.   Default: 0.001

-----------------------------------------

ud    : useDirection    [boolean]
    If true, use direction flag. The input curves are first projected in a specified direction and then intersected. If false, this command will only find true 3D intersections.   Default: false

    """

def curveOnSurface(a=1,d="float",k="float",n="string",per=1,uv="[float, float]",r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/curveOnSurface.html



-----------------------------------------

curveOnSurface is undoable, NOT queryable, and NOT editable.

The curve command creates a new curve from a list of control vertices (CVs). A
string is returned containing the pathname to the newly created curve. You can
create a curve from points either in world space or object (local) space,
either with weights or without. You can replace an existing curve by using the
"-r/replace" flag. You can append a point to an existing curve by using the
"-a/append" flag.

To create a curve-on-surface, use the curveOnSurface command.

To change the degree of a curve, use the rebuildCurve command.

To change the of parameter range curve, use the rebuildCurve command.

The curve-on-surface command creates a new curve-on-surface from a list of
control vertices (CVs). A string is returned containing the pathname to the
newly created curve-on-surface. You can replace an existing curve by using the
"-r/replace" flag. You can append points to an existing curve-on-surface by
using the "-a/append" flag. See also the curve command, which describes how to
query curve attributes.


-----------------------------------------


Return Value:

string  \- name of new curve-on-surface    
string  The path to the new curve or the replaced curve


-----------------------------------------


Flags:

-----------------------------------------

a     : append          [boolean] []
    Appends point(s) to the end of an existing curve. If you use this flag, you must specify the name of the curve to append to, at the end of the command. (See examples below.)

-----------------------------------------

d     : degree          [float] []
    The degree of the new curve. Default is 3. Note that you need (degree+1) curve points to create a visible curve span. eg. you must place 4 points for a degree 3 curve.

-----------------------------------------

k     : knot            [float] []
    A knot value in a knot vector. One flag per knot value. There must be (numberOfPoints + degree - 1) knots and the knot vector must be non- decreasing.

-----------------------------------------

n     : name            [string] []
    Name of the curve

-----------------------------------------

per   : periodic        [boolean] []
    If on, creates a curve that is periodic. Default is off.

-----------------------------------------

uv    : positionUV      [[float, float]] []
    The uv position of a point.

-----------------------------------------

r     : replace         [boolean]
    Replaces an entire existing curve. If you use this flag, you must specify the name of the curve to replace, at the end of the command. (See examples below.)

    """

def detachCurve(q=1,e=1,cch=1,k=1,nds="int",p="float",ch=1,cos=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/detachCurve.html



-----------------------------------------

detachCurve is undoable, queryable, and editable.

The detachCurve command detaches a curve into pieces, given a list of
parameter values. You can also specify which pieces to keep and which to
discard using the "-k" flag. The names of the newly detached curve(s) is
returned. If history is on, then the name of the resulting dependency node is
also returned.

You can use this command to open a periodic curve at a particular parameter
value. You would use this command with only one "-p" flag.

If you are specifying "-k" flags, then you must specify one, none or all "-k"
flags. If you are specifying all "-k" flags, there must be one more "-k" flag
than "-p" flags.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

k     : keep            [boolean] ['query', 'edit']
    Whether or not to keep a detached piece. This multi attribute should be one element larger than the parameter multi attribute.   Default: true

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    Parameter values to detach at   Default: 0.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def duplicateCurve(q=1,e=1,cch=1,ch=1,l=1,max="float",mi=1,min="float",n="string",nds="int",rn=1,r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/duplicateCurve.html



-----------------------------------------

duplicateCurve is undoable, queryable, and editable.

The duplicateCurve command takes a curve on a surface and and returns the 3D
curve. The curve on a surface could be isoparam component, trimmed edge or
curve on surface object.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

l     : local           [boolean] []
    Copy the transform of the surface and connect to the local space version instead.

-----------------------------------------

max   : maxValue        [float] ['query', 'edit']
    Maximum parameter value for the curve segment. Must be greater than or equal to the minValue attribute. If relative is true, then this attribute has maximum value of 1.0.   Default: -1.0

-----------------------------------------

mi    : mergeItems      [boolean] []
    Merge component results where possible. For example, instead of returning a[1] and a[2], return a[1:2].

-----------------------------------------

min   : minValue        [float] ['query', 'edit']
    Minimum parameter value for the curve segment If relative is true, then this attribute has minimum value of 0.0.   Default: 1.0

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rn    : range           [boolean] []
    Force a curve range on complete input curve.

-----------------------------------------

r     : relative        [boolean]
    True means use a relative parameter range, from 0.0 to 1.0. Otherwise, the parameter values are absolute values.   Default: false

    """

def extendCurve(q=1,e=1,cch=1,d="linear",em="int",et="int",ip="[linear, linear, linear]",jn=1,nds="int",px="linear",py="linear",pz="linear",rmk=1,s="int",ch=1,cos=1,n="string",nc=1,o=1,rn=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/extendCurve.html



-----------------------------------------

extendCurve is undoable, queryable, and editable.

This command extends a curve or creates a new curve as an extension


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : distance        [linear] ['query', 'edit']
    The distance to extend Used only for extendMethod is byDistance.   Default: 1

-----------------------------------------

em    : extendMethod    [int] ['query', 'edit']
    The method with which to extend: 0 - based on distance, 2 - to a 3D point   Default: 0

-----------------------------------------

et    : extensionType   [int] ['query', 'edit']
    The type of extension: 0 - linear, 1 - circular, 2 - extrapolate   Default: 0

-----------------------------------------

ip    : inputPoint      [[linear, linear, linear]] ['query', 'edit']
    The point to extend to (optional)

-----------------------------------------

jn    : join            [boolean] ['query', 'edit']
    If true, join the extension to original curve   Default: true

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

px    : pointX          [linear] ['query', 'edit']
    X of the point to extend to   Default: 0

-----------------------------------------

py    : pointY          [linear] ['query', 'edit']
    Y of the point to extend to   Default: 0

-----------------------------------------

pz    : pointZ          [linear] ['query', 'edit']
    Z of the point to extend to   Default: 0

-----------------------------------------

rmk   : removeMultipleKnots [boolean] ['query', 'edit']
    If true remove multiple knots at join Used only if join is true.   Default: false

-----------------------------------------

s     : start           [int] ['query', 'edit']
    Which end of the curve to extend. 0 - end, 1 - start, 2 - both   Default: 1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nc    : noChanges       [boolean] ['query', 'edit']
    If set then the operation node will be automatically put into pass- through mode.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rn    : range           [boolean] []
    Force a curve range on complete input curve.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def filletCurve(q=1,e=1,b="linear",bc=1,cch=1,cir=1,cp1="float",cp2="float",d="linear",fb=1,nds="int",r="linear",ch=1,jn=1,n="string",o=1,rpo=1,t=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/filletCurve.html



-----------------------------------------

filletCurve is undoable, queryable, and editable.

The curve fillet command creates a fillet curve between two curves. If no
objects are specified in the command line, then the first two active curves
are used. The fillet created can be circular (with a radius) or freeform (with
a type of tangent or blend).


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

b     : bias            [linear] ['query', 'edit']
    Adjusting the bias value causes the fillet curve to be skewed to one of the input curves. Available only if blendControl is true.   Default: 0.0

-----------------------------------------

bc    : blendControl    [boolean] ['query', 'edit']
    If true then depth and bias can be controlled. Otherwise, depth and bias are not available options.   Default: false

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cir   : circular        [boolean] ['query', 'edit']
    Curve fillet will be created as circular if true or freeform if false.   Default: true

-----------------------------------------

cp1   : curveParameter1 [float] ['query', 'edit']
    Parameter where fillet curve will contact the primary input curve.   Default: 0.0

-----------------------------------------

cp2   : curveParameter2 [float] ['query', 'edit']
    Parameter where fillet curve will contact the secondary input curve.   Default: 0.0

-----------------------------------------

d     : depth           [linear] ['query', 'edit']
    Adjusts the depth of the fillet curve. Available only if blendControl is true.   Default: 0.5

-----------------------------------------

fb    : freeformBlend   [boolean] ['query', 'edit']
    The freeform type is blend if true or tangent if false. Available if the fillet type is freeform.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

r     : radius          [linear] ['query', 'edit']
    The radius if creating a circular fillet.   Default: 1.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

jn    : join            [boolean] []
    Should the fillet be joined?

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean] []
    Create "in place" (i.e., replace).

-----------------------------------------

t     : trim            [boolean]
    Should the fillet be trimmed?

    """

def fitBspline(q=1,e=1,cch=1,nds="int",tol="linear",ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fitBspline.html



-----------------------------------------

fitBspline is undoable, queryable, and editable.

The fitBspline command fits the CVs from an input curve and and returns a 3D
curve.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance for the fit. The resulting curve will be kept within tolerance of the given points.   Default: 0.1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def hardenPointCurve(q=1,e=1,cch=1,m="int",nds="int",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/hardenPointCurve.html



-----------------------------------------

hardenPointCurve is undoable, queryable, and editable.

The hardenPointCurve command changes the knots of a curve given a list of
control point indices so that the knot corresponding to that control point
gets the specified multiplicity. Multiplicity of -1 is the universal value
used for multiplicity equal to the degree of the curve.

limitations  
The CV whose multiplicity is being raised needs to have its neighbouring CVs
of multiplicity 1. How many neighbours depends on the degree of the curve and
the difference in CV multiplicities before and after this operation. For
example, if you're changing a CV of multiplicity 1 into a CV of multiplicity
3, you will need the 4 neighbouring CVs (2 on each side) to be of multiplicity
1. The CVs that do not satisfy that requirement will be ignored.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

m     : multiplicity    [int] ['query', 'edit']
    the required multiplicity of the curve knot   Default: -1

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def illustratorCurves(q=1,e=1,cch=1,ch=1,ifn="string",nds="int",o=1,tl="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/illustratorCurves.html



-----------------------------------------

illustratorCurves is undoable, queryable, and editable.

The illustratorCurves command creates NURBS curves from an input Adobe(R)
Illustrator(R) file.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

ifn   : illustratorFilename [string] []
    Input Adobe(R) Illustrator(R) file name.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

tl    : tolerance       [float]
    CVs on the output curve get snapped if the distance between two contiguous CVs are lesser than this tolerance value.   Default: 0.001f

    """

def insertKnotCurve(q=1,e=1,add=1,cch=1,ib=1,nds="int",nk="int",p="float",ch=1,cos=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/insertKnotCurve.html



-----------------------------------------

insertKnotCurve is undoable, queryable, and editable.

The insertKnotCurve command inserts knots into a curve given a list of
parameter values. The number of knots to add at each parameter value and
whether the knots are added or complemented can be specified. The name of the
curve is returned. If construction history is on, the name of the resulting
dependency node is also returned.

An edit point will appear where you insert the knot. Also, the number of spans
and CVs in the curve will increase in the area where the knot is inserted.

You can insert up to "degree" knots at a curve parameter that isn't already an
edit point. eg. for a degree three curve, you can insert up to 3 knots.

Use this operation if you need more CVs in a local area of the curve. Use this
operation (or "hardenPoint") if you want to create a corner in a curve.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addKnots        [boolean] ['query', 'edit']
    Whether to add knots or complement. Complement means knots will be added to reach the specified number of knots.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ib    : insertBetween   [boolean] ['query', 'edit']
    If set to true, and there is more than one parameter value specified, the knots will get inserted at equally spaced intervals between the given parameter values, rather than at the parameter values themselves.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nk    : numberOfKnots   [int] ['query', 'edit']
    How many knots to insert. At any point on the curve, there can be a maximum of "degree" knots.   Default: 1

-----------------------------------------

p     : parameter       [float] ['query', 'edit']
    Parameter value(s) where knots are added   Default: 0.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def nurbsSquare(q=1,e=1,cch=1,c="[linear, linear, linear]",cx="linear",cy="linear",cz="linear",d="int",nds="int",nr="[linear, linear, linear]",nrx="linear",nry="linear",nrz="linear",sl1="linear",sl2="linear",sps="int",ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsSquare.html



-----------------------------------------

nurbsSquare is undoable, queryable, and editable.

The nurbsSquare command creates a square


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

c     : center          [[linear, linear, linear]] ['query', 'edit']
    The center point of the square.

-----------------------------------------

cx    : centerX         [linear] ['query', 'edit']
    X of the center point.   Default: 0

-----------------------------------------

cy    : centerY         [linear] ['query', 'edit']
    Y of the center point.   Default: 0

-----------------------------------------

cz    : centerZ         [linear] ['query', 'edit']
    Z of the center point.   Default: 0

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting circle: 1 - linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic   Default: 3

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nr    : normal          [[linear, linear, linear]] ['query', 'edit']
    The normal of the plane in which the square will lie.

-----------------------------------------

nrx   : normalX         [linear] ['query', 'edit']
    X of the normal direction.   Default: 0

-----------------------------------------

nry   : normalY         [linear] ['query', 'edit']
    Y of the normal direction.   Default: 0

-----------------------------------------

nrz   : normalZ         [linear] ['query', 'edit']
    Z of the normal direction.   Default: 1

-----------------------------------------

sl1   : sideLength1     [linear] ['query', 'edit']
    The length of a side on the square.   Default: 1.0

-----------------------------------------

sl2   : sideLength2     [linear] ['query', 'edit']
    The length of an adjacent side on the square.   Default: 1.0

-----------------------------------------

sps   : spansPerSide    [int] ['query', 'edit']
    The number of spans per side determines the resolution of the square.   Default: 1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def offsetCurve(q=1,e=1,cch=1,cb="int",cl=1,cr="linear",d="linear",nds="int",nr="[linear, linear, linear]",rp=1,st=1,sd="int",tol="linear",ugn=1,ch=1,n="string",o=1,rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/offsetCurve.html



-----------------------------------------

offsetCurve is undoable, queryable, and editable.

The offset command creates new offset curves from the selected curves. The
connecting type for breaks in offsets is off (no connection), circular
(connect with an arc) or linear (connect linearly resulting in a sharp
corner). If loop cutting is on then any loops in the offset curves are trimmed
away. For the default cut radius of 0.0 a sharp corner is created at each
intersection. For values greater than 0.0 a small arc of that radius is
created at each intersection. The cut radius value is only valid when loop
cutting is on. Offsets (for planar curves) are calculated in the plane of that
curve and 3d curves are offset in 3d. The subdivisionDensity flag is the
maximum number of times the offset object can be subdivided (i.e. calculate
the offset until the offset comes within tolerance or the iteration reaches
this maximum.) The reparameterize option allows the offset curve to have a
different parameterization to the original curve. This avoids uneven parameter
distributions in the offset curve that can occur with large offsets of curves,
but is more expensive to compute.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cb    : connectBreaks   [int] ['query', 'edit']
    Connect breaks method (between gaps): 0 - off, 1 - circular, 2 - linear   Default: 2

-----------------------------------------

cl    : cutLoop         [boolean] ['query', 'edit']
    Do loop cutting.   Default: false

-----------------------------------------

cr    : cutRadius       [linear] ['query', 'edit']
    Loop cut radius. Only used if cutLoop attribute is set true.   Default: 0.0

-----------------------------------------

d     : distance        [linear] ['query', 'edit']
    Offset distance   Default: 1.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

nr    : normal          [[linear, linear, linear]] ['query', 'edit']
    Offset plane normal

-----------------------------------------

rp    : reparameterize  [boolean] ['query', 'edit']
    Do reparameterization. It is not advisable to change this value.   Default: false

-----------------------------------------

st    : stitch          [boolean] ['query', 'edit']
    Stitch curve segments together. It is not advisable to change this value.   Default: true

-----------------------------------------

sd    : subdivisionDensity [int] ['query', 'edit']
    Maximum subdivision density per span   Default: 5

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance   Default: 0.01

-----------------------------------------

ugn   : useGivenNormal  [boolean] ['query', 'edit']
    Use the given normal (or, alternativelly, geometry normal)   Default: 1

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def offsetCurveOnSurface(q=1,e=1,cch=1,cp="int",cb="int",cl=1,d="linear",nds="int",st=1,sd="int",tol="linear",ch=1,n="string",o=1,rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/offsetCurveOnSurface.html



-----------------------------------------

offsetCurveOnSurface is undoable, queryable, and editable.

The offsetCurveOnSurface command offsets a curve on surface resulting in
another curve on surface. The connecting type for breaks in offsets is off (no
connection), circular (connect with an arc) or linear (connect linearly
resulting in a sharp corner). If loop cutting is on then any loops in the
offset curves are trimmed away and a sharp corner is created at each
intersection. The subdivisionDensity flag is the maximum number of times the
offset object can be subdivided (i.e. calculate the offset until the offset
comes within tolerance or the iteration reaches this maximum.) The checkPoints
flag sets the number of points per span at which the distance of the offset
curve from the original curve is determined. The tolerance flag determines how
accurately the offset curve should satisfy the required offset distance. A
satisfactory offset curve is one for which all of the checkpoints are within
the given tolerance of the required offset.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cp    : checkPoints     [int] ['query', 'edit']
    Checkpoints for fit quality per span. Not advisable to change this value.   Default: 3

-----------------------------------------

cb    : connectBreaks   [int] ['query', 'edit']
    Connect breaks method (between gaps): 0 - off, 1 - circular, 2 - linear   Default: 2

-----------------------------------------

cl    : cutLoop         [boolean] ['query', 'edit']
    Do loop cutting.   Default: false

-----------------------------------------

d     : distance        [linear] ['query', 'edit']
    Offset distance   Default: 1.0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

st    : stitch          [boolean] ['query', 'edit']
    Stitch curve segments together. Not advisable to change this value.   Default: true

-----------------------------------------

sd    : subdivisionDensity [int] ['query', 'edit']
    Maximum subdivision density per span   Default: 5

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    Tolerance   Default: 0.01

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rn    : range           [boolean]
    Force a curve range on complete input curve.

    """

def pointCurveConstraint(q=1,e=1,cch=1,nds="int",puv="[float, float, float]",pw="float",p="[float, float, float]",w="float",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pointCurveConstraint.html



-----------------------------------------

pointCurveConstraint is undoable, queryable, and editable.

The command enables direct manipulation of a NURBS curve. It does so by apply
a position constraint at the specified parameter location on the NURBS curve.

If construction history for the cmd is enabled, a locator is created to enable
subsequent interactive manipulation of the curve. The locator position may be
key framed or transformed and the "curve1" will try to match the position of
the locator.

The argument is a curve location


-----------------------------------------


Return Value:

string[]  Object Name(s), node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

puv   : pointConstraintUVW [[float, float, float]] ['query', 'edit']
    Point constraint parameter space location on input NURBS Object

-----------------------------------------

pw    : pointWeight     [float] ['query', 'edit']
    Point constraint weight. Determines how strong an influence the constraint has on the input NURBS object.   Default: 1.0

-----------------------------------------

p     : position        [[float, float, float]] []
    The new desired position in space for the nurbs object at the specified parameter space component. If not specified, the position is taken to be the one evaluated at the parameter space component on the nurbs object.

-----------------------------------------

w     : weight          [float] []
    weight of the lsq constraint. The larger the weight, the least squares constraint is strictly met.

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def pointOnCurve(q=1,e=1,cch=1,ch=1,cc=1,cr=1,nds="int",no=1,nn=1,nt=1,pr="float",p=1,t=1,top=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pointOnCurve.html



-----------------------------------------

pointOnCurve is undoable, queryable, and editable.

This command returns information for a point on a NURBS curve. If no flag is
specified, it assumes p/position by default.


-----------------------------------------


Return Value:

float[3]  Vector query result    
float  Single float query result  
string  String query result  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cc    : curvatureCenter [boolean] []
    Returns the (x,y,z) center of curvature of the specified point on the curve

-----------------------------------------

cr    : curvatureRadius [boolean] []
    Returns the radius of curvature of the specified point on the curve

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

no    : normal          [boolean] []
    Returns the (x,y,z) normal of the specified point on the curve

-----------------------------------------

nn    : normalizedNormal [boolean] []
    Returns the (x,y,z) normalized normal of the specified point on the curve

-----------------------------------------

nt    : normalizedTangent [boolean] []
    Returns the (x,y,z) normalized tangent of the specified point on the curve

-----------------------------------------

pr    : parameter       [float] ['query', 'edit']
    The parameter value on curve   Default: 0.0

-----------------------------------------

p     : position        [boolean] []
    Returns the (x,y,z) position of the specified point on the curve

-----------------------------------------

t     : tangent         [boolean] []
    Returns the (x,y,z) tangent of the specified point on the curve

-----------------------------------------

top   : turnOnPercentage [boolean]
    Whether the parameter is normalized (0,1) or not   Default: false

    """

def projectTangent(q=1,e=1,cch=1,c=1,cs="linear",ie=1,nds="int",rt=1,ro="angle",td="int",ts="linear",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/projectTangent.html



-----------------------------------------

projectTangent is undoable, queryable, and editable.

The project tangent command is used to align (for tangents) a curve to two
other curves or a surface. A surface isoparm may be selected to define the
direction (U or V) to align to. The end of the curve must intersect with these
other objects. Curvature continuity may also be applied if required.

Tangent continuity means the end of the curve is modified to be tangent at the
point it meets the other objects.

Curvature continuity means the end of the curve is modified to be curvature
continuous as well as tangent.

If the normal tangent direction is used, the curvature continuity and rotation
do not apply. Also, curvature continuity is only available if align to a
surface (not with 2 curves).


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

c     : curvature       [boolean] ['query', 'edit']
    Curvature continuity is on if true and off otherwise.   Default: false

-----------------------------------------

cs    : curvatureScale  [linear] ['query', 'edit']
    Curvature scale applied to curvature of curve to align. Available if curvature option is true.   Default: 0.0

-----------------------------------------

ie    : ignoreEdges     [boolean] ['query', 'edit']
    If false, use the tangents of the trim edge curves if the surface is trimmed. If true, use the tangents of the underlying surface in the U/V directions.   Default: false

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rt    : reverseTangent  [boolean] ['query', 'edit']
    Reverse the tangent direction if true and leave it the way it is if false.   Default: false

-----------------------------------------

ro    : rotate          [angle] ['query', 'edit']
    Amount by which the tangent of the curve to align will be rotated. Available only if the normal direction (3) is not used for tangentDirection.   Default: 0.0

-----------------------------------------

td    : tangentDirection [int] ['query', 'edit']
    Tangent align direction type legal values: 1=u direction (of surface or use first curve), 2=v direction (of surface or use second curve), 3=normal direction (at point of intersection).   Default: 1

-----------------------------------------

ts    : tangentScale    [linear] ['query', 'edit']
    Tangent scale applied to tangent of curve to align.   Default: 1.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def rebuildCurve(q=1,e=1,cch=1,d="int",end="int",fr=1,kcp=1,kep=1,kr="int",kt=1,nds="int",rt="int",scr=1,s="int",tol="linear",ch=1,n="string",o=1,rn=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rebuildCurve.html



-----------------------------------------

rebuildCurve is undoable, queryable, and editable.

This command rebuilds a curve by modifying its parameterization. In some cases
the shape may also change. The rebuildType (-rt) determines how the curve is
to be rebuilt.

The optional second curve can be used to specify a reference parameterization.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

d     : degree          [int] ['query', 'edit']
    The degree of the resulting curve 1 - linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic   Default: 3

-----------------------------------------

end   : endKnots        [int] ['query', 'edit']
    End conditions for the curve 0 - uniform end knots, 1 - multiple end knots,   Default: 0

-----------------------------------------

fr    : fitRebuild      [boolean] ['query', 'edit']
    If true use the least squares fit rebuild. Otherwise use the convert method.   Default: true

-----------------------------------------

kcp   : keepControlPoints [boolean] ['query', 'edit']
    If true, the CVs will remain the same. This forces uniform parameterization unless rebuildType is matchKnots.   Default: false

-----------------------------------------

kep   : keepEndPoints   [boolean] ['query', 'edit']
    If true, keep the endpoints the same.   Default: true

-----------------------------------------

kr    : keepRange       [int] ['query', 'edit']
    Determine the parameterization for the resulting curve. 0 - reparameterize the resulting curve from 0 to 1, 1 - keep the original curve parameterization, 2 - reparameterize the result from 0 to number of spans   Default: 1

-----------------------------------------

kt    : keepTangents    [boolean] ['query', 'edit']
    If true, keep the end tangents the same.   Default: true

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

rt    : rebuildType     [int] ['query', 'edit']
    How to rebuild the input curve. 0 - uniform, 1 - reduce spans, 2 - match knots, 3 - remove multiple knots, 4 - curvature 5 - rebuild ends 6 - clean   Default: 0

-----------------------------------------

scr   : smartSurfaceCurveRebuild [boolean] ['query', 'edit']
    If true, curve on surface is rebuild in 3D and 2D info is kept   Default: false

-----------------------------------------

s     : spans           [int] ['query', 'edit']
    The number of spans in resulting curve Used only if rebuildType is uniform.   Default: 4

-----------------------------------------

tol   : tolerance       [linear] ['query', 'edit']
    The tolerance with which to rebuild.   Default: 0.01

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rn    : range           [boolean] []
    Force a curve range on complete input curve.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def reverseCurve(q=1,e=1,cch=1,nds="int",ch=1,cos=1,n="string",o=1,rn=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/reverseCurve.html



-----------------------------------------

reverseCurve is undoable, queryable, and editable.

The reverseCurve command reverses the direction of a curve or curve-on-
surface. A string is returned containing the pathname of the newly reversed
curve and the name of the resulting dependency node. The reversed curve has
the same parameter range as the original curve.


-----------------------------------------


Return Value:

string[]  (object name and node name)    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cos   : curveOnSurface  [boolean] []
    If possible, create 2D curve as a result.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rn    : range           [boolean] []
    Force a curve range on complete input curve.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def smoothCurve(q=1,e=1,cch=1,nds="int",s="float",ch=1,n="string",o=1,rpo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/smoothCurve.html



-----------------------------------------

smoothCurve is undoable, queryable, and editable.

The smooth command smooths the curve at the given control points.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

s     : smoothness      [float] ['query', 'edit']
    smoothness factor   Default: 10.0

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rpo   : replaceOriginal [boolean]
    Create "in place" (i.e., replace).

    """

def textCurves(q=1,e=1,f="string",n="string",o=1,t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/textCurves.html



-----------------------------------------

textCurves is undoable, queryable, and editable.

The textCurves command creates NURBS curves from a text string using the
specified font.

A single letter can be made up of more than one NURBS curve. The number of
curves per letter varies with the font.


-----------------------------------------


Return Value:

string[]  Object name and node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

f     : font            [string] []
    The font to use.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

t     : text            [string]
    The string to create the curves for.

    """

def changeSubdivComponentDisplayLevel(q=1,l="int",r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/changeSubdivComponentDisplayLevel.html



-----------------------------------------

changeSubdivComponentDisplayLevel is undoable, queryable, and NOT editable.

Explicitly forces the subdivision surface to display components at a
particular level of refinement.


-----------------------------------------


Return Value:

int  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

l     : level           [int] ['query']
    Specifies the display level of components.

-----------------------------------------

r     : relative        [boolean]
    If set, level refers to the relative display level

    """

def changeSubdivRegion(a="int",l="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/changeSubdivRegion.html



-----------------------------------------

changeSubdivRegion is undoable, NOT queryable, and NOT editable.

Changes a subdivision surface region based on the command parameters. The
command operates on the selected subdivision surfaces.


-----------------------------------------


Return Value:

boolean  Command result


-----------------------------------------


Flags:

-----------------------------------------

a     : action          [int] []
    Specifies the action to the selection region 1 = delete selection region 2 = enlarge selection region

-----------------------------------------

l     : level           [int]
    Specify the level of the subdivision surface to perform the operation

    """

def coarsenSubdivSelectionList():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/coarsenSubdivSelectionList.html



-----------------------------------------

coarsenSubdivSelectionList is undoable, NOT queryable, and NOT editable.

Coarsens a subdivision surface set of components based on the selection list.
The selected components are selected at a coarser level.


-----------------------------------------


Return Value:

boolean  Command result
    """

def createSubdivRegion():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/createSubdivRegion.html



-----------------------------------------

createSubdivRegion is undoable, NOT queryable, and NOT editable.

Creates a subdivision surface region based on the selection list. Once a
selection region is created, only the components in the selection list or
converted from the selection list will be displayed and selectible through the
UI.


-----------------------------------------


Return Value:

boolean  Command result
    """

def nurbsToSubdiv(q=1,e=1,aut=1,cch=1,cp=1,ch=1,mp=1,mpc="int",n="string",nds="int",o=1,rn=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsToSubdiv.html



-----------------------------------------

nurbsToSubdiv is undoable, queryable, and editable.

This command converts a NURBS surface and produces a subd surface. The name of
the new subdivision surface is returned. If construction history is ON, then
the name of the new dependency node is returned as well.


-----------------------------------------


Return Value:

string[]  The subd surface and optionally the dependency node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

aut   : addUnderTransform [boolean] ['query', 'edit']
    Specify whether the new surface should be added under the old transform or not.

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cp    : collapsePoles   [boolean] ['query', 'edit']
    Collapse poles into a single point   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

mp    : matchPeriodic   [boolean] ['query', 'edit']
    Match periodic surface texture mapping in the result.   Default: false

-----------------------------------------

mpc   : maxPolyCount    [int] ['query', 'edit']
    The maximum number of base mesh faces in the resulting subdivision surface.   Default: 1000

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

o     : object          [boolean] []
    Create the result, or just the dependency node.

-----------------------------------------

rn    : reverseNormal   [boolean]
    Reverse the NURBS surface normal in the conversion.   Default: true

    """

def nurbsToSubdivPref(q=1,br="int",ct="int",cp=1,mp=1,mpc="int",o="linear",rn=1,st="int",t00="float",t01="float",t02="float",t10="float",t11="float",t12="float",t20="float",t21="float",t22="float",t30="float",t31="float",t32="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nurbsToSubdivPref.html



-----------------------------------------

nurbsToSubdivPref is undoable, queryable, and NOT editable.

This command sets the values used by the nurbs-to-subdivision surface
preference. This preference is used by the nurbs creation commands and is
saved between Maya sessions.

To query any of the flags, use the "-query" flag.

For more information on the flags, see the node documentation for the
"nurbsToSubdivProc" node.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

br    : bridge          [int] ['query']
    Valid values are 0, 1, 2 or 3.

-----------------------------------------

ct    : capType         [int] ['query']
    Valid values are 0 or 1.

-----------------------------------------

cp    : collapsePoles   [boolean] ['query']
    

-----------------------------------------

mp    : matchPeriodic   [boolean] ['query']
    

-----------------------------------------

mpc   : maxPolyCount    [int] ['query']
    

-----------------------------------------

o     : offset          [linear] ['query']
    

-----------------------------------------

rn    : reverseNormal   [boolean] ['query']
    

-----------------------------------------

st    : solidType       [int] ['query']
    Valid values are 0, 1 or 2.

-----------------------------------------

t00   : trans00         [float] ['query']
    

-----------------------------------------

t01   : trans01         [float] ['query']
    

-----------------------------------------

t02   : trans02         [float] ['query']
    

-----------------------------------------

t10   : trans10         [float] ['query']
    

-----------------------------------------

t11   : trans11         [float] ['query']
    

-----------------------------------------

t12   : trans12         [float] ['query']
    

-----------------------------------------

t20   : trans20         [float] ['query']
    

-----------------------------------------

t21   : trans21         [float] ['query']
    

-----------------------------------------

t22   : trans22         [float] ['query']
    

-----------------------------------------

t30   : trans30         [float] ['query']
    

-----------------------------------------

t31   : trans31         [float] ['query']
    

-----------------------------------------

t32   : trans32         [float]
    

    """

def polyToSubdiv(q=1,e=1,ap=1,amr=1,cch=1,me="int",mpc="int",nds="int",pvo=1,qc=1,uvp="[float, float]",uvu="float",uvv="float",uvt="int",aut=1,ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/polyToSubdiv.html



-----------------------------------------

polyToSubdiv is undoable, queryable, and editable.

This command converts a polygon and produces a subd surface. The name of the
new subdivision surface is returned. If construction history is ON, then the
name of the new dependency node is returned as well.


-----------------------------------------


Return Value:

string  \- the subdivision and optionally the dependency node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ap    : absolutePosition [boolean] ['query', 'edit']
    If true, the possible blind data information that comes from the polygon will be treated as absolute positions of the vertices, instead of the relative offsets. You most likelly just want to use the default of false, unless you know that the blind data has the absolute positions in it.   Default: false

-----------------------------------------

amr   : applyMatrixToResult [boolean] ['query', 'edit']
    If true, the matrix on the input geometry is applied to the object and the resulting geometry will have identity matrix on it. If false the conversion is done on the local space object and the resulting geometry has the input object's matrix on it.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

me    : maxEdgesPerVert [int] ['query', 'edit']
    The maximum allowed valence for a vertex on the input mesh   Default: 32

-----------------------------------------

mpc   : maxPolyCount    [int] ['query', 'edit']
    The maximum number of polygons accepted on the input mesh.   Default: 1000

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

pvo   : preserveVertexOrdering [boolean] ['query', 'edit']
    Preserve vertex ordering in conversion   Default: true

-----------------------------------------

qc    : quickConvert    [boolean] ['query', 'edit']
    Debug flag to test the performance   Default: true

-----------------------------------------

uvp   : uvPoints        [[float, float]] ['query', 'edit']
    This is a cached uv point needed to transfer uv data associated with finer level vertices (when switching between standard editing mode and poly proxy mode.

-----------------------------------------

uvu   : uvPointsU       [float] ['query', 'edit']
    U value of a cached uv point

-----------------------------------------

uvv   : uvPointsV       [float] ['query', 'edit']
    V value of a cached uv point

-----------------------------------------

uvt   : uvTreatment     [int] ['query', 'edit']
    Treatment of Subd UVs when in proxy mode:    * 0 - preserve Subd UVs   * 1 - build Subd UVs from Poly UVs   * 2 - no UVs on Subd     Default: 0

-----------------------------------------

aut   : addUnderTransform [boolean] []
    If true then add the new subdivision surface under the poly's transform.

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def querySubdiv(a="int",l="int",r=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/querySubdiv.html



-----------------------------------------

querySubdiv is undoable, NOT queryable, and NOT editable.

Queries a subdivision surface based on a set of query parameters and updates
the selection list with the results.


-----------------------------------------


Return Value:

boolean  Command result


-----------------------------------------


Flags:

-----------------------------------------

a     : action          [int] []
    Specifies the query parameter: 1 = find all tweaked verticies at level 2 = find all sharpened vertices at level 3 = find all sharpened edges at level 4 = find all faces at level If the attribute "level" is not specified then the query is applied to the current component display level. If the attribute level is specified then the query is applied to that level, either absolute or relative to the current level based on the "relative" flag state.

-----------------------------------------

l     : level           [int] []
    Specify the level of the subdivision surface on which to perform the operation.

-----------------------------------------

r     : relative        [boolean]
    If set, level flag refers to the level relative to the current component display level.

    """

def refineSubdivSelectionList():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/refineSubdivSelectionList.html



-----------------------------------------

refineSubdivSelectionList is undoable, NOT queryable, and NOT editable.

Refines a subdivision surface set of components based on the selection list.
The selected components are subdivided. The selection list after the command
is the newly created components at the finer subdivision level.


-----------------------------------------


Return Value:

boolean  Command result
    """

def subdAutoProjection(q=1,e=1,cch=1,nds="int",ch=1,l="int",lm="int",n="string",o="int",ps="float",p="int",sc="int",si=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdAutoProjection.html



-----------------------------------------

subdAutoProjection is undoable, queryable, and editable.

Projects a texture map onto an object, using several orthogonal projections
simultaneously.

The argument is a face selection list.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

l     : layout          [int] ['query', 'edit']
    What layout algorithm should be used:   0 UV pieces are aligned along the U axis.   1 UV pieces are moved in a square shape.

-----------------------------------------

lm    : layoutMethod    [int] ['query', 'edit']
    Which layout method to use:   0 Block Stacking.   1 Shape Stacking.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : optimize        [int] ['query', 'edit']
    Use two different flavors for the cut generation.   0 Every face is assigned to the best plane. This optimizes the map distortion.   1 Small UV pieces are incorporated into larger ones, when the extra distortion introduced is reasonable. This tends to produce fewer UV pieces.

-----------------------------------------

ps    : percentageSpace [float] ['query', 'edit']
    When layout is set to square, this value is a percentage of the texture area which is added around each UV piece. It can be used to ensure each UV piece uses different pixels in the texture.   Maximum value is 5 percent.

-----------------------------------------

p     : planes          [int] ['query', 'edit']
    Number of intermediate projections used. Valid numbers are 4, 5, 6, 8, and 12.   C: Default is 6.

-----------------------------------------

sc    : scale           [int] ['query', 'edit']
    How to scale the pieces, after projections:   0 No scale is applied.   1 Uniform scale to fit in unit square.   2 Non proportional scale to fit in unit square.

-----------------------------------------

si    : skipIntersect   [boolean] ['query', 'edit']
    When on, self intersection of UV pieces are not tested. This makes the projection faster and produces fewer pieces, but may lead to overlaps in UV space.

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is "off".

    """

def subdCleanTopology():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdCleanTopology.html



-----------------------------------------

subdCleanTopology is undoable, NOT queryable, and NOT editable.

Command cleans topology of subdiv surfaces - at all levels. It cleans the
geometry of vertices that satisfy the following conditions: \- Zero edits \-
Default uvs (uvs obtained by subdividing parent face). \- No creases.


-----------------------------------------


Return Value:

boolean  Success or Failure.
    """

def subdCollapse(q=1,e=1,cch=1,l="int",nds="int",ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdCollapse.html



-----------------------------------------

subdCollapse is undoable, queryable, and editable.

This command converts a takes a subdivision surface, passed as the argument,
and produces a subdivision surface with a number of hierarchy levels
"removed". Returns the name of the subdivision surface created and optionally
the DG node that does the conversion.


-----------------------------------------


Return Value:

string[]  The subd surface and optionally the dependency node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

l     : level           [int] ['query', 'edit']
    The level that will now become the base mesh.   Default: 0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def subdDuplicateAndConnect():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdDuplicateAndConnect.html



-----------------------------------------

subdDuplicateAndConnect is undoable, NOT queryable, and NOT editable.

This command duplicates the input subdivision surface object, connects up the
outSubdiv attribute of the original subd shape to the create attribute of the
newly created duplicate shape and copies over the shader assignments from the
original shape to the new duplicated shape.

The command will fail if no objects are selected or sent as argument or if the
object sent as argument is not a subdivision surface object.


-----------------------------------------


Return Value:

None
    """

def subdEditUV(q=1,a="float",pu="float",pv="float",r=1,rr="float",rot=1,s=1,su="float",sv="float",u="float",uvs="string",v="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdEditUV.html



-----------------------------------------

subdEditUV is undoable, queryable, and NOT editable.

Command edits uvs on subdivision surfaces. When used with the query flag, it
returns the uv values associated with the specified components.


-----------------------------------------


Return Value:

boolean  Success or Failure.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : angle           [float] ['query']
    Specifies the angle value (in degrees) that the uv values are to be rotated by.

-----------------------------------------

pu    : pivotU          [float] ['query']
    Specifies the pivot value, in the u direction, about which the scale or rotate is to be performed.

-----------------------------------------

pv    : pivotV          [float] ['query']
    Specifies the pivot value, in the v direction, about which the scale or rotate is to be performed.

-----------------------------------------

r     : relative        [boolean] ['query']
    Specifies whether this command is editing the values relative to the currently existing values. Default is true;

-----------------------------------------

rr    : rotateRatio     [float] ['query']
    Specifies the ratio value that the uv values are to be rotated by Default is 1.0

-----------------------------------------

rot   : rotation        [boolean] ['query']
    Specifies whether this command is editing the values with rotation values

-----------------------------------------

s     : scale           [boolean] ['query']
    Specifies whether this command is editing the values with scale values

-----------------------------------------

su    : scaleU          [float] ['query']
    Specifies the scale value in the u direction.

-----------------------------------------

sv    : scaleV          [float] ['query']
    Specifies the scale value in the v direction.

-----------------------------------------

u     : uValue          [float] ['query']
    Specifies the value, in the u direction - absolute if relative flag is false..

-----------------------------------------

uvs   : uvSetName       [string] ['query']
    Specifies the name of the uv set to edit uvs on. If not specified will use the current uv set if it exists.

-----------------------------------------

v     : vValue          [float]
    Specifies the value, in the v direction - absolute if relative flag is false..

    """

def subdiv(q=1,cl=1,csl=1,dl="int",dsl=1,est=1,fst=1,mpl="int",pm="int",so=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdiv.html



-----------------------------------------

subdiv is undoable, queryable, and NOT editable.

Provides useful information about the selected subdiv or components, such as
the deepest subdivided level, the children or parents of the currently
selected components, etc.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cl    : currentLevel    [boolean] ['query']
    When queried, this flag returns an integer representing the level of the currently selected subdiv surface component(s). Returns -1, if there are more than one level of CVs are selected, (even if they are from different objects) Returns -2, if there are no input subdiv CVs to process.

-----------------------------------------

csl   : currentSubdLevel [boolean] ['query']
    When queried, this flag returns an integer representing the level of the currently selected subdiv surface, regardless of whether components are selected or not. Returns -2, if there are no input subdiv CVs to process.

-----------------------------------------

dl    : deepestLevel    [int] ['query']
    When queried, this flag returns an integer representing the deepest level to which the queried subdiv surface has been subdivided.

-----------------------------------------

dsl   : displayLoad     [boolean] ['query']
    When queried, this flag prints the display load of selected subdiv

-----------------------------------------

est   : edgeStats       [boolean] ['query']
    When queried, this flag prints stats on the current subd.

-----------------------------------------

fst   : faceStats       [boolean] ['query']
    When queried, this flag prints stats on the current subd.

-----------------------------------------

mpl   : maxPossibleLevel [int] ['query']
    When queried, this flag returns an integer representing the maximum possible level to which the queried subdiv surface can been subdivided.

-----------------------------------------

pm    : proxyMode       [int] ['query']
    When queried, this flag returns an integer representing whether or not the subdivision surface is in "polygon proxy" mode. "Proxy" mode allows the base mesh of a subdivision surface without construction history to be edited using the polygonal editing tools. Returns 1, if the subdivision surface is in "polygon proxy" mode. Returns 0, if the surface is not currently in "proxy" mode, but could be put into "proxy" mode since it has no construction history. (This state is also known as "standard" mode.) Returns 2, if the surface is not in "proxy" mode and cannot be put into proxy mode, as it has construction history.

-----------------------------------------

so    : smallOffsets    [boolean]
    When queried, this flag prints the number of subdiv vertices in the hierarchy that have a small enough offset so that the vertex is not required

    """

def subdivCrease(sh=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdivCrease.html



-----------------------------------------

subdivCrease is undoable, NOT queryable, and NOT editable.

Set the creasing on subdivision mesh edges or mesh points that are on the
selection list.


-----------------------------------------


Return Value:

boolean  Command result


-----------------------------------------


Flags:

-----------------------------------------

sh    : sharpness       [boolean]
    Specifies the sharpness value to set the crease to

    """

def subdivDisplaySmoothness(q=1,all=1,s="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdivDisplaySmoothness.html



-----------------------------------------

subdivDisplaySmoothness is undoable, queryable, and NOT editable.

Sets or querys the display smoothness of subdivision surfaces on the selection
list or of all subdivision surfaces if the -all option is set. Smoothness
options are; rough, medium, or fine. Rough is the default.


-----------------------------------------


Return Value:

boolean  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

      : all             [boolean] ['query']
    If set, change smoothness for all subdivision surfaces

-----------------------------------------

s     : smoothness      [int]
    Smoothness - 1 rough, 2 medium, 3 fine

    """

def subdLayoutUV(q=1,e=1,cch=1,nds="int",ch=1,fr=1,l="int",lm="int",n="string",ps="float",rbf="int",sc="int",se="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdLayoutUV.html



-----------------------------------------

subdLayoutUV is undoable, queryable, and editable.

Move UVs in the texture plane to avoid overlaps.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

fr    : flipReversed    [boolean] ['query', 'edit']
    If this flag is turned on, the reversed UV pieces are fliped.

-----------------------------------------

l     : layout          [int] ['query', 'edit']
    How to move the UV pieces, after cuts are applied:   0 No move is applied.   1 Layout the pieces along the U axis.   2 Layout the pieces in a square shape.

-----------------------------------------

lm    : layoutMethod    [int] ['query', 'edit']
    Which layout method to use:   0 Block Stacking.   1 Shape Stacking.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

ps    : percentageSpace [float] ['query', 'edit']
    When layout is set to square, this value is a percentage of the texture area which is added around each UV piece. It can be used to ensure each UV piece uses different pixels in the texture.   Maximum value is 5 percent.

-----------------------------------------

rbf   : rotateForBestFit [int] ['query', 'edit']
    0 No rotation is applied. 1 Only allow 90 degree rotations. 2 Allow free rotations.

-----------------------------------------

sc    : scale           [int] ['query', 'edit']
    How to scale the pieces, after move and cuts:   0 No scale is applied.   1 Uniform scale to fit in unit square.   2 Non proportional scale to fit in unit square.

-----------------------------------------

se    : separate        [int] ['query', 'edit']
    Which UV edges should be cut:   0 No cuts.   1 Cut only along folds.   2 Make all necessary cuts to avoid all intersections.

-----------------------------------------

ws    : worldSpace      [boolean]
    If true, performs the operation in world space coordinates as opposed to local space.

    """

def subdListComponentConversion(bo=1,fe=1,ff=1,fuv=1,fv=1,internal=1,te=1,tf=1,tuv=1,tv=1,uvs=1,uvb=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdListComponentConversion.html



-----------------------------------------

subdListComponentConversion is undoable, NOT queryable, and NOT editable.

This command converts subdivision surface components from one or more types to
another one or more types, and returns the list of the conversion. It does not
change the currently selected objects.

Use the "-in/internal" flag to specify conversion to "connected" vs.
"contained" components. For example, if the internal flag is specified when
converting from subdivision surface vertices to faces, then only faces that
are entirely contained by the vertices will be returned. If the internal flag
is not specified, then all faces that are connected to the vertices will be
returned.


-----------------------------------------


Return Value:

string[]  List of subdivision surface components


-----------------------------------------


Flags:

-----------------------------------------

bo    : border          [boolean] []
    Convert to a border.

-----------------------------------------

fe    : fromEdge        [boolean] []
    Indicates the component type to convert from: Edges

-----------------------------------------

ff    : fromFace        [boolean] []
    Indicates the component type to convert from: Faces

-----------------------------------------

fuv   : fromUV          [boolean] []
    Indicates the component type to convert from: UVs

-----------------------------------------

fv    : fromVertex      [boolean] []
    Indicates the component type to convert from: Vertex

-----------------------------------------

internal : internal        [boolean] []
    Applicable when converting from "smaller" component types to larger ones. Specifies conversion to "connected" vs. "contained" components. See examples below.

-----------------------------------------

te    : toEdge          [boolean] []
    Indicates the component type to convert to: Edges

-----------------------------------------

tf    : toFace          [boolean] []
    Indicates the component type to convert to: Faces

-----------------------------------------

tuv   : toUV            [boolean] []
    Indicates the component type to convert to: UVs

-----------------------------------------

tv    : toVertex        [boolean] []
    Indicates the component type to convert to: Vertices

-----------------------------------------

uvs   : uvShell         [boolean] []
    Will return UV components within the same UV shell. Only works with -tuv and -fuv flags.

-----------------------------------------

uvb   : uvShellBorder   [boolean]
    Will return UV components on the border within the same UV shell. Only works with -tuv and -fuv flags.

    """

def subdMapCut(q=1,e=1,cch=1,ch=1,n="string",nds="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdMapCut.html



-----------------------------------------

subdMapCut is undoable, queryable, and editable.

Cut along edges of the texture mapping. The cut edges become map borders.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nds   : nodeState       [int]
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

    """

def subdMapSewMove(q=1,e=1,cch=1,nds="int",ch=1,lps=1,n="string",nf="int",ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdMapSewMove.html



-----------------------------------------

subdMapSewMove is undoable, queryable, and editable.

This command can be used to Move and Sew together separate UV pieces along
geometric edges. UV pieces that correspond to the same geometric edge, are
merged together by moving the smaller piece to the larger one.

  
The argument is a UV selection list.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

lps   : limitPieceSize  [boolean] ['query', 'edit']
    When on, this flag specifies that the face number limit described above should be used.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

nf    : numberFaces     [int] ['query', 'edit']
    Maximum number of faces in a UV piece. When trying to combine two UV pieces into a single one, the merge operation is rejected if the smaller piece has more faces than the number specified by this flag.   This flag is only used when limitPieceSize is set to on.

-----------------------------------------

ws    : worldSpace      [boolean]
    If true, performs the operation in world space coordinates as opposed to local space.

    """

def subdMatchTopology(foc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdMatchTopology.html



-----------------------------------------

subdMatchTopology is undoable, NOT queryable, and NOT editable.

Command matches topology across multiple subdiv surfaces - at all levels.


-----------------------------------------


Return Value:

boolean  Success or Failure.


-----------------------------------------


Flags:

-----------------------------------------

foc   : frontOfChain    [boolean]
    This command is used to specify that the new addTopology node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the addTopology node will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added.

    """

def subdMirror(q=1,e=1,cch=1,nds="int",xm=1,ym=1,zm=1,ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdMirror.html



-----------------------------------------

subdMirror is undoable, queryable, and editable.

This command takes a subdivision surface, passed as the argument, and produces
a subdivision surface that is a mirror. Returns the name of the subdivision
surface created and optionally the DG node that does the mirroring.


-----------------------------------------


Return Value:

string[]  The subdivision surface and optionally the dependency node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

xm    : xMirror         [boolean] ['query', 'edit']
    Mirror the vertices in X   Default: false

-----------------------------------------

ym    : yMirror         [boolean] ['query', 'edit']
    Mirror the vertices in Y   Default: false

-----------------------------------------

zm    : zMirror         [boolean] ['query', 'edit']
    Mirror the vertices in Z   Default: false

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def subdPlanarProjection(q=1,e=1,cch=1,nds="int",ch=1,cm=1,ic2="[float, float]",icx="float",icy="float",is2="[float, float]",isu="float",isv="float",ibd=1,kir=1,md="string",n="string",pc="[linear, linear, linear]",pcx="linear",pcy="linear",pcz="linear",ph="linear",ps="[linear, linear]",pw="linear",ro="[angle, angle, angle]",rx="angle",ry="angle",rz="angle",ra="angle",sf=1,ws=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdPlanarProjection.html



-----------------------------------------

subdPlanarProjection is undoable, queryable, and editable.

TsubProjCmdBase is a base class for the command to create a mapping on the
selected subdivision faces. Projects a map onto an object, using an orthogonal
projection. The piece of the map defined from isu, isv, icx, icy area, is
placed at pcx, pcy, pcz location.


-----------------------------------------


Return Value:

string  The node name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

cm    : createNewMap    [boolean] ['query', 'edit']
    This flag when set true will create a new map with a the name passed in, if the map does not already exist.

-----------------------------------------

ic2   : imageCenter     [[float, float]] ['query', 'edit']
    This flag specifies the center point of the 2D model layout.   C: Default is 0.5 0.5.   Q: When queried, this flag returns a float[2].

-----------------------------------------

icx   : imageCenterX    [float] ['query', 'edit']
    This flag specifies X for the center point of the 2D model layout.   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

icy   : imageCenterY    [float] ['query', 'edit']
    This flag specifies Y for the center point of the 2D model layout.   C: Default is 0.5.   Q: When queried, this flag returns a float.

-----------------------------------------

is2   : imageScale      [[float, float]] ['query', 'edit']
    This flag specifies the UV scale : Enlarges or reduces the 2D version of the model in U or V space relative to the 2D centerpoint.   C: Default is 1.0 1.0.   Q: When queried, this flag returns a float[2].

-----------------------------------------

isu   : imageScaleU     [float] ['query', 'edit']
    This flag specifies the U scale : Enlarges or reduces the 2D version of the model in U space relative to the 2D centerpoint.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

isv   : imageScaleV     [float] ['query', 'edit']
    This flag specifies the V scale : Enlarges or reduces the 2D version of the model in V space relative to the 2D centerpoint.   C: Default is 1.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ibd   : insertBeforeDeformers [boolean] []
    This flag specifies if the projection node should be inserted before or after deformer nodes already applied to the shape. Inserting the projection after the deformer leads to texture swimming during animation and is most often undesirable.   C: Default is on.

-----------------------------------------

kir   : keepImageRatio  [boolean] []
    True means keep any image ratio

-----------------------------------------

md    : mapDirection    [string] []
    This flag specifies the mapping direction.   'x', 'y' and 'z' projects the map along the corresponding axis.   'c' projects along the current camera viewing direction.   'p' does perspective projection if current camera is perspective.   'b' projects along the best plane fitting the objects selected.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

pc    : projectionCenter [[linear, linear, linear]] ['query', 'edit']
    This flag specifies the origin point from which the map is projected.   C: Default is 0.0 0.0 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

pcx   : projectionCenterX [linear] ['query', 'edit']
    This flag specifies X for the origin point from which the map is projected.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pcy   : projectionCenterY [linear] ['query', 'edit']
    This flag specifies Y for the origin point from which the map is projected.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

pcz   : projectionCenterZ [linear] ['query', 'edit']
    This flag specifies Z for the origin point from which the map is projected.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ph    : projectionHeight [linear] ['query', 'edit']
    This flag specifies the height of the map relative to the 3D projection axis.   C: Default is 1.0   Q: When queried, this flag returns a float.

-----------------------------------------

ps    : projectionScale [[linear, linear]] ['query', 'edit']
    This flag specifies the width and the height of the map relative to the 3D projection axis.   C: Default is 1.0 1.0.   Q: When queried, this flag returns a float[2].

-----------------------------------------

pw    : projectionWidth [linear] ['query', 'edit']
    This flag specifies the width of the map relative to the 3D projection axis.   C: Default is 1.0   Q: When queried, this flag returns a float.

-----------------------------------------

ro    : rotate          [[angle, angle, angle]] ['query', 'edit']
    This flag specifies the mapping rotate angles.   C: Default is 0.0 0.0 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

rx    : rotateX         [angle] ['query', 'edit']
    This flag specifies X mapping rotate angle.   C: Default is 0.0.   Q: When queried, this flag returns a float[3].

-----------------------------------------

ry    : rotateY         [angle] ['query', 'edit']
    This flag specifies Y mapping rotate angle.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

rz    : rotateZ         [angle] ['query', 'edit']
    This flag specifies Z mapping rotate angle.   C: Default is 0.0.   Q: When queried, this flag returns a float.

-----------------------------------------

ra    : rotationAngle   [angle] ['query', 'edit']
    This flag specifies the rotation angle in the mapping space. When the angle is positive, then the map rotates counterclockwise on the mapped model, whereas when it is negative then the map rotates lockwise on the mapped model.   C: Default is 10.0.   Q: When queried, this flag returns a float.

-----------------------------------------

sf    : smartFit        [boolean] []
    True means use the smart fit algorithm

-----------------------------------------

ws    : worldSpace      [boolean]
    This flag specifies which reference to use. If "on" : all geometrical values are taken in world reference. If "off" : all geometrical values are taken in object reference.   C: Default is "off".   Q: When queried, this flag returns an int.

    """

def subdToBlind(ap=1,ic=1,izo=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdToBlind.html



-----------------------------------------

subdToBlind is undoable, NOT queryable, and NOT editable.

The subdivision surface hierarchical edits will get copied into blind data on
the given polygon. The polygon face count and topology must match the
subdivision surface base mesh face count and topology. If they don't, the
blind data will still appear, but is not guaranteed to produce the same result
when converted back to a subdivision surface.  
  
The command takes a single subdivision surface and a single polygonal object.
Additional subdivision surfaces or polygonal objects will be ignored.


-----------------------------------------


Return Value:

boolean  Command result


-----------------------------------------


Flags:

-----------------------------------------

ap    : absolutePosition [boolean] []
    If set to true, the hierarchical edits are represented as the point positions, not the point offsets. Most of the time, this is not desirable, but if you're just going to be merging/deleting a bunch of things and not move any vertices, then you could set it to true. False is the default and saves the offsets.

-----------------------------------------

ic    : includeCreases  [boolean] []
    If set, the creases get transfered as well. With it false, the subdivision surface created from the blind data + polygon will have lost all the craese information. The default is false.

-----------------------------------------

izo   : includeZeroOffsets [boolean]
    If set, the zero offset will get included in the blind data. This will greatly increase the size of the blind data, but will also let you keep all created vertices in the conversion back to polys. This flag does not change the behaviour for the vertices up to and including level 2 as they're always created. If not set, only the edited vertices will be included in the blind data. This will still maintain the shape of your object faithfully. The default is false.

    """

def subdToPoly(q=1,e=1,amr=1,cch=1,cut=1,d="int",epp=1,f="int",inSubdCVId="[int, int]",isl="int",isr="int",mp="int",nds="int",os="[int, int]",osl="int",osr="int",ov="int",pvo=1,sc="int",suv=1,un=1,aut=1,cs=1,ch=1,n="string",o=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdToPoly.html



-----------------------------------------

subdToPoly is undoable, queryable, and editable.

This command tessellates a subdivision surface and produces polygon. The name
of the new polygon is returned. If construction history is ON, then the name
of the new dependency node is returned as well.


-----------------------------------------


Return Value:

string[]  The polygon and optionally the dependency node name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

amr   : applyMatrixToResult [boolean] ['query', 'edit']
    If true, the matrix on the input geometry is applied to the object and the resulting geometry will have identity matrix on it. If false the conversion is done on the local space object and the resulting geometry has the input object's matrix on it.   Default: true

-----------------------------------------

cch   : caching         [boolean] ['query', 'edit']
    Toggle caching for all attributes so that no recomputation is needed

-----------------------------------------

cut   : copyUVTopology  [boolean] ['query', 'edit']
    Copy over uv topology (shared/unshared) from the original subdivision surface to the converted polygonal mesh.   Default: false

-----------------------------------------

d     : depth           [int] ['query', 'edit']
    The depth at which constant-depth tessellates the surface   Default: 0

-----------------------------------------

epp   : extractPointPosition [boolean] ['query', 'edit']
    Determines how the position of a mesh point is calculated If on the position of the mesh point is returned. If off the position of the point of the surface is returned.   Default: false

-----------------------------------------

f     : format          [int] ['query', 'edit']
    Format:    * 0 - Uniform   * 1 - Adaptive   * 2 - Polygon Count   * 3 - Vertices     Default: 0

-----------------------------------------

inSubdCVId : inSubdCVId      [[int, int]] ['query', 'edit']
    Input CV Id

-----------------------------------------

isl   : inSubdCVIdLeft  [int] ['query', 'edit']
    Higher 32 bit integer of the input CV Id

-----------------------------------------

isr   : inSubdCVIdRight [int] ['query', 'edit']
    Lower 32 bit integer of the input CV Id

-----------------------------------------

mp    : maxPolys        [int] ['query', 'edit']
    The maximum number of polygons at which by polygons tessellates. If this attribute is greater than zero, it will override the sample count and depth attributes.   Default: 0

-----------------------------------------

nds   : nodeState       [int] ['query', 'edit']
    Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.  The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.  The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute. Additional details about each of these 3 states follow.  | State | Description

-----------------------------------------

os    : outSubdCVId     [[int, int]] ['query', 'edit']
    Output CV Id

-----------------------------------------

osl   : outSubdCVIdLeft [int] ['query', 'edit']
    Higher 32 bit integer of the output CV Id

-----------------------------------------

osr   : outSubdCVIdRight [int] ['query', 'edit']
    Lower 32 bit integer of the output CV Id

-----------------------------------------

ov    : outv            [int] ['query', 'edit']
    Out Vertices corresponding to the inSubDCVs.

-----------------------------------------

pvo   : preserveVertexOrdering [boolean] ['query', 'edit']
    Preserve vertex ordering in conversion   Default: true

-----------------------------------------

sc    : sampleCount     [int] ['query', 'edit']
    The number of samples per face   Default: 1

-----------------------------------------

suv   : shareUVs        [boolean] ['query', 'edit']
    Force sharing of uvs on all common vertices - the value of this attribute gets overridden by the value of the copyUVTopology attribute.   Default: false

-----------------------------------------

un    : subdNormals     [boolean] ['query', 'edit']
    Keep subdiv surface normals   Default: false

-----------------------------------------

aut   : addUnderTransform [boolean] ['query']
    If true then add the result underneath a transform node

-----------------------------------------

cs    : connectShaders  [boolean] []
    If true, all shader assignment will be copied from the original subdiv surface to the converted polygonal surface.   Default: true

-----------------------------------------

ch    : constructionHistory [boolean] []
    Turn the construction history on or off.

-----------------------------------------

n     : name            [string] []
    Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.

-----------------------------------------

o     : object          [boolean]
    Create the result, or just the dependency node.

    """

def subdTransferUVsToCache():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/subdTransferUVsToCache.html



-----------------------------------------

subdTransferUVsToCache is undoable, NOT queryable, and NOT editable.

The subdivision surface finer level uvs will get copied to the polygonToSubd
node sent in as argument.  
  
The command takes a single subdivision surface and a single polygonToSubd node
as input. Additional inputs will be ignored. Please note that this command is
an internal command and is to be used with care, directly by the user


-----------------------------------------


Return Value:

boolean  Command result
    """

