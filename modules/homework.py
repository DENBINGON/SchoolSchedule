# [{'data':data,'description':desc}]
#   DESCRIPTION data saver   ->    [{'id':id, 'lesson':lesson}, 'hw':hw]
# [('26.08.2020', "[{'id':id, 'lesson':lesson, 'hw':hw}]"), ('26.08.2020', "[{'id':id, 'lesson':lesson, 'hw':hw}]")]
import json
from modules import db


class getHomework:
    def __init__ ( self ):
        self.DBMethods = db.dataBaseMethods( )

    def getAndParceHomework ( self, date ):
        list = json.loads( str( self.DBMethods.getHomework( date ) ).split( "'" )[ 3 ] )

        container_list, out = 0, f'Д/з на {date} для 11Б\n\n'
        for event in list:
            container_list += 1

        for container_id in range( 0, container_list ):
            cont = list[ f"container_{container_id + 1}" ]
            out += f'{container_id + 1}. {cont[ "lesson" ]} -> {cont[ "hw" ]}\n'

        return out
