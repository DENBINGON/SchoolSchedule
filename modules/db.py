import sqlite3, wget, os
from modules.const import __dataBase_Download__


# [{'id': 271808173, 'first_name': 'Руслан', 'last_name': 'Соловьев'}]

class dataBaseMethods( ):
    def __init__ ( self ):
        if os.path.exists( 'modules/db.sqlite' ) == True:
            pass
        else:
            wget.download( __dataBase_Download__, 'modules/db.sqlite' )

        self.connection = sqlite3.connect( 'modules/db.sqlite' )
        self.cursor = self.connection.cursor( )

    def addNewUserInformation ( self, info ):
        self.cursor.execute( f"""INSERT INTO users VALUES ({info[ 'id' ]}, '{info[ 'first_name' ]}',
                                                          '{info[ 'last_name' ]}')""" )
        self.connection.commit( )

    def addNewScheduleInformation ( self, info ):
        self.cursor.execute( "" )
        self.connection.commit( )

    def watchInformation ( self, info ):
        self.cursor.execute( "" )
        self.connection.commit( )

    def getUserFirstName ( self, user_id ):
        return str( self.cursor.execute( f"SELECT * FROM users WHERE user_id={user_id}" ).fetchone( ) ).split( "'" )[
            1 ]
