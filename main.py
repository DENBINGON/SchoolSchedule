# Импорт библиотек
import vk_api, random
from modules import const, db, sys
from modules.bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType


# Основной класс
class SchoolScheduleMainApp( ):
    def __init__ ( self ):
        self.vk = vk_api.VkApi( token=const.__TOKEN__ )
        self.vk._auth_token( )
        self.longpoll = VkLongPoll( self.vk )
        for event in self.longpoll.listen( ):
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    print( 'New message:' )
                    print( f'For me by: {event.user_id}\n', end='' )
                    bot = VkBot( event.user_id )
                    self.WriteMessage( event.user_id, bot.MessageParcer( event.text ) )
                    print( 'Text: ', event.text )

    def WriteMessage ( self, user_id, message ):
        self.vk.method( 'messages.send', { 'user_id': user_id, 'message': message, 'random_id': random.random( ) * 1000,
                                           'keyboard': const.__KEYBOARD__ } )


# Запускаем
if __name__ == "__main__":
    start = SchoolScheduleMainApp( )
