__author__ = 'MoMo'
import re
from decorators import safe_failure
def joint( parent, child, **kwargs ):
    '''
    Returns string with child appended to parent, since string are immutable objects in Python
    :Author: Mohseen [pun intended]
    :param parent: string
    :param child: string
    :param kwargs: (optional) Seperator: string
    :return: string
    '''
    parent = str( parent )
    child = str( child )
    for key, value in kwargs.iteritems():
        if key.lower() == "seperator":
            return( "".join( ( parent, str( value ), child ) ) )

    return( "".join( ( parent, child ) ) )

@safe_failure()
def test_regex_search( pattern, sample ):
    regex = re.compile( pattern )
    return( regex.search( str( sample ) ) )

@safe_failure()
def test_regex( pattern, replace, sample ):
    return re.sub( pattern, replace, str( sample ) )