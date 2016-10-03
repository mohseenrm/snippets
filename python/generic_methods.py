__author__ = 'MoMo'
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