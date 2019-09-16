def addDynamic():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/addDynamic.html



-----------------------------------------

addDynamic is undoable, NOT queryable, and NOT editable.

Makes the "object" specified as second argument the source of an existing
field or emitter specified as the first argument. In practical terms, what
this means is that a field will emanate its force from its owner object, and
an emitter will emit from its owner object.

addDynamic makes the specified field or emitter a child of the owner's
transform (adding it to the model if it was not already there), and makes the
necessary attribute connections.

If either of the arguments is omitted, addDynamic searches the selection list
for objects to use instead. If more than one possible owner or field/emitter
is selected, addDynamic will do nothing.

If the specified field/emitter already has a source, addDynamic will remove
the current source and replace it with the newly specified source.

If a subset of the owner object's cvs/particles/vertices is selected,
addDynamic will add the field/emitter to that subset only.


-----------------------------------------


Return Value:

string  The name of the source object and the field or emitter which was
attached to it.
    """

def addPP(atr="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/addPP.html



-----------------------------------------

addPP is undoable, NOT queryable, and NOT editable.

Adds per-point (per-cv, per-vertex, or per-particle) attribute capability for
an attribute of an emitter or field. The -atr flag identifies the attribute.
If no attribute is named, addPP returns a warning and does nothing.

The command adds any other necessary attributes wherever they are needed, and
makes all necessary connections. If any of the attributes already exist, the
command simply connects to them. The command also toggles any relevant
attributes in the emitter or field to indicate that per-point capability is
being used.

The command adds a separate per-point attribute to the owning object for each
emitter/field. For example, for emission rate, there is a separate ratePP for
each emitter. These attributes are named according to the convention
<emitter/field name><attr name>PP. For example, if a particle shape owned an
emitter "smoke", that shape would get attribute "smokeRatePP."

The name of the object must be the emitter or field for which per-point
capability is to be added (or the name of its parent transform). The addPP
command adds the per-point capability for that emitter or field but not for
any others owned by the same object. If per-point capability is not supported
for a named object, the command will trigger a warning, but will continue
executing for any other objects which were valid.

If no objects are named, addPP uses any objects in the current selection list
for which the specified attribute is applicable. (For example, it would add
per-point rate for all selected emitters.)

If addPP detects that the owner object has left-over attributes from a deleted
emitter, it will remove those attributes before adding the new ones. Thus, you
can delete the emitter, make a new one, and run addPP again, and addPP will
clean up after the deleted emitter. This is most commonly used if you have a
geometry emitter and then decide to change the geometry. Likewise, if addPP
detects that some cvs or vertices have been added to the geometry, then it
will expand the corresponding multi-attributes as necessary. However, if it
detects that some cvs/vertices have been removed, it will not remove any
entries from the multi. See the user manual for more discussion.


-----------------------------------------


Return Value:

string[]  Returns names of emitters/fields for which the per-point capability
was added for the specified attribute.


-----------------------------------------


Flags:

-----------------------------------------

atr   : attribute       [string]
    Name of attribute to which you wish to add PP capability. Currently the only attribute supported is rate (for emitters).

    """

def air(q=1,e=1,att="float",dx="float",dy="float",dz="float",es=1,fs=1,iro=1,iv="float",m="float",mxd="linear",n="string",pv=1,pos="[linear, linear, linear]",s="float",sp="float",tsr="linear",vco=1,vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle",wks=1,wns=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/air.html



-----------------------------------------

air is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. The air field simulates the effects
of moving air. The affected objects will be accelerated or decelerated so that
their velocities match that of the air.

With the '-vco true' flag thrown, only accelerations are applied. By parenting
an air field to a moving part of an object (ie. a foot of a character) and
using '-i 1 -m 0 -s .5 -vco true' flags, one can simulate the movement of air
around the foot as it moves, since the TOTAL velocity vector of the field
would be only based on the movement of the foot. This can be done while the
character walks through leaves or dust on the ground.

For each listed object, the command creates a new field. The transform is the
associated dependency node. Use connectDynamic to cause the field to affect a
dynamic object.

If fields are created, this command returns the field names. If a field was
queried, the results of the query are returned. If a field was edited, the
field name is returned.

If the -pos flag is specified, a field is created at the position specified.
If not, if object names are provided or the active selection list is non-
empty, the command creates a field for every object in the list and calls
addDynamic to add it to the object; otherwise the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

dx    : directionX      [float] ['query', 'edit']
    

-----------------------------------------

dy    : directionY      [float] ['query', 'edit']
    

-----------------------------------------

dz    : directionZ      [float] ['query', 'edit']
    Direction that the air will try to match the affected particles' velocity to. NOTE: This is not the velocity; this is only the direction. Use the -s flag to set the speed.

-----------------------------------------

es    : enableSpread    [boolean] ['query', 'edit']
    This tells the system whether or not to use the spread angle given by '-sp'. If this is 'false' then all connected objectswithin the maximum distance will be affected. Also, if this is set to 'false', all affected objects are forced to match their velocities along the direction vector. If this is set to 'true' and spread is used, then the direction of the force is along the direction from the field to the object.

-----------------------------------------

fs    : fanSetup        [boolean] ['edit']
    Similar to 'windSetup' except that the effects of a fan or a person blowing air are approximated. The user can pass the same flags on the command line to adjust them from the defaults. These are the values that get set to approximate a 'fan': inheritVelocity 1.0 inheritRotation true componentOnly false enableSpread true spread .5 (45 degrees from center )

-----------------------------------------

iro   : inheritRotation [boolean] ['query', 'edit']
    If this is set to 'true', then the direction vector described with -dx, -dy, and -dz will be considered local to the owning object. Therefore, if the owning object's transform undergoes any rotation (by itself or one of its parents), the direction vector of the air field will undergo that same rotation.

-----------------------------------------

iv    : inheritVelocity [float] ['query', 'edit']
    Amount (from 0 to 1) of the field-owner's velocity added to the vector determined by the direction and speed flags. The combination of these two vectors makes up the TOTAL velocity vector for the air field. This allows the air to be determined directly by the motion of the owning object.

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

s     : speed           [float] ['query', 'edit']
    How fast the affected objects' speed reaches the speed (based on the -mag, -dx, -dy, -dz flags) of the air field. This value gets clamped internally to be between 0.0 and 1.0. A value of 0.0 will make the air field have no effect. A value of 1.0 will try to match the air field's speed much quicker, but not necessarily immediately.

-----------------------------------------

sp    : spread          [float] ['query', 'edit']
    This represents the angle from the direction vector within which objects will be affected. The values are in the range of 0 to 1. A value of 0 will result in an effect only exactly in front of the air field along the direction vector. A value of 1 will result in any object in front of the owning object, 90 degrees in all direction from the direction vector.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

vco   : velocityComponentOnly [boolean] ['query', 'edit']
    If this is 'false', the air will accelerate or decelerate the affected objects so that their velocities will eventually match the TOTAL velocity vector of the air field. If this is 'true', only ACCELERTION is applied to the affected objects so that their velocity component along the TOTAL velocity vector matches or is greater in magnitude than the TOTAL velocity vector. This will not slow objects down to match velocities, only speed them up to match components. This is most useful when using the -iv flag with a value >0\.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle] ['query', 'edit']
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

-----------------------------------------

wks   : wakeSetup       [boolean] ['edit']
    Like the 'windSetup' and 'fanSetup', 'wakeSetup' sets certain values in the field to approximate the movement of air near a moving object, such as a character's foot or hand. The values that are set are: inheritVelocity 1.0 inheritRotation false componentOnly true enableSpread false speed 0.0

-----------------------------------------

wns   : windSetup       [boolean]
    This will set some of the values above in a way that approximates the effects of a basic wind. This allows the user to then change certain values as he/she wishes on the same command line. First the preset values get set, and then any other flags that were passed get taken into account. These are the values that get set to approximate 'wind': inheritVelocity 0.0 inheritRotation true componentOnly false enableSpread false

    """

def arrayMapper(da="string",iu="string",iv="string",mt="string",t="string",ty="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/arrayMapper.html



-----------------------------------------

arrayMapper is undoable, NOT queryable, and NOT editable.

Create an arrayMapper node and connect it to a target object. If the -type
flag is used, then this command also creates an external node used for
computing the output values. If the input attribute does not already exist, it
will be created. The output attribute must exists. If a flag is omitted, the
selection list will be used to supply the needed objects. If none are found,
that action is omitted.


-----------------------------------------


Return Value:

string[]  Names of created arrayMapper nodes.


-----------------------------------------


Flags:

-----------------------------------------

da    : destAttr        [string] []
    Specifies the attribute which will be the downstream connection for the output data from the mapper node. The attribute type will be used to determine which output attribute to use: float array gets outValuePP, vector array gets outColorPP. If the flag is omitted, no output connection is made.

-----------------------------------------

iu    : inputU          [string] []
    Specifies the upstream attribute to connect to the mapper's uCoordPP attribute. If the flag is omitted, no input connection is made.

-----------------------------------------

iv    : inputV          [string] []
    Specifies the upstream attribute to connect to the mapper's vCoordPP attribute. If the flag is omitted, no input connection is made.

-----------------------------------------

mt    : mapTo           [string] []
    Specifies an existing node to be used to compute the output values. This node must be of the appropriate type. Currently, only ramp nodes may be used.

-----------------------------------------

t     : target          [string] []
    Specifies the target object to be connected to.

-----------------------------------------

ty    : type            [string]
    Specifies the node type to create which will be used to compute the output values. Currently, only ramp is valid. If the flag is omitted, no connection is made and the external node is not created.

    """

def collision(q=1,e=1,f="float",n="string",o="float",r="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/collision.html



-----------------------------------------

collision is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. The collision command causes
particles to collide with geometry. It also allows you to specify values for
the surface properties (friction and resilience) of the collision. These
values are stored in the geoConnector node for the geometry object. Unlike
earlier versions of Maya, there is no separate "collision node."

If a soft object is in the selection list, the collision command assumes that
you want to make it a collider. In order to make the soft object collide with
something use, use connectDynamic -c. The collision menu option sorts this out
using the lead object rule and issues the necessary commands. On creation,
this command returns a string array of the geometry names that were setup for
particle collision.

When the command is used to query information, there are several possible
return types. These include:

  * If the -resilience or -friction flag is passed on the command line and a single collision geometry is either selected or on the command line, then resilience or friction value for that collision geometry is returned as a single float value.

  * If the -resilience or -friction flag is passed on the command line and a single collision geometry and a single particle object are either selected or on the command line, then two results might occur. If the particle object is not set up to collide with the geometry, then an error is displayed stating that. If the objects are set up to collide with each other, then the resilience or friction value that the particle object is using for collisions with the geometry is returned as a single float value. This can be different than the geometry's resilience and friction, because the user may break the connection from the geometry's geoConnector node's resilience or friction to the particle, and set a different value in the particle's collisionResilience, collisionFriction or collisionOffset attribute that is used for that geometry. This allows the user to make each particle respond to the same surface differently. 

  * If neither flag is pass on the command line and a single geometry and single particle object are either selected or on the command line, then a single integer value of 1 is returned if the objects are set up to collide with each other, and 0 is returned if they are not. 

  * Lastly, if no flags are passed on the command line and a single particle object is either selected or on the command line, then a string array with the names of all geometries that the particle object will collide against and the multiIndex that the geometries are connected to is returned. The array is formatted as follows: 

pPlaneShape1:0 pPlaneShape2:2 nurbsSphereShape1:3

...where the number following the ":" is the multiIndex.


-----------------------------------------


Return Value:

string[]  Geometry names that were setup for particle collision.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

f     : friction        [float] ['query', 'edit']
    Friction of the surface. This is the amount of the colliding particle's velocity parallel to the surface which is removed when the particle collides. A value of 0 will mean that no tangential velocity is lost, while a value of 1 will cause the particle to reflect straight along the normal of the surface.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

o     : offset          [float] ['query', 'edit']
    Offset value for the connector.

-----------------------------------------

r     : resilience      [float]
    Resilience of the surface. This is the amount of the colliding particle's velocity reflected along the normal of the surface. A value of 1 will give perfect reflection, while a value of 0 will have no reflection along the normal of the surface.

    """

def connectDynamic(ash="script",c="string",d=1,em="string",f="string",rsh="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/connectDynamic.html



-----------------------------------------

connectDynamic is undoable, NOT queryable, and NOT editable.

Dynamic connection specifies that the force fields, emitters, or collisions of
an object affect another dynamic object. The dynamic object that is connected
to a field, emitter, or collision object is influenced by those fields,
emitters and collision objects.

Connections are made to individual fields, emitters, collisions. So, if an
object owns several fields, if the user wants some of the fields to affect an
object, s/he can specify each field with a "-f" flag; but if the user wants to
connect all the fields owned by an object, s/he can specify the object name
with the "-f" flag. The same is true for emitters and collisions. Different
connection types (i.e., for fields vs. emitters) between the same pair of
objects are logically independent. In other words, an object can be influenced
by another object's fields without being influenced by its emitters or
collisions.

Each connected object must be a dynamic object. The object connected to can be
any object that owns fields, emitters, etc.; it need not be dynamic. Objects
that can own influences are particles, geometry objects (nurbs and polys) and
lattices. You can specify either the shape name or the transform name of the
object to be influenced.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

ash   : addScriptHandler [script] []
    Registers a script that will be given a chance to handle calls to the dynamicConnect command. This flag allows other dynamics systems to override the behaviour of the connectDynamic command. You must pass a Python function as the argument for this flag, and that function must take the following keyword arguments: fields, emitters, collisionObjects and objects. The python function must return True if it has handled the call to connectDynamic. In the case that the script returns true, the connectDynamic command will not do anything as it assumes that the work was handled by the script. If all of the callbacks return false, the connectDynamic command will proceed as normal. The addScriptHandler flag may not be used with any other flags. When the flag is used, the command will return a numerical id that can be used to deregister the callback later (see the removeScriptHandler flag)

-----------------------------------------

c     : collisions      [string] []
    Connects each object to the collision models of the given object.

-----------------------------------------

d     : delete          [boolean] []
    Deletes existing connections.

-----------------------------------------

em    : emitters        [string] []
    Connects each object to the emitters of the given object.

-----------------------------------------

f     : fields          [string] []
    Connects each object to the fields of the given object.

-----------------------------------------

rsh   : removeScriptHandler [int]
    This flag is used to remove a callback that was previously registered with the addScriptHandler flag. The argument to this flag is the numerical id returned by dynamicConnect when the addScriptHandler flag was used. If this flag is called with an invalid id, then the command will do nothing. This flag may not be used with any other flag.

    """

def constrain(q=1,e=1,br=1,d="float",dhi=1,hi=1,i=1,na=1,n="string",o="[float, float, float]",pin=1,p="[float, float, float]",rl="float",s=1,st="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/constrain.html



-----------------------------------------

constrain is undoable, queryable, and editable.

This command constrains rigid bodies to the world or other rigid bodies.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

br    : barrier         [boolean] ['query']
    Creates a barrier constraint. This command requires one rigid bodies.

-----------------------------------------

d     : damping         [float] ['query', 'edit']
    Sets the damping constant. Default value: 0.1 Range: -1000.0 to 1000.0

-----------------------------------------

dhi   : directionalHinge [boolean] ['query']
    Creates a directional hinge constraint. This command requires two rigid bodies. The directional hinge always maintains the initial direction of its axis.

-----------------------------------------

hi    : hinge           [boolean] ['query']
    Creates a hinge constraint. This command requires one or two rigid bodies.

-----------------------------------------

i     : interpenetrate  [boolean] ['query', 'edit']
    Allows (or disallows) the rigid bodies defined in the constrain to ipenetrate.

-----------------------------------------

na    : nail            [boolean] ['query']
    Creates a nail constraint. This command requires one rigid body.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Names the rigid constraint.

-----------------------------------------

o     : orientation     [[float, float, float]] ['query', 'edit']
    Set initial orientation of the constraint in world space. This command is only valid with hinge and barrier constraints Default value: 0.0 0.0 0.0

-----------------------------------------

pin   : pinConstraint   [boolean] ['query']
    Creates a pin constraint. This command requires two rigid bodies.

-----------------------------------------

p     : position        [[float, float, float]] ['query', 'edit']
    Set initial position of the constraint in world space. Default value: 0.0 0.0 0.0 for uni-constraints, midpoint of bodies for deul constraint.

-----------------------------------------

rl    : restLength      [float] ['query', 'edit']
    Sets the rest length. Default value: 1.0

-----------------------------------------

s     : spring          [boolean] ['query']
    Creates a spring constraint. This command requires one or two rigidies.

-----------------------------------------

st    : stiffness       [float]
    Sets the springs stiffness constant. Default value: 5.0

    """

def drag(q=1,e=1,att="float",dx="float",dy="float",dz="float",m="float",mxd="linear",n="string",pv=1,pos="[linear, linear, linear]",tsr="linear",ud=1,vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/drag.html



-----------------------------------------

drag is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. Drag exerts a friction, or braking
force proportional to the speed of a moving object. If direction is not
enabled, the drag acts opposite to the current velocity of the object. If
direction is enabled, it acts opposite to the component of the velocity in the
specified direction. The force is independent of the position of the affected
object.

The transform is the associated dependency node. Use connectDynamic to cause
the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

dx    : directionX      [float] ['query', 'edit']
    X-component of direction.

-----------------------------------------

dy    : directionY      [float] ['query', 'edit']
    Y-component of direction.

-----------------------------------------

dz    : directionZ      [float] ['query', 'edit']
    Z-component of direction

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

ud    : useDirection    [boolean] ['query', 'edit']
    Enable/disable direction. Drag will use -dx/-dy/-dz arguments if and only if this flag is set true.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def dynCache():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynCache.html



-----------------------------------------

dynCache is undoable, NOT queryable, and NOT editable.

Cache the current state of all particle shapes at the current time.


-----------------------------------------


Return Value:

None
    """

def dynExport(all=1,atr="string",f="string",mxf="time",mnf="time",oup=1,os="int",p="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynExport.html



-----------------------------------------

dynExport is undoable, NOT queryable, and NOT editable.

Export particle data to disk files.

For cache export (-format cache), dynExport also sets three attributes of the
current dynGlobals node. It sets the useParticleRenderCache attribute to true,
and the min/maxFrameOfLastParticleRenderCache attributes to correspond to the
min and max frames.

Exported .pda or .pdb files are assigned a name of form object
name.frame.extension, where extension is "pda" or "pdb."

The naming convention for .pdc files is similar but does not use frame
numbers, it uses a more precise representation of the time instead.

By default, the pda and pdb formats export all per-particle attributes, and
all integer or float type attributes except those which are hidden or not
storable. (Exception: level of detail is not exported, by default) The pdc
format exports all attributes which the particle object needs for its state
cache.

To specify only selected attributes, use the -atr flag (which is multi-use).
In general, it is recommended not to use this flag with pdc type, since you
need all the attributes in order for the cache to be useful.

dynExport exports data for the current frame, or for a range of frames
specified with -mnf and -mxf. If you are not already at the start frame,
dynExport will run up the scene for you.  VERY VERY IMPORTANT NOTE: If you use
dynExport in -prompt mode, it does NOT automatically force evaluation of your
objects. You must do this yourself from your script. The easiest way is to
request each particle object's "count" attribute each frame. You must request
the count attribute for each object you want to export, because their solvers
run independently of one another. In interactive mode, objects WILL get
evaluated automatically and you don't have to worry about any of this.

When exporting a particle object whose particles are created from collisions
involving particles in another particle object(s), you must make sure you
simultaneously export all the particle objects involved in the dependency
chain otherwise you will get an empty cache file.

For non-per-particle attributes, pda and pdb formats write the identical value
once for each particle. The following types of non-per-particle attributes can
be exported: float, double, doubleLinear, doubleAngle, byte, short, long,
enum. The first four are exported as "Real" (in PDB parlance), and the last
four as "Integer."

In the pda and pdb formats, "particleId" and "particleId0" are exported as
Integer, and are exported under the names "id" and "id0" respectively. All
other attributes are exported under their long names.


-----------------------------------------


Return Value:

string  Path to the exported files


-----------------------------------------


Flags:

-----------------------------------------

all   : allObjects      [boolean] []
    Ignore the selection list and export all particle objects. If you also specify an object name, the -all flag will be ignored.

-----------------------------------------

atr   : attribute       [string] []
    Name of attribute to be exported. If any specified object does not have one of the specified attributes, dynExport will issue an error and not do the export.

-----------------------------------------

f     : format          [string] []
    Desired format: "binary" ("pdb"), "ascii" ("pda"), or "cache" ("pdc").   The pdc format is for use by the Maya particle system to cache particle data. The pda and pdb format options are intended for pipelines involving other software (for example, sending the data to some program written in-house); Maya cannot read pda or pdb files.   There is no formal description of the PDB format, but the ExploreMe/particles/readpdb directory contains the source and Makefile for a small, simple C program called "readpdb" which reads it. Note that you must compile and run readpdb on the platform which you exported the files on.

-----------------------------------------

mxf   : maxFrame        [time] []
    Ending frame to be exported.

-----------------------------------------

mnf   : minFrame        [time] []
    Starting frame to be exported. The export operation will play the scene through from min frame to max frame as it exports.

-----------------------------------------

oup   : onlyUpdateParticles [boolean] []
    Specify to only update the particles before exporting.

-----------------------------------------

os    : overSampling    [int] []
    OverSampling to be used during export.

-----------------------------------------

p     : path            [string]
    This option allows you to specify a subdirectory of the workspace "particles" directory where you want the exported files to be stored. By default, files are stored in the workspace particles directory, i.e., -path is relative to that directory.   ( Please Read This:  This is a change from previous versions of Maya in which the path was relative to the workspace root directory.) You can set the "particles" directory anywhere you want using the project window or workspace -fr command. (In this way, you can use an absolute path for export).   The -path flag cannot handle strings which include "/" or "\", in other words, it lets you go down only one level in the directory hierarchy. If you specify a path which doesn't exist, the action will create it if possible; if it can't create the path it will warn you and fail. If you are using a project for which a particle data directory is not defined, dynExport will create a default one called "particles" and add it to your workspace.

    """

def dynExpression(q=1,e=1,c=1,n="string",r=1,rad=1,rbd=1,s="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynExpression.html



-----------------------------------------

dynExpression is undoable, queryable, and editable.

This command describes an expression that belongs to the specified particle
shape. The expression is a block of code of unlimited length with a C-like
syntax that can perform conversions, mathematical operations, and logical
decision making on any numeric attribute(s) or per-particle attribute(s) in
the scene. One expression can read and alter any number of these attributes.
Every particle shape in your scene has three expressions, one for the
runtimeBeforeDynamics, one for the runtimeAfterDynamics and one for creation
time. The create expression gets executed for every particle in the object
whose age is 0.0. The runtime expression gets executed for each particle with
an age greater then 0.0. Unlike expressions created with the expression
command, particle expressions always exist and are a part of the owning
particle object's shape. They default to empty strings, but they are always
there. Because of this, there is no need to use the '-e' flag. Every call to
the dynExpression command is considered an edit by default. Per-particle
attributes are those attributes of a particle shape that have a potentially
different value for each particle in the object. Examples of these include
position and velocity.

If this command is being sent by the command line or in a script, then the
user should be sure to embed escaped newlines (\n), tabs (\t) for clarity when
reading them in the expression editor. Also, quotes in an expression must be
escaped (\") so that they are not confused by the system as the end of your
string. When using the expression editor, these characters are escaped for you
unless they are already within quotes.

This type of expression is executed during the evaluation of the dynamics. If
an output of the expression is requested before that, then the dynamics will
be force to compute at that time. If dynamics is disabled, then these
expressions will have no effect.


-----------------------------------------


Return Value:

string  The particle shape which this expression belongs to    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : creation        [boolean] ['query', 'edit']
    Tells the command that the string passed will be a creation expression for the particle shape. This means that this expression will be executed when a particle is emitted or at the beginning of the scene for existing particles.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name to use for this command

-----------------------------------------

r     : runtime         [boolean] ['query', 'edit']
    Tells the command that the string passed will be a runtime expression for the particle shape. This expression will be executed at the beginning of runtime.

-----------------------------------------

rad   : runtimeAfterDynamics [boolean] ['query', 'edit']
    Tells the command that the string passed will be a runtime expression for the particle shape. This expression will be executed after dynamics whenever a particle's age is greater then zero (0).

-----------------------------------------

rbd   : runtimeBeforeDynamics [boolean] ['query', 'edit']
    Tells the command that the string passed will be a runtime expression for the particle shape. This expression will be executed before dynamics whenever a particle's age is greater then zero (0).

-----------------------------------------

s     : string          [string]
    Set the expression string. This is queriable with the -q/query flag and the -rbd/runtimeBeforeDynamics, the -rab/runtimeAfterDynamics or the -c/creation flag.

    """

def dynGlobals(q=1,e=1,a=1,la=1,os="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynGlobals.html



-----------------------------------------

dynGlobals is undoable, queryable, and editable.

This node edits and queries the attributes of the active dynGlobals node in
the scene. There can be only one active node of this type. The active
dynGlobals node is the first one that was created, either with a "createNode"
command or by accessing/editing any of the attributes on the node through this
command.


-----------------------------------------


Return Value:

string  For edit commands    
int  or string For query commands, depending on the flag queried.  
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

a     : active          [boolean] ['query']
    This flag returns the name of the active dynGlobals node in the the scene. Only one dynGlobals node is active. It is the first on created. Any additional dynGlobals nodes will be ignored.

-----------------------------------------

la    : listAll         [boolean] ['query']
    This flag will list all of the dynGlobals nodes in the scene.

-----------------------------------------

os    : overSampling    [int]
    This flag will set the current overSampling value for all of the particle in the scene.

    """

def dynPref(q=1,ac=1,ec=1,rf="int",rt=1,sq=1,sr=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynPref.html



-----------------------------------------

dynPref is undoable, queryable, and NOT editable.

This action modifies and queries the current state of "autoCreate rigid
bodies", "run up to current time", and "run up from" (previous time or start
time).


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ac    : autoCreate      [boolean] ['query']
    If on, autoCreate rigid bodies.

-----------------------------------------

ec    : echoCollision   [boolean] ['query']
    If on, will cause particle systems to echo to the Script Editor the command that they are running for each particle collision event. If off, only the output of the command will be echoed.

-----------------------------------------

rf    : runupFrom       [int] ['query']
    If on, run up from previous time; if 2, run up from start time

-----------------------------------------

rt    : runupToCurrentTime [boolean] ['query']
    If on, run up the scene to current time

-----------------------------------------

sq    : saveOnQuit      [boolean] ['query']
    If on, save the current values of preferences to userPrefs file.

-----------------------------------------

sr    : saveRuntimeState [boolean]
    If on, runtime state as well as initial state of all particle objects will be saved to file. If off, only initial state will be saved.

    """

def emit(at="string",fv="float",o="string",pos="[float, float, float]",vv="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/emit.html



-----------------------------------------

emit is undoable, NOT queryable, and NOT editable.

The emit action allows users to add particles to an existing particle object
without the use of an emitter. At the same time, it allows them to set any
per-particle attribute for the particles that are created with the action.

The particles created do not become a part of the initial state for the
particle object, and will disappear when the scene is rewound unless they are
saved into the initial state by the user explicitly. In addition, a particle
object will accept particles from an emit action ONLY at frames greater than
or equal to its start frame. For example, if you want to use the emit action
to create particles at frame -5, you must set startFrame for that particle
shape to -5 or less.

Unlike many commands or actions, the emit action uses the order of its flags
as important information as to how it works. The -object and -position flags
can appear anywhere in the argument list. The -attribute and the value flags
are interpreted based on their order. Any value flags after an -attribute flag
and before the next -attribute flag will set the values for the attribute
specified by the closest -attribute flag before them in the argument list. See
the Examples section below for more detail on how these flags work.

Currently, no creation expression is executed for the new particles unless
they are created from within a particle expression defined with the
dynExpression command or the Expression Editor. If you want any particular
values put into the particles at the time they are created, then those values
should be set using the -attribute, -vectorValue, and -floatValue flags.


-----------------------------------------


Return Value:

int[]  Integer array containing the list of the particleId attribute values
for the created particles in the same order that the position flags were
passed.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    Specifies the attribute on the particle object that any value flags following it and before the next -attribute flag will be associated with. The same attribute can be specified later in the command to pick up where the first one left off. The attributes used must be per-particle attributes. This will accept both long and short names for the attributes. Note the per- particle attribute must already exist on the particle object prior to being specified via this command flag.

-----------------------------------------

fv    : floatValue      [float] []
    Sets the float value to be used for the "current" attribute of the "current" particle. By current attribute, it is meant the attribute specified by the most recent -attribute flag. By current particle, it is meant the particle in the list of -position flags that corresponds to the number of values that have been set for the "current" attribute. If the current attribute is a vector-per-particle attribute, then the float value specified will be used for all three components of the vector.

-----------------------------------------

o     : object          [string] []
    This flag takes the name of a particleShape or the transform directly above it in the DAG as its parent. It specifies which object to add the particles to. This flag must be passed, as the selection list is ignored for this action.

-----------------------------------------

pos   : position        [[float, float, float]] []
    Specifies the positions in the particle object's space (usually world space) where the particles are to be created. One particle is created for each occurence of this flag.

-----------------------------------------

vv    : vectorValue     [[float, float, float]]
    Sets the vector value to be used for the "current" attribute of the "current" particle. By current attribute, it is meant the attribute specified by the most recent -attribute flag. By current particle, it is meant the particle in the list of -position flags that corresponds to the number of values that have been set for the "current" attribute. If the current attribute is a float-per-particle attribute, then the length of the vector described by this flag will be used. The length is described as SQR( xVal2 \+ yVal2 \+ zVal2 ).

    """

def emitter(q=1,e=1,alx="float",arx="float",afx="float",afc="float",cye="string",cyi="int",dx="linear",dy="linear",dz="linear",drs="float",mxd="linear",mnd="linear",n="string",nuv=1,nsp="float",pos="[linear, linear, linear]",rnd="float",r="float",sro=1,ssz=1,spd="float",srn="float",sp="float",tsp="float",tsr="linear",typ="string",vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/emitter.html



-----------------------------------------

emitter is undoable, queryable, and editable.

Creates, edits or queries an auxiliary dynamics object (for example, a field
or emitter). Creates an emitter object. If object names are provided or if
objects are selected, applies the emitter to the named/selected object(s)in
the scene. Particles will then be emitted from each. If no objects are named
or selected, or if the -pos option is specified, creates a positional emitter.

If an emitter was created, the command returns the name of the object owning
the emitter, and the name of emitter shape. If an emitter was queried, the
command returns the results of the query.

Keyframeable attributes of the emitter node: rate, directionX, directionY,
directionZ, minDistance, maxDistance, spread.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

alx   : alongAxis       [float] ['query', 'edit']
    Initial velocity multiplier in the direction along the central axis of the volume. See the diagrams in the documentation. Applies only to volume emitters.

-----------------------------------------

arx   : aroundAxis      [float] ['query', 'edit']
    Initial velocity multiplier in the direction around the central axis of the volume. See the diagrams in the documentation. Applies only to volume emitters.

-----------------------------------------

afx   : awayFromAxis    [float] ['query', 'edit']
    Initial velocity multiplier in the direction away from the central axis of the volume. See the diagrams in the documentation. Used only with the cylinder, cone, and torus volume emitters.

-----------------------------------------

afc   : awayFromCenter  [float] ['query', 'edit']
    Initial velocity multiplier in the direction away from the center point of a cube or sphere volume emitter. Used only with the cube and sphere volume emitters.

-----------------------------------------

cye   : cycleEmission   [string] ['query', 'edit']
    Possible values are "none" and "frame." Cycling emission restarts the random number stream after a specified interval. This can either be a number of frames or a number of emitted particles. In each case the number is specified by the cycleInterval attribute. Setting cycleEmission to "frame" and cycleInterval to 1 will then re-start the random stream every frame. Setting cycleInterval to values greater than 1 can be used to generate cycles for games work.

-----------------------------------------

cyi   : cycleInterval   [int] ['query', 'edit']
    Specifies the number of frames or particles between restarts of the random number stream. See cycleEmission. Has no effect if cycleEmission is set to None.

-----------------------------------------

dx    : directionX      [linear] ['query', 'edit']
    x-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.

-----------------------------------------

dy    : directionY      [linear] ['query', 'edit']
    y-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.

-----------------------------------------

dz    : directionZ      [linear] ['query', 'edit']
    z-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.

-----------------------------------------

drs   : directionalSpeed [float] ['query', 'edit']
    For volume emitters only, adds a component of speed in the direction specified by the directionX, Y, and Z attributes. Applies only to volume emitters. Does not apply to other types of emitters.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which emission ends.

-----------------------------------------

mnd   : minDistance     [linear] ['query', 'edit']
    Minimum distance at which emission starts.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Object name

-----------------------------------------

nuv   : needParentUV    [boolean] ['query', 'edit']
    If aNeedParentUV is true, compute parentUV value from each triangle or each line segment, then send out to the target particle object. You also need to add parentU and parentV attributes to the particle object to store these values.

-----------------------------------------

nsp   : normalSpeed     [float] ['query', 'edit']
    Normal speed multiple for point emission. For each emitted particle, multiplies the component of the velocity normal to the surface or curve by this amount. Surface and curve emitters only.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    world-space position

-----------------------------------------

rnd   : randomDirection [float] ['query', 'edit']
    Magnitude of a random component of the speed from volume emission.

-----------------------------------------

r     : rate            [float] ['query', 'edit']
    Rate at which particles emitted (can be non-integer). For point emission this is rate per point per unit time. For surface emission it is rate per square unit of area per unit time.

-----------------------------------------

sro   : scaleRateByObjectSize [boolean] ['query', 'edit']
    Applies to curve and surface emitters, only. If true, number of particles is determined by object size (area or length) times rate value. If false, object size is ignored and the rate value is used without modification. The former is the way Maya behaved prior to version 3.0.

-----------------------------------------

ssz   : scaleSpeedBySize [boolean] ['query', 'edit']
    Indicates whether the scale of a volume emitter affects its velocity.

-----------------------------------------

spd   : speed           [float] ['query', 'edit']
    Speed multiple. Multiplies the velocity of the emitted particles by this amount. Does not apply to volume emitters. For that emitter type, use directionalSpeed.

-----------------------------------------

srn   : speedRandom     [float] ['query', 'edit']
    Identifies a range of random variation for the speed of each generated particle. If set to a non-zero value, speed becomes the mean value of the generated particles, whose speeds vary by a random amount up to plus or minus speedRandom/2. For example, speed 5 and speedRandom 2 will make the speeds vary between 4 and 6.

-----------------------------------------

sp    : spread          [float] ['query', 'edit']
    Random spread (0-1), as a fraction of 90 degrees, along specified direction. Directional emitters only.

-----------------------------------------

tsp   : tangentSpeed    [float] ['query', 'edit']
    Tangent speed multiple for point emission. For each emitted particle, multiplies the component of the velocity tangent to the surface or curve by this amount. Surface and curve emitters only.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

typ   : type            [string] ['query', 'edit']
    Type of emitter. The choices are omni | dir | direction | surf | surface | curve | curv. The default is omni. The full definition of these types are: omnidirectional point emitter, directional point emitter, surface emitter, or curve emitter.

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the emitter. Volume offset translates the emission volume by the specified amount from the actual emitter location. This is in the emitter's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the emitter. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which particles are generated. Values are: "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the emitter. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def event(q=1,e=1,ct="uint",d=1,die=1,em="uint",ls=1,n="string",pr="script",r=1,re="string",s=1,spl="uint",sp="float",t="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/event.html



-----------------------------------------

event is undoable, queryable, and editable.

The event command assigns collision events to a particle object. Collision
events are stored in multi-attributes in the particle shape. The event command
returns the event name.


-----------------------------------------


Return Value:

string  for creation; string array for list.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ct    : count           [uint] ['query', 'edit']
    Collision number (for each particle) to which this event applies. Zero (the default) indicates that it applies to all collisions.

-----------------------------------------

d     : delete          [boolean] []
    Delete the specified event.

-----------------------------------------

die   : dieAtCollision  [boolean] ['query', 'edit']
    Particle dies at the collision specified by "count." If no count value is given, die at first collision.

-----------------------------------------

em    : emit            [uint] ['query', 'edit']
    Emit n additional particles into the assigned target object. The original (colliding) particle survives as well, and remains in its original object. The new particles have age zero and mass equal to the emitting particle. They use the velocity inheritance parameter of the target object.

-----------------------------------------

ls    : list            [boolean] []
    List all events for the chosen shape, like this: event1Name event2Name ... If no shape identified, list all events for all shapes, like this: shape1Name event1Name shape2Name event2Name... Returns a string array.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Assign a name to an event you are creating, or identify an event you wish to edit, query, or delete. See examples.

-----------------------------------------

pr    : proc            [script] ['query', 'edit']
    Specify a MEL proc to be called each time the event occurs. This must be a global proc with arguments as follows: global proc procName( string obj, int id, string objHit ); Arguments passed in are the name of the particle object, the id of the particle which collided, and the name of the object collided with. You can use particle -id -q to get values of the particle's attributes.

-----------------------------------------

r     : random          [boolean] ['query', 'edit']
    Used with -split and -emit flags. If -random is set true and -split or -emit is set to n, then a random number of particles uniformly distributed between 1 and n will be created at the event.

-----------------------------------------

re    : rename          [string] ['query']
    Assign a new name to an event you are editing. See examples.

-----------------------------------------

s     : select          [boolean] []
    This flag is obsolete. See the -name flag.

-----------------------------------------

spl   : split           [uint] ['query', 'edit']
    Colliding particle splits into specified number of new particles. These new particles become part of the assigned target object. If no target has been assigned, they become part of the same object. The new particles inherit the current age of the particle that split. They use the velocity inheritance parameter of the target object. If you set both emit and split, the event will do both: first emit new particles, then split the original one. This is a change from earlier versions where emit and split were mutually exclusive.

-----------------------------------------

sp    : spread          [float] ['query', 'edit']
    Particles created at collision will spread out a random amount from the rebound direction of the colliding particle. The spread is specified as a fraction (0-1) of 90 degrees. If spread is set at 0 (the default) all the new particles created may coincide.

-----------------------------------------

t     : target          [string]
    Target object for emitting or split particles. New particles created through the -emit or -split flags join this object.

    """

def expression(q=1,e=1,ae="uint",an="uint",a="string",n="string",o="string",sf=1,sn=1,s="string",td=1,uc="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/expression.html



-----------------------------------------

expression is undoable, queryable, and editable.

This command describes an expression that belongs to the current scene. The
expression is a block of code of unlimited length with a C-like syntax that
can perform conversions, mathematical operations, and logical decision making
on any numeric attribute(s) in the scene. One expression can read and alter
any number of numeric attributes. Theoretically, every expression in a scene
can be combined into one long expression, but it is recommended that they are
separated for ease of use and editing, as well as efficiency.

If this command is being sent by the command line or in a script, then the
user should be sure to embed escaped newlines (\n), tabs (\t) for clarity when
reading them in the expression editor. Also, quotes in an expression must be
escaped (\") so that they are not confused by the system as the end of your
string. When using the expression editor, these characters are escaped for you
unless they are already within quotes.

Note, expressions that alter or use per-particle attributes of a particle
shape should use the '[dynExpression][751]' command.

   [751]: dynExpression.html


-----------------------------------------


Return Value:

string  The name of the expression    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ae    : alwaysEvaluate  [uint] ['query', 'edit']
    If this is TRUE (the default), then the expression will be evaluated whenever time changes regardless of whether the other inputs have changed, and an output is requested. If it is FALSE, then the expression will only be evaluated if one or more of the inputs changes and an output is requested. Note, if 'time' or 'frame' are inputs, then the expression will act as if this was set to TRUE.

-----------------------------------------

an    : animated        [uint] ['query', 'edit']
    Sets the animation mode on the expression node: 0 = Not Animated, 1 = Animated, 2 = Animated with No Callback.

-----------------------------------------

a     : attribute       [string] ['query', 'edit']
    Sets the name of the attribute to use for the expression

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Sets the name of the dependency graph node to use for the expression

-----------------------------------------

o     : object          [string] ['query', 'edit']
    Sets the "default" object for the expression. This allows the expression writer to not type the object name for frequently-used objects. See the examples below.

-----------------------------------------

sf    : safe            [boolean] ['query']
    Returns true if no potential side effect can occurs running that expression. Safe expression will be optimized to evaluate only when needed even if flagged alwaysEvaluate.

-----------------------------------------

sn    : shortNames      [boolean] ['query', 'edit']
    When used with the -q/query flag, tells the command to return the expression with attribute names as short as possible. The default is to return the FULL attribute name, regardless of how the user entered it into the expression, including the object names. With this flag set, attribute names are returned as their short versions, and any attribute that belongs to the default object, if there is one specified, will not display the object's name.

-----------------------------------------

s     : string          [string] ['query', 'edit']
    Set the expression string

-----------------------------------------

td    : timeDependent   [boolean] ['query']
    Returns true if expression is evaluated when time change. An expression can be time-dependent for the following reasons: \- The expression refers to 'time' or 'frame' keywords. \- The expression have side effects (unsafe). \- The expression node's "time" attribute is connected manually. If the expression is safe and not time dependent, then they will always evaluate on depend, even if alwaysEvaluate is on.

-----------------------------------------

uc    : unitConversion  [string]
    Insert specified unit conversion nodes at creation: "all", "none," or "angularOnly." Default is "all." For angularOnly, will insert unit conversion nodes only for angular attributes (allowing degrees-to-radians conversion). This is for performance tuning. If queried, returns the option used when the expression was created or last edited.

    """

def expressionEditorListen(lf="string",la="string",le="string",ln="string",sla="string",sle="string",sln="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/expressionEditorListen.html



-----------------------------------------

expressionEditorListen is undoable, NOT queryable, and NOT editable.

Listens for messages for the Expression Editor, at its request, and
communicates them to it. This action is for internal use only and should not
be called by users. This action should be called only by the Expression
Editor.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

lf    : listenFile      [string] []
    Listen for changes to the file argument.

-----------------------------------------

la    : listenForAttr   [string] []
    Listen for changes to the attributes of the node argument.

-----------------------------------------

le    : listenForExpression [string] []
    Listen for changes to the named expression

-----------------------------------------

ln    : listenForName   [string] []
    Listen for name changes for the node argument.

-----------------------------------------

sla   : stopListenForAttr [string] []
    Stop listening for changes to the attributes of the node argument.

-----------------------------------------

sle   : stopListenForExpression [string] []
    Stop listening for changes to the named expression

-----------------------------------------

sln   : stopListenForName [string]
    Stop listening for name changes for the node argument.

    """

def getParticleAttr(a=1,at="string",o="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getParticleAttr.html



-----------------------------------------

getParticleAttr is undoable, NOT queryable, and NOT editable.

This action will return either an array of values, or the average value and
maximum offset, for a specied per-particle attribute of a particle object or
component. If a particle component is specified on the command line, values
are returned for that component only. If an object name is given instead,
values are returned for all particles in that object. If no object name is
passed, but a particle object or component is selected, values are returned
for the selection.

If you list components, they must all be from the same particle object; the
action ignores all objects after the first. Likewise if you list more than one
object, the actiion will return values only for the first one.


-----------------------------------------


Return Value:

float[]  Command result


-----------------------------------------


Flags:

-----------------------------------------

a     : array           [boolean] []
    Tells the action whether you want a full array of data. If set true, the action returns an array of floats containing the values for all the specified particles. If set false (the default), the action returns the average value and the maximum offset from the average over the component. If the attribute is a vector attribute, the action returns six values: Average X, Average Y, Average Z, Maximum offset in X, Y, and Z of component.

-----------------------------------------

at    : attribute       [string] []
    Tells the action which attribute you want the value of. Must be a per- particle attribute.

-----------------------------------------

o     : object          [string]
    This flag is obsolete. Instead of using it, please pass the name of the object and/or components you want on the command line. See the examples.

    """

def goal(q=1,g="string",i=1,utr=1,w="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/goal.html



-----------------------------------------

goal is undoable, queryable, and NOT editable.

Specifies the given objects as being goals for the given particle object. If
the goal objects are geometry, each particle in the particle object will each
try to follow or match its position to that of a certain vertex/CV/lattice
point of the goal. If the goal object is another particle object, each
particle will try to follow a paricle of the goal. In any other case, all the
particles will try to follow the current location of the goal object's
transform. You can get this latter behavior for a geometry or particle object
too by using -utr true.

The goal weight can be keyframed. It lives on the particle object to which the
goal was added and is a multi-attribute.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

g     : goal            [string] ['query']
    This flag specifies string to be a goal of the particle object on the command line or the currently selected particle object. This flag can be used multiple times to specify multiple goals for a particle object. Query is for use by the attribute editor.

-----------------------------------------

i     : index           [boolean] ['query']
    Returns array of multi-attribute indices for the goals. Intended for use by the Attribute Editor.

-----------------------------------------

utr   : useTransformAsGoal [boolean] []
    Use transform of specified object instead of the shape. Meaningful only for particle and geometry objects. Can only be passed once, applies to all objects passed with -g.

-----------------------------------------

w     : weight          [float]
    This specifies the goal weight as a value from 0 to 1. A value of 0 means that the goal's position will have no effect on the particle object, while a weight of 1 will make the particle object try to follow the goal object exactly. This flag can only be passed once and sets the weight for every goal passed with the -g/-goal flag.

    """

def gravity(q=1,e=1,att="float",dx="float",dy="float",dz="float",m="float",mxd="linear",n="string",pv=1,pos="[linear, linear, linear]",tsr="linear",vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/gravity.html



-----------------------------------------

gravity is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. A gravity field simulates the
Earth's gravitational force. It pulls objects in a fixed direction (generally
downward) entirely independent of their position or mass.

The transform is the associated dependency node. Use connectDynamic to cause
the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.

The default for -dx -dy -dz is always the opposite of the current up
direction. For example, if the current up direction is (0,1,0) (a standard
Maya configuration), then the gravity default is -dx 0 -dy -1 -dz 0. The
default for -a is 9.8. 9.8 meters per second squared happens to be standard
Earth gravity, but in fact Maya interprets this value as centimeters per
second squared. If we were to use it as meters per second squared then with
default Maya units, your particles would vanish almost in the wink of an eye.
If you want a different value, set it in the gravity option box.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

dx    : directionX      [float] ['query', 'edit']
    X-component of direction.

-----------------------------------------

dy    : directionY      [float] ['query', 'edit']
    Y-component of direction.

-----------------------------------------

dz    : directionZ      [float] ['query', 'edit']
    Z-component of direction

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def newton(q=1,e=1,att="float",m="float",mxd="linear",mnd="float",n="string",pv=1,pos="[linear, linear, linear]",tsr="linear",vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/newton.html



-----------------------------------------

newton is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. A Newton field pulls an object
towards the exerting object with force dependent on the exerting object's
mass, using Newton's universal law of gravitation.

The transform is the associated dependency node. Use connectDynamic to cause
the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

mnd   : minDistance     [float] ['query', 'edit']
    Minimum distance at which field is exerted. Distance is in the denominator of the field force equation. Setting md to a small positive number avoids bizarre behavior when the distance gets extremely small.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def particle(q=1,e=1,at="string",ch=1,c="float",ct=1,dc=1,dal=1,fv="float",grs="linear",i="float",jbp="[linear, linear, linear]",jr="linear",ll="[linear, linear, linear]",n="string",nj="uint",order="int",id="int",ppd=1,ppv=1,p="[linear, linear, linear]",sn="string",ur="[linear, linear, linear]",vv="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/particle.html



-----------------------------------------

particle is undoable, queryable, and editable.

The particle command creates a new particle object from a list of world space
points. If a particle object is created, the command returns the names of the
new particle shape and its associated particle object dependency node. If an
object was queried, the results of the query are returned. Per particle
attributes can be queried using the particleId or the order of the particle in
the particle array. If an object was edited, nothing is returned.


-----------------------------------------


Return Value:

string  The name of the particle object created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] ['query', 'edit']
    Used in per particle attribute query and edit. Specifies the name of the attribute being queried or edited.  In query mode, this flag needs a value.

-----------------------------------------

ch    : cache           [boolean] ['query', 'edit']
    Turns caching on/off for the particle shape.

-----------------------------------------

c     : conserve        [float] ['query', 'edit']
    Conservation of momentum control (between 0 and 1). Specifies the fraction of the particle shape's existing momentum which is conserved from frame to frame. A value of 1 (the default) corresponds to true Newtonian physics, in which momentum is conserved.

-----------------------------------------

ct    : count           [boolean] ['query']
    Returns the number of particles in the object.

-----------------------------------------

dc    : deleteCache     [boolean] []
    Deletes the particle shapes cache. This command is not undoable.

-----------------------------------------

dal   : dynamicAttrList [boolean] ['query']
    Returns a list of the dynamic attributes in the object.

-----------------------------------------

fv    : floatValue      [float] ['edit']
    Used only in per particle attribute edit. Specifies that the edit is of a float attribute and must be followed by the new float value.

-----------------------------------------

grs   : gridSpacing     [linear] ['query']
    Spacing between particles in the grid.

-----------------------------------------

i     : inherit         [float] ['query', 'edit']
    Inherit this fraction (0-1) of emitting object's velocity.

-----------------------------------------

jbp   : jitterBasePoint [[linear, linear, linear]] ['query']
    Base point (center point) for jitters. The command will create one swatch of jitters for each base point. It will pair up other flags with base points in the order they are given in the command line. If not enough instances of the other flags are availble, the last one on the line with be used for all other instances of -jpb.

-----------------------------------------

jr    : jitterRadius    [linear] ['query']
    Max radius from the center to place the particle instances.

-----------------------------------------

ll    : lowerLeft       [[linear, linear, linear]] ['query']
    Lower left point of grid.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of particle object

-----------------------------------------

nj    : numJitters      [uint] ['query']
    Number of jitters (instances) per particle.

-----------------------------------------

order : order           [int] ['query', 'edit']
    Used in per particle attribute query and edit. Specifies the zero-based order (index) of the particle whose attribute is being queried or edited in the particle array. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.  In query mode, this flag needs a value.

-----------------------------------------

id    : particleId      [int] ['query', 'edit']
    Used in per particle attribute query and edit. Specifies the id of the particle whose attribute is being queried or edited. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.  In query mode, this flag needs a value.

-----------------------------------------

ppd   : perParticleDouble [boolean] ['query']
    Returns a list of the per-particle double attributes, excluding initial- state, cache, and information-only attributes.

-----------------------------------------

ppv   : perParticleVector [boolean] ['query']
    Returns a list of the per-particle vector attributes, excluding initial- state, cache, and information-only attributes.

-----------------------------------------

p     : position        [[linear, linear, linear]] []
    World-space position of each particle.

-----------------------------------------

sn    : shapeName       [string] ['query', 'edit']
    Specify the shape name used for geometry instancing. DO not confuse this with the -n flag which names the particle object.

-----------------------------------------

ur    : upperRight      [[linear, linear, linear]] ['query']
    Upper right point of grid.

-----------------------------------------

vv    : vectorValue     [[float, float, float]]
    Used only in per particle attribute edit. Specifies that the edit is of a vector attribute and must be followed by all three float values for the vector.

    """

def particleExists():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/particleExists.html



-----------------------------------------

particleExists is undoable, NOT queryable, and NOT editable.

This command is used to query if a particle or soft object with the given name
exists. Either the transform or shape name can be used as well as the name of
the soft object.


-----------------------------------------


Return Value:

boolean  True if there is a particle object or soft object by the given name,
false otherwise.
    """

def particleFill(cp=1,dw=1,mxx="float",mxy="float",mxz="float",mnx="float",mny="float",mnz="float",pd="float",rs="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/particleFill.html



-----------------------------------------

particleFill is NOT undoable, NOT queryable, and NOT editable.

This command generates an nParticle system that fills the selected object with
a grid of particles.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cp    : closePacking    [boolean] []
    If this is on then the particles are positioned as closely as possible in a hexagonal close packing arrangement. Otherwise particles are packed in a uniform grid lattice.

-----------------------------------------

dw    : doubleWalled    [boolean] []
    This flag should be used if the thickness of the object to fill has been modeled( for example a mug ). Otherwise the particles will be created inside the wall. Note that doubleWalled will not handle some cases very well. For example a double walled donut shape may get the center region of the donut filled. In cases like this it may be better to make the internal wall a separate mesh then fill that without using doubleWalled.

-----------------------------------------

mxx   : maxX            [float] []
    The fill max bounds of the particles in X relative to the X bounds of the object. A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.

-----------------------------------------

mxy   : maxY            [float] []
    The fill max bounds of the particles in Y relative to the Y bounds of the object. A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.

-----------------------------------------

mxz   : maxZ            [float] []
    The fill max bounds of the particles in Z relative to the Z bounds of the object. A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.

-----------------------------------------

mnx   : minX            [float] []
    The fill lower bounds of the particles in X relative to the X bounds of the object. A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.

-----------------------------------------

mny   : minY            [float] []
    The fill lower bounds of the particles in Y relative to the Y bounds of the object. A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.

-----------------------------------------

mnz   : minZ            [float] []
    The fill lower bounds of the particles in Z relative to the Z bounds of the object. A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.

-----------------------------------------

pd    : particleDensity [float] []
    This controls the size of the particles. At a value of 1.0 the particle size will exactly match the grid spacing determined by the resolution parameter and the object bounds. Particles which overlap the surface will be rejected even if the center of the particle is inside.

-----------------------------------------

rs    : resolution      [int]
    This determines the total number of particles generated. It represent the resolution along the largest axis of the object's bounding box. For a cube shape the total potential particles will be the cube of the resolution. For other shapes it will be less. The default value for this flag is 10, so 1000 particles could be generated for a cube shape.

    """

def particleInstancer(q=1,e=1,a=1,aa="string",ad="string",ap="string",aua="string",awu="string",am=1,c="string",sto="string",cs="float",csu="string",i="int",id="string",lod="string",n="string",obj="string",oi="string",age="string",p="string",rm=1,r="string",ro="string",rt="string",ru="string",sc="string",sh="string",vis="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/particleInstancer.html



-----------------------------------------

particleInstancer is undoable, queryable, and editable.

This command is used to create a particle instancer node and set the proper
attributes in the particle shape and in the instancer node. It will also
create the connections needed between the particle shape and the instancer
node.


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

aa    : aimAxis         [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the aim axis of the instanced objects.

-----------------------------------------

ad    : aimDirection    [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the aim direction of the instanced objects.

-----------------------------------------

ap    : aimPosition     [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the aim position of the instanced objects.

-----------------------------------------

aua   : aimUpAxis       [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the aim up axis of the instanced objects.

-----------------------------------------

awu   : aimWorldUp      [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the aim world up of the instanced objects.

-----------------------------------------

am    : attributeMapping [boolean] ['query']
    This flag queries the particle attribute mapping list.

-----------------------------------------

c     : cycle           [string] ['query', 'edit']
    This flag sets or queries the cycle attribute for the instancer node. The options are "none", "sequential". The default is "none".

-----------------------------------------

sto   : cycleStartObject [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the cycle start object of the instanced objects.

-----------------------------------------

cs    : cycleStep       [float] ['query', 'edit']
    This flag sets or queries the cycle step attribute for the instancer node. This attribute indicates the size of the step in frames or seconds (see cycleStepUnits).

-----------------------------------------

csu   : cycleStepUnits  [string] ['query', 'edit']
    This flag sets or queries the cycle step unit attribute for the instancer node. The options are "frames" or "seconds". The default is "frames".

-----------------------------------------

i     : index           [int] ['query']
    This flag is used to query the name of the ith instanced object.

-----------------------------------------

id    : instanceId      [string] ['query']
    This flag queries the particle attribute name to be used for the id of the instanced objects.

-----------------------------------------

lod   : levelOfDetail   [string] ['query', 'edit']
    This flag sets or queries the level of detail of the instanced objects. The options are "geometry", "boundingBox" or "boundingBoxes". The default is "geometry".

-----------------------------------------

n     : name            [string] ['query']
    This flag sets or queries the name of the instancer node.

-----------------------------------------

obj   : object          [string] ['query', 'edit']
    This flag indicates which objects will be add/removed from the list of instanced objects. The flag is used in conjuction with the -addObject and -remove flags. If neither of these flags is specified on the command line then -addObject is assumed.

-----------------------------------------

oi    : objectIndex     [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the object index of the instanced objects.

-----------------------------------------

age   : particleAge     [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the age of the instanced objects.

-----------------------------------------

p     : position        [string] ['query', 'edit']
    DEFAULT "worldPosition" This flag sets or queries the particle attribute name to be used for the positions of the instanced objects. By default the attribute is worldPosition.

-----------------------------------------

rm    : removeObject    [boolean] ['edit']
    This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.

-----------------------------------------

r     : rotation        [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the rotation of the instanced objects.

-----------------------------------------

ro    : rotationOrder   [string] ['query', 'edit']
    This flag specifies the rotation order associated with the rotation flag. The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX. By default the attribute is XYZ.

-----------------------------------------

rt    : rotationType    [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the rotation type of the instanced objects.

-----------------------------------------

ru    : rotationUnits   [string] ['query', 'edit']
    This flag specifies the rotation units associated with the rotation flag. The options are degrees or radians. By default the attribute is degrees.

-----------------------------------------

sc    : scale           [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the scale of the instanced objects.

-----------------------------------------

sh    : shear           [string] ['query', 'edit']
    This flag sets or queries the particle attribute name to be used for the shear of the instanced objects.

-----------------------------------------

vis   : visibility      [string]
    This flag sets or queries the particle attribute name to be used for the visibility of the instanced objects.

    """

def particleRenderInfo(q=1,al="int",ala=1,n="int",rtc=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/particleRenderInfo.html



-----------------------------------------

particleRenderInfo is undoable, queryable, and NOT editable.

This action provides information access to the particle render subclasses.
These are derived from TdynRenderBase. This action is used primarily by the
Attribute Editor to gather information about attributes used for rendering.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

al    : attrList        [int] ['query']
    Return the list of attributes used by this render type.

-----------------------------------------

ala   : attrListAll     [boolean] ['query']
    Return a complete list of all render attributes used by the particle object. This also includes the per particle attributes.

-----------------------------------------

n     : name            [int] ['query']
    Return the name of the render subclass using the render type.

-----------------------------------------

rtc   : renderTypeCount [boolean]
    Return the count of registered render classes for particle.

    """

def radial(q=1,e=1,att="float",m="float",mxd="linear",n="string",pv=1,pos="[linear, linear, linear]",tsr="linear",typ="float",vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/radial.html



-----------------------------------------

radial is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. A radial field pushes objects
directly towards or directly away from it, like a magnet.

The transform is the associated dependency node. Use connectDynamic to cause
the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

typ   : type            [float] ['query', 'edit']
    Type of radial field (0 - 1). This controls the algorithm by which the field is attenuated. Type 1, provided for backward compatibility, specifies the same algorithm as Alias | Wavefront Dynamation. A value between 0 and 1 yields a linear blend.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def rigidBody(q=1,e=1,act=1,av=1,afa="string",b="float",c=1,com="[float, float, float]",cl=1,cc=1,cn=1,cp=1,dp="float",dc=1,df="float",f=1,ig=1,i="[float, float, float]",imp="[float, float, float]",iav="[float, float, float]",iv="[float, float, float]",l="int",lcm=1,m="float",n="string",o="[float, float, float]",pc=1,pas=1,p="[float, float, float]",rs="string",slv="string",si="[float, float, float]",sio="string",sf="float",tf="int",vel=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rigidBody.html



-----------------------------------------

rigidBody is undoable, queryable, and editable.

This command creates a rigid body from a polygonal or nurbs surface.


-----------------------------------------


Return Value:

string  New rigid body name.    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

act   : active          [boolean] ['query', 'edit']
    Creates a rigid body that is active. An active rigid body accepts and causes collisions and is effected by dynamic fields. This is the default.

-----------------------------------------

av    : angularVelocity [boolean] ['query']
    Current angular velocity of rigid body.

-----------------------------------------

afa   : applyForceAt    [string] ['query', 'edit']
    Determines how forces are applied to the rigid body. The choices are centerOfMass | boundingBox | verticesOrCVs. Default: boundingBox

-----------------------------------------

b     : bounciness      [float] ['query', 'edit']
    Sets the restitution (or bounciness) of the rigid body. Range: 0.0 - 2.0 Default: 0.6

-----------------------------------------

c     : cache           [boolean] ['query', 'edit']
    Turns caching on (1) or off (0) for the rigid body. Default: off

-----------------------------------------

com   : centerOfMass    [[float, float, float]] ['query', 'edit']
    Sets the center of mass (x,y,z) of the rigid body. Default: actual center of mass.

-----------------------------------------

cl    : collisions      [boolean] ['query', 'edit']
    Truns collisions on/off for the rigid body. If the collisions are turned of the rigid body will not collide with any other rigid body. Default: on.

-----------------------------------------

cc    : contactCount    [boolean] ['query']
    returns the current contact count for the rigid body.

-----------------------------------------

cn    : contactName     [boolean] ['query']
    returns all the rigid body names which are in contact with this shape. One name for each contact will be returned.

-----------------------------------------

cp    : contactPosition [boolean] ['query']
    returns all the contact position. One position for each contact will be returned.

-----------------------------------------

dp    : damping         [float] ['query', 'edit']
    Sets the damping value of the rigid body. Range: -2.0 - 2.0 Default: 0.0

-----------------------------------------

dc    : deleteCache     [boolean] ['edit']
    Deletes the cache (if one exists) of the rigid body.

-----------------------------------------

df    : dynamicFriction [float] ['query', 'edit']
    Sets the dynamic friction for the rigid body. Range: 0.0 - 1.0 Default: 0.2

-----------------------------------------

f     : force           [boolean] ['query']
    Current force on the rigid body.

-----------------------------------------

ig    : ignore          [boolean] ['query', 'edit']
    Causes the rigid body to be ignored in the rigid solver. Default: off

-----------------------------------------

i     : impulse         [[float, float, float]] ['edit']
    Applies an impulse (instantaneous) force on a rigid body. Default: 0.0 0.0 0.0

-----------------------------------------

imp   : impulsePosition [[float, float, float]] ['edit']
    The position at which the impulse is applied. Default: the bodies center of mass.

-----------------------------------------

iav   : initialAngularVelocity [[float, float, float]] ['query', 'edit']
    Sets the initial angular velocity of the rigid body. Default: 0.0 0.0 0.0

-----------------------------------------

iv    : initialVelocity [[float, float, float]] ['query', 'edit']
    Sets the initial velocity of the rigid body. Default: 0.0 0.0 0.0

-----------------------------------------

l     : layer           [int] ['query', 'edit']
    Sets the collision layer of the rigid body. Only rigid bodies in the same collision layer can collide with each other. Range: >= 0 Default: 0.

-----------------------------------------

lcm   : lockCenterOfMass [boolean] ['query', 'edit']
    Locks the center of mass for the rigid body. Default: off

-----------------------------------------

m     : mass            [float] ['query', 'edit']
    Sets the mass of the rigid body. Range: > 0 Default: 1.0

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Assigns the rigid body the given name.

-----------------------------------------

o     : orientation     [[float, float, float]] ['query', 'edit']
    Sets the initial orientation (x,y,z) of the rigid body. Default: current orientation.

-----------------------------------------

pc    : particleCollision [boolean] ['query', 'edit']
    Turns the ability for a rigid body to collide with particles on and off. The particles will exert a force on the rigid body. Default: off

-----------------------------------------

pas   : passive         [boolean] ['query', 'edit']
    Creates a rigid body that is passive. A passive rigid body does not react to collisions but active rigid bodies can collide with it. Dynamic Fields will not effect a passive rigid body. Only passive rigid bodies can be keyframed.

-----------------------------------------

p     : position        [[float, float, float]] ['query', 'edit']
    Sets the initial position (x,y,z) of the rigid body. Default: current position.

-----------------------------------------

rs    : removeShape     [string] ['query', 'edit']
    Remove the named shape.

-----------------------------------------

slv   : solver          [string] ['query', 'edit']
    The name of the solver which this rigid node is to resided. If the solver does not exists then the rigid body will not be created. If the edit flag is thrown add the solver exists, the rigid body will be moved to that solver.

-----------------------------------------

si    : spinImpulse     [[float, float, float]] ['edit']
    Applies an spin impulse (instantaneous rotational) force on a rigid body. Default: 0.0 0.0 0.0

-----------------------------------------

sio   : standInObject   [string] ['query', 'edit']
    Causes the simulator to use a stand in object for the simulation. The choices are none | cube | sphere. The default is none. Default: none

-----------------------------------------

sf    : staticFriction  [float] ['query', 'edit']
    Sets the static friction for the rigid body. Range: 0.0 - 1.0 Default: 0.2

-----------------------------------------

tf    : tesselationFactor [int] ['query']
    Sets the tesselation factor for a rigid body surface. Range: >= 10 Default: 200.

-----------------------------------------

vel   : velocity        [boolean]
    Current velocity of rigid body.

    """

def rigidSolver(q=1,e=1,at=1,b=1,cd=1,c=1,ct="float",ctd=1,cr=1,cu=1,deleteCache=1,dcm=1,dc=1,dv=1,d=1,f=1,i=1,ic=1,n="string",rb=1,rbc=1,sc=1,si=1,sm="int",stt="float",st=1,sta=1,s="float",vs="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/rigidSolver.html



-----------------------------------------

rigidSolver is undoable, queryable, and editable.

This command sets the attributes for the rigid solver


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : autoTolerances  [boolean] ['query', 'edit']
    Turns the auto tolerance calculation on and off. The auto tolerances calculation will override the default or user defined values of the step size and collision tolerance value that is calculated based on the objects in the scene. Default: 0 (off)

-----------------------------------------

b     : bounciness      [boolean] ['query', 'edit']
    Turns bounciness on and off for the an the objects in the simulation. Default value: on

-----------------------------------------

cd    : cacheData       [boolean] ['query', 'edit']
    Turns the cache on fall all rigid bodies in the system. Default value: off

-----------------------------------------

c     : collide         [boolean] ['query', 'edit']
    Disallows the interpenetration of the two rigid bodies listed. Default: Collide is on for all bodies.

-----------------------------------------

ct    : collisionTolerance [float] ['query', 'edit']
    Sets the collision tolerance. This is the error at which two objects are considered to have collided. Range: 0.0005 - 1.000 Default: 0.02

-----------------------------------------

ctd   : contactData     [boolean] ['query', 'edit']
    Turns the contact data information on/off for all rigid bodies. Default value: off

-----------------------------------------

cr    : create          [boolean] []
    Creates a new rigid solver.

-----------------------------------------

cu    : current         [boolean] []
    Sets rigid solver as the current solver.

-----------------------------------------

deleteCache : deleteCache     [boolean] ['query', 'edit']
    Deletes the cache for all rigid bodies in the system.

-----------------------------------------

dcm   : displayCenterOfMass [boolean] ['query', 'edit']
    Displays the center of mass icon. Default value: on

-----------------------------------------

dc    : displayConstraint [boolean] ['query', 'edit']
    Displays the constraint vectors. Default value: on

-----------------------------------------

dv    : displayVelocity [boolean] ['query', 'edit']
    Displays the velocity vectors. Default value: off

-----------------------------------------

d     : dynamics        [boolean] ['query', 'edit']
    Turns dynamics on and off for the an the objects in the simulation. Default value: on

-----------------------------------------

f     : friction        [boolean] ['query', 'edit']
    Turns friction on and off for the an the objects in the simulation. Default value: on

-----------------------------------------

i     : interpenetrate  [boolean] ['query', 'edit']
    Allows the two rigid bodies listed to interpenetrate. Default: interpenetration is off for all bodies.

-----------------------------------------

ic    : interpenetrationCheck [boolean] ['edit']
    Checks for interpenetrating rigid bodies in the scene.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Name of the new object

-----------------------------------------

rb    : rigidBodies     [boolean] ['query']
    Returns a list of rigid bodies in the solver.

-----------------------------------------

rbc   : rigidBodyCount  [boolean] ['query']
    Returns the number of rigid bodies in the solver.

-----------------------------------------

sc    : showCollision   [boolean] ['query', 'edit']
    Displays the colliding objects in a different color.

-----------------------------------------

si    : showInterpenetration [boolean] ['query', 'edit']
    Displays the interpenetrating objects in a different color.

-----------------------------------------

sm    : solverMethod    [int] ['query', 'edit']
    Sets the solver method. The choices are 0 | 1 | 2. 0 = Euler (fastest/least acurate), 1 = Runge-Kutta ( slower/more acurate), 2 = adaptive Runge-Kutta (slowest/most acurate). The default is 2 (adaptive Runge-Kutta)

-----------------------------------------

stt   : startTime       [float] ['query', 'edit']
    Sets the start time for the solver.

-----------------------------------------

st    : state           [boolean] ['query', 'edit']
    Turns the rigid solver on or off.

-----------------------------------------

sta   : statistics      [boolean] ['query', 'edit']
    Turns the statistic information on/off for all rigid bodies. Default value: off

-----------------------------------------

s     : stepSize        [float] ['query', 'edit']
    Sets the solvers step size. This is the maximum size of a single step the solver will take at one time. Range: 0.0004 - 0.100 Default: 0.0333

-----------------------------------------

vs    : velocityVectorScale [float]
    scales the velocity vector display. Default value: 1.0

    """

def runup(cch=1,fpf=1,fsf=1,mxf="time",st=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/runup.html



-----------------------------------------

runup is undoable, NOT queryable, and NOT editable.

runup plays the scene through a frame of frames, forcing dynamic objects to
evaluate as it does so. If no max frame is specified, runup runs up to the
current time.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

cch   : cache           [boolean] []
    Cache the state after the runup.

-----------------------------------------

fpf   : fromPreviousFrame [boolean] []
    Run up the animation from the previously evaluated frame. If no flag is supplied this is the default.

-----------------------------------------

fsf   : fromStartFrame  [boolean] []
    Run up the animation from the start frame. If no flag is supplied -fromPreviousFrame is the default.

-----------------------------------------

mxf   : maxFrame        [time] []
    Ending time for runup, in current user time units. The runup will always start at the minimum start frame for all dynamic objects.

-----------------------------------------

st    : state           [boolean]
    Turns runup and cache on/off.

    """

def saveInitialState(atr="string",all=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/saveInitialState.html



-----------------------------------------

saveInitialState is undoable, NOT queryable, and NOT editable.

saveInitialState saves the current state of dynamics objects as the initial
state. A dynamic object is a particle shape, rigid body, rigid constraint or
rigid solver. If no objects are specified, it saves the initial state for any
selected objects. It returns the names of the objects for which initial state
was saved.


-----------------------------------------


Return Value:

string  Command result


-----------------------------------------


Flags:

-----------------------------------------

atr   : attribute       [string] []
    Save the initial state of the specified attribute only. This is a multi- use flag.

-----------------------------------------

all   : saveall         [boolean]
    Save the initial state for all dynamics objects in the scene.

    """

def setDynamic(awr=1,dwr=1,all=1,off=1,on=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setDynamic.html



-----------------------------------------

setDynamic is undoable, NOT queryable, and NOT editable.

setDynamic sets the isDynamic attribute of particle objects on or off. If no
objects are specified, it sets the attribute for any selected objects. If -all
is thrown, it sets the attribute for all particle objects in the scene. By
default it sets the attribute true (on); if the -off flag is thrown, it sets
the attribute false (off).

WARNING: setDynamic is obsolescent. This is the last version of Maya in which
it will be supported.


-----------------------------------------


Return Value:

string  array


-----------------------------------------


Flags:

-----------------------------------------

awr   : allOnWhenRun    [boolean] []
    Obsolete, no longer suppported or necessary.

-----------------------------------------

dwr   : disableAllOnWhenRun [boolean] []
    Obsolete, no longer suppported or necessary.

-----------------------------------------

all   : setAll          [boolean] []
    Set for all objects.

-----------------------------------------

off   : setOff          [boolean] []
    Sets isDynamic false.

-----------------------------------------

on    : setOn           [boolean]
    Sets isDynamic true. This flag is set by default.

    """

def setParticleAttr(at="string",fv="float",o="string",rf="float",rv="[float, float, float]",r=1,vv="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setParticleAttr.html



-----------------------------------------

setParticleAttr is undoable, NOT queryable, and NOT editable.

This action will set the value of the chosen attribute for every particle or
selected component in the selected or passed particle object. Components
should not be passed to the command line. For setting the values of
components, the components must be selected and only the particle object's
names should be passed to this action. If the attribute is a vector attribute
and the -vv flag is passed, then the three floats passed will be used to set
the values. If the attribute is a vector and the -fv flag is pass and the -vv
flag is not passed, then the float will be repeated for each of the X, Y, and
Z values of the attribute. Similarly, if the attribute is a float attribute
and a vector value is passed, then the length of the vector passed will be
used for the value. Note: The attribute passed must be a Per-Particle
attribute.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    Tells the action which attribute you want to set

-----------------------------------------

fv    : floatValue      [float] []
    Tells what you want the value to be set to of a float attribute

-----------------------------------------

o     : object          [string] []
    If this flag is passed and the STRING is the name of a particle object's transform or shape, then ONLY that object will be edited, ignoring the selection list or command line, and ALL of its particles' values will be changed for the specified attribute.

-----------------------------------------

rf    : randomFloat     [float] []
    Tells the command to add a random value from -FLOAT to +FLOAT to the results of each particle. The default is 0.0.

-----------------------------------------

rv    : randomVector    [[float, float, float]] []
    Tells the command to add a random value from <<-x,-y,-z>> to <<x,y,z>> to the results of each particle. The default 0 0 0.

-----------------------------------------

r     : relative        [boolean] []
    If this is set to TRUE (the default is FALSE), then the float or vector value will be added to the current value for each particle.

-----------------------------------------

vv    : vectorValue     [[float, float, float]]
    Tells what you want the value to be set to of a vector attribute

    """

def soft(q=1,c=1,d=1,dh=1,g="float",h=1,n="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/soft.html



-----------------------------------------

soft is undoable, queryable, and NOT editable.

Makes a soft body from the object(s) passed on the command line or in the
selection list. The geometry can be a NURBS, polygonal, lattice object. The
resulting soft body is made up of a hierarchy with a particle shape and a
geometry shape, thus:

    
    
                     
    
    
                T    
    
    
                / \  
    
    
               T   G 
    
    
              /      
    
    
            P        
    
    
                     

Dynamics are applied to the particle shape and the resulting particle
positions then drive the locations of the geometry's CVs, vertices, or lattice
points.

With the convert option, the particle shape and its transform are simply
inserted below the original shape's hierarchy. With the duplicate option, the
original geometry's transform and shape are duplicated underneath its parent,
and the particle shape is placed under the duplicate. Note that any animation
on the hierarchy will affect the particle shape as well. If you do not want
then, then reparent the structure outside the hierarchy.

When duplicating, the soft portion (the duplicate) is given the name "copyOf"
\+ "original object name". The particle portion is always given the name
"original object name" \+ "Particles."

None of the flags of the soft command can be queried. The soft -q command is
used only to identify when an object is a soft body, or when two objects are
part of the same soft body. See the examples.


-----------------------------------------


Return Value:

string  array    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : convert         [boolean] []
    This tells the command that you want the original object to be the actual deformed object. The particle shape portion of the soft body will be inserted in the same hierarchy as the original, under the same parent (with one additional intervening transform which is initially the identity). If no flags are passed, then this is assumed. The combination -c -h 1 is not valid; if you have this in your scripts, remove the -h 1.

-----------------------------------------

d     : duplicate       [boolean] []
    This tells the command that you want to make a copy of the original object and use the copy as the deforming geometry. Input connections to the original object are duplicated. You would do this if you wanted to keep the original object in your scene and also have a copy of it that was a soft body. This flag and -dh are mutually exclusive.

-----------------------------------------

dh    : duplicateHistory [boolean] []
    This is the same as -d, except that upstream history, is duplicated as well, instead of just input connections. This flag and -d are mutually exclusive.

-----------------------------------------

g     : goal            [float] []
    This is the same as -d, but in addition it tells the command that you want the resulting soft body to try to follow the original geometry, using the set goal weight as the value that controls how strongly it is to follow it. A value of 1.0 will try to follow exactly, and a value of 0.0 will not follow at all. The default value is 0.5. This value must be from 0.0 to 1.0. You could use -d with -g, but it is redundant. If you want history to be duplicated, you can use -dh and -g together.

-----------------------------------------

h     : hideOriginal    [boolean] []
    This flag is used only when duplicating (-d, -g, or -dh). If set to true, whichever of the two objects is NOT the soft object will be hidden. In other words, with -d -h true, the original object will be hidden; with -d -c -h 1 the duplicate object will be hidden. You would typically do this if you want to use the non-dynamic object as a goal for the soft one (see -g) but you do not want it visible in the scene. The flags -h 1 and -c are mutually exclusive.

-----------------------------------------

n     : name            [string]
    This flag is obsolete. If you wish to give your new soft object a name, use the rename command (or from the UI, use the outliner).

    """

def spring(q=1,e=1,add=1,all=1,ct=1,d="float",dPS="float",efw="float",exc=1,l="float",mxd="float",mnd="float",mm=1,n="string",nd=1,rl="float",rPS="float",sfw="float",s="float",sPS="float",udp=1,urp=1,usp=1,wl="uint",wf=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/spring.html



-----------------------------------------

spring is undoable, queryable, and editable.

The spring command can do any of the following:

* create a new spring object (shape plus transform). The shape contains springs between the points (particles, cvs, etc.) of the objects selected or listed on the command line.

* create new springs and add them to an existing spring object

* edit or query certain attributes of an existing spring object

One "spring object" may have hundreds or even thousands of individual springs.
Certain attributes of the spring object specify exactly where the springs are
attached to which other objects.

Springs may be attached to the following: particles, vertices of soft bodies,
CVs or edit points of curves or surfaces, vertices of polygonal objects, and
points of lattices. In the case where one endpoint of a spring is non-dynamic
(a CV, edit point, etc.), the spring does not affect its motion, but the
motion of the point affects the spring. A spring will be created only if at
least one of the endpoints is dynamic: for example, a spring will never be
created between two CVs. A single spring object can hold springs which are
incident to any number of other objects.

The spring has creation-only flags and editable flags. Creation-only flags
(minDistance, maxDistance, add, exclusive, all, wireframe, walklength,
checkExisting) can be used only when creating new springs (including adding
springs to existing spring object). Editable flags modify attributes of an
existing spring object.

If a spring object is created, this command returns the names of the shape and
transform. If a spring object is queried, the command returns the results of
the query.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

add   : addSprings      [boolean] []
    If specified, springs will be added to the existing selected set of springs. (Default is to create a new spring object.)

-----------------------------------------

all   : allPoints       [boolean] ['edit']
    If True, sets the mode of spring application to All. This will add springs between all points selected. (Default is False.)

-----------------------------------------

ct    : count           [boolean] ['query']
    Return the number of springs in the shape. Query-only. We maintain this flag only for compatibility with earlier versions of Maya. To get the count of springs, it is much faster and simpler to use the spring shape's count attribute: getAttr <shapeName>.count.

-----------------------------------------

d     : damping         [float] ['query', 'edit']
    Damping factor for the springs created in the spring object. (Default = 0.2 )

-----------------------------------------

dPS   : dampingPS       [float] ['query', 'edit']
    Damping factor for the springs created in the spring object. This will initialize all the entries in dampingPS to the specified value. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = 0.2 )

-----------------------------------------

efw   : endForceWeight  [float] ['query', 'edit']
    Amount of the force of the spring that gets applied to the point to which the spring ends. Valid range is from 0.0 to 1.0. (Default = 1.0 )

-----------------------------------------

exc   : exclusive       [boolean] []
    If true, tells the command to create springs only between pairs of points which are not in the same object. (Default is False.)

-----------------------------------------

l     : length          [float] ['query', 'edit']
    Vestigial form of "restLength." Please use "restLength" instead.

-----------------------------------------

mxd   : maxDistance     [float] ['edit']
    Maximum distance between two points that a spring would be considered.

-----------------------------------------

mnd   : minDistance     [float] []
    Minimum distance between two points that a spring would be considered. (Default = 0.0. See Defaults for more information on this flag's default.)

-----------------------------------------

mm    : minMax          [boolean] []
    If True, sets the mode of the spring application to Min/Max. This will add springs between all points from the specified point groups that are between the minimum and maximum distance values set with min and max. (Default is False.) Note: This gets automatically set if either the min or max flags are used.

-----------------------------------------

n     : name            [string] ['query']
    Name of spring object.

-----------------------------------------

nd    : noDuplicate     [boolean] []
    Check for existing springs and don't add a new spring between two points already connected by a spring in the same object. Only the object the command is working on is checked. This flag is relevant only when using -add. (Default = false)

-----------------------------------------

rl    : restLength      [float] ['query', 'edit']
    Per-object rest length for the new springs. Springs can use either their per-object or per-spring rest length. See the -lPS and -ulp flags.

-----------------------------------------

rPS   : restLengthPS    [float] ['query', 'edit']
    Per-spring rest length for the new springs. This will initialize all the entries in restLengthPS to the specified value. If this flag is not thrown, each rest length will be initialized to the distance between the two points at the time the spring is created (i.e., the initial length of the spring). When playing back, springs can use either their per-spring or per-object rest length. See the -rl and -urp flags. In both the flag and the attribute name, "PS" stands for "per-spring."

-----------------------------------------

sfw   : startForceWeight [float] ['query', 'edit']
    Amount of the force of the spring that gets applied to the point from which the spring starts. Valid range is from 0.0 to 1.0. (Default = 1.0 )

-----------------------------------------

s     : stiffness       [float] ['query', 'edit']
    Stiffness of the springs created in the spring object. (Default = 1.0 ) -damp float Vestigial form of "damping." Please use "damping" instead.

-----------------------------------------

sPS   : stiffnessPS     [float] ['query', 'edit']
    Stiffness of the springs created in the spring object. This will initialize all the entries in stiffnessPS to the specified value. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = 1.0 )

-----------------------------------------

udp   : useDampingPS    [boolean] ['query', 'edit']
    Specifies whether to use dampingPS (per spring damping). If set to false, the per object damping attribute value will be used. This flag simply sets the useDampingPS attribute of the spring shape. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = false )

-----------------------------------------

urp   : useRestLengthPS [boolean] ['query', 'edit']
    Specifies whether to use restLengthPS (per spring restLength). If set to false, the per object restLength attribute value will be used. This flag simply sets the useRestLengthPS attribute of the spring shape. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = false )

-----------------------------------------

usp   : useStiffnessPS  [boolean] ['query', 'edit']
    Specifies whether to use stiffnessPS (per spring stiffness). If set to false, the per object stiffness attribute value will be used. This flag simply sets the useStiffnessPS attribute of the spring shape. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = false )

-----------------------------------------

wl    : walkLength      [uint] []
    This flag is valid only when doing wireframe creation. It will create springs between pairs of points connected by the specified number of edges. For example, if walk length is 2, each pair of points separated by no more than 2 edges will get a spring. Walk length measures the distance between pairs of vertices just like the number of blocks measures the distance between two intersections in a city.

-----------------------------------------

wf    : wireframe       [boolean]
    If True, sets the mode of the spring application to Wireframe. This is valid only for springs created on a soft body. It will add springs along all edges connecting the adjacent points (vertices or CV's) of curves and surfaces. (Default is False.)

    """

def turbulence(q=1,e=1,att="float",f="float",m="float",mxd="linear",n="string",nsl="int",nsr="float",pv=1,p="float",px="float",py="float",pz="float",pos="[linear, linear, linear]",tsr="linear",vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/turbulence.html



-----------------------------------------

turbulence is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. A turbulence field causes
irregularities (also called 'noise' or 'jitter') in the motion of affected
objects.

Use connectDynamic to cause the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

f     : frequency       [float] ['query', 'edit']
    Frequency of turbulence field. This determines how often motion is disrupted.

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

nsl   : noiseLevel      [int] ['query', 'edit']
    If the noiseLevel parameter is greater than zero, the field will do multiple lookups in the table. Each additional lookup is weighted using noiseRatio (which see). The noiseLevel is the number of additional lookups, so if noiseLevel is 0, there is just one lookup. A value of 0 (the default) corresponds to the way the field behaved prior to Maya 3.0.

-----------------------------------------

nsr   : noiseRatio      [float] ['query', 'edit']
    If noiseLevel is greater than zero, then noiseRatio is the relative magnitude for each consecutive noise evaluation. These are cumulative: for example, if noiseRatio is 0.5, then the first evaluation is weighted 0.5, the second 0.25, and so on. Has no effect if noiseLevel is zero.

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

p     : phase           [float] ['query', 'edit']
    Phase shift of turbulence field. This influences the direction of the disruption. This flag is obsolete and is retained only for backward compatibility. It is replaced by -phaseX, -phaseY, and -phaseZ. Setting -phase is identical to setting -phaseZ (the phase shift was always in the Z dimension).

-----------------------------------------

px    : phaseX          [float] ['query', 'edit']
    X component of phase shift of turbulence field. This influences the direction of the disruption.

-----------------------------------------

py    : phaseY          [float] ['query', 'edit']
    Y component of phase shift of turbulence field. This influences the direction of the disruption.

-----------------------------------------

pz    : phaseZ          [float] ['query', 'edit']
    Z component of phase shift of turbulence field. This influences the direction of the disruption.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def uniform(q=1,e=1,att="float",dx="float",dy="float",dz="float",m="float",mxd="linear",n="string",pv=1,pos="[linear, linear, linear]",tsr="linear",vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/uniform.html



-----------------------------------------

uniform is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. A uniform field pushes objects in a
fixed direction. The field strength, but not the field direction, depends on
the distance from the object to the field location.

The transform is the associated dependency node. Use connectDynamic to cause
the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

dx    : directionX      [float] ['query', 'edit']
    X-component of direction.

-----------------------------------------

dy    : directionY      [float] ['query', 'edit']
    Y-component of direction.

-----------------------------------------

dz    : directionZ      [float] ['query', 'edit']
    Z-component of direction

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def volumeAxis(q=1,e=1,alx="float",arx="float",att="float",afx="float",afc="float",dtr="float",dx="float",dy="float",dz="float",drs="float",ia=1,m="float",mxd="linear",n="string",pv=1,pos="[linear, linear, linear]",tsr="linear",trb="float",tfx="float",tfy="float",tfz="float",tox="float",toy="float",toz="float",trs="float",vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/volumeAxis.html



-----------------------------------------

volumeAxis is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. A volume axis field can push
particles in four directions, defined with respect to a volume: along the
axis, away from the axis or center, around the axis, and in a user-specified
direction. These are analogous to the emission speed controls of volume
emitters. The volume axis field also contains a wind turbulence model
(different from the turbulence field) that simulates an evolving flow of
liquid or gas. The turbulence has a build in animation that is driven by a
connection to a time node.

The transform is the associated dependency node. Use connectDynamic to cause
the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

alx   : alongAxis       [float] ['query', 'edit']
    Initial velocity multiplier in the direction along the central axis of the volume. See the diagrams in the documentation.

-----------------------------------------

arx   : aroundAxis      [float] ['query', 'edit']
    Initial velocity multiplier in the direction around the central axis of the volume. See the diagrams in the documentation.

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

afx   : awayFromAxis    [float] ['query', 'edit']
    Initial velocity multiplier in the direction away from the central axis of the volume. See the diagrams in the documentation. Used only with the cylinder, cone, and torus volumes.

-----------------------------------------

afc   : awayFromCenter  [float] ['query', 'edit']
    Initial velocity multiplier in the direction away from the center point of a cube or sphere volume. Used only with the cube and sphere volumes.

-----------------------------------------

dtr   : detailTurbulence [float] ['query', 'edit']
    The relative intensity of a second higher frequency turbulence. This can be used to create fine features in large scale flows. Both the speed and the frequency on this second turbulence are higher than the primary turbulence. When the detailTurbulence is non-zero the simulation may run a bit slower, due to the computation of a second turbulence.

-----------------------------------------

dx    : directionX      [float] ['query', 'edit']
    x-component of force direction. Used with directional speed.

-----------------------------------------

dy    : directionY      [float] ['query', 'edit']
    y-component of force direction. Used with directional speed.

-----------------------------------------

dz    : directionZ      [float] ['query', 'edit']
    z-component of force direction. Used with directional speed.

-----------------------------------------

drs   : directionalSpeed [float] ['query', 'edit']
    Adds a component of speed in the direction specified by the directionX, Y, and Z attributes.

-----------------------------------------

ia    : invertAttenuation [boolean] ['query', 'edit']
    If this attribute is FALSE, the default, then the attenuation makes the field's effect decrease as the affected point is further from the volume's axis and closer to its edge. If the is set to TRUE, then the effect of the field increases in this case, making the full effect of the field felt at the volume's edge.

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

trb   : turbulence      [float] ['query', 'edit']
    Adds a force simulating a turbulent wind that evolves over time.

-----------------------------------------

tfx   : turbulenceFrequencyX [float] ['query', 'edit']
    The repeats of the turbulence function in X.

-----------------------------------------

tfy   : turbulenceFrequencyY [float] ['query', 'edit']
    The repeats of the turbulence function in Y.

-----------------------------------------

tfz   : turbulenceFrequencyZ [float] ['query', 'edit']
    The repeats of the turbulence function in Z.

-----------------------------------------

tox   : turbulenceOffsetX [float] ['query', 'edit']
    The translation of the turbulence function in X.

-----------------------------------------

toy   : turbulenceOffsetY [float] ['query', 'edit']
    The translation of the turbulence function in Y.

-----------------------------------------

toz   : turbulenceOffsetZ [float] ['query', 'edit']
    The translation of the turbulence function in Z.

-----------------------------------------

trs   : turbulenceSpeed [float] ['query', 'edit']
    The rate of change of the turbulence over time. The turbulence loops seamlessly every 1.0/turbulenceSpeed seconds. To animate this rate attach a new time node to the time input on the volumeAxisNode then animate the time value on the time node.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def vortex(q=1,e=1,att="float",ax="float",ay="float",az="float",m="float",mxd="linear",n="string",pv=1,pos="[linear, linear, linear]",tsr="linear",vex=1,vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/vortex.html



-----------------------------------------

vortex is undoable, queryable, and editable.

For each listed object, the command creates a new field. The field has a shape
which lives in the DAG and it has an associated dependency node. The field is
added to the list of fields owned by the object. Use connectDynamic to cause
the field to affect a dynamic object. Note that if more than one object is
listed, a separate field is created for each object.

If fields are created, this command returns the names of each owning shape and
of the field shapes themselves. If a field was queried, the results of the
query are returned. If a field was edited, the field name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the list is
empty, the command defaults to -pos 0 0 0. A vortex field pulls objects in a
circular direction, like a whirlpool or tornado. Objects affected by the
vortex field tend to rotate around the axis specified by -ax, -ay, and -az.

The transform is the associated dependency node. Use connectDynamic to cause
the field to affect a dynamic object.

If fields are created, this command returns the names of each of the fields.
If a field was queried, the results of the query are returned. If a field was
edited, the field name is returned.

If object names are provided or the active selection list is non-empty, the
command creates a field for every object in the list and calls addDynamic to
add it to the object. If the list is empty, the command defaults to -pos 0 0
0.

Setting the -pos flag with objects named on the command line is an error.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

att   : attenuation     [float] ['query', 'edit']
    Attentuation rate of field

-----------------------------------------

ax    : axisX           [float] ['query', 'edit']
    X-component of vortex axis

-----------------------------------------

ay    : axisY           [float] ['query', 'edit']
    Y-component of vortex axis

-----------------------------------------

az    : axisZ           [float] ['query', 'edit']
    Z-component of vortex axis

-----------------------------------------

m     : magnitude       [float] ['query', 'edit']
    Strength of field.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of field

-----------------------------------------

pv    : perVertex       [boolean] ['query', 'edit']
    Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

vex   : volumeExclusion [boolean] ['query', 'edit']
    Volume exclusion of the field. If true, points outside the volume (defined by the volume shape attribute) are affected, If false, points inside the volume are affected. Has no effect if volumeShape is set to "none."

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the field. Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the field. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the field. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def nBase(q=1,e=1,cct="string",cs=1,ss=1,ttv="string"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nBase.html



-----------------------------------------

nBase is undoable, queryable, and editable.

Edits one or more nBase objects. Note that nBase objects include nCloth,
nRigid and nParticle objects, but the options on this command do not currently
apply to nParticle objects.


-----------------------------------------


Return Value:

boolean  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cct   : clearCachedTextureMap [string] ['edit']
    Clear the cached texture map for the specified attribute from the nBase.

-----------------------------------------

cs    : clearStart      [boolean] ['edit']
    Indicates that start state should be cleared

-----------------------------------------

ss    : stuffStart      [boolean] ['edit']
    Indicates that current state should be stuffed into the start state

-----------------------------------------

ttv   : textureToVertex [string]
    Transfer the texture map data for the specified attribute into the related per-vertex attribute.

    """

def nParticle(q=1,e=1,at="string",ch=1,c="float",ct=1,dc=1,dal=1,fv="float",grs="linear",i="float",jbp="[linear, linear, linear]",jr="linear",ll="[linear, linear, linear]",n="string",nj="uint",order="int",id="int",ppd=1,ppv=1,p="[linear, linear, linear]",sn="string",ur="[linear, linear, linear]",vv="[float, float, float]"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nParticle.html



-----------------------------------------

nParticle is undoable, queryable, and editable.

The nParticle command creates a new nParticle object from a list of world
space points. If an nParticle object is created, the command returns the names
of the new particle shape and its associated particle object dependency node.
If an object was queried, the results of the query are returned. Per particle
attributes can be queried using the particleId or the order of the particle in
the particle array. If an object was edited, nothing is returned.


-----------------------------------------


Return Value:

string  The name of the nParticle object created    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] ['query', 'edit']
    Used in per particle attribute query and edit. Specifies the name of the attribute being queried or edited.  In query mode, this flag needs a value.

-----------------------------------------

ch    : cache           [boolean] ['query', 'edit']
    Turns caching on/off for the particle shape.

-----------------------------------------

c     : conserve        [float] ['query', 'edit']
    Conservation of momentum control (between 0 and 1). Specifies the fraction of the particle shape's existing momentum which is conserved from frame to frame. A value of 1 (the default) corresponds to true Newtonian physics, in which momentum is conserved.

-----------------------------------------

ct    : count           [boolean] ['query']
    Returns the number of particles in the object.

-----------------------------------------

dc    : deleteCache     [boolean] []
    Deletes the particle shapes cache. This command is not undoable.

-----------------------------------------

dal   : dynamicAttrList [boolean] ['query']
    Returns a list of the dynamic attributes in the object.

-----------------------------------------

fv    : floatValue      [float] ['edit']
    Used only in per particle attribute edit. Specifies that the edit is of a float attribute and must be followed by the new float value.

-----------------------------------------

grs   : gridSpacing     [linear] ['query']
    Spacing between particles in the grid.

-----------------------------------------

i     : inherit         [float] ['query', 'edit']
    Inherit this fraction (0-1) of emitting object's velocity.

-----------------------------------------

jbp   : jitterBasePoint [[linear, linear, linear]] ['query']
    Base point (center point) for jitters. The command will create one swatch of jitters for each base point. It will pair up other flags with base points in the order they are given in the command line. If not enough instances of the other flags are availble, the last one on the line with be used for all other instances of -jpb.

-----------------------------------------

jr    : jitterRadius    [linear] ['query']
    Max radius from the center to place the particle instances.

-----------------------------------------

ll    : lowerLeft       [[linear, linear, linear]] ['query']
    Lower left point of grid.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    name of particle object

-----------------------------------------

nj    : numJitters      [uint] ['query']
    Number of jitters (instances) per particle.

-----------------------------------------

order : order           [int] ['query', 'edit']
    Used in per particle attribute query and edit. Specifies the zero-based order (index) of the particle whose attribute is being queried or edited in the particle array. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.  In query mode, this flag needs a value.

-----------------------------------------

id    : particleId      [int] ['query', 'edit']
    Used in per particle attribute query and edit. Specifies the id of the particle whose attribute is being queried or edited. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.  In query mode, this flag needs a value.

-----------------------------------------

ppd   : perParticleDouble [boolean] ['query']
    Returns a list of the per-particle double attributes, excluding initial- state, cache, and information-only attributes.

-----------------------------------------

ppv   : perParticleVector [boolean] ['query']
    Returns a list of the per-particle vector attributes, excluding initial- state, cache, and information-only attributes.

-----------------------------------------

p     : position        [[linear, linear, linear]] []
    World-space position of each particle.

-----------------------------------------

sn    : shapeName       [string] ['query', 'edit']
    Specify the shape name used for geometry instancing. DO not confuse this with the -n flag which names the particle object.

-----------------------------------------

ur    : upperRight      [[linear, linear, linear]] ['query']
    Upper right point of grid.

-----------------------------------------

vv    : vectorValue     [[float, float, float]]
    Used only in per particle attribute edit. Specifies that the edit is of a vector attribute and must be followed by all three float values for the vector.

    """

def nSoft(q=1,c=1,d=1,dh=1,g="float",h=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/nSoft.html



-----------------------------------------

nSoft is undoable, queryable, and NOT editable.

Makes a nSoft body from the object(s) passed on the command line or in the
selection list. The geometry can be a NURBS, polygonal, lattice object. The
resulting nSoft body is made up of a hierarchy with a particle shape and a
geometry shape, thus:

    
    
                     
    
    
                T    
    
    
                / \  
    
    
               T   G 
    
    
              /      
    
    
            P        
    
    
                     

Dynamics are applied to the particle shape and the resulting particle
positions then drive the locations of the geometry's CVs, vertices, or lattice
points.

With the convert option, the particle shape and its transform are simply
inserted below the original shape's hierarchy. With the duplicate option, the
original geometry's transform and shape are duplicated underneath its parent,
and the particle shape is placed under the duplicate. Note that any animation
on the hierarchy will affect the particle shape as well. If you do not want
them, then reparent the structure outside the hierarchy.

When duplicating, the nSoft portion (the duplicate) is given the name "copyOf"
\+ "original object name". The particle portion is always given the name
"original object name" \+ "Particles."

None of the flags of the nSoft command can be queried. The nSoft -q command is
used only to identify when an object is a nSoft body, or when two objects are
part of the same nSoft body. See the examples.


-----------------------------------------


Return Value:

string  array    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

c     : convert         [boolean] []
    This tells the command that you want the original object to be the actual deformed object. The particle shape portion of the nSoft body will be inserted in the same hierarchy as the original, under the same parent (with one additional intervening transform which is initially the identity). If no flags are passed, then this is assumed. The combination -c -h 1 is not valid; if you have this in your scripts, remove the -h 1.

-----------------------------------------

d     : duplicate       [boolean] []
    This tells the command that you want to make a copy of the original object and use the copy as the deforming geometry. Input connections to the original object are duplicated. You would do this if you wanted to keep the original object in your scene and also have a copy of it that was a nSoft body. This flag and -dh are mutually exclusive.

-----------------------------------------

dh    : duplicateHistory [boolean] []
    This is the same as -d, except that upstream history, is duplicated as well, instead of just input connections. This flag and -d are mutually exclusive.

-----------------------------------------

g     : goal            [float] []
    This is the same as -d, but in addition it tells the command that you want the resulting nSoft body to try to follow the original geometry, using the set goal weight as the value that controls how strongly it is to follow it. A value of 1.0 will try to follow exactly, and a value of 0.0 will not follow at all. The default value is 0.5. This value must be from 0.0 to 1.0. You could use -d with -g, but it is redundant. If you want history to be duplicated, you can use -dh and -g together.

-----------------------------------------

h     : hideOriginal    [boolean]
    This flag is used only when duplicating (-d, -g, or -dh). If set to true, whichever of the two objects is NOT the nSoft object will be hidden. In other words, with -d -h true, the original object will be hidden; with -d -c -h 1 the duplicate object will be hidden. You would typically do this if you want to use the non-dynamic object as a goal for the nSoft one (see -g) but you do not want it visible in the scene. The flags -h 1 and -c are mutually exclusive.

    """

def dynPaintEditor(q=1,e=1,ao=1,autoSave=1,cam="string",cm=1,cu=1,cc="[string, string, string, string]",cl="[float, float, float]",ctl=1,ccs=1,dt="string",dsa="string",dfg=1,di="int",dsl="string",dst="string",dtx=1,dtg="string",dbf=1,da=1,drc=1,ex=1,fu="int",fil="string",f="string",fmc="string",hlc="string",ig=1,li="string",lck=1,mlc="string",mn="string",nim=1,ni="[int, int, float, float, float]",pa="float",pnl="string",p="string",rl=1,ref=1,rmd="int",ra=1,ri=1,rig="[float, float]",sa=1,sbm="string",si=1,sb="float",sg="float",sr="float",slc="string",sbf=1,snp=1,sts=1,swp="int",ts="int",up=1,uc=1,ulk=1,upd=1,ut="string",wr="[boolean, boolean]",wi="string",zm="float"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/dynPaintEditor.html



-----------------------------------------

dynPaintEditor is undoable, queryable, and editable.

Create a editor window that can be painted into


-----------------------------------------


Return Value:

string  Editor name    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ao    : activeOnly      [boolean] ['query', 'edit']
    For Scene mode, this determines if only the active strokes will be refreshed.

-----------------------------------------

autoSave : autoSave        [boolean] ['query', 'edit']
    For Canvas mode, this determines if the buffer will be saved to a disk file after every stroke. Good for painting textures and viewing the results in shaded display in the model view.

-----------------------------------------

cam   : camera          [string] ['query', 'edit']
    Sets the name of the camera which the Paint Effects panel looks through.

-----------------------------------------

cm    : canvasMode      [boolean] ['query', 'edit']
    Sets the Paint Effects panel into Canvas mode if true.

-----------------------------------------

cu    : canvasUndo      [boolean] ['edit']
    Does a fast undo in Canvas mode. This is a special undo because we are not using any history when we paint in Canvas mode so we provide a single level undo for the Canvas.

-----------------------------------------

cc    : changeCommand   [[string, string, string, string]] ['query', 'edit']
    Parameters:    * First string: command   * Second string: editorName   * Third string: editorCmd   * Fourth string: updateFunc  Call the command when something changes in the editor The command should have this prototype :   command(string $editor, string $editorCmd, string $updateFunc, int $reason)   The possible reasons could be :    * 0: no particular reason   * 1: scale color   * 2: buffer (single/double)   * 3: axis    * 4: image displayed   * 5: image saved in memory

-----------------------------------------

cl    : clear           [[float, float, float]] ['edit']
    Clears the buffer (if in Canvas mode) to the floating point values (R,G,B).

-----------------------------------------

ctl   : control         [boolean] ['query']
    Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.

-----------------------------------------

ccs   : currentCanvasSize [boolean] ['query']
    In Query mode, this returns the (X,Y) resolution of the current canvas.

-----------------------------------------

dt    : defineTemplate  [string] []
    Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.

-----------------------------------------

dsa   : displayAppearance [string] ['query', 'edit']
    Sets the display appearance of the model panel. Possible values are "wireframe", "points", "boundingBox", "smoothShaded", "flatShaded". This flag may be used with the -interactive and -default flags. Note that only "wireframe", "points", and "boundingBox" are valid for the interactive mode.

-----------------------------------------

dfg   : displayFog      [boolean] ['query', 'edit']
    For Scene mode, this determines if fog will be displayed in the Paint Effects panel when refreshing the scene. If fog is on, but this is off, fog will only be drawn on the strokes, not the rest of the scene.

-----------------------------------------

di    : displayImage    [int] ['query', 'edit']
    Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.

-----------------------------------------

dsl   : displayLights   [string] ['query', 'edit']
    Sets the lighting for shaded mode. Possible values are "selected", "active", "all", "default".

-----------------------------------------

dst   : displayStyle    [string] ['query', 'edit']
    Set the mode to display the image. Valid values are:    * "color" to display the basic RGB image   * "mask" to display the mask channel   * "lum" to display the luminance of the image

-----------------------------------------

dtx   : displayTextures [boolean] ['query', 'edit']
    Turns on or off display of textures in shaded mode

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

drc   : drawContext     [boolean] ['query']
    Returns the name of the context.

-----------------------------------------

ex    : exists          [boolean] []
    Returns whether the specified object exists or not. Other flags are ignored.

-----------------------------------------

fu    : fastUpdate      [int] []
    Obsolete - do not use

-----------------------------------------

fil   : fileName        [string] ['query', 'edit']
    This sets the file to which the canvas will be saved.

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

ig    : iconGrab        [boolean] ['edit']
    This puts the Paint Effects panel into Grab Icon mode where the user is expected to drag out a section of the screen to be made into an icon.

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

mn    : menu            [string] []
    Sets the name of the script used to build a menu in the editor. The script takes the editor name as an argument.

-----------------------------------------

nim   : nbImages        [boolean] ['query']
    returns the number of images

-----------------------------------------

ni    : newImage        [[int, int, float, float, float]] ['query', 'edit']
    Starts a new image in edit mode, setting the resolution to the integer values (X,Y) and clearing the buffer to the floating point values (R,G,B). In Query mode, this returns the (X,Y) resolution of the current Image.

-----------------------------------------

pa    : paintAll        [float] ['edit']
    Redraws the buffer in current refresh mode.

-----------------------------------------

pnl   : panel           [string] ['query']
    Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.

-----------------------------------------

p     : parent          [string] ['query', 'edit']
    Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.

-----------------------------------------

rl    : redrawLast      [boolean] ['edit']
    Redraws the last stroke again. Useful when it's brush has just changed. This feature does a fast undo and redraws the stroke again.

-----------------------------------------

ref   : refresh         [boolean] ['edit']
    requests a refresh of the current Editor Image.

-----------------------------------------

rmd   : refreshMode     [int] ['query', 'edit']
    Sets the refresh mode to the specified value. 0 - Do not draw strokes on refresh, 1 - Redraw strokes in wireframe mode, 2 - Redraw strokes in final rendered mode.

-----------------------------------------

ra    : removeAllImages [boolean] ['edit']
    remove all the Editor Images from the Editor Image Stack

-----------------------------------------

ri    : removeImage     [boolean] ['edit']
    remove the current Editor Image from the Editor Image Stack

-----------------------------------------

rig   : rollImage       [[float, float]] ['edit']
    In Canvas mode, this rolls the image by the floating point values (X,Y). X and Y are between 0 (no roll) and 1 (full roll). A value of .5 rolls the image 50% (ie. the border moves to the center of the screen.

-----------------------------------------

sa    : saveAlpha       [boolean] ['query', 'edit']
    For Canvas mode, this determines if the alpha will be saved when storing the canvas to a disk file.

-----------------------------------------

sbm   : saveBumpmap     [string] ['query', 'edit']
    Saves the current buffer as a bump map to the specified file.

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

sbf   : singleBuffer    [boolean] ['query', 'edit']
    Set the display in single buffer mode

-----------------------------------------

snp   : snapShot        [boolean] ['edit']
    Takes a snapshot of the current camera view.

-----------------------------------------

sts   : stateString     [boolean] ['query']
    Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.

-----------------------------------------

swp   : swap            [int] []
    Obsolete - do not use

-----------------------------------------

ts    : tileSize        [int] ['edit']
    Sets the size of the tile for the hardware texture redraw of the display buffer.

-----------------------------------------

up    : unParent        [boolean] ['edit']
    Specifies that the editor should be removed from its layout. This cannot be used in query mode.

-----------------------------------------

uc    : undoCache       [boolean] ['edit']
    By default the last image is cached for undo. If this is set false, then undoing will be disabled in canvas mode and undo in scene mode will force a full refresh. Less memory will be used if this is set false before the first clear or refresh of the current scene.

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

wr    : wrap            [[boolean, boolean]] ['query', 'edit']
    For Canvas mode, should the buffer wrap in U, and V (respectively) when painting.

-----------------------------------------

wi    : writeImage      [string] ['edit']
    write the current Editor Image to disk

-----------------------------------------

zm    : zoom            [float]
    Zooms the Canvas image by the specified value.

    """

def getDefaultBrush():
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getDefaultBrush.html



-----------------------------------------

getDefaultBrush is undoable, NOT queryable, and NOT editable.

The command returns the name of the default Paint Effects brush.


-----------------------------------------


Return Value:

string  Name of the default brush node
    """

def paintEffectsDisplay(q=1,me=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/paintEffectsDisplay.html



-----------------------------------------

paintEffectsDisplay is NOT undoable, queryable, and NOT editable.

Command to set the global display methods for paint effects items


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

me    : meshDrawEnable  [boolean]
    Set whether mesh draw is enabled on objects

    """

def pfxstrokes(fn="string",pc=1,sl=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/pfxstrokes.html



-----------------------------------------

pfxstrokes is NOT undoable, NOT queryable, and NOT editable.

This command will loop through all the Paint Effects strokes, including
pfxHair nodes, and write the current state of all the tubes to a file. For
normal stroke nodes tubes must be ON in the brush or there will be no output.
For pfxHair nodes there will always be output, but the format is different
than for stroke nodes(however one can assign a brush with tubes = ON to a
pfxHair node, in which case it will output the same format as strokes). The
general file format is ASCII, using commas to separate numerical values and
newlines between blocks of data. The format used for pfxHair nodes presents
the hair curves points in order from root to tip of the hair. The hairs follow
sequentially in the following fashion: NumCvs pointX,pointY,pointZ,
normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU
pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB,
paramU etc... NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width,
colorR,colorG,colorB, paramU etc.. The format used to output files for brushes
with tubes=ON is more complex. The tubes can branch and the order the segments
are written is the same order they are drawn in. Slowly drawing a tall grass
brush in the paint effects panel can help to illustrate the order the segments
will appear in the file. New tubes can start "growing" before others are
finished. There is no line for "NumCvs". Instead all data for each segment
appears on each line. The data on each line is the same as passed into the
paint effects runtime function. See the argument list of paintRuntimeFunc.mel
for the order and a description of these parameters. The parameters match up
exactly in the order they appear on a line of the output file with the order
of arguments to this function. If one wishes to parse the output file and
connect the segments together into curves the branchId, parentId and
siblingCnt parameters can help when sorting which segment connects to which
line. Using the -postCallback option will write out the tubes data after it
has been proessed by the runTime callback.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

fn    : filename        [string] []
    The output file.

-----------------------------------------

pc    : postCallback    [boolean] []
    Output information to the file after the Runtime Callback MEL function has been invoked. The default is to output the information prior to the callback.

-----------------------------------------

sl    : selected        [boolean]
    Only loop through the selected strokes.

    """

def stroke(n="string",pr=1,s="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/stroke.html



-----------------------------------------

stroke is undoable, NOT queryable, and NOT editable.

The stroke command creates a new Paint Effects stroke node.


-----------------------------------------


Return Value:

string  (The path to the new stroke or the replaced stroke)


-----------------------------------------


Flags:

-----------------------------------------

n     : name            [string] []
    Sets the name of the stroke to the input string

-----------------------------------------

pr    : pressure        [boolean] []
    On creation, allows the copying of the pressure mapping settings from the Paint Effects Tool. Default is false.

-----------------------------------------

s     : seed            [int]
    Sets the random seed for this stroke.

    """

def colorAtPoint(u="float",v="float",xu="float",xv="float",mu="float",mv="float",o="string",su="uint",sv="uint"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/colorAtPoint.html



-----------------------------------------

colorAtPoint is NOT undoable, NOT queryable, and NOT editable.

The colorAtPoint command is used to query textures or ocean shaders at passed
in uv coordinates. (For ocean shaders uv is x and z in worldspace ). The
return value is a floating point array whose size is determined by either the
number of input uv arguments passed in and the the queried value. One can
query alpha only, rgb only, or rgba values. The returned array is only single
indexed, so if rgb is specified then the index for red values would be index *
3. Blue is index * 3 + 1, and green is index * 3 + 2. For rgba use a multiple
of 4 instead of 3. For alpha only one can simply use the index. There are two
basic argument formats that may be used: colorAtPoint -u 0 -v 0 -u .2 -v .1
etc.. for all points or colorAtPoint -mu 0 -mv 0 -xu 1 -xv 1 -su 10 -sv 10 //
samples 100 points If one is sampling several points and they are all in a
regular grid formation it is more efficient to call this routine with the
latter method, which uses a min/max uv and number of samples, rather than a
long argument list of uv coords.

  * return values (-o A or RGB or RGBA )
  * individual UV coordinates to sample (-u float -v float )
  * (numbers of calls to -u and -v must match)
  * uniform grid of points to sample (-su int -sv int)
  * (may not use this in combination with -u or -v)
  * bounds for sample grid (-mu float -mv float -xu float -xv float)


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

u     : coordU          [float] []
    Input u coordinate to sample texture at.

-----------------------------------------

v     : coordV          [float] []
    Input v coordinate to sample texture at.

-----------------------------------------

xu    : maxU            [float] []
    DEFAULT 1.0 Maximum u bounds to sample.

-----------------------------------------

xv    : maxV            [float] []
    DEFAULT 1.0 Maximum v bounds to sample.

-----------------------------------------

mu    : minU            [float] []
    DEFAULT 0.0 Minimum u bounds to sample.

-----------------------------------------

mv    : minV            [float] []
    DEFAULT 0.0 Minimum v bounds to sample.

-----------------------------------------

o     : output          [string] []
    Type of data to output: A = alpha only RGB = color only RGBA = color and alpha

-----------------------------------------

su    : samplesU        [uint] []
    DEFAULT 1 The number of points to sample in the U dimension.

-----------------------------------------

sv    : samplesV        [uint]
    DEFAULT 1 The number of points to sample in the V dimension.

    """

def fluidCacheInfo(q=1,e=1,at="string",t="time",ef=1,hc=1,hd=1,ic=1,pb=1,re=1,sf=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fluidCacheInfo.html



-----------------------------------------

fluidCacheInfo is undoable, queryable, and editable.

A command to get information about the fluids cache. Get the startFrame and
resolution for InitialConditions. Get the endFrame as well for a playback
cache. Note that for the playback cache, it will look at the current time (or
last frame if the current time is past end of cache)


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] ['query', 'edit']
    Modifier to the "hasData" flag, used to query whether a cache has data (at the current time) for a specific fluid attribute. Valid attribute values are "density", "velocity", "temperature", "fuel", "color", "coordinates" (for texture coordinates), "falloff".

-----------------------------------------

t     : cacheTime       [time] ['query', 'edit']
    Only valid with the -hasData flag. The time the -hasData flag uses when it queries the cache to see if there is data.

-----------------------------------------

ef    : endFrame        [boolean] ['query', 'edit']
    Returns end time of cache as float.

-----------------------------------------

hc    : hasCache        [boolean] ['query', 'edit']
    Returns true if fluid has specified cache, false if not.

-----------------------------------------

hd    : hasData         [boolean] ['query', 'edit']
    Queries whether a given cache has data in it at the time specified by the -time flag. (If not -time flag is present, -hasData assumes the current time.) When used with the "attribute" flag, indicates if data for the specified attribute exists in the cache. When used without the "attribute" flag, "hasData" indicates whether there is data in the cache for any of the valid fluid attributes.

-----------------------------------------

ic    : initialConditions [boolean] ['query', 'edit']
    Specifies the cache to be queried is the "Initial Conditions" cache.

-----------------------------------------

pb    : playback        [boolean] ['query', 'edit']
    Specifies the cache to be queried is the "Playback" cache.

-----------------------------------------

re    : resolution      [boolean] ['query', 'edit']
    Returns cache resolution as float[].

-----------------------------------------

sf    : startFrame      [boolean]
    Returns start time for cache as float.

    """

def fluidEmitter(q=1,e=1,cye="string",cyi="int",der="float",fdr="float",fer="float",her="float",mxd="linear",mnd="linear",n="string",pos="[linear, linear, linear]",r="float",tsr="linear",typ="string",vof="[linear, linear, linear]",vsh="string",vsw="angle"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fluidEmitter.html



-----------------------------------------

fluidEmitter is undoable, queryable, and editable.

Creates, edits or queries an auxiliary dynamics object (for example, a field
or emitter). Creates an emitter object. If object names are provided or if
objects are selected, applies the emitter to the named/selected object(s)in
the scene. Fluid will then be emitted from each. If no objects are named or
selected, or if the -pos option is specified, creates a positional emitter.

If an emitter was created, the command returns the name of the object owning
the emitter, and the name of emitter shape. If an emitter was queried, the
command returns the results of the query.


-----------------------------------------


Return Value:

string  Command result    
  
In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

cye   : cycleEmission   [string] ['query', 'edit']
    Possible values are "none" and "frame." Cycling emission restarts the random number stream after a specified interval. This can either be a number of frames or a number of emitted particles. In each case the number is specified by the cycleInterval attribute. Setting cycleEmission to "frame" and cycleInterval to 1 will then re-start the random stream every frame. Setting cycleInterval to values greater than 1 can be used to generate cycles for games work.

-----------------------------------------

cyi   : cycleInterval   [int] ['query', 'edit']
    Specifies the number of frames or particles between restarts of the random number stream. See cycleEmission. Has no effect if cycleEmission is set to None.

-----------------------------------------

der   : densityEmissionRate [float] ['query', 'edit']
    Rate at which density is emitted.

-----------------------------------------

fdr   : fluidDropoff    [float] ['query', 'edit']
    Fluid Emission Dropoff in volume

-----------------------------------------

fer   : fuelEmissionRate [float] ['query', 'edit']
    Rate at which is emitted.

-----------------------------------------

her   : heatEmissionRate [float] ['query', 'edit']
    Rate at which density is emitted.

-----------------------------------------

mxd   : maxDistance     [linear] ['query', 'edit']
    Maximum distance at which emission ends.

-----------------------------------------

mnd   : minDistance     [linear] ['query', 'edit']
    Minimum distance at which emission starts.

-----------------------------------------

n     : name            [string] ['query', 'edit']
    Object name

-----------------------------------------

pos   : position        [[linear, linear, linear]] ['query', 'edit']
    world-space position

-----------------------------------------

r     : rate            [float] ['query', 'edit']
    Rate at which particles emitted (can be non-integer). For point emission this is rate per point per unit time. For surface emission it is rate per square unit of area per unit time.

-----------------------------------------

tsr   : torusSectionRadius [linear] ['query', 'edit']
    Section radius for a torus volume. Applies only to torus. Similar to the section radius in the torus modelling primitive.

-----------------------------------------

typ   : type            [string] ['query', 'edit']
    Type of emitter. The choices are omni | dir | direction | surf | surface | curve | curv. The default is omni. The full definition of these types are: omnidirectional point emitter, directional point emitter, surface emitter, or curve emitter.

-----------------------------------------

vof   : volumeOffset    [[linear, linear, linear]] ['query', 'edit']
    Volume offset of the emitter. Volume offset translates the emission volume by the specified amount from the actual emitter location. This is in the emitter's local space.

-----------------------------------------

vsh   : volumeShape     [string] ['query', 'edit']
    Volume shape of the emitter. Sets/edits/queries the field's volume shape attribute. If set to any value other than "none", determines a 3-D volume within which particles are generated. Values are: "cube," "sphere," "cylinder," "cone," "torus."

-----------------------------------------

vsw   : volumeSweep     [angle]
    Volume sweep of the emitter. Applies only to sphere, cone, cylinder, and torus. Similar effect to the sweep attribute in modelling.

    """

def fluidVoxelInfo(cb=1,ib="[int, int, int]",os=1,r="float",v="[float, float, float]",vc=1,xi="int",yi="int",zi="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/fluidVoxelInfo.html



-----------------------------------------

fluidVoxelInfo is NOT undoable, NOT queryable, and NOT editable.

Provides basic information about the mapping of a fluid voxel grid into world-
or object space of the fluid. Use this command to determine the center point
of a voxel, or to find the voxel containing a given point, among other things.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

cb    : checkBounds     [boolean] []
    If this flag is on, and the voxel index of a point that is out of bounds is requested, then we return nothing.

-----------------------------------------

ib    : inBounds        [[int, int, int]] []
    Are the three ints representing the x, y, z indices of a voxel within the bounds of the fluid's voxel grid? True if yes, false if not. (For 2D fluids, pass in z=0 for the third argument. See examples.)

-----------------------------------------

os    : objectSpace     [boolean] []
    Whether the queried value should be returned in object space (TRUE), or world space (FALSE, the default).

-----------------------------------------

r     : radius          [float] []
    Modifier for the -voxel flag. Returns a list of index triples identifying voxels that fall within the given radius of the point specified by the -voxel flag.

-----------------------------------------

v     : voxel           [[float, float, float]] []
    Returns array of three ints representing the x, y, z indices of the voxel within which the given point position is contained. If the checkBounds flag is on, and the point is out of bounds, we return nothing. Otherwise, even if the point is out of bounds, index values are returned. When combined with the -radius flag, returns an array of index triples representing a list of voxels within a given radius of the given point position.

-----------------------------------------

vc    : voxelCenter     [boolean] []
    The center position of the specified voxels. Returns an array of floats (three for each of the indices in the query). (Valid only with the -xIndex, -yIndex, and -zIndex flags.)

-----------------------------------------

xi    : xIndex          [int] []
    Only return values for cells with this X index

-----------------------------------------

yi    : yIndex          [int] []
    Only return values for cells with this Y index

-----------------------------------------

zi    : zIndex          [int]
    Only return values for cells with this Z index

    """

def getFluidAttr(at="string",lf=1,xi="int",x=1,yi="int",y=1,zi="int",z=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/getFluidAttr.html



-----------------------------------------

getFluidAttr is NOT undoable, NOT queryable, and NOT editable.

Returns values of built-in fluid attributes such as density, velocity, etc.,
for individual grid cells or for all cells in the grid.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

at    : attribute       [string] []
    Specifies the fluid attribute for which to display values. Valid attributes are "force", "velocity", "density", "falloff", "fuel", "color", and "temperature". (Note that getting force values is an alternate way of getting velocity values at one time step.)

-----------------------------------------

lf    : lowerFace       [boolean] []
    Only valid with "-at velocity". Since velocity values are stored on the edges of each voxel and not at the center, using voxel based indices to set velocity necessarily affects neighboring voxels. Use this flag to only set velocity components on the lower left three faces of a voxel, rather than all six.

-----------------------------------------

xi    : xIndex          [int] []
    Only return values for cells with this X index

-----------------------------------------

x     : xvalue          [boolean] []
    Only get the first component of the vector-valued attribute specified by the "-at/attribute" flag.

-----------------------------------------

yi    : yIndex          [int] []
    Only return values for cells with this Y index

-----------------------------------------

y     : yvalue          [boolean] []
    Only get the second component of the vector-valued attribute specified by the "-at/attribute" flag.

-----------------------------------------

zi    : zIndex          [int] []
    Only return values for cells with this Z index

-----------------------------------------

z     : zvalue          [boolean]
    Only get the third component of the vector-valued attribute specified by the "-at/attribute" flag.

    """

def loadFluid(q=1,e=1,ct=1,f="float",ic=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/loadFluid.html



-----------------------------------------

loadFluid is undoable, queryable, and editable.

A command to set builtin fluid attributes such as Density, Velocity, etc for
all cells in the grid from the initial state cache


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ct    : currentTime     [boolean] ['query', 'edit']
    This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.

-----------------------------------------

f     : frame           [float] ['query', 'edit']
    This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.

-----------------------------------------

ic    : initialConditions [boolean]
    load initial conditions cache

    """

def resampleFluid(q=1,e=1,rd="int",rh="int",rw="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/resampleFluid.html



-----------------------------------------

resampleFluid is undoable, queryable, and editable.

A command to extend the fluid grid, keeping the voxels the same size, and
keeping the existing contents of the fluid in the same place. Note that the
fluid transform is also modified to make this possible.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

rd    : resampleDepth   [int] ['query', 'edit']
    Change depth resolution to this value

-----------------------------------------

rh    : resampleHeight  [int] ['query', 'edit']
    Change height resolution to this value

-----------------------------------------

rw    : resampleWidth   [int]
    Change width resolution to this value

    """

def saveFluid(q=1,e=1,ct="int",et="int",st="int"):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/saveFluid.html



-----------------------------------------

saveFluid is undoable, queryable, and editable.

A command to save the current state of the fluid to the initial state cache.
The grids to be saved are determined by the cache attributes: cacheDensity,
cacheVelocity, etc. These attributes are normally set from the options on Set
Initial State. The cache must be set up before invoking this command.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.


-----------------------------------------


Flags:

-----------------------------------------

ct    : currentTime     [int] ['query', 'edit']
    cache state of fluid at current time

-----------------------------------------

et    : endTime         [int] ['query', 'edit']
    end Time for cacheing

-----------------------------------------

st    : startTime       [int]
    start Time for cacheing

    """

def setFluidAttr(ad=1,at="string",cl=1,fr="float",fv="float",lf=1,re=1,vr="[float, float, float]",vv="[float, float, float]",xi="int",x=1,yi="int",y=1,zi="int",z=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/setFluidAttr.html



-----------------------------------------

setFluidAttr is NOT undoable, NOT queryable, and NOT editable.

Sets values of built-in fluid attributes such as density, velocity, etc., for
individual grid cells or for all cells in the grid.


-----------------------------------------


Return Value:

None


-----------------------------------------


Flags:

-----------------------------------------

ad    : addValue        [boolean] []
    Add specified value to attribute

-----------------------------------------

at    : attribute       [string] []
    Specifies the fluid attribute for which to set values. Valid attributes are "velocity", "density", "fuel", "color", "falloff", and "temperature".

-----------------------------------------

cl    : clear           [boolean] []
    Set this attribute to 0

-----------------------------------------

fr    : floatRandom     [float] []
    If this was a scalar (e.g. density) attribute, use a random value in +-VALUE If fv is specified, it is used as the base value and combined with the random value. If the fv flag is not specified, the base is assumed to be 0.

-----------------------------------------

fv    : floatValue      [float] []
    If this was a scalar (e.g. density) attribute, use this value

-----------------------------------------

lf    : lowerFace       [boolean] []
    Only valid with "-at velocity". Since velocity values are stored on the edges of each voxel and not at the center, using voxel based indices to set velocity necessarily affects neighboring voxels. Use this flag to only set velocity components on the lower left three faces of a voxel, rather than all six.

-----------------------------------------

re    : reset           [boolean] []
    Set this attribute to default value

-----------------------------------------

vr    : vectorRandom    [[float, float, float]] []
    If this was a vector (e.g. velocity) attribute, use a random value in +-VALUE If vv is specified, it is used as the base value and combined with the random value. If the vv flag is not specified, the base is assumed to be 0,0,0.

-----------------------------------------

vv    : vectorValue     [[float, float, float]] []
    If this was a vector (e.g. velocity) attribute, use this value

-----------------------------------------

xi    : xIndex          [int] []
    Only return values for cells with this X index

-----------------------------------------

x     : xvalue          [boolean] []
    Only set the first component of the vector-valued attribute specified by the "-at/attribute" flag.

-----------------------------------------

yi    : yIndex          [int] []
    Only return values for cells with this Y index

-----------------------------------------

y     : yvalue          [boolean] []
    Only set the second component of the vector-valued attribute specified by the "-at/attribute" flag.

-----------------------------------------

zi    : zIndex          [int] []
    Only return values for cells with this Z index

-----------------------------------------

z     : zvalue          [boolean]
    Only set the third component of the vector-valued attribute specified by the "-at/attribute" flag.

    """

def truncateFluidCache(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/truncateFluidCache.html



-----------------------------------------

truncateFluidCache is undoable, queryable, and editable.

This command sets the end time of a fluid cache to the current time. If the
current time is less than the end time of the cache, the cache is truncated so
that only the portion of the cache up to and including the current time is
preserved.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.
    """

def truncateHairCache(q=1,e=1):
    """
http://help.autodesk.com/cloudhelp/2019/ENU/Maya-Tech-Docs/CommandsPython/truncateHairCache.html



-----------------------------------------

truncateHairCache is undoable, queryable, and editable.

This command sets the end time of a hair cache to the current time. If the
current time is less than the end time of the cache, the cache is truncated so
that only the portion of the cache up to and including the current time is
preserved.


-----------------------------------------


Return Value:

None

In query mode, return type is based on queried flag.
    """

