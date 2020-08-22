import sqlite3, wget, os
from modules.const import __dataBase_Download__


# {'first_name': 'Руслан', 'id': 271808173, 'last_name': 'Соловьев', 'home_town': 'Туапсе', 'status': '/kick %USERNAME%', 'bdate': '28.6.2001', 'bdate_visibility': 1,
# 'city': {'id': 1151, 'title': 'Туапсе'}, 'country': {'id': 1, 'title': 'Россия'}, 'phone': '+7 *** *** ** 85', 'relation': 6, 'screen_name': 'denbingon', 'sex': 2}

class dataBaseMethods( ):
    def __init__ ( self ):
        if os.path.exists( 'modules/db.sqlite' ) == True:
            pass
        else:
            wget.download( __dataBase_Download__, 'modules/db.sqlite' )

        self.connection = sqlite3.connect( 'modules/db.sqlite' )
        self.cursor = self.connection.cursor( )

    def addNewUserInformation ( self, info ):
        if info[ 'home_town' ] == None:
            info[ 'home_town' ] = None
        else:
            pass
        if info[ 'bdate' ] == None:
            info[ 'bdate' ] = None
        else:
            pass
        if info[ 'screen_name' ] == None:
            info[ 'screen_name' ] = None
        else:
            pass
        self.cursor.execute(
            f"""INSERT INTO users VALUES ({info[ 'id' ]}, '{info[ 'first_name' ]}', '{info[ 'last_name' ]}',
                                         '{info[ 'home_town' ]}', '{info[ 'bdate' ]}', {info[ 'sex' ]}, 
                                         '{info[ 'screen_name' ]}')""" )
        self.connection.commit( )

    def addNewScheduleInformation ( self, info ):
        self.cursor.execute( "" )
        self.connection.commit( )

    def watchInformation ( self, info ):
        self.cursor.execute( "" )
        self.connection.commit( )
