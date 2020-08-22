from modules import const, db
from modules.messages import *

class VkBot:
    def __init__ ( self, user_id ):
        self._USER_ID = user_id
        self._COMMANDS = [ "КТО ТЫ", "ДОБАВИТЬ", "УДАЛИТЬ", "РАССПИСАНИЕ", "ЧТО НА ЗАВТРА", "ЧТО НА", "НАЧАТЬ",
                           "ПОМОЩЬ" ]
        self.DBMethods = db.dataBaseMethods( )
    def MessageParcer ( self, message ):
        if message.upper( ) == self._COMMANDS[ 0 ]:
            return whoMe, 1
        elif message.upper( ) == self._COMMANDS[ 1 ]:
            return dev, 1
        elif message.upper( ) == self._COMMANDS[ 2 ]:
            return dev, 1
        elif message.upper( ) == self._COMMANDS[ 3 ]:
            return dev, 1
        elif message.upper( ) == self._COMMANDS[ 4 ]:
            return dev, 1
        elif message.upper( ) == self._COMMANDS[ 5 ]:
            return dev, 1
        elif message.upper( ) == self._COMMANDS[ 6 ]:
            try:
                userFirstName = self.DBMethods.getUserFirstName( self._USER_ID )
            except:
                userFirstName = None
            return firstHello_1 + str( userFirstName ) + firstHello_2, 0
        elif message.upper( ) == self._COMMANDS[ 7 ]:
            return dev, 1
        else:
            return dontKnow, 1
