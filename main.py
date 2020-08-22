# Импорт библиотек
import vk_api, random
from modules import const, db, sys, userAuthMethods
from modules.bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType


# Основной класс
class SchoolScheduleMainApp( ):
    def __init__ ( self ):
        self.session = vk_api.VkApi( token=const.__TOKEN_APP__ )
        self.session._auth_token( )
        self.longpoll = VkLongPoll( self.session )
        self.userMethods = userAuthMethods.UserAuth( )
        self.DBMethods = db.dataBaseMethods( )
        for event in self.longpoll.listen( ):
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    print( 'New message:' )
                    print( f'For me by: {event.user_id}\n', end='' )
                    bot = VkBot( event.user_id )
                    answer, userCode = bot.MessageParcer( event.text )
                    if userCode == 1:
                        self.WriteMessage( event.user_id, answer )
                    else:
                        self.DBMethods.addNewUserInformation( self.userMethods.getUserInformation( event.user_id ) )
                        self.WriteMessage( event.user_id, answer )

                    print( 'Text: ', event.text )

    def WriteMessage ( self, user_id, message ):
        self.session.method( 'messages.send',
                             { 'user_id': user_id, 'message': message, 'random_id': random.random( ) * 1000,
                               'keyboard': const.__KEYBOARD__ } )


# Запускаем
if __name__ == "__main__":
    start = SchoolScheduleMainApp( )
