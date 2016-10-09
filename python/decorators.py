__author__ = 'MoMo'
import time
#import snippets.python.decorators as momo
#@momo.debug
#@momo.safe_fail(fail=-1)
#momo.safe_failure()
from functools import wraps

def debug( func ):
    '''
    Debug Wrapper, Lazy debugging
    :Author: Mohseen Mukaddam
    :param func: function to be wrapped
    :return: wrapped function
    '''
    def wrapper( *args, **kwargs ):
        results = func( *args, **kwargs )
        print '{0} (args: {1} | kwargs: {2}) | result: {3}'.format( func.__name__, args, kwargs, results )
        print 'Return Type: {0}'.format( type( results ) )
        return results
    return wrapper

def run_time( func ):
    '''
    Time Wrapper for calculating code run time
    :Author: Mohseen Mukaddam
    :param func: function to be wrapped
    :return: wrapped function
    '''
    def wrapper( *args, **kwargs ):
        init = time.time()
        results = func( *args, **kwargs )
        print 'Run time: {0}'.format( time.time() - init )
        return results
    return wrapper

#deprecated : doesn't work well with nested decorators; Use @safe_failure()
def safe_fail( fail=-1 ):
    '''
    :returns safe values on failure of function
    :Author: Mohseen
    :param func: function to be wrapped
    :return: wrapped function
    '''
    def outer_wrapper( func ):
        @wraps( func )
        def wrapper( *args, **kwargs ):
            results = func( *args, **kwargs )
            if results is not None :
                return results
            else:
                return fail
        return wrapper
    return outer_wrapper

#please call it via @safe_failure()
# lack of () causes the compiler to confuse the argument properties, which... is not nice

class safe_failure( object ):
    '''
    A function decorated with @safe_failure() will return a fail value of -1 ( default ) or the value passed via the call
    @safe_fail(fail=x); this was written to reduce the boilerplate code that is associated with such tasks
    '''
    def __init__( self, fail=-1 ):
        # self.fail = kwargs.get( 'fail', -1 )
        self.fail = fail

    def __call__( self, func ):
        '''
        This guy get called when the decorator is written on top of the function,
        decorator wraps the function below, calls __call__ with the function parsers its arguments to the wrapper
        and the gives control to the decorator
        '''
        def wrapper( *args, **kwargs ):
            results = func( *args, **kwargs )
            if results is not None:
                return results
            else:
                return self.fail
        return wrapper