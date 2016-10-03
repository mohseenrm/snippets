import time
#import snippets.python.decorators as momo
#@momo.debug
#@momo.safe_fail(fail=-1)
def debug( func ):
    '''
    Debug Wrapper, Lazy debugging
    :Author: Mohseen Mukaddam
    :param func: function to be wrapped
    :return: wrapped function
    '''
    def wrapper( *args, **kwargs ):
        results = func( *args, **kwargs )
        print '{0} ({1}{2}) : {3}'.format( func.__name__, args, kwargs, results )
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

def safe_fail( fail=-1 ):
    '''
    :returns safe values on failure of function
    :Author: Mohseen
    :param func: function to be wrapped
    :return: wrapped function
    '''
    def outer_wrapper( func ):
        def wrapper( *args, **kwargs ):
            results = func( *args, **kwargs )
            if( results is not None ):
                return results
            else:
                return( fail )
        return wrapper
    return outer_wrapper