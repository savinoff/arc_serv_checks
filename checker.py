



from classes.arcserv import ArcServ
from testsets.arcserv_ts_1 import testset

def checker(arc):
    print(arc)

    print(testset)

    testset.start_tests(arc)

    print(testset)

#TODO прикрутить вывод в jinja2 html
#TODO добавить проверку изменний и тех. долга

if __name__ == '__main__':
    #Создадим архитектуру для проверки
    arc = ArcServ()
    arc.arcitect = 'Кукукин Петр Иваааныч'
    arc.code = 'Вот такая вот архитектура'
    arc.description = 'Длинное описание архитектуры, про что она. Короче, такой дескриптион'
    arc.period = 'Q3_2021_'

    checker(arc)