# 22.02.2020

def timeToStr ( time ):
    return time.replace( '.', '' )


# 22022020

def strToTime ( time ):
    chars = [ ]
    for char in str( time ):
        chars.append( char )
    return f'{chars[ 0 ] + chars[ 1 ]}.{chars[ 2 ] + chars[ 3 ]}.{chars[ 4 ] + chars[ 5 ] + chars[ 6 ] + chars[ 7 ]}'
