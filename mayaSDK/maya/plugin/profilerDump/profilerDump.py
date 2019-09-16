def profilerToCSV(fileName, durationMin):
    """
    fileName : name of file to write to disk
    useIndex : write events using index lookup to category and name lists
    durationMin : only write out events which have at least this minimum time duration
    
    Description:
            Sample to output profiler event information only to CSV format.
    Example:
            > profilerToCSV('profiler.csv', 0.0)
    """

    pass


def profilerFormatJSON(fileName, fileName2):
    """
    fileName : name of file to read
    fileName2 : name of file to write to
    
    Description:
            Simple utility code to read a JSON file sort and format it before
            writing to a secondary file.
    
    Example:
            > profilerFormatJSON('profilerIn.json', 'profilerFormatted.json')
    """

    pass


def initializePlugin(obj):
    """
    # Nothing run on initialize for now
    """

    pass


def profilerToJSON(fileName, useIndex, durationMin):
    """
    fileName : name of file to write to disk
    useIndex : write events using index lookup to category and name lists
    durationMin : only write out events which have at least this minimum time duration
    
    Description:
            Sample code to extract profiler information and write to file in JSON format
    
    Example usage:
            > profilerToJSON('profiler_indexed.json', True, 0.0) # Index without a duration clamp
            > profilerToJSON('profiler_nonIndexed.json', False, 10.0) # Non-Indexed with duration clamp
    """

    pass


def uninitializePlugin(obj):
    pass



