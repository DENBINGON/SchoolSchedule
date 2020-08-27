import sqlite3, wget, os
from modules.const import __dataBase_Download__

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
        return self.cursor.execute( "SELECT * FROM schedule_calls" ).fetchall( )

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

    def getHomework ( self, date ):
        return self.cursor.execute( f'SELECT * FROM schedule_homework WHERE date={date}' ).fetchone( )

    def insertHomework ( self, date, obj ):
        self.cursor.execute( f"""INSERT INTO schedule_homework VALUES ({date}, '{obj}')""" )
        self.connection.commit( )

    def runSQLRequest ( self, req ):
        try:
            out = self.cursor.execute( req ).fetchall( )
        except:
            self.cursor.execute( req )
            out = 'Done!'
        self.connection.commit( )
        return out

    def removeHomework ( self, date ):
        self.cursor.execute( f"DELETE FROM schedule_homework WHERE date={date}" )
        self.connection.commit( )

    def anotherInfoAdd ( self, user_id ):
        self.cursor.execute( f'INSERT INTO another_info VALUES ({user_id})' )
        self.connection.commit( )

    def anotherInfoRemove ( self, user_id ):
        self.cursor.execute( f'DELETE FROM another_info WHERE user_id={user_id}' )
        self.connection.commit( )

    def anotherInfoGet ( self, user_id ):
        tuple = self.cursor.execute( f'SELECT * FROM another_info' ).fetchall( )
        idList, count = [ ], 0
        for id in tuple:
            idList.append( id[ 0 ] )
        if user_id in idList:
            for inx in idList:
                if user_id == inx:
                    count += 1
                else:
                    pass
            self.anotherInfoRemove( user_id )
            if count > 1:
                count -= 1
                for i in range( 0, count ):
                    self.anotherInfoAdd( user_id )
            else:
                self.anotherInfoRemove( user_id )
            return True
        else:
            return False
