from modules import db, homework, const
from modules.messages import *
import pendulum, datetime


class VkBot:
    def __init__ ( self, user_id ):
        self._USER_ID = user_id
        self.whatTheyWant = None
        self._COMMANDS = [ "КТО ТЫ", "ДОБАВИТЬ", "УДАЛИТЬ", "РАСПИСАНИЕ", "ЧТО НА ЗАВТРА", "ДОМАШНИЕ ЗАДАНИЯ",
                           "НАЧАТЬ", "ПОМОЩЬ", "РАСПИСАНИЕ ЗВОНКОВ" ]
        self._COMMANDS_SHORT_DATES = [ "СЕГОДНЯ", "ЗАВТРА", "ПОСЛЕЗАВТРА", "НАЗАД", "СВОЯ ДАТА" ]
        self._COMMANDS_SCH = [ "УРОКОВ", "ЗВОНКОВ", "НАЗАД" ]
        self.DBMethods = db.dataBaseMethods( )
        self.HomeworkMethods = homework.HomeworkMethods( )

    def MessageParcer ( self, message ):
        if message.upper( ) == self._COMMANDS[ 0 ]:
            return whoMe, 1
        elif message.upper( ) == self._COMMANDS[ 1 ]:
            if self._USER_ID in const.access_ID:
                self.DBMethods.anotherInfoAdd( self._USER_ID, 'add' )
                return addSch, 1
            else:
                return accessDenied, 1
        elif message.upper( ) == self._COMMANDS[ 2 ]:
            return dev, 1
        elif message.upper( ) == self._COMMANDS[ 3 ]:
            self.DBMethods.anotherInfoAdd( self._USER_ID, 'sch' )
            return selectSch, 4


        # ВЕСЬ КОД СЮДА
        elif message.upper( ) == self._COMMANDS[ 5 ]:
            self.DBMethods.anotherInfoAdd( self._USER_ID, 'hw' )
            return getHWOnDate, 2


        elif message.upper( ) == self._COMMANDS[ 6 ]:
            try:
                userFirstName = self.DBMethods.getUserFirstName( self._USER_ID )
            except:
                userFirstName = None
            return firstHello_1 + str( userFirstName ) + firstHello_2, 0
        elif message.upper( ) == self._COMMANDS[ 7 ]:
            return help, 1

        else:
            # обработчик UserDataContinue
            try:
                try:
                    self.whatTheyWant = self.DBMethods.anotherInfoGet( self._USER_ID )
                except:
                    self.whatTheyWant = None

                # двойное и более меню

                if self.whatTheyWant == 'hw':
                    if message.upper( ) == self._COMMANDS_SHORT_DATES[ 0 ]:
                        return self.HomeworkMethods.getAndParceHomework(
                            pendulum.today( 'Europe/Moscow' ).format( 'DD.MM.YYYY' ) ), 1
                    elif message.upper( ) == self._COMMANDS_SHORT_DATES[ 1 ]:
                        return self.HomeworkMethods.getAndParceHomework(
                            pendulum.tomorrow( 'Europe/Moscow' ).format( 'DD.MM.YYYY' ) ), 1
                    elif message.upper( ) == self._COMMANDS_SHORT_DATES[ 2 ]:
                        overmorrow = datetime.date.today( ) + datetime.timedelta( days=2 )
                        return self.HomeworkMethods.getAndParceHomework( overmorrow.strftime( '%d.%m.%Y' ) ), 1
                    elif message.upper( ) == self._COMMANDS_SHORT_DATES[ 3 ]:
                        return 'Главное меню', 1
                    elif message.upper( ) == self._COMMANDS_SHORT_DATES[ 4 ]:
                        self.DBMethods.anotherInfoAdd( self._USER_ID, 'hw-on-date' )
                        return getHWOnDateSelect, 3
                elif self.whatTheyWant == 'add':
                    data = message.split( '\n' )
                    self.HomeworkMethods.insertHomework( data[ 0 ], data[ 1 ].split( ' ' ) )
                    return 'Успех', 1
                elif self.whatTheyWant == 'hw-on-date':
                    if message.upper( ) != 'НАЗАД':
                        try:
                            return self.HomeworkMethods.getAndParceHomework( message ), 1
                        except:
                            return 'Неверная дата', 1
                    else:
                        return 'Главное меню', 1
                elif self.whatTheyWant == 'sch':
                    if message.upper( ) == self._COMMANDS_SCH[ 0 ]:
                        return scheduleInformation, 1
                    elif message.upper( ) == self._COMMANDS_SCH[ 1 ]:
                        return scheduleCallsInformation, 1
                    elif message.upper( ) == self._COMMANDS_SCH[ 2 ]:
                        return 'Главное меню', 1

                else:
                    return dontKnow, 1
            except:
                pass
