"""
Utility to verify that the evaluation manager is yielding the same results
as the Maya DG evaluation.

It is a simple wrapper around run_correctness_test().  See its documentation
for more details.

Legal values for modes are 'ems' and 'emp' with an optional '+XXX' to
indicate that evaluator XXX should be turned on during the test or an
optional '-XXX' to indicate that it should be turned off. Evaluator
states will be returned to their original value after the test is run.
If an evaluator is not explicitly listed the current state of it will
be used for the test.

e.g. modes=['ems','emp+deformer']  means run the comparison twice, first
against EM Serial mode, the second time against EM Parallel mode with
the 'deformer' evaluator turned on. You can use multiple evaluators if
you wish: modes=['ems+deformer-dynamics'].

Sample usage to run the tests on a single file:

    from maya.debug.emCorrectnessTest import emCorrectnessTest
    serialErrors = emCorrectnessTest(fileName='MyDir/MyFile.ma', resultsPath='MyDir/emCorrectness', modes=['ems'])[1]

Sample usage to run the tests on the current scene in parallel mode with the deformer evaluator and ignore output:

    from maya.debug.emCorrectnessTest import emCorrectnessTest
    parallelErrors = emCorrectnessTest(modes=['emp+deformer'])

Sample usage to run the tests on the current scene in serial and parallel mode and
show formatted detailed results in the script editor window:

    def comp1(a,b):
        print '    {}   {}'.format(a[0], b[0])
    def comp3(a,b):
        print '    {}'.format( '
    '.join(str(numpy.array([a, b])).split('
')) )
    def comp16(a,b):
        for i in range(4):
            print '    {}'.format( '
    '.join(str(numpy.array([a[i*4:i*4+4], b[i*4:i*4+4]])).split('
')) )

    from maya.debug.emCorrectnessTest import emCorrectnessTest
    import numpy
    results = emCorrectnessTest(verbose=True, modes=['ems','emp'], dataTypes=['mesh','number','matrix','screen'],maxFrames=300)
    print  '
EM Correctness results'
    print  '=' * 22
    modeNames = {'ems':'EM Serial', 'emp':'EM Parallel'}
    for (result_type,result_list) in results.iteritems():
        if len(result_list) > 0:
            print '
Changes in %s' % modeNames[result_type]
        for (plug,values) in result_list.iteritems():
            print '------' + plug
            try:
                array1 = [float(value) for value in values['value'].split(' ')]
                array2 = [float(value) for value in values['other'].split(' ')]
                if len(array1) == 1:
                    comp1(array1, array2)
                elif len(array1) == 3:
                    comp3(array1, array2)
                elif len(array1) == 16:
                    comp16(array1, array2)
            except ValueError:
                # If the comparison result isn't floats just print as-is
                print '    {}'.format( values['value'] )
                print '    {}'.format( values['other'] )

    # Put the summary at the end for easier reading
    for (resultType,result) in results.iteritems():
        print 'Change count for %s = %d' % (modeNames[resultType], len(result))
"""

from maya.debug.correctnessUtils import run_correctness_test

class EMCorrectnessMode(object):
    """
    This class represents a mode to be tested in EM correctness tests.
    """
    
    
    
    def __init__(self, mode):
        pass
    
    
    def getContext(self):
        pass
    
    
    def getEmMode(self):
        pass
    
    
    def getTitle(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def emCorrectnessTest(fileName='None', resultsPath='None', verbose='False', modes="['ems']", maxFrames='20', dataTypes="['matrix', 'vertex', 'screen']", emSetup='0'):
    """
    Evaluate the file in multiple evaluation manager modes and compare the results.
    
    fileName:    See fileName parameter in run_correctness_test.
    resultsPath: See resultsPath parameter in run_correctness_test.
    verbose:     See verbose parameter in run_correctness_test.
    modes:       List of modes to run the tests in. 'ems' and 'emp' are the
                 only valid ones. A mode can optionally enable or disable an
                 evaluator as follows:
                     'ems+deformer': Run in EM Serial mode with the deformer evalutor turned on
                     'emp-dynamics': Run in EM Parallel mode with the dynamics evalutor turned off
                     'ems+deformer-dynamics': Run in EM Serial mode with the dynamics evalutor
                                              turned off and the deformer evaluator turned on
    maxFrames:   See maxFrames parameter in run_correctness_test.
    dataTypes:   See dataTypes parameter in run_correctness_test.
    emSetup:     See emSetup parameter in run_correctness_test.
    
    Returns the output of run_correctness_test().
    """

    pass



CORRECTNESS_NO_SETUP = 0

CORRECTNESS_MAX_FRAMECOUNT = 20


