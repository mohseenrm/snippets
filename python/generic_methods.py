__author__ = 'MoMo'
import re

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

def test_regex_search( pattern, sample ):
    regex = re.compile( pattern )
    return( regex.search( sample ) )

def test_regex( pattern, replace, sample ):
    return re.sub( pattern, replace, sample)