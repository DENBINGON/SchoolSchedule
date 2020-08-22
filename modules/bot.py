from modules import const, db


class VkBot:
    def __init__ ( self, user_id ):
        self._USER_ID = user_id
        self._COMMANDS = [ "КТО ТЫ", "ДОБАВИТЬ", "УДАЛИТЬ", "РАССПИСАНИЕ", "ЧТО НА ЗАВТРА", "ЧТО НА", "НАЧАТЬ",
                           "ПОМОЩЬ" ]
        self.DBMethods = db.dataBaseMethods( )
    def MessageParcer ( self, message ):
        if message.upper( ) == self._COMMANDS[ 0 ]:
            return f"Привет🖐!\nЯ бот помощник 🤖, созданный специально для облегчения твоей жизни 😜❤\n\n✌ Бот-помощник SchoolSchedule\n✅ Версия -> {const.__version__}\n📑 Source code available on https://github.com/denbingon/schoolschedule\n📑 Автор -> https://vk.com/denbingon", 1
        elif message.upper( ) == self._COMMANDS[ 1 ]:
            return f"разработка", 1
        elif message.upper( ) == self._COMMANDS[ 2 ]:
            return f"разработка", 1
        elif message.upper( ) == self._COMMANDS[ 3 ]:
            return f"разработка", 1
        elif message.upper( ) == self._COMMANDS[ 4 ]:
            return f"разработка", 1
        elif message.upper( ) == self._COMMANDS[ 5 ]:
            return f"разработка", 1
        elif message.upper( ) == self._COMMANDS[ 6 ]:
            try:
                userFirstName = self.DBMethods.getUserFirstName( self._USER_ID )
            except:
                userFirstName = None
            return f"Ой, привет {userFirstName}! Вижу ты тут в первые.", 0
        elif message.upper( ) == self._COMMANDS[ 7 ]:
            return f"разработка", 1
        else:
            return 'Не понимаю о чем ты... Воспользуйся коммандой "помощь" и я расскажу тебе что я умею!', 1
