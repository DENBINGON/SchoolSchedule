from modules.const import __version__
from modules.db import dataBaseMethods

DBMethods = dataBaseMethods( )

def scheduleInformation ( ):
    scheduleList = DBMethods.getScheduleList( )
    weekList = [ 'Понедельник: ', 'Вторник: ', 'Среда: ', 'Четверг: ', 'Пятница: ', 'Суббота: ' ]
    scheduled, schedule = [ ], [ ]
    score, out = 0, 'Рассписание 11Б\n'
    for row in scheduleList:
        scheduled.append( schedule )
        schedule = [ ]
        for col in row:
            schedule.append( col )
    del scheduled[ 0 ]
    for dayAWeek in weekList:
        out += '\n' + str( dayAWeek ) + '\n'
        numOfLesson = 0
        for day in scheduled:
            numOfLesson += 1
            if day[ score ] == None:
                pass
            else:
                out += str( numOfLesson ) + '. ' + str( day[ score ] ) + '\n'
        score += 1
    return out


def scheduleCallsInformation ( ):
    scheduleList = DBMethods.getScheduleCallsList( )
    weekList = [ 'Понедельник - пятница: ', 'Суббота: ' ]
    scheduled, schedule = [ ], [ ]
    out, score = 'Рассписание звонков МАОУ СОШ №5 г.Туапсе\n', 0
    for row in scheduleList:
        scheduled.append( schedule )
        schedule = [ ]
        for col in row:
            schedule.append( col )
    del scheduled[ 0 ]
    for dayAWeek in weekList:
        out += '\n' + str( dayAWeek ) + '\n'
        numOfLesson = 0
        for day in scheduled:
            numOfLesson += 1
            if day[ score ] == None:
                pass
            else:
                out += str( numOfLesson ) + '. ' + str( day[ score ] ) + '\n'
        score += 1
    return out


scheduleInformation = scheduleInformation( )
scheduleCallsInformation = scheduleCallsInformation( )

firstHello_1, firstHello_2 = "Ой, привет ", '! Вижу Ты тут в первые. Напиши мне "Кто ты" и я расскажу о себе)'
dev = "Функция уже в разработке, скоро станет доступна, осталось совсем чуть чуть :)"
whoMe = f"Привет🖐!\nЯ бот помощник 🤖, созданный специально для облегчения твоей жизни 😜❤\n\n✌ Бот-помощник SchoolSchedule\n✅ Версия -> {__version__}\n📑 Source code available on https://github.com/denbingon/schoolschedule\n📑 Автор -> https://vk.com/denbingon"
dontKnow = 'Не понимаю о чем Ты... Воспользуйся коммандой "помощь" и я расскажу Тебе что я умею!'

help = '''Виу, виу, виу... Нужна помощь!

Тут описаны основные команды для управления мной :)

"Кто ты" -> напиши мне эту команду и я расскажу Тебе о себе
"Расписание уроков" -> после этой команды я Тебе покажу расписание для 11Б класса МАОУ СОШ№5 г.Туапсе
"Расписание звонков" -> тоже еще одно расписание, но теперь звонков для всех классов школы
"Начать" -> выполняя эту команду я запоминаю как тебя зовут, если Ты по каким то не известным причинам изменишь имя то используй данную команду
"Что на завтра" -> тут все предельно легко, я Тебе скажу какую домашнюю работу задали на завтра и какие ожидаются мероприятия
"Что на" -> такая же как и предыдущая команда только теперь я буду ждать от тебя число на которое Ты хочешь узнать информацию
"Помощь" -> ну собственно функционал данной команды Ты наблюдаешь прямо сейчас

Ну что ж... Вот и все, краткий гайд по мне подошел к концу, надеюсь я смог разъяснить твою проблему, если же нет то обращайся к https://vk.com/denbingon/, он то Тебе точно поможет!
Приятного пользования мной! Хорошего дня!
'''
