from modules import const


class VkBot:
    def __init__ ( self, user_id ):
        print( "Создан объект бота!" )
        self._USER_ID = user_id

        self._COMMANDS = [ "КТО ТЫ", "ДОБАВИТЬ", "УДАЛИТЬ", "РАССПИСАНИЕ", "ЧТО НА ЗАВТРА", "ЧТО НА", "НАЧАТЬ" ]

    def MessageParcer ( self, message ):
        if message.upper( ) == self._COMMANDS[ 0 ]:
            return f"Привет🖐!\nЯ бот помощник 🤖, созданный специально для облегчения твоей жизни 😜❤\n\n✌ Бот-помощник SchoolSchedule\n✅ Версия -> {const.__version__}\n📑 Source code available on https://github.com/denbingon/schoolschedule\n📑 Автор -> https://vk.com/denbingon"
        elif message.upper( ) == self._COMMANDS[ 1 ]:
            return f"Выполняю действие, подожди минутку"
        elif message.upper( ) == self._COMMANDS[ 2 ]:
            return f"Выполняю действие, подожди минутку"
        elif message.upper( ) == self._COMMANDS[ 3 ]:
            return f"Выполняю действие, подожди минутку"
        elif message.upper( ) == self._COMMANDS[ 4 ]:
            return f"Выполняю действие, подожди минутку"
        elif message.upper( ) == self._COMMANDS[ 5 ]:
            return f"Выполняю действие, подожди минутку"
        elif message.upper( ) == self._COMMANDS[ 6 ]:
            return f"Ой, привет! Вижу ты тут в первые. Скажи мне как тебя зовут?)"
        else:
            return "Не понимаю о чем вы..."
