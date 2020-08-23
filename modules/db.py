import sqlite3, wget, os
from modules.const import __dataBase_Download__


# [{'id': 271808173, 'first_name': 'Руслан', 'last_name': 'Соловьев'}]

# [('русский', 'математика', 'информатика', 'английский', 'биология', 'кубановеденье', None),
# ('русский', 'математика', 'информатика', 'английский', 'биология', 'кубановеденье', None),
# ('русский', 'математика', 'информатика', 'английский', 'биология', 'кубановеденье', None)]


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

    def getScheduleList ( self ):
        return self.cursor.execute( "SELECT * FROM schedule" ).fetchall( )

    def getScheduleCallsList ( self ):
        return self.cursor.execute( "SELECT * FROM schedule_call" ).fetchall( )

    def watchInformation ( self, info ):
        self.cursor.execute( "" )
        self.connection.commit( )

    def removeUser ( self, user_id ):
        self.cursor.execute( f"DELETE FROM users WHERE user_id={user_id}" )

    def checkUser ( self, user_id ):
        if self.cursor.execute( f"SELECT * FROM users WHERE user_id={user_id}" ).fetchone( ) == None:
            return False
        else:
            return True

    def getUserFirstName ( self, user_id ):
        return str( self.cursor.execute( f"SELECT * FROM users WHERE user_id={user_id}" ).fetchone( ) ).split( "'" )[
            1 ]
