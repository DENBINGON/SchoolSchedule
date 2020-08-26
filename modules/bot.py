from modules import db, homework, const
from modules.messages import *
import pendulum, vk

class VkBot:
    def __init__ ( self, user_id ):
        self._USER_ID = user_id
        self._COMMANDS = [ "КТО ТЫ", "ДОБАВИТЬ", "УДАЛИТЬ", "РАСПИСАНИЕ УРОКОВ", "ЧТО НА ЗАВТРА", "ЧТО НА", "НАЧАТЬ",
                           "ПОМОЩЬ", "РАСПИСАНИЕ ЗВОНКОВ" ]
        self.DBMethods = db.dataBaseMethods( )
        self.HomeworkMethods = homework.HomeworkMethods( )

    def MessageParcer ( self, message ):
        if message.upper( ) == self._COMMANDS[ 0 ]:
            return whoMe, 1
        elif message.upper( ) == self._COMMANDS[ 1 ]:
            dataA = self.waitAdditionalInformation( addSch ).split( '\n' )
            dataB = dataA[ 1 ].split( ' ' )
            self.HomeworkMethods.insertHomework( dataA[ 0 ], dataB )
            return 'Успешно!', 1
        elif message.upper( ) == self._COMMANDS[ 2 ]:
            return dev, 1
        elif message.upper( ) == self._COMMANDS[ 3 ]:
            return scheduleInformation, 1
        elif message.upper( ) == self._COMMANDS[ 4 ]:
            return self.HomeworkMethods.getAndParceHomework(
                pendulum.tomorrow( 'Europe/Moscow' ).format( 'DD.MM.YYYY' ) ), 1
        elif message.upper( ) == self._COMMANDS[ 5 ]:
            return self.HomeworkMethods.getAndParceHomework( self.waitAdditionalInformation( getHWOnDate ) ), 1
        elif message.upper( ) == self._COMMANDS[ 6 ]:
            try:
                userFirstName = self.DBMethods.getUserFirstName( self._USER_ID )
            except:
                userFirstName = None
            return firstHello_1 + str( userFirstName ) + firstHello_2, 0
        elif message.upper( ) == self._COMMANDS[ 7 ]:
            return help, 1
        elif message.upper( ) == self._COMMANDS[ 8 ]:
            return scheduleCallsInformation, 1
        else:
            return dontKnow, 1

    def waitAdditionalInformation ( self, text, work=1 ):
        self.session_ = vk.Session( access_token=const.__TOKEN_APP__ )
        self.API = vk.API( self.session_ )
        self.API.messages.send( user_id=self._USER_ID, v='5.21', message=f'{text}' )

        while work == 1:
            mes = self.API.messages.getConversations( offset=0, count=20, filter="unanswered", v='5.21' )
            if mes[ "count" ] >= 1:
                if mes[ "items" ][ 0 ][ "last_message" ][ "from_id" ] == self._USER_ID:
                    self.DBMethods.anotherInfoAdd( self._USER_ID )
                    return mes[ "items" ][ 0 ][ "last_message" ][ "text" ]
                else:
                    pass
