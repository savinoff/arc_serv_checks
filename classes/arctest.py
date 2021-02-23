

from classes.testresult import TestResult
from classes.arcserv import ArcServ


class ArcTestList(list):
    """
    Список тестов
    """

    def __init__(self, code: str, name: str):
        self.code : str = code
        self.name : str = name
        self.arcserv: ArcServ

    def append(self, object):
        if object.__class__.__name__ == 'ArcTest':
            super().append(object)
        else:
            raise Exception('Append is only for ArcTest objects')

    def extend(self, object):
        raise Exception('Extend is forbidden for ArcTestList')

    def __str__(self):
        str_res = "\t"
        for x in self:
            str_res = str_res + str(x) + '\n\t'
            # print(type(x))
        return f"{self.__class__.__name__}: {self.code} ({len(self)})  \n{str_res[:-1]}"

    def start_tests(self, arcserv: ArcServ):
        self.arcserv = arcserv
        for test in self:
            test.arcserv = self.arcserv
            test.start_test()


class ArcTest():
    """
    Описание класса теста
    code - код класса
    name - наименование
    description - описание
    result - результат проверки
    arcserv - объект архитектуры сервиса
    start_test() - функция проверки
    """

    def __init__(self, code: str, name: str = '', description: str = ''):
        self.code : str = code
        self.name : str = name
        self.description : str =description
        self.result : TestResult = TestResult()
        self.arcserv: ArcServ
        self.test_function: object


    def start_test(self):
       """
       Клас запуска теста, для переопределения, проставляет результат выполнения теста
       :return:
       """
       self.result = self.test_function(self.arcserv)

    def __str__(self):
        return  f'{self.__class__.__name__}: {self.code}; {self.result}'


if __name__ == '__main__':
    arctest = ArcTest()
    arctest.name = 'Тестовый тест'
    print(arctest)

    atl = ArcTestList()
    atl.code = 'ТН1'
    atl.name = 'Тестовый набор тестов'
    atl.append(arctest)
    arctest.name = 'Тестовый тест2'
    arctest.code = 'Т2'
    atl.append(arctest)
    print(atl)

    # atl.append(1)
    atl.extend(2)


