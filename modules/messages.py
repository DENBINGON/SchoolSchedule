from modules.const import __version__
from modules.db import dataBaseMethods

DBMethods = dataBaseMethods( )


def scheduleInformation ( ):
    scheduleList = DBMethods.getScheduleList( )
    weekList = [ 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье' ]
    scheduled, schedule = [ ], [ ]
    for row in scheduleList:
        scheduled.append( schedule )
        schedule = [ ]
        for col in row:
            schedule.append( col )
    del scheduled[ 0 ]
    score = 0
    out = 'Рассписание 11Б\n'
    for dayAWeek in weekList:
        out += '\n' + str( dayAWeek ) + '\n'
        numOfLesson = 0
        for day in scheduled:
            numOfLesson += 1
            out += str( numOfLesson ) + '. ' + str( day[ score ] ) + '\n'
        score += 1

    return out


firstHello_1, firstHello_2 = "Ой, привет ", "! Вижу ты тут в первые."
dev = "Функция уже в разработке, скоро станет доступна, осталось совсем чуть чуть :)"
whoMe = f"Привет🖐!\nЯ бот помощник 🤖, созданный специально для облегчения твоей жизни 😜❤\n\n✌ Бот-помощник SchoolSchedule\n✅ Версия -> {__version__}\n📑 Source code available on https://github.com/denbingon/schoolschedule\n📑 Автор -> https://vk.com/denbingon"
dontKnow = 'Не понимаю о чем ты... Воспользуйся коммандой "помощь" и я расскажу тебе что я умею!'
