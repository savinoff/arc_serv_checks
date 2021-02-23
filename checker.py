



from classes.arcserv import ArcServ
from testsets.arcserv_ts_1 import testset

from jinja2 import Environment, FileSystemLoader

def checker(arc):
    print(arc)

    print(testset)

    testset.start_tests(arc)

    print(testset)

#TODO прикрутить вывод в jinja2 html
#TODO добавить проверку изменний и тех. долга

    template_dir = 'templates'
    env = Environment(loader=FileSystemLoader(template_dir),
                      trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('check_arc_serv_tmpl.html')
    with open('res.html', 'w') as res:
        res.write(template.render(check_list = testset))

if __name__ == '__main__':
    #Создадим архитектуру для проверки
    arc = ArcServ()
    arc.arcitect = 'Кукукин Петр Иваааныч'
    arc.code = 'Вот такая вот архитектура'
    arc.description = 'Длинное описание архитектуры, про что она. Короче, такой дескриптион'
    arc.period = 'Q3_2021_'

    checker(arc)