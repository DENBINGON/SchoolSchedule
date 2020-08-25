# [{'data':data,'description':desc}]
#   DESCRIPTION data saver   ->    [{'id':id, 'lesson':lesson}, 'hw':hw]
# [('26.08.2020', "[{'id':id, 'lesson':lesson, 'hw':hw}]"), ('26.08.2020', "[{'id':id, 'lesson':lesson, 'hw':hw}]")]
import json
from modules import db


class HomeworkMethods:
    def __init__ ( self ):
        self.DBMethods = db.dataBaseMethods( )

    def getAndParceHomework ( self, date ):
        try:
            list = json.loads( str( self.DBMethods.getHomework( date ) ).split( "'" )[ 3 ] )

            container_list, out = 0, f'Д/з на {date} для 11Б\n\n'
            for event in list:
                container_list += 1

            for container_id in range( 0, container_list ):
                cont = list[ f"container_{container_id + 1}" ]
                out += f'{container_id + 1}. {cont[ "lesson" ]} -> {cont[ "hw" ]}\n'
        except:
            out = 'Ничего не найдено :('
        return out

    def insertHomework ( self, date, data ):
        try:
            list = json.loads( str( self.DBMethods.getHomework( date ) ).split( "'" )[ 3 ] )
            container_list, obj = 0, '{'
            for event in list:
                container_list += 1
            for container_id in range( 0, container_list ):
                cont = list[ f"container_{container_id + 1}" ]
                obj += f'"container_{container_id + 1}' + '":{"id":' + str( container_id + 1 ) + ',"lesson":"' + cont[
                    'lesson' ] + '","hw":"' + cont[ 'hw' ] + '"}'
                if container_id + 1 == container_list:
                    obj += f',"container_{container_id + 2}' + '":{"id":' + str( container_id + 2 ) + ',"lesson":"' + \
                           data[
                               0 ] + '","hw":"' + data[ 1 ] + '"}'
                else:
                    obj += ','
            obj += '}'
        except:
            obj = '{'
            obj += f'"container_1' + '":{"id":' + str( 1 ) + ',"lesson":"' + data[
                0 ] + '","hw":"' + data[ 1 ] + '"}}'
        print( obj )
        self.DBMethods.insertHomework( date, obj )
