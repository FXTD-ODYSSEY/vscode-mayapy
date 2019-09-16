"""
Utility script to scour the known debugging commands and dump a formatted collection of
information on what capabilities are available. Done in a backwards compatible manner
so that it can be run on earlier versions to find capabilities retroactively.

    from maya.debug.current_debug_capabilities import current_debug_capabilities
    print current_debug_capabilities( None )

Output is formatted as JSON for easy parsing for document creation. Here's a simple
example for the dbtrace command, which initially only supported the "compute" keyword
in customer cuts.

{
    "debugging" :
    {
        "dbtrace" :
        {
            "help" : "Synopsis: dbtrace [flags]Flags:   -q -query   -f -filter   String   -i -info       -k -keyword  String (multi-use) (Query Arg Optional)   -l -level    UnsignedInt (multi-use) (Query Arg Mandatory)   -m -mark       -o -output   String -off -           -t -title    String  -tm -timed    on|off   -v -verbose Command Type: Command",
            "keywords" :
            {
                "compute" : "High level trace of the compute path."
            }
        }
    }

For any section requiring commands not available in the current cut an
abbreviated output is provided:

{
    "debugging" :
    {
        "dbtrace" : { "help" : "The dbtrace command is not available in this cut" }
    }
"""

def dgdirty_capabilities():
    """
    Find the current capabilities of the dgdirty command if it exists.
    """

    pass


def dgeval_capabilities():
    """
    Find the current capabilities of the dgeval command if it exists.
    """

    pass


def dgdebug_capabilities():
    """
    Find the current capabilities of the dgdebug command if it exists.
    """

    pass


def dgInfo_capabilities():
    """
    Find the current capabilities of the dgInfo command if it exists.
    """

    pass


def dbtrace_keyword_split(keyword):
    """
    Split a dbtrace keyword into key and level. Formatting is KEY[LEVEL]
    for internal traces and just KEY for customer-facing ones. In the
    latter case a level of 0 is returned for consistency.
    """

    pass


def dbpeek_capabilities():
    """
    Find the current capabilities of the dbpeek command if it exists.
    Only embedded help is available for specific dbpeek operations so
    that is all provided here. Documentation for the command itself is
    available online in the command documentation.
    
        {
            "help" : "HELP INFORMATION FROM 'help dbpeek'"
            "operations" :
            {
                "OPERATION" : "SUMMARY FROM 'dbpeek -op OPERATION -q'"
            }
        }
    """

    pass


def current_debug_capabilities(file_name):
    """
    Dump out the current debugging capabilities to the named file.
    :param file_name: Name of file to receive the results. If None then
                      the results are returned in a JSON dictionary.
    """

    pass


def dbmessage_capabilities():
    """
    Find the current capabilities of the dbmessage command if it exists.
    """

    pass


def command_available(command, results):
    """
    Check to see if a command is available in this cut.
    :param command: Name of command to check
    :param results: Returned help information. If the command is available
                    it will have the output from 'help command' appended,
                    otherwise it will have a notice that the command is
                    not available.
    :return: True if the command is available, False if not
    """

    pass


def dbtrace_capabilities():
    """
    Find the current capabilities for the dbtrace command and return it
    in a dictionary. Only the help information and a summary of each
    available keyword derived from the 'info' flag is provided.
    
        {
            "help" : "HELP INFORMATION FROM 'help dbtrace'"
            "keywords" :
            {
                "KEYWORD" : "SUMMARY FROM 'dbtrace -k KEYWORD -q -info'"
            }
        }
    """

    pass


def dgmodified_capabilities():
    """
    Find the current capabilities of the dgmodified command if it exists.
    """

    pass


def dbcount_capabilities():
    """
    Find the current capabilities of the dbcount command if it exists.
    """

    pass



RE_DBTRACE_KEYWORD_LEVEL = None


