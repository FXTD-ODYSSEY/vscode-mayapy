"""
The apply override nodes that may be inserted in a shading network are divided into two families:
 - absolute override
 - relative override
and they can output the following types:
 - float, float2, float3
 - int, int2, int3
 - enum (absolute only)
 - bool (absolute only)
 - string (absolute only)
and they can be enabled or not.

Absolute overrides have the following inputs:
 - an original value (original)
 - an override value (attrValue)
 - an enabled bool (enabled)
In pseudo code, their output would be evaluated as:
  out = enabled? attrValue : original;
  
Relative overrides have the following inputs:
 - an original value (original)
 - a multiply value (multiply)
 - an offset value (offset)
 - an enabled bool (enabled)
 In pseudo code, their output would be evaluated as:
  out = enabled? original * multiply + offset : original;

Plugin renderers need to translate these nodes in order for their shading network to be evaluated accurately.

IMPORTANT:

Apply override nodes are connected to override nodes.
Override nodes define the override parameters (attrValue (absolute), offset, multiply (relative)).
Apply overrides are a specific application of the override on a specific target node, since an override can apply to one or more targets. They read the 
parameters from the override nodes and these parameters are readable AND writable attributes (in and out).
They are NOT computed by the override node but simply "forwarded" to the apply override nodes.
They may have SOURCE CONNECTIONS or be KEYED though. This means that the override nodes don't need to be translated
since they do not compute the outputs. But the override node's sources must be translated and connected to the translated apply override 
in order to be well evaluated.

Example:
                                                                                 
                                                                                 
  -----------      ---------------      --------------         --------------    
 | SOME NODE |    |  ABSOLUTE OV  |    | APPLY ABS OV |       | A SHADING NODE | 
 |           |    |               |    |              |       |                | 
 o someIn    |    |               |    o original     |   /---o anAttribute    | 
 |   someOut o----o attrValue     o----o attrValue    |   |   o <other attrs>  | 
 |           |    o enabled       o----o enabled      |   |   |                | 
 |           |    |               |    |       output o---/   |      <outputs> o 
  -----------      ---------------      --------------         ----------------
"""

class _MPxShadingNodeOverride(object):
    """
    Base class for user defined shading node overrides.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
    
        pass
    
    
    def allowConnections(*args, **kwargs):
        """
        allowConnections() -> bool
        
        Returns True if connections should be allowed to parameters of the fragment that do not have custom mappings that
        specifically prevent connections.
        
        An override may prevent Maya from connecting fragments to specific parameters of the fragment for this
        override by providing custom attribute parameter mappings. It is also possible to prevent connections to all
        parameters on the fragment by overriding this method to return False.
        In that case, the fragment for this override will become a final fragment, and nothing will be connected to it.
        This is equivalent to creating an attribute parameter mapping for every parameter on the fragment and setting
        the allowConnection flag on each mapping to False.
        
        This method is called once only, just after creation of the override.
        """
    
        pass
    
    
    def fragmentName(*args, **kwargs):
        """
        fragmentName() -> string
        
        Override this method to return the name of the fragment or fragment graph to use for rendering the shading node associated with this override. This fragment will be automatically connected to the other fragments for the other nodes in the shading network to produce a complete shading effect.
        
        A fragment with the returned name must already exist in the fragment manager for rendering to succeed. If the fragment does not exist, the associated node will not contribute to shading.
        
        The parameter values for the fragment will be automatically populated from the attribute values on the node wherever the name and type of a parameter on the fragment match the name and type of an attribute on the node.
        
        The fragment will only be connected to the other fragments in the graph if the output parameter of the fragment has the same name as the output attribute of the node that is connected to the rest of the shading network. To support multiple output attributes of a node, the fragment should return a "struct" type parameter. The names of the members of the struct should match the names of the output attributes for which support is desired. The fragment must compute all output attributes on every execution.
        
        Returns the name of the fragment to use
        """
    
        pass
    
    
    def getCustomMappings(*args, **kwargs):
        """
        getCustomMappings(mappings) -> self
        
        Maya will automatically match parameters on the shade fragment specified by this override with attributes on the
        associated Maya node as long as the names and types match. In order to specify custom attribute parameter mappings,
        override this method.
        
        This method will be called before Maya performs its automatic matching so it can be used to prevent that process by
        defining mappings for parameters that would normally be mapped automatically.
        Such mappings will take precedence over automatic mappings.
        
        It is an error to provide more than one mapping per fragment parameter.
        Only the first such mapping will be used.
        
        The same attribute may be used for multiple parameters.
        
        By default, this method defines no custom mappings.
        
        * mappings [OUT] (MAttributeParameterMappingList) - An attribute parameter mapping list; fill with any desired custom mappings.
        """
    
        pass
    
    
    def outputForConnection(*args, **kwargs):
        """
        outputForConnection(sourcePlug, destinationPlug) -> string
        
        Returns the name of an output parameter on the fragment for the override.
        
        When Maya attempts to connect the fragment for this override to the fragment for another node in the shading network,
        it will call this method to get the name of the output on the fragment to use for the connection.
        By default, this will simply return the name of the output attribute on the node for the override that is driving the connection.
        Override this method to specify that a different output of the fragment should be used instead.
        This method may also be overridden to get information about how and where the fragment is being connected.
        
        If the output of the fragment is of "struct" type, this method should return the name of one of the members of the struct.
        
        This method is called after getCustomMappings().
        
        If the name returned does not match the name of any output parameter (or struct member in the case of struct output) on the
        fragment for this override then the fragment will not be connected to the overall shading effect.
        
        * sourcePlug (MPlug) - The plug on the node for this override which is the source of the connection.
                               By default the name of the attribute for this plug is returned.
        * destinationPlug (MPlug) - The plug on the node which is the destination of the connection.
        """
    
        pass
    
    
    def supportedDrawAPIs(*args, **kwargs):
        """
        supportedDrawAPIs() -> DrawAPI
        
        Returns the draw API supported by this override.
        """
    
        pass
    
    
    def updateDG(*args, **kwargs):
        """
        updateDG() -> self
        
        This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
        produced by this override is a part. In this method implementations should query and cache any values needed for setting
        parameters on the final shading effect in updateShader().
        """
    
        pass
    
    
    def updateShader(*args, **kwargs):
        """
        updateShader(shader, mappings) -> self
        
        This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
        produced by this override is a part. Implementations may use the information from the mappings list to set parameter values on
        the shader. The list contains all parameter mappings for the override, both automatic and custom. Although it is possible to set
        the value for any parameter on the shader it is an error to do so for parameters which are not defined by the fragment for this
        override and doing so may result in unpredictable behaviour.
        
        The default implementation does nothing. Note that values for parameters with valid attribute parameter mappings will be set
        automatically. This method need only be overridden if custom behaviour is required.
        
        For performance, consider caching the resolved parameter names of parameters needing update the first time this method is called.
        This will avoid searching the mappings list and then retrieving the resolved name from the mapping on each update. Resolved names
        are guaranteed to remain constant until the next time fragmentName() is called. Const pointers to individual mappings may also be
        cached in this way and are valid for the same duration.
        Do not attempt to cache mappings created in the getCustomMappings() method.
        
        It is an error to attempt to access the Maya dependency graph from within updateShader().
        Any attempt to do so will result in instability. Required data should be retrieved and cached in updateDG().
        
        * shader (MShaderInstance) - The shader instance.
        * mappings (MAttributeParameterMappingList) - The attribute parameter mappings for this override.
        """
    
        pass
    
    
    def valueChangeRequiresFragmentRebuild(*args, **kwargs):
        """
        valueChangeRequiresFragmentRebuild(plug) -> bool
        
        Returns True if a change in attribute values should cause a rebuild of the complete shading effect.
        
        This method will be called by Maya when it detects changes in the attribute values of nodes in the shading network.
        If this method returns True, Maya will assume that the change means that a new configuration of the total fragment graph
        is necessary and it will trigger a rebuild of the complete shading effect. This will cause fragmentName() to be invoked
        again at which point a different fragment name could be returned.
        
        For example, if a texture node has multiple modes, each implemented with a different fragment, then a change to the active
        mode would require the shading effect to be rebuilt in order to switch which fragment is used.
        
        The plug parameter passed in is Maya's best attempt at informing the implementation of what changed. However due to the
        nature of the change management system a single source plug cannot always be determined in which case the plug may be NULL.
        
        The default implementation returns False.
        
        * plug (MPlug) - The plug that changed, may be None.
        """
    
        pass
    
    
    __new__ = None


class ApplyOverrideShadingNodeOverride(_MPxShadingNodeOverride):
    """
    Base class for shading node overrides for the apply override nodes.
    Subclasses only provide the fragment body template to be filled in with template args.
    """
    
    
    
    def __init__(self, obj):
        pass
    
    
    def fragmentName(self):
        pass
    
    
    def supportedDrawAPIs(self):
        pass
    
    
    def creator(cls, obj):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class ApplyAbsOverrideShadingNodeOverride(ApplyOverrideShadingNodeOverride):
    pass


class ApplyRelOverrideShadingNodeOverride(ApplyOverrideShadingNodeOverride):
    pass



def initialize():
    pass


def getDrawdbClassification(typeid):
    pass


def uninitialize():
    pass



_classifToCreator = {}

_classifToTypeIds = {}


